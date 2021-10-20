from astronaut import Astronaut
from mission_util import Mission_Util
from supplies_util import Supplies_Util
from supplies import Supplies
from ship import Ship

NUM_ASTRONAUTS=3
astronaut_list=[]
supplies={}

def select_astro():
  for i in range(NUM_ASTRONAUTS):
    astronaut_list.append(Astronaut("Jon", 32, i))

def test_display_astro():
  for i in range(NUM_ASTRONAUTS):
    print(astronaut_list[i].id, astronaut_list[i].name, astronaut_list[i].age, astronaut_list[i].room)

def select_supplies():
  Supplies_Util.randomly_choose(supplies)

def test_display_supplies():
  print(supplies)
  
def pick_mission():
  mission=Mission_Util.randomly_choose()
  #print(mission.name, mission.description, mission.difficulty)


def take_off():
  print("Taking off...")
  pick_mission()

select_astro()
test_display_astro()
select_supplies();
test_display_supplies()
take_off()

print("")
ship=Ship("UFO")
ship.room_menu(astronaut_list)

test_display_astro()
ship.print_rooms()


  