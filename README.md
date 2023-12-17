# Measles Susceptibility Genomic Analysis

This repository contains scripts and datasets for analyzing genomic data related to measles susceptibility. The analysis pipeline includes conversion of VCF files to matrix format, population mapping, and PCA analysis.

## Directory Structure

- `code/`
  - `vcf_to_matrix.py`: Script to convert VCF files into a matrix format.
  - `population_map.ipynb`: Jupyter Notebook for mapping population data.
  - `pca.ipynb`: Jupyter Notebook for performing PCA on genomic data.
- `data/`
  - Genomic data sourced from GWAS, the 1000 Genomes Project, etc.
  - Data include variants or SNPs associated with measles susceptibility.
  - VCF format datasets of samples with variants filtered for measles-associated ones.
- `matrix/`
  - Output files from `vcf_to_matrix.py`, used for PCA analysis.
- `ensembl/`
  - Data extracted from the Ensembl database.
- `haploreg/`
  - Data extracted from the HaploReg database.

## Data Sources

- GWAS
- 1000 Genomes Project
- Ensembl
- HaploReg

## Requirements

- Python 3.x
- Jupyter Notebook
- Additional Python libraries as required by the scripts and notebooks (e.g., pandas, scikit-learn, matplotlib, pysam).

## Contributing

Contributions to the project are welcome. Please fork the repository and submit a pull request with your changes.
