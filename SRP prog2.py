class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def is_eligible_for_promotion(self):
        return self.salary > 50000


class Promoter:
    def promote(self, employee):
        if employee.is_eligible_for_promotion():
            print(f"Promoting {employee.name} to a higher position!")
        else:
            print(f"{employee.name} is not eligible for promotion.")


class SalaryManager:
    def increase_salary(self, employee, amount):
        employee.salary += amount
        print(f"Salary for {employee.name} increased to {employee.salary}")


class Notifier:
    def send_notification(self, message, employee_name):
        print(f"Notification sent to {employee_name}: {message}")


class EmployeeManager:
    def __init__(self, employee, promoter, salary_manager, notifier):
        self.employee = employee
        self.promoter = promoter
        self.salary_manager = salary_manager
        self.notifier = notifier

    def manage_employee(self):
        self.promoter.promote(self.employee)
        if self.employee.is_eligible_for_promotion():
            self.salary_manager.increase_salary(self.employee, 5000)
            self.notifier.send_notification(
                "You have been promoted and received a salary increase.", self.employee.name)
        else:
            self.notifier.send_notification(
                "You are not eligible for promotion.", self.employee.name)


employee = Employee("John Doe", "Software Engineer", 55000)
promoter = Promoter()
salary_manager = SalaryManager()
notifier = Notifier()

employee_manager = EmployeeManager(
    employee, promoter, salary_manager, notifier)
employee_manager.manage_employee()
