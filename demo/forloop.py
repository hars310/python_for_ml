str1 = input("Enter the string: ")
length = len(str1)

def checkPalindrome(string):
    for i in range(length // 2):
        if string[i] != string[length - i - 1]:
            print("Not a palindrome")  
            return
    print("Palindrome string")

checkPalindrome(str1)
