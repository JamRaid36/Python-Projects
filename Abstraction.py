from abc import ABC, abstractmethod

class Aircraft(ABC):

    def cargo(self, weight): # regular method
        print("This aircraft can carry: ", weight)

    @abstractmethod
    def flight(self): # abstract method
        pass

class Helicopter(Aircraft):

    def flight(self): # defining abstract method for Helicopter
        print("Helicopters fly by the use of high speed, spinning rotary blades that produce lift")


class Airplane(Aircraft):

    def flight(self): # defining abstract method for Airplane
        print("Airplanes require a constant airflow over it's wings to stay in flight")


    

Heli = Helicopter() # creating object that utilizes child class Helicopter
Heli.flight() # Utilizing parent abstract method for child class Helicopter
Plane = Airplane() # creating object that utilizes child class Airplane
Plane.flight() # Utilizing parent abstract method for child class Airplane
Plane.cargo("2000 lbs") # Utilizing parent regular method for child class Airplane


