#Files that I want to Make...
TARGETS = cv1.pdf cv1.tex


#Rule to make CV1.pdf...
cv1.pdf: cv1.tex
	pdflatex $<


#Rule to update CV1.tex
cv1.tex: py-resume.py fetch_gh.py fetch_linkedin.py person_info.py secrets.py tidy_tex.py
	python2 $<


clean:
	rm -rf *.pdf *.pyc
