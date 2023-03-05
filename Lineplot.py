import matplotlib.pyplot as plt
import pandas as pd

#define a function called child_social_care_func()
def child_social_care_func():
    
    #read the csv file using pandas and store the data in 'df' dataframe
    df = pd.read_csv("Children_s_social_care_in_England_2022_underlying_data (1).csv")
   
    
    df.dropna(inplace=True)
    
    ## Creating a Line chart using the extracted data 
    line_chart1 = plt.plot(df["Years"], df["Residential Special Schools"])
    line_chart2 = plt.plot(df["Years"], df["Residential Family Centres"])
    line_chart3 = plt.plot(df["Years"], df["Adoption Support Agencies"])
    line_chart4 = plt.plot(df["Years"], df["Further Education Colleges with Residential Accommodation"])
    line_chart4 = plt.plot(df["Years"], df["Adoption Support Agencies"])

    # Adding a title to the chart
    plt.title('National number of Childrens social care places six monthly')
    
    #Adding the label of x-axis and y-axis
    plt.xlabel('Years')
    plt.ylabel('Number Of Childrens')
    
    # Add legend and title
    plt.legend(["Residential Special Schools", "Residential Family Centres","Adoption Support Agencies","Further Education Colleges with Residential Accommodation","Adoption Support Agencies"],loc='center left', bbox_to_anchor=(1, 0.5,))
    
    plt.show()
    
    
child_social_care_func()