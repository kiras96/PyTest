import time

log_file = open('../log.txt', 'a')


def get_local_time():
    my_time = time.strftime("%d.%m.%Y %H:%M", time.localtime())
    return my_time


class Logger:

    @staticmethod
    def write_log(message):
        log_file.write(message + "\n")
