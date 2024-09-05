# Import the FreeSimpleGUI library for creating the graphical user interface
import FreeSimpleGUI as sg
# Import the make_conversion function from the conversion module
from conversion import make_conversion


# Apply a theme
sg.theme('Black')

# Create GUI elements

# Label and input for entering feet
feet_label = sg.Text("Enter feet")
feet_input = sg.Input(key="feet")

# Label and input for entering inches
inches_label = sg.Text("Enter inches")
inches_input = sg.Input(key="inches")

# Button to initiate the conversion process
convert_btn = sg.Button("Convert")
# Text element to display the conversion result in meters
result_in_meter = sg.Text("", key="output")

# Button to exit and close the program
button_exit = sg.Button("Exit", key="exit")

# Create the main window with all GUI elements
window = sg.Window(title="Convertor - Hyperbar",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [convert_btn, button_exit,result_in_meter]])

# Main application loop
while True:
    # Read events and values from the window
    event, value = window.read()

    match event:
        case "exit":
            break
        case sg.WIN_CLOSED:
            break


    # Convert the input values to float
    feet = float(value["feet"])
    inches = float(value["inches"])

    # Call the make_conversion function to convert feet and inches to meters
    conversion = make_conversion(feet, inches)

    # Update the output text element with the conversion result
    window["output"].update(value=f"{conversion} m", text_color="white")

    # Close the window when the loop exits
window.close()
