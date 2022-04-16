# module_d.py
import utils

no_capitalized = "bla bla bla"
capitalized = utils.capitalize(no_capitalized)
print(capitalized)

to_evaluate = "123d123"
print("Is ", to_evaluate, " numeric? >> ", utils.is_numeric(to_evaluate))

rest = utils.module(23, 7)
print("The rest is: ", rest)