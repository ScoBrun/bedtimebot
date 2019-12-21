import bedtimes


def testing_get_nap():
    testing_time = '23:55'
    expected_output = {"nap": "00:20"}

    sleeping_time = bedtimes.get_requested_time(testing_time)
    actual_output = bedtimes.get_naptime(sleeping_time)

    assert actual_output == expected_output


def testing_times_to_wake_up():
    testtime = '00:30'

    expected_output = {
        "nap": "00:55",
        "1_cycle": "02:15",
        "2_cycle": "03:45",
        "3_cycle": "05:15",
        "4_cycle": "06:45",
        "5_cycle": "08:15",
        "6_cycle": "09:45"
    }

    actual_output = bedtimes.times_to_wake_up(testtime)

    assert actual_output == expected_output


def testing_times_to_sleep_at():
    testtime = '10:00'

    expected_output = {
        '1_cycle': '08:45',
        '2_cycle': '07:15',
        '3_cycle': '05:45',
        '4_cycle': '04:15',
        '5_cycle': '02:45',
        '6_cycle': '01:15',
        '7_cycle': '23:45',
        '8_cycle': '22:15'}

    actual_output = bedtimes.times_to_sleep_at(testtime, 8)

    assert actual_output == expected_output
