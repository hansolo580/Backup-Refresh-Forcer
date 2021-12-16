# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import date

drivepaths = {
    "Movies": "I:\\",
    "Shows": "H:\\",
    "Family": "E:\\",
    "Overflow": "D:\\"
}


def make_garbage(string_path):
    # Use a breakpoint in the code line below to debug your script.
    with open(string_path+'/dummy.txt', 'w') as file:
        file.write('Created new dummy file on ' + str(date.today()))
    return file


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in drivepaths.values():
        print(i)
        make_garbage(i)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
