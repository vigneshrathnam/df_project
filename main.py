import requests
import pandas as pd
url = "http://dummy.restapiexample.com/api/v1/employees"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
}
req = requests.get(url, headers=headers)
# I added 'User-Agent' Header field since it throws me 406 HTTP error from server.

data = None
if req.status_code >= 200 and req.status_code < 400:
    data = req.text
else:
    print("Some error occured in the website. Status code - %s\n\
        So using the json data from local server " % req.status_code)
    with open("file.json", 'r') as file:
        data = file.read()
df = pd.read_json(data)
df = pd.json_normalize(df['data'])
file_name = "data.csv"
df.to_csv(file_name, index=False)
df = pd.read_csv(file_name)
df = df.dropna(1)

def press_key():
    input("\n\nPress Enter to continue...\n\n")

def invalid_input():
    print("\n\tInvalid input! Please try again...")
    press_key()

def print_df(df):
    if len(df) > 0:
        print(df.to_string(index=False))
    else:
        print("\n\tDataFrame is Empty")

while(True):
    print("\n\tOptions:\
    \n\t  1. List First X values\
    \n\t  2. List Employee details where salary<=X\
    \n\t  3. List Employee details where salary>=X\
    \n\t  4. List Employee names where age<=X\
    \n\t  5. List Employee names where age>=X\
    \n\t  6. Get Employee details based on id,name\
    \n\t  7. Exit\
    \n\
    ")
    try:
        choice = int(input("\tEnter your choice:\t "))
    except:
        invalid_input()
        continue
    if choice == 1:
        try:
            N = int(input("\n\tEnter the count:\t "))
        except:
            invalid_input()
            continue
        value = df.head(N)[['employee_name', 'employee_salary',
                            'employee_age']]
        print_df(value)
        press_key()
    elif choice == 2:
        try:
            salary = int(input("\n\tEnter the salary:\t"))
        except:
            invalid_input()
            continue
        value = df[df.employee_salary <= salary][['employee_name',
                                                  'employee_salary', 'employee_age']]
        print_df(value)
        press_key()
    elif choice == 3:
        try:
            salary = int(input("\n\tEnter the salary:\t"))
        except:
            invalid_input()
            continue
        value = df[df.employee_salary >= salary][['employee_name',
                                                  'employee_salary', 'employee_age']]
        print_df(value)
        press_key()
    elif choice == 4:
        try:
            age = int(input("\n\tEnter the age to filter:\t"))
        except:
            invalid_input()
            continue
        value = df[df.employee_age <= age]
        [['employee_name']]
        print_df(value)
        press_key()
    elif choice == 5:
        try:
            age = int(input("\n\tEnter the age to filter:\t"))
        except:
            invalid_input()
            continue
        value = df[df.employee_age >= age]
        [['employee_name']]
        print_df(value)
        press_key()
    elif choice == 6:
        try:
            print("\n\tChoose:\
                \n\t  1. Name\
                \n\t  2. ID\
                \n\t  3. Close\
                ")
            choice_2 = int(input("\n\tEnter the input:\t"))
        except:
            invalid_input()
            continue
        if choice_2 == 1:
            try:
                name = str(input("\n\tEnter the name:\t"))
            except:
                invalid_input()
                continue
            if len(name)==0:
                invalid_input()
                continue
            value = df[df.employee_name.str.contains(name, case=False)][[
                'employee_name', 'employee_salary', 'employee_age']]
            print_df(value)
        elif choice_2 == 2:
            try:
                id = int(input("\n\tEnter the employee id:\t"))
            except:
                invalid_input()
                continue
            value = df[df.id == id][['employee_name', 'employee_salary',
                                     'employee_age']]
            print_df(value)
        elif choice_2 == 3:
            continue
        else:
            invalid_input()
            continue
        press_key()
    elif choice == 7:
        exit()
    else:
        invalid_input()
        continue
