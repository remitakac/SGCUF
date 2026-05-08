# SGCUF — Format Specification  
*(English + Slovak version)*

# English Version

This document describes the binary structure of the SGCUF format (Suprapixel‑Gradient‑Contrast Unified Format).  
SGCUF combines suprapixel maps, edge maps, and JPEG‑compressed YCbCr channels into a single compact file.

---
## Naming Note (EN + SK)

### English
This document describes the SGCUF format.  
SGCU is the algorithm; SGCUF is the file container.  
Future formats may use different suffixes (e.g., SGCUL, SGCUX).

### Slovak
Tento dokument popisuje SGCUF formát.  
SGCU je algoritmus; SGCUF je súborový kontajner.  
Budúce formáty môžu používať iné sufixy (napr. SGCUL, SGCUX).
---
## 1. Magic Header

Every SGCUF file begins with the ASCII sequence:

SGCUFMT\n

Length: 8 bytes  
Purpose: format identification and basic validation.

---

## 2. Format Version

1 byte  
Current version: 1

---

## 3. Metadata Block

All values are stored in big‑endian order:

- width (4 bytes, uint32)
- height (4 bytes, uint32)
- T — edge threshold (1 byte, uint8)
- Q — JPEG quality (1 byte, uint8)

---

## 4. JPEG Section

Contains three independent JPEG bytestreams:

1. Y_channel_length (4 bytes)  
2. Y_channel_data (N bytes)

3. Cb_channel_length (4 bytes)  
4. Cb_channel_data (M bytes)

5. Cr_channel_length (4 bytes)  
6. Cr_channel_data (K bytes)

Each channel is encoded using a standard JPEG encoder.

---

## 5. Edge Map

Binary edge map, size width × height.

Stored as:

- edge_length (4 bytes)
- edge_data (edge_length bytes)

Each pixel is 0 or 1.

---

## 6. Suprapixel Map

Suprapixel ID map, size width × height.

Stored as:

- spx_length (4 bytes)
- spx_data (spx_length bytes)

Each pixel contains a suprapixel ID (uint16 or uint32 depending on implementation).

---

## 7. Section Order

1. Magic header  
2. Version  
3. Metadata  
4. JPEG Y  
5. JPEG Cb  
6. JPEG Cr  
7. Edge map  
8. Suprapixel map  

---

## 8. File Validation

A decoder must verify:

- correct magic header  
- supported version  
- consistent dimensions  
- valid block lengths  
- decodable JPEG sections  

---

## 9. Implementation Notes

- SGCUF does not compress edge/spx maps (yet).  
- JPEG quality Q applies to all three channels.  
- The format is designed to be extensible (versioning + block lengths).

---

## 10. Future Extensions

- delta compression for suprapixels  
- optional RLE compression for edge maps  
- support for 16‑bit images  
- version 2 with chunk‑based structure  

---

## 11. Binary Encoding Rules

### 11.1 Endianness
All multi‑byte values in SGCUF are stored in big‑endian order.

### 11.2 Data Types
- uint8  — 1 byte
- uint16 — 2 bytes
- uint32 — 4 bytes
- byte[] — raw data block

### 11.3 Row‑Major Ordering
All 2D maps (edge map, suprapixel map) are stored in row‑major order.

### 11.4 Block Structure
Each variable‑length block is stored as:
uint32 block_length
byte[block_length] block_data

---

# Slovenská verzia

Tento dokument popisuje binárnu štruktúru formátu SGCUF (Suprapixel‑Gradient‑Contrast Unified Format).  
SGCUF kombinuje suprapixelové mapy, edge mapy a JPEG kompresiu YCbCr kanálov do jedného kompaktného súboru.

---

## 1. Magic header

Každý SGCUF súbor začína ASCII sekvenciou:

SGCUFMT\n

Dĺžka: 8 bajtov  
Účel: identifikácia formátu a základná validácia.

---

## 2. Verzia formátu

1 bajt  
Aktuálna verzia: 1

---

## 3. Metadata blok

Hodnoty sú uložené v big‑endian poradí:

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

Každý kanál je komprimovaný štandardným JPEG encoderom.

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

Každý pixel obsahuje ID suprapixelu (uint16 alebo uint32).

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
- dekódovateľnosť JPEG sekcií  

---

## 9. Poznámky k implementácii

- SGCUF zatiaľ nekomprimuje edge/spx mapy.  
- JPEG kvalita Q sa aplikuje na všetky tri kanály.  
- Formát je navrhnutý tak, aby bol rozšíriteľný.

---

## 10. Budúce rozšírenia

- delta‑kompresia suprapixelov  
- voliteľná RLE kompresia edge mapy  
- podpora 16‑bitových obrázkov  
- verzia 2 s chunk‑based štruktúrou

---

## 11. Binárne pravidlá

### 11.1 Endianita
Všetky viacbajtové hodnoty sú uložené v big‑endian poradí.

### 11.2 Dátové typy
- uint8  — 1 bajt
- uint16 — 2 bajty
- uint32 — 4 bajty
- byte[] — surové dáta

### 11.3 Row‑major poradie
Všetky 2D mapy (edge mapa, suprapixel mapa) sú uložené v row‑major poradí.

### 11.4 Štruktúra blokov
Každý blok s premenlivou dĺžkou je uložený ako:
uint32 block_length
byte[block_length] block_data


