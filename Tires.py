class Bicycle:
    def __init__(self):
        self.tires = self.add_tires()
    def add_tires(self):
        return GenericTires()
    def get_tire_type(self):
        return self.tires.tire_type()

class MountainBike(Bicycle):
    def add_tires(self):
        return MountainTires()
    
class GenericTires:
    def tire_type(self):
        return 'generic'

class MountainTires:
    def tire_type(self):
        return 'mountain'
mountain_bike = MountainBike()
print(mountain_bike.get_tire_type())
