#                       **CHECK PRIMALITY...**


while True:
    try:
        user = int(input("INPUT A NUMBER FOR PRIMALITY CHECK... "))

        if user < 2:
            print(f"{user} is not a prime number")
        elif user == 2:
            print("2 is a prime number")
        elif user > 1:
            for i in range(2, user):
                if (user % i) == 0:
                    print(f"{user} is not a prime number")
                    break
                else:
                    print(f"{user} is a prime number")
    except ValueError as e:
        print(e)
        print("Please input an integer greater than 1...")
    except Exception as e:
        print(e)
        print("Something went wrong. :( ")

