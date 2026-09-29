---
name: jobsearch-people-tracker
description: People tracker for the Job Search AI Operating System — who you know at the companies you're applying to. Invoke when a job seeker says "who do I know at", "import my LinkedIn connections", "here's my LinkedIn export", "add a contact", "track this referral", or uploads a LinkedIn Connections file. Reads the LinkedIn Connections export, keeps only the people at companies in your pipeline on a live People board, and drafts the intro request — drafts only, never sent.
disable-model-invocation: false
---

> **Words rule (never break):** the lowest pay the person will accept is their **minimum pay**
> (in their pay type), in every status line, reply, file, and tracker. The comparison against
> it is the **salary check**. Never call it a "floor", even if an older profile or memory does.

> **Naming rule (never break):** the product is the **Job Search AI Operating System**.
> Use only this product name — never an older one. Never name profile or connection filenames in conversation.

A referral usually beats a cold application. This keeps track of the people you know
at the companies you're applying to, and makes "ask for the intro first" one click.

## Privacy first (say this once, the first time)

"Your LinkedIn export lists other people's names and jobs. It stays in this Project.
I only copy the people who work at companies on your Application Board onto your
People board, and I never message anyone — every intro request is a draft you send
yourself."

## Get the connections file

If no LinkedIn Connections file is in this Project yet, give these steps (don't guess
the menu if the person says theirs looks different — LinkedIn's labels vary):

1. On LinkedIn, click **Me** → **Settings & Privacy** → **Data privacy** → **Get a copy
   of your data**.
2. Pick the **larger data archive** (that's the one that includes connections) and
   request it.
3. LinkedIn emails a download link — usually within 24 hours — and the link works for
   72 hours.
4. Unzip it and upload **Connections.csv** into this Project.

Until it arrives, add people by hand: "Add a contact — name, company, how you know
them."

## Read the file (carefully)

- **Find the header row; don't assume it's line one.** The file usually starts with a
  short "Notes:" paragraph and a blank line. The header is the first line that
  contains both `First Name` and `Company` — typically `First Name, Last Name, URL,
  Email Address, Company, Position, Connected On`. Tolerate an extra or missing
  preamble line and extra columns.
- **Email is usually blank.** LinkedIn only includes an email when that person allows
  it. Never promise an email address and never key anything on email.
- **Match by company, not email.** Normalize company names before matching: ignore
  case, punctuation, and suffixes like Inc, LLC, Ltd, Corp, Co, Health, Group, and "The";
  also match an obvious short form ("Riverbend Family Health" ↔ "Riverbend Health").
  When a match is uncertain, list it as "possible match" and let the person confirm.
- **Blank Company or Position** → "role unknown"; never guess.
- **Connected On** comes as a date like `24 Jul 2026` (some files use `11/21/15`).
  Read both; never sort dates as text.
- Very large files: read only the columns you need (names, URL, Company, Position,
  Connected On).

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

## What goes on the People board

List this Project's artifacts first, including ones from earlier conversations. If a
**"People"** artifact exists, update it; create it only if absent. Keep a CSV copy
(People.csv) in the Project and keep it in sync.

**Only people at companies on the Application Board** (any stage except Closed), plus
anyone the person adds by hand. Never copy the whole export onto the board.

Columns: Name · Company · Their role · How you know them (LinkedIn connection since
[date] · former colleague · classmate · friend · other) · Profile link · Last touch ·
Intro status (not asked → asked → introduced → referred → declined) · For which
application · Next · Notes.

When a new company lands on the Application Board, check the connections file again
for that company and add any matches.

## Who do I know at …?

For a named company: list matches from the People board, then the connections file
(possible matches marked). For each, one line on the likeliest path: a direct ask
(a former colleague, a close connection) or a warm intro through someone else.

## Ask for the intro

Draft the message (60–120 words, the person's voice from the profile), one per
contact, never more than two contacts at the same company at once:
- **To someone at the company:** a real memory or the connection, the role by name and
  link, one line on why it fits (from the person's wins), and one small ask — "would
  you be comfortable referring me, or pointing me to the hiring manager?" — with an
  easy out.
- **Offer to write the forwardable blurb** (three lines they can paste) and include it.
- Gmail connected → a draft, To: filled only if the address is known. LinkedIn
  messages are paste-ready text. **Nothing is ever sent.**

Then update the row: Intro status "asked", Last touch today, Next "follow up once in
five business days". On the Application Board row: Source "referral (pending)",
Next action "intro from [name]", Due five business days out.

## Constraints

- Every claim about the person traces to their profile or resume.
- Nothing invented about the contact — only what the file or the person says.
- Never scrape LinkedIn, never message anyone, never send.
- Sample runs never import files; the sample shows an empty People board with one
  hand-added fictional contact labeled SAMPLE.

## Close

What was imported (count of matches at pipeline companies, not the whole export),
what was drafted and where, then "What's next?" — offer the command center.

## About this plugin

Part of the Job Search AI Operating System by The AI Career Lab. https://clowealex.gumroad.com/l/job-search-ai-os
