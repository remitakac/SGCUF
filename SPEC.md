# SGCUF — Špecifikácia formátu

Tento dokument popisuje binárny formát SGCUF (Suprapixel‑Gradient‑Contrast Unified Format), ktorý kombinuje suprapixelové mapy, edge mapy a JPEG kompresiu YCbCr kanálov do jedného súboru.

---

## 1. Magic header

Každý SGCUF súbor začína ASCII sekvenciou:

SGCUFMT\n

Dĺžka: 8 bajtov  
Účel: identifikácia formátu a jednoduchá validácia.

---

## 2. Verzia formátu

1 bajt  
Aktuálna verzia: 1

---

## 3. Metadata blok

Nasledujúce hodnoty sú uložené v big‑endian poradí:

- width (4 bajty, uint32)
- height (4 bajty, uint32)
- T – prah pre edge mapu (1 bajt, uint8)
- Q – JPEG kvalita (1 bajt, uint8)

---

## 4. JPEG sekcia

Obsahuje tri samostatné JPEG bytestreamy:

1. Y_channel_length (4 bajty)
2. Y_channel_data (N bajtov)

3. Cb_channel_length (4 bajty)
4. Cb_channel_data (M bajtov)

5. Cr_channel_length (4 bajty)
6. Cr_channel_data (K bajtov)

Každý kanál je komprimovaný samostatne pomocou štandardného JPEG encoderu.

---

## 5. Edge mapa

Binárna mapa hrán, veľkosť width × height.

Uloženie:

- edge_length (4 bajty)
- edge_data (edge_length bajtov)

Každý pixel je 0 alebo 1.

---

## 6. Suprapixel mapa

Mapa suprapixelov, veľkosť width × height.

Uloženie:

- spx_length (4 bajty)
- spx_data (spx_length bajtov)

Každý pixel obsahuje ID suprapixelu (uint16 alebo uint32 podľa implementácie).

---

## 7. Poradie sekcií v súbore

1. Magic header  
2. Version  
3. Metadata  
4. JPEG Y  
5. JPEG Cb  
6. JPEG Cr  
7. Edge mapa  
8. Suprapixel mapa  

---

## 8. Validácia súboru

Dekóder musí overiť:

- správny magic header  
- podporovanú verziu  
- konzistentné rozmery  
- dĺžky dátových blokov  
- že JPEG sekcie sú dekódovateľné  

---

## 9. Poznámky k implementácii

- SGCUF neobsahuje žiadnu kompresiu pre edge/spx mapy (zatiaľ).  
- JPEG kvalita Q sa aplikuje rovnako na všetky tri kanály.  
- Formát je navrhnutý tak, aby bol rozšíriteľný (verzia + dĺžky blokov).

---

## 10. Budúce rozšírenia

- delta‑kompresia suprapixelov  
- voliteľná RLE kompresia edge mapy  
- podpora 16‑bitových obrázkov  
- verzia 2 s chunk‑based štruktúrou

