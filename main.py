import pyautogui
import time
from random import randint
NumberOfCommentsYouWant = 3


# Count Line On Comment.txt ##
file = open("Comment.txt", "r")
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
file.close()
#print(line_count)

a= 0
while True:
    # Read teh Text on Comment.txt line
    with open('Comment.txt') as c:
        myCommentList = c.read().splitlines()
        d = randint(1, line_count-1)
        print(myCommentList[d])

    time.sleep(5)
    pyautogui.typewrite(myCommentList[d]+str(a))
    time.sleep(5)
    a=a+1

    pyautogui.press('enter')
    if a == NumberOfCommentsYouWant+1:
        break
