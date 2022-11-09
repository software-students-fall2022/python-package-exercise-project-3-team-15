
# pyBirthdays

Get to know all the famous people who have birthdays on a specific day (birthdays as a service)

![Badge](https://github.com/software-students-fall2022/python-package-exercise-project-3-team-15/actions/workflows/build.yaml/badge.svg)

## Installation

To install, run `pip install -i https://test.pypi.org/simple/ pybirthdayspackage`

## How to Contribute & Use

After installing the above package and the virtual environment (`pipenv shell`), you can run the tests in the project directory by using the following command: `python3 -m pytest`.

To add to your program, simply import this package: `from pybirthdayspackage import pybirthdays`

## Usage

`get_people(date)` Allow user to input date, return all the famous people who have birthdays on that date

`get_birthday(person)` Allow user to input famous person name, return the birthday of that person if found

`get_profession_birthdays(profession, limit)` Allow user to input a profession and the desired number of outputs, return the top 'x' most popular famous people that have that profession and their birthdays

`search_by_birthsign(birth_sign, limit)` Allow user to input a birth sign and the desired number of outputs, return the top 'x' most popular famous people that have that birth sign and their birthdays

## PyPI

[Link](https://test.pypi.org/project/pybirthdayspackage/)

## Team Members

- [Grace Zhang](https://github.com/gracezhang89)
- [Ishana Goyal](https://github.com/ishana-goyal)
- [Laura Mazoni](https://github.com/qlaueen)
- [Mark Chen](https://github.com/markizenlee)
