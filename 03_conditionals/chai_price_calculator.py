cup=input("Choose your cup size (small/medium/large):").lower()
if cup not in ["small", "medium", "large"]:
    print("invlid input")
else:    
    if cup=="small":
        print("Price is 10 rupees")
    elif cup=="medium":
        print("Price is 15 rupees")
    elif cup=="large":
        print("Price is 25 rupees")
    else:
        print("Unknown cupsize")    
    


