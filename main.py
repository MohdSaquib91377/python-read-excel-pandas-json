# Define imports
import pandas
import json

# Read excel by using specific column
excel_data = pandas.read_excel("Doctors _Login _Details_with_Clinic _manager _email.xlsx", usecols= ["Clinic Manager  ID ","Official Id","Map Co-ordinates"])

# Convert excel sheet to dictionary
excel__to_json = excel_data.to_json(orient="records")

#Dum into json file
with open("Doctors _Login _Details_with_Clinic _manager _email.json", "w") as f:
    f.write(excel__to_json)

# Read data from json file
with open("Doctors _Login _Details_with_Clinic _manager _email.json","r") as f:
    data = json.load(f)
    
for item in data:
    print(f"{item['Clinic Manager  ID ']} ------> {item['Official Id']}   ------> {item['Map Co-ordinates']}")