alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def coding(option):
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))%26
  if option==-1:
    shift=26-shift
  new = []
  for i in text:
    if option==1:
      new.append(alphabet[alphabet.index(i)+(shift)])
    else:
      new.append(alphabet[alphabet.index(i)+(shift)])
  return "".join(new)

print("""
   ____                              ____ _       _               
  / ___|__ _  ___  ___  __ _ _ __   / ___(_)_ __ | |__   ___ _ __ 
 | |   / _` |/ _ \/ __|/ _` | '__| | |   | | '_ \| '_ \ / _ \ '__|
 | |__| (_| |  __/\__ \ (_| | |    | |___| | |_) | | | |  __/ |   
  \____\__,_|\___||___/\__,_|_|     \____|_| .__/|_| |_|\___|_|   
                                           |_|                    
""")

option = int(input("""Press 1 to Encode.
Press 2 to decode.\n"""))

if option==1:
  print(f"Encrypted message: {coding(1)}")

if option==2:
  print(f"Decrypted message: {coding(-1)}")

