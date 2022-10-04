# Define imports
import pandas
import json

# read excel by using specific column
excel_data = pandas.read_excel("Doctors _Login _Details_with_Clinic _manager _email.xlsx", usecols= ["Clinic Manager  ID ","Official Id","Map Co-ordinates"])

# convert excel sheet to dictionary
excel__to_json = excel_data.to_json(orient="records")



with open("Doctors _Login _Details_with_Clinic _manager _email.json", "w") as f:
    f.write(excel__to_json)