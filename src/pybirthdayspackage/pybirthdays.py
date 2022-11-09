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

        result = person + "'s Birthday is on: " + \
            month.text.strip() + " " + day.text[-2:] + ", " + year[-1].text
        # print(person, "'s Birthday is on: ", month.text, " ",
        #       day.text[-2:], ", ", year[-1].text, sep='')

        return result
    except:
        error_message = "Sorry! " + person + " is not in our database..."
        return error_message
        #print("Sorry!", person, "is not in our database...")


def get_people(date):
    clean_date = date.lower().replace(" ", "")
    url = "https://www.famousbirthdays.com/" + clean_date + ".html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    main_div = soup.find("div", {"class": "list-page"})

    try:
        first_row = main_div.find_all("div", {"class": "row"})
        names = first_row[1].find_all("div", {"class": "name"})

        result = list()

        for elem in names:
            result.append(elem.text.strip())
            # print(elem.text.strip())
        return result
    except:
        error_message = "Sorry! That does not look like a valid date..."
        return error_message
        # print("Sorry! That does not look like a valid date...")


def search_by_profession(profession, limit=5):
    profession_cleaned = profession.lower().replace(" ", "")
    url = "https://www.famousbirthdays.com/profession/" + profession_cleaned + ".html"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        title = soup.find("title").text
        if "Page Not Found" in title:
            error_message = "Sorry! The profession " + profession + \
                " is not in our database!"
            return error_message
        else:
            people = soup.find_all("div", {"class": "name"})
            result_list = list()
            for i in range(int(limit)):
                data = people[i].text
                person = data.split(",")[0]
                result = get_birthday(person.strip())
                result_list.append(result)

            return result_list
    except:
        error_message = "Sorry! " + profession + " is not in our database..."
        return error_message
        #print("Sorry!", profession, "is not in our database...")


def search_by_birthsign(birth_sign, limit=5):
    birth_sign_cleaned = birth_sign.lower()
    url = "https://www.famousbirthdays.com/astrology/" + birth_sign_cleaned + ".html"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find("title").text
    if "Page Not Found" in title:
        error_message = "Sorry! The birth sign " + birth_sign + \
            " doesn't exist! Please check if your spelling is correct."
        return error_message
    else:
        people = soup.find_all("div", {"class": "name"})

        result_list = list()

        for i in range(int(limit)):
            try:
                data = people[i].text
            except:
                break
            person = data.split(", ")[0]
            result = get_birthday(person.strip())
            result_list.append(result)

        return result_list


# def main():

#     welcome = '''Welcome to pyBirthdays! Select one of the following options:
#     (1) Enter a famous person's name
#     (2) Enter a date
#     (3) Enter a profession and a desired number of records to be returned
#     (4) Enter a birth sign and a desired number of records to be returned'''

#     print(welcome)

#     option = input()

#     if option == "1":
#         name = input("Enter a famous person's name to see their birthday: ")
#         result = get_birthday(name)
#         return result
#     elif option == "2":
#         date = input("Enter a date (Month Day): ")
#         result = get_people(date)
#         return result
#     elif option == "3":
#         profession = input("Enter a profession: ")
#         limit = input("Enter the desired number of records: ")
#         result = search_by_profession(profession, limit)
#         return result
#     elif option == "4":
#         birth_sign = input("Enter a birth sign from the following 12: " +
#                            "Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius and Pisces.\n")
#         limit = input("Enter the desired number of records: ")
#         result = search_by_birthsign(birth_sign, limit)
#         return result


# result = main()

# if isinstance(result, list):
#     for elem in result:
#         print(elem)
# else:
#     print(result)
