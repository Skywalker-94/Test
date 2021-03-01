class User():
    def __init__(self, first_name, last_name, sex, age):
        self.first_name=first_name
        self.last_name=last_name
        self.sex=sex
        self.age=age
        self.login_attempts=0
        
    def describe_user(self):
        print(self.first_name+' '+self.last_name+ ' '+self.sex+' '+str(self.age)+' '+str(self.login_attempts))
        
    def greet_user(self):
        print('Nice to meet you, '+self.first_name+' '+self.last_name)
        
    def increment_login_attempts(self):
        self.login_attempts+=1
        
    def reset_login_attempts(self):
        self.login_attempts=0
        
    
        
jack = User('Jack','London','male',32)
jack.greet_user()
jack.increment_login_attempts()
jack.increment_login_attempts()
jack.increment_login_attempts()
jack.describe_user()
jack.reset_login_attempts()
jack.describe_user()

