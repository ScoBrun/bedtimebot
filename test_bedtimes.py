import bedtimes


def testing_get_nap():
    testing_time = '23:55'
    expected_output = {"nap": "00:20"}

    actual_output = bedtimes.get_nap(testing_time)

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
