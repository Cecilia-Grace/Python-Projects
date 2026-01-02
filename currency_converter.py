amount = float(input("Enter the amount: "))
amount_currency = input("Currency of your amount(AUD, KSH): ").lower()
target_currency = input("Target currency(AUD, KSH): ").lower()

if amount_currency == "aud" and target_currency == "ksh":
    to_ksh = amount * 86.41
    print(f"{amount}{amount_currency.upper()} is equal to {to_ksh}{target_currency.upper()}")
elif amount_currency == "ksh" and target_currency == "aud":
    to_aud = amount * 0.012
    print(f"{amount}{amount_currency.upper()} is equal to {to_aud}{target_currency.upper()}")
else:
    print("Fill with correct inputs")
