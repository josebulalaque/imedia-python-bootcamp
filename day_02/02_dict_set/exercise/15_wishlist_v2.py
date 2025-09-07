# TODO: Fill in the details of the items you plan to buy
orders = [{
    "Name": "Laptop",
    "Info": "High end laptop"
},
{
    "Name": "Desktop",
    "Info": "High end desktop"
},
{
    "Name": "Router",
    "Info": "High end router"
}
]

# TODO: Print the item details in the following format (for each order):

for order in orders: #orders datatype is list
    print("Order:")
    for key, value in order.items(): #order datatype here is dictionary
        print(f"\t{key} : {value}")

"""
Order:
	Name: item name
	Info: item info
	...
"""
