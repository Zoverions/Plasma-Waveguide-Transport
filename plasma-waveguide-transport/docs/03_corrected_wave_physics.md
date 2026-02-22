# Corrected Wave Physics

### Critical Correction

**Phase velocity is irrelevant for transport.**
Only **group velocity** carries energy and information.

### Whistler‑Mode Group Velocity (Low‑Frequency Limit)

\[
v_g \approx \frac{2 c \sqrt{\omega \omega_c}}{\omega_p}
\]

(Note: The code implementation uses the full R-wave dispersion relation for numerical accuracy near resonance.)

This velocity is:
- Always **subluminal**
- Fully consistent with Maxwell + plasma theory
- Experimentally verified since the 1950s

### Why Earlier Artifacts Occurred

Numerical approximations that infer an “effective refractive index” from phase velocity break down in magnetized plasmas. This repository **does not compute refractive index at all**.
