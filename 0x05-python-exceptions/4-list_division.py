#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newArray = []
    for i in range(list_length):
        division = 0
        try:
            division = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            pass
        except TypeError:
            print("wrong type")
            pass
        except IndexError:
            print("out of range")
            pass
        finally:
            newArray.append(division)
    return newArray
