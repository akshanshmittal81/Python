seat_type=input("Enter seat type (sleeper/A/General/Luxury)").lower()
if seat_type not in ["sleeper","ac","general","luxury"]:
    print("invalid seat type")
else:    
    match seat_type:
        case "sleeper":
            print("Sleeper=No AC,beds available")
        case "ac":
            print("AC=Air conditional, comfy ride")
        case "general":
            print("Genaral-Cheapest option,no reservation")
        case "luxury":
            print("Luxury-Premium seats with meals")
        case _:
            print("Invalid seat type")                
