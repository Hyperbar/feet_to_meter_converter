import FreeSimpleGUI as sg
from conversion import make_conversion

feet_label = sg.Text("Enter feet", )
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches", )
inches_input = sg.Input(key="inches")

convert_btn = sg.Button("Convert")
result_in_meter = sg.Text("", key="output")

window = sg.Window(title="Convertor - Hyperbar",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [convert_btn, result_in_meter]])

while True:
    event, value = window.read()
    feet = float(value["feet"])
    inches = float(value["inches"])
    conversion = make_conversion(feet, inches)
    window["output"].update(value=f"{conversion} m", text_color="white")

window.close()
