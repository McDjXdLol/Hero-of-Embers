from library import Library
class Selection:
    """
    Class that is used to start the game. It's gotten the class selection etc.
    """
    @staticmethod
    def giveNickname():
        return input("Enter username: ")

    @staticmethod
    def ClassSelect():
        print("Choose class:")
        for class_nr, classes in enumerate(Library.PLAYER_CLASSES):
            print(f"{class_nr+1}. {classes[0]}")
        while True:
            try:
                class_nr_input = int(input(""))
                if class_nr_input > len(Library.PLAYER_CLASSES):
                    print("The number is incorrect!")
                elif class_nr_input <= 0:
                    print("The number is incorrect!")
                else:
                    break
            except ValueError:
                print("You have to enter the number! Try again.")
        return class_nr_input-1
