import os
import csv

#Define the variables
months = []
profit_loss_change = []

total_mos = 0
net_profit_loss = 0
prev_mos_profit_loss = 0
curr_mos_profit_loss = 0
profit_loss_change = 0

# Define path
main_csv = os.path.join( 'Resources', 'budget_data.csv')

# Open and read csv
with open(main_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read header row 
    csv_header = next(csv_file)

    print(f"Header: {csv_header}")


 
    #for row in csv_reader:
     #   print (row[0])



'''total_months = 0
total_profit_losses = 0

for row in csv_reader:
  
  
  date = row[0]
  profit_losses = row[1]
  total_months = 
  total_profit_losses = int(row[1])

  print(total_months)
'''
# Create a function and have it accept 'final_data' as its sole parameter
#def final_data(main_data):

    # Assign values to variables with descriptive names
 #   months = str(main_data[0])
 #   profit_losses = float(main_data[1])

    # * The total number of months included in the dataset - 
 #   final_data(months).sum()

'''
    total_months = 0  
    total_profit_losses = 0

for row in csv_reader: #(***3.3 1:52:00)
    date = row[0]
    profit_losses = row[1]
    total_months += 1
    total_profit_losses += int(row[1])

bank_data = []

for row in csv_reader:
    profit_losses = row[1]
    bank_data.append(profit_losses)



* Your task is to create a Python script that analyzes the records to calculate each of the following:
  
  * The total number of months included in the dataset - 

  * The net total amount of "Profit/Losses" over the entire period

  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* As an example, your analysis should look similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
'''




