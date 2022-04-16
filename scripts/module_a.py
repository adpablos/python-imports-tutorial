# module_a.py
A_CONSTANT = 'I am a string constant within the python module a'


def multiply(number: int, times: int):
    print(times, " times ", number, " is ", times * number)


if __name__ == '__main__':
    multiply(10, 10)
