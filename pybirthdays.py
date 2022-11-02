import requests
from bs4 import BeautifulSoup


def get_birthday(person):
    name_cleaned = person.lower().replace(" ", "-").replace("'", "-")

    url = "https://www.famousbirthdays.com/people/" + name_cleaned + ".html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    main_div = soup.find("div", {"class": "stat box"})

    try:
        month = main_div.find("span", {"class": "hidden-sm"})
        day = main_div.find("a")
        year = main_div.find_all("a")
        print(person, "'s Birthday is on: ", month.text, " ", day.text[-2:], ", ", year[-1].text, sep='')
    except:
        print("Sorry!", person, "is not in our database...")

def get_people(date):
    clean_date = date.lower().replace(" ", "")
    url = "https://www.famousbirthdays.com/" + clean_date + ".html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    main_div = soup.find("div", {"class":"list-page"})

    try:
        first_row = main_div.find_all("div", {"class":"row"})
        names = first_row[1].find_all("div", {"class":"name"})
        for elem in names:
            print(elem.text.strip())
    except:
        print("Sorry! That does not look like a valid date...")
        
def get_profession_birthdays(profession, limit):
    profession_cleaned = profession.lower().replace(" ", "")
    url = "https://www.famousbirthdays.com/profession/" + profession_cleaned + ".html"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    people = soup.find_all("div", {"class": "name"})

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        people = soup.find_all("div", {"class": "name"})

        for i in range(limit):
            print(people[i])
            data = people[i].text
            person = data.split(",")[0]
            get_birthday(person)
    except:
        print("Sorry!", profession, "is not in our database...")

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
    elif option == "3":
        profession = input("Enter a profession: ")
        limit = input("Enter the desired number of records: ")
        get_profession_birthdays(profession, limit)
    elif option == "2":
        date = input("Enter a date (Month Day): ")
        get_people(date)
    else:
        print("Coming soon to pyBirthdays!")


main()
