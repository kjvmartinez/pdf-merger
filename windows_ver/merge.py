import sys
from PyPDF2 import PdfMerger as pdfM
import glob
import os
from datetime import datetime

# Define the create_dirs function before it's used in the main function
def scan_folders(fpath):
    KRAs = [f'{fpath}/KRA I', f'{fpath}/KRA II']  # Added missing slashes
    list_roots = []
        
    for folder in KRAs:
        for (root, dirs, files) in os.walk(folder, topdown=True):
            if not any(f.endswith('.pdf') for f in files):
                continue
            list_roots.append(root)
    return list_roots



def create_dirs():
    kra1_dictionary = {
        'level 0': 'KRA I',
        'Cri A': 'CRITERION A Teaching Effectiveness',
        'Cri B': 'CRITERION B Curriculum and Instructional Materials Developed',
        'Cri C': 'CRITERION C Special Projects, Capstone Projects, Thesis, Dissertation, and Mentorship Services',
    }

    kra2_dictionary = {
        'level 0': 'KRA II',
        'Cri A': 'CRITERION A Research, Innovation, and Creative Work',
        'Cri B': 'CRITERION B Inventions',
        'Cri C': 'CRITERION C Creative Works',
    }

    KRA_I = [
        os.path.join(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri A')),
        # ... Add other paths for KRA I criteria
    ]

    KRA_II = [
        os.path.join(kra2_dictionary.get('level 0'), kra2_dictionary.get('Cri A')),
        # ... Add other paths for KRA II criteria
    ]

    for path in KRA_I:
        os.makedirs(path, exist_ok=True)

    for path in KRA_II:
        os.makedirs(path, exist_ok=True)

# ... (other code remains the same)

def merge_pdf(files, filename):
    if len(files) == 1:  # If there's only one PDF file, skip merging
        print(f"Skipping merge for {filename} as there's only one PDF file.")
        return 0

    merger = pdfM()
    for i in files:
        merger.append(i)
    merger.write(filename)
    return len(merger.pages)

# ... (other code remains the same)

def main():
    '''
    Create directories.
    '''
    create_dirs()
   
    '''
    Merge pdf files in not empty folders and save it as output.pdf
    '''
    now = datetime.now()

    folder_path = input("Enter path of folders:")
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
