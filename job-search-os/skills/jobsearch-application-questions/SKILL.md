---
name: jobsearch-application-questions
description: Answer the questions on an online job application for the Job Search AI Operating System — why do you want to work here, why this job, desired pay, how did you hear about us, work authorization, licenses, notice period, and short written questions — in your voice, from your own record and a sourced company brief. Invoke when a job seeker says "answer these application questions", "fill out this application", "why do you want to work here", "what should I put for desired salary", or pastes application-form questions. Never answers voluntary demographic or self-identification questions for you.
disable-model-invocation: false
---

> **Words rule (never break):** the lowest pay the person will accept is their **minimum pay**
> (in their pay type), in every status line, reply, file, and tracker. The comparison against
> it is the **salary check**. Never call it a "floor", even if an older profile or memory does.

> **Naming rule (never break):** the product is the **Job Search AI Operating System**.
> Use only this product name — never an older one. Never name profile or connection filenames in conversation.

Most online applications ask the same handful of questions, and a rushed "I'm
passionate about your mission" reads like every other one. These answers are short,
specific, and yours.

## Pre-flight

- **Profile:** `./job-search-os-profile.md`, then this Project's instructions, then a
  pasted block — target roles, pay type and minimum pay, target pay, share-my-minimum
  preference, location and remote, wins, what a hiring manager might question, the
  approved line on why you're looking, voice samples. (Older profiles: `Minimum
  salary:` or `Salary floor:` mean minimum pay, annual unless the value says otherwise;
  **Shipped artifacts** means wins; `Positioning challenges:` means things a hiring
  manager might question.)
- **The posting**, the **Application Board** row, and **Company brief — [Company].md**
  if it exists in this Project. No brief and the form asks "why us"? Build a short one
  first (the company-brief method: sources or nothing; if web search isn't available,
  say so and ask the person to paste their about page).
- **The questions** — pasted, a screenshot, or a link to the form.

<!-- shared:board-check:start — edit products/job-search-os/shared-instructions/board-check.md, then run scripts/job-search-os/sync-shared-instructions.py -->
## Board check — moves saved on the board (always first)

Run this before anything else in this job reads, counts, summarizes, or changes the
**Application Board**. It is not optional and it is not silent: it ends with one line
that says what you found. Never report what moved, what's stale, stage counts, or
"nothing moved" until this check has run in this conversation.

The person can move a card on the board themselves. A board built from the template
saves each move in the board artifact's storage: one document per row in its `moves`
collection, holding the row id, the new stage, and when it was saved.

1. **Find the board.** List this Project's artifacts, including ones from earlier
   conversations, and open the one named **Application Board** (never one named
   "SAMPLE — …" unless this is a sample run).
2. **Read the saved moves.** Use the tool that reads an artifact's stored data to list
   every document in the board's `moves` collection. Do this every time; don't assume
   there are none because the data block looks current or because an earlier reply
   said so.
3. **Apply each saved move whose row is still on the board.** These are the person's
   own edits: apply them without asking "apply it?". A saved move is the person's
   latest word on that row's stage.
   - Set that row's **Stage** in the board's data block to the saved stage.
   - If the date for the new stage is blank, fill it with the date the move was saved
     (Applied → Applied on, Screening → Screen on, Interviewing → Interview on,
     Onsite → Final on, Offer → Offer on, Closed → Closed on) and mark it
     `[confirm date]`.
   - A row moved to Closed with no Closed why: leave it blank and ask for the reason
     at the end of this job, as clickable choices.
4. **Save it once.** Republish the board, update the CSV backup, then delete exactly
   the saved-move documents you applied (and any for rows no longer on the board). If
   Claude asks permission to write the board or its backup, that request covers this
   step — ask in this same turn and carry on with the job; don't stop and wait for a
   separate "apply it".
5. **Say what you found, in one line, then continue:**
   - "Board check: applied 2 moves you made on the board — Northwind → Interviewing,
     Harbor → Closed."
   - "Board check: no moves saved on the board since last time."
   - If the moves were read but the board couldn't be written (permission declined or
     the file is locked): "Board check: you moved Northwind → Interviewing on the board;
     I'm using that here, and it will be saved to the board next time." Use the moved
     stages for everything in this job anyway.
   - If this board has no storage, or the stored-data tool isn't available here:
     "Board check: I can't read moves saved on the board here, so I'm using the board
     as it was last published — tell me if you moved anything."

From here on, use the board with the saved moves applied.
<!-- shared:board-check:end -->

## Answer each question

- **Why do you want to work here? / Why this company?** — 60–120 words: one specific,
  sourced thing about them (from the brief, never a guess), one line connecting it to
  a win from the record, one line on what the person wants to do there. No "I've always
  admired", no "passionate".
- **Why this role? / What interests you about this position?** — the posting's top need
  and the person's matching result; 60–100 words.
- **Tell us about yourself / cover-note box** — three or four sentences: target role,
  two wins, why now (the approved line only).
- **Desired pay / salary expectations** — in the pay type the role uses (hourly,
  annual, base plus commission, or step on a schedule):
  - **The posting shows a range:** answer inside it, anchored to what the person's
    record supports, never below their minimum pay.
  - **Free-text field, no range posted:** a researched range with the person's minimum
    pay as the bottom, or "Open to discussing, based on the full package" if they'd
    rather not name a number. Follow the profile's share-my-minimum setting.
  - **Numbers-only field:** explain the trade-off in one line (a number now can anchor
    the offer; a low number is hard to walk back) and **let the person pick the
    number**. Never invent market data; never enter a placeholder like 0 or 999 for
    them.
- **Current or past pay / salary history:** many US states and some provinces bar
  employers from asking (for example California, Colorado, Massachusetts, New York,
  Washington, and British Columbia in Canada — the lists change; check a
  maintained tracker or your state or province's labour-standards page, "as of" the
  date you apply). Say: "Where your state bans this question you can leave it blank or
  decline. Elsewhere, you can still answer with what you're looking for instead." Never
  fill in pay history for them. Not legal advice.
- **How did you hear about us?** — the true source from the Application Board (and the
  referrer's name only with their permission).
- **Work authorization / sponsorship** — the person answers these themselves; draft
  only if they tell you the facts, and never guess.
- **Licenses and certifications** — from the record: type, state or province, status,
  expiry. A license number only if the person gives it and the form asks.
- **Notice period / start date / relocation / schedule** — from the profile or ask once.
- **Short essay questions** — answer from a named Story Bank entry or win; 100–200
  words; never a story the person didn't tell you.

## Never answer these for them

Voluntary self-identification questions — race or ethnicity, gender, sexual
orientation, veteran status, disability — are the person's to answer or decline. Say
once: "These are voluntary. On US federal-contractor forms, choosing not to answer
can't be held against you, and there's always an 'I don't wish to answer' option. I'll
leave them for you." Never pre-select or suggest an answer.

## Deliver

- One paste-ready answer per question, in the form's order, each labeled with the
  question and its character or word limit if the form shows one (trim to fit).
- Saved as "Application answers — [Company].md" in this Project (and in the company's
  Drive folder when connected), and noted on the Application Board row.
- The oversell, undersell, source, and salary checks apply.

## Constraints

- Nothing submitted, clicked, or filled in for them — answers are text to paste.
- Every claim traces to the record; every company fact to the brief's sources.
- No Social Security or Social Insurance number, bank details, or ID numbers in any
  answer before a written offer — if a form asks for them up front, that's a caution
  signal worth checking.

## Close

Which answers need the person's input (`[confirm]`, the pay number if they're picking
it, anything left for them), where it was saved, then "What's next?" — offer the
command center.

## About this plugin

Part of the Job Search AI Operating System by The AI Career Lab. https://clowealex.gumroad.com/l/job-search-ai-os
