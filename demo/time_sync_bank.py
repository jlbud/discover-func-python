import datetime
import threads_read_txt


def func():
    print("running task")
    # 每天
    threads_read_txt.Timer(86400, func).start()


def run():
    # 获取现在时间
    now_time = datetime.datetime.now()
    year = now_time.date().year
    month = now_time.date().month
    day = now_time.date().day
    # 定时器触发时间
    recently_time = datetime.datetime.strptime(str(year) + "-" + str(month) + "-" + str(day) + " 14:54:00",
                                               "%Y-%m-%d %H:%M:%S")
    print("recently_time:", recently_time)
    print("now_time", now_time)
    if recently_time > now_time:
        timer_start_time = (recently_time - now_time).total_seconds()
        print("remain seconds: %s" % timer_start_time)
        timer = threads_read_txt.Timer(timer_start_time, func)
        timer.start()
    else:
        now_time = datetime.datetime.now()
        next_time = now_time + datetime.timedelta(days=+1)
        recently_time = datetime.datetime.strptime(
            str(next_time.date().year) + "-" + str(next_time.date().month) + "-" + str(
                next_time.date().day) + " 14:54:00",
            "%Y-%m-%d %H:%M:%S")
        timer_start_time = (recently_time - now_time).total_seconds()
        threads_read_txt.Timer(timer_start_time, func).start()
        print("remain seconds: %s" % 86400)


# nohup python3 time_sync.py >> ./my.log 2>&1 &
if __name__ == '__main__':
    run()
