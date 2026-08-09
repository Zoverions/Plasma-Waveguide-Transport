# Plasma Waveguide Transport
## A Self-Contained Research & Engineering Package
**Version 1.0 — February 2026**

> **Status:** Computational research prototype. The included checks exercise a bounded cold-plasma model; they do not establish laboratory validation, engineering feasibility, safe hardware operation, or a deployment-ready transport system.

This repository contains a bounded computational investigation of magnetized plasma waveguides for guided energy and particle transport. The work explicitly avoids superluminal claims, refractive-index artifacts, and speculative spacetime manipulation. It focuses on conventional equations for **group-velocity-limited transport**, **ponderomotive channel formation**, and **wakefield acceleration**. The repository has not experimentally validated a combined transport system.

### What This Is
- A **cold-plasma computational study**
- A **proposed laboratory concept** requiring independent design review
- Early **scaling considerations**, not validated space-transport engineering

### What This Is Not
- Not faster-than-light transport
- Not warp drive physics
- Not topology change in GR
- Not speculative propulsion claims

## Reproducible check

Python 3.12 is the tested runtime.

```bash
python -m venv .venv
# Activate .venv using the command for your shell.
python -m pip install --disable-pip-version-check -r requirements.txt
PYTHONPATH=src python -m unittest discover -s tests -v
```

The validation suite rejects inputs outside the declared whistler branch and checks finite, positive, subluminal group velocity over a sampled valid domain. See [`MIGRATION_REVIEW.md`](MIGRATION_REVIEW.md) for the hash-bound decision not to import weaker or unlicensed overlap code.

## Repository Structure

```
plasma-waveguide-transport/
│
├── README.md
├── LICENSE
│
├── docs/
│   ├── 01_background_and_motivation.md
│   ├── 02_physical_model.md
│   ├── 03_corrected_wave_physics.md
│   ├── 04_simulation_methodology.md
│   ├── 05_lab_experiment_proposal.md
│   ├── 06_scaling_considerations.md
│   └── 07_limitations_and_scope.md
│
├── src/
│   ├── plasma_physics.py
│   ├── waveguide_simulation.py
│   └── visualization.py
│
├── notebooks/
│   └── plasma_waveguide_validation.ipynb
│
├── references/
│   └── bibliography.md
│
└── figures/
    └── example_outputs.png
```
