import matplotlib.pyplot as plt
import pandas as pd

def create_bar_plot():
    # Read data from CSV file using Pandas
    df = pd.read_csv('Book2.csv')

    # Extract data for x-axis and y-axis from dataframe
    x_data = df['Age Group'].tolist()
    y_data = df['Percentage of cause-specific deaths out of total deaths'].tolist()

    # Create a bar plot
    plt.bar(x_data, y_data )

    # Set the x and y axis labels
    plt.xlabel('Age Group')
    plt.ylabel('Percentage' )

    # Set the chart title
    plt.title('Bar Plot Title')
    
    

    # Display the chart
    plt.show()

# Call the function to create the bar plot
create_bar_plot()
