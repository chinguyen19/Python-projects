"""
COMP.CS.100 | Programming 1 | Fall 2020
Tampere University
Students: Nguyễn Hữu Linh Chi | Steeven Buitrago Hernández
Student ID Numbers: 050358427 | 050358566
chi.nguyen@tuni.fi
steeven.buitragohernandez@tuni.fi
Project: Accesscontrol.
"""

DOORCODES = {'TC114': ['TIE'], 'TC203': ['TIE'], 'TC210': ['TIE', 'TST'],
             'TD201': ['TST'], 'TE111': [], 'TE113': [], 'TE115': [],
             'TE117': [], 'TE102': ['TIE'], 'TD203': ['TST'], 'TA666': ['X'],
             'TC103': ['TIE', 'OPET', 'SGN'], 'TC205': ['TIE', 'OPET', 'ELT'],
             'TB109': ['OPET', 'TST'], 'TB111': ['OPET', 'TST'],
             'TB103': ['OPET'], 'TB104': ['OPET'], 'TB205': ['G'],
             'SM111': [], 'SM112': [], 'SM113': [], 'SM114': [],
             'S1': ['OPET'], 'S2': ['OPET'], 'S3': ['OPET'], 'S4': ['OPET'],
             'K1705': ['OPET'], 'SB100': ['G'], 'SB202': ['G'],
             'SM220': ['ELT'], 'SM221': ['ELT'], 'SM222': ['ELT'],
             'secret_corridor_from_building_T_to_building_F': ['X', 'Y', 'Z'],
             'TA': ['G'], 'TB': ['G'], 'SA': ['G'], 'KA': ['G']}


class Accesscard:
    """
    This class models an access card which can be used to check
    whether a card should open a particular door or not.
    """

    def __init__(self, id, name):
        """
        Constructor, creates a new object that has no access rights.

        :param id: str, card holders personal id
        :param name: str, card holders name

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME OR THE
        PARAMETERS!
        """

        self.__id = id
        self.__name = name
        self.__raw_access = []
        self.__simplified_access = []
        self.__door_access = []

    def info(self):
        """
        The method has no return value. It prints the information related to
        the access card in the format:
        id, name, access: a1,a2,...,aN
        for example:
        777, Thelma Teacher, access: OPET, TE113, TIE
        Note that the space characters after the commas and semicolon need to
        be as specified in the task description or the test fails.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE PRINTOUT FORMAT!
        """

        string_access = ', '.join(self.__simplified_access)
        print(f"{self.__id}, {self.__name}, access: {string_access}")

    def get_name(self):
        """
        :return: str, the name of the accesscard holder.
        """

        return self.__name

    def get_access(self):
        """
        :return: list, the codes to which the accesscard holder can enter.
        """
        return self.__simplified_access

    def add_access(self, new_access_code):
        """
        The method adds a new accesscode into the accesscard according to the
        rules defined in the task description.

        :param new_access_code: str, the accesscode to be added in the card.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """

        self.__raw_access.append(new_access_code)
        self.__raw_access.sort()

        if new_access_code not in self.__simplified_access:
            self.__simplified_access.append(new_access_code)

        for possible_area_codes in self.__simplified_access:
            for i in DOORCODES:
                if possible_area_codes in DOORCODES[i] and i in \
                        self.__simplified_access:
                    self.__simplified_access.remove(i)
        self.__simplified_access.sort()

        self.__door_access = list.copy(self.__raw_access)
        for door in DOORCODES:
            for area in DOORCODES[door]:
                if area in self.__raw_access:
                    self.__door_access.append(door)
        self.__door_access.sort()

    def check_access(self, door):
        """
        Checks if the accesscard allows access to a certain door.

        :param door: str, the doorcode of the door that is being accessed.
        :return: True: The door opens for this accesscard.
                 False: The door does not open for this accesscard.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """

        if door in self.__door_access:
            return True
        else:
            return False

    def merge(self, card):
        """
        Merges the accesscodes from another accesscard to this accesscard.

        :param card: Accesscard, the accesscard whose access rights are
        added to this card.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """

        new_access_list = card.get_access()
        for permission in new_access_list:
            self.add_access(permission)


def main():

    try:
        file = open('accessinfo.txt', mode="r")
    except OSError:
        print("Error: file cannot be read.")
        return
    info_dict = {}
    for file_lines in sorted(file):
        id_number, name, access = file_lines.rstrip().split(";")
        access = access.split(",")
        info_dict[id_number] = Accesscard(id_number, name)
        for permission in access:
            info_dict[id_number].add_access(permission)
    file.close()

    areacodes = []
    for door in DOORCODES:
        for area in DOORCODES[door]:
            if area not in areacodes:
                areacodes.append(area)
    areacodes.sort()

    while True:
        line = input("command> ")

        if line == "":
            break

        strings = line.split()
        command = strings[0]

        if command == "list" and len(strings) == 1:
            for id_code in info_dict:
                info_dict[id_code].info()

        elif command == "info" and len(strings) == 2:
            try:
                if strings[1] not in info_dict:
                    raise KeyError
                card_id = strings[1]
                info_dict[card_id].info()
            except KeyError:
                print('Error: unknown id.')

        elif command == "access" and len(strings) == 3:
            card_id = strings[1]
            door_id = strings[2]

            try:
                if card_id not in info_dict:
                    raise KeyError
                elif door_id not in DOORCODES:
                    raise ValueError
                else:
                    if info_dict[card_id].check_access(door_id):
                        print(f'Card {card_id} ('
                              f' {info_dict[card_id].get_name()} ) has '
                              f'access to door {door_id}')
                    else:
                        print(f'Card {card_id} ('
                              f' {info_dict[card_id].get_name()} ) has no '
                              f'access to door {door_id}')
            except KeyError:
                print('Error: unknown id.')
            except ValueError:
                print('Error: unknown doorcode.')

        elif command == "add" and len(strings) == 3:
            card_id = strings[1]
            access_code = strings[2]
            try:
                if card_id not in info_dict:
                    raise KeyError
                elif access_code not in DOORCODES and access_code not in \
                        areacodes:
                    raise ValueError
                else:
                    info_dict[card_id].add_access(access_code)
            except KeyError:
                print('Error: unknown id.')
            except ValueError:
                print('Error: unknown accesscode.')

        elif command == "merge" and len(strings) == 3:
            card_id_to = strings[1]
            card_id_from = strings[2]
            try:
                if card_id_to not in info_dict or card_id_from not in \
                        info_dict:
                    raise ValueError
                info_dict[card_id_to].merge(info_dict[card_id_from])
            except ValueError:
                print('Error: unknown id.')

        elif command == "quit":
            print("Bye!")
            return
        else:
            print("Error: unknown command.")


if __name__ == "__main__":
    main()
