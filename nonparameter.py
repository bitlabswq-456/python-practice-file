#example for non-parameterized constructor

class item:

    def __init__(self):

        self.name="harika"

        self.id=456
        
        self.city="vijayawada"

    def display(self):

        print(self.name,self.id,self.city)

obj=item()

obj.display()