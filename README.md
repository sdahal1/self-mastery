# Self-Mastery I - Field Guide

The complete, portable codebase for the Introduction and all 26 weeks of Gary van Warmerdam's Self-Mastery I. This is a self-contained static web app: HTML, CSS, JavaScript, JSON, and PDFs. It has no runtime packages, server database, API keys, external fonts, analytics, or Sites dependency.

## Start on your Mac

Double-click **Start Self-Mastery.command**. It starts a local server and opens the app in your default browser. Keep the Terminal window open while using it; press Control-C to stop.

Alternatively, open Terminal in this folder and run:

```sh
python3 scripts/serve.py --open
```

Then visit **http://127.0.0.1:8765/**. Python 3.8 or later is required; no pip or npm installation is needed. If port 8765 is busy, use `python3 scripts/serve.py --port 8766 --open`. Keep a consistent address and port to keep using the same browser-local notebook.

The app works without internet while the local server is running. Original recording links and ChatGPT handoffs still need internet. Open it through the local server, rather than double-clicking `dist/index.html`, because the app fetches its JSON files over HTTP.

## Deploy anywhere that serves static files

The ready-to-publish website is **dist/**. Upload the **contents** of that folder to your host's web root, or configure the host's publish/output directory as `dist`.

- Framework preset: Other / static HTML.
- Build command: none when deploying the included `dist/`.
- Optional build command for source-based deployment: `python3 scripts/build.py`.
- Entry point: `index.html`.
- No server runtime, database, environment variables, or secrets are needed.
- No single-page-app rewrite is needed: routes use URL fragments such as `#week/00/learn`.
- Keep the directory structure intact, including `data/` and `readers/`.
- Relative asset links also allow hosting under a subdirectory.

The existing hosted site uses a Sites-provided ChatGPT sign-in gate. That gate is not part of this static codebase. Configure access control with your chosen host if you want the new deployment to remain private. Serve `dist/`, rather than the whole source repository.

## Edit and rebuild

```sh
python3 scripts/build.py
python3 scripts/validate.py
```

The build validates source references and copies all required assets. It recreates `dist/`; make edits in the source folders below. The included PDF files are ready-made assets; a rebuild copies them without retranscribing recordings or reformatting documents.

| Path | Purpose |
| --- | --- |
| `src/index.html` | Page shell and navigation |
| `src/app.js` | Routing, lessons, exercises, notebook, search, and handoffs |
| `src/style.css` | Desktop, phone, and print styling |
| `src/mark.svg` | App icon |
| `content/weeks_*.json` | Editable weekly learning guides |
| `content/SCHEMA.md` | Weekly content field reference |
| `content/library/index.json` | Course/source/PDF index |
| `content/library/sources-XX.json` | Full transcripts and handout text for each week |
| `assets/readers/` | All 27 weekly PDFs and the complete combined PDF |
| `scripts/` | Portable build, validation, and local server scripts |
| `dist/` | Complete generated website, ready to host |
| `EXPORT.json` | Published-version provenance and export inventory |
| `SHA256SUMS.json` | Original export file checksums |

## Included content

- 27 weekly guides, visual learning maps, exercises, stories, quizzes, and printable cheat sheets.
- All 201 sources: 109 transcripts and 92 handouts, containing 29,941 timestamped segments and 396 original handout pages.
- 57 stories and 80 quiz questions across the course.
- 27 individual weekly PDFs, plus the combined 1,080-page course PDF.
- Browser-local notes, reading/practice/review progress, notebook export/import, and prompts to copy into ChatGPT.

The source archive retains its existing transcription and OCR limitations. This export does not add new transcription or audio/video files. The original recording links remain in the source data.

## Your notebook and progress

The notebook is stored in your browser's localStorage for the specific website address. Export it from the hosted site's **My notebook**, then import the JSON file into your local app or new deployment. The codebase contains course content, not your personal browser notebook.

Notes do not automatically sync across devices, browsers, domains, or ports. Use notebook export/import to move them. Clearing browser data can remove local notes. ChatGPT handoffs copy text for you to paste into a separate conversation; there is no embedded AI service or scheduled follow-up.

## Export scope

This package includes the full static app implementation and all assets needed to run it, together with self-contained build inputs. It does not require files from the original development workspace. Hosting credentials, Git remotes, and the original Sites project configuration are intentionally absent from the portable package. The original hosted app remains unchanged.

