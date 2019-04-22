import datetime


def minutes_f():
    minutes = datetime.datetime.now().strftime("%M")
    return minutes


def hours_f():
    hours = datetime.datetime.now().strftime("%H")
    return hours


def time_f():
    time = datetime.datetime.now().strftime("%B %d")
    return time
