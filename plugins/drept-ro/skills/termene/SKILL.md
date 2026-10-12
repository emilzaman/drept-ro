---
name: termene
description: >
  Calculează data exactă la care expiră un termen legal din România: contestație
  la ANAF, plângere contravențională, apel, recurs, preaviz, decizie
  disciplinară, notificări, prescripție. Ia textul care stabilește termenul din
  serverul Romanian Law MCP, alege regula de calcul (zile libere, calendaristice,
  lucrătoare, luni, ani), ține cont de sărbătorile legale și de prorogarea în
  prima zi lucrătoare, și arată calculul pas cu pas. Folosește-l ori de câte ori
  cineva întreabă „până când pot...”, „în câte zile...”, „mai sunt în termen?”,
  „când expiră...”, sau a primit un act și trebuie să răspundă la timp.
argument-hint: "[ce act, când a fost primit / când a început termenul]"
---

# Calculul termenelor

Citește mai întâi `../../references/reguli-comune.md`, relativ la directorul acestui skill.

Un termen ratat de multe ori nu se mai poate recupera, pentru că legea leagă de el decăderea. Calculul trebuie să fie corect și ușor de verificat. Textul legii decide regula. Scriptul `scripts/termen.py` face aritmetica, ca să nu numeri zilele în minte.

## Pasul 1. Află termenul din lege

1. Identifică actul la care se răspunde sau acțiunea de făcut (contestație, plângere, apel, preaviz, decizie de sancționare).
2. Găsește articolul care stabilește termenul și citește-l întreg cu `get_provision`. Reține:
   - durata și unitatea (zile, zile calendaristice, zile lucrătoare, luni, ani);
   - momentul de la care curge (comunicarea, înmânarea, luarea la cunoștință, săvârșirea faptei, data actului);
   - sancțiunea depășirii (decădere, nulitate, prescripție);
   - unde și cum se depune.
3. Rulează `check_currency` pe act.

Dacă utilizatorul spune un termen („am 30 de zile”), verifică-l cu textul înainte de calcul.

## Pasul 2. Alege regula de calcul

Ordinea e: legea specială, apoi regula generală.

1. **Regula din legea specială**, dacă există. Exemplu: notele din Codul muncii despre RIL nr. 8/2024 spun că preavizul curge din ziua următoare comunicării și se împlinește în ultima zi a termenului. Regulile din Codul de procedură civilă și Codul civil nu se aplică aici. Citește notele ÎCCJ și CCR din textul articolului.
2. **Termene procedurale** (instanță, executare, proceduri fiscale): art. 181-183 din Codul de procedură civilă. Pentru procedura fiscală, art. 75 din Codul de procedură fiscală trimite tot la Codul de procedură civilă. Pe zile, nu se socotesc nici prima, nici ultima zi (modul `libere`). Dacă ultima zi e nelucrătoare, termenul se prelungește la prima zi lucrătoare.
3. **Termene de drept substanțial** (contracte, prescripție, obligații civile): art. 2551-2556 din Codul civil. Pe zile, nu se iau în calcul prima și ultima zi (art. 2553). Prorogarea în prima zi lucrătoare e la art. 2554.
4. **Termene exprimate „în zile calendaristice”** în legi speciale (de exemplu decizia de sancționare din Codul muncii): verifică dacă textul sau o decizie ÎCCJ spune cum se numără. Dacă nu spune, arată ambele calcule (modul `calendaristice` și modul `libere`) și recomandă data mai timpurie.

Ia textul acestor articole cu `get_provision` și citează-l. Nu te baza pe rezumatul de mai sus: el arată unde să cauți, dar textul primit decide.

## Pasul 3. Calculează cu scriptul

```bash
python3 <director-skill>/scripts/termen.py --start AAAA-LL-ZZ --n <număr> --mod <mod>
```

- `--start` e ziua evenimentului de la care curge termenul (ziua comunicării, nu ziua următoare). Scriptul exclude singur ziua de început.
- `--mod`: `libere`, `calendaristice`, `lucratoare`, `saptamani`, `luni`, `ani`.
- Prorogarea e implicită la `libere`, `saptamani`, `luni`, `ani` și oprită la `calendaristice`. O schimbi cu `--prorogare` sau `--fara-prorogare`, după regula din Pasul 2.
- `--nelucratoare AAAA-LL-ZZ` adaugă o zi liberă stabilită prin hotărâre de guvern. Aceste zile sunt de obicei pentru sectorul public, iar efectul lor asupra termenelor e discutabil, așa că marchează-le `[de analizat]`.
- `--sarbatori AN` listează sărbătorile legale din art. 139 din Codul muncii pentru anul dat.
- `--json` dă rezultatul structurat.

Dacă nu poți rula scripte, fă calculul manual și arată fiecare pas.

## Pasul 4. Răspunsul

```markdown
**Termenul expiră:** [ziua săptămânii, ZZ.LL.AAAA][, la ora închiderii registraturii, dacă actul se depune fizic]

**Temeiul:** [art. ... din ...]: „[textul care stabilește termenul]” [MCP]
**Regula de calcul:** [art. ... / decizia ...] [MCP], [de ce se aplică]
**Calculul:**
- termenul curge de la [eveniment, data]
- [pașii din script]
- [prorogare, dacă a fost cazul]

**Riscuri:** [data comunicării nesigură, comunicare prin SPV / poștă / afișare, depunere prin poștă sau curier, termen ratat]
**Verificare:** ...
```

Lucruri care schimbă data și pe care le semnalezi când apar:

- **Data comunicării.** Comunicarea electronică (SPV, e-mail), prin poștă cu confirmare, prin afișare sau prin publicitate au reguli proprii. Întreabă cum a fost comunicat actul dacă nu e clar. Pentru actele fiscale caută regula comunicării în Codul de procedură fiscală.
- **Depunerea prin poștă, curier, fax sau e-mail.** Actul trimis înăuntrul termenului pe aceste căi se socotește făcut în termen (art. 183 din Codul de procedură civilă; pentru actele de drept civil, art. 2556 din Codul civil). Depunerea direct la registratură se termină la ora de închidere (art. 182 alin. (2) din Codul de procedură civilă). Citește articolele înainte să te bazezi pe ele.
- **Termene de decădere vs. prescripție.** Prescripția se poate suspenda sau întrerupe, decăderea de regulă nu. Spune care e.
- **Termene la limită.** Dacă mai sunt sub 3 zile lucrătoare, spune asta la început și recomandă depunerea imediată.

Data calculată e ultima zi în care legea mai permite actul. Recomandă depunerea cu câteva zile înainte.
