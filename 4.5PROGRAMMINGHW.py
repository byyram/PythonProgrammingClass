def seconds_since_midnight(seconds):
    hour_in_seconds = int(input("What hour of the day is it:")) * 60 * 60
    minute_in_seconds = int(input("What minute of the hour is it:")) * 60
    second_in_seconds = int(input("How many seconds:"))

    seconds = hour_in_seconds + minute_in_seconds + second_in_seconds
    print(seconds)
    return seconds

seconds_since_midnight(seconds = 0)