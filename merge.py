import sys
from PyPDF2 import PdfMerger as pdfM

import glob
import os
from datetime import datetime

''''
Create all directories and subdirectories.
'''
def create_dirs():
    kra1_dictionary = {
        'level 0' : 'KRA I',
        'Cri A' : 'CRITERION A Teaching Effectiveness',
        'Cri B' : 'CRITERION B Curriculum and Instructional Materials Developed',
        'Cri C' : 'CRITERION C Special Projects, Capstone Projects, Thesis, Dissertation, and Mentorship Services',
    }

    kra2_dictionary = {
        'level 0' : 'KRA II',
        'Cri A' : 'CRITERION A Research, Innovation, and Creative Work',
        'Cri B' : 'CRITERION B Inventions',
        'Cri C' : 'CRITERION C Creative Works',
    }
 

    KRA_I =[
        './{}/{}'.format(kra1_dictionary.get('level 0'),kra1_dictionary.get('Cri A')),
        './{}/{}/1.1.1	Student’s Evaluation'.format(kra1_dictionary.get('level 0'),kra1_dictionary.get('Cri A')),
        './{}/{}/1.1.2 Supervisor’s Evaluation'.format(kra1_dictionary.get('level 0'),kra1_dictionary.get('Cri A')),
        './{}/{}'.format(kra1_dictionary.get('level 0'),kra1_dictionary.get('Cri B')),
        './{}/{}/1.1.1 Sole Authorship'.format(kra1_dictionary.get('level 0'),kra1_dictionary.get('Cri B')),
        './{}/{}/1.1.2 Co-Authorship'.format(kra1_dictionary.get('level 0'),kra1_dictionary.get('Cri B')),
        './{}/{}/2 Academic Programs Developed or Revised and Implemented'.format(kra1_dictionary.get('level 0'),kra1_dictionary.get('Cri B')),
        './{}/{}'.format(kra1_dictionary.get('level 0'),kra1_dictionary.get('Cri C')),
        './{}/{}/1.1.1 Adviser'.format(kra1_dictionary.get('level 0'),kra1_dictionary.get('Cri C')),
        './{}/{}/1.1.2 Panel'.format(kra1_dictionary.get('level 0'),kra1_dictionary.get('Cri C')),
        './{}/{}/2 Services Rendered as Mentor'.format(kra1_dictionary.get('level 0'),kra1_dictionary.get('Cri C'))
        ]

    KRA_II =[
        './{}/{}'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A')),
        './{}/{}/1.1.1 Sole Authorship'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A')),
        './{}/{}/1.1.2 Co-Authorship'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A')),
        './{}/{}/2.2.1 Lead Researcher'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A')),
        './{}/{}/2.2.2 Contributor'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A')),
        './{}/{}/3.3.1 Local Authors'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A')),
        './{}/{}/3.3.2 International Authors'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A')),
        './{}/{}'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B')),
        './{}/{}/1.1.1	Invention Patents'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B')),
        './{}/{}/1.1.2	Utility Models and Industrial Design'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B')),
        './{}/{}/1.2.1 Local'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B')),
        './{}/{}/1.2.2 International'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B')),
        './{}/{}/2.1.1 New Software Products'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B')),
        './{}/{}/2.1.2 Updated Software Products'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B')),
        './{}/{}/2.2 New Plant Variety or Animal Breeds Development Microbial Stains Isolated that are propagated or reproduced'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B')),
        './{}/{}'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri C')),
        './{}/{}/1.1 New Creative Performing Artworks'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri C')),
        './{}/{}/1.2 Exhibition'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri C')),
        './{}/{}/1.3 Juried or Peer-Reviewed Designs'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri C')),
        './{}/{}/1.4 Literary Publications'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri C'))
        ]


    for path in KRA_I:
        os.makedirs(path)

    for path in KRA_II:
        os.makedirs(path)


''''
Scan all KRA folders.
Return: All folders that are not empty and contains pdf file. 
'''
def scan_folders(fpath):
    KRAs = [f'{fpath}/KRA I',f'{fpath}/KRA II']
    list_roots = []
        
    for folder in KRAs:
        for (root, dirs, files) in os.walk(folder, topdown=True):
            if not (any(f.endswith('.pdf') for f in files)):
                    continue
            list_roots.append(root)
    return list_roots
            

def merge_pdf(files, filename):
    merger=pdfM()
    for i in files:
        merger.append(i)
    merger.write(filename)
    return len(merger.pages)

def main():
    '''
    Create directories.
    ''' 
    # create_dirs()
   
    '''
    Merge pdf files in not empty folders and save it as output.pdf
    '''
    # datetime object containing current date and time
    now = datetime.now()
 
    
    folder_path = input("Enter path of folders: ")
    file_path = f'{folder_path} {now} merge details.txt'
    file = open(file_path, 'a')

    roots_not_empty = scan_folders(folder_path)
    for folder in roots_not_empty:
        str_path = f"{folder}/**/*.pdf"
        print(f"{folder} [DONE]")
        files = glob.glob(str_path, recursive=True)
        number_of_pages = merge_pdf(files, folder + '/output.pdf')
        file.write(f"{folder} {number_of_pages} pages" + '\n')
    file.close()
        

if __name__ == "__main__":
    main()