def find_item_by_name(items, item_name):
    return next((i for i in items if item_name in i.name), None)

# Generator:
# (expression for element in iterable if condition)
# numbers = (i+1 for i in range(1,10) if i%2==0)
# list(numbers) returns the result