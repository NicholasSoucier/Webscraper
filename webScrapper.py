import requests
from bs4 import BeautifulSoup

print('''


░██╗░░░░░░░██╗███████╗██████╗░░██████╗░█████╗░██████╗░░█████╗░██████╗░███████╗
░██║░░██╗░░██║██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
░╚██╗████╗██╔╝█████╗░░██████╦╝╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝█████╗░░
░░████╔═████║░██╔══╝░░██╔══██╗░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗██████╦╝██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝


''')

URL = input("Please Enter a URL to Scrape: ")
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


#Search Algorithm for scraping the page - Selector
def inspectSelector():
    while True:
        print('''
        Choose how you'll inspect the page:
            Search Elements:
            [1] - Find element(s) by ID
            [2] - Find element(s) by Class Name
            [3] - Find Context element(s) by Class Name
            [4] - Find Context element(s) by String
            [5] - Exit Program''')
        chk = input("> ")
        if chk == "1":
            scrapeID()
        elif chk == "2":
            scrapeClass()
        elif chk == "3":
            scrapeContext()
        elif chk == "4":
            scrapeString()
        elif chk == "5":
            exit()
        else:
            print("Not a valid option, try again")

#Search Algorithm for scraping the page - by ID
def scrapeID():
    searchid = input("Please enter HTLM ID: ")
    results = soup.find_all(id=str(searchid))
    printResults(results)
#Search Algorithm for scraping the page - by Class Name
def scrapeClass():
    searchclass = input("Please enter HTLM Class Name: ")
    results = soup.find_all(class_=str(searchclass))
    printResults(results)
#Search Algorithm for scraping the page - by context and class
def scrapeContext():
    searchContext = input("Please enter HTML object context: ")
    searchClass = input("Please enter HTML Class Name: ")
    results = soup.find_all(searchContext, class_=str(searchClass))
    printResults(results)
#Search Algorithm for scraping the page - by String
def scrapeString():
    searchContext = input("Please enter HTML object context: ")
    searchString = input("Please enter string to search: ")
    results = soup.find_all(searchContext, string=lambda text: searchString in text.lower())
    printResults(results)

def printResults(resultArray):
    for x in resultArray:
        print(x, end="\n"*2)
        print("...Type 't' to extract text, 'q' to quit, or press enter to continue...")
        cont = input()
        if cont == "t":
            print(x.text.strip())
            print("...Press enter to continue...")
            input()
        if cont == "q":
            break


#Check status and start scraping.

if(page.status_code == 200):
    print("Page Found Successfully")
    inspectSelector()
else:
    print("Page Not Found Successfully")
    exit()
