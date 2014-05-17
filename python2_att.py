#Append path and import
from linkedin import linkedin
import urllib

#########################
#Import secrets
from secrets import secret

#Info I don't want on Linkedin, but want on a submitted CV:
from person_info import person_info

#######################
#Load auth keys
CONSUMER_KEY = secret['API_KEY']
CONSUMER_SECRET = secret['Secret_Key']
USER_TOKEN = secret['OAUT']
USER_SECRET = secret['OAUS']
RETURN_URL = 'http://localhost:8000'

def fetch_newest_data():
    authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET,
                                                          USER_TOKEN, USER_SECRET,
                                                          RETURN_URL, linkedin.PERMISSIONS.enums.values())
    # Pass it in to the app...
    application = linkedin.LinkedInApplication(authentication)
    
    # Use the app....
    app_data=application.get_profile(selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations','interests','honors-awards','num-recommenders'])
    return app_data


def write_all_to_file(lists,texts):
    for (i,j) in  zip(lists,texts):
        # print i,j
        f = open(j,'w')
        f.write(i)
        f.close()


#Fetch current profile
app_data = fetch_newest_data() 

#Separate items
education = app_data['educations']
names = [app_data['firstName'],app_data['lastName']]

#Strip skills
skill_list =  app_data['skills']
skills = [skill['skill']['name'] for skill in skill_list['values']]


interests_lists = app_data['interests']
interests = interests_lists.split(',')

#strip honours:
awards_list =  app_data['honorsAwards']
awards = [award for award in awards_list['values']]


#write_all_to_file([education,skills,interests],['edu.txt','skill.txt','ints.txt'])
def process_ed(entry1):
   # print "\section{Education}"
    return "\cventry{"+str(entry1['startDate']['year'])+"--"+str(entry1['endDate']['year'])+"}{"+str(entry1['degree'])+"}{"+str(entry1['schoolName'])+"}{"+str(entry1['fieldOfStudy'])+"}"


def save_ed(fname='edu.tex',vals=education['values']):
    edu_tex = "\section{Education}\n"
    for entry1 in vals:
        edu_tex+=process_ed(entry1)
        edu_tex+='\n'
    
    f=open(fname,'w')
    f.write(edu_tex)
    f.close()

def years_active(eventry):
    tmp=''
    if 'startDate' in [i for i in eventry]:
        tmp+='{'+str(eventry['startDate']['year'])+'--'
        tmp+=str(eventry['endDate']['year'])+'}'

    #Awards do not have year active, but need to avoid title put in year..
    else:
        tmp+='{}'

    return tmp

def cv_entry(eventry,black_list=[]):
    #Initialize
    ent='\cventry'
    tmp=''
    #Treack length of entry
    leni=0

    #Handle years active
    ent+=years_active(eventry)
    leni+=1

    #items to ignore...
    black_list.append('startDate')
    black_list.append('endDate')

    #loop over items
    for i in eventry:
        if i in black_list:
            pass
        else:
            ent+='{'+str(eventry[i])+'}'
            leni+=1

    #make sure entry is long enough. Need atleast 5 entries to avoid prompt.
    for i in range(6-leni):
        ent+='{}'

    return ent

def gen_sec(fname='edu.tex',vals=education['values'],section='Education',black_list=['id'],sv=False):
    edu_tex = "\section{"+section+"}\n"
    for entry1 in vals:
        edu_tex+=cv_entry(entry1,black_list)
        edu_tex+='\n'
        
    #Optionally save to tex.
    if sv==True:
        f=open(fname,'w')
        f.write(edu_tex)
        f.close()


    return edu_tex



def set_preamble():
    #define preamble for cv
    preamble = "\\documentclass[11pt,a4paper]{moderncv}\n\\moderncvtheme[blue]{classic}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8x]{inputenc}\n\\usepackage[croatian]{babel}\n\\usepackage[scale=0.8]{geometry}\n\\recomputelengths\n\\fancyfoot{}\n\\fancyfoot[LE,RO]{\\thepage}\n\\fancyfoot[RE,LO]{\\footnotesize }"
    
    return preamble

def personal_data(names,person_info):
    #personal data
    personal_data = "\\firstname{"+names[0]+"}\n"+"\\familyname{"+names[1]+"}\n"+"\\title{Curriculum Vitae}\n"+"\\address{Midleton}\n"+"\\mobile{"+person_info['mob_num']+"}\n"+"\\phone{<Phone number>}\n"+"\\fax{<Fax number>}\n"+"\\email{"+person_info['email']+"}\n"
    #%\extrainfo{additional information (optional)}
    #%\photo[84pt]{placeholder.jpg}\n"

    return personal_data

def quote(qref='1'):
    q="\\quote{\"Success is the ability to go from failure to failure without losing your enthusiasm.\" -- Winston Churchill\"}"
    return q


def main_tex():
    #Write tex file.

    tex1 = ''
    tex1 += set_preamble()
    tex1 += personal_data(names,person_info)

    tex1 += '\\begin{document}\n'

    tex1 += '\\maketitle\n'

    #Education
    tex1 += gen_sec()
    
    #Awards
    tex1 += gen_sec(fname='awa.tex',vals=awards_list['values'],section='Awards and Honours',black_list=['id'])

    tex1 += '\\end{document}\n'

    f=open('cv1.tex','w')
    f.write(tex1)
    f.close()
