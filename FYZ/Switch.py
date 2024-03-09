class Python_Switch:
    def day(self, month):

        default ="Incorrect day"

        return getattr(self, 'case_' + str(month), lambda: default)()
    
    def case_1(self):
        return "Jan"
    
    def case_2(self):
        return "Feb"
    
    def case_3(self):
        return "mar"
    #print(day)
    #create an instance of the class
switch_instance = Python_Switch()   

#Example usage
print(switch_instance.day(2)) #Output: Mar
    
        
    