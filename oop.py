class student:
    roll = " "
    gpa =" "

    def  set_value(self,roll,gpa):
         self.roll = roll
         self.gpa = gpa

    def display(self):
        print(f"gpa:{self.gpa},roll:{self.roll}")



rahim =student()
rahim.set_value(100,3.67)
rahim.display()



ahim =student()
ahim.set_value(522,3.96)
ahim.display()

