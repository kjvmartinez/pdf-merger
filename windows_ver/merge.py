import sys
from PyPDF2 import PdfMerger as pdfM
import glob
import os
from datetime import datetime

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

    merger = pdfM()
    for i in files:
        merger.append(i)
    merger.write(filename)
    return len(merger.pages)


def main():
    '''
    Merge pdf files in not empty folders and save it as output.pdf
    '''
    now = datetime.now()

    folder_path = input("Enter path of parent folder:")
    if not folder_path.endswith(os.path.sep):
        folder_path += os.path.sep
    
    file_path = f"{folder_path}{now.strftime('%Y%m%d_%H%M%S')} merge details.txt"
    
    print(file_path)

    f = open(file_path, "w")

    roots_not_empty = scan_folders(folder_path)
    print(roots_not_empty)

    for folder in roots_not_empty:
        str_path = os.path.join(folder, '**/*.pdf')  # Use os.path.join for paths
        print(f"Merging files in {folder}")
        files = glob.glob(str_path, recursive=True)
        number_of_pages = merge_pdf(files, os.path.join(folder, 'output.pdf'))
        if number_of_pages > 0:
            f.write(f"{folder}\n{number_of_pages} pages" + '\n')
            print(f"Merged files in {folder} [DONE]")
        else:
            print(f"No merging done for {folder}")
    
    f.close()

if __name__ == "__main__":
    main()
