# module_c.py
import module_string
import module_number

no_capitalized = "bla bla bla"
capitalized = module_string.capitalize(no_capitalized)
print(capitalized)

to_evaluate = "123d123"
print("Is ", to_evaluate, " numeric? >> ", module_string.is_numeric(to_evaluate))

with_upper_case = "I dO NoT thinK THis WiLl WorK..."
in_lower_case = module_string.to_lower_case(with_upper_case)
print(in_lower_case)

rest = module_number.module(23, 7)
print("The rest is: ", rest)
