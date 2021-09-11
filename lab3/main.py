from lab3.person import Person
from list import PersonList


if __name__ == '__main__':
    data = PersonList('test.txt')

    data.add_person(
        Person().create('asd', 'hsdf', 'ff')
    )

    print(
        data.get_person_str(0)
    )
