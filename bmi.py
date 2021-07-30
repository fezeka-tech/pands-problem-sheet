#This is a python program that calculates a person's BMI#


def bmi():
    def square_meter(cm):
        meter = cm * 0.01  # converts height in cm to m
        m_square = meter * meter
        return m_square

    weight = int(input("Enter weight : "))
    height = int(input("Enter height : "))

    body_mass = weight / square_meter(height)  
    print(f'BMI is {body_mass:.2f}.')


if __name__ == "__main__":
    bmi()
