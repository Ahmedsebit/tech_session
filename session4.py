class School:
    
    def __init__(self, name):
        self.name = name
        self.classes = []
        
    def add_details(self, location, principal):
        self.location = location
        self.principal = principal
        
    def add_class(self, class_name):
        self.classes.append(class_name)
        
        
class Classes:
    
    def __init__(self, name):
        self.name = name
        self.students = []
        
    def add_details(self, teacher):
        self.teacher = teacher
        
    
    

school = School('Olympic Primary')
school.add_details("Olympic", "Mr")

class_name = Classes('1 red')

school.add_class(class_name)

print(school.location, school.principal, [i.name for i in school.classes])
 