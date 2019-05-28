import json
import sys
import requests
print("\nWelcome to Foreign exchange rates\n")

#function to print instructions for user
def print_instructions():
    print("This program displays foreign exchange rates for given base currency ")
    print("    To get help:")
    print("         python crypt.py -h")
    print("    To create a key file:")
    print("         python crypt.py -c Currency code")
    print(" \nPlesae use below valid arguments for this program: ")
    print(" BGN: Bulgarian Lev\n",
          "NZD: New Zealand Dollar\n",
          "ILS: Israeli New Shekel\n",
          "RUB: Russian Ruble\n",
          "CAD: Canadian Dollar\n",
          "USD: US Dollar\n",
          "PHP: Philippine Piso\n",
          "CHF: Swiss Franc\n",
          "ZAR: South African Rand\n",
          "AUD: Australian Dollar\n",
          "JPY: Japanese yen\n",
          "TRY: Turkish lira\n",
          "HKD: Hong Kong Dollar\n",
          "MYR: Malaysian Ringgit\n",
          "THB: Thai Baht\n",
          "HRK: Croatian Kuna\n",
          "NOK: Norwegian Krone\n",
          "IDR: Indonesian Rupiah\n",
          "DKK: Danish Krone\n",
          "CZK: Czech Koruna\n",
          "HUF: Hungarian Forint\n",
          "GBP: Pound sterling\n",
          "MXN: Mexican Peso\n",
          "KRW: South Korean won\n",
          "ISK: Icelandic Króna\n",
          "SGD: Singapore Dollar\n",
          "BRL: Brazilian Real\n",
          "PLN: Poland złoty\n",
          "INR: Indian Rupee\n",
          "RON: Romanian Leu\n",
          "CNY:  Chinese Yuan\n",
          "SEK: Swedish Krona\n")

def print_error():
    print("\nERROR: Invalid command line arguments!\n")

#main
if len(sys.argv) == 2 and sys.argv[1] == '-h':
    print_instructions()

elif len(sys.argv) == 3 and sys.argv[1] == '-c':

#api call
     f = requests.get("https://api.exchangeratesapi.io/latest?base="+sys.argv[2].upper())
     json_string = f.text
     parsed_json = json.loads(json_string)
     
     if len(json_string) < 1:
         
         print("The API is currently unavailable. Please try again in a few minutes. ")
     
     else:
          
         parsed_json = json.loads(json_string)

#using try to validate the arguments and print instruction when needed   
         try:
             
             list1 = parsed_json['rates']
             list2 = parsed_json['base']
             print("Below are the exchage rates for the base currency:",list2)
             print("\nCurrency\tRate")
             for i in list1:
                 print("{}\t\t{:.2f}".format(i, list1[i]))

         except:
             print_error()
             print_instructions()
           
else:
    print_error()
    print_instructions()
