Lays = 10
Doritos = 10
Snicker = 20
CocaCola = 10


price_lays = 30
price_doritos = 30
price_snickers = 10
price_CocaCola = 15


def user_choice():

    game = input("cost of: Lays: $30   Doritos: $30   snickers: $10   CocaCola: $15\nType OK to Proceed :").lower()

    print("contents in the machine: 10 Lays  10 doritos  20 Snickers  10 CocaCola's")

    while game == "ok":
        user_input = input(f"what would you like to have? \n input: 1 for Lays, 2 for Doritos, 3 for Snickers, 4 for CocaCola , 5 to exit: ")
        if user_input == "1":
            number_of_lays = int(input("how many lays do you want? "))
            price = number_of_lays * price_lays
            print(f"that would be ${price}")
            global Lays
            Lays -= number_of_lays

        elif user_input == "2":
            number_of_doritos = int(input("how many doritos do you want? "))
            price = number_of_doritos * price_doritos
            print(f"that would be ${price}")
            global Doritos
            Doritos -= number_of_doritos

        elif user_input == "3":
            number_of_snickers = int(input("how many snickers do you want? "))
            price = number_of_snickers * price_snickers
            print(f"that would be ${price}")
            global Snicker
            Snicker -= number_of_snickers

        elif user_input == "4":
            number_of_cocacola = int(input("how many cans do you want? "))
            price = number_of_cocacola * price_CocaCola
            print(f"that would be ${price}")
            global CocaCola
            CocaCola -= number_of_cocacola

        elif user_input == "5":
            game = False




user_choice()
print(f"the contents in machine are: \n {Lays} lays \n {Doritos} Doritos\n {Snicker} snickers\n {CocaCola} CocaCola's. ")