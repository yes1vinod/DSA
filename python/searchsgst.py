from typing import List
class Solution():

    def suggestedProducts(self, products: List[str], searchWord: str):
        bigList=[]
        products.sort()
        for i in range(1,len(searchWord)):
            smallList=[]
            for item in products:
                if(searchWord[0:i] == item[0:i]):
                    if(len(smallList)<3):
                        smallList.append(item)
            print(searchWord[0:i])
            bigList.append(smallList)
            print(bigList)

instance = Solution()
instance.suggestedProducts( ["mobile","mouse","moneypot","monitor","mousepad"],"mouse")