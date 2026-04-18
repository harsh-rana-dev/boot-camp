bot_name: str = "bob"
print(f"hii im {bot_name}")

while True:
    user_input: str = input("you: "). lower()

    if user_input in ['hii', 'hello']:
        print("hello, user")

    elif user_input in ['by', 'thek hai']:
        print("ok")

    elif user_input in ["+", "add"]:

        print("provide numbers")
        try:
            num1: float = float(input(':'))
            num2: float = float(input(":"))
            print(num1 + num2)
        except ValueError as e:
            print('put a number')

    else:
        print("fu")


