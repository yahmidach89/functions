#Bonus : Mini casse tête (3 points bonus)
def decrypt(message: [int]) -> str:
    return ''.join(chr(i) for i in message)

message = [84, 104, 105, 115, 32, 101, 120, 101, 114, 99, 105, 99,
           101, 32, 105, 115, 32, 97, 119, 101, 115, 111, 109,
           101, 32, 33]

decrypted_message = decrypt(message)
print(decrypted_message)

