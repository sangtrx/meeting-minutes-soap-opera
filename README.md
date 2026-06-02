# Meeting Minutes → Soap Opera

Turn boring meeting notes into dramatic recap episodes.

## Quick start

- `python main.py --file notes.txt`
- `cat notes.txt | python main.py`
- `python main.py --file notes.txt --mode full --style snarky`
- `python main.py --mode actions --max-items 3`

## Options

- `--file` — Input file with meeting notes
- `--seed` — Make the output repeatable
- `--mode` — `recap`, `summary`, `actions`, or `full`
- `--style` — `dramatic`, `snarky`, or `neutral`
- `--max-items` — Limit summary/action items
