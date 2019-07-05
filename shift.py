import datetime, math, sqlite3, terminaltables

MINIMUM_WAGE = 13.15

def create_table():
    connection = sqlite3.connect("time-clock.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS shifts(shift_id INTEGER PRIMARY KEY, shift_started_at TEXT, shift_ended_at TEXT, shift_started_at_friendly TEXT, shift_ended_at_friendly TEXT, hours_worked FLOAT, pay_per_hour FLOAT, total_pay FLOAT)")
        
    connection.commit()
    connection.close() 

def drop_table():
    confirmation = input("ARE YOU SURE YOU WANT TO PERFORM THIS ACTION (Y/N): ")

    if confirmation == "Y" or confirmation == "y":
        connection = sqlite3.connect("time-clock.db")
            
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS shifts")
            
        connection.commit()
        connection.close() 
        print("Database Reset.")
    elif confirmation == "N" or confirmation == "n":
        print("Aborting Database Reset.")
    else:
        print("Input Not Recognized, Please Try Again!")

def add_shift():
    shift_started_at = datetime.datetime.strptime(input("Enter The Date and Time That The Shift Started (DD/MM/YYYY HH:MM AM/PM): "), "%d/%m/%Y %I:%M %p")
    shift_ended_at = datetime.datetime.strptime(input("Enter The Date and Time That The Shift Ended (DD/MM/YYYY HH:MM AM/PM): "), "%d/%m/%Y %I:%M %p")
    hours_worked = divmod((shift_ended_at - shift_started_at).total_seconds(), 3600)[0] 
    shift_started_at_friendly = str(datetime.datetime.strftime(shift_started_at, "%I:%M %p on %A, %d %B %Y"))
    shift_ended_at_friendly = str(datetime.datetime.strftime(shift_ended_at, "%I:%M %p on %A, %d %B %Y"))

    try:
        pay_per_hour = float(input("Enter The Pay Per Hour: "))
        if pay_per_hour < MINIMUM_WAGE:
            print("The pay per hour cannot be below minimum wage which is " + str(MINIMUM_WAGE))
    except ValueError:
        print("The value entered was not an float.")

    total_pay = pay_per_hour * hours_worked

    connection = sqlite3.connect("time-clock.db")

    cursor = connection.cursor()
    cursor.execute("INSERT INTO shifts VALUES(null, ?, ?, ?, ?, ?, ?, ?)", [str(shift_started_at), str(shift_ended_at), str(shift_started_at_friendly), str(shift_ended_at_friendly), str(hours_worked), float(pay_per_hour), float(total_pay)])
        
    connection.commit()
    connection.close()
    
def list_shifts():
    connection = sqlite3.connect("time-clock.db")

    cursor = connection.cursor()
    shifts = cursor.execute("SELECT * FROM shifts").fetchall()
        
    connection.commit()
    connection.close()

    shifts_data = [
        ["Shift ID", "Shift Started At", "Shift Ended At", "Hours Worked", "Pay Per Hour", "Total Pay"],
    ]

    for shift in shifts:
        shifts_data.append([shift[0], shift[3], shift[4], shift[5], shift[6], shift[7]])
        
        table = terminaltables.ascii_table.AsciiTable(shifts_data)
        print(table.table)


def get_shift():
    try:
        id = int(input("Enter The Shift ID: "))
    except ValueError:
        print("The value entered was not an integer.")
        
    connection = sqlite3.connect("time-clock.db")

    cursor = connection.cursor()
    shift = cursor.execute("SELECT * FROM shifts WHERE shift_id = ?", [id,]).fetchone()

    connection.commit()
    connection.close()

    shifts_data = [
        ["Shift ID", "Shift Started At", "Shift Ended At", "Hours Worked", "Pay Per Hour", "Total Pay"],
        [shift[0], shift[3], shift[4], shift[5], shift[6], shift[7]],
    ]

    table = terminaltables.ascii_table.AsciiTable(shifts_data)
    print(table.table)

def delete_shift():
    confirmation = input("ARE YOU SURE YOU WANT TO PERFORM THIS ACTION (Y/N): ")

    if confirmation == "Y" or confirmation == "y":
        try:
            id = int(input("Enter The Shift ID: "))
        except ValueError:
            print("The value entered was not an integer.")
                
        connection = sqlite3.connect("time-clock.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM shifts WHERE shift_id = ?", [id,])
        
        connection.commit()
        connection.close()
    elif confirmation == "N" or confirmation == "n":
        print("Aborting Shift Deletion.")
    else:
        print("Input Not Recognized, Please Try Again!")	