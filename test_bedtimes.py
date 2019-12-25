import pytest

import bedtimes


def testing_get_nap():
    """
    Testing for get_nap method.

    Returns: null

    """

    testing_time = '23:55'
    expected_output = {"nap": "00:20"}

    sleeping_time = bedtimes.get_requested_time(testing_time)
    actual_output = bedtimes.get_naptime(sleeping_time)

    assert actual_output == expected_output


def testing_times_to_wake_up():
    """
    Testing for times_to_wake_up method.

    Returns: null

    """

    testtime = '00:30'

    expected_output = {
        "nap": "00:55",
        "1": "02:15",
        "2": "03:45",
        "3": "05:15",
        "4": "06:45",
        "5": "08:15",
        "6": "09:45"
    }

    actual_output = bedtimes.times_to_wake_up(testtime)

    assert actual_output == expected_output


def testing_times_to_sleep_at():
    """
    Testing for times_to_sleep_at method.

    Returns: null

    """

    testtime = '10:00'

    expected_output = {
        '1': '08:45',
        '2': '07:15',
        '3': '05:45',
        '4': '04:15',
        '5': '02:45',
        '6': '01:15',
        '7': '23:45',
        '8': '22:15'}

    actual_output = bedtimes.times_to_sleep_at(testtime, 8)

    assert actual_output == expected_output


def testing_validate_input_time_successful():
    """
    Testing for validate_input_time method.
    Should be successful if it can parse the time.

    Returns: null

    """
    assert bedtimes.validate_input_time('10:00') == True


def testing_validate_input_time_fail():
    """
    Testing for validate_input_time method.
    Should throw error for test to be successful.

    Returns: null

    """
    with pytest.raises(ValueError):
        bedtimes.validate_input_time('10comma00')
