---
name: cercetare
description: >
  Răspunde la orice întrebare despre legislația din România pe baza textului
  oficial și în vigoare al legilor, luat din serverul Romanian Law MCP: ce spune
  legea, ce obligații ai, ce termen sau ce sancțiune se aplică, dacă ai voie să
  faci ceva. Leagă mai multe acte între ele (cod, lege specială, norme de
  aplicare) și citează articolele exacte. Folosește acest skill de fiecare dată
  când cineva întreabă despre dreptul românesc, chiar dacă nu spune „lege” sau
  „articol”: impozite și ANAF, firme și PFA, salariați și concedieri, contracte,
  chirii, moșteniri, amenzi, GDPR, procese, termene, penal. Folosește-l și pentru
  întrebări în engleză despre legea română.
argument-hint: "[întrebarea, cu faptele relevante]"
---

# Cercetare juridică

Citește mai întâi `../../references/reguli-comune.md`, relativ la directorul acestui skill. Acolo sunt regulile despre surse, vigoare și format, iar ele se aplică tot timpul. Pentru alegerea actelor și traducerea termenilor, deschide `../../references/harta-domenii.md`.

Skill-ul scurtează drumul de la o întrebare la textul de lege aplicabil. Cititorul trebuie să poată verifica fiecare afirmație în câteva secunde, așa că fiecare regulă vine cu articolul ei și cu textul primit de la server.

## Pasul 1. Înțelege întrebarea

Stabilește, fără să scrii încă răspunsul:

- **Faptele**: cine, ce, când. Data faptelor contează pentru versiunea legii.
- **Ce vrea utilizatorul**: să afle regula, să știe dacă are voie, să afle un termen, să evite o sancțiune, să conteste ceva.
- **Problemele juridice distincte.** O speță reală are adesea 2-4 probleme, din domenii diferite. De exemplu, la un salariat care a furat date apar o problemă penală, una de dreptul muncii și una de protecția datelor. Le tratezi separat.

Dacă lipsește un fapt care schimbă răspunsul (e plătitor de TVA? are salariați? când a primit actul?), ai două variante. Pui cel mult două întrebări scurte. Sau, dacă variantele sunt puține, răspunzi pe ramuri („dacă e plătitor de TVA: ...; dacă nu: ...”). Nu cere detalii care nu schimbă răspunsul.

O întrebare care primește răspunsul dintr-un singur articol nu are nevoie de toți pașii de mai jos. Ia articolul, verifică vigoarea și răspunde scurt.

## Pasul 2. Găsește textul

Pentru fiecare problemă:

1. Alege actele din harta domeniilor. Dacă domeniul nu e clar, pornește cu `build_legal_stance` pe întrebarea reformulată în termeni juridici.
2. Caută cu `search_legislation`, câte un concept pe interogare, cu filtrul `document_id` pe actul ales.
3. Citește articolul întreg cu `get_provision`, nu doar fragmentul din căutare. Alineatele, literele și notele de modificare schimbă des sensul.
4. Urmează trimiterile: „prevăzute la art. X”, „prin derogare de la”, definițiile, normele de aplicare. `get_references` pe articol arată ce citează și cine îl citează.
5. Rulează `check_currency` pe fiecare act pe care îl vei cita. Uită-te la notele de modificare și compară-le cu data faptelor.

Te oprești când fiecare problemă are regula, excepțiile ei și, dacă e cazul, termenul și sancțiunea. Nu te opri la primul articol care pare să răspundă. Excepțiile stau de obicei în alineatele următoare sau într-o lege specială.

## Pasul 3. Scrie răspunsul

Folosește structura de mai jos pentru o speță cu mai multe probleme. La o întrebare simplă păstrează doar **Pe scurt**, citarea și rândul de verificare.

```markdown
**Pe scurt:** [răspunsul în 1-3 propoziții, cu articolele principale]

### 1. [Prima problemă, formulată ca întrebare]
[Regula, cu citat scurt din lege și articolul exact, marcat [MCP].]
[Aplicarea la fapte. Condiții și excepții.]
[Termen / sancțiune, dacă există.]

### 2. [A doua problemă]
...

### Ce rămâne de stabilit
[Faptele care lipsesc și cum schimbă răspunsul. Judecățile marcate [de analizat].]

**Verificare:** [surse, vigoare verificată la data X, ce trebuie confirmat]

**Mai departe:** [2-4 variante concrete, de exemplu: redactez notificarea / calculez termenul exact cu /drept-ro:termene / verific contractul cu /drept-ro:analiza-document]
```

Regulile de scriere:

- Răspunsul stă în **Pe scurt**. Cine citește doar primul rând trebuie să afle ce are de făcut.
- Citează cu precizie: „art. 252 alin. (1) din Codul muncii”. Pentru regula esențială, pune textul între ghilimele, scurt (o propoziție sau două).
- Cifrele (procente, plafoane, termene, amenzi) se iau din textul primit de la server, nu din memorie. Pragurile se schimbă des prin ordonanțe.
- Dacă un act UE e relevant (GDPR, regulamente vamale), spune că textul lui nu e în corpus. Dă trimiterea cu `[de verificat]` și arată ce act românesc îl aplică (`get_eu_basis`).
- Când o regulă depinde de o apreciere (abatere „gravă”, clauză „abuzivă”, „bună-credință”), descrie criteriile din lege și marchează decizia `[de analizat]`. Nu decide în locul celui care răspunde pentru ea.

## Exemplu de răspuns scurt

Întrebare: „Cât e perioada de probă maximă pentru un post de execuție?”

> **Pe scurt:** cel mult 90 de zile calendaristice pentru funcțiile de execuție și cel mult 120 pentru funcțiile de conducere (art. 31 alin. (1) din Codul muncii) [MCP].
>
> **Verificare:** text din MCP, Codul muncii în vigoare (verificat azi).

(Exemplul arată forma. Cifrele vin întotdeauna din textul primit la momentul întrebării.)

## Ce nu face acest skill

- Nu ia decizia în locul utilizatorului. Arată regula, aplicarea și variantele.
- Nu inventează jurisprudență. Deciziile care nu apar în textul primit se menționează doar cu `[de verificat]`.
- Nu înlocuiește un avocat sau un consultant fiscal pentru acțiuni cu miză. Pentru acestea încheie cu rezumatul de dus la specialist (vezi regulile comune, punctul 9).
