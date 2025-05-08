def calculate_bmi(height,weight):
    print("Height= " + str(height))
    print("Weight= " + str(weight))
    bmi = weight/(height**2)
    if bmi<18.5:
        x = -1
    elif bmi>=18.5 and bmi<=25.0:
        x = 0
    else:
        x = 1
    return bmi,x

def classify_bmi(bmi_value): 

    if bmi_value<18.5:
        print("Under Weight")
    elif bmi_value>=18.5 and bmi_value<=25.0:
        print("Normal Weight")
    else:
        print("Over Weight")
    

def main():
    bmi_output,x = calculate_bmi(1.8,55)
    print("BMI: " + str(bmi_output))
    classify_bmi(bmi_output)
    print(x)

if __name__ == "__main__":
    main()