def main():
    numbers = []
    while len (numbers) != 5 :
        user_num = int(input("Enter a number"))
        numbers.append(user_num)

    print("The first number is {} ".format(numbers[0]))
    print("The last number is {} " .format(numbers[-1]))
    print("The smallest number is {} ".format(min(numbers)))
    print("The largest number is {} ".format(max(numbers)))
    numbers.sort()
    mean = sum(numbers) / 5
    print("The average {} ".format(mean))








main()