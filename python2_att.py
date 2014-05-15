#Append path and import
from linkedin import linkedin
import urllib

#########################
#Import secrets
from secrets import secret

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
    app_data=application.get_profile(selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations','interests'])
    return app_data


def write_all_to_file(lists,texts):
    for (i,j) in  zip(lists,texts):
        print i,j
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


def cv_entry(eventry):
    ent='\{cventry}'
    tmp=''
    for i in eventry:
        print i
        if i=='startDate':
            tmp+='{'+str(eventry[i]['year'])+'--'
        elif i=='endDate':
            tmp+=str(eventry[i]['year'])+'}'
            ent+=tmp
        else:
            ent+='{'+str(eventry[i])+'}'
    return ent

def save_ed2(fname='edu.tex',vals=education['values'],section='Education'):
    edu_tex = "\section{"+section+"}\n"
    for entry1 in vals:
        edu_tex+=cv_entry(entry1)
        edu_tex+='\n'
    
    f=open(fname,'w')
    f.write(edu_tex)
    f.close()
