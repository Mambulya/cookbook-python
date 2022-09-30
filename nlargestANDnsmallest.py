from heapq import nlargest, nsmallest


products = [
    {"name": "bred", "price": 100, "weight": 30},
    {"name": "milk", "price": 20, "weight": 50},
    {"name": "pear", "price": 5, "weight": 10},
    {"name": "apple", "price": 5, "weight": 5}
]

print(nlargest(2, products, key = lambda s: s["price"]))
print(nsmallest(2, products, key = lambda s: s["price"]))
