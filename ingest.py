import sys
import csv

def read_observations(filename):
    """ Read Observations CSV and collect unique taxonomic orders from a specified column """
    observed_species = set()
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                observed_species.add(row["Taxonomic Order"])
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        sys.exit(1)
    return observed_species

def find_matches_and_spuh(taxonomy_filename, observed_species):
    """ Find matching lines and then check for the next 'spuh' lines """
    try:
        with open(taxonomy_filename, mode='r', newline='', encoding='utf-8') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                taxonomic_order = line.split(',')[0]
                if taxonomic_order in observed_species:
                    print(line.strip())  # Print the matching line
                    # Skip to the first 'spuh' line after the match
                    found_spuh = False
                    for j in range(i+1, len(lines)):
                        if 'spuh' in lines[j]:
                            print(lines[j].strip())
                            found_spuh = True
                            # Continue to print 'spuh' lines until a non-'spuh' line is encountered
                            k = j + 1
                            while k < len(lines) and 'spuh' in lines[k]:
                                print(lines[k].strip())
                                k += 1
                            break
                    if not found_spuh:
                        print("No 'spuh' found following the observed species.")
    except Exception as e:
        print(f"Error reading {taxonomy_filename}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_csv_file> <taxonomy_csv_file>")
        sys.exit(1)

    input_csv_file = sys.argv[1]
    taxonomy_csv_file = 'eBird-Clements-v2023-integrated-checklist-October-2023.csv'

    # Get unique taxonomic orders from the input CSV
    observed_species = read_observations(input_csv_file)

    # Find and print matching taxonomic orders from the taxonomy CSV
    find_matches_and_spuh(taxonomy_csv_file, observed_species)
