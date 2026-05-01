# SGCUF — SGCU Hybrid Image Format

## English Version

SGCUF is an experimental hybrid image format based on SGCU (Suprapixel‑Gradient‑Contrast Units) combined with JPEG compression.  
The goal is to merge:

- suprapixel maps (low‑contrast regions),
- edge maps (high‑contrast structures),
- JPEG‑compressed Y, Cb, Cr channels,

into a single compact binary format.

---

## Repository Structure

SGCUF/
├── sgcu_core.py
├── sgcuf_format.py
├── test_encode.py
├── test_decode.py
│
├── examples/
│   └── real_test.png
│
└── output/

---

## Usage

### Encode
python test_encode.py

Output:
output/real_test.sgcuf

### Decode
python test_decode.py

Output:
output/real_test_decoded.png

---

## SGCUF Format (Short Overview)

- Magic header: `SGCUFMT\n`
- Version: 1
- Metadata: width, height, T, Q
- JPEG Y, Cb, Cr channels
- Edge map (binary)
- Suprapixel map (binary)

A full technical specification is available in `SPEC.md`.

---

## License
The repository is currently private.  
License will be added upon release (likely MIT).

---

# Slovenská verzia

SGCUF je experimentálny hybridný obrazový formát založený na SGCU (Suprapixel‑Gradient‑Contrast Units) a JPEG kompresii.  
Cieľom je kombinovať:

- suprapixelové mapy (nízky kontrast),
- edge mapy (vysoký kontrast),
- JPEG kompresiu Y, Cb, Cr kanálov,

do jedného kompaktného binárneho formátu.

---

## Štruktúra repozitára

SGCUF/
├── sgcu_core.py
├── sgcuf_format.py
├── test_encode.py
├── test_decode.py
│
├── examples/
│   └── real_test.png
│
└── output/

---

## Použitie

### Encode
python test_encode.py

Výstup:
output/real_test.sgcuf

### Decode
python test_decode.py

Výstup:
output/real_test_decoded.png

---

## Formát SGCUF (stručný popis)

- Magic header: `SGCUFMT\n`
- Version: 1
- Metadata: rozmery, T, Q
- JPEG Y, Cb, Cr
- Edge mapa (binárna)
- Suprapixel mapa (binárna)

Podrobná špecifikácia je v `SPEC.md`.

---

## Licencia
Repozitár je zatiaľ súkromný.  
Licencia bude pridaná po zverejnení (pravdepodobne MIT).
## Naming Standard (EN + SK)

### English
SGCU is the main name of the algorithm and the entire technology family.  
Suffix letters define specific formats, modules, or variants.

- SGCU = core algorithm and brand
- SGCUF = SGCU File Format (current format)
- SGCUL = SGCU Lossless Format
- SGCUX = SGCU Experimental Format
- SGCUH = SGCU Hybrid Format
- SGCU‑E = SGCU Edge‑Enhanced algorithm variant
- SGCU‑S = SGCU Suprapixel variant

The suffix is not permanent. It changes depending on the module or format being developed.

### Slovak
SGCU je hlavný názov algoritmu a celej technologickej rodiny.  
Písmená na konci určujú konkrétny formát, modul alebo variant.

- SGCU = základný algoritmus a značka
- SGCUF = SGCU súborový formát (aktuálny formát)
- SGCUL = SGCU bezstratový formát
- SGCUX = SGCU experimentálny formát
- SGCUH = SGCU hybridný formát
- SGCU‑E = SGCU variant so zvýraznenými hranami
- SGCU‑S = SGCU suprapixelový variant

Sufix nie je trvalý. Mení sa podľa toho, čo sa práve vyvíja.
