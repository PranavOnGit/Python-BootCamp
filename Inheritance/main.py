
from  Base import Base
from  Child import Child

base = Base.can_Write()
base = Base.can_Read()
base = Base.can_Create()

child = Child.can_underline()
child = Child.can_Create()  # Base method can be called from child
Child = Child.can_Read() # overriden method in Child