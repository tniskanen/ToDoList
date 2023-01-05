import PySimpleGUI as sg

label_1 = sg.Text('Enter feet:')
textbox_1 = sg.InputText()

label_2 = sg.Text('Enter inches:')
textbox_2 = sg.Input()

button = sg.Button('Convert')

window = sg.Window('Convertor', layout=[[label_1, textbox_1],
                                        [label_2, textbox_2],
                                        [button]])

window.read()
window.close()
