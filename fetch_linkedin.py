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


def return_tidy_data():
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

    return names,education,skills,interests,awards
