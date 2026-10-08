#INITIAL VARIABLE
airtime = 3500
data_mb = 0
first_time_buyer = True

while True:
    print("\n---welco0me to GLO USSD menu ----")
    print("1.check ballance \n2. buy [1.5GB]*{1000}\n3.buy[5GB]*{2500}\n4. browse tiktok\n.5 exit system")
    choice = input("please select an option(1-5):").strip()

    if choice == "1":
        print(f"\nAirtimebalance:#{airtime}")
        print(f"data balance {data_mb}MB")
    elif choice == "2":
        if airtime >= 1000:
            airtime -= 1000
            data_mb += 1500
            print("\nsuccessfully purchased 1.5GB of data plan from the glo USSD menu")
            if first_time_buyer==True:
                data_mb += 500
                print("\ndata bonus for first time user is 500mb")
                first_time_buyer = False
        else:
            print("\n insufficient airtime balance")
    elif choice == "3":
        if airtime  >= 2500:
            airtime -= 2500
        data_mb  += 500
        print("\nsuccessfully purchased 5GB of data plan on the glo USSD menu ")
        if first_time_buyer == True: 
            data_mb += 500
            print("\ndata bonus for first time user is 500mb")
            first_time_buyer = False
        else:
            print("\ninsufficient airtime balance")
    elif choice =="4":
        if data_mb >= 800:
            data_mb -= 800
            print("\nenjoy your streamings")
        elif airtime >= 500:
            airtime -= 500
            print("\ndata exhausted charge 500 from airtime for browsing. ")
        else:
            print("\n network disconnected please recharge.")
    elif choice == "0":
        print("\nthanks for your patronage ")
        break
    else:
        print('invalid option')
          