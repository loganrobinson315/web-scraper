from bs4 import BeautifulSoup
import requests
from datetime import date
import itertools
import json 


def gather_info():
    search_term =  val.replace(" ", "+")
    print(search_term)
    source = requests.get(f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow=0&criteria=formNumber&value={search_term}&isDescending=false',).text
    soup = BeautifulSoup(source, 'lxml')
    # file_number = soup.find_all('th', {'class':'ShowByColumn'})
    for table in soup.find_all('tr', {'class':['even','odd']}):
        if table.td(text={val}):
            form_number = table.td.text
            form_title = table.find('td', class_='MiddleCellSpacer').text
    
    for table in soup.find_all('tr', {'class':['even','odd']}):
        if table.td(text={val}):
            output = []
            min_years = table.find('td', class_='EndCellSpacer').text.split()
            my_min_year = 9999
            my_max_year = 0000
            for i in min_years:
                my_year = int(i)
                if my_year < my_min_year:
                    my_min_year = my_year  
    
    for table in soup.find_all('tr', {'class':['even','odd']}):
        if table.td(text={val}):
            output = []
            min_years = table.find('td', class_='EndCellSpacer').text.split()
            for i in min_years:
                my_year = int(i)
                if my_year > my_max_year:
                    my_max_year = my_year
    x = {
    "form_number": form_number.strip(),
    "form_title": form_title.strip(),
    "min_year": my_min_year,
    "max_year": my_max_year,
    }
    

    y = json.dumps(x)

    print('Here is the info for', val)
    print()
    print(y)
    print()

    
def download():
    search_term =  val.replace(" ", "+")
    # print(search_term)
    source = requests.get(f'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow=0&criteria=formNumber&value={search_term}&isDescending=false',).text
    soup = BeautifulSoup(source, 'lxml')
    links = soup.find_all('a')
    i = 0
    if answer == "y":   
        for link in links:
            for year_number in range(start_number, end_number+1):
                if link(text={val}):
                    if ('.pdf' and str(year_number) in link.get('href', [])):
                        i += 1
                        print("Downloading file: ", i)
                        response = requests.get(link.get('href'))
                        pdf = open(val+"-"+str(year_number)+".pdf", 'wb')
                        pdf.write(response.content)
                        pdf.close()
                        print("File ", i, " downloaded")
        print('downloaded')
    else:
        print('does not exist')

    
print('Welcome!')
val = input("Please enter a Form Value (This needs to bee an exact match): ")
gather_info()
answer = input("Lets download the files, enter y to continue:")
start_number = int(input("Please enter a START year you would like to download: "))
end_number = int(input("Please enter an END year you would like to download: "))
download()
    











