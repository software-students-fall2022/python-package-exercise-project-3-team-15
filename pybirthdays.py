import requests
from bs4 import BeautifulSoup

def get_birthday(person):
    name_cleaned = person.lower().replace(" ", "-")

    url = "https://www.famousbirthdays.com/people/" + name_cleaned + ".html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    main_div = soup.find("div", {"class":"stat box"})

    try: 
        month = main_div.find("span", {"class":"hidden-sm"})
        day = main_div.find("a")
        year = main_div.find_all("a")
        print(person, "'s Birthday is on: ", month.text, " ", day.text[-1], ", ", year[-1].text, sep='')
    except:
        print("Sorry!", person, "is not in our database...")

def main():

    welcome = '''Welcome to pyBirthdays! Select one of the following options: 
    (1) Enter a famous person's name
    (2) Enter a date
    (3) Enter a profession and a desired number of records to be returned
    (4) Enter a birth sign and a desired number of records to be returned'''

    print(welcome)

    option = input()

    if option == "1":
        name = input("Enter a famous person's name to see their birthday: ")
        get_birthday(name)
    else:
        print("Coming soon to pyBirthdays!")

main()