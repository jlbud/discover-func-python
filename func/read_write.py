def read_file(filepath):
    str = ""
    fp = open(filepath)
    content = fp.readlines()
    for c in content:
        str += c.replace('\n', ' ')
    fp.close()
    return str


ret = read_file('file')
print(ret)
