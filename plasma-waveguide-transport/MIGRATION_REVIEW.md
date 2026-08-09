# Conventional plasma consolidation review

Date: 2026-08-09

Destination baseline: `Zoverions/Plasma-Waveguide-Transport@44eeb6ea0778596aaf6d5e144ff8dbcc4e50a0bb`

## Decision

No source code is migrated in this change. The reviewed MIT-compatible candidate does not add a correct, implemented capability beyond the destination. Two other sources remain blocked by missing reuse grants. Their unique work and negative findings remain in their original repositories and portfolio backups.

## MIT-compatible source review

Source: `Zoverions/The-Fractal-Transport-Master-Plan@2cf1debf5212b095cddca2c7092befedf967ffb1`

| Source path | SHA-256 | Finding | Decision |
|---|---|---|---|
| `src/plasma_waveguide/whistler_modes.py` | `5e9dfb749019675cd848a0c28246b6e28094654b3683cf620d7d3b97c5f2dd4e` | Computes a phase-derived refractive index and labels an `n < 1` condition “superluminal”; it does not calculate group velocity | Do not copy into the group-velocity-limited core |
| `src/plasma_waveguide/accelerator.py` | `240e323242ad6be2256fc06e9f067318cd4eb35fe0b96edc2b22e0656271f680` | Contains only `"Not yet implemented"` | Preserve as a negative implementation finding; do not migrate |
| `LICENSE` | `84514bc5571a10c383f50d87285b12750b80ed5cb8d4e8fe0a12fddcb2b817d9` | MIT permission grant | License-compatible, but technical and duplication gates still reject migration |

The destination's existing `src/plasma_physics.py` at the baseline SHA has SHA-256 `c408d0e5c99b29a1a303883858291033ca7fb68d71d3585c742e8504a7cf7ba4` and already implements the bounded cold-plasma group-velocity expression described in `docs/03_corrected_wave_physics.md`.

## License-blocked sources

- `Zoverions/Coherent-Transport-in-Magnetized-Plasma-Channels@26cb6f9c09223c2acc1b951ea35f77460bf905c8` has potentially relevant interferometry, whistler, and channel utilities but no detected permission grant. Its implementation also labels a script as a PIC simulation although it does not implement a particle-in-cell solver. Do not copy it without an owner rights/license decision and module-level validation.
- `Zoverions/Fractal-Transport@7675d63af3c3ff753740486bc92c2c072576bb90` has no detected permission grant and mixes conventional calculations with speculative ER=EPR material. Do not copy it into the grounded core.

## Destination hardening performed instead

- Validate finite, positive density and magnetic-field magnitude.
- Reject nonfinite, nonpositive, cyclotron-resonant, and above-resonance frequencies.
- Test that the declared whistler branch remains finite, positive, and subluminal across 400 sampled frequencies.
- Test the documented low-frequency approximation against the implemented expression.
- Pin the tested NumPy/SciPy environment and add immutable CI action pins.

This review does not establish laboratory validation, engineering feasibility, or a transport deployment. It verifies only the bounded computational behavior covered by the tests.
