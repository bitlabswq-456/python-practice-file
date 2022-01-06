#example for parameterized constructor

class item:

    def __init__(self,name,id,city):

        self.name=name

        self.id=id

        self.city=city

    def display(self):

        print(self.name,self.id,self.city)

obj=item("harika",456,"vijayawada")

obj.display()