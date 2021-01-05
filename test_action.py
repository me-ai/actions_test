import time


def test_function(number):
    time.sleep(number)
    sleep_time = 'Sleep for'.format(str(number))
    return sleep_time
