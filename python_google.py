from webbrowser import open as wopen
'''
def google_file(file):
    url="http://google.com/?#q="
    with open(file)() as f:
        lines = file.readlines()
        for line in lines:
            searchTerm=line
            wopen(url+searchTerm)
        
'''

######
# NB - this function works. DO NOT TOUCH IT.
def google_file(file):
    url="http://google.com/?#q="
    f=open(file,'r')
    lines = f.readlines()
    for line in lines:
        searchTerm=line
        wopen(url+searchTerm)
    f.close()
#########

def google_input():
    url="http://google.com/?#q="
    term=input('search for: ')
    wopen(url+term)
