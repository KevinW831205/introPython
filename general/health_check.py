import shutil
import psutil
import time
import socket

import general.emails as emails


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 80


def check_memory():
    available = psutil.virtual_memory()[1]
    return available > 524288000  # 500 MB in bytes


def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"


def send_error(subject):
    message = emails.generate_email("automation@example.com", "student-02-5bece8f61bcc@example.com", subject,
                                    "Please check your system and resolve the issue as soon as possible", None)
    emails.send_email(message)


def run_checks():
    if not check_memory():
      #  send_error("Error - Available memory is less than 500MB")
        print("memory")
    if not check_cpu_usage():
        #send_error("Error - CPU usage is over 80%")
        print("cpu")
    if not check_disk_usage("/"):
        #send_error("Error - Available disk space is less than 20%")
        print("disk")
    if not check_localhost():
        #send_error("Error - localhost cannot be resolved to 127.0.0.1")
        print("network")

if __name__ == '__main__':
    run_checks()
    # starttime = time.time()
    # while True:
    #     # run_checks()
    #     print("ran")
    #     time.sleep(60.0 - ((time.time() - starttime) % 60.0))


# cron job   * * * * * ~/health_check.py