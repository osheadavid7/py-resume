from fetch_linkedin import return_tidy_ln_data
from fetch_gh import return_tidy_gh_data
from tidy_tex import *

from person_info import person_info

#Fetch profile data
names,education,skills,interests,awards,positions = return_tidy_ln_data()
gh_user,repo_list = return_tidy_gh_data()

#Handle data




#Write data to tex
tex1 = ''
tex1 += set_preamble()
tex1 += personal_data(names,person_info)


tex1 += custom_func()
tex1 += '\\begin{document}\n'

tex1 += '\\maketitle\n'

#draw horizontal line above first section
tex1 +='\\textcolor{airforceblue}{\\rule{\\textwidth}{1pt}}'

#Work experience
tex1 += gen_sec('Experience',positions,'year',['id','isCurrent'],False,'pos.tex','mycventry')


#Education
tex1 += gen_sec('Education',education['values'],'year',['id'],False,'edu.tex','')

#Awards
tex1 += gen_sec('Awards and Honours',awards[0:2],'',['id'],False,'awa.tex','')

#GitHub
tex1 += gen_sec('Code',[repo_list[0],repo_list[2]],'name',['id'],False,'gh.tex','mycventry')


tex1 += '\\end{document}\n'

f=open('cv1.tex','w')
f.write(tex1)
f.close()
