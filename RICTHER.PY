'''# Function to determine the result based on Richter magnitude
def analyze_richter_magnitude(magnitude):
    if 1.0 <= magnitude < 2.0:
        result = "Microearthquakes not felt or rarely felt"
    elif 2.0 <= magnitude < 4.0:
        result = "Very rarely causes damage"
    elif 4.0 <= magnitude < 5.0:
        result = "Damage done to weak buildings"
    elif 5.0 <= magnitude < 6.0:
        result = "Cause damage to poorly constructed buildings"
    elif 6.0 <= magnitude < 7.0:
        result = "Causes damage to well-built structures"
    elif 7.0 <= magnitude < 8.0:
        result = "Causes damage to most buildings"
    elif 8.0 <= magnitude < 9.0:
        result = "Causes major destruction"
    elif magnitude >= 9.0:
        result = "Causes unbelievable damage"
    else:
        result = "Magnitude value should be non-negative"

    return result

# Main program
try:
    # Read Richter magnitude from the user
    magnitude = float(input("Enter the Richter magnitude value: "))
    
    # Ensure the magnitude is non-negative
    if magnitude < 0:
        print("Please enter a non-negative Richter magnitude.")
    else:
        # Analyze and display the result
        result = analyze_richter_magnitude(magnitude)
        print(f"For Richter magnitude {magnitude}, the result is: {result}")

except ValueError:
    print("Invalid input. Please enter a valid numerical value for Richter magnitude.")'''