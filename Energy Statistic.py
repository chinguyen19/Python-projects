"""
COMP.CS.100 | Programming 1 | Fall 2020
Tampere University
Students: Nguyễn Hữu Linh Chi | Steeven Buitrago Hernández
Student ID Numbers: 050358427 | 050358566
chi.nguyen@tuni.fi
steeven.buitragohernandez@tuni.fi
Outputs a logarithmic histogram of integer energy consumption measurements
entered by the user.
"""


def read_number(prompt):
    """Asks the user for a numeric input and returns it if it's positive.
    Also, if the user enters an empty line, returns an empty string (this is to
    trigger other functions' features). If none of these two conditions are
    met, asks over and over until a valid input is given.

    :param prompt: str,
        The message to be displayed before the user input
        space.
    :returns: int or str,
        Depending on the entered value, returns a positive
        integer or an empty string.
    """
    entered_value = input(prompt)
    try:
        if entered_value == "":
            return ""
        elif int(entered_value) >= 0:
            return int(entered_value)
        else:
            print(f"You entered: {entered_value}."
                  f" Enter non-negative numbers only!")
            return read_number(prompt)
    except ValueError:
        print(f"You entered: {entered_value}."
              f" Enter non-negative numbers only!")
        return read_number(prompt)


def read_consumption():
    """Reads the energy consumptions entered by the user, saves the values
    in a list, and returns the list when an empty string is entered.

    :return: list,
        Each element is an error-checked value entered by the user.
    """
    list = []
    while True:
        new_line = read_number("Enter energy consumption (kWh): ")
        if new_line == "":
            break
        list.append(new_line)
    return list


def maximum_class(data_list):
    """Returns the largest logarithmic class for a given set of data.

    :param data_list: list,
        The set of data to be analysed and whose maximum
        logarithmic class will be returned.
    :return: int,
        The maximum logarithmic class in which at least one
        element of <data_list> is present.
    """
    max_class_number = 0

    # There's a special case for this program when it comes to interpret the
    # logarithmic classes as a geometric series, that case occurs when the
    # maximum value for the consumption is 0. According to the instructions,
    # the first class includes 0 (instead of being 1-9), that's why this
    # function will include it "manually".
    if max(data_list) == 0:
        return 1
    else:
        while max(data_list) >= 10 ** max_class_number:
            max_class_number += 1
    return max_class_number


def class_minimum_value(class_number):
    """Returns the lower bound for an ordered logarithmic class number.

    :param class_number: int,
        The number of the logarithmic class whose
        lower bound is wanted.
    :return: int,
        The lower bound for the logarithmic class number
        <class_number>.
    """
    return 10 ** class_number // 100 * 10


def class_maximum_value(class_number):
    """Returns the upper bound for an ordered logarithmic class number.

    :param class_number: int,
        The number of the logarithmic class whose
        upper bound is wanted.
    :return: int,
        The upper bound for the logarithmic class number
        <class_number>.
    """
    return 10 ** class_number - 1


def numbers_in_each_class(values_list, largest_class):
    """Counts the number of values in a given list that belong to each
    logarithmic class, and returns a list containing such quantities.

    :param values_list: list,
        The data set whose values need to be classified.
    :param largest_class: int,
        The largest possible logarithmic class to
        which an element of <values_list> can belong.
    :return: list,
        Each element states the number of values in
        <values_list> that are included in the scope of the respective
        logarithmic class.
    """
    # First, we'll set two needed lists: one will contain the number of each
    # of the logarithmic classes and the other will be created to have enough
    # room to store the number of values belonging to those logarithmic
    # classes.
    classes_list = list(range(1, largest_class + 1))
    count_list = [0] * largest_class

    # This nested loop syncs the indexes of the classes list and the list
    # containing the number of values inside each class.
    for i in range(len(values_list)):
        for j in range(largest_class):
            if class_minimum_value(classes_list[j]) <= values_list[i] <=\
                    class_maximum_value(classes_list[j]):
                count_list[j] += 1
    return count_list


def print_single_histogram_line(class_number, count, largest_class_number):
    """Prints one correctly indented histogram line as described
    in the assignment instructions.

    :param class_number: int,
        Expresses which consumption class (1, 2, 3, ...)
        should the histogram line be printed for. The <class_number> is used
        to decide which value range (0-9, 10-99, 100-999, ...) should be
        printed in front of the histogram markers ("*").

    :param count: int,
        How many of the values entered by the user belong to <class_number>.

    :param largest_class_number: int,
        What is the largest class out of all input values
        the user entered. This is needed when deciding the indentations
        for all other histogram lines.  For example, if the largest
        number the user entered was 91827364 (8 digits) the value
        of this parameter should be 8.
    """

    # <range_string> represents the range of the values the line's
    # histogram will represent in the printout.  For example "1000-9999".

    min_value = class_minimum_value(class_number)
    max_value = class_maximum_value(class_number)
    range_string = f"{min_value}-{max_value}"

    # How many characters will the largest class' range need when printed.
    # For example if the <largest_class_number> is 7, it would print
    # "1000000-9999999" in the beginning of the line and requires 15
    # characters. This value defines the print width for all the other
    # <range_string>'s.

    largest_width = 2 * largest_class_number + 1

    # Now all the preparations have been done and we can print the
    # histogram line with the correct number of whitespaces in the
    # beginning of the line followed by the correct number of '*'
    # characters. ">" character in the following f-string places
    # <range_string>'s value to the right edge of the output field
    # (filler white spaces will be printed in the beginning).

    print(f"{range_string:>{largest_width}}: {'*' * count}")


def main():
    print("Enter energy consumption data.")
    print("End by entering an empty line.")
    print()

    # If the user enters an empty line as their only input or, in the other
    # hand, if they don't enter a single valid input (positive integers),
    # at some point an exception will occur since the list containing valid
    # data will be empty and there's some operators depending on at least
    # one numeric value. In such case, the program will print a message
    # notifying that there's nothing to print and will end.
    try:
        input_data = read_consumption()
        largest_class = maximum_class(input_data)
        classes_list = list(range(1, largest_class + 1))
        values_per_class = numbers_in_each_class(input_data, largest_class)
        for index in range(largest_class):
            print_single_histogram_line(classes_list[index], values_per_class[
                index], largest_class)
    except ValueError:
        print("Nothing to print. Done.")


if __name__ == "__main__":
    main()
