class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __str__(self):
        return self.name

class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def say(self, stuff):
        return self.name + ' says: ' + self.lecture(stuff)

class Singer(Lecturer):
    def sing(self, stuff):
        return stuff + ' Tra la la'
    def lecture(self, stuff):
        return self.sing(Lecturer.lecture(self, stuff))

class ArrogantProfessor(Professor):
    def say(self, stuff):
        return 'It is obvious that ' + self.lecture(stuff)


e = Person('eric')
le = Lecturer('eric')
pe = Professor('eric')
se = Singer('eric')
ae = ArrogantProfessor('eric')

# e.say('the sky is blue')
# le.say('the sky is blue')
# le.lecture('the sky is blue')
# pe.say('the sky is blue')  eric says I believe that erics says the 
# pe.lecture('the sky is blue') I believe that erics says the sky 
# pe.sing('the sky is blue') error
# se.say('the sky is blue')
# se.lecture('the sky is blue')
# se.sing('the sky is blue')
ae.lecture('the sky is blue')
I believe that erics say s