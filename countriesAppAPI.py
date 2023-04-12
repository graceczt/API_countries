import requests


base_url = 'https://restcountries.com/v3.1/'


# create a define function to choose option
def choose_option():
    print('What information do you want to search about a country? Choose one.')

    # create dictionary of options
    options = {
        '1': 'Population',
        '2': 'Language',
        '3': 'Timezone',
        '4': 'Currency'
    }
    # display options choices to user
    for key, value in options.items():
        print(key + ': ' + value)
    # user input for option
    option = input('Choose an option: ')
    # check if option is valid
    if option not in options:
        print('Invalid option. Please try again.')
        # return to choose option function
        return choose_option()
    # print the option chosen
    print('You chose option ' + option + ': ' + options[option])
    # prompt user to enter country name
    country = input('Which country do you want that information for? ')
    print(country.capitalize())
    # check if country is valid
    response = requests.get(base_url + 'name/' + country)
    if response.status_code == 404:
        print('Invalid country. Please try again.')
        # return to choose option function
        return choose_option()
    # return the option and country chosen
    return option, country

def proceed_option():
    while True:
        option, country = choose_option()
        if option == '1':
             get_population(country)
        if option == '2':
             get_language(country)
        if option == '3':
             get_timezone(country)
        if option == '4':
             get_currency(country)
        else:
             break

def get_population(country):
    response = requests.get(base_url + 'name/' + country)
    json_result = response.json()
    for pop in json_result:
    
        number = str(round((pop['population']/1000000), 3)) + " million"
        print(f"The population of {pop['name']['common']} is {number}.")

        


def get_language(country):
    # get the languages of the country using for loop
    response = requests.get(base_url + 'name/' + country)
    json_result = response.json()
    for countryData in json_result:
        languages = countryData['languages'].values()
        print(f"The language/s of {countryData['name']['common']} is/are {', '.join(languages)}.")
            
    

def get_timezone(country):
    response = requests.get(base_url + 'name/' + country)
    json_result = response.json()
    # get the timezone of the country using for loop
    for countryData in json_result:
        timezone = countryData['timezones']
        print(f"The timezone/s of {countryData['name']['common']} is/are {timezone}.")

def get_currency(country):
    response = requests.get(base_url + 'name/' + country)
    json_result = response.json()
     # get the currency of the country using for loop
    for countryData in json_result:
        currency = countryData['currencies'].values()
        # extract only values of name and symbol
        for value in currency:
            currency = value['name'] + ' (' + value['symbol'] + ')'
        print(f"The currency of {countryData['name']['common']} is {currency}.")

    
proceed_option()

















