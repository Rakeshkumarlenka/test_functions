iterable_value = 'welcome'
iterable_obj = iter(iterable_value)

while True:
    try:

        # Iterate by calling next
        item = next(iterable_obj)
        print(item)
    except StopIteration:

        # exception will happen when iteration will over
        break