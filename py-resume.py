from fetch_linkedin import return_tidy_data
from tidy_tex import *

from person_info import person_info

#Fetch profile data
names,education,skills,interests,awards = return_tidy_data()


#Handle data




#Write data to tex
tex1 = ''
tex1 += set_preamble()
tex1 += personal_data(names,person_info)

tex1 += '\\begin{document}\n'

tex1 += '\\maketitle\n'

#Education
tex1 += gen_sec('edu.tex',education['values'],'Education',['id'])

#Awards
tex1 += gen_sec(fname='awa.tex',vals=awards,section='Awards and Honours',black_list=['id'])

tex1 += '\\end{document}\n'

f=open('cv1.tex','w')
f.write(tex1)
f.close()
