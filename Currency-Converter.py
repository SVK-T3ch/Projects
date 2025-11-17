# M A D E  B Y  SVK-T3CH
print('Welcome to the Currency Converter!')
print('This program converts commonly known currencies.More Currencies Coming Soon!(eg- USD -> INR)')
rates = {
    "USD": 1.00,      # US Dollar
    "EUR": 0.92,      # Euro
    "GBP": 0.79,      # British Pound
    "JPY": 151.6,     # Japanese Yen
    "CAD": 1.38,      # Canadian Dollar
    "CHF": 0.90,      # Swiss Franc
    "CNY": 7.23,      # Chinese Yuan
    "AUD": 1.52,      # Australian Dollar
    "INR": 84.0,      # Indian Rupee
    "SGD": 1.36       # Singapore Dollar
}
while True:
 FromCurrency = input("Enter the currency to convert from [USD/EUR/GBP/JPY/CAD/CHF/CNY/AUD/INR/SGD]: ").upper()
 while FromCurrency not in rates:
    FromCurrency = input("Please try again,Enter the Currency To Convert From [USD/EUR/GBP/JPY/CAD/CHF/CNY/AUD/INR/SGD]: ").upper()
 ToCurrency = input("Enter the currency to convert to [USD/EUR/GBP/JPY/CAD/CHF/CNY/AUD/ISR/SGD]: ").upper()
 while ToCurrency not in rates:
    ToCurrency = input("Please try again,Enter the currency to convert to [USD/EUR/GBP/JPY/CAD/CHF/CNY/AUD/INR/SGD]: ").upper()
 Amount = float(input('Enter the Amount: '))
 while Amount <= 0:
    print('Please enter a valid input.')
    Amount = float(input('Enter the Amount: '))
 CurrencyUSD = Amount / rates[FromCurrency]
 CurrencyConverted = round(CurrencyUSD * rates[ToCurrency],2)
 print(f'Your converted currency is : {CurrencyConverted} {ToCurrency}.')
 while True:
  q = input('Would you like to try again? [Y/n]: ').lower()
  if q == 'n':
    print('Thank you for using this program!')
    exit()
  elif q == 'y':
    break
  else:
    print('Please enter either y or n.')