README
=============

Requries:
-------
python-inkedin url = git@github.com:ozgur/python-linkedin.git
python2.7

Use:
-------
secrets.py: create a py with your linkedin api keys in here. This is not tracked by git for security reasons
person_info.py: create this file if you wish to include data in your CV/resume that is not available on the web. Example: personal mobile number.


About
-------
This project is used to render a cv based on a users profile on Linkedin.

Linkedin have a resume builder but currently it does not work well with Honours and Awards.
Furthermore, the current selection do not look very appealling and I would rather a LaTex style on my resume.

Also I wish to eventually include data that is not contained entirely on Linkedin, such as Google Scholar Data (when I eventually publish..) and GitHub, where this (and eventually ...) other projects are hosted.

Please feel free to use and modify this code if you think it will be of use. A link back to this GitHub project would be greatly appreciated.

Kind regards,
David


Current issues/failings:
---------------------
As of May 17 2014, Linkedin Api does not return full data on 'HonorsAwards'. Year of award and description is missing! May need to fill in some blanks...

Yet to implement GitHub
Yet to implement Google Scholar
