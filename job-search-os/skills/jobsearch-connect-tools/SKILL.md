---
name: jobsearch-connect-tools
description: Connect Gmail, Google Calendar, and Google Drive to the Job Search AI Operating System. Invoke when a job seeker says "connect my tools", "connect my email", "hook up Gmail", "check my connections", or asks how to get application drafts, interview holds, and tailored resumes into their real inbox, calendar, and Drive. Verifies each connector with a safe read and saves a connections record so every search job knows where to put drafts, events, and files.
---

> **Naming rule (never break):** the product is the **Job Search AI Operating System**.
> Use only this product name — never an older one. Never name profile or connection filenames in conversation.

Get someone from "not connected" to "verified" in under ten minutes. Outlook and
Microsoft 365 users: the same steps work with those connectors if they're what's
installed — use whichever mail, calendar, and file connectors are actually present.

One rule before anything else: **use a personal account, never a current employer's.**
If the only mail or Drive connected belongs to an employer, say so and record
`not-connected` — a job search never runs through work systems.

## Step 0 — Re-run

Read `./jobsearch-connections.md`.
- **Present:** say what's recorded as connected and when it was verified, then offer as
  clickable choices: "Re-check everything", "Fix one connection", "All good — back to my
  command center". Continue below only for what they pick; rewrite the file at the end.
- **Absent:** continue.

## Step 1 — Profile check

Look for the career profile (the Project file `./job-search-os-profile.md`, then this
Project's instructions, then a pasted block). If none, say: "Quick heads-up — your
career story isn't set up yet. Connections work without it, but drafts come out
generic. Say 'run the setup wizard' anytime." Then continue.

## Step 2 — How this works (say it once, plainly)

- "I work inside your own accounts. Nothing sends, nothing lands on your calendar, and
  nothing is filed without your click. Claude may ask you to approve actions — choosing
  **Allow for this task** covers the rest of that run."
- "Reading your inbox means: I look for messages from recruiters and hiring teams, show
  you what I found, and you confirm before anything is used."
- "If a tool isn't connected, every job still works — you paste the message or posting
  and get copy-paste-ready output and files saved here instead."

## Step 3 — Connect and verify

Check which connector tools are actually available in this session — never assume a
tool name. For each one missing, explain: "Open **Customize → Connectors**, add
[Gmail / Google Calendar / Google Drive], sign in with your **personal** account, then
come back and say 'check my connections'." If the user says skip, record
`not-connected` and move on.

- **Email — test:** create one draft to the user's own address, subject "Job Search OS
  connection test — safe to delete". Confirm it exists by listing drafts.
- **Calendar — test:** read today's events and report the count. An empty day is a
  successful read. Create no test event.
- **Drive — test:** ask for the folder name as a clickable choice — default
  "[First name] — Job Search" or "type my own". Create that one folder. Create no test
  files. Tell them: each company gets a subfolder inside (resume, cover letter, prep
  brief, offer notes).

## Step 4 — Save

Write `./jobsearch-connections.md`:

    # Job Search OS connections
    gmail: connected | not-connected
    calendar: connected | not-connected
    drive: connected | not-connected
    drive-root-folder: [folder name]
    account-note: personal
    verified: [today's date]

Use the real results. Every search job reads this file to decide where outputs go.

## Step 5 — Back home

One line per connector ("Email ✓ — drafts land in your Drafts folder", "Calendar ✓ —
interview holds go here"), then: "You're set. Paste a posting and say **'tailor and
apply'** — or open your command center." Offer the command center (`jobsearch-os`).
