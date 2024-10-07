# DSC 510
# Week 6
# Programming Assignment Week 6
# Author TOUKA
# 10/5/2024

# Program to manage a list of temperatures

def main():
    temperatures = []
    print("Enter temperatures (type 'stop' to end) :")

    while True:
        enter = input("Temperature: ")
        if enter.lower() == 'stop':
            break
        try:
            temperature = float(enter)
            temperatures.append(temperature)
        except ValueError:
            print("Invalid input. Please enter a number or 'stop'.")

    if temperatures:
        temp_max = max(temperatures)
        temp_min = min(temperatures)
        total = len(temperatures)

        print(f"\nLargest temperature: {temp_max}°F")
        print(f"Smallest temperature: {temp_min}°F")
        print(f"Number of temperatures : {total}")

    else:
        print("No temperatures were entered.")

if __name__ == "__main__":
    main()

