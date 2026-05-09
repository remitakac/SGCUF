# SGCUF Pipeline Architecture
## Version 1.0.0

Tento dokument definuje kompletný, deterministický pipeline pre SGCUF formát. Pipeline je univerzálny, nezávislý od vstupného formátu a pozostáva z presne definovaných krokov pre enkódovanie a dekódovanie. Všetky kroky sú sekvenčné, modulárne a rozšíriteľné.

## 1. Encode Pipeline (RGB → SGCUF)

### 1.1 Load Input Image
Vstupom môže byť ľubovoľný podporovaný obrazový formát (JPEG, PNG, WebP, TIFF, BMP).  
Výstupom je RGB matica typu uint8 s rozmermi H × W × 3.

### 1.2 Pad to Even Dimensions
Ak je šírka alebo výška nepárna, posledný riadok/stĺpec sa duplikuje.  
Výstupom je RGB obraz s rozmermi padded_H × padded_W a pôvodné rozmery orig_H × orig_W.

### 1.3 Convert RGB → YCbCr
RGB obraz sa prevedie na tri luminančno‑chrominančné kanály Y, Cb, Cr.  
Výstupom sú tri 2D matice typu uint8.

### 1.4 Structural Analysis (Edges, Suprapixels)
Z Y kanála sa vypočítajú:
- edge mapa (uint8)
- suprapixel mapa (uint8)

Obe majú rozmer padded_H × padded_W.

### 1.5 JPEG Compression of Y, Cb, Cr
Každý kanál sa komprimuje samostatne pomocou JPEG pri kvalite Q.  
Výstupom sú tri bytestreamy: Y_jpeg, Cb_jpeg, Cr_jpeg.

### 1.6 Compute Segment Lengths
Získajú sa dĺžky:
- LEN_Y
- LEN_CB
- LEN_CR
- LEN_EDGE = padded_H × padded_W
- LEN_SUPRA = padded_H × padded_W

### 1.7 Build SGCUF Header
Hlavička obsahuje:
- MAGIC = "SGCUFMT\n"
- VERSION
- ORIG_WIDTH, ORIG_HEIGHT
- PADDED_WIDTH, PADDED_HEIGHT
- T (threshold)
- Q (JPEG quality)
- RESERVED = 0

### 1.8 Write Segment Length Table
Zapíšu sa dĺžky všetkých segmentov v poradí:
LEN_Y, LEN_CB, LEN_CR, LEN_EDGE, LEN_SUPRA.

### 1.9 Write Payloads
V poradí:
1. JPEG Y
2. JPEG Cb
3. JPEG Cr
4. Edge mapa (raw uint8)
5. Suprapixel mapa (raw uint8)

Výsledkom je kompletný SGCUF súbor.

---

## 2. Decode Pipeline (SGCUF → RGB)

### 2.1 Read File and Verify MAGIC
Načítajú sa všetky dáta a overí sa MAGIC.

### 2.2 Parse Header
Z hlavičky sa načítajú:
VERSION, ORIG_WIDTH, ORIG_HEIGHT, PADDED_WIDTH, PADDED_HEIGHT, T, Q.

### 2.3 Parse Segment Lengths
Načítajú sa hodnoty LEN_Y, LEN_CB, LEN_CR, LEN_EDGE, LEN_SUPRA.

### 2.4 Extract Payloads
Z dát sa vyrežú:
- Y_jpeg
- Cb_jpeg
- Cr_jpeg
- edge mapa (raw)
- suprapixel mapa (raw)

### 2.5 Reconstruct Structural Maps
Edge a suprapixel mapy sa prevedú na 2D matice typu uint8.

### 2.6 JPEG Decompression
Každý kanál sa dekomprimuje:
Yd, Cbd, Crd.

### 2.7 Convert YCbCr → RGB
Získaný je RGB obraz s rozmermi padded_H × padded_W.

### 2.8 Crop to Original Size
Obraz sa oreže na orig_H × orig_W.  
Výstupom je finálny RGB obraz.

---

## 3. Pipeline Properties

### Deterministic
Každý krok má jednoznačný vstup a výstup.  
Pipeline neobsahuje žiadne náhodné operácie.

### Modular
Každý krok je samostatný modul, ktorý možno nahradiť bez zmeny ostatných krokov.

### Extensible
Pipeline umožňuje budúce rozšírenia:
- ďalšie štrukturálne vrstvy
- alternatívne kompresné metódy
- metadáta
- validačné bloky

### Format‑Independent Input
Pipeline je nezávislý od vstupného formátu.  
Všetky vstupy sa konvertujú na RGB a pipeline pokračuje jednotne.

---

## 4. Summary

SGCUF pipeline definuje kompletný tok dát od vstupného obrazu po binárny SGCUF súbor a späť.  
Je deterministický, modulárny, rozšíriteľný a nezávislý od vstupného formátu.  
Tento dokument slúži ako architektonický základ pre implementáciu, validáciu a budúci vývoj SGCUF systému.
