from library import Library


class Selection:
    """
    Class that is used to start the game. It's gotten the class selection etc.
    """

    @staticmethod
    def give_nickname():
        return input("Enter username: ")

    @staticmethod
    def class_select():
        print("Choose class:")
        for class_nr, classes in enumerate(Library.PLAYER_CLASSES):
            print(f"{class_nr + 1}. {classes[0]}")
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
        return class_nr_input - 1

    @staticmethod
    def difficulty_select():
        print("Choose difficulty:")
        for diff_nr, diff in enumerate(Library.DIFFICULTIES):
            print(f"{diff_nr + 1}. {diff[0]}")
        while True:
            try:
                diff_nr_input = int(input(""))
                if diff_nr_input > len(Library.DIFFICULTIES):
                    print("The number is incorrect!")
                elif diff_nr_input <= 0:
                    print("The number is incorrect!")
                else:
                    break
            except ValueError:
                print("You have to enter the number! Try again.")
        return diff_nr_input - 1


    def give_difficulty_stats(self):
        diff_nr = self.difficulty_select()
        difficulty_stats = []
        for stat_nr, stat in enumerate(Library.DIFFICULTIES[diff_nr]):
            if stat_nr == 0:
                pass
            else:
                difficulty_stats.append(stat)
        return difficulty_stats

