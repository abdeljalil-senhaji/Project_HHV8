# 🧬 Project_HHV8
[![Documentation](https://img.shields.io/badge/Documentation-github-brightgreen.svg?style=for-the-badge)](https://github.com/abdeljalil-senhaji/Project_HHV8)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Project_HHV8** (Viral RNA-seq Study) is a bioinformatics project focused on the analysis of RNA-seq data targeting viral gene expression, particularly from HHV-8, using high-throughput sequencing data.

---

## 📁 Project Structure
Project_VRS/
├── data/ # Raw data (FASTQ, genomes, annotations)
├── results/ # Alignment results (BAM, counts, PCA, DEG)
├── scripts/ # Analysis scripts (Python, R, Snakemake)
├── notebooks/ # Jupyter Notebooks for exploratory analysis
├── reports/ # Analysis reports, figures
├── README.md 
└── Snakefile # Snakemake pipeline

---

## 🛠 Technologies Used

- **STAR**: RNA-seq alignment and gene quantification
- **featureCounts**: Read counting per gene
- **DESeq2** (R) or **pyDESeq2** (Python): Differential expression analysis
- **PCA, heatmap, clustering**: Data visualization
- **Jupyter Notebook / RStudio**: Interactive analysis
- **Snakemake**: Pipeline management

---

## 📌 Goals

This project aims to:
- Analyze viral gene expression (e.g., HHV-8) from RNA-seq data
- Compare expression levels across samples
- Identify differentially expressed genes (DEGs)
- Visualize the global structure of the data (PCA, heatmap)
- Build a **reproducible pipeline** for viral RNA-seq analysis

---

## 🧪 Analysis Highlights

- RNA-seq alignment using **STAR**
- Gene counting with **featureCounts**
- Data normalization: `logCPM`, `RPKM`, `VST`, `rlog`
- Visualization: **PCA**, heatmap, clustering
- Differential expression analysis (if experimental groups are defined)
- Exploration of viral genes (e.g., **LANA**)

---

## 📦 Dependencies

### Python environment:
```bash
pandas numpy matplotlib seaborn scikit-learn pydeseq2 jupyter
```
## 📨 Contact

👤 Abdeljalil Senhaji Rachik
📧 senhajirachikabdeljalil@gmail.com
🐙 GitHub