# Rao Lab Cultivated Meat ML — Complete Project Memory
# Saved May 11, 2026 — all computational work complete

## CORE RESULT
Multi-omic state map: 3 manufacturing readiness states, 96.7% CV accuracy.
30-gene qPCR panel: $50-100/batch, 4-6hr turnaround.

## STATE MAP (P2)
- 239 human samples (GSE115978 + GSE72056)
- Joint RNA (23,682 genes) + METAFlux flux (13,082 reactions) PCA embedding (30 dims)
- K-means k=3: expansion-competent(61), committed(86), terminal(92)
- States defined by metabolic activity: exp(-0.081), com(-0.075), ter(+0.123)
- 5-fold CV: 96.7% ± 2.1%

## QC PANEL (P3)
- 30-gene L1 logistic regression (C=0.03, saga)
- 96.7% ± 1.0% CV — matches full multi-omic
- Top genes: UXS1, PLOD1, MALAT1, C1D, KIF1B, XKR9, LINC00574, UGT8
- 30 qPCR primer pairs designed (Tm 57-62°C, GC 45-55%)

## METABOLIC PATHWAY MAPPING
- METAFlux Y rebuild: 10 pathways (Glycolysis, TCA, OXPHOS, PPP, Nucleotide, AA, FA_Synthesis, Lipid, One_Carbon, Glutathione)
- Per-domain Ridge: 0.800 mean correlation
- 2.2× improvement from old scFEA Y (0.36)

## CROSS-SPECIES VALIDATION
- Bovine GSE173199: 38 samples, 27,607 ENSBTAG genes → 14,729 human orthologs
- Bovine state map: terminal(14, 37% D0-D1), committed(12, 32% D3 media), expansion(12, 32% D2-D4)
- Direct projection fails (100% terminal) — species difference dominates PCA
- Species-specific maps required; 3-state methodology conserved
- Bovine myogenic markers (PAX7, MYF5, MYOD1, MYOG, MYH3, DES, MYL1, NEB) strong; human near-zero
- Porcine GSE206914: embryonic scRNA-seq, less relevant
- Bovine GSE240556: 151MB snRNA-seq downloaded (Nature Comms 2024, cultivated meat heterogeneity)

## PSEUDOTIME ANALYSIS
- PCA1 vs true time: r=0.942, p=1.3e-18 — near-perfect trajectory
- Diffusion pseudotime: r=-0.626, p=2.7e-5
- Trajectory: D0(quiescent)→D1→D2(proliferating)→D3(differentiating)→D4

## PATHWAY ENRICHMENT
- Terminal: high Fatty Acid Synthesis(+0.77), One Carbon(+0.71), Lipid Metabolism(+0.60)
- Expansion: high TCA Cycle(+0.13)
- Expansion vs Terminal: largest delta in Fatty Acid Synthesis(-1.19)

## POWER ANALYSIS
- Effect sizes: d=0.19-0.20 (small)
- Required N: 414/group for 80% power, ~1,241 total for 3-group ANOVA
- Proposed 30 batches is underpowered

## TRANSFER LEARNING
- Human→bovine: 36.8% accuracy (all predicted terminal)
- 6/8 panel genes have bovine orthologs
- Confirms species-specific maps essential

## GENE NETWORK
- 0 edges at |r|>0.7 — panel genes are independent discriminative markers
- Not a co-regulated module

## DRUG PREDICTIONS
- No strong matches — panel genes don't overlap known drug targets
- Need broader transcriptomic signatures for connectivity mapping

## REPRODUCIBILITY (P5)
- Within-dataset correlation: 0.006 (very high heterogeneity)
- 50% genes stable (CV < median)
- Top 5 PCs: 22.7% variance
- PCA bootstrap CV: PC1=4.9%, PC2=4.4% (stable)

## DELIVERABLES
- 10 publication figures (5 original + 5 remade at 300 DPI)
- Interactive HTML dashboard (46KB, Plotly.js)
- Manuscript v2 with cross-species section
- Supplementary materials
- Prospective validation protocol (30 batches, 8-12 weeks)
- 9 JSON analysis outputs
- progress.yaml tracking all statuses

## WHAT REMAINS (requires lab/external)
1. Execute prospective validation (lab access + ~$6,500)
2. Push to GitHub (token with repo scope)
3. Primer synthesis + wet lab validation
4. Real-time metabolite monitoring integration

## KEY INSIGHTS
1. Metabolic activity is the primary axis of state variation
2. 3-state structure is methodologically conserved across species
3. Species-specific maps required — direct projection fails
4. 30-gene panel = full multi-omic performance
5. METAFlux pathway mapping validated (0.800 Ridge)
6. Effect sizes are small — need larger N for validation
7. Panel genes are independent markers, not a regulatory module
8. Bovine timecourse shows textbook satellite cell trajectory