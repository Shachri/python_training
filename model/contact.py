class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, address=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address = address
        self.id = id

    def __repr__(self):
        return '%s %s %s, %s' % (self.lastname, self.firstname, self.middlename, self.address)

    def __eq__(self, other):
        return self.lastname == other.lastname,self.firstname==other.firstname, self.middlename==other.middlename, self.address==other.address
