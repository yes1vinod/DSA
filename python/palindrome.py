class Palindrome():
    def findLongPalindrome(self, input:str)->int:
        maxLength=0
        print("Input String is "+ input)
        # find all combination of data
        for i in range(0,len(input)-1):
            for j in range(i+1,len(input)+1):
                # check if it is a palindrome
                inputInstance=  input[i:j]
                if(inputInstance==inputInstance[::-1]):
                    # Hey! Palindrome
                    tempLength= len(inputInstance)
                    if(tempLength>maxLength):
                        maxLength=tempLength


        return maxLength


instance  =  Palindrome()
print(str(instance.findLongPalindrome("BB")))
