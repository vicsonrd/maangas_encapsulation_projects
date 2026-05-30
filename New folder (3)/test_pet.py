from pet import Pet

def main() -> None:
    my_pet = Pet()

    print("--- Pet Data Entry ---")
    user_name = input("Enter the name of your pet: ")
    user_type = input("Enter the type of animal (e.g., Dog, Cat, Bird): ")
    user_age = int(input("Enter the age of your pet: "))

    my_pet.set_name(user_name)
    my_pet.set_animal_type(user_type)
    my_pet.set_age(user_age)

    print("\n--- Retrieving Pet Data ---")
    print(f"Pet Name: {my_pet.get_name()}")
    print(f"Animal Type: {my_pet.get_animal_type()}")
    print(f"Age: {my_pet.get_age()}")

if __name__ == "__main__":
    main()