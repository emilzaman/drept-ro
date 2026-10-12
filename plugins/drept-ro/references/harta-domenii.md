# Harta domeniilor: ce acte să cauți

Punct de plecare pentru a alege actele potrivite. Lista nu e completă. Dacă întrebarea nu se potrivește aici, folosește `build_legal_stance` sau `search_legislation` fără filtru. Identificatorii din coloana a doua merg direct în parametrul `document_id`. Rulează totuși `check_currency` înainte să citezi.

## Acte pe domenii

| Domeniu | Acte (`document_id`) | Ce reglementează |
|---|---|---|
| Fiscal | `Codul fiscal` (Legea 227/2015), `HG 1/2016` (Normele metodologice) | impozite, TVA, contribuții, microîntreprinderi, PFA |
| Procedură fiscală | `Codul de procedură fiscală` (Legea 207/2015) | inspecție, decizii de impunere, contestații, executare silită, termene fiscale |
| Facturare și raportare | `OUG 120/2021` (RO e-Factura și sistemul național), `Legea 82/1991` (contabilitatea) | e-Factura, evidență contabilă |
| Evaziune | `Legea 241/2005` | infracțiuni fiscale |
| Muncă | `Codul muncii` (Legea 53/2003), `Legea 62/2011` (dialogul social), `Legea 81/2018` (telemunca), `HG 905/2017` (REVISAL) | contract de muncă, concediere, disciplină, timp de lucru, concedii |
| Sănătate și securitate în muncă | `Legea 319/2006` | obligațiile angajatorului, accidente de muncă |
| Concedii medicale | `OUG 158/2005` | indemnizații de asigurări sociale de sănătate |
| Civil și contracte | `Codul civil` (Legea 287/2009), `Legea 71/2011` (punerea în aplicare) | obligații, contracte, răspundere, proprietate, familie, succesiuni, prescripție, termene |
| Dobânzi și întârzieri la plată | `OG 13/2011` (dobânda legală), `Legea 72/2013` (întârzieri între profesioniști) | dobânzi, penalități |
| Procedură civilă | `Codul de procedură civilă` (Legea 134/2010) | competență, termene procedurale, căi de atac, executare silită |
| Societăți | `Legea 31/1990`, `Legea 265/2022` (registrul comerțului) | SRL, SA, AGA, administratori, cesiune de părți sociale, înregistrări ONRC |
| PFA, II, IF | `OUG 44/2008` | activități economice ale persoanelor fizice |
| Insolvență | `Legea 85/2014` | insolvență, concordat, răspunderea administratorilor |
| Spălarea banilor | `Legea 129/2019` | beneficiar real, obligații KYC |
| Concurență | `Legea 21/1996` | înțelegeri, abuz de poziție dominantă |
| Consumatori | `OG 21/1992`, `OUG 34/2014` (contracte la distanță), `Legea 193/2000` (clauze abuzive), `Legea 363/2007` (practici incorecte) | drepturile consumatorilor, retragere, garanții |
| Date personale și securitate cibernetică | `law-doc-201834` (GDPR, Regulamentul (UE) 2016/679, text integral), `Legea 190/2018` (aplicarea GDPR), `Legea 506/2004` (comunicații electronice), `OUG 155/2024` (NIS2) | protecția datelor, incidente, DNSC |
| Penal | `Codul penal` (Legea 286/2009), `Codul de procedură penală` (Legea 135/2010) | infracțiuni, pedepse, plângeri, prescripție |
| Contravenții | `OG 2/2001` | proces-verbal, amenzi, plângere contravențională |
| Administrativ | `OUG 57/2019` (Codul administrativ), `Legea 554/2004` (contenciosul administrativ) | autorități publice, funcționari, acte administrative, acțiuni în contencios |
| Achiziții publice | `Legea 98/2016`, `Legea 101/2016` (remedii) | proceduri de atribuire, contestații CNSC |
| Imobiliar și construcții | `Legea 7/1996` (cadastru), `Legea 50/1991` (autorizații de construire), `Legea 196/2018` (asociații de proprietari), `Legea 17/2014` (terenuri agricole) | carte funciară, autorizații, bloc, vânzarea terenurilor agricole |
| Rutier | `OUG 195/2002` (Codul rutier) | circulație, permis, amenzi rutiere |
| Profesii juridice | `Legea 51/1995` (avocații), `Legea 36/1995` (notarii) | organizarea profesiilor |

## Din limbaj curent în termeni legali

Corpusul e în română juridică. O căutare cu termenii obișnuiți ratează textul. Traduce înainte:

| Utilizatorul spune | Caută |
|---|---|
| firmă, SRL mic | „microîntreprindere”, „impozit pe profit”, „societate cu răspundere limitată” |
| PFA, freelancer | „venituri din activități independente”, „persoană fizică autorizată” |
| salariu, leafă | „venituri din salarii”, „salariul de bază” |
| angajat, contract de muncă | „contractul individual de muncă”, „salariat” |
| dat afară | „concediere”, „încetarea contractului individual de muncă” |
| demisie | „demisie”, „preaviz” |
| concediu | „concediu de odihnă”, „concediu medical”, „concediu pentru creșterea copilului” |
| amendă | „contravenție”, „amendă contravențională”, „proces-verbal de constatare” |
| a contesta la ANAF | „contestație”, „act administrativ fiscal”, „decizie de impunere” |
| a da în judecată | „cerere de chemare în judecată”, „competența” |
| datorie neplătită | „obligație de plată”, „dobânda legală penalizatoare”, „somație” |
| chirie | „contractul de locațiune” |
| moștenire | „succesiune”, „moștenitori legali”, „rezervă succesorală” |
| crypto | „monedă virtuală” |
| scurgere de date | „încălcarea securității datelor cu caracter personal”, „incident” |

## Sfaturi de căutare

- Un singur concept pe interogare. „impozit pe profit” și „TVA” se caută separat.
- Când știi actul, folosește filtrul `document_id` și nu pune numele actului în textul căutării. Numele codului nu apare în textul articolelor și strică rezultatele.
- Diacriticele sunt opționale. „microintreprindere” găsește „microîntreprindere”.
- Pentru o expresie exactă folosește ghilimele: `"zile calendaristice"`. Pentru variante de cuvânt folosește `*`: `concedi*`.
- Când știi articolul, nu căuta. Cere-l direct cu `get_provision`.
