def checkSpeed(speed):
    point=0
    if speed<=70:
        print("OK")
    else:
        value=speed-70
        value=value//5
        point+=value
        if point >= 12:
            print("License Suspended")
        else:
            print("Points = ",point)

speed=int(input("Enter the speed"))
checkSpeed(speed)
