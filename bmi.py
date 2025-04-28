def calculate_bmi(height,weight):
    print("Height= " + str(height))
    print("Weight= " + str(weight))
    bmi = weight/(height*height)
    return bmi

def classify_bmi(bmi_value): 

    if bmi_value<18.5:
        print("Under Weight")

    elif bmi_value>=18.5 and bmi_value<=25.0:
        print("Normal Weight")

    else:
        print("Over Weight")
    return
        
def main():
    bmi_output = calculate_bmi(1.8,55)
    print("BMI: " + str(bmi_output))
    classify_bmi(bmi_output)

    if __name__ == "__main__":
        main()