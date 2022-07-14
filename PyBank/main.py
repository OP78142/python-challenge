# import dependencies
import os
import csv

# Define vars
profit_loss_changes = []
months=[]

net_profit_loss = 0
prev_mth_profit_loss = 0
cur_mth_profit_loss = 0
profit_loss_chg = 0

count_months = 0

# Open file
budget_data_CSV_path = os.path.join('Resources', 'budget_data.csv')
#csvpath = os.path.join('..', 'Resources', 'contacts.csv')

# Collect data
with open(budget_data_CSV_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read Headers
    csv_header = next(csvfile)

    # Read through data by row
    for row in csv_reader:
        count_months +=1
        cur_mth_profit_loss = int(row[1])
        net_profit_loss += cur_mth_profit_loss
        if  (count_months ==1):
            # Make the value of previous month to be equal to current month
            prev_mth_profit_loss = cur_mth_profit_loss
            continue

        else:
                #Compute change
                profit_loss_chg = cur_mth_profit_loss - prev_mth_profit_loss

                # Append Months
                months.append(row[0])

                #Append loss change
                profit_loss_changes.append(profit_loss_chg)

                # Set the cur_mth_profit_loss to be prev_mth_profit_loss for the next loop
                prev_mth_profit_loss = cur_mth_profit_loss

        # Sum and Average of the changes in "Profit/Losses" column over the full period
        sum_profit_loss = sum(profit_loss_changes)
        avg_profit_loss = round(sum_profit_loss / (count_months - 1), 2)

        # Highest and Lowest change in "Profit/Losses" column over the full period
        highest_change = max(profit_loss_changes)
        lowest_change = min(profit_loss_changes)

        # Find the index of the highest and lowest changes in "Profit/Losses" column over the full period
        highest_month_index = profit_loss_changes.index(highest_change)
        lowest_month_index = profit_loss_changes.index(lowest_change)

        # Define the best and worst months
        best_month = months[highest_month_index]
        worst_month = months[lowest_month_index]

# Output the data to the terminal
print("Financial Details")
print("--------------------------------------------")
print(f"Total Number of Months:  {count_months}")
print(f"Total dollar amount:  ${net_profit_loss}")
print(f"Mean Change:  ${avg_profit_loss}")
print(f"Greatest Profit Increase:  {best_month} (${highest_change})")
print(f"Greatest Loss Decrease:  {worst_month} (${lowest_change})")

# Check if Analysis folder has already been created
isExist = os.path.exists("Analysis")

if not isExist:
    # Create a new directory because it does not exist
    os.mkdir("Analysis")


# Output the data as text file

analysis_file = os.path.join("analysis", "analysis_data.txt")
with open(analysis_file, "w") as outfile:

    outfile.write("Financial Details\n")
    outfile.write("--------------------------------------------\n")
    outfile.write(f"Total Number of Months:  {count_months}\n")
    outfile.write(f"Total dollar amount:  ${net_profit_loss}\n")
    outfile.write(f"Mean Change:  ${avg_profit_loss}\n")
    outfile.write(f"Greatest Profit Increase:  {best_month} (${highest_change})\n")
    outfile.write(f"Greatest Loss Decrease:  {worst_month} (${lowest_change})\n")




