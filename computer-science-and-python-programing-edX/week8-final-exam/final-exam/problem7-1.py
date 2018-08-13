class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        self.before = before
    def setAfter(self, after):
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    # Your Code Here 

    # left
    if newFrob.myName()<atMe.myName():
        t=atMe
        while True:
            if t.getBefore() is not None:
                if newFrob.myName()<t.myName():
                    t= t.getBefore() 
                else:
                    tnext=t.getAfter()
                    tnext.setBefore(newFrob)
                    newFrob.setAfter(tnext)
                    t.setAfter(newFrob)
                    newFrob.setBefore(t)
                    break
            else:
                newFrob.setAfter(t)
                newFrob.setBefore(None)
                t.setBefore(newFrob)
                break
    else:
        # right
        t=atMe
        while True:
            if t.getAfter() is not None:
                if t.myName()<=newFrob.myName()<t.getAfter().myName():
                    tnext=t.getAfter()
                    tnext.setBefore(newFrob)
                    newFrob.setAfter(tnext)
                    newFrob.setBefore(t)
                    t.setAfter(newFrob)
                    break
                else:
                    t=t.getAfter()
            else:
                t.setAfter(newFrob)
                newFrob.setAfter(None)
                newFrob.setBefore(t)
                break

def prt(root):
    while True:
        if root.getAfter() is not None:
            print(root.myName(),'-->',end='')
            root=root.getAfter()
        else:
            print(root.myName())
            break


eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')
insert(eric,andrew)
insert(eric, fred)
insert(eric, ruth)

prt(eric)
insert(ruth, martha)
prt(andrew)