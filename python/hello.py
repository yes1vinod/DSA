print("hello python!")
def addTwoNumbers(a,b):
    varwithGap= " vinod is working "
    print(varwithGap.lstrip());
    motorcycles = ['honda', 'aamaha', 'suzuki']
    motorcycles.insert(1,"Trek");
    motorcycles.append("Splendid")
    motorcycles.pop(1)
    motorcycles.sort(reverse=True);
    for bike in motorcycles:
        print(bike);
    print("second motor cycle is " + motorcycles.pop(1));
    sum = a+ b
    print("Sum : "+ str(sum))

addTwoNumbers(5,5)



