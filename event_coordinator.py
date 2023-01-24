guests = {}


def read_guestlist(file_name):
    text_file = open(file_name, 'r')
    while True:
        line_data = text_file.readline().strip().split(",")
        if len(line_data) < 2:
            # If no more lines, close file
            text_file.close()
            break
        name = line_data[0]
        age = int(line_data[1])
        guests[name] = age
        val = yield name, age
        if val is not None:
            val = val.split(",")
            name = val[0]
            age = int(val[1])
            guests[name] = age
            yield name, age


guest_list = read_guestlist("guest_list.txt")

for i in range(10):
    print(next(guest_list))

print(guest_list.send("Jane,35"))
print(next(guest_list))
print(next(guest_list))
print(next(guest_list))
# print(next(guest_list))

print(guests)
guests_over_21 = (name for name in guests if int(guests[name]) >= 21)

for guest in guests_over_21:
    print(guest)


def chicken_table():
    food, table = "Chicken", 1
    for i in range(1, 6):
        yield (food, f"Table {table}", f"Seat: {i}")


def beef_table():
    food, table = "Beef", 2
    for i in range(1, 6):
        yield (food, f"Table {table}", f"Seat: {i}")


def fish_table():
    food, table = "Fish", 3
    for i in range(1, 6):
        yield (food, f"Table {table}", f"Seat: {i}")


def combined_tables():
    yield from chicken_table()
    yield from beef_table()
    yield from fish_table()


def table_assigner(guests, table_gen):
    for guest in guests:
        yield (guest, next(table_gen))


all_tables_gen = combined_tables()

seats = table_assigner(guests, all_tables_gen)

for seat in seats:
    print(seat)
