class Astronaut:
      
  room=""

  def __init__(self, name, age, id):
    self.name=name
    self.age=age
    self.id=id

  def get_info(self):
    print("Name: " + self.name, "ID: " + str(self.id))
    print("Age: " + str(self.age), "Room: " + self.room)