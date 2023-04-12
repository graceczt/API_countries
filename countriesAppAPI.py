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
        # if option == '4':
        #     get_currency(country)
        else:
             break

def get_population(country):
    response = requests.get(base_url + 'name/' + country)
    json_result = response.json()
    print(f"The population of {country.capitalize()} is {json_result[0]['population']}.")


def get_language(country):
    # using for loop to get all languages
    response = requests.get(base_url + 'name/' + country)
    json_result = response.json()
    print(f"The language/s of {country.capitalize()} is/are {json_result[1]['languages']}.")
    

def get_timezone(country):
    response = requests.get(base_url + 'name/' + country)
    json_result = response.json()
    print(f"The timezone/s of {country.capitalize()} is/are {json_result[0]['timezones']}.")  

def get_currency(country):
    response = requests.get(base_url + 'name/' + country)
    json_result = response.json()
    print(f"The currency of {country.capitalize()} is {json_result[0]['currencies']}.")
    

proceed_option()

















