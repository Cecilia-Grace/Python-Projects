currencies = ('KSH', 'AUD')

exchange_rates = {
        'AUD': {'KSH': 86.41},
        'KSH': {'AUD': 0.012}
    }

while True:
    try:
        user_input = input("Enter the amount(or q to quit): ")
        if user_input.lower() == 'q':
            break

        amount = float(user_input)
        
        amount_currency = input("Enter the amount currency(KSH/AUD): ").upper()
        target_currency = input("Enter the target currency(KSH/AUD): ").upper()
        
        if amount_currency not in currencies and target_currency not in currencies:
            print("Invalid currencies")
        
        if amount_currency == target_currency:
            print(amount)
            
    except(ValueError, TypeError):
        print("Enter correct inputs")

    result = amount*exchange_rates[amount_currency][target_currency]

    print(f"{amount}{amount_currency} is {result}{target_currency}")

        
    