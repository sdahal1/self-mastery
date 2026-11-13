# Weekly study content

Edit the weekly guide arrays in this directory. Full source texts and stable source IDs are in `library/sources-XX.json`. `library/index.json` maps every week to its sources and PDF. Rebuild with `python3 scripts/build.py` after editing.

Schema per week (all fields required):
```
{
"id": "01", "title": "Gratitude", "eyebrow": "short theme, 3-6 words",
"overview": "80-130 words explaining the week's objective, connection and nuances",
"outcomes": ["3 concrete learning outcomes"],
"concepts": [{"title":"concept", "explanation":"80-130 words", "sourceIds":["SM1-008"]}],
"visual": {"title":"descriptive model", "intro":"State this is a study illustration of the course framework", "steps":[{"label":"short label","detail":"one sentence"}], "takeaway":"one sentence"},
"practice": {"title":"actual weekly exercise", "sourceIds":["SM1-008"], "cadence":"Course stated practice frequency/time; do not invent", "steps":[{"title":"step","body":"full clear instructions"}], "prompts":["3-5 concrete prompts for an interactive writing activity"], "obstacles":[{"title":"obstacle","response":"course-grounded guidance"}]},
"stories":[{"title":"source story title", "kind":"Anecdote|Metaphor|Example|Parable", "summary":"100-160 words, faithful paraphrase. No invented attributed stories.", "lesson":"takeaway", "sourceId":"SM1-006", "locator":"Original page N or 00:00:00-00:00:00"}],
"storiesNote":"If empty, say no distinct anecdote/parable identified in reviewed sources; don't invent one",
"cheatsheet":{"principle":"one sentence", "remember":["4-6 specific takeaways"], "try":"one practical cue", "watchFor":"one misunderstanding", "question":"one recall question"},
"quiz":[{"question":"question", "options":["option0","option1","option2"], "answer":0,"explanation":"why with course nuance"}],
"reflection":["3 weekly review prompts"],
"sourceIds":["every source reviewed/included in study synthesis"],
"coverageNote":"Which supporting sources extend the week, and transcript uncertainty if material"
}
```

Provide 4-6 concepts, 4-8 practice steps (Introduction can be orientation), 2-4 quiz items, 1-3 stories when present. Aim 1000-1600 words per week, substantive and useful; avoid generic filler or overcompressed bullets. Attribute beliefs/psychological claims to Gary/the course rather than universal fact. Clearly distinguish suggested reflection prompts/study visuals from official exercises. Do not add medical claims; keep personal practice voluntary and ungraded. No need for web research: this is transformation of supplied course. Source IDs must exist and belong to the same week unless a connection is explicitly labeled. Text plain strings, no HTML/Markdown formatting required. Use normal punctuation; no instructions for the app itself. Record any genuine source limitations in the relevant guide.
