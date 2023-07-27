import datetime
from datetime import date
import matplotlib.pyplot as plt
import streamlit as st

def main():
    st.title("Weeks Lived and Future Birthday Calculator")

    # Get the user's birth date
    bday = st.text_input("Enter your birth date in DD/MM/YYYY format")
    if not bday:
        st.warning("Please enter your birth date.")
        return

    # Convert the birth date to datetime object
    date_split = bday.split('/')
    day = int(date_split[0])
    month = int(date_split[1])
    year = int(date_split[2])
    bday_date = datetime.date(year, month, day)

    # Get today's date
    tday = date.today()
    st.write("Today's date is ", tday.strftime("%d/%m/%Y"))

    # Calculate the number of days and weeks lived
    days = tday - bday_date
    st.write("You have lived", days.days, "days")
    weeks = int(days.days / 7)
    st.write("You have lived", weeks, "weeks")

    # Get the future birthday date
    future_bday_number = st.text_input("Which future birth date would you like to consider for this exercise?")

    # Calculate the weeks and days left for the future birth date
    future_bday(future_bday_number, month, day, weeks)

def future_bday(future_bday_number, month, day, weeks):    
    # Get the future birthday date    
    future_bday_year = year + int(future_bday_number)
    future_bday = datetime.date(future_bday_year, month, day)

    # Calculate days and weeks until the future 90th birthday
    future_days = future_bday - tday
    st.write("Your 90th birthday is", future_days.days, "days away")
    future_weeks = int(future_days.days / 7)
    st.write("Your 90th birthday is", future_weeks, "weeks away")

    # Calculate the total number of weeks
    number_of_Circles = weeks + future_weeks

    # Create the colored chart using Matplotlib
    create_colored_chart(number_of_Circles, weeks)

def create_colored_chart(number_of_Circles, weeks):
    # Determine the number of rows required for the chart
    num_rows = (number_of_Circles + 51) // 52
    # Determine the number of circles to be colored red in the top row
    num_colored = min(weeks, number_of_Circles)

    # Create the plot using Matplotlib
    fig, ax = plt.subplots(figsize=(10, num_rows*2))

    for row in range(num_rows):
        for col in range(52):
            each_circle = row * 52 + col
            if each_circle < number_of_Circles:
                if each_circle < num_colored:
                    # Coloring the specified number of circles red in the top row
                    temp_circle = plt.Circle((col, num_rows - row - 1), 0.4, color='red', edgecolor='black', linewidth=1.5, alpha=0.7)
                else:
                    # Coloring the remaining circles black
                    temp_circle = plt.Circle((col, num_rows - row - 1), 0.4, color='black', edgecolor='black', linewidth=1.5, alpha=0.7)
                ax.add_patch(temp_circle)

    # Set plot properties
    ax.set_aspect('equal', adjustable='box')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-0.5, 51.5)
    ax.set_ylim(-0.5, num_rows - 0.5)
    plt.title(f"{num_colored} weeks completed out of {number_of_Circles} weeks")

    # Display the plot in the Streamlit app
    st.pyplot(fig)

if __name__ == "__main__":
    main()
