import random
from supplies import Supplies
item_types=["medkit", "food"]

class Supplies_Util():

  def randomly_choose(supplies):
    r=random.randint(1, len(item_types))-1
    return Supplies(item_types[r], 3);