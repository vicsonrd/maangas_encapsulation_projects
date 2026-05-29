from fan import Fan

def main():
    
    fan1 = Fan()
    fan1.set_speed(Fan.FAST)
    fan1.set_radius(10.0)
    fan1.set_color("yellow")
    fan1.set_on(True)

    
    fan2 = Fan()
    fan2.set_speed(Fan.MEDIUM)
    fan2.set_radius(5.0)
    fan2.set_color("blue")
    fan2.set_on(False)

    
    print("--- Fan 1 Properties ---")
    print(f"Speed: {fan1.get_speed()}")
    print(f"Radius: {fan1.get_radius()}")
    print(f"Color: {fan1.get_color()}")
    print(f"Is On?: {fan1.get_on()}\n")

    print("--- Fan 2 Properties ---")
    print(f"Speed: {fan2.get_speed()}")
    print(f"Radius: {fan2.get_radius()}")
    print(f"Color: {fan2.get_color()}")
    print(f"Is On?: {fan2.get_on()}")

if __name__ == "__main__":
    main()