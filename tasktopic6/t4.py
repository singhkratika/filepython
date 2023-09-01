#In program (3) create a class Loan before the code of Payslip class. In Loan class create a method setLoan() which is used to initialize amt variable. Now inherit Loan class in Payslip class and in netSalary() method also print salary on hand as (bs+hra+da-amt). This is an example of hybrid inheritance.

#Hybrid inheritence
class Employee:
	def setEmployee(self,empid,empname):
		self.empid=empid
		self.empname=empname
	def getEmployee(self):
		print("Employee Id = ", self.empid)
		print("Employee Name = ", self.empname)
class Payroll(Employee):
	def setPayroll(self,bs,hra,da):
		self.bs=bs
		self.hra=hra
		self.da=da
	def getPayroll(self):
		print("Basic salary = ", self.bs)
		print("House Rent Allowance = ", self.hra)
		print("Dearness Allowance = ", self.da)
class Loan:
	def setLoan(self, amt):
		self.amt=amt
class Payslip(Payroll,Loan):
	def netSalary(self):
		print("Net salary = ", self.bs+self.hra+self.da)
		print("Salary in hand = ", self.bs+self.hra+self.da-amt)
ps=Payslip()
empid=int(input("Enter employee id : "))
empname=input("Enter your name : ")
ps.setEmployee(empid,empname)
bs=int(input("Enter basic salary: "))
hra=int(input("Enter house rent allowance: "))
da=int(input("Enter dearness allowance: "))
ps.setPayroll(bs,hra,da)
amt=int(input("Enter monthly loan amount : "))
ps.setLoan(amt)
print("pay slip..")
ps.getEmployee()
ps.getPayroll()
ps.netSalary()