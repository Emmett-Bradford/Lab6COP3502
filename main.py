def encode(to_encode):
  string = ''
  for i in range(len(to_encode)):
    string += str((int(to_encode[i])+3)%10)
  return string

def decode(to_decode):
  string = ''
  for i in range(len(to_decode)):
    string += str((int(to_decode[i])-3)%10)
  return string

if __name__ == '__main__':
  passw = None
  dpassw = None
  while True:
    modenum = input('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: ')
    if modenum == '1':
      passw = encode(input("Please enter your password to encode: "))
      print("Your password has been encoded and stored!\n")
    elif modenum == '2':
      try:
        dpassw = decode(passw)
        print(f"The encoded password is {passw}, and the original password is {dpassw}")
      except:
        print("You need to encode a password first!")
    elif modenum == '3':
      break