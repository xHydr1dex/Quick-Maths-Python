import random
import time

min = 1
max = 10
OPERATOR = ["+","-","*"]
TOTAL = 10

def question():

    left = random.randint(min,max)
    right = random.randint(min,max)
    operation = random.choice(OPERATOR)

    expr = str(left) + " " + operation + " " + str(right)
    
    # print(expr)

    answer = eval(expr)

    return expr,answer

correct = 0
wrong = 0

print("---------------------------------------")
print("welcome to the the quiz!")
print("---------------------------------------")
input("press enter to start the quiz! ")
print("---------------------------------------")

start_time = time.time()

for i in range(TOTAL):
    expr,answer  = question()

    while True:
        guess = input("Problem #"+ str(i+1)+ " : " + expr + " = ")
        if(guess == str(answer)):
            correct+=1
            print("That's correct!")
            print("Total : ", correct)
            break
        else:
            wrong+=1
            print("That's wrong :(")
            print("Total : ",correct)
            break

end_time = time.time()

total_time = end_time - start_time

print("\n---------------------------------------\n")

print("correct : ", correct)
print("wrong: ", wrong)

print("\n%age : ",(correct/TOTAL)*100)

print("\ntotal time taken : ", round(total_time,2))

if(total_time>25):
    print("\nYou are too slow!")
else:
    print("\nwell done!\n")

print("Thank you for playing!\n")






