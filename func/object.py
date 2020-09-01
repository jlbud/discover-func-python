class Parent:
    w = 0
    r = 0

    def __init__(self, r=0, w=0):
        self.r = r
        self.w = w

    def val(self):
        n = self.w + self.r
        print(n)


class Children(Parent):
    subr = 0
    subw = 0

    def __init__(self, subr=0, subw=0, r=0, w=0):
        Parent.__init__(self, r=r, w=w)
        self.subr = subr
        self.subw = subw

    def val(self):
        n = self.subr + self.subw + self.r + self.w
        print(n)


s = Children(subr=100, subw=100, r=1, w=1)
s.val()
