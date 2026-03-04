import re

with open("raw.txt", "r") as file:
    text = file.read()

print("Receipt text:")
print(text)


import re

with open("raw.txt", "r") as file:
    text = file.read()

# 1. Extract all prices
prices = re.findall(r"\d+\.\d{2}", text)
print("Prices:", prices)


# 2. Find all product names
products = [p.strip() for p in re.findall(r"([A-Za-z ]+)\s+\d+\.\d{2}", text)]
print("Products:", products)


# 3. Extract date
date = re.search(r"\d{2}/\d{2}/\d{4}", text)
print("Date:", date.group() if date else "Not found")

# 4. Extract time
time = re.search(r"\d{2}:\d{2}", text)
print("Time:", time.group() if time else "Not found")

# 5. Find payment method
payment = re.search(r"Payment Method:\s*(\w+)", text)
print("Payment Method:", payment.group(1) if payment else "Not found")

# 6. Calculate total
total = sum(float(price) for price in prices)
print("Calculated Total:", total)

# 7. Structured output (JSON)
import json
receipt_data = {
    "products": [p.strip() for p in products],
    "prices": prices,
    "total": total,
    "date": date.group() if date else None,
    "time": time.group() if time else None,
    "payment_method": payment.group(1) if payment else None
}
print(json.dumps(receipt_data, indent=4))

import re

# 01 Match: 'a' followed by zero or more 'b'
pattern = r"^ab*$"
text = input()
if re.match(pattern, text):
    print("Match found")
else:
    print("No match")


# 02 Match: 'a' followed by two to three 'b'
pattern = r"^ab{2,3}$"
text = input()
if re.match(pattern, text):
    print("Match found")
else:
    print("No match")


# 03 Find lowercase words joined with underscore
text = input()
matches = re.findall(r"\b[a-z]+_[a-z]+\b", text)
print(matches)


# 04 Find one uppercase letter followed by lowercase letters
text = input()
matches = re.findall(r"\b[A-Z][a-z]+\b", text)
print(matches)


# 05 Match 'a' followed by anything, ending in 'b'
pattern = r"^a.*b$"
text = input()
if re.match(pattern, text):
    print("Match found")
else:
    print("No match")


# 06 Replace space, comma, or dot with colon
text = input()
result = re.sub(r"[ ,\.]", ":", text)
print(result)


# 07 Convert snake_case to camelCase
text = input()
result = re.sub(r"_([a-z])", lambda x: x.group(1).upper(), text)
print(result)


# 08 Split string at uppercase letters
text = input()
result = re.split(r"(?=[A-Z])", text)
print(result)


# 09 Insert spaces between words starting with capital letters
text = input()
result = re.sub(r"(?<!^)(?=[A-Z])", " ", text)
print(result)


# 10 Convert camelCase to snake_case
text = input()
result = re.sub(r"(?<!^)([A-Z])", r"_\1", text).lower()
print(result)


