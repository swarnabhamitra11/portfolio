# Synaptic Plasticity as Short-Term Memory
### DataForge 2026 · Pathway Track

Interactive educational explainer and toy reimplementation for the approved concept **Synaptic Plasticity as Short-Term Memory**.

> **Central claim:** A recurrent model can temporarily store sequential associations in a fixed-shape synaptic state using local Hebbian outer-product writes, avoiding a token-by-token KV cache; however, dense synaptic memory develops associative interference as stored bindings approach or exceed the effective representational rank.

**Important:** this is a toy educational reimplementation, not the official Pathway BDH implementation.

## Public artifact
The artifact is `artifact.html`. When GitHub Pages is enabled for this repository, it can be served without sign-in.

Expected path from the portfolio repo:
`https://swarnabhamitra11.github.io/portfolio/dataforge-synaptic/artifact.html`

## Local setup
### Browser artifact
Open `artifact.html` directly in any modern browser. It has no backend and no sign-in requirement.

### Python toy experiment
Requirements: Python 3.10+, NumPy, Matplotlib.

```bash
pip install -r requirements.txt
python src/interference_demo.py
```

The experiment is synthetic and demonstrates interference in a dense outer-product memory. It must not be interpreted as an official BDH reproduction.

## Submission files
- `artifact.html` — self-contained interactive learning artifact.
- `blog.pdf` — technical blog / visual essay.
- `concept_summary.pdf` — one-page concept summary.
- `source_license_record.md` — sources, licenses, data, graphics and fonts.
- `ai_assistance_disclosure.md` — AI assistance and technical ownership disclosure.
- `src/interference_demo.py` — toy numerical experiment used by the artifact package.
- `requirements.txt` — local experiment dependencies.

## Recent primary literature (2022–2026)
1. Tyulmankov, Yang & Abbott (2022), *Meta-learning synaptic plasticity and memory addressing for continual familiarity detection*, Neuron 110(3):544–557.e8.
2. Shervani-Tabar & Rosenbaum (2023), *Meta-learning biologically plausible plasticity rules with random feedback pathways*, Nature Communications 14:1805.
3. Agnes & Vogels (2024), *Co-dependent excitatory and inhibitory plasticity accounts for quick, stable and long-lasting memories in biological networks*, Nature Neuroscience 27:964–974.
4. Kosowski et al. (2025), *The Dragon Hatchling: The Missing Link between the Transformer and Models of the Brain*, arXiv:2509.26507.

## Evidence discipline
BDH-specific claims are grounded in the primary BDH paper and official Pathway materials. Reported benchmark values are labeled as reported/precomputed rather than independent reproductions. The toy implementation is explicitly separate from BDH.

## Scope and limitations
This project does not claim that all biological memory is equivalent to a matrix state, that BDH is a conventional SSM, that sparse updates are automatically efficient on standard GPUs, or that developer-reported benchmarks are independent reproductions.

## License
Project-authored code and web content are MIT licensed. Research papers, third-party repositories, trademarks and reused components remain under their original licenses; see `source_license_record.md`.
