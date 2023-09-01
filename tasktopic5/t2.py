#wap to create a class with name'employee'.employees class take three instance variable empoid,empname and salary.create two methods in class first setemployee()&second display()set employee()method initilizeinstance variableempid,empname,salary and display()method display value of empid,empnameand salary.now test emplloyee class.
class emplyoee:
 employee_empid=0
 emplyoee_empname=""
 emplyoee_salary=""
#emplyoee class first setemployee():
def setemloyee(employee,empid,empname,salary):
 employee._empid=empid
 employee.empname= empname
 employee._salary=salary
#emplyoee second display setemployee():
def displaydata(employee):
 print("employee id:",employee_empid)
 print("employee name:",employee_empname)
 print("employee salary:",employee_salary)
e=emplyoee()
ename=str(input("enter employee name:"))
esalary=int(input("enter employee salary:"))
e.setvalue(eid,ename,esalary)
e.display()