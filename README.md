# Plasma Waveguide Transport

Computational research prototype for group-velocity-limited transport in magnetized plasma waveguides.

The maintained package is in [`plasma-waveguide-transport/`](plasma-waveguide-transport/). It contains the model, bounded validation tests, documentation, notebooks, references, and example output.

This repository does not claim laboratory validation, engineering feasibility, safe hardware operation, faster-than-light transport, or deployment readiness.

## Validate

Use Python 3.12 from the package directory:

```bash
python -m venv .venv
# Activate .venv using the command for your shell.
python -m pip install --disable-pip-version-check -r requirements.txt
PYTHONPATH=src python -m unittest discover -s tests -v
```

The hosted workflow runs the same bounded-model tests. See [`SECURITY.md`](SECURITY.md) for private vulnerability reporting and [`MIGRATION_REVIEW.md`](plasma-waveguide-transport/MIGRATION_REVIEW.md) for the hash-bound overlap decision.
