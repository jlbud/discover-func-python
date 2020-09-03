from time import sleep

for i in range(100):
    # end默认是\n换行，所以要设置为""，
    # \r表示将光标移动到行首，
    # j就可以实现同一行重复打印
    print("\r", "进度是{:.0f}%".format(i + 1), end="", flush=True)
    sleep(1)
