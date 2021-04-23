class Resistor():
    resistor_values = {20:6,47:6,8:1}
    def __init__(self,res_input):
        self.input = res_input
        
resistor_values = {20:6,47:6,8:1}
resistor_values[20] -= 1
print(resistor_values[20])