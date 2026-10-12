---
name: redactare
description: >
  Redactează acte juridice românești pe baza textului legii în vigoare din
  serverul Romanian Law MCP: contestație la ANAF, plângere contravențională,
  notificare și punere în întârziere, somație de plată, cerere de chemare în
  judecată, întâmpinare, convocare la cercetare disciplinară, decizie de
  sancționare sau de concediere, act adițional, hotărâre AGA, răspuns către o
  autoritate. Verifică ce mențiuni obligatorii cere legea, le pune în act și
  spune termenul și locul de depunere. Folosește-l când cineva cere „scrie-mi”,
  „redactează”, „fă-mi un model de”, „cum arată o contestație”, sau după o
  analiză când utilizatorul vrea actul propriu-zis.
argument-hint: "[ce act, pentru cine, faptele esențiale]"
---

# Redactarea unui act juridic

Citește mai întâi `../../references/reguli-comune.md`, relativ la directorul acestui skill. Pentru structura actelor uzuale deschide `references/structuri.md` din acest skill.

Un act juridic e respins sau anulat cel mai des pentru o mențiune obligatorie lipsă sau pentru un termen depășit, nu pentru stil. De aceea, înainte de redactare, afli din lege ce trebuie să conțină actul. La final verifici, mențiune cu mențiune, că apar toate.

## Pasul 1. Stabilește actul

- **Ce act e** și cine îl semnează: utilizatorul, firma lui, avocatul.
- **Către cine**: autoritate, instanță, angajat, partener contractual.
- **Ce urmărește**: anularea unui act, plata unei sume, o sancțiune, o modificare de contract.
- **Termenul** în care trebuie depus sau comunicat. Dacă există unul, îl calculezi cu scriptul din skill-ul `termene` și îl spui la început.

Dacă din conversație reiese deja o analiză (de exemplu o decizie ANAF verificată cu `analiza-document`), folosește-o. Nu reface analiza.

## Pasul 2. Află din lege conținutul obligatoriu

1. Găsește articolul care spune ce trebuie să cuprindă actul. `references/structuri.md` arată unde să cauți pentru actele uzuale. Pentru celelalte, caută cu `search_legislation` termeni ca „va cuprinde”, „sub sancțiunea nulității”, „cuprinsul”.
2. Citește-l cu `get_provision` și fă o listă cu fiecare mențiune cerută și sancțiunea lipsei ei.
3. Rulează `check_currency` pe act.
4. Caută și regulile de formă: număr de exemplare, semnătură, ștampilă, comunicare prin scrisoare recomandată, taxă de timbru, anexe.

## Pasul 3. Strânge faptele

Ai nevoie de fapte reale: nume, date, numere de acte, sume, ce s-a întâmplat. Nu le inventa.

- Dacă lipsește un fapt fără de care actul nu stă în picioare (de exemplu motivul contestației), întreabă. Cel mult 2-3 întrebări odată.
- Pentru restul, lasă în text un marcaj vizibil: `[de completat: numărul deciziei]`. Utilizatorul trebuie să-l găsească ușor.
- Motivele de drept se construiesc din articole primite de la server. Un argument fără temei verificat se scoate sau se marchează în nota de după act.

## Pasul 4. Redactează

- Limbaj juridic românesc obișnuit, clar, fără formule pompoase. Paragrafe numerotate acolo unde e uzual (motivele de fapt, motivele de drept, probele).
- Temeiurile de drept apar în text în forma obișnuită: „art. 270 alin. (1) din Legea nr. 207/2015 privind Codul de procedură fiscală”.
- **Actul trebuie să fie curat.** Nu pune în corpul actului etichete ca `[MCP]` sau `[de verificat]` și nici comentarii pentru utilizator. Ele merg în nota de după act. În act rămân doar marcajele `[de completat: ...]`.
- Nu adăuga antetul `CONFIDENȚIAL` pe un act care pleacă la o autoritate sau la cealaltă parte.

## Pasul 5. Predă actul

```markdown
**Termen:** [ultima zi de depunere/comunicare, calculată cu scriptul, și temeiul]. Dacă nu există termen, omite rândul.

---
[ACTUL, gata de completat și semnat]
---

**Mențiuni obligatorii verificate:**
| Mențiunea cerută de lege | Unde apare în act | Temei |
|---|---|---|
| ... | pct. 1 / antet / [de completat] | art. ... din ... [MCP] |

**De completat de tine:** [lista marcajelor din act]
**Cum se depune:** [unde, cum, câte exemplare, taxă, anexe]
**Verificare:** [sursele temeiurilor, vigoarea, ce argumente sunt [de analizat] sau [de verificat]]
```

Dacă utilizatorul vrea actul ca fișier, salvează-l ca .docx (sau .md dacă nu ai cum să faci .docx), cu marcajele `[de completat: ...]` păstrate.

## Limite

- Skill-ul nu depune și nu trimite nimic. Utilizatorul semnează și depune.
- Pentru acte cu miză mare (acțiuni în instanță, concedieri, contestații cu sume mari), spune în nota finală că actul trebuie revăzut de un avocat sau consultant înainte de depunere, mai ales dacă utilizatorul nu e jurist.
- Nu inventa jurisprudență și nu cita decizii care nu apar în textul primit de la server.
