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




