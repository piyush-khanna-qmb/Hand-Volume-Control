"""
COMPLETELY FUNCTIONAL!
>> Reads from webcam, estimates distance between index finger and thumb.
>> Controls Gripper servo to move according to distance.
"""

import serial

def homePos(ard):
    give= f"#1ZZ#2ZZ#3ZZ#4ZZ#5ZZ#6ZZ****"
    ard.write(give.encode())

command= f"#1ZZ#2ZZ#3ZZ#4ZZ#5ZZ#6ZZ****"
haath = serial.Serial('COM5', baudrate=9600, timeout=0.5)

while True:
    forWhich= input("Which motor to move? ")
    if forWhich=="0":
        homePos(haath)
        break
    try:
        vol= int(input("Enter value: "))
        newStr= f"{forWhich}{chr(vol)}{chr(60)}"
        place= command.index(forWhich)
        oldStr= command[place:place+3]
        print(oldStr)
        command= command.replace( oldStr, newStr)
        print(command)
        haath.write(command.encode())
    except:
        break

