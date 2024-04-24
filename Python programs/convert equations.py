import re

def desmos_to_excel(expression):
    # Replace 'x' with 'A1'
    expression = expression.replace('x', 'A1')

    # Replace trigonometric functions
    expression = expression.replace('sin', 'SIN')
    expression = expression.replace('cos', 'COS')
    expression = expression.replace('tan', 'TAN')
    expression = expression.replace('asin', 'ASIN')
    expression = expression.replace('acos', 'ACOS')
    expression = expression.replace('atan', 'ATAN')

    # Replace logarithmic functions
    expression = expression.replace('ln', 'LN')
    expression = expression.replace('log', 'LOG')

    # Replace other functions
    expression = expression.replace('abs', 'ABS')
    expression = expression.replace('floor', 'FLOOR')
    expression = expression.replace('ceil', 'CEILING')

    # Correcting the replacement for square root including brackets and \left, \right
    expression = re.sub(r'\\left', r'', expression)
    expression = re.sub(r'\\right', r'', expression)

    # Adding brackets where necessary
    expression = expression.replace('(', '(')
    expression = expression.replace(')', ')')

    # Add multiplication sign (*) where necessary
    expression = re.sub(r'(\d+)([a-zA-Z\(])', r'\1*\2', expression)
    expression = re.sub(r'([a-zA-Z])(\d+)', r'\1*\2', expression)

    return expression

desmos_function = input("Enter the Desmos function: ")
excel_function = desmos_to_excel(desmos_function)
print('Excel function:', excel_function)
