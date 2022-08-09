from post_code_api import PostcodeChecker

postcode = PostcodeChecker("rm137bs")
print(postcode.get_postcode())
print(postcode.get_latitude())
print(postcode.get_longitude())
