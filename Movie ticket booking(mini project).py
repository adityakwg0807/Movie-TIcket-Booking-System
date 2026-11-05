
print("...... MOVIE TICKET BOOKING SYSTEM ......")

print("\nAvailable Movies:")
print("1. Avengers:Doomsday - Rs. 450")
print("2. Ramayana: Rise of a Legend - Rs. 500")
print("3. The Cat in the Hat - Rs. 300")
print("4. Delhi-6 - Rs. 250")

movie_choice = int(input("\nSelect a movie (1-4): "))

if movie_choice == 1:
    movie = "Avengers:Doomsday"
    price = 450

elif movie_choice == 2:
    movie = "Ramayana: Rise of a Legend"
    price = 500

elif movie_choice == 3:
    movie = "The Cat in the Hat"
    price = 300

elif movie_choice == 4:
    movie = "Delhi-6"
    price = 250

else:
    print("Invalid movie selection!")
    exit()

print("\nSelect Seat Category:")
print("1. Normal - Rs. 0 extra")
print("2. Silver - Rs. 50 extra")
print("3. Gold - Rs. 100 extra")
print("4. Platinum - Rs. 150 extra")

seat = int(input("\nChoose your seat (1-4): "))

if seat == 1:
    category = "Normal"
    extra = 0

elif seat == 2:
    category = "Silver"
    extra = 50

elif seat == 3:
    category = "Gold"
    extra = 100

elif seat == 4:
    category = "Platinum"
    extra = 150

else:
    print("Invalid seat selection!")
    exit()

tickets = int(input("\nEnter number of tickets: "))

if tickets <= 0:
    print("Invalid ticket quantity!")

else:
    total = (price + extra) * tickets

    print("\n===== BOOKING CONFIRMED =====")
    print("Movie Name:", movie)
    print("Seat Category:", category)
    print("Ticket Price: Rs.", price)
    print("Extra Seat Charge: Rs.", extra)
    print("Number of Tickets:", tickets)
    print("Total Amount: Rs.", total)
    print("=============================")
    print("Thank you for booking!")
