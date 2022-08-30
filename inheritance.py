class students:
    nums = 0
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.email = f'{self.fname}{self.lname}@gmail.com'
        
    def fullName(self):
        return f'\nFirstName: {self.fname}\nLastName: {self.lname}\nAge: {self.age}\nEmail: {self.email}\nRank: {self.rank}'
    
    #nums.teachers += 1
    
class teachers(students):
    def __init__(self, fname, lname, age, rank):
        super().__init__(fname, lname, age)
        self.rank = rank
    
T1 = teachers('Danladi', 'Sunday', 39, 11)
T2 = teachers('Sam', 'Mark', 29, 9)

#print(nums.teachers)
print(T1.fullName())
print(T2.fullName())