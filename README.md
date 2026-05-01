SGCUF je experimentálny hybridný obrazový formát založený na SGCU (Suprapixel‑Gradient‑Contrast Units) a JPEG kompresii.  
Cieľom je kombinovať:

- suprapixelové mapy (nízky kontrast),
- edge mapy (vysoký kontrast),
- JPEG kompresiu Y, Cb, Cr kanálov,

do jedného kompaktného binárneho formátu.

---

## 🔧 Štruktúra repozitára

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

## 🚀 Použitie

### Encode
python test_encode.py

Výstup:
output/real_test.sgcuf

### Decode
python test_decode.py

Výstup:
output/real_test_decoded.png

---

## 📦 Formát SGCUF (stručný popis)

- Magic header: `SGCUFMT\n`
- Version: 1
- Metadata: rozmery, T, Q
- JPEG Y, Cb, Cr
- Edge mapa (binárna)
- Suprapixel mapa (binárna)

Podrobná špecifikácia bude doplnená neskôr.

---

## 📄 Licencia
Repozitár je zatiaľ súkromný.  
Licencia bude pridaná po zverejnení (pravdepodobne MIT).
