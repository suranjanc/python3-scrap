class employee():
    def __init__(self, fullName, salary=None, height=None, nationality=None):
       self.firstName=str(fullName).split(' ')[0]
       self.lastName=str(fullName).split(' ')[1] 
       if salary is not None:
           self.salary=salary   
       if height is not None:
           self.height=height
       if nationality is not None:
           self.nationality=nationality


john = employee("John Doe")
print(john.firstName)
richard = employee("Richard Roe", salary=110000, height=178)
print(richard.height)