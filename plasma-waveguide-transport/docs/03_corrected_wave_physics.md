# Corrected Wave Physics

### Critical Correction

**Phase velocity is irrelevant for transport.**
Only **group velocity** carries energy and information.

### Whistler-Mode Group Velocity

To ensure strict causality across all regimes, the simulation uses the full cold-plasma dispersion relation:

$$
v_g = c \frac{\sqrt{1+X}}{1 + \frac{X \omega_c}{2(\omega_c - \omega)}}
$$

Where $X = \frac{\omega_p^2}{\omega(\omega_c - \omega)}$.

In the low-frequency limit ($\omega \ll \omega_c \ll \omega_p$), this simplifies to:

$$
v_g \approx \frac{2 c \sqrt{\omega \omega_c}}{\omega_p}
$$

This velocity is:
- Always **subluminal** (verified numerically)
- Fully consistent with Maxwell + plasma theory
- Experimentally verified since the 1950s

### Why Earlier Artifacts Occurred

Numerical approximations that infer an “effective refractive index” from phase velocity break down in magnetized plasmas. This repository **does not compute refractive index at all**.
