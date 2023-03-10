import xml.etree.ElementTree as ET
tree = ET.parse('wf_load_customer_order_summary.xml')

# Get the root element
root = tree.getroot()

orders_elem = root.find(".//*[@NAME='CUSTOMER']")
print("CUSTOMER")
for field_elem in orders_elem.findall("./SOURCEFIELD"):
    print(field_elem.get('NAME'), end=" ")
print()
orders_elem = root.find(".//*[@NAME='ORDERS']")


print("ORDERS")


for field_elem in orders_elem.findall("./SOURCEFIELD"):

    print(field_elem.get('NAME'), end=" ")

print()


orders_elem = root.find(".//*[@NAME='LINEITEM']")


print("LINEITEM")


for field_elem in orders_elem.findall("./SOURCEFIELD"):

    # Print the name attribute of the field element

    print(field_elem.get('NAME'), end=" ")


print()


orders_elem = root.find(".//*[@NAME='PART']")


print("PART")


for field_elem in orders_elem.findall("./SOURCEFIELD"):

    # Print the name attribute of the field element

    print(field_elem.get('NAME'), end=" ")


print()


orders_elem = root.find(".//*[@NAME='SUPPLIER']")


print("SUPPLIER")


for field_elem in orders_elem.findall("./SOURCEFIELD"):

    # Print the name attribute of the field element

    print(field_elem.get('NAME'), end=" ")


print()


orders_elem = root.find(".//*[@NAME='FACT_CUSTOMER_ORDERS_SUMMARY']")

print("FACT_CUSTOMER_ORDERS_SUMMARY")

for field_elem in orders_elem.findall("./TARGETFIELD"):

    # Print the name attribute of the field element

    print(field_elem.get('NAME'), end=" ")


print()
