import pytest
from pybirthdayspackage import pybirthdays


class Tests:

    #
    # Fixtures - these are functions that can do any optional setup or teardown before or after a test function is run.
    #

    @pytest.fixture
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
        '''verify that get_birthday() returns a non-empty string when input is valid'''

        name = 'Justin Bieber'
        result = pybirthdays.get_birthday(name)
        assert isinstance(
            result, str), f"Expected get_birthday() to return a string. Instead, it returned {result}"
        assert len(
            result) > 0, f"Expected get_birthday() not to be empty. Instead, it returned a string with {len(result)} characters"

    def test_get_birthdays_invalidInput(self):
        '''verify that get_birthday() returns an error string when input is invalid'''

        name = "Not a Real Name"
        errorMessage = "Sorry! " + name + " is not in our database..."
        result = pybirthdays.get_birthday(name)
        assert isinstance(
            result, str), f"Expected get_birthday() to return a string. Instead, it returned {result}"
        assert len(
            result) > 0, f"Expected get_birthday() not to be empty. Instead, it returned a string with {len(result)} characters"
        assert result == errorMessage, f"Expected get_birthday() to return a message stating {errorMessage}. Instead, it returned {result}"

    def test_get_birthdays_validInput(self):
        '''verify that get_birthday() returns the correct birthday when input is valid'''

        name = 'Justin Bieber'
        birthday = "Justin Bieber's Birthday is on: March  1, 1994"
        result = pybirthdays.get_birthday(name)
        assert result == birthday, f"Expected get_birthday() to return a message stating {birthday}. Instead, it returned {result}"

    def test_get_people(self):
        '''verify that get_people() returns a non-empty list when input is valid'''

        date = "December 27"
        result = pybirthdays.get_people(date)
        assert isinstance(
            result, list), f"Expected get_people() to return a list. Instead, it returned {result}"
        assert len(
            result) > 0, f"Expected get_people() not to be empty. Instead, it returned a list with {len(result)} items"

    def test_get_people_invalidInput(self):
        '''verify that get_people() returns an error string when input is invalid'''

        for date in ["June 33", "Apr.1"]:
            result = pybirthdays.get_people(date)
            errorMessage = "Sorry! That does not look like a valid date..."
            assert isinstance(
                result, str), f"Expected get_people() to return a string. Instead, it returned {result}"
            assert len(
                result) > 0, f"Expected get_people() not to be empty. Instead, it returned a string with {len(result)} characters"
            assert result == errorMessage, f"Expected get_people() to return a message stating {errorMessage}. Instead, it returned {result}"

    def test_get_people_validInput(self):
        '''verify that get_people() returns the correct birthday when input is valid'''

        date = 'March 1'
        name = "Justin Bieber"
        result = pybirthdays.get_people(date)
        assert name in '\t'.join(
            result), f"Expected get_people() to return a list with {name} included. Instead, it returned {result}"

    def test_search_by_profession(self):
        '''verify that search_by_profession() returns a non-empty list when input is valid'''

        profession = "Dancer"
        result = pybirthdays.search_by_profession(profession, 5)
        assert isinstance(
            result, list), f"Expected search_by_profession() to return a list. Instead, it returned {result}"
        assert len(
            result) > 0, f"Expected search_by_profession() not to be empty. Instead, it returned a list with {len(result)} items"

    def test_search_by_profession_invalidInput(self):
        '''verify that search_by_profession() returns an error string when input is invalid'''

        profession = "Fake Profession"
        errorMessage = "Sorry! The profession " + profession + \
            " is not in our database!"
        result = pybirthdays.search_by_profession(profession, 5)
        assert isinstance(
            result, str), f"Expected search_by_profession() to return a string. Instead, it returned {result}"
        assert len(
            result) > 0, f"Expected search_by_profession() not to be empty. Instead, it returned a string with {len(result)} items"
        assert result == errorMessage, f"Expected search_by_profession() to return a message stating {errorMessage}. Instead, it returned {result}"

    def test_search_by_profession_validInput(self):
        '''verify that search_by_profession() returns the correct birthday when input is valid'''

        profession = "Pop Singer"
        name = "Justin Bieber"
        result = pybirthdays.search_by_profession(profession, 10)
        assert name in '\t'.join(
            result), f"Expected search_by_profession() to return a list with {name} included. Instead, it returned {result}"

    def test_search_by_birthsign(self):
        '''verify that search_by_birthsign() returns a non-empty list when input is valid'''

        sign = "Cancer"
        result = pybirthdays.search_by_birthsign(sign, 5)
        assert isinstance(
            result, list), f"Expected search_by_birthsign() to return a list. Instead, it returned {result}"
        assert len(
            result) > 0, f"Expected search_by_birthsign() not to be empty. Instead, it returned a list with {len(result)} items"

    def test_search_by_birthsign_invalidInput(self):
        '''verify that search_by_birthsign() returns an error string when input is invalid'''

        sign = "Fake Profession"
        errorMessage = "Sorry! The birth sign " + sign + \
            " doesn't exist! Please check if your spelling is correct."
        result = pybirthdays.search_by_birthsign(sign, 5)
        assert isinstance(
            result, str), f"Expected search_by_birthsign() to return a string. Instead, it returned {result}"
        assert len(
            result) > 0, f"Expected search_by_birthsign() not to be empty. Instead, it returned a string with {len(result)} items"
        assert result == errorMessage, f"Expected search_by_birthsign() to return a message stating {errorMessage}. Instead, it returned {result}"

    def test_search_by_birthsign_validInput(self):
        '''verify that search_by_birthsign() returns the correct birthday when input is valid'''

        sign = "Pisces"
        name = "Justin Bieber"
        result = pybirthdays.search_by_birthsign(sign, 10)
        assert name in '\t'.join(
            result), f"Expected search_by_birthsign() to return a list with {name} included. Instead, it returned {result}"
