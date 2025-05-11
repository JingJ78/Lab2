print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
import statistics

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    numbers = input("Enter numbers: ")
    str_list = numbers.split(",")
    float_list = [float(i) for i in str_list]
    print (float_list)
    return float_list

def calc_average_temperature(numlist):
    average = sum(numlist)/len(numlist)
    print(average)
    return average

def calc_min_max_temperature(numlist):
    small = min(numlist)
    big = max(numlist)
    values = [small, big]
    values = [int(i) for i in values]
    print(values)
    return values


def calc_median_temperature(numlist):
    import statistics
    med = statistics.median(numlist)
    print("Median = " + str(med))
    return med
def main():
    display_main_menu()
    num_list = get_user_input()
    calc_average_temperature(num_list)
    calc_min_max_temperature(num_list)
    calc_median_temperature(num_list)

if __name__ == "__main__":
    main()