from astronaut import Astronaut

room_list={"engine":"", "cabin":"", "bridge":"", "control":"", "shield":""}

room_key={"e":"engine", "c":"cabin", "b":"bridge", "s":"shield", "n":"control"}

class Ship:
    def __init__(self, name):
        self.name = name
        self.room_list = room_list
        self.room_count=len(room_list)

    def get_empty_rooms(self):
        for x in room_list:
            if room_list[x] == "":
                print(list(room_key.keys())[list(room_key.values()).index(x)], x)

    def print_rooms(self):
        for x in room_list:
            print(x, room_list[x])

    def room_menu(self, astronaut_list):
        print("These rooms are empty: ")
        self.get_empty_rooms()
        print("")
        print("Astronaut Info: ")
        for x in astronaut_list:
            x.get_info()
        print("")
        print("Using the single character id")
        room=input("Which room would you like to assign? ")
        while room not in room_key:
            room=input("Which room would you like to assign? ")
        print("Using the astronaut ID number")
        person=int(input("Which astronaut would you like to assign? "))
        while person < 0 or person > len(astronaut_list):
            person=int(input("Which astronaut would you like to assign"))

        #room_list[room_key[room]]=astronaut_list[person]
        room_list[room_key[room]]=astronaut_list[person].id
        astronaut_list[person].room=room_key[room]
    