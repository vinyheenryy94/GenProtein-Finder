# GenProtein-Finder

Welcome to GenProtein Finder! - https://doi.org/10.5281/zenodo.17179914

A Python tool for analyzing protein distribution across multiple genomes, enabling bidirectional searches and comparative genomics analysis.

## 📋 Features

- **Genome-to-Protein Search**: Find all proteins present in a specific genome
- **Protein-to-Genome Search**: Identify which genomes contain a specific protein
- **Occurrence Statistics**: Analyze protein distribution and identify shared proteins across genomes
- **Partial Name Matching**: Search genomes using partial names (e.g., "GCA_")
- **Interactive Menu**: User-friendly command-line interface

## 🚀 Getting Started

### Prerequisites

- Python 3.6+
- pandas
- openpyxl (for Excel file support)

### Installation

Install required dependencies:

```bash
pip install pandas openpyxl
````
### Input Data Format

The script expects an Excel file with the following structure:

- **Columns 1-3**: Metadata (ignored by the script)
- **Columns 4+**: Each column represents a genome, containing protein names
- Protein names should be listed in each genome column
- Empty cells are automatically handled

Example:

| Meta1 | Meta2 | Meta3 | GCA_000001.1 | GCA_000002.1 | GCA_000003.1 |
|-------|-------|-------|--------------|--------------|--------------|
| ...   | ...   | ...   | CP000360.1_737 | CP000360.1_737 | CP000455.1_123 |
| ...   | ...   | ...   | CP000360.1_891 | CP000455.1_123 | CP000360.1_737 |

## 🔧 Usage

1. If you are using Linux and running from the terminal, give execution permission to the script:

```
chmod +x genprotein_finder.py
```
2. Update the file path in the script:

```python
excel_file = "path/to/your/excel/file.xlsx"
```
3. Run
```
python3 genprotein_finder.py
```

## 📞 Contact

Vinicius Henrique de Oliveira Franzote - vinicius.henrique@unesp.br  
