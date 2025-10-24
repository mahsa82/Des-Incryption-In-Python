from Crypto.Cipher import DES
import binascii

# Static key 
key = b'8bytekey'

# Memory for the last text which was encoding
last_encrypted = None

def encrypt(msg):
    global last_encrypted
    msg_bytes = msg.encode('utf-8')
    cipher = DES.new(key, DES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg_bytes)
    data = nonce + tag + ciphertext
    last_encrypted = data
    # print(f"DEBUG: nonce={nonce.hex()}, tag={tag.hex()}, ciphertext={ciphertext.hex()}")
    return data.hex()

def decrypt(encrypted_hex):
    encrypted_bytes = binascii.unhexlify(encrypted_hex)
    nonce_len = 16 
    nonce = encrypted_bytes[:nonce_len]
    tag = encrypted_bytes[nonce_len:nonce_len+8]
    ciphertext = encrypted_bytes[nonce_len+8:]
    # print(f"DEBUG: nonce={nonce.hex()}, tag={tag.hex()}, ciphertext={ciphertext.hex()}")
    cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
    decrypted_bytes = cipher.decrypt_and_verify(ciphertext, tag)
    return decrypted_bytes.decode('utf-8')

# Main program
while True:
    choice = input("If you want to encode/decode print (e/d) or exit with (q):\n").lower()

    if choice == 'e':
        text = input("Enter your message: ")
        encrypted = encrypt(text)
        print("\nEncoded text:")
        print(encrypted)

    elif choice == 'd':
        hex_input = input("Enter the hex string to decode (or press Enter to use last encrypted):\n")
        if hex_input.strip() == "":
            if last_encrypted is None:
                print("No message has been encrypted yet.")
            else:
                decrypted = decrypt(last_encrypted.hex())
                print("\nYou message is:")
                print(decrypted)
        else:
            decrypted = decrypt(hex_input)
            print("\nYour message is:")
            print(decrypted)

    elif choice == 'q':
        print("Exiting! Goodbye.")
        break

    else:
        print("Please enter one of (e/d/q):")
