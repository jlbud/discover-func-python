import datetime
import threading


def func():
    print("running task")
    # 每天
    threading.Timer(86400, func).start()


def run():
    # 获取现在时间
    now_time = datetime.datetime.now()
    year = now_time.date().year
    month = now_time.date().month
    day = now_time.date().day
    # 距离3点的时间
    recently_time = datetime.datetime.strptime(str(year) + "-" + str(month) + "-" + str(day) + " 15:56:00",
                                               "%Y-%m-%d %H:%M:%S")
    if recently_time > now_time:
        timer_start_time = (recently_time - now_time).total_seconds()
        print("remain seconds: %s" % timer_start_time)
        timer = threading.Timer(timer_start_time, func)
        timer.start()
    else:
        threading.Timer(86400, func).start()
        print("remain seconds: %s" % 86400)


if __name__ == '__main__':
    run()
