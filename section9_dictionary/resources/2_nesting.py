# Nesting

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg"], "total_visits": 5},
}

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
