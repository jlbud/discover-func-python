import datetime
import threading

import time


def cycle_time():
    while True:
        # 刷新
        time_now = time.strftime("%H:%M:%S", time.localtime())
        # 此处设置每天定时的时间
        if time_now == "15:25:00":
            # 此处3行替换为需要执行的动作
            print("hello")
            subject = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " 定时发送测试"
            print(subject)
            # 因为以秒定时，所以暂停2秒，使之不会在1秒内执行多次
            time.sleep(2)


def next_time():
    def func():
        print("haha")
        # 如果需要循环调用，就要添加以下方法
        timer = threading.Timer(86400, func)
        timer.start()

    # 获取现在时间
    now_time = datetime.datetime.now()
    # 获取明天时间
    next_time = now_time + datetime.timedelta(days=+1)
    next_year = next_time.date().year
    next_month = next_time.date().month
    next_day = next_time.date().day
    # 获取明天3点时间
    next_time = datetime.datetime.strptime(str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " 15:34:00",
                                           "%Y-%m-%d %H:%M:%S")
    # # 获取昨天时间
    # last_time = now_time + datetime.timedelta(days=-1)

    # 获取距离明天3点时间，单位为秒
    timer_start_time = (next_time - now_time).total_seconds()
    print(timer_start_time)
    # 54186.75975

    # 定时器,参数为(多少时间后执行，单位为秒，执行的方法)
    timer = threading.Timer(timer_start_time, func)
    timer.start()


def tomorrow():
    # 明天
    yesterday = (datetime.date.today() + datetime.timedelta(days=+1)).strftime("%Y-%m-%d")
    print(yesterday)


if __name__ == '__main__':
    tomorrow()
