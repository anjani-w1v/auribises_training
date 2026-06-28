#task---------------------------------------------------------
# Identify the use cases where u see references copy opertains.






#task---------------------------------------------------------
# code (zomaao) screen






# Assignment:---------------------------------------------------------
#  1. code as list of dictinaries (makemytrip.com)  2. code as dictinaries of list of dictinaries(bookmyshow.com)

#1
flights = [             #in list no key
    {
        "airline": "Air India",
        "flight_no": "AI 7713",
        "from": "DEL",
        "to": "ZRH",
        "departure": "01:05",
        "arrival": "06:20",
        "duration": "08h 45m",
        "stops": "Non-stop",
        "price": 156593,
        "trip": "Onward"
    },

    {
        "airline": "Swiss",
        "flight_no": "LX 2646",
        "from": "ZRH",
        "to": "DEL",
        "departure": "12:35",
        "arrival": "00:05 +1 Day",
        "duration": "08h",
        "stops": "Non-stop",
        "price": 156593,
        "trip": "Return"
    }
]

print(flights)


#2
theatre = {
    "Prime": [
        {"row": "F", "seat": 10, "price": 380, "status": "Available"},
        {"row": "E", "seat": 11, "price": 380, "status": "Unavailable"},
        {"row": "D", "seat": 12, "price": 380, "status": "Available"}
    ],

    "Classic": [
        {"row": "C", "seat": 13, "price": 300, "status": "Available"},
        {"row": "B", "seat": 12, "price": 300, "status": "Available"},
        {"row": "A", "seat": 11, "price": 300, "status": "Available"}
    ]
}