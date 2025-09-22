import pandas as pd

# Path Excel file
excel_file = "insert/your/path/"

# Load the spreadsheet
df = pd.read_excel(excel_file) #csv = df - pd.read_csv(excel_file)

# Create the dictionaries
genome_proteins = {}
protein_genomes = {}

for coluna in df.columns[3:]:
    proteinas = df[coluna].dropna().tolist()
    genome_proteins[coluna] = proteinas
    for proteina in proteinas:
        if proteina not in protein_genomes:
            protein_genomes[proteina] = []
        protein_genomes[proteina].append(coluna)

# Menu
while True:
    print("\n--- Welcome to GenProtein Finder ---")

    print("\n--- MENU ---")
    print("1 - Search proteins by genome")
    print("2 - Search genomes by protein")
    print("3 - Show occurrence statistics")
    print("4 - Exit")

    opcao = input("Choose an option: ")

    if opcao == "1":
        nome_genoma = input("Enter the genome name (partial or complete) (e.g., GCA_...): ")

        # Partial search by genome
        matches = [k for k in genome_proteins if nome_genoma in k]

        if matches:
            for match in matches:
                print(f"\nGenome '{match}' contains {len(genome_proteins[match])} proteins:")
                for p in genome_proteins[match]:
                    print(" -", p)
        else:
            print("Genome not found.")

    elif opcao == "2":
        nome_proteina = input("Enter the protein name (ex: CP000360.1_737): ")
        if nome_proteina in protein_genomes:
            print(f"\nProtein '{nome_proteina}' found in {len(protein_genomes[nome_proteina])} genomes:")
            for g in protein_genomes[nome_proteina]:
                print(" -", g)
        else:
            print("Protein not found.")

    elif opcao == "3":
        print("\n=== Statistics ===")

        # 1. Shared proteins (present in more than one genome)
        print("\n2. Shared proteins (present in >1 genome) and their genomes: ")
        compartilhadas = {p: g for p, g in protein_genomes.items() if len(g) > 1}

        if not compartilhadas:
            print("No shared proteins found.")
        else:
            # Sort by number of genomes (descending) and then by protein name
            for proteina, genomas in sorted(compartilhadas.items(),
                                          key=lambda x: (-len(x[1]), x[0])):
                print(f"\nProtein: {proteina}")
                print(f"Total genomes: {len(genomas)}")
                print("Genomes where it appears:")
                for genoma in sorted(genomas):
                    print(f" - {genoma}")

    elif opcao == "4":
        print("EXIT...")
        break
    else:
        print("Invalid option. Try again.")
