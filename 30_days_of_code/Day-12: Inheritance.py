class Student(Person):
    def __init__(self, fName, lName, sId, scores):
        super().__init__(fName, lName, sId)
        self.scores = scores

    def calculate(self):
        avg = 0.0
        for score in self.scores:
            avg += score

        avg = avg/len(self.scores)
        if avg < 40:
            return 'T'
        elif avg < 55:
            return 'D'
        elif avg < 70:
            return 'P'
        elif avg < 80:
            return 'A'
        elif avg < 90:
            return 'E'
        else:
            return 'O'




'''
#   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
'''
