import shift
import terminaltables

action_messages = [["Action", "Description"], ["1) Create A Shift", "Selecting this action allows you to create / log a shift!"], ["2) Delete A Shift", "Selecting this action allows you to delete a shift!"], ["3) Get A Shift", "Selecting this action allows you to retrieve information about a specific shift."], ["4) List All Shifts", "Selecting this action allows you to see a list of all logged shifts."], ["5) Reset All Shifts", "This will delete all logged shifts, BE CAREFUL!"]]
table = terminaltables.ascii_table.AsciiTable(action_messages)

def main():
    shift.create_table()

    print("--- TimeClock ---")
    print(table.table)
        
    action = int(input("Please enter a number: "))

    if action == 1:
        shift.add_shift()
    elif action == 2:
        shift.list_shifts()
        shift.delete_shift()
    elif action == 3:
        shift.list_shifts()
        shift.get_shift()
    elif action == 4:
        shift.list_shifts()
    elif action == 5:
        shift.drop_table()
        shift.create_table()
    else:
        print("Invalid Action Entered, Please Try Again!")
    print("--- TimeClock ---")


if __name__ == "__main__":
    main()
    