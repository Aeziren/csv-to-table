import sys
from csv import DictReader
from tabulate import tabulate

def main():
    # Argument Handling
    if len(sys.argv) != 2:
        sys.exit(r"Usage: python pizza.py path/to/file.csv")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Path must be to a .csv file")

    # Tabulate csv file and print
    try:
        with open(sys.argv[1]) as file:
            reader = DictReader(file)
            print(tabulate(reader, tablefmt="grid", headers="keys"))

    except FileNotFoundError:
        sys.exit("File not found")

if __name__ == "__main__":
    main()