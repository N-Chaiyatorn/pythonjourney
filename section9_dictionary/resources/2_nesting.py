# Nesting

travel_log = {
    "France": {
            "cities_visited": ["Paris", "Lille", "Dijon"], 
            "total_visits": 12
            },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg"], 
        "total_visits": 5
        },
}

print(travel_log["France"]["total_visits"])            #The result is 12     
travel_log = [
    {
        country: "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        country: "Germany",
        "cities_visited": ["Berlin", "Hamburg"],
        "total_visits": 5,
    },
]
