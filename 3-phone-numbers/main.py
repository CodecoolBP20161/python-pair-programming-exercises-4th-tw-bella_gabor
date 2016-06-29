import csv
import sys
from person import Person


def open_csv(file_name):
    persons = []
    with open(file_name, "r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            persons.append(Person(row[0], Person.normalize_phone_number(row[1])))
    return persons


def get_csv_file_name(argv_list):
    if len(argv_list) < 2:
        return None
    else:
        return argv_list[1]


def format_output(person):
    if person is None:
        return 'No match found.'
    else:
        return ('This number belongs to: ' + str(person._name))


def get_person_by_phone_number(person_list, user_input_phone_number):
    for i in person_list:
        if i._phone_number == user_input_phone_number:
            return i


def main():
    file_name = get_csv_file_name(sys.argv)
    if file_name is None:
        print('No database file was given.')
        sys.exit(0)

    person_list = open_csv(file_name)
    user_input_phone_number = input('Please enter the phone number: ')
    match_person = get_person_by_phone_number(person_list, user_input_phone_number)
    print(format_output(match_person))
if __name__ == '__main__':
    main()
