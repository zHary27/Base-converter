import PySimpleGUI as sg

sg.theme('Dark grey 9')

sg.SetOptions(
    font=('Verdana', 10)
)

layout = [
[sg.Text('Enter the number: ', font=('Verdana', 12), key='enternumbertxt')],
[sg.Input(key='number')],
[sg.Checkbox('Binary', key='bincheck'), sg.Checkbox('Hexadecimal', key = 'hexcheck'), sg.Checkbox('Octal', key = 'octcheck')],
[sg.Text()],
[sg.Text('Binary value: ', key='binconv', size=(0,1))],
[sg.Text('Hexadecimal value: ', key='hexconv', size=(0,1))],
[sg.Text('Octal value: ', key='octconv', size=(0,1))],
[sg.Text()],
[sg.Button('Convert', key='convbutton', size=(64,2))],
[sg.Text(key='error', size=(0,1), text_color='red', visible=False)]
]

window = sg.Window('Base converter', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'quit':
        break
    try:
        if values['bincheck'] == False and values['hexcheck'] == False and values['octcheck'] == False:
            window['error'].update('SELECT SOMETHING')
            window['error'].update(visible=True)
        if values['bincheck'] == True:
            window['error'].update('')
            window['error'].update(visible=False)
            x = int(values['number'])
            z = bin(x)
            window['binconv'].update('Binary value: ' + z[2:])
        else:
            window['binconv'].update('Binary value: ---')
        if values['hexcheck'] == True:
            window['error'].update('')
            window['error'].update(visible=False)
            x1 = int(values['number'])
            z1 = hex(x1).upper()
            window['hexconv'].update('Hexadecimal value: ' + z1[2:])
        else:
            window['hexconv'].update('Hexadecimal value: ---')
        if values['octcheck'] == True:
            window['error'].update('')
            window['error'].update(visible=False)
            x2 = int(values['number'])
            z2 = oct(x2)
            window['octconv'].update('Octal value: ' + z2[2:])
        else:
            window['octconv'].update('Octal value: ---')
    except ValueError:
        window['error'].update(visible=True)
        window['error'].update('INVALID ARGUMENT')
        window['number'].update('')
        window['octconv'].update('Octal value: ---')
        window['binconv'].update('Binary value: ---')
        window['hexconv'].update('Hexadecimal value: ---')

window.close()
