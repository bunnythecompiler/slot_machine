from random import choice, random
import random
boss_amount = 47000
a= 1
b = 5
bank = 0
refund = 0

def win_loss_algo(amount):
    global bank
    global refund
    #amount = float(input("enter cash [2-10]"))
    win = ['won','lost']
    t = random.choice(win)
    random_odd = random.uniform(a,b)
    print("this is the random odd before if: ",random_odd)
    wit = amount * random_odd
    if t == "won":
        print("money in the bank before anything else is ",bank)
        if wit > bank:
            print("the prize is more than we can afford , sorry again, loading loop")
            refund += amount
            print("the bank currently has ",round(bank,2))
            print(" you will be refunded ",refund)
        else:
            print("you won")
            bank -= wit
            print("you have rceived cash",round(wit,2))
            print("money in the bank after winning",round(bank,2))
    else:
        print("you have lost it all")
        bank += amount



while True:
    amount = float(input("enter cash [2-10]"))
    win_loss_algo(amount)