# SGCUF Roadmap  
*(English + Slovak version)*

# English Version

## 1. Completed
- Core SGCUF format defined (v1)
- Basic SGCU logic (edges + suprapixels)
- YCbCr conversion pipeline
- JPEG channel compression
- SGCUF encoder and decoder
- Full binary specification (SPEC.md)
- Test scripts for encoding/decoding
- Dual‑language documentation (README, SPEC)
- MIT License (EN + SK)

---

## 2. In Progress
- Refinement of suprapixel threshold logic
- Improved hybrid reconstruction
- Internal validation of edge/supra maps
- SGCUF integrity checking tools

---

## 3. Planned for v1.1
- Optional RLE compression for edge maps
- Optional delta compression for suprapixel maps
- Cleaner separation of SGCU logic vs. SGCUF I/O
- Command‑line interface (CLI)
- Basic performance benchmarks

---

## 4. Planned for v2.0
- Chunk‑based SGCUF structure (extensible blocks)
- Support for 16‑bit images
- Multi‑resolution suprapixel layers
- Optional lossless mode
- Metadata extensions (author, creation time, parameters)

---

## 5. Long‑term Vision
SGCUF aims to combine:
- structural information (edges, suprapixels),
- classical compression (JPEG),
- and future SGCU‑based enhancements.

Goal: a compact, interpretable, extensible hybrid image format.

------------------------------------------------------------

# Slovenská verzia

## 1. Hotové
- Definovaný základný SGCUF formát (v1)
- Základná SGCU logika (edges + suprapixely)
- YCbCr konverzný pipeline
- JPEG kompresia kanálov
- SGCUF enkóder a dekóder
- Kompletná binárna špecifikácia (SPEC.md)
- Testovacie skripty pre encode/decode
- Dvojjazyčná dokumentácia (README, SPEC)
- MIT licencia (EN + SK)

---

## 2. Prebieha
- Spresnenie prahov pre suprapixely
- Vylepšená hybridná rekonštrukcia
- Interná validácia edge/supra máp
- Nástroje na kontrolu integrity SGCUF súborov

---

## 3. Plánované pre v1.1
- Voliteľná RLE kompresia edge máp
- Voliteľná delta kompresia suprapixelov
- Čistejšie oddelenie SGCU logiky od SGCUF I/O
- Command‑line rozhranie (CLI)
- Základné benchmarky výkonu

---

## 4. Plánované pre v2.0
- Chunk‑based SGCUF štruktúra (rozšíriteľné bloky)
- Podpora 16‑bitových obrázkov
- Multi‑rezolučné suprapixelové vrstvy
- Voliteľný bezstratový režim
- Rozšírené metadata (autor, čas vytvorenia, parametre)

---

## 5. Dlhodobá vízia
SGCUF má spájať:
- štrukturálne informácie (edges, suprapixely),
- klasickú kompresiu (JPEG),
- a budúce SGCU‑založené vylepšenia.

Cieľ: kompaktný, interpretovateľný a rozšíriteľný hybridný obrazový formát.
