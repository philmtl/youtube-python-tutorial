monthConversions = {
    "jan": "january",
    "feb":"febuary",
    "jun":"june",
}

print(monthConversions["feb"])

print(monthConversions.get("feb"))
print(monthConversions.get("luv", "not a valid key"))