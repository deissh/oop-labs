from employer import Employer
from student import Student
from list import PersonList


if __name__ == '__main__':
    filename = input('filename=')
    data = PersonList(filename) if filename else PersonList()

    st = Student().create('asd', 'hsdf', 'ff', 'pr123', 2)
    data.add_person(st)

    em = Employer().create('employer', 'name', 'andsdads')
    data.add_person(em)

    print(
        data.get_person_str(1)
    )
