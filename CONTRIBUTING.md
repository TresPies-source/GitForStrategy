# Contributing

*Grounded in experience, written in plain words, checked before it merges.*

## Seeds

A seed comes from real work, not theory. "I think this would help" is not enough; "this happened on a project, and here is what we learned" is.

1. Run `python3 scripts/gfs.py new seed "Name of the pattern"` from a workspace, or copy `templates/seed.md` into `seeds/`.
2. Fill in every section. Grew from says where the pattern came from — the project or retro, and when — and cites any published source.
3. No numbers without a source. If the effect was not measured, say so.
4. Run `python3 scripts/gfs.py seeds index --write --plugin` to update the index of the seeds that ship here.

## The contract

Changes to `SPEC.md` start the way any decision does here: a scout and a decision record in this repository's own workspace, `strategy/`. A change that adds optional fields, sections, or types is a minor version. A change to what is required is a major version. Update `scripts/gfs.py`, the templates, and the tests in the same pull request as the spec.

## The script and the commands

`scripts/gfs.py` uses the Python standard library only and runs on Python 3.9 or later. Add a test in `tests/` for any behavior you change. Commands that create artifacts write through `gfs.py` and validate what they write; keep it that way.

## Before you open a pull request

```bash
python3 -m unittest discover -s tests
python3 scripts/gfs.py selfcheck
python3 scripts/gfs.py validate --strict
python3 scripts/gfs.py validate --root examples/native-or-web --strict
```

CI runs the same checks.

## Writing

Plain, calm, concrete. Address the reader as "you." Short declarative sentences. No hype words, no emoji, no exclamation marks. Every number has a source, or the text says *not measured*.

## AI assistance

If AI tools helped write a contribution, say so in the pull request.

## License

This project is licensed under Apache-2.0. Under section 5 of that license, a contribution you submit is licensed under the same terms.
