class Employee:
    def __init__(self, name, emp_id):
        self.name = name  # Public attribute
        self.__emp_id = emp_id  # Private attribute
        self._salary = 0  # Protected attribute

    def set_salary(self, salary):  # Public method
        self._salary = salary

    def __set_emp_id(self, emp_id):  # Private method
        self.__emp_id = emp_id

    def _get_salary(self):  # Protected method
        return self._salary
