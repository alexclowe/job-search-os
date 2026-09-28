# Troubleshooting

The single home for "something's not working." Other docs point here. If your problem isn't listed, ask Claude inside your Project — describe what you're trying to do — or email **alex@theaicareerlab.com**.

---

## Install & setup

**"Set me up" doesn't start setup.**
You need to be in a conversation **inside your Project**, not a loose chat. Create one from **Projects** in the left sidebar, open it, start a new conversation there, and say **set up my Job Search OS** again (or type `/jobsearch-setup-wizard`). The Project is where your profile and trackers are saved.

**I don't see the plugin after uploading.**
Open **Customize → Plugins → Yours** and check it's listed with its toggle on. If it isn't, upload again: **Add ▾ → Upload plugin**, and pick the `job-search-os-claude-plugin-…zip` **as-is** — don't unzip it.

**Error: "zip cannot contain nested zip files."**
You picked the documentation zip. Upload the **plugin** zip (the smaller one with `-claude-plugin` in the name).

**It keeps asking for my minimum pay.**
That's the one field the wizard insists on — the salary guard can't run without it. If you genuinely don't want one, say "no minimum" and it records that the guard is off; roles below what you'd take will not be flagged until you set one. Paid hourly or on commission? Give the minimum in that unit ("$44/hour", "$55,000 base or $120,000 expected total") and the check compares like with like.

**Outputs don't use my background / sound generic.**
Work inside the Project where you ran setup. If you skipped setup, say **set up my Job Search OS** — paste your resume and it fills in most of your profile in two minutes. If setup ran but drafts still feel thin, the fix is almost always more **wins** and better **voice samples**: say "complete my profile".

---

## Jobs, tools & trackers

**A job didn't put anything in Gmail, Calendar, or Drive.**
Say **connect my tools**. It checks each connection and tells you what's missing (connectors are added under **Customize → Connectors** — use a personal account). Until then, jobs hand you paste-ready output and save files in your Project.

**It won't read my work email.**
By design. A job search never runs through a current employer's mail or Drive. Connect a personal account, or paste the message.

**"Check my inbox" found the wrong messages, or missed one.**
It searches for recruiters, hiring teams, and anyone on your Application Board's Contact column, then shows you the list to confirm. Paste the missing message, or add the sender to the board's Contact column and run it again.

**Claude keeps asking me to approve actions.**
That's by design — nothing touches your email, calendar, or files without your click. Choosing **Allow for this task** covers the rest of that job. Tracker updates always ask with a quick confirm.

**A job didn't find my Application Board, Story Bank, Offer Tracker, or Weekly Search Log.**
Open it from **Artifacts** in the sidebar to confirm it exists, then tell the job: "use the Application Board" (or whichever it is). Trackers named "SAMPLE — …" came from the sample run and are ignored on purpose.

**My scheduled run didn't show up in Gmail or on my calendar.**
Scheduled runs prepare everything and save it for your review — they don't read your inbox or write to your email or calendar on their own. Open the conversation it created, review, and say "move these to Gmail" or "add my focus blocks."

**I want to start over.**
Say **"open my command center"** from anywhere — it drops what was in progress and shows home again.

---

## Claims, numbers & your minimum pay

**It put something on my resume I didn't do, or a number I don't recognize.**
It shouldn't — every figure, title, and date is meant to trace to your resume or profile, and anything without a source becomes `[confirm]`. If one slipped through, say "where did this come from?" and give the real figure or tell it to cut the line. Never send a draft with an unconfirmed claim.

**It flagged a role as below my minimum pay and I want to apply anyway.**
Say "applying anyway." It marks the row "below minimum — applying" on your board and carries on. The flag exists so a role below your minimum doesn't quietly become your main option.

**It won't tell me what the role "should" pay.**
Correct — it organizes evidence you supply or that public search returns, each figure with a source and date, and it never invents a "typical" rate. Run `/comp-research` and give it what you have.

**It drafted something legal-sounding (severance, equity, non-compete).**
Those get a "worth a professional's eyes" line on purpose. The scripts help you ask the right questions; an employment attorney or your jurisdiction's labor office answers them.

---

## Voice & quality

**The letter or answer doesn't sound like me.**
- Say **set up my Job Search OS** → Complete my profile and paste two or three passages of your own writing.
- Add to the request: "Plainer. Shorter sentences. No adjectives about me."
- If a sentence could open anyone's cover letter, tell it to cut that sentence.

**The output is too long.**
Add "200 words max. Cut anything that doesn't apply to this role."

---

## Skills

**I'm not sure which skill to use for a task.**
- Say **"open my command center"** — most of a search is one of the five jobs.
- Or say **"browse all skills"** (`/jobsearch-skill-catalog`, also [skill-catalog.md](./skill-catalog.md)) for the full grouped list.
- Something just happened? A posting → `/job-posting-decoder`; "what are you currently making?" → `/recruiter-screen-prep`; an offer → `/salary-negotiation-script`; laid off today → `/severance-leverage-script`.

**I ran a skill outside the Project by accident.**
Output will be generic — it can't see your profile or trackers. Move to a conversation inside your Project and run it again.

---

## Still stuck?

Ask Claude inside your Project, or email **alex@theaicareerlab.com** with the product name, what you said, and what happened. A human reads every message — and the next version gets better because of it.
