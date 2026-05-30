from car import Car

def main() -> None:
    my_car = Car("2026", "Mustang Dark Horse")
    
    for i in range(1, 6):
        my_car.accelerate()
        print(f"Call {i}: Current speed is {my_car.get_speed()} mph")

    for i in range(1, 6):
        my_car.brake()
        print(f"Call {i}: Current speed is {my_car.get_speed()} mph")

if __name__ == "__main__":
    main()