# OLIONMUODOSTIN JA OLETUSARVOT
# =============================

class RasekoMember():
    """Creates a member of Raseko OrganisaTION"""
    def __init__(self, firstname, lastname, role='Student'):
        self.firstname = firstname
        self.lastname = lastname
        self.role = role

if __name__ == "__main__":

    student = RasekoMember('Jonne', 'Janttari')
    print(f'{student.firstname} rooli organisaatiossa on {student.role}')

    teacher = RasekoMember('Mikko', 'Viljanen', 'Teacher')
    print(f'{teacher.firstname} rooli organisaatiossa on {teacher.role}')