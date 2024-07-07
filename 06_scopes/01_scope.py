#userName = "Vaishnavi Pol"

#def func():
   # userName = "Vaishnavi"
    #print(userName)

#print(userName)
#func()



#x = 10
#def func2(y):
 #   z = x + y
  #  return z

#result = func2(5)
#print(result)



#number = 10
#def func3():
 #   global number
  #  number = 9
#func3()
#print(number)



#number2 = 10
#def f1():
 #   number2 = 20
  #  def f2():
   #     print(number2)
    #return f2    
#myResult = f1()
#myResult()



number3 = 10
def pythonCoder(num):
    def actual(number3):
        return number3 ** num
    return actual

f = pythonCoder(2)
g = pythonCoder(3)

print(f(9))
print(g(9))

