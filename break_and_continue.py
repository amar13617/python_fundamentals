cars = ["ok", "ok", "ok", "faulty", "ok"]
for car in cars:
    if car == "faulty":
        print("stop the production line")
        break
    print(f"this is {car}")
    print("shipping new car to production")


cars = ["ok", "ok", "ok", "faulty", "ok"]
for car in cars:
    if car == "faulty":
        print("find faulty car skipping")
        continue
    print(f"this is {car}")
    print("shipping new car to production")

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break

    print(f"This car is {status}.")
else:
    print("All cars built successfully. No faulty cars!")

