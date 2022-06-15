import PySimpleGUI as sg
import port_sweeper

sg.theme("DarkGrey15")

layout = [
    [sg.Text("IP to sweep ports on : ", expand_x=True), sg.In(key="-IP-")],
    [sg.Text("Port to start looking from :", expand_x=True), sg.In(key="-BOTTOM_PORT-")],
    [sg.Text("Number of ports to check :", expand_x=True), sg.In(key="-NUMBER_OF_PORTS-")],
    [sg.Text("Number of threads to use :", expand_x=True), sg.In(key="-NUMBER_OF_THREADS-")],
    [sg.Text("Name of the file to export data to : ", expand_x=True), sg.In("servers.txt", key="-FILE_PATH-")],
    [sg.Text("Folder to save the file to : "), sg.Push(), sg.FolderBrowse(key="-FOLDER-")],
    [sg.Button("Start!", key="-START_SWEEPER-"), sg.Text("", expand_x=True, key="-OUTPUT-")]
    ]

# Create the window
window = sg.Window("Minecraft server port sweeper", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break
    elif event == "-START_SWEEPER-":
        if "" in values.values():
            window["-OUTPUT-"].update("You're missing some entries !")
            continue

        ip = values["-IP-"]
        filePath = "{}//{}".format(values["-FOLDER-"], values["-FILE_PATH-"])
        if ".txt" not in filePath:
            filePath += ".txt"

        try:
            bottomPort = int(values["-BOTTOM_PORT-"])
            numberOfPorts = int(values["-NUMBER_OF_PORTS-"])
            numberOfThreads = int(values["-NUMBER_OF_THREADS-"])
        except ValueError as ve:
            window["-OUTPUT-"].update("Some values you entered need to be numbers")
            continue

        sweeper = port_sweeper.Sweeper(ip, bottomPort, numberOfPorts, numberOfThreads, filePath)
        window["-OUTPUT-"].update("Starting the sweeper!")

        sweeper.start()

        window["-OUTPUT-"].update("Done ! check {} for the servers found".format(filePath))

window.close()
