import sys
import csv
from tabulate import tabulate

def main():
    # Check command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    
    # Check if file is CSV file
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    
    # Try to open and read the CSV file
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            data = list(reader)
    except FileNotFoundError:
        sys.exit("File does not exist")
    
    # Check if data exists
    if not data:
        sys.exit("File is empty")
    
    # Get headers and rows
    headers = data[0]
    rows = data[1:]
    
    # Print table using tabulate with grid format
    print(tabulate(rows, headers, tablefmt="grid"))

if __name__ == "__main__":
    main()
