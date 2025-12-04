'''
Employee Data Analytics Dashboard
--------------------------------
A complete data pipeline that processes, cleans, analyzes, and reports on employee data.
'''


# Employee Database
employees = [
    # [Name, Age, Department, Salary, Email, Years_Experience]
    ["John", 35, "Engineering", 85000, "john@company.com", 8],          # 0 row
    ["Sarah", 28, "Marketing", 65000, "sarah@company.com", 4],          # 1 row
    ["Mike", 42, "Sales", 95000, "mike@company", 15],  # Invalid email! # 2 row
    ["Lisa", 31, "Engineering", 90000, "lisa@company.com", 6],          # 3 row
    ["David", 26, "Marketing", 60000, "david@company.com", 2],          # 4 row
    ["Emma", 45, "Sales", 110000, "emma@company.com", 20],              # 5 row
    ["Tom", 29, "Engineering", 80000, "tom@company.com", 5],            # 6 row
    ["Anna", 38, "HR", 70000, "anna@company", 12]  # Invalid email!     # 7 row
]

departments = ["Engineering", "Marketing", "Sales", "HR"]

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Phase 1: Data Cleaning & Validation (Email Validator Skills)

# 1 Validate emails (must end with .com)
import copy
val_emails = 0
unval_emails = 0
for name, age, department, salary, email, years_experience in employees:
    if email.endswith('.com'):
        val_emails += 1
        print(f'👍 {name}: {email}') # 2 Flag invalid records
    else:
        unval_emails += 1
        print(f'👎 {name}: {email}')

# 3 Create clean dataset

original_employees = copy.deepcopy(employees)  # original data Backup!
work_data= copy.deepcopy(employees) # Create working copy for cleaning

clean_dataset = []
for emp in work_data:
    if emp[4].endswith('.com'):
        clean_dataset.append(emp)


print(f"Original dataset: {len(original_employees)} records")
print(f"Clean dataset: {len(clean_dataset)} records")   # ONLY valid emails       

#Phase 2: Data Analysis (CSV Processor Skills)

# 4 Average salary per department                                 skipped tell i learn dictionaries
#-----------------------------------------------------------------
# 5 Highest paid employee

Highest_paid_employee = 0
Highest_paid_employee_name = ''

for name, age, department, salary, email, years_experience in clean_dataset:
    if salary > Highest_paid_employee:
        Highest_paid_employee = salary
        Highest_paid_employee_name = name

print(f'Highest paid: {Highest_paid_employee_name} - ${Highest_paid_employee:,}')

# 6 Youngest/Oldest employees

youg_emp = 1000 #Start with huge number
old_emp = 0
youg_emp_name = ''
old_emp_name = ''
for name, age, department, salary, email, years_experience in clean_dataset:
    if age > old_emp:
        old_emp = age
        old_emp_name = name
    if age < youg_emp:
        youg_emp = age
        youg_emp_name = name

print(f'Oldest Employee:{old_emp_name} have {old_emp} years old '
      f'AND the Youngest Employee:{youg_emp_name} have {youg_emp} years old')


# 7 Count employees per department

eng = 0
eng_emp_names = []
marketing = 0
marketing_emp_names = []
sales = 0
sales_emp_names = []
for  name, age, department, salary, email, years_experience in clean_dataset:
    if department == 'Engineering':
        eng += 1
        eng_emp_names.append(name) #ADDS to the list!
    if department == 'Marketing':
        marketing += 1
        marketing_emp_names.append(name)
    if department == 'Sales':
        sales += 1
        sales_emp_names.append(name)

print(f'Number of Engineering employee :{eng}  {eng_emp_names}')
print(f'Number of marketing employee :{marketing} {marketing_emp_names}')
print(f'Number of sales employee :{sales} {sales_emp_names} ')


#Phase 3: Advanced Analysis (New Skills)

# 8 Sort employees by salary (using lambda with sorted())

sorted_emp = sorted(clean_dataset , key=lambda emp :emp[3], reverse=True)

print('Salary Rank:')
for emp in sorted_emp:
    salary = emp[3]
    name = emp[0]
    print(f'{name} - ${salary}')

# 9 Use zip() to pair names with salaries

name_list = []
salaries_list = []
for emp in clean_dataset:
    name_list.append(emp[0])
    salaries_list.append(emp[3])

print('Name : salary')
zipped = list(zip(name_list , salaries_list))
for name , salary in zipped:
    print(f'{name} ${salary}')


# Phase 4: Reporting

# 10 Generate summary report

print("=" * 50)
print('                 summary report')
print("=" * 50)
print()

print("DATA QUALITY")
print('------------')
print(f"• Original records: {len(original_employees)}")
print(f"• Valid records: {len(clean_dataset)}")
print(f"• Invalid emails removed: {len(original_employees) - len(clean_dataset)}")
print()

print("SALARY ANALYSIS")
print('----------------')
print(f'Highest paid: {Highest_paid_employee_name} - ${Highest_paid_employee:,}')
print('Salary Rank:')
for emp in sorted_emp:
    salary = emp[3]
    name = emp[0]
    print(f'{name} - ${salary}')
print()

print('DPEARTMNTS')
print('----------')
print(f'Number of Engineering employee :{eng}  {eng_emp_names}')
print(f'Number of marketing employee :{marketing} {marketing_emp_names}')
print(f'Number of sales employee :{sales} {sales_emp_names} ')
print(f'Oldest Employee:{old_emp_name} have {old_emp} years old '
      f'AND the Youngest Employee:{youg_emp_name} have {youg_emp} years old')
print()

# 11 Find department with highest avg salary

eng_total = 0
mkt_total = 0  
sales_total = 0
for name, age, department, salary, email, years_experience in clean_dataset:
    if department == "Engineering":
        eng_total += salary 
    elif department == "Marketing":
        mkt_total += salary
    elif department == "Sales":
        sales_total += salary

# Calculate averages
eng_avg = eng_total / len(eng_emp_names) if len(eng_emp_names) > 0 else 0 
mkt_avg = mkt_total / len(marketing_emp_names) if len(marketing_emp_names) > 0 else 0  
sales_avg = sales_total / len(sales_emp_names)  if len(sales_emp_names)  > 0 else 0

highest_dept = ""
highest_avg = 0

if eng_avg > highest_avg:
    highest_avg = eng_avg
    highest_dept = "Engineering"
    
if mkt_avg > highest_avg:
    highest_avg = mkt_avg  
    highest_dept = "Marketing"
    
if sales_avg > highest_avg:
    highest_avg = sales_avg
    highest_dept = "Sales"

print(f"DEPARTMENT SALARY ANALYSIS")
print(f"Engineering: ${eng_avg:,.0f} average")
print(f"Marketing: ${mkt_avg:,.0f} average")  
print(f"Sales: ${sales_avg:,.0f} average")
print(f"\nHighest average salary: {highest_dept} (${highest_avg:,.0f})")

# 12 Identify experienced employees (>10 years)

exper_emp_more_than_10_years = 0
exper_emp_name = []
for  name, age, department, salary, email, years_experience in clean_dataset:
    if years_experience > 10:
        exper_emp_more_than_10_years += 1
        exper_emp_name.append(name)

print(f'The Most Experienced employee is :{exper_emp_name} more than 10 years')
