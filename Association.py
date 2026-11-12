class Admin:
    def __init__(self, name: str):
        self.name = name
        self.track_employee = []

class Tracker:
    def __init__(self, employee_id: int, admins: Admin):
        self.employee_id = employee_id
        self.admin = admins
        admins.track_employee.append(self)

John = Admin("John")

Tracker1 = Tracker(202, John)
Tracker2 = Tracker(203, John)

for i in John.track_employee:
    print(f'Employee Id: {i.employee_id}')
