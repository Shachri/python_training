from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, address=None, id=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.id = id

    def __repr__(self):
        return '%s %s %s, %s,%s' % (self.lastname, self.firstname, self.middlename, self.address, self.id)

    def __eq__(self, other):
        return self.lastname == other.lastname, self.firstname == other.firstname, self.middlename == other.middlename, self.address == other.address

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
