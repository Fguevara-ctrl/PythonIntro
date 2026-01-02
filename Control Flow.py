fav_cars = [
    {
        "Make" : "Nissan",
        "Model" : "Skyline",
        "Year" : 2002 ,
        "Legal" : False ,
        "Dealer" : None,
        "Modes" : ["Turbo", "Spoiler"]
    },
    
    {
        "Make" : "BMW",
        "Model" : "M3",
        "Year" : 1998 ,
        "Legal" : True ,
        "Dealer" : None ,
        "Modes" : ["Turbo", "Body kit"]

    }

]

if fav_cars == []:
    print("This list is empty")
    print("Please add Some cars to the list")
    print("Thank you")
elif fav_cars[0]["Make"] == "Nissan":
    print("The skyline is made by Nissan")


else:
    print("This list is not empty")
    Print(fav_cars)
    
