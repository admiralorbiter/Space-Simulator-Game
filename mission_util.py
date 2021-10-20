import random
from mission import Mission

mission_types=["rescue", "salvage", "steal"]

class Mission_Util():

    def randomly_choose():
        def Rescue_Mission():
            return Mission(mission_types[0], "Rescue Something", 5)

        def Salvage_Mission():
            return Mission(mission_types[1], "Salvage Something", 5)

        def Steal_Mission():
            return Mission(mission_types[2], "Steal Something", 5)

        r=random.randint(1, len(mission_types))-1
        type=mission_types[r]
        if type=="rescue":
            return Rescue_Mission()
        elif type=="salvage":
            return Salvage_Mission()
        elif type=="steal":
            return Steal_Mission()

    
    
