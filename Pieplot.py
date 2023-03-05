#importing required libraries
import matplotlib.pyplot as plt
import pandas as pd


#define a function called rating_fpoc_Pie()
def rating_fpoc_Pie():
    
    
    # read the csv file using pandas and store the data in 'df' dataframe
    df = pd.read_csv('Book2.csv')
    
    
    # Extracting the required data from the dataframe to plot the pie chart
    labels = df['Age Group'].tolist()
    sizes = df['Death-rate '].tolist()
    
    # Creating a pie chart using the extracted data 
    plt.pie(sizes, labels=labels, autopct='%1.1f%%' )
    
    
        
    # Adding a title to the chart
    plt.title('WHO Mortality Death Database', fontsize='20')
    
   
    # Add legend and title
    legend = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5,))
    legend.set_title('Age')
   

    
    # Display the chart
    return(plt.show())

#Call the function rating_fpoc_Pie() and store the returned value in variable PieChart    
PieChart = rating_fpoc_Pie()

#Print the PieChart variable
print(PieChart)