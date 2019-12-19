import datetime

# TODO - input / error handling.
default_naptime = 25
default_sleepcycles = 6


def times_to_wake_up(time="NOW", number_of_cycles=default_sleepcycles):
    """
    Calculates the times the user should wake up in order to complete the certain sleep cycles.

    Args:
        time: User requested time. Default is "NOW", which uses the current time.
        number_of_cycles: Number of cycles to request. Default is set at default_sleepcycles.

    Returns: Dictionary containing the sleep cycles counted and their times.

    """
    # Get datetime-formatted for user request.
    if time == "NOW":
        requested_time = datetime.datetime.now()
    else:
        requested_time = get_requested_time(time)

    times = get_nap(time)

    # Loop to calculate the rest of the sleep cycles before return.
    for i in range(1, number_of_cycles + 1):
        minutes = 15 + (i * 90)
        cycle_time = requested_time + datetime.timedelta(minutes=minutes)
        times.update({f"{i}_cycle": cycle_time.strftime("%H:%M")})

    return times


def times_to_sleep_at(time, number_of_cycles=default_sleepcycles):
    """
    Calculates the times the user should go to sleep at in order to complete the certain sleep cycles.

    Args:
        time: The time that the user wants to get up at.
        number_of_cycles: Number of cycles to request. Default is set at default_sleepcycles.

    Returns: Dictionary containing the sleep cycles counted and their times.

    """

    # TODO Stub.
    return 0


def get_requested_time(time):
    """
    Converts the user requested time into a usable datetime format.
    This is done in this separate method to help keep the code AMAP.

    Args:
        time: User requested time.

    Returns: Requested time in usable datetime format.

    """
    hours, minutes = map(int, time.split(':'))
    return datetime.datetime.now().replace(hour=hours, minute=minutes)


def get_nap(time, minutes=default_naptime):
    """
    Returns the time a user would wake up at if they were going for a nap.

    Args:
        time: User requested time.
        minutes: User requested minutes to nap. Default is set at default_naptime.

    Returns: The time the user would wake up.

    """

    nap_wakeup_time = get_requested_time(time) + datetime.timedelta(minutes=minutes)
    return {"nap": nap_wakeup_time.strftime("%H:%M")}
