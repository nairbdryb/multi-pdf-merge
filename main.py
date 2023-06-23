import os
import sys
from PyPDF2 import PdfMerger

def combine_pdfs(input_file, output_file):
    merger = PdfMerger()

    with open(input_file, 'r') as file:
        pdf_files = file.read().splitlines()

        for pdf_file in pdf_files:
            if os.path.isfile(pdf_file):
                merger.append(pdf_file)
            else:
                print(f"Error: PDF file '{pdf_file}' does not exist.")

    merger.write(output_file)
    merger.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python combine_pdfs.py <input_file.txt> <output_file.pdf>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]

        if not os.path.isfile(input_file):
            print(f"Error: Input file '{input_file}' does not exist.")
        else:
            combine_pdfs(input_file, output_file)
            print(f"PDF files combined successfully. Output saved as '{output_file}'.")
