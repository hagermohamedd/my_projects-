import time
import random

print("Get Ready")

ran = random.randint(1,10)
time.sleep(ran)

print("GO!")

start = time.time()

enter =input("")

end = time.time()

timee = round(end-start,2)

print (f"Your reaction time: {timee} sec")

if timee > 1.44 :
    print ("too slow bro!!")
    
else:
    print("fast, good job!")