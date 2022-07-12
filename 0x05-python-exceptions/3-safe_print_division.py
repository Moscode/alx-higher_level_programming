#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        solution = a / b
        return solution
    except Exception:
        solution = None
        return solution
    finally:
        print("Inside result: {}".format(solution))
