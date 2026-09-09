from pathlib import Path
import nbformat

# Folder where this script is located
NOTEBOOK_FOLDER = Path(__file__).parent

# Find all notebooks
notebook_files = list(NOTEBOOK_FOLDER.glob("*.ipynb"))

# Remove this script's output notebook if necessary
print(f"Found {len(notebook_files)} notebooks")

if not notebook_files:
    print("ERROR: No notebooks found!")
    print(f"Looking in: {NOTEBOOK_FOLDER}")
else:
    # Save output in the main project folder
    PROJECT_FOLDER = NOTEBOOK_FOLDER.parent
    output_file = PROJECT_FOLDER / "all_notebook_code.txt"

    with open(output_file, "w", encoding="utf-8") as output:

        for notebook_file in notebook_files:
            print(f"Processing: {notebook_file.name}")

            output.write("\n")
            output.write("=" * 80 + "\n")
            output.write(f"NOTEBOOK: {notebook_file.name}\n")
            output.write("=" * 80 + "\n\n")

            notebook = nbformat.read(notebook_file, as_version=4)

            code_count = 0

            for cell in notebook.cells:
                if cell.cell_type == "code":
                    output.write(cell.source)
                    output.write("\n\n")
                    code_count += 1

            print(f"  Extracted {code_count} code cells")

    print("\nDone!")
    print(f"Output saved to: {output_file}")