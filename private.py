#program for private variables

class ABC:

    __name="bitlabs"

    def m1(self):

        print(self.__name)

class XYZ(ABC):

    def m2(self):

        print("hi")

obj=XYZ()

obj.m2()
        