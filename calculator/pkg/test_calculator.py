from pkg.calculator import Calculator

calculator = Calculator()
try:
    result = calculator.evaluate("7 * 2")
    print(result)
except Exception as e:
    print(f"Error: {e}")