#guessing game
secret_number=int(input('Enter the secret number:'))
guess_count=0
guess_limit=3
while guess_count<guess_limit:
 guess=int(input('guess the secret number:'))
 if guess==secret_number:
  print('You won')
  break
 elif guess_count!=guess_limit-1:
  print('sorry try again')
 guess_count+=1
else:
  print('You loss the game')