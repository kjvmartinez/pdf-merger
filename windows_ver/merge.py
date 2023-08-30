import sys
from PyPDF2 import PdfMerger as pdfM
import glob
import os
from datetime import datetime
from PyPDF2 import PdfMerger
import time

# Define the create_dirs function before it's used in the main function
# def scan_folders(fpath):
#     KRAs = [f'{fpath}/KRA I', f'{fpath}/KRA II',f'{fpath}/KRA III', f'{fpath}/KRA IV']  # Added missing slashes
#     list_roots = []
        
#     for folder in KRAs:
#         for (root, dirs, files) in os.walk(folder, topdown=True):
#             if not any(f.endswith('.pdf') for f in files):
#                 continue
#             list_roots.append(root)
#     return list_roots


def scan_folders(root_directory):
    list_roots = []
    
    for (root, dirs, files) in os.walk(root_directory, topdown=True):
        if any(f.endswith('.pdf') for f in files):
            list_roots.append(root)
    
    return list_roots

def merge_pdf(files, filename):
    if len(files) == 1:  # If there's only one PDF file, skip merging
        print(f"Skipping merge for {filename} as there's only one PDF file.")
        return 0

    merger = PdfMerger()
    for pdf_file in files:
        merger.append(pdf_file)
        
        # merger.append(i)
    merger.write(filename)
    num_pages = len(merger.pages)
    merger.close()
    return num_pages


def main():
    '''
    Merge pdf files in not empty folders and save it as output.pdf
    '''
    # Record the start time
    start_time = time.time()

    now = datetime.now()

    folder_path = input("Enter path of parent folder:")
    if not folder_path.endswith(os.path.sep):
        folder_path += os.path.sep
    
    file_path = f"{folder_path}{now.strftime('%Y%m%d_%H%M%S')} merge details.txt"

    f = open(file_path, "w", encoding='utf-8')

    roots_not_empty = scan_folders(folder_path)
    total_pages = 0
    for folder in roots_not_empty:
        str_path = os.path.join(folder, '*.pdf')  # Use os.path.join for paths
        # print(f"Merging files in {folder}")
        files = glob.glob(str_path, recursive=True)
        number_of_pages = merge_pdf(files, os.path.join(folder, 'output.pdf'))
        if number_of_pages > 0:
            f.write(f"📁 {folder} {number_of_pages} pages" + '\n')
            total_pages += number_of_pages
            print(f"📄 Merged files in {folder}")
        else:
            print(f"No merging done for {folder}")
    
    f.close()

    # Record the end time
    end_time = time.time()
    
    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Print the elapsed time
    print(f"Elapsed time: {elapsed_time:.6f} seconds Total Pages: {total_pages}")





if __name__ == "__main__":
    main()
