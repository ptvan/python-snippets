class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print('')

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class SalaryEmployee(Employee):
    def __init__(self, id, name, monthly_salary):
        super().__init__(id, name)
        self.monthly_salary = monthly_salary
    
    def calculate_payroll(self):
        return self.monthly_salary

class ContractEmployee(Employee):
    def __init__(self, id, name, contract_salary):
        super().__init__(id, name)
        self.contract_salary = contract_salary
    
    def calculate_payroll(self):
        return self.contract_salary


salary_employee = SalaryEmployee(1, "John Doe", 1500)
contract_employee = ContractEmployee(2, "Jane Appleseed", 15000)

payroll = PayrollSystem()

payroll.calculate_payroll([salary_employee, contract_employee])

