#The income labour tax for individuals (IRPF) is a progressive tax that works by different sections. In other words, it is increased as the income is. To calculate the amount that a worker must pay to the official tax office from their incomes, a different percentage is applied to each section. Specifically, the tax intervals in Spain are as follows:

#Less than €12450: 19%
#From €12450 to €20200: 24%
#From €20200 to €35000: 30%
#From €35000 to €60000: 37%
#From €60000 to €300000: 45%
#More than €300000: 47%

#Write a program that asks the user for an annual income and displays on the screen:
#a) The corresponding tax rate for that income
#b) The amount to be paid in taxes
#c) The net amount received

#It should be noted that the above tax rates are applied section by section. For instance, a person with a yearly salary of 30000 euros will have to pay:
#· 19% of the first 12450 euros
#· 24% of the amount between 12450 and 20200 euros
#· 30% of the amount between 20200 and 30000 euros

#Expected output: a) 30% section (from 20200 to 35000) b) 7165.5 euros c) 22834.5 euros

incomes = input('Please enter your incomes: ')
incomes = float(incomes)

THRESHOLD_VERY_LOW = 12450
THRESHOLD_LOW = 20200
THRESHOLD_MEDIUM = 35000
THRESHOLD_HIGH = 60000
THRESHOLD_VERY_HIGH = 300000

PERCENT_MINIMUM = 0.19
PERCENT_LOW = 0.24
PERCENT_MEDIUM = 0.3
PERCENT_HIGH = 0.37
PERCENT_VERY_HIGH = 0.45
PERCENT_MAXIMUM = 0.47

if incomes <= THRESHOLD_VERY_LOW:
    taxes = incomes * PERCENT_MINIMUM
else:
    taxes = THRESHOLD_VERY_LOW * PERCENT_MINIMUM
    if incomes <= THRESHOLD_LOW:
        taxes += (incomes - THRESHOLD_VERY_LOW) * PERCENT_LOW
    else:
        taxes += (THRESHOLD_LOW - THRESHOLD_VERY_LOW) * PERCENT_LOW
        if incomes <= THRESHOLD_MEDIUM:
            taxes += (incomes - THRESHOLD_LOW) * PERCENT_MEDIUM
        else:
            taxes += (THRESHOLD_MEDIUM - THRESHOLD_LOW) * PERCENT_MEDIUM
            if incomes <= THRESHOLD_HIGH:
                taxes += (incomes - THRESHOLD_MEDIUM) * PERCENT_HIGH
            else:
                taxes += (THRESHOLD_HIGH - THRESHOLD_MEDIUM) * PERCENT_HIGH
                if incomes <= THRESHOLD_VERY_HIGH:
                    taxes += (incomes - THRESHOLD_HIGH) * PERCENT_VERY_HIGH
                else:
                    taxes += (THRESHOLD_VERY_HIGH - THRESHOLD_HIGH) * PERCENT_VERY_HIGH
                    taxes += (incomes - THRESHOLD_VERY_HIGH) * PERCENT_MAXIMUM
net_incomes = incomes - taxes
print('Your total amount of taxes is: ', taxes)
print('Your net incomes are: ', net_incomes)