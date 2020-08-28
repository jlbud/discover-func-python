def abc():
    print("this is middle")


# 被别的模块导入时也会执行
print("running anyway anywhere")

# 当模块abc()被导入时，下面代码不会执行
if __name__ == '__main__':
    print("this is before")
    abc()
    print("this is after")
