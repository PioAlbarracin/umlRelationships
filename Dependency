class Calculator:
    def calculate_given(self, given: str):
        print(f'Calculating: {given}')

class PrintCalculated:
    def __init__(self, content: str):
        self.content = content

    def output_given(self, calculator_device: Calculator):
        calculator_device.calculate_given(self.content)

my_calculator = Calculator()
outputCalculated = PrintCalculated("The calculated is n!")

outputCalculated.output_given(my_calculator)
