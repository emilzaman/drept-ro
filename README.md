# drept-ro

Plugin pentru Claude Code și Claude Cowork care răspunde la întrebări despre legislația României cu textul oficial în vigoare. Textele vin din serverul Romanian Law MCP, care preia actele normative de pe legislatie.just.ro.

Fiecare răspuns citează articolul exact și spune de unde vine fiecare afirmație. Textul primit de la server e marcat `[MCP]`, iar ce vine din memorie e marcat `[de verificat]`.

## Ce conține

| Comandă | Ce face |
|---|---|
| `/drept-ro:cercetare` | Răspunde la o întrebare juridică. Găsește actele aplicabile, inclusiv legea specială și normele de aplicare, citează articolele și verifică dacă sunt în vigoare. |
| `/drept-ro:analiza-document` | Verifică un document față de lege: decizie ANAF, proces-verbal de contravenție, contract, decizie de sancționare. Arată problemele, gravitatea lor și termenul de contestare. |
| `/drept-ro:termene` | Calculează data la care expiră un termen legal, cu sărbătorile legale și prorogarea în prima zi lucrătoare. |
| `/drept-ro:verificare-citari` | Verifică toate trimiterile la lege dintr-un text: dacă articolul există, dacă spune ce susține textul, dacă e în vigoare sau a fost renumerotat. |
| `/drept-ro:redactare` | Redactează actul propriu-zis (contestație, plângere, notificare, somație, cerere de chemare în judecată, decizie de sancționare, act adițional) cu mențiunile obligatorii cerute de lege și cu termenul de depunere. |

Comenzile nu sunt obligatorii. O întrebare obișnuită despre legea română pornește singură skill-ul potrivit.

## Instalare în Claude Code

```
/plugin marketplace add <calea-către-acest-folder sau owner/repo de pe GitHub>
/plugin install drept-ro@drept-ro
```

Repornește Claude Code. La prima folosire, rulează `/mcp` și autentifică serverul `romanian-law`.

Instalează pluginul pentru utilizator (user scope), nu pentru proiect. Altfel nu poate citi documentele din afara folderului proiectului.

## Profil opțional

Dacă scrii în `~/.claude/plugins/config/drept-ro/profil.md` rolul tău și datele firmei (formă de organizare, regim fiscal, TVA, număr de salariați, CAEN), răspunsurile țin cont de ele. Fișierul nu e obligatoriu. Pluginul îți oferă să-l creeze când spui astfel de lucruri în conversație.

## Limite

- Serverul conține legislația națională de pe legislatie.just.ro, în forma consolidată curentă. Unele acte UE sunt incluse (de exemplu GDPR). Pot lipsi ordinele unor instituții, procedurile ANAF, contractele colective, anexele unor acte, jurisprudența (în afara notelor din text) și multe acte UE.
- Pentru fapte mai vechi, versiunea legii de la data faptelor trebuie verificată separat.
- Răspunsurile sunt documentare juridică, nu consultanță. Pentru decizii cu miză (concedieri, contestații, contracte importante), verifică cu un avocat sau consultant fiscal.

## Structură

```
.claude-plugin/marketplace.json
plugins/drept-ro/
  .claude-plugin/plugin.json
  .mcp.json                      serverul Romanian Law MCP
  references/reguli-comune.md    regulile citite de toate skill-urile
  references/harta-domenii.md    actele pe domenii și termenii de căutare
  skills/<nume>/SKILL.md
  skills/termene/scripts/termen.py
  skills/redactare/references/structuri.md
evals/evals.json                 întrebările de test
```

## Licență

Apache License 2.0. Regulile comune sunt adaptate după [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal). Vezi `NOTICE`.
