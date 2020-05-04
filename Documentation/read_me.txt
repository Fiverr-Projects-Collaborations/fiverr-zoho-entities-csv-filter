Prerequisite:
-- Python 3.7.7
-- Names of the files MUST be same.


1. Installing required packages to run script.py file.
- Open terminal/command prompt.
- Navigate to the project folder "an_Zoho".
- Execute command
Command : pip install -r requirement.txt

2. Replace dummy files with required files from "Data/Data - DF" directory.
3. Replace "EXCEL LIST.xlsx" under "Data" directory.
4. Make sure "Output" directory is empty (else data will be overwritten).
5. Execute script script.py 
Command : python_path script.py

----------------------------------------------------------------------------------------
To write data into database:
-- Modify config file and put required information to connect MySQL database.
Host Name : host
Database Name: db
User Name to login: user
Passoword: pass

-- uncomment code line
engine = database_config()

-- Put below code in place of each, to_csv line of code

df_to_db(engine, name_of_dataframe, 'table_name')

name_of_dataframe : Variable names with the postfix "_filtered"
e.g. : account_details_filtered, contact_details_filtered, leads_details_filtered etc

table_name: Name of the table in which data should be inserted into.

For reference see line number : 74