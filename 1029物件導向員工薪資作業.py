class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, id, name, salary):
        super().__init__(id, name)
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class PartTimeEmployee(Employee):
    def __init__(self, id, name, hourly_wage):
        super().__init__(id, name)
        self.hourly_wage = hourly_wage
        self.hours_worked = 0

    def calculate_salary(self):
        return self.hourly_wage * self.hours_worked

    def set_hours_worked(self, hours):
        self.hours_worked = hours

class Intern(Employee):
    def __init__(self, id, name, stipend):
        super().__init__(id, name)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend

class EmployeeManagementSystem:
    def __init__(self):
        self.employee_list = []
        self.current_employee_id = 1

    def add_employee(self, employee):
        try:
            assert isinstance(employee, Employee),
            self.employee_list.append(employee)
            employee.id = self.current_employee_id
            self.current_employee_id += 1
        except AssertionError as e:
            print(f"員工加入失敗: {e}")

    def calculate_all_salary(self):
        total_salary = sum(employee.calculate_salary() for employee in self.employee_list)
        return total_salary

    def add_work_hours(self, employee, hours):
        try:
            assert isinstance(employee, PartTimeEmployee), 
            assert isinstance(hours, int) and hours > 0,
            employee.set_hours_worked(hours)
        except AssertionError as e:
            print(f"工作時數加入失敗: {e}")

    def set_stipend(self, employee, stipend):
        try:
            assert isinstance(employee, Intern), 
            assert stipend > 0,
            employee.stipend = stipend
        except AssertionError as e:
            print(f"獎學金加入失敗: {e}")

    def set_full_time_salary(self, employee, salary):
        try:
            assert isinstance(employee, FullTimeEmployee),
            assert salary > 0, 
            employee.salary = salary
        except AssertionError as e:
            print(f"月薪增加失敗: {e}")

    def print_all_employee(self):
        for employee in self.employee_list:
            self.print_employee(employee)

    def print_employee(self, employee):
        print(f"員工 ID: {employee.id}, 姓名: {employee.name}, 薪水: ${employee.calculate_salary()}")


ems = EmployeeManagementSystem()

full_time_employee = FullTimeEmployee(None, "John", 50000)
part_time_employee = PartTimeEmployee(None, "Alice", 20)
intern = Intern(None, "Bob", 1000)

ems.add_employee(full_time_employee)
ems.add_employee(part_time_employee)
ems.add_employee(intern)

ems.add_work_hours(part_time_employee, 30)
ems.set_stipend(intern, 1500)
ems.set_full_time_salary(full_time_employee, 55000)

ems.print_all_employee()
total_salary = ems.calculate_all_salary()
print(f"所有員工薪水總和: ${total_salary}")
