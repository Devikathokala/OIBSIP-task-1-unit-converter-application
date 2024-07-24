def meters_to_kilometers(meters):
    return meters / 1000.0

def meters_to_miles(meters):
    return meters * 0.000621371

def meters_to_feet(meters):
    return meters * 3.28084

def meters_to_inches(meters):
    return meters * 39.3701

def main():
    print("Welcome to the Length Unit Converter!")
    print("Supported units: meters, kilometers, miles, feet, inches")

    try:
        value = float(input("Enter the length value: "))
        unit_from = input("Enter the unit to convert from (e.g., meters): ").strip().lower()
        unit_to = input("Enter the unit to convert to (e.g., kilometers): ").strip().lower()
        
        if unit_from == "meters":
            meters = value
        elif unit_from == "kilometers":
            meters = value * 1000.0
        elif unit_from == "miles":
            meters = meters_to_miles(value)
        elif unit_from == "feet":
            meters = meters_to_feet(value)
        elif unit_from == "inches":
            meters = meters_to_inches(value)
        else:
            print("Unsupported unit to convert from.")
            return
        
        if unit_to == "meters":
            result = meters
        elif unit_to == "kilometers":
            result = meters_to_kilometers(meters)
        elif unit_to == "miles":
            result = meters_to_miles(meters)
        elif unit_to == "feet":
            result = meters_to_feet(meters)
        elif unit_to == "inches":
            result = meters_to_inches(meters)
        else:
            print("Unsupported unit to convert to.")
            return
        
        print(f"{value} {unit_from} is equal to {result} {unit_to}")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
