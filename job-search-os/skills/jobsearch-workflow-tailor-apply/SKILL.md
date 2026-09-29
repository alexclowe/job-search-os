---
name: jobsearch-workflow-tailor-apply
description: Tailor and apply for the Job Search AI Operating System. Invoke when a job seeker says "tailor and apply", "tailor my resume to this posting", "apply to this job", "here's a posting", "write my cover letter for this role", or pastes a job description and asks for a resume or application. Starts with one check card — is it real, does the pay clear your minimum, how well you fit, and whether you know someone there — then produces a tailored resume and cover letter that lead with real results, shows which posting terms made it in and which your record can't support yet, drafts the application-form answers, and files it on the Application Board.
---

> **Naming rule (never break):** the product is the **Job Search AI Operating System**.
> Use only this product name — never an older one. Never name profile or connection filenames in conversation.
> **Words rule (never break):** the lowest pay the person will accept is their **minimum pay**
> (in their pay type), in every status line, reply, file, and tracker. The comparison against
> it is the **salary check**. Never call it a "floor", even if an older profile or memory does.

One posting, start to finish: is it real and worth your hour, do you know someone
there, what they actually want, a resume and letter built from what you did and what
came of it, the form answers, and a row on the board so it doesn't vanish.

## How this job delivers its outputs

- **Anything that leaves your hands** — submitted, attached, or edited in Word (resume,
  cover letter, a one-page addendum) — is a real file: .docx or .pdf, saved in this
  Project (and in the Drive folder when Drive is connected).
- **Anything you come back to** — the Application Board, the Story Bank, the Offer
  Tracker, the Weekly Search Log — **must be published or updated as a live artifact**
  in your Artifacts sidebar on every run (a CSV alone is not enough when artifacts are
  available). Before creating one, look for an existing artifact with the same name
  (including from earlier conversations) and update it instead of making a duplicate.
  The **Application Board** is always built from its fixed template (see "Application
  Board" in the Tailor & apply job): a board with a column per stage, where the person
  can move a card themselves. Keep a CSV copy of a tracker's rows in the Project as a
  backup and keep it in sync. Sample-run items go in a separate "Samples" section and
  never count toward totals. If artifacts aren't available in this environment, use the
  CSV alone and say so once.
- **Emails** are Gmail drafts when Gmail is connected, otherwise paste-ready text (also
  saved as a .txt file). Nothing is ever sent or submitted.
- In the close, name the one output to look at first.

## Pre-flight 1 — Profile

Look for the career profile where every skill in this pack looks: the Project file
`./job-search-os-profile.md`, then this Project's instructions, then a profile block
pasted in this chat. Accept any block with the profile fields, whatever its heading says.
- **Present:** use current role, years, target roles, career stage, pay type and
  minimum pay, things a hiring manager might question, wins, location and remote
  preference, and voice samples. Don't re-ask. (Older profiles say `Minimum salary:` or
  `Salary floor:` for minimum pay, **Shipped artifacts** for wins, and `Positioning
  challenges:` for things a hiring manager might question — read them the same way.)
- **Absent:** say the profile isn't set up and that "run the setup wizard" takes about
  two minutes. If they decline, continue with what they paste, mark the salary check
  "no minimum pay on file", and say so in the close.

## Pre-flight 2 — Connections

Read `./jobsearch-connections.md`.
- **Present:** note which of gmail / calendar / drive are connected and the
  `drive-root-folder`.
- **Absent:** say once: "I'm not connected to your tools yet — say 'connect my tools'
  anytime. For now everything comes out paste-ready." Continue.

Check which connector tools actually exist in this session; never assume a tool name.

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

## Intake

Trackers named "SAMPLE — …" are from the demo. Never read from or write to them except
during a sample run.

**Read first, ask last.** If the person pasted or pointed to anything (the posting, a
link, their resume, a referral's message), pull every answer you can from it first.
Then ask only what's still missing — at most 3 questions in one card of clickable
choices — and produce a first draft. Anything still unknown goes in the draft as
`[confirm]`, not another question.

**Missing profile detail?** If this job needs something the profile doesn't have
(minimum pay, remote preference, the current resume), ask for it once here, use it,
then save it into the matching section of the profile with one line: "Saved to your
profile so I won't ask again — say 'undo' to remove it." Never block the job on it.

1. **The posting** — pasted text, a link (fetch it if you have web access; otherwise
   ask for the text), or a message from a recruiter or referrer. Note company, title,
   location and remote terms, the schedule (shift, hours, days), and the pay exactly
   as posted — an hourly range, an annual range, base plus commission, or a
   salary-schedule placement.
2. **The resume** — the master resume in this Project ("Master resume.docx" or
   "Master resume.md"), a file they point to, or pasted text. If none exists anywhere,
   offer, as clickable options: **Paste it now** · **Build one from scratch (about ten
   minutes)**. On build, run the master-resume method inline (the
   `jobsearch-master-resume` interview: three short cards, then a master resume in
   current conventions, saved to this Project), then come back here and continue.
   Never write a resume from the profile alone.
3. **How they're applying** (clickable): company site or ATS · through a recruiter ·
   through a referral (name) · by email to a hiring manager.
4. **Anything to get ahead of for this one** — a gap, a title mismatch, a location
   question — beyond what a hiring manager might question already on file.

**Profession archetype (read, don't ask).** If the profile or the posting names a
profession, look for a matching archetype file — first `./archetypes/<profession>.md`
in this Project, then the `archetypes/` folder that ships next to this skill (for
example `archetypes/nurse.md`, `archetypes/teacher.md`, `archetypes/bookkeeper.md`).
Find the file through `archetypes/index.md` first (it ships in the same folder): match the profession against its Name and Also called columns and open only that one file. If more than one row fits ("nurse" could be a registered nurse, an LPN, a nurse practitioner, or a nursing assistant), ask one short question with those rows as options before opening anything.
An archetype is a short, hedged brief: the titles that hiring teams use for the role,
where the postings tend to live, what a recruiter screens for first, the story types
that land, the red flags in postings, how pay is usually structured, and what's
usually negotiable. Use it to sharpen the posting decode and the
resume's ordering; it never supplies a claim, a number, or a keyword the person's own
record doesn't support. If no archetype matches, continue without one and say nothing
about it. Anyone can add one — see `archetypes/_template.md`.

## Before you tailor — one check card (non-negotiable)

Four checks, in this order, on **one card** — not four interruptions. Decode the
posting while you run them (must-haves vs. nice-to-haves in their own words, the three
things the hiring manager is most likely worried about, the terms an
applicant-tracking system will match on, the schedule and pay exactly as posted), then
show the card and wait for one choice. **End your turn on the card.** Do not draft,
tailor, or file anything until the person picks, even when every check is clean; a
clean card still ends with the three choices. (The one exception is the sample run,
which picks Tailor it on the person's behalf and says so.)

**1. Is this real?** Run the `jobsearch-real-check` signals on the posting and any
recruiter message: the stop-and-check signals from official consumer-protection
guidance (pay to start, a check to send back, ID or bank details before an interview,
crypto, an unexpected text about a job never applied for, chat-only interviews, a
free or look-alike email domain, big pay for vague work, pressure, reshipping) and the
softer maybe-not-an-open-role signals (not on the employer's own careers page, old or
reposted, no named team, a legally required pay range missing, a posting that says
it isn't for a current vacancy). Report counts and what showed them — **signals,
never a verdict**, and never call a named company a scam.

**2. Pay.** Compare the posting against the minimum pay on file, **like with like**
(the salary guard's rules):
- **Hourly:** the top of the posted hourly range against the hourly minimum.
  Differentials, overtime, and sign-on bonuses are noted separately, never added to
  the base. If one side is annual and the other hourly, convert with a stated hours
  assumption ("at 36 hours a week [confirm hours/week]").
- **Annual salary:** the top of the posted range against the annual minimum.
- **Commission or commission plus base:** the base (or draw) against any base minimum,
  and the realistic expected total the posting or recruiter states against the
  expected-total minimum. "Up to" and "top producers earn" figures don't count.
- **Salary schedule:** the step and lane the posting or district would likely place
  you at, and that step's figure on the published schedule, against the minimum.
No pay posted → look in the recruiter's message; if none, "pay unknown — ask on the
first call". Say the result in these words: "Salary check passes: [posted pay] against
your [minimum pay] minimum." or "Salary check: no pay posted, so ask on the first call." For hourly and commission roles, add the one pay question worth asking
on the first call (guaranteed hours and the differential schedule, or the split,
draw, and ramp).

**3. Fit.** Match the must-haves against the person's record (profile wins, master
resume, Story Bank): **strong** (every must-have has a matching result) · **partial**
(most do; name the gaps) · **stretch** (two or more must-haves have nothing behind
them). Always name the two biggest gaps and whether each is a real gap or just
missing from the resume ("you've done this — it's not on your resume yet").

**4. Do you know someone there?** Read the **People** board (and the LinkedIn
connections file in this Project, if there is one) for this company — the
`jobsearch-people-tracker` method: match by company name, not email. If there's no
People board and no connections file, and the profile doesn't say `People import:
offered` yet, add one line offering it once: "Want to check whether you know anyone
here? Your LinkedIn connections export takes up to a day to arrive — say 'import my
connections' anytime." Then write `People import: offered [date]` into the profile's
**Target** section so it isn't offered again.

**The card** (clickable, then wait):

```
[Company] — [Role] · [location / remote] · [schedule]
Is this real?  [0 caution signals · or: N stop-and-check signals — check before replying]
Pay            [posted pay] vs your minimum [minimum] → [above · below · unknown] [+ the one pay question]
Fit            [strong · partial · stretch] — gaps: [gap 1] · [gap 2]
People         [You know N people there: Name (role) · or: nobody on your list yet]
What they want [three must-haves, in their words]

→ Tailor it   → Skip it   → Get the intro first
```

- **Any stop-and-check signal** fired → the card leads with "Check this before you
  reply or send anything," lists the ten-minute checks, and **Tailor it** becomes
  "Tailor it after I've checked". Never draft a "YES" reply to an unsolicited text;
  never put an SSN, SIN, bank details, or ID number into anything before a written
  offer.
- **Pay below the minimum** → the card says it plainly: "This role posts at [pay as
  posted], and your minimum is [minimum pay]. Flagging it now, not after three
  rounds." **Tailor it** becomes two choices: "Apply anyway and raise pay on the first
  call" · "Apply and mark it as a fallback". Record the choice on the board.
- **Stretch fit** → say it once, kindly, and still let them choose.
- **Someone there** → **Get the intro first** is pre-selected.

**Show the choices every time.** Render the card with the visual card/widget tool
when it is available: the checks as the card body, and the three choices as its
buttons (with the changed labels above when a check fired). When that tool isn't
available, or you can't tell whether it rendered, end the message with these three
numbered lines, exactly, and nothing after them:

```
1. Tailor it
2. Skip it
3. Get the intro first
```

A check-card reply that ends without the three choices is incomplete: add them before
you stop. Clicking a choice only stages it; act when the choice arrives, clicked,
typed, or as its number.

**On "Skip it":** add the row at stage **Closed**, Closed why "skipped — [reason]",
and stop. **On "Get the intro first":** draft the intro request (the people-tracker
method: 60–120 words in the person's voice, the role by name and link, one small ask,
an easy out, plus a three-line forwardable blurb), as a Gmail draft when connected or
paste-ready; update the **People** row (Intro status "asked", Last touch today, Next
"follow up once in five business days") and add the Application Board row at stage
**Interested** with Source "referral (pending)", Next action "intro from [name]", Due
five business days out. Then offer: "Want the tailored resume and letter ready now, so
you can send them the moment the intro lands?" — and continue to Produce only on yes.
**On "Tailor it":** continue.

Before any tool writes, say once: "As I work, Claude may ask you to approve actions —
this run involves about [N] (the resume file, the cover letter, one folder, and the
Application Board). Choosing **Allow for this task** covers the rest of this run, and
tracker updates always take a quick confirm."

## Produce

1. **Tailored resume (.docx)** — the person's real resume (the master resume when
   there is one), reordered and rewritten for this posting:
   - Summary (3 lines max) that names the target role and leads with the two wins most
     relevant to their worries — **what was done and its result before any title**.
   - Each bullet: action, scope, result, in the posting's vocabulary where the person's
     record honestly supports it. Quantify only with figures the person supplied; a
     bullet with no figure says what changed, not a made-up percentage.
   - Whatever a hiring manager might question is handled in the text, not in a
     disclaimer: a manager returning to hands-on work leads with the hands-on work from
     the management years; a career changer leads with the results that carry over, in
     the new field's words; someone returning to work gets a one-line, factual entry
     for the gap; a license from another state names its status plainly.
   - Same page count as the original unless they asked to cut. Plain formatting an
     ATS can parse: one column, standard section titles, no tables, text boxes, or
     graphics, no contact details in the page header or footer.
   - A **change log** at the end of the chat message: what moved, what was reworded,
     what was cut, and any claim the person should double-check.
2. **Posting terms — what made it in, and what your record can't support yet** (in
   chat, right after the resume):
   - **Now on your resume:** the posting's key terms the tailored resume uses, each
     with the resume line that backs it.
   - **Not supported by your record yet — tell me if you've done these:** each missing
     term as a question — "Did you do [X]? Tell me what and I'll add it." **Never add a
     term, skill, or tool to the resume because the posting wants it.** A term goes in
     only after the person gives you the real experience behind it.
3. **Cover letter (.docx, 250–350 words)** in the person's voice: a specific opening
   about this company or problem (never "I am excited to apply"), two short paragraphs
   pairing their two strongest wins with the posting's top worries, one line that gets
   ahead of what a hiring manager might question, a plain close. No adjectives about
   themselves ("results-driven", "passionate"), no mention of pay.
4. **Application-form answers** (when they're applying through a company site or ATS,
   or paste the form's questions) — the `jobsearch-application-questions` method:
   why us (one sourced fact about the company — from **Company brief — [Company].md**
   in this Project, or a short brief built now with sources; never a guess), why this
   role, desired pay in the role's pay unit (inside a posted range and never below the
   minimum; for a numbers-only field, explain the trade-off and let the person pick the
   number), how they heard about it (the true source), licenses from the record.
   Salary-history questions: note that many states and some provinces bar them and
   the person can leave them blank or decline where that applies (not legal advice).
   **Never answer voluntary self-identification questions** (race, gender, veteran,
   disability) — say they're voluntary and theirs to answer or decline. Saved as
   "Application answers — [Company].md".
5. **Application note** (only for referral or email applications) — 60–120 words to
   the referrer or hiring manager, in their voice, attaching or naming the two files.

## Compliance pass (inline — do not hand off)

Screen every file in this turn:
- **Traceability:** every metric, title, date, employer, and accomplishment traces to
  the resume or profile the person supplied. Anything else is cut or replaced with
  `[confirm]`. Never round a number up.
- **Every claim holds up:** for each claim, could the person back it with a specific example
  in an interview? Flag any that reads stronger than the record ("led" where they
  "contributed to"; "owned" where they "worked on").
- **Nothing undersold:** judged against the same record — any win that answers one of
  the posting's top worries but is buried, understated ("helped with" where the record
  says they did it), or left out gets flagged with the stronger honest line (the
  undersell check). Never adds anything the record doesn't support.
- **Posting terms:** no term went onto the resume just because the posting used it;
  every added term has a record line behind it.
- **Form answers:** no voluntary self-identification answer, no pay history, no SSN,
  SIN, bank, or ID number anywhere.
- **AI-register tells:** remove "leverage", "synergy", "results-driven", "passionate",
  "spearheaded", "dynamic", stacked adjectives, and any sentence that could open any
  cover letter. Read the letter aloud in your head; if it doesn't sound like the voice
  samples, rewrite it.
- **Privacy:** no home street address, no date of birth, no photo, no current-employer
  confidential figures (name the scale in relative terms if the profile marks it
  confidential), no salary history.
- **Minimum pay:** the salary-check result is recorded on the board; the letter never names
  a number.
Append one short **Before you submit** checklist with only the checks that fired.

## Route outputs

- **Drive connected:** create `[drive-root-folder]/[Company] — [Role]/` and save the
  resume as "[First Last] — Resume — [Company].docx" and the letter as "[First Last]
  — Cover letter — [Company].docx". Never overwrite the master resume.
- **Gmail connected:** the application note as a draft, To: filled only if the address
  is known. **Never send.** Never draft into an employer's inbox for them.
- **Calendar connected:** one reminder titled "Follow up — [Company]" only if the
  person gives a follow-up date; never invent one.
- **Otherwise:** both files saved to this Project's folder, the note paste-ready.
- **Form answers** go in the same company folder (Drive) or this Project as
  "Application answers — [Company].md". Nothing is typed into the employer's form for
  them.

## Application Board (living tracker)

List this Project's artifacts first, including ones from earlier conversations. If an
**"Application Board"** artifact exists, add this application; create it only if
absent. This job owns the board's columns; every other job and skill writes to them:

Company · Role · Stage (Interested → Applied → Screening → Interviewing → Onsite →
Offer → Closed) · Posted range · Salary check (above / below, applying anyway / below,
fallback / unknown) · Real check (0 signals / N stop-and-check / N maybe-not-open) ·
Fit (strong / partial / stretch) · Source (referral · job board · recruiter reached
out · applied direct · other) · Referral (name, or blank) · Applied on · Reply on ·
Screen on · Interview on (one date per round, separated by semicolons) · Final on ·
Offer on · Closed on · Closed why (no reply · rejected after screen · rejected after
interview · rejected after final · withdrew · skipped · offer declined · accepted
elsewhere) · Last touch · Next action · Due · Contact · Notes.

Set **Applied on** when the person says they've submitted (ask on the next run if it's
still blank at stage Interested). **An older board without the newer columns keeps
working:** carry its rows over and leave the missing columns blank — blank means
unknown, never zero. Board views: by stage, plus a "Due this week" list at the top.
Sample rows sit under "Samples" and never count.

**Build it from the template, every time.** The board is the fixed template
`templates/application-board.html` that ships with this job
(`jobsearch-workflow-tailor-apply/templates/application-board.html`): a column per
stage, a "Due this week" list, a Samples section, and every column in a table the
person can open. Copy the file exactly and change **only the JSON inside
`<script type="application/json" id="board-data">`** — never the markup, styles, or
code. In that block, each row is one object with the keys `id`, `company`, `role`,
`stage`, `postedRange`, `salaryCheck`, `realCheck`, `fit`, `source`, `referral`,
`appliedOn`, `replyOn`, `screenOn`, `interviewOn`, `finalOn`, `offerOn`, `closedOn`,
`closedWhy`, `lastTouch`, `nextAction`, `due`, `contact`, `notes` (dates as
YYYY-MM-DD, blank as ""); sample rows go in `samples`, never in `rows`; `asOf` is
today's date. **A row's `id` never changes;** a new row takes the next free id
(`r1`, `r2`, …), because the moves the person saves are keyed to it.
- **Publish it with the artifact's storage (database) capability turned on**, default
  access rules, so the person's moves are saved and every job can read them. Keep the
  title "Application Board".
- **Updating** means: apply saved moves first (the board check above), read the
  board's current data block, change the rows, and republish the same template. An
  older board that isn't built on the template (a plain table from an earlier
  version) is rebuilt on it once, carrying every row and column over; say so in one
  line.
- **The first time** a board with storage is published, add one line to the close:
  "Your board saves moves you make on it. Boards that save moves stay private to your
  organization (no public link), and anyone you share it with as a viewer can see it
  but not move cards."
- **No artifacts or no storage here:** publish the board without storage (or keep
  the CSV alone when artifacts aren't available) and say once: "Tell me when a card
  moves, for example 'move Northwind to Interviewing'."

## Close

Never narrate your own tooling in the close: nothing about files you could not open, workbooks you could not recalculate, pages you did not open, or what the sandbox lacks. State what was produced, what needs confirming, and where it landed.

List what was made and where (resume / letter / answers / note / folder / board row),
the `[confirm]` list, the check card in one line (real · pay · fit · people), the
"did you do these?" questions still open, then "What's next?" — offer the command
center. If a Story Bank exists and a strong story surfaced during tailoring
that isn't on it, offer to add it.
