import PySimpleGUI as sg

sg.theme('LightBrown1')   # Add a touch of color
sg.SetOptions(button_color=(sg.theme_background_color(),
                            sg.theme_background_color()))
# All the stuff inside your window.
layout = [[sg.Text('Pick an emote!')],
          [sg.Button('', key='pensivecowboy',
                     image_filename='./assets/pensivecowboy.png', image_subsample=2)],
          [sg.Button('', key='pensivecowboy', image_filename='./assets/pensivecowboy.png', image_subsample=2)]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    print(event)

window.close()
