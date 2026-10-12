#!/usr/bin/env python3
"""Calculează data la care se împlinește un termen legal românesc.

Scriptul face doar aritmetica. Regula de calcul (zile libere, zile calendaristice,
zile lucrătoare, luni, ani) o alege cel care îl rulează, după textul legii.

Moduri:
  libere          nu se socotește nici ziua de început, nici ziua în care termenul
                  se împlinește (art. 181 alin. (1) pct. 2 CPC, art. 2553 alin. (1) C.civ.)
  calendaristice  termenul curge din ziua următoare și se împlinește în ultima lui zi
                  (de ex. preavizul din Codul muncii, RIL nr. 8/2024)
  lucratoare      se numără doar zilele lucrătoare de după ziua de început
  saptamani|luni|ani
                  se împlinește în ziua corespunzătoare; dacă luna nu are acea zi,
                  în ultima zi a lunii (art. 181 alin. (1) pct. 3 CPC, art. 2552 C.civ.)

Prorogarea (art. 181 alin. (2) CPC, art. 2554 C.civ.): dacă ultima zi e nelucrătoare,
termenul se mută în prima zi lucrătoare. Implicit e activă pentru libere și pentru
săptămâni/luni/ani, inactivă pentru calendaristice. Se schimbă cu --prorogare / --fara-prorogare.

Exemple:
  termen.py --start 2026-11-03 --n 45 --mod libere
  termen.py --start 2026-10-12 --n 20 --mod lucratoare
  termen.py --start 2026-01-31 --n 1 --mod luni --json
"""
from __future__ import annotations

import argparse
import calendar
import json
import sys
from datetime import date, timedelta

ZILE = ["luni", "marți", "miercuri", "joi", "vineri", "sâmbătă", "duminică"]


def paste_ortodox(an: int) -> date:
    """Paștele ortodox (calculul iulian plus diferența de 13 zile, valabil 1900-2099)."""
    a, b, c = an % 4, an % 7, an % 19
    d = (19 * c + 15) % 30
    e = (2 * a + 4 * b - d + 34) % 7
    luna = (d + e + 114) // 31
    zi = (d + e + 114) % 31 + 1
    return date(an, luna, zi) + timedelta(days=13)


def sarbatori_legale(an: int) -> dict[date, str]:
    """Zilele de sărbătoare legală nelucrătoare din art. 139 alin. (1) din Codul muncii.

    Nu include cele două zile acordate doar membrilor altor culte religioase.
    """
    p = paste_ortodox(an)
    zile = {
        date(an, 1, 1): "Anul Nou",
        date(an, 1, 2): "Anul Nou (a doua zi)",
        p - timedelta(days=2): "Vinerea Mare",
        p: "Paștele",
        p + timedelta(days=1): "a doua zi de Paști",
        date(an, 5, 1): "1 Mai",
        p + timedelta(days=49): "Rusaliile",
        p + timedelta(days=50): "a doua zi de Rusalii",
        date(an, 8, 15): "Adormirea Maicii Domnului",
        date(an, 12, 1): "Ziua Națională",
        date(an, 12, 25): "Crăciunul",
        date(an, 12, 26): "a doua zi de Crăciun",
    }
    if an >= 2012:
        zile[date(an, 11, 30)] = "Sfântul Andrei"
    if an >= 2017:
        zile[date(an, 1, 24)] = "Ziua Unirii Principatelor"
        zile[date(an, 6, 1)] = "Ziua Copilului"
    if an < 2018:
        zile.pop(p - timedelta(days=2))
    if an >= 2024:
        zile[date(an, 1, 6)] = "Boboteaza"
        zile[date(an, 1, 7)] = "Sfântul Ioan Botezătorul"
    return zile


class Calendar:
    def __init__(self, extra: list[date]):
        self.extra = set(extra)
        self._cache: dict[int, dict[date, str]] = {}

    def motiv_nelucratoare(self, z: date) -> str | None:
        if z in self.extra:
            return "zi nelucrătoare adăugată manual"
        sarb = self._cache.setdefault(z.year, sarbatori_legale(z.year)).get(z)
        if sarb:
            return f"sărbătoare legală: {sarb}"
        if z.weekday() >= 5:
            return ZILE[z.weekday()]
        return None

    def lucratoare(self, z: date) -> bool:
        return self.motiv_nelucratoare(z) is None


def adauga_luni(z: date, luni: int) -> date:
    total = z.month - 1 + luni
    an, luna = z.year + total // 12, total % 12 + 1
    return date(an, luna, min(z.day, calendar.monthrange(an, luna)[1]))


def calculeaza(start: date, n: int, mod: str, prorogare: bool | None, cal: Calendar) -> dict:
    pasi: list[str] = []
    if mod == "libere":
        sfarsit = start + timedelta(days=n + 1)
        pasi.append(f"ziua de început ({start}) nu se socotește; se numără {n} zile întregi, "
                    f"de la {start + timedelta(days=1)} la {start + timedelta(days=n)}")
        pasi.append(f"nici ziua împlinirii nu se socotește, deci actul se poate face până pe {sfarsit} inclusiv")
        implicit = True
    elif mod == "calendaristice":
        sfarsit = start + timedelta(days=n)
        pasi.append(f"termenul curge din {start + timedelta(days=1)} și se împlinește în a {n}-a zi, {sfarsit}")
        implicit = False
    elif mod == "lucratoare":
        z, numarate = start, 0
        while numarate < n:
            z += timedelta(days=1)
            if cal.lucratoare(z):
                numarate += 1
        sfarsit = z
        pasi.append(f"se numără {n} zile lucrătoare după {start}; a {n}-a este {sfarsit}")
        implicit = False
    elif mod in ("saptamani", "luni", "ani"):
        if mod == "saptamani":
            sfarsit = start + timedelta(weeks=n)
        else:
            sfarsit = adauga_luni(start, n * (12 if mod == "ani" else 1))
        pasi.append(f"se împlinește în ziua corespunzătoare: {sfarsit}"
                    + (" (luna nu are zi corespunzătoare, deci ultima zi a lunii)"
                       if mod != "saptamani" and sfarsit.day != start.day else ""))
        implicit = True
    else:
        raise ValueError(mod)

    aplica = implicit if prorogare is None else prorogare
    initial = sfarsit
    prorogat_de: list[str] = []
    if aplica:
        while not cal.lucratoare(sfarsit):
            prorogat_de.append(f"{sfarsit} ({cal.motiv_nelucratoare(sfarsit)})")
            sfarsit += timedelta(days=1)
        if prorogat_de:
            pasi.append("ultima zi cade într-o zi nelucrătoare: " + ", ".join(prorogat_de)
                        + f"; termenul se prelungește până pe {sfarsit}")
    elif not cal.lucratoare(sfarsit):
        pasi.append(f"atenție: ultima zi ({sfarsit}) este nelucrătoare "
                    f"({cal.motiv_nelucratoare(sfarsit)}), iar prorogarea nu a fost aplicată")

    nelucratoare = []
    z = start + timedelta(days=1)
    while z <= sfarsit:
        motiv = cal.motiv_nelucratoare(z)
        if motiv and not motiv.startswith(("sâmbătă", "duminică")):
            nelucratoare.append(f"{z} ({motiv})")
        z += timedelta(days=1)

    return {
        "start": start.isoformat(),
        "n": n,
        "mod": mod,
        "prorogare_aplicata": aplica,
        "ultima_zi_inainte_de_prorogare": initial.isoformat(),
        "ultima_zi": sfarsit.isoformat(),
        "ziua_saptamanii": ZILE[sfarsit.weekday()],
        "pasi": pasi,
        "sarbatori_in_interval": nelucratoare,
    }


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--start", help="data de la care curge termenul, AAAA-LL-ZZ")
    ap.add_argument("--n", type=int, help="durata termenului")
    ap.add_argument("--mod", choices=["libere", "calendaristice", "lucratoare", "saptamani", "luni", "ani"])
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--prorogare", dest="prorogare", action="store_true", default=None)
    g.add_argument("--fara-prorogare", dest="prorogare", action="store_false")
    ap.add_argument("--nelucratoare", action="append", default=[],
                    help="zi nelucrătoare suplimentară, AAAA-LL-ZZ (se poate repeta)")
    ap.add_argument("--sarbatori", type=int, metavar="AN", help="doar listează sărbătorile legale din anul dat")
    ap.add_argument("--zi", metavar="AAAA-LL-ZZ",
                    help="doar spune dacă ziua e lucrătoare și, dacă nu e, care e prima zi lucrătoare de după ea")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)

    if a.sarbatori:
        for z, nume in sorted(sarbatori_legale(a.sarbatori).items()):
            print(f"{z} {ZILE[z.weekday()]:9} {nume}")
        return 0
    if a.zi:
        cal = Calendar([date.fromisoformat(x) for x in a.nelucratoare])
        z = date.fromisoformat(a.zi)
        motiv = cal.motiv_nelucratoare(z)
        if motiv is None:
            print(f"{z} ({ZILE[z.weekday()]}) este zi lucrătoare")
        else:
            urm = z
            while not cal.lucratoare(urm):
                urm += timedelta(days=1)
            print(f"{z} este nelucrătoare ({motiv}); prima zi lucrătoare: {urm} ({ZILE[urm.weekday()]})")
        return 0
    if a.start is None or a.n is None or a.mod is None:
        ap.error("--start, --n și --mod sunt obligatorii")

    cal = Calendar([date.fromisoformat(x) for x in a.nelucratoare])
    r = calculeaza(date.fromisoformat(a.start), a.n, a.mod, a.prorogare, cal)
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        print(f"Ultima zi: {r['ultima_zi']} ({r['ziua_saptamanii']})")
        for p in r["pasi"]:
            print(f"- {p}")
        if r["sarbatori_in_interval"]:
            print("Sărbători legale în interval: " + ", ".join(r["sarbatori_in_interval"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
