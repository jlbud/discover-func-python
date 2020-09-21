class Config:
    def __init__(self, staff, org):
        self.staff = staff
        self.org = org

    def getStaff(self):
        return self.staff

    def getOrg(self):
        return self.org
