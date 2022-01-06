#program for protected variables

class ABC:

    _name="bitlabs"

    def m1(self):

        print(self._name)

class XYZ(ABC):

    def m2(self):

        print(self._name)


obj=XYZ()

obj.m1()

obj.m2()
        