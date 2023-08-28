import sys
from PyPDF2 import PdfMerger as pdfM
import glob
import os

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
        './{}/{}'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri A')),
        # ... Add other paths for KRA I criteria
    ]

    KRA_II = [
        './{}/{}'.format(kra2_dictionary.get('level 0'), kra2_dictionary.get('Cri A')),
        # ... Add other paths for KRA II criteria
    ]

    for path in KRA_I:
        os.makedirs(path)

    for path in KRA_II:
        os.makedirs(path)

def scan_folders():
    KRAs = ['./KRA I', './KRA II']
    list_roots = []
        
    for folder in KRAs:
        for (root, dirs, files) in os.walk(folder, topdown=True):
            if not any(f.endswith('.pdf') for f in files):
                continue
            list_roots.append(root)
    return list_roots

def main():
    '''
    Create directories.
    ''' 
    create_dirs()
   
    '''
    Merge pdf files in not empty folders and save it as output.pdf
    '''
    # roots_not_empty = scan_folders()
    # for folder in roots_not_empty:
    #     str_path = f"{folder}/**/*.pdf"
    #     print(f"Merging files in {folder}")
    #     files = glob.glob(str_path, recursive=True)
    #     merge_pdf(files, f"{folder}/output.pdf")
    #     print(f"Merged files in {folder} [DONE]")

if __name__ == "__main__":
    main()
