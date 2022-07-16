from datetime import date

drivepaths = {
    "Movies A": "I:\\",
    "Movies B": "H:\\",
    "Family": "E:\\",
    "Overflow": "D:\\",
    "Temp Storage": "F:\\",
    "Shows": "J:\\"
}


def make_garbage(string_path):
    with open(string_path+'/dummy.txt', 'w') as file:
        file.write('Created new dummy file on ' + str(date.today()))
    return file


if __name__ == '__main__':
    for i in drivepaths.values():
        make_garbage(i)

