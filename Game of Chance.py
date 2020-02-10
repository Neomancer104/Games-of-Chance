import random

money = 100


#CoinFlip Game
def coin_flip(call, bet):
  coin = random.randint(1, 2)
  
  #RULES
  if bet > money:
    print("You dont have enough money to make that bet!")
    return
  elif bet <= -1:
    print("Bet must be positive!")
    return
  
  #Coin lands on Heads!

  elif coin == 1 and call == "Heads!":
    print ("Heads! $" + str(bet))
    return bet
  
  elif coin == 1 and call == "Tails!":
    print ("Heads! $" + str(bet-(bet*2)))
    return -bet
  #Coin lands on Tails!
  
  elif coin == 2 and call == "Tails!":
    print ("Tails! $" + str(bet))
    return bet
  
  elif coin == 2 and call == "Heads!":
    print ("Tails! $" + str(bet-(bet*2)))
    return -bet
  
#Cho_han Game
def cho_han(call, bet):
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  dice_roll=dice1+dice2
  
  #RULES
  if bet > money:
    print("You dont have enough money to make that bet!")
    return
  elif bet <= -1:
    print("Bet must be positive!")
    return
 
  #Dice roll
  elif dice_roll % 2 == 0 and call == "Even!":
    print ("Even! $" + str(bet))
    return bet
  elif dice_roll % 2 == 0 and call == "Odd!":
    print ("Even! $" + str(bet-(bet*2)))
    return -bet
  elif dice_roll % 2 > 0 and call == "Odd!":
    print ("Odd! $" + str(bet))
    return bet
  elif dice_roll % 2 > 0 and call == "Even!":
    print ("Odd! $" + str(bet-(bet*2)))
    return -bet
  
#Card_draw Game
def card_draw(bet):
  card_p1 = random.randint(1, 13)
  card_p2 = random.randint(1, 13)
  
  #RULES
  if bet > money:
    print("You dont have enough money to make that bet!")
    return
  elif bet <= -1:
    print("Bet must be positive!")
    return
 
  elif card_p1 > card_p2:
    print ("Player 1 wins $" + str(bet))
    return bet
  elif card_p2 > card_p1:
    print ("Player 1 lost $" + str(bet-(bet*2)))
    return -bet
  elif card_p1 == card_p2:
    print ("Tie $" + str(0))
    return 0

#Roulette Game
#    Impair (Odd) und Pair (Even), 1:2
#    Manque (Low, 1–18) und Passe (High, 19–35), 1:2
#    Number (specific Number), 1:35

def roulette(call, bet):
  number = random.randint(0, 36)
  
  #RULES
  if bet > money:
    print("You dont have enough money to make that bet!")
    return
  elif bet <= -1:
    print("Bet must be positive!")
    return
 
  elif (call == 0 or call == 36):
    print ("Roulette: Specific Number must be between 1 and 35!")
    return money-money
  
  #specific number
  elif number == call:
    print (str(number) + ", Player wins! $" + str(bet*35))
    return (bet*35)
  
  #0, 00
  elif number == 0:
    print ("0, Player lost! $" + str(bet-(bet*2)))
    return -bet
  elif number == 36:
    print ("00, Player lost! $" + str(bet-(bet*2)))
    return -bet
  
  #low/high
  elif (number >= 1 and number <= 18) and call == "Low!":
    print ("Low, Player wins! $" + str(bet))
    return bet
  elif (number >= 1 and number <= 18) and call == "High!":
    print ("Low, Player lost! $" + str(bet-(bet*2)))
    return -bet
  elif (number >= 19 and number <= 35) and call == "Low!":
    print ("High, Player lost! $" + str(bet-(bet*2)))
    return -bet
  elif (number >= 19 and number <= 35) and call == "High!":
    print ("High, Player wins! $" + str(bet))
    return bet
  
  #odd/even
  elif call == "Even!" and number % 2 == 0:
    print ("Even, Player wins! $" + str(bet))
    return bet
  elif call == "Even!" and number % 2 != 0:
    print ("Odd, Player lost! $" + str(bet-(bet*2)))
    return -bet
  elif call == "Odd!" and number % 2 == 0:
    print ("Even, Player lost! $" + str(bet-(bet*2)))
    return -bet
  elif call == "Odd!" and number % 2 != 0:
    print ("Odd, Player wins! $" + str(bet))
    return bet
  
  #not specific number
  else:
    print ("Player lost! $" + str(bet-(bet*2)))
    return -bet
  


print("GameTestsStart")
#Call CoinFlipGame
print("CoinFlip:")
print(coin_flip("Tails!", 10))

#Call Cho-han Game
print("Cho-han:")
print(cho_han("Odd!", 10))

#Call Card_draw Game
print("Card_draw:")
print(card_draw(10))

#Call Roulette
print("Roulette:")
print(roulette(0,10))

print("GameTestsEnd")
print(" ")


#Play roulette, cho_han, coin_flip or card_draw!

#roulette(call,bet)   cho_han(call,bet)   coin_flip(call,bet)   card_draw(bet)

#CoinFlip call needs to be either "Heads!" or "Tails!"

#Cho-han call needs to be either "Odd!" or "Even!"

#Roulette call needs to be either "Odd!", "Even!", "High!", "Low!" or a specific Number between 1 and 35!

try:
  
  money += roulette("High!",10)
  money += cho_han("Even!",10)
  money += coin_flip("Heads!",10)
  money += card_draw(10)
  
except:
  print("Follow the Rules!")
  
print(str(money) + "$ left!")












