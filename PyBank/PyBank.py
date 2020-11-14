import os
import csv

#Define the variables
months = []
profit_loss_changes = []

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

    print(f"header: {csv_header}")

    #Read through rows
    for row in csv_reader:

        # The total number of months included in the dataset
        total_mos += 1
        #print(total_mos)

        # The net total amount of "Profit/Losses" over the entire period
        curr_mos_profit_loss = int(row[1])
        net_profit_loss += curr_mos_profit_loss
        print (curr_mos_profit_loss)

        # Change the index to match the month
        if (total_mos == 1):
          prev_mos_profit_loss = curr_mos_profit_loss - prev_mos_profit_loss

          # Add the months 
          months.append(row[0])

          # Change current month loss to prev month loss for next iteration
          prev_mos_profit_loss = curr_mos_profit_loss

        else:
          # Calculate the change in profit loss
          profit_loss_change = curr_mos_profit_loss - prev_mos_profit_loss

          # Add the months
          months.append(row[0])

          # Add the profit loss change to profit loss change
          profit_loss_changes.append(profit_loss_change)

          # Change current month loss to prev month loss for next iteration
          prev_mos_profit_loss = curr_mos_profit_loss

    # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    total_profit_loss = sum(profit_loss_changes)
    avg_profit_loss = round(total_profit_loss/(total_mos -1), 2)
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # Define the index of the value for the greatest increase in profits (date and amount) over the entire period
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)
    greatest_month = months[highest_month_index]
    lowest_month = months[lowest_month_index]

# Print results
print(" Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_mos}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${avg_profit_loss}")
print(f"Greatest Increase in Profits: {greatest_month} ${highest_change}")
print(f"Greatest Decrease in Profits: {lowest_month} ${lowest_change}")

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
PyBank_file = os.path.join("Resources", "PyBank_JBK.txt")
with open (PyBank_file, "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {total_mos}\n")
    outfile.write(f"Total:  ${net_profit_loss}\n")
    outfile.write(f"Average Change:  ${avg_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {greatest_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {lowest_month} (${lowest_change})\n") 

  



'''------------------------------------------------------------------------------------------------------------------------------
Disregard everything from here. This was my work throughout the week trying to organize/decompose/develop - JB Kinlacheeny

total_months = 0
total_profit_losses = 0

for row in csv_reader:
  
  
  date = row[0]
  profit_losses = row[1]
  total_months = 
  total_profit_losses = int(row[1])

  print(total_months)

Create a function and have it accept 'final_data' as its sole parameter
def final_data(main_data):

     Assign values to variables with descriptive names
 #   months = str(main_data[0])
 #   profit_losses = float(main_data[1])

    # * The total number of months included in the dataset - 
 #   final_data(months).sum()

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




