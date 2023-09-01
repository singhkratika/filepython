#3Write a python program to create a class Employee. In Employee class take two instance variables empid and empname. In Employee class create two methods setEmployee() and getEmployee(). setEmployee() method is used to initialize instance variables empid and empname whereas getEmployee() method is used 
to display values of empid and empname. By inheriting Employee class create a new class Payroll. In Payroll class create three instance variables bs, hra and da. In Payroll class create two methods setPayroll() and getPayroll(). setPayroll() method is used to initialize variables bs, hra and da whereas getPayroll() method is used to display values of empid and empname .by inheriting employee class create a new class payroll.in payroll class create three instance variaable bs,hra and da.in payroll class create two methods setpayroll()and get payroll().setpayrolll()method is used to display values of bs,hra and da where as getpayroll()method is used to display values of bs,hra and da.now by inheriting payroll class create a new class payship.in payshipclass create a method named netsalary()which displays net salarywith adition of basic salary,hraand da .now test payslipclass.this is anexample of mutlilevel inheritance.


class Employee:
 def setEmployee(self,empid,empname):
   self.empid=empid
   self.empname=empname
 def getEmployee(self):
   print("Employee Id=",self.empid)
   print("Employee Name=",self.empname)
class Payroll(Employee):
 def setPayroll(self,bs,hra,da):
  self.bs=bs
  self.hra=hra
  self.da=da
 def getPayroll(self):
  print("Basic Salary=",self.bs)
  print("House Rent Allownces=",self.hra)
  print("Dearness Allownces=",self.da)
class Payslip(Payroll):
 def netSalary(self):
  print("Net Salary=",(self.bs+self.hra+self.da))
eid=int(input("Enter Employee Id : "))
ename=input("Enter Employee Name : ")
b=int(input("Enter Basic Salary : "))
h=int(input("Enter House Rent Allownces : "))
d=int(input("Enter Dearness Allownces : "))
ps=Payslip()
ps.setEmployee(eid,e…