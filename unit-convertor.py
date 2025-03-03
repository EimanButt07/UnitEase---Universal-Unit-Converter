import streamlit as st

# Set up the app title
st.title("🌍 Unit Converter App")
st.markdown("### Convert units easily between different measurement systems!")

# User selects a category of conversion
category = st.selectbox("Select the unit category:", ["Length", "Weight", "Time", "Temperature"])

# Function to handle unit conversion
def convert_units(category, value, unit):
    """Convert values between different units based on category."""
    
    # Length Conversions
    if category == "Length":
        conversions = {
            "Kilometers to Miles": value * 0.621371,
            "Miles to Kilometers": value / 0.621371,
            "Meters to Feet": value * 3.28084,
            "Feet to Meters": value / 3.28084,
            "Inches to Centimeters": value * 2.54,
            "Centimeters to Inches": value / 2.54,
            "Yards to Meters": value * 0.9144,
            "Meters to Yards": value / 0.9144,
            "Miles to Yards": value * 1760,
            "Yards to Miles": value / 1760
        }
    
    # Weight Conversions
    elif category == "Weight":
        conversions = {
            "Kilograms to Pounds": value * 2.20462,
            "Pounds to Kilograms": value / 2.20462,
            "Grams to Ounces": value * 0.035274,
            "Ounces to Grams": value / 0.035274,
            "Milligrams to Grams": value / 1000,
            "Grams to Milligrams": value * 1000,
            "Metric Tons to Kilograms": value * 1000,
            "Kilograms to Metric Tons": value / 1000,
            "Stones to Pounds": value * 14,
            "Pounds to Stones": value / 14
        }
    
    # Time Conversions
    elif category == "Time":
        conversions = {
            "Seconds to Minutes": value / 60,
            "Minutes to Seconds": value * 60,
            "Minutes to Hours": value / 60,
            "Hours to Minutes": value * 60,
            "Hours to Days": value / 24,
            "Days to Hours": value * 24,
            "Days to Weeks": value / 7,
            "Weeks to Days": value * 7,
            "Weeks to Months": value / 4.345,
            "Months to Weeks": value * 4.345,
            "Months to Years": value / 12,
            "Years to Months": value * 12
        }
    
    # Temperature Conversions
    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9
        elif unit == "Celsius to Kelvin":
            return value + 273.15
        elif unit == "Kelvin to Celsius":
            return value - 273.15
        elif unit == "Fahrenheit to Rankine":
            return value + 459.67
        elif unit == "Rankine to Fahrenheit":
            return value - 459.67
        elif unit == "Kelvin to Rankine":
            return value * 1.8
        elif unit == "Rankine to Kelvin":
            return value / 1.8
        else:
            return None  # Handle unexpected cases
    
    # Return the converted value
    return conversions.get(unit, None)

# Define unit conversion options for each category
unit_options = {
    "Length": [
        "Kilometers to Miles", "Miles to Kilometers", "Meters to Feet", "Feet to Meters", 
        "Inches to Centimeters", "Centimeters to Inches", "Yards to Meters", "Meters to Yards",
        "Miles to Yards", "Yards to Miles"
    ],
    "Weight": [
        "Kilograms to Pounds", "Pounds to Kilograms", "Grams to Ounces", "Ounces to Grams", 
        "Milligrams to Grams", "Grams to Milligrams", "Metric Tons to Kilograms", 
        "Kilograms to Metric Tons", "Stones to Pounds", "Pounds to Stones"
    ],
    "Time": [
        "Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes",
        "Hours to Days", "Days to Hours", "Days to Weeks", "Weeks to Days",
        "Weeks to Months", "Months to Weeks", "Months to Years", "Years to Months"
    ],
    "Temperature": [
        "Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius",
        "Fahrenheit to Rankine", "Rankine to Fahrenheit", "Kelvin to Rankine", "Rankine to Kelvin"
    ]
}

# User selects the specific conversion type
unit = st.selectbox(f"Select the conversion type for {category}:", unit_options[category])

# User inputs the value to be converted
value = st.number_input(f"Enter the value to convert ({unit.split(' ')[0]}):", min_value=0.0)

# Perform conversion when the button is clicked
if st.button("Convert"):
    result = convert_units(category, value, unit)
    
    if result is not None:
        st.success(f"✅ Converted Value: {result:.4f}")
    else:
        st.error("⚠️ Something went wrong with the conversion. Please check your inputs.")
