

#task---------------------------------------------------------
# Identify the use cases where u see references copy opertains.

# ans - ATM, mobile app, and website reference the same bank account. we can withdraw in many ways
#       Application works with the same database record.



#task---------------------------------------------------------
# code (zomaao) screen

coupons = {
    "coupon_code": "Have a coupon code? Type here",
    "restaurant_coupon": {
        "title": "Flat ₹100 OFF",
        "coupon_code": "GET100",
        "discount": 100,
        "description": "Save ₹100.00 with this code",
        "selected": True
    },

    "payment_coupons": [
        {
            "title": "5% OFF upto ₹30 using BHIM Payments App",
            "coupon_code": "BHIMAPP",
            "discount": "5% upto ₹30",
            "description": "Save ₹30.00 with this code",
            "selected": False
        },
        {
            "title": "10% OFF upto ₹100 using Utkarsh Small Finance Bank Debit Cards",
            "coupon_code": "UTKARSH",
            "discount": "10% upto ₹100",
            "description": "Save ₹89.60 with this code",
            "selected": False
        }
    ],
}

print(coupons["restaurant_coupon"]["title"])



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