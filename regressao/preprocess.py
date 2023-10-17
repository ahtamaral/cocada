import csv
from datetime import datetime, timedelta

# Define the CSV file name
csv_file = "pesagem.csv"

# Initialize empty arrays to store data
data = []

# Open the CSV file and read its contents
with open(csv_file, mode='r', newline='') as file:
    csv_reader = csv.reader(file, delimiter=' ')
    
    # Read the first date and parse it
    first_date_str = next(csv_reader)[0]
    first_date = datetime.strptime(first_date_str, '%d/%m')
    
    # Reset the file pointer to the beginning
    file.seek(0)
    
    for row in csv_reader:
        date_str = row[0]
        date = datetime.strptime(date_str, '%d/%m')
        
        # Calculate the difference in days and update the date
        day_difference = (date - first_date).days
        row[0] = str(day_difference)
        
        data.append(row)

# Now, 'data' contains the updated dates with the first date as zero
# You can access the data like this:
#for row in data:
#    print(row)


with open('processed-pesagem.csv', mode='w', newline='') as file:
	writer = csv.writer(file)
	for row in data:
		writer.writerow(row)

