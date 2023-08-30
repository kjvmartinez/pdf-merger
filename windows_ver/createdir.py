import os

''''
Create all directories and subdirectories.
'''
def create_dirs(folder_path):
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

    kra3_dictionary = {
        'level 0' : 'KRA III',
        'Cri A' : 'CRITERION A Service to the Institution',
        'Cri B' : 'CRITERION B Service to the Community',
        'Cri C' : 'CRITERION C Quality of Extension Service',
        'Cri D' : 'CRITERION D Bonus Criterion',
    }

    kra4_dictionary = {
        'level 0' : 'KRA IV',
        'Cri A' : 'CRITERION A Involvement in Professional Organization',
        'Cri B' : 'CRITERION B Continuing Development',
        'Cri C' : 'CRITERION C Awards and Recognition',
        'Cri D' : 'CRITERION D Bonus Indicators for Newly Appointed Faculty',
    }
 
    KRA_I = [
        ('.\\{}\\{}'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri A'))),
        ('.\\{}\\{}\\1.1 STUDENT EVALUATION'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri A'))),
        ('.\\{}\\{}\\1.2 SUPERVISOR’S EVALUATION'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri A'))),
        ('.\\{}\\{}'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\1.1 SOLE AUTHORSHIP'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\1.1 SOLE AUTHORSHIP\\1'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\1.1 SOLE AUTHORSHIP\\2'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\1.2 CO-AUTHORSHIP'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\1.2 CO-AUTHORSHIP\\1'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\1.2 CO-AUTHORSHIP\\2'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\2 ACADEMIC PROGRAMS DEVELOPED OR REVISED AND IMPLEMENTED'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\2 ACADEMIC PROGRAMS DEVELOPED OR REVISED AND IMPLEMENTED\\1'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\2 ACADEMIC PROGRAMS DEVELOPED OR REVISED AND IMPLEMENTED\\2'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri B'))),
        ('.\\{}\\{}'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri C'))),
        ('.\\{}\\{}\\1.1 ADVISER'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri C'))),
        ('.\\{}\\{}\\1.1 ADVISER\\1 SPECIAL OR CAPSTONE PROJECT'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri C'))),
        ('.\\{}\\{}\\1.1 ADVISER\\2 UNDERGRADUATE THESIS'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri C'))),
        ('.\\{}\\{}\\1.1 ADVISER\\3 MASTER’S THESIS'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri C'))),
        ('.\\{}\\{}\\1.1 ADVISER\\4 DISSERTATION'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri C'))),
        ('.\\{}\\{}\\1.2 PANEL'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri C'))),
        ('.\\{}\\{}\\1.2 PANEL\\1 SPECIAL OR CAPSTONE PROJECT'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri C'))),
        ('.\\{}\\{}\\1.2 PANEL\\2 UNDERGRADUATE THESIS'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri C'))),
        ('.\\{}\\{}\\1.2 PANEL\\3 MASTER’S THESIS'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri C'))),
        ('.\\{}\\{}\\1.2 PANEL\\4 DISSERTATION'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri C'))),
        ('.\\{}\\{}\\2 FOR SERVICES RENDERED AS MENTOR'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri C'))),
        ('.\\{}\\{}\\2 FOR SERVICES RENDERED AS MENTOR\\1'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri C'))),
        ('.\\{}\\{}\\2 FOR SERVICES RENDERED AS MENTOR\\2'.format(kra1_dictionary.get('level 0'), kra1_dictionary.get('Cri C')))
    ]
    

    KRA_II =[
        ('.\\{}\\{}'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A'))),
        ('.\\{}\\{}\\1.1 SOLE AUTHORSHIP'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A'))),
        ('.\\{}\\{}\\1.1 SOLE AUTHORSHIP\\1'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A'))),
        ('.\\{}\\{}\\1.1 SOLE AUTHORSHIP\\2'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A'))),
        ('.\\{}\\{}\\1.2 CO-AUTHORSHIP'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A'))),
        ('.\\{}\\{}\\1.2 CO-AUTHORSHIP\\1'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A'))),
        ('.\\{}\\{}\\1.2 CO-AUTHORSHIP\\2'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A'))),
        ('.\\{}\\{}\\2.1 LEAD RESEARCHER'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A'))),
        ('.\\{}\\{}\\2.1 LEAD RESEARCHER\\1'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A'))),
        ('.\\{}\\{}\\2.1 LEAD RESEARCHER\\2'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A'))),
        ('.\\{}\\{}\\2.2 CONTRIBUTOR'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A'))),
        ('.\\{}\\{}\\2.2 CONTRIBUTOR\\1'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A'))),
        ('.\\{}\\{}\\2.2 CONTRIBUTOR\\2'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A'))),
        ('.\\{}\\{}\\3.1 LOCAL AUTHORS'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A'))),
        ('.\\{}\\{}\\3.1 LOCAL AUTHORS\\1'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A'))),
        ('.\\{}\\{}\\3.1 LOCAL AUTHORS\\2'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A'))),
        ('.\\{}\\{}\\3.2 INTERNATIONAL AUTHORS'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A'))),
        ('.\\{}\\{}\\3.2 INTERNATIONAL AUTHORS\\1'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A'))),
        ('.\\{}\\{}\\3.2 INTERNATIONAL AUTHORS\\2'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri A'))),
        ('.\\{}\\{}'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\1.1.1 INVENTION PATENTS (SOLE INVENTOR)'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\1.1.1 INVENTION PATENTS (SOLE INVENTOR)\\1'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\1.1.1 INVENTION PATENTS (SOLE INVENTOR)\\2'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\1.1.1 INVENTION PATENTS (MULTIPLE INVENTORS)'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\1.1.1 INVENTION PATENTS (MULTIPLE INVENTORS)\\1'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\1.1.1 INVENTION PATENTS (MULTIPLE INVENTORS)\\2'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\1.1.2 UTILITY MODELS AND INDUSTRIAL DESIGNS (SOLE INVENTOR)'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\1.1.2 UTILITY MODELS AND INDUSTRIAL DESIGNS (SOLE INVENTOR)\\1'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\1.1.2 UTILITY MODELS AND INDUSTRIAL DESIGNS (SOLE INVENTOR)\\2'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\1.2.1 LOCAL'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\1.2.1 LOCAL\\1'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\1.2.1 LOCAL\\2'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),

        ('.\\{}\\{}\\1.2.2 INTERNATIONAL'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\1.2.2 INTERNATIONAL\\1'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\1.2.2 INTERNATIONAL\\2'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),

        ('.\\{}\\{}\\2.1.1 NEW SOFTWARE PRODUCTS (SOLE DEVELOPER)'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\2.1.1 NEW SOFTWARE PRODUCTS (SOLE DEVELOPER)\\1'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\2.1.1 NEW SOFTWARE PRODUCTS (SOLE DEVELOPER)\\2'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\2.1.1 NEW SOFTWARE PRODUCTS (MULTIPLE DEVELOPERS)'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\2.1.1 NEW SOFTWARE PRODUCTS (MULTIPLE DEVELOPERS)\\1'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\2.1.1 NEW SOFTWARE PRODUCTS (MULTIPLE DEVELOPERS)\\2'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),

        ('.\\{}\\{}\\2.1.2 UPDATED SOFTWARE PRODUCTS'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\2.1.2 UPDATED SOFTWARE PRODUCTS\\1'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\2.1.2 UPDATED SOFTWARE PRODUCTS\\2'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\2.2 NEW PLANT VARIETY OR ANIMAL BREEDS DEVELOPED OR NEW MICROBIAL STRAINS ISOLATED THAT ARE PROPAGATED OR REPRODUCED (SOLE DEVELOPER)'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\2.2 NEW PLANT VARIETY OR ANIMAL BREEDS DEVELOPED OR NEW MICROBIAL STRAINS ISOLATED THAT ARE PROPAGATED OR REPRODUCED (SOLE DEVELOPER)\\1'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\2.2 NEW PLANT VARIETY OR ANIMAL BREEDS DEVELOPED OR NEW MICROBIAL STRAINS ISOLATED THAT ARE PROPAGATED OR REPRODUCED (SOLE DEVELOPER)\\2'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\2.2 NEW PLANT VARIETY OR ANIMAL BREEDS DEVELOPED OR NEW MICROBIAL STRAINS ISOLATED THAT ARE PROPAGATED OR REPRODUCED (MULTIPLE DEVELOPERS)'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\2.2 NEW PLANT VARIETY OR ANIMAL BREEDS DEVELOPED OR NEW MICROBIAL STRAINS ISOLATED THAT ARE PROPAGATED OR REPRODUCED (MULTIPLE DEVELOPERS)\\1'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),
        ('.\\{}\\{}\\2.2 NEW PLANT VARIETY OR ANIMAL BREEDS DEVELOPED OR NEW MICROBIAL STRAINS ISOLATED THAT ARE PROPAGATED OR REPRODUCED (MULTIPLE DEVELOPERS)\\2'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri B'))),

        ('.\\{}\\{}'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri C'))),
        ('.\\{}\\{}\\1.1 NEW CREATIVE PERFORMING ARTWORK'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri C'))),
        ('.\\{}\\{}\\1.1 NEW CREATIVE PERFORMING ARTWORK\\1'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri C'))),
        ('.\\{}\\{}\\1.1 NEW CREATIVE PERFORMING ARTWORK\\2'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri C'))),

        ('.\\{}\\{}\\1.2 EXHIBITION'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri C'))),
        ('.\\{}\\{}\\1.2 EXHIBITION\\1'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri C'))),
        ('.\\{}\\{}\\1.2 EXHIBITION\\2'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri C'))),

        ('.\\{}\\{}\\1.3 JURIED OR PEER-REVIEWED DESIGNS'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri C'))),
        ('.\\{}\\{}\\1.3 JURIED OR PEER-REVIEWED DESIGNS\\1'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri C'))),
        ('.\\{}\\{}\\1.3 JURIED OR PEER-REVIEWED DESIGNS\\2'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri C'))),

        ('.\\{}\\{}\\1.4 LITERARY PUBLICATIONS'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri C'))),
        ('.\\{}\\{}\\1.4 LITERARY PUBLICATIONS\\1'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri C'))),
        ('.\\{}\\{}\\1.4 LITERARY PUBLICATIONS\\2'.format(kra2_dictionary.get('level 0'),kra2_dictionary.get('Cri C')))
        ]

    

        

    KRA_III =[
        ('.\\{}\\{}'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri A'))),
    ('.\\{}\\{}\\1 FOR EVERY SUCCESSFUL LINKAGE, NETWORKING OR PARTNERSHIP ACTIVITY'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri A'))),
    ('.\\{}\\{}\\1 FOR EVERY SUCCESSFUL LINKAGE, NETWORKING OR PARTNERSHIP ACTIVITY\\1'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri A'))),
    ('.\\{}\\{}\\1 FOR EVERY SUCCESSFUL LINKAGE, NETWORKING OR PARTNERSHIP ACTIVITY\\2'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri A'))),
    ('.\\{}\\{}\\2 TOTAL CONTRIBUTION TO INCOME GENERATION'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri A'))),
    ('.\\{}\\{}'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\1.1 FOR SERVICES IN ACCREDITATION, EVALUATION, ASSESSMENT WORKS AND OTHER RELATED EDUCATION QA ACTIVITIES'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\1.1 FOR SERVICES IN ACCREDITATION, EVALUATION, ASSESSMENT WORKS AND OTHER RELATED EDUCATION QA ACTIVITIES\\1'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\1.1 FOR SERVICES IN ACCREDITATION, EVALUATION, ASSESSMENT WORKS AND OTHER RELATED EDUCATION QA ACTIVITIES\\2'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\1.2 SERVICES AS JUDGE OR EXAMINER FOR LOCAL OR INTERNATIONAL RESEARCH AWARDS AND ACADEMIC COMPETITIONS'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\1.2 SERVICES AS JUDGE OR EXAMINER FOR LOCAL OR INTERNATIONAL RESEARCH AWARDS AND ACADEMIC COMPETITIONS\\1'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\1.2 SERVICES AS JUDGE OR EXAMINER FOR LOCAL OR INTERNATIONAL RESEARCH AWARDS AND ACADEMIC COMPETITIONS\\2'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\1.3 FOR SERVICES AS A SHORT-TERM CONSULTANT OR EXPERT'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\1.3 FOR SERVICES AS A SHORT-TERM CONSULTANT OR EXPERT\\1'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\1.3 FOR SERVICES AS A SHORT-TERM CONSULTANT OR EXPERT\\2'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\1.4 SERVICES THROUGH MEDIA'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\1.4 SERVICES THROUGH MEDIA\\1.4.1 Writer of occasional newspaper column'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\1.4 SERVICES THROUGH MEDIA\\1.4.2 Writer of regular newspaper column'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\1.4 SERVICES THROUGH MEDIA\\1.4.3 Host of TV or Radio Program'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\1.4 SERVICES THROUGH MEDIA\\1.4.4 Guesting as technical expert for TV or radio program or print media or online media'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\1.5 FOR EVERY HOUR OF TRAINING COURSE, SEMINAR, WORKSHOP CONDUCTED AS A RESOURCE PERSON, CONVENOR, FACILITATOR, MODERATOR, KEYNOTE OR PLENARY SPEAKER OR PANELIST'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\1.5 FOR EVERY HOUR OF TRAINING COURSE, SEMINAR, WORKSHOP CONDUCTED AS A RESOURCE PERSON, CONVENOR, FACILITATOR, MODERATOR, KEYNOTE OR PLENARY SPEAKER OR PANELIST\\1'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\1.5 FOR EVERY HOUR OF TRAINING COURSE, SEMINAR, WORKSHOP CONDUCTED AS A RESOURCE PERSON, CONVENOR, FACILITATOR, MODERATOR, KEYNOTE OR PLENARY SPEAKER OR PANELIST\\2'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri B'))),

    ('.\\{}\\{}\\2 FOR EVERY SERVICE-ORIENTED PROJECT IN THE COMMUNITY PARTICIPATED, INCLUDING ADVOCACY INITIATIVES'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\2 FOR EVERY SERVICE-ORIENTED PROJECT IN THE COMMUNITY PARTICIPATED, INCLUDING ADVOCACY INITIATIVES\\1'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\2 FOR EVERY SERVICE-ORIENTED PROJECT IN THE COMMUNITY PARTICIPATED, INCLUDING ADVOCACY INITIATIVES\\2'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri B'))),
    ('.\\{}\\{}'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri C'))),
    ('.\\{}\\{}\\1 CLIENT SATISFACTION RATING FOR OUTREACH AND EXTENSION PROJECTS'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri C'))),
    ('.\\{}\\{}\\1 CLIENT SATISFACTION RATING FOR OUTREACH AND EXTENSION PROJECTS\\AY 2019-2020'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri C'))),
    ('.\\{}\\{}\\1 CLIENT SATISFACTION RATING FOR OUTREACH AND EXTENSION PROJECTS\\AY 2020-2021'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri C'))),
    ('.\\{}\\{}\\1 CLIENT SATISFACTION RATING FOR OUTREACH AND EXTENSION PROJECTS\\AY 2021-2022'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri C'))),
    ('.\\{}\\{}\\1 CLIENT SATISFACTION RATING FOR OUTREACH AND EXTENSION PROJECTS\\AY 2022-2023'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri C'))),

    ('.\\{}\\{}'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri D'))),
    ('.\\{}\\{}\\1.1 HIGHEST ADMINISTRATIVE DESIGNATION HELD FOR AT LEAST ONE YEAR WITH THE EVALUATION PERIOD'.format(kra3_dictionary.get('level 0'),kra3_dictionary.get('Cri C')))
    ]

    KRA_IV =[
        ('.\\{}\\{}'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri A'))),
    ('.\\{}\\{}\\1 FOR CURRENT INDIVIDUAL MEMBERSHIP AND ACTIVE ROLE CONTRIBUTION IN PROFESSIONAL ORGANIZATION, LEARNED OR HONOR OR SCIENTIFIC SOCIETY'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri A'))),
    ('.\\{}\\{}\\1 FOR CURRENT INDIVIDUAL MEMBERSHIP AND ACTIVE ROLE CONTRIBUTION IN PROFESSIONAL ORGANIZATION, LEARNED OR HONOR OR SCIENTIFIC SOCIETY\\1'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri A'))),
    ('.\\{}\\{}\\1 FOR CURRENT INDIVIDUAL MEMBERSHIP AND ACTIVE ROLE CONTRIBUTION IN PROFESSIONAL ORGANIZATION, LEARNED OR HONOR OR SCIENTIFIC SOCIETY\\2'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri A'))),
    ('.\\{}\\{}'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\1.1 FOR DOCTORATE DEGREE (First Time)'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\1.2 ADDITIONAL DEGREES'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\1.2 ADDITIONAL DEGREES\\1'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\1.2 ADDITIONAL DEGREES\\2'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\2 FOR EVERY PARTICIPATION IN CONFERENCES, SEMINARS, WORKSHOPS, INDUSTRY IMMERSION'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\2 FOR EVERY PARTICIPATION IN CONFERENCES, SEMINARS, WORKSHOPS, INDUSTRY IMMERSION\\1'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\2 FOR EVERY PARTICIPATION IN CONFERENCES, SEMINARS, WORKSHOPS, INDUSTRY IMMERSION\\2'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\2 FOR EVERY PARTICIPATION IN CONFERENCES, SEMINARS, WORKSHOPS, INDUSTRY IMMERSION\\3'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\2 FOR EVERY PARTICIPATION IN CONFERENCES, SEMINARS, WORKSHOPS, INDUSTRY IMMERSION\\4'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\2 FOR EVERY PARTICIPATION IN CONFERENCES, SEMINARS, WORKSHOPS, INDUSTRY IMMERSION\\5'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\2 FOR EVERY PARTICIPATION IN CONFERENCES, SEMINARS, WORKSHOPS, INDUSTRY IMMERSION\\6'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\2 FOR EVERY PARTICIPATION IN CONFERENCES, SEMINARS, WORKSHOPS, INDUSTRY IMMERSION\\7'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\2 FOR EVERY PARTICIPATION IN CONFERENCES, SEMINARS, WORKSHOPS, INDUSTRY IMMERSION\\8'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\2 FOR EVERY PARTICIPATION IN CONFERENCES, SEMINARS, WORKSHOPS, INDUSTRY IMMERSION\\9'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\3 FOR EVERY PAPER PRESENTATION IN CONFERENCES'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\3 FOR EVERY PAPER PRESENTATION IN CONFERENCES\\1'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\3 FOR EVERY PAPER PRESENTATION IN CONFERENCES\\2'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\3 FOR EVERY PAPER PRESENTATION IN CONFERENCES\\3'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri B'))),
    ('.\\{}\\{}\\3 FOR EVERY PAPER PRESENTATION IN CONFERENCES\\4'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri B'))),
    ('.\\{}\\{}'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri C'))),
    ('.\\{}\\{}\\1 FOR EVERY AWARD OF DISTINCTION RECEIVED IN RECOGNITION OF ACHIEVEMENT IN RELEVANT AREAS OF SPECIALIZATION, PROFESSION AND OR ASSIGNMENT OF THE FACULTY CONCERNED'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri C'))),
    ('.\\{}\\{}\\1 FOR EVERY AWARD OF DISTINCTION RECEIVED IN RECOGNITION OF ACHIEVEMENT IN RELEVANT AREAS OF SPECIALIZATION, PROFESSION AND OR ASSIGNMENT OF THE FACULTY CONCERNED\\1'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri C'))),
    ('.\\{}\\{}\\1 FOR EVERY AWARD OF DISTINCTION RECEIVED IN RECOGNITION OF ACHIEVEMENT IN RELEVANT AREAS OF SPECIALIZATION, PROFESSION AND OR ASSIGNMENT OF THE FACULTY CONCERNED\\2'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri C'))),
    ('.\\{}\\{}\\1 FOR EVERY AWARD OF DISTINCTION RECEIVED IN RECOGNITION OF ACHIEVEMENT IN RELEVANT AREAS OF SPECIALIZATION, PROFESSION AND OR ASSIGNMENT OF THE FACULTY CONCERNED\\3'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri C'))),
    ('.\\{}\\{}\\1 FOR EVERY AWARD OF DISTINCTION RECEIVED IN RECOGNITION OF ACHIEVEMENT IN RELEVANT AREAS OF SPECIALIZATION, PROFESSION AND OR ASSIGNMENT OF THE FACULTY CONCERNED\\4'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri C'))),
    ('.\\{}\\{}'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri D'))),
    ('.\\{}\\{}\\1 FOR EVERY YEAR OF FULL-TIME ACADEMIC SERVICE IN AN INSTITUTION OF HIGHER LEARNING'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri C'))),
    ('.\\{}\\{}\\1 FOR EVERY YEAR OF FULL-TIME ACADEMIC SERVICE IN AN INSTITUTION OF HIGHER LEARNING\\1'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri C'))),
    ('.\\{}\\{}\\1 FOR EVERY YEAR OF FULL-TIME ACADEMIC SERVICE IN AN INSTITUTION OF HIGHER LEARNING\\2'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri C'))),
    ('.\\{}\\{}\\2 FOR EVERY YEAR OF INDUSTRY EXPERIENCE (NON-ACADEMIC ORGANIZATION)'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri C'))),
    ('.\\{}\\{}\\2 FOR EVERY YEAR OF INDUSTRY EXPERIENCE (NON-ACADEMIC ORGANIZATION)\\1'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri C'))),
    ('.\\{}\\{}\\2 FOR EVERY YEAR OF INDUSTRY EXPERIENCE (NON-ACADEMIC ORGANIZATION)\\2'.format(kra4_dictionary.get('level 0'),kra4_dictionary.get('Cri C')))
    ]

    all_KRAs = [KRA_I, KRA_II, KRA_III, KRA_IV]

    for kra in all_KRAs:
        for path_tuple in kra:
            path = os.path.join(path_tuple)
            path = os.path.join(folder_path, path)
            os.makedirs(path, exist_ok=True)

def create_tree(root_dir, output_file, level=0):
    items = os.listdir(root_dir)
    for item in sorted(items):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            output_file.write("  " * level + "📁 " + item + "\n")
            create_tree(item_path, output_file, level + 1)
        else:
            output_file.write("  " * level + "📄 " + item + "\n")

        
def main():
    '''
    Create directories.
    ''' 
    folder_path = input("Enter your name (Last name, First name MI): ")
    create_dirs(folder_path)

    root_directory = f'{folder_path}'  # Replace with the desired root directory
    output_filename = 'tree_structure.txt'  # Name of the output file

    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write("📁 " + root_directory + "\n")
        create_tree(root_directory, output_file)

    x = input("Folders created.")

if __name__ == "__main__":
    main()