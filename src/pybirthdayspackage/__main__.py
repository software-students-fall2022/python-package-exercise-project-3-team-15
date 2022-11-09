import pybirthdayspackage.pybirthdays as pybirthdays


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
        result = pybirthdays.get_birthday(name)
        # return result
    elif option == "2":
        date = input("Enter a date (Month Day): ")
        result = pybirthdays.get_people(date)
        # return result
    elif option == "3":
        profession = input("Enter a profession: ")
        limit = input("Enter the desired number of records: ")
        result = pybirthdays.search_by_profession(profession, limit)
        # return result
    elif option == "4":
        birth_sign = input("Enter a birth sign from the following 12: " +
                           "Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius and Pisces.\n")
        limit = input("Enter the desired number of records: ")
        result = pybirthdays.search_by_birthsign(birth_sign, limit)
        # return result
    else:
        result = None

    if isinstance(result, list):
        for elem in result:
            print(elem)
    else:
        print(result)


if __name__ == '__main__':
    main()
