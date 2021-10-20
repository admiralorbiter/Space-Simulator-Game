from astronaut import Astronaut
from supplies_util import Supplies_Util
from supplies import Supplies

NUM_ASTRONAUTS=3
astronaut_list=[]
supplies={}

def select_astro():
  for i in range(NUM_ASTRONAUTS):
    astronaut_list.append(Astronaut("Jon", 32))

def test_display_astro():
  for i in range(NUM_ASTRONAUTS):
    print(astronaut_list[i].name, astronaut_list[i].age)

def select_supplies():
  item=Supplies_Util.randomly_choose(supplies)
  supplies[item.name]=item.amount

def test_display_supplies():
  print(supplies)
  
def pick_mission():
  

def take_off():
  print("Taking off...")
  pick_mission()

select_astro();
test_display_astro();
select_supplies();
test_display_supplies();
take_off();


  