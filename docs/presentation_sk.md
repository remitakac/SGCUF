# SGCUF v1.0  
### Štruktúrna kompresia obrazu — nový hybridný formát

---

## SLIDE 1 — Názov
**SGCUF v1.0**  
Štruktúrna kompresia obrazu — nový hybridný formát

---

## SLIDE 2 — Problém
### Problém dnešných formátov
- komprimujú pixely, nie štruktúru  
- hrany sa rozmazávajú  
- suprapixely sa strácajú  
- technické obrázky trpia artefaktmi  
- mapy, UI a schémy strácajú čitateľnosť  

---

## SLIDE 3 — Čo je SGCU
### SGCU = algoritmus
SGCU analyzuje obraz ako:
- hrany  
- suprapixely  
- farebné vrstvy  
- štruktúrne vzťahy  

SGCU = *ako obraz chápeme*.

---

## SLIDE 4 — Čo je SGCUF
### SGCUF = súborový formát
Obsahuje:
- SGCU hrany  
- SGCU suprapixely  
- YCbCr kanály  
- JPEG kompresiu  
- metadáta  
- štruktúrny header  

---

## SLIDE 5 — Prečo to funguje
Tradičné formáty:  
→ „Ako uložiť pixely?“

SGCUF:  
→ „Ako uložiť štruktúru?“

Výsledok:
- ostrejšie hrany  
- presnejšie tvary  
- menej artefaktov  
- lepšia čitateľnosť  

---

## SLIDE 6 — Pipeline
1. RGB → YCbCr  
2. Detekcia hrán  
3. Suprapixelová segmentácia  
4. JPEG kompresia  
5. Uloženie štruktúrnych vrstiev  
6. Zbalenie do SGCUF  

---

## SLIDE 7 — Použitie
- mapy  
- UI prvky  
- technické výkresy  
- schémy  
- textúry  
- vizualizácie  

---

## SLIDE 8 — Stav projektu
### SGCUF v1.0 — hotové
- encoder  
- decoder  
- špecifikácia  
- testy  
- príklady  
- dokumentácia  
- naming standard  
- verejný release  

---

## SLIDE 9 — Roadmapa
- RLE pre edge mapy  
- delta kompresia suprapixelov  
- CLI nástroj  
- optimalizácia rýchlosti  
- experimentálne varianty  

