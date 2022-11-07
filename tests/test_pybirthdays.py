import pytest
from pybirthdayspackage import pybirthdays

class Tests:

    #
    # Fixtures - these are functions that can do any optional setup or teardown before or after a test function is run.
    #

    def example_fixture(self):
        '''
        An example of a pytest fixture - a function that can be used for setup and teardown before and after test functions are run.
        '''

        # place any setup you want to do before any test function that uses this fixture is run

        yield  # at th=e yield point, the test function will run and do its business

        # place with any teardown you want to do after any test function that uses this fixture has completed

    #
    # Test functions
    #

    def test_sanity_check(self, example_fixture):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"

    def test_get_birthdays(self):
        '''verify that get_birthday() returns a non-empty string 
        (either a person's birthday or an error message saying the person is not in the database)'''

        # since get_birthday takes a person's name, test on multiple names (both those that exist, don't exist, and are formatted strangely)

        for name in ['Justin Bieber', 'lisa KuDROw', 'John Applesmith', 'Derek Jeter', 'hasan minhaj']:
            result = pybirthdays.get_birthday(name)
            assert isinstance(
                result, str), f"Expected get_birthday() to return a string. Instead, it returned {result}"
            assert len(
                result) > 0, f"Expected get_birthday() not to be empty. Instead, it returned a string with {len(result)} characters"

    def test_get_people(self):
        '''verify that get_people() returns a non-empty string 
        (either a list of people born on that date or an error message saying the date is not valid)'''

        # since get_people takes a date, test on multiple formats (correct and incorrect)

        for date in ['December 27', 'June 51', 'ApRIl11']:
            result = pybirthdays.get_people(date)
            assert isinstance(
                result, str), f"Expected get_people() to return a string. Instead, it returned {result}"
            assert len(
                result) > 0, f"Expected get_people() not to be empty. Instead, it returned a string with {len(result)} characters"

    def test_search_by_profession(self):
        '''verify that search_by_profession() returns a non-empty string 
        (either a list of people in that profession and their birthday or an error message saying the profession is not in the database)'''

        # since search_by_profession takes a profession, test on multiple professions (those that exist, don't exist, and are formatted strangely)

        for profession in ['Dancer', 'movie AcTreSS', 'Fake Profession', 'us president']:
            result = pybirthdays.search_by_profession(profession, 5)
            assert isinstance(
                result, str), f"Expected search_by_profession() to return a string. Instead, it returned {result}"
            assert len(
                result) > 0, f"Expected search_by_profession() not to be empty. Instead, it returned a string with {len(result)} characters"

    def test_search_by_birthsign(self):
        '''verify that search_by_profession() returns a non-empty string 
        (either a list of people with that birth sign and their birthday or an error message saying the sign is not in the database)'''

        # since search_by_profession takes a profession, test on multiple professions (those that exist, don't exist, and are formatted strangely)

        for sign in ['Cancer', 'LiBra', 'Zodiac', 'scorpio']:
            result = pybirthdays.search_by_birthsign(sign, 5)
            assert isinstance(
                result, str), f"Expected test_search_by_birthsign() to return a string. Instead, it returned {result}"
            assert len(
                result) > 0, f"Expected test_search_by_birthsign() not to be empty. Instead, it returned a string with {len(result)} characters"
