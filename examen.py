import os

products = {}

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('welcome to clothing stores MATYW')
    print("\nMenú:")
    print("1. get into")
    print("2. see products")
    print("3. exit")

    option = int(input("choose option-> "))
    if option == 1:
 
        os.system('cls' if os.name == 'nt' else 'clear')
        product_name = input("enter product name-> ")
        product_price = float(input("producte price-> "))
        product_quantity = int(input("amount-> "))
        products[product_name] = {"price": product_price, "quantity": product_quantity}

    elif option == 2:
        print(products)
       
        os.system('cls' if os.name == 'nt' else 'clear')
   
    elif option == 3:
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Opción inválida. Por favor, elija una opción del menú.")

print("thanks for using clothing stores MATYW.")
