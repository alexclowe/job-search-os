# Security

## Reporting

Email **alex@theaicareerlab.com** with "job-search-os security" in the subject. Please do not open a public issue for anything that could expose another person's data. You will get a reply within five business days.

## What this plugin can and cannot do

This repository contains markdown skill files and one JSON manifest. It ships no executable code, makes no network calls of its own, and has no telemetry. Everything it does happens inside your own Claude account, under the permissions you have granted Claude.

It **can**, when you connect them and only with your approval per action:

- create drafts in your Gmail Drafts folder,
- create events on your Google Calendar,
- create files in your Google Drive,
- read messages you point it at, or search your inbox for recruiter and hiring-team threads when you ask it to.

It **cannot**, and is written never to:

- send an email, submit an application, accept or decline an offer, or click anything on your behalf,
- connect to an employer's mailbox or Drive (the connect-tools flow asks for personal accounts only),
- move your data anywhere outside your Claude account and the Google account you connected,
- invent a figure, title, date, or employer; anything without a source in your own record is marked `[confirm]`.

## Scope of the validation workflow

`scripts/validate.py` checks structure (frontmatter, manifest, archetype sections). It is not a security scanner. If you find a skill whose wording could lead Claude to take an action the user did not approve, treat it as a security report.

## Supported versions

Only the latest release on `main` is supported.
