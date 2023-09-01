#Write a python program to create a class named Base. In Base class create a method showBase(), this method display a message ‘This message from base class’. By inheriting Base class now create a class named Derived. In Derived class create a method showDerived(), this method display a message ‘This message from derived class’. Now test Base and Derived class.

class Base:
 def showBase(self):
    print("ye hai base")
class Derived(Base):
  def showDerived(self):
     print("ye hai derived")
base_instance=Base()
base_instance.showBase()
derived_instance=Derived()
derived_instance.showDerived()