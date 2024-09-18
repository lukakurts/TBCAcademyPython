automobile_speed = float(input("please enter your automobile speed: "))

if automobile_speed >= 120:
    print("very fast")
elif automobile_speed >= 60:
    print("fast")
elif automobile_speed >= 30:
    print("moderate")
else:
    print("slow")
