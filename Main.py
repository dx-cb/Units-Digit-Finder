# what is the units digit of 703**703
import sys

pattern = []  # im setting up the list

multiplier = int(input("Enter the number that you want the units value of when raised to its self, e.g 123^123: "))
lastDigit = multiplier % 10  # mod 10 because the remainder will be that last digit if you think about it
pattern.append(lastDigit)

NoPatternStatus = True

while NoPatternStatus:  # you can just do while and then a boolean and it assumes the '== True' part
    listLength = len(pattern)  # find the length of the list at this current iteration
    lastDigit = (lastDigit * multiplier) % 10  # repeating the cycle of the actual maths
    pattern.append(lastDigit)  # writing it in the list

    # now here is the cool part - this checks the list to see if any patterns were made after each iteration
    for i in range(1, (listLength // 2) + 1):
        if pattern[-i:] == pattern[-2 * i:-i]:
            swappingElement = pattern.pop()  # 2 in 1 thing, removes the last element and assigns
                                             # it to a variable (swappingElement in this case)
            pattern.insert(0, swappingElement)  # index 0 , variable
            print(f"The numbers {pattern[-i:]} will continue repeating.")

            lengthPatternList = len(pattern[-i:])
            lastNum = multiplier % lengthPatternList
            print(f"This means that the the last digit of {multiplier} raised to the power of {multiplier} is {lastNum}.")


            sys.exit()

