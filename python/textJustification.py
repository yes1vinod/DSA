from typing import List
class Solution:
    class Solution(object):
        
    def computeSpace(self, wordLength, availableslots,flag):
        space=0.0
        space = float(availableslots)/(wordLength-1)
        print(space)
        spaceString=""
        if(flag):
            space=math.ceil(space)
        for item in range(0,int(space)):
            spaceString=spaceString+ " "    
        return spaceString
        
    def fullJustify(self, words, maxWidth):
        result =[]
        line=""
        for word in words:
            if(len(line+word)<=maxWidth):
                line=line + word +" "
                continue
             
            else:
                # find the spaces required
                line = line.rstrip()
                result.append(line) 
                line=word+" "
        result.append(line)
        newLine=""
        newResult=[]
        for line in result:
            # lineWords= line.split(" ")
            availableSlots = maxWidth - len(line)
            lineWords=line.split(" ")
            newLine=""
            spaceString= ""
            for i in range(0,(len(lineWords)-1)):
                if(i ==0):
                    spaceString= self.computeSpace(len(lineWords),availableSlots,True)
                else:
                    spaceString= self.computeSpace(len(lineWords),availableSlots,False)
                newLine=newLine+lineWords[i]+" " +spaceString;
            newLine=newLine+ lineWords[len(lineWords)-1]
            newResult.append(newLine)
        return newResult
        
instance =Solution()
instance.fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16)

       