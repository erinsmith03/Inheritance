
class Plant:
    def __init__(self,color):
        self.__color = color


    def get_color(self):
        return self.__color


class Flower(Plant):
    def __init__(self,color, petals):
        Plant.__init__(self,color) #have to first call init method for super class, and supply thos attributes
#get color is still available to sub class to use
        self.__petals = petals

    def get_petals(self):
        return self.__petals
