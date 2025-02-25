"""
author: Ryan Gwin
Date Written: 02/22/2025
description: user enters a float value, and clicks on whether to
convert to fahrenheit or celsius
"""

from breezypythongui import EasyFrame, FloatField

class App(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
    
        #add label for post conversion
        self.label = self.addLabel(text = f"Temperature Conversion", row = 0, column = 0, columnspan = 4, sticky='N')
        #add input for temperature
        self.input = self.addFloatField(value=0.0, row = 1, column=0, columnspan=2, sticky='ew')
        self.input.configure(justify="center")
        #add button for conversion
        self.convert_to_f = self.addButton(text = "Convert to Fahrenheit", row = 2, column = 0, state="normal",command=self.convert_to_f)
        self.convert_to_f.configure(width=20)
        self.convert_to_c = self.addButton(text="Convert to Celsius", row=3, column=0, state="normal", command=self.convert_to_c)
        self.convert_to_c.configure(width=20)
        #add label for showing conversion
        self.conversion_label = self.addLabel(text=f"", row = 4, column = 0, sticky="s", columnspan=2)

    #add function for converting to fahrenheit
    def convert_to_f(self):
        #gets float field value on convert button click
        try:
            self.temp = self.input.getNumber()
            if self.temp < (-273.15):
                self.conversion_label["text"] = f"Error: Cannot go below absolute 0 (-237.15{chr(176)}C)"
            else:
                self.conversion_value = ((9/5) * self.temp) + 32
                self.conversion_label["text"] = f"{self.temp}{chr(176)}C = {self.conversion_value:.2f}{chr(176)}F"
        except ValueError:
            self.conversion_label["text"] = "ERROR: Enter a number."

    def convert_to_c(self):
        try:
            self.temp = self.input.getNumber()
            if self.temp < (-459.67):
                self.conversion_label["text"] = f"Error: Cannot go below absolute 0 (-459.67{chr(176)}F)"
            else:
                self.conversion_value = (self.temp - 32) * (5/9)
                self.conversion_label["text"] = f"{self.temp}{chr(176)}F = {self.conversion_value:.2f}{chr(176)}C"
        except ValueError:
            self.conversion_label["text"] = "Error: Enter a number."

def main():
    App().mainloop()


if __name__ == "__main__":
    main()


