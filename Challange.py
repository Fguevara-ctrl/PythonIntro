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

print(fav_cars[0]["Model"])
print(fav_cars[0]["Make"])

print(fav_cars[1]["Make"])
print(fav_cars[1]["Model"])

print(fav_cars[1]["Modes"][1])