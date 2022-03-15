a = input("Enter your car model:")
if a.lower() == "toyota" or a.lower() == "lexus":
    b = int(input("Year of manufacture:"))
    if b >= 2004:
        c = input("Color of car:")
        if c.lower() == "white" or c.lower() == "grey":
            e = int(input("Number of former owners:"))
            if e <= 2:
                f = input("Left or right rudder:")
                if f.lower() == "left":
                    d = int(input("Total KM:"))
                    if d <= 150000:
                        g = int(input("Price:"))
                        if g <= 10000:
                            print(g, "1st option")
                    elif d <= 2000000:
                        g = int(input("Price:"))
                        if g <= 8000:
                            print(g, "2nd option")
