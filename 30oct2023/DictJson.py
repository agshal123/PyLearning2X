#Convert to Dict JSON Response and Print and Booking Id AND checkin and Checkout Data

dict_response={

"bookingid": 2384,

"booking": {

"firstname": "PRAMOD",

"lastname": "Dutta",

"totalprice": 432,

"depositpaid": False,

"bookingdates": {

"checkin": "2022-01-01",

"checkout": "2022-01-01"

},

"additionalneeds": "Lunch"

}

}
print(dict_response["bookingid"])
print(dict_response.get("booking",{}).get("bookingdates"))

