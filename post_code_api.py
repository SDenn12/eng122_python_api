"""
import the required packages
valid post-code or return invalid - url of the API address
store the data
"""
# import requests
# import json
#
# url = "http://api.postcodes.io/postcodes/"
# postcode = "e147le"
#
# url_arg = url + postcode
# # display the outcome
# print(url_arg)  # http://api.postcodes.io/postcodes/e147le
# # display url with given postcode
# r = requests.get(url_arg)
# # check the data type of data scrapped from the web-response
# print(r.status_code)
# # convert data type if needed to iterate through the data and print required information
# content = r.json()
#
# # display longitude - latitude - postcode - etc.
#
# desired = ["postcode", "longitude", "latitude"]
# for key in desired:
#     if key == "postcode":
#         confirmation = input("Please confirm the postcode. ")
#         if confirmation == content["result"]["postcode"]:
#     print(content["result"][key])


# print longitude + latitude
# once completed - create a function to do return the required value - 1 function must only return 1 value.
# create function that checks if the postcode is valid - prompt the user to input the postcode
# create a class with all of the functions
# create a file called postcode_checker.py
# import file and class, call the functions
import requests


class PostcodeChecker:
    def __init__(self, postcode):
        base_url = "http://api.postcodes.io/postcodes/"
        self.postcode = postcode
        self.url = base_url + self.postcode
        r = requests.get(self.url)
        self.data = r.json()
        self.confirm_postcode()

    def confirm_postcode(self):
        user_input = input("Please confirm your postcode. ").lower()
        if user_input != self.postcode:
            print("That was the incorrect postcode")


    def get_postcode(self):
        for key in self.data["result"].keys():
            if key == "postcode":
                return self.data["result"][key]

    def get_latitude(self):
        for key in self.data["result"].keys():
            if key == "latitude":
                return self.data["result"][key]

    def get_longitude(self):
        for key in self.data["result"].keys():
            if key == "longitude":
                return self.data["result"][key]


# postcodesss = PostcodeChecker("rm137bs")
# print(postcodesss.get_postcode())

