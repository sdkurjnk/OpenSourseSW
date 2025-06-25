import curses

#Basic Variables
row = 3
column = 4
data = [['0' for i in range(column)] for j in range(row)]
command = ["adrow", "adcol", "set", "rm", "save", "exit"]


#Making Empey Data Table
data[0][0] = "MyFile"
for i in range(1, row):
    data[i][0] = f"row{i}"
for j in range(1, column):
    data[0][j] = f"col{j}"

#Saving Data in Txt
def Saving():
    global row, column, data

    maxstring = 0

    for i in range(row):
        for j in range(column):
            if (maxstring < len(data[i][j])):
                maxstring = len(data[i][j])
    
    file = open(f"{data[0][0]}.txt", "w")

    for i in range(row):
        output = ""
        for j in range(column):
            cell = str(data[i][j]).rjust(maxstring)
            output += f"| {cell}"
        output += " |\n"
        file.write(output)
        
    file.close()
    
def main(stdscr):
    #Display Variables
    global row, column, data
    curses.curs_set(1)
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    status_h = 3
    input_h = 3
    display_h = h - (status_h + input_h)

    display_win = curses.newwin(display_h, w, 0, 0)
    input_win = curses.newwin(input_h, w, display_h + status_h, 0)
    status_win = curses.newwin(status_h, w, display_h, 0)
    display_win.scrollok(True)
    status_win.scrollok(True)

    def printdata():
        maxstring = 0

        for i in range(row):
            for j in range(column):
                if (maxstring < len(data[i][j])):
                    maxstring = len(data[i][j])
        
        display_win.clear()
        for i in range(row):
            output = ""
            for j in range(column):
                cell = str(data[i][j]).rjust(maxstring)
                output += f"| {cell} "
            output += "|"
            display_win.addstr(output + "\n")
        display_win.refresh()

    def printerror(errorcode):
        if errorcode == 1001:
            status_win.addstr("<Error> : Argument Error")
            status_win.refresh()
        elif errorcode == 1002:
            status_win.addstr("<Error> : Index Error")
            status_win.refresh()

    #Working Part
    while True:
        input_win.clear()
        input_win.border()
        input_win.addstr(1, 1, ">>> ")
        input_win.refresh()
        status_win.clear()

        printdata()

        curses.echo()
        user_input = input_win.getstr(1, 6).decode("utf-8").strip()
        curses.noecho()

        inputcommand = user_input.split()

        if not (inputcommand[0] in command):
            status_win.addstr(f"<Error> Unknown command : {user_input}\n")
            status_win.refresh()
        else: #Command Process
            if (inputcommand[0] == "adrow"): #"adrow" Cammand
                if (len(inputcommand) != 1):
                    printerror(1001)
                else:
                    data.append(['0' for _ in range(column)])
                    row += 1
                    data[len(data)-1][0] = f"row{row-1}"
            elif (inputcommand[0] == "adcol"): #"adcolumn" Command
                if (len(inputcommand) != 1):
                    printerror(1001)
                else:
                    for r in data:
                        r.append('0')
                    column += 1
                    data[0][column-1] = f"col{column-1}"
            elif (inputcommand[0] == "set"): #"setdata" Command
                if (len(inputcommand) != 4):
                    printerror(1001)
                elif ((int(inputcommand[1]) > row) or (int(inputcommand[2]) > column)):
                    printerror(1002)
                else:
                    data[int(inputcommand[1])][int(inputcommand[2])] = inputcommand[3]
            elif (inputcommand[0] == "rm"): #"rmdata" Command
                if (len(inputcommand) != 3):
                    printerror(1001)
                elif ((int(inputcommand[1]) > row) or (int(inputcommand[2]) > column)):
                    printerror(1002)
                else:
                    data[int(inputcommand[1])][int(inputcommand[2])] = '0'
            elif (inputcommand[0] == "save"): #"save" Command
                if (len(inputcommand) != 1):
                    printerror(1001)
                else:
                    Saving()
                    status_win.addstr(f"File was saved in {data[0][0]}.txt")
                    status_win.refresh()
            elif (inputcommand[0] == "exit"): #"exit" Command
                if (len(inputcommand) > 1):
                    printerror(1002)
                else:
                    break

curses.wrapper(main)
