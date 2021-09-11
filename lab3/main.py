from person import Person
from list import PersonList


if __name__ == '__main__':
    filename = input('filename=')
    data = PersonList(filename) if filename else PersonList()

    data.add_person(
        Person().create('asd', 'hsdf', 'ff')
    )

    print(
        data.get_person_str(0)
    )
