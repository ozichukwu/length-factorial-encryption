"""
Length Factorial Encryption

For how to use, see below the code
--------------------------------------

"abcde12345" with key "px[9-6-1-2-7-5-8-4-10-3]". 


NOTES
-------
*Encryption key in the format px[a-b-c-d-ef-g...]
	meaning "message is padded with x chars at the end and then encrypted with 'a-b-c-d-ef-g...'"

*Higher length of message, l_m = higher encryption. 

Chosen length of message, cl_m
cl_m >= l_m

if cl_m > l_m, then l_m is padded, at its end, with x random chars

2. encrypted message = em. length of em = cl_m.


ENCRYPTION PROCESS
-------------------
"abcde12345" with key "px[9-6-1-2-7-5-8-4-10-3]"
*message is first padded with x random chars
*letters interchange position with the key i.e "a" goes to 9th pos, "b" goes to 6th ...and so on to em

DECRYPTION PROCESS
--------------------
Key "px[9-6-1-2-7-5-8-4-10-3]"
Assuming em = "54321edcba";
*key interchange position with the letters i.e 9th pos ("b") becomes 1st, 6th ("e") becomes 2nd ...and so on to
	get the message with paddings
*last x chars are removed to get the message
"""

import random
import string

class LFE:
    def __init__(self, msg, paddings, key=None):
        self.msg = msg
        self.paddings = paddings
        self.key = key
        
    def encrypt_msg(self):
        if self.key == None:
            self.key = self.create_key()

        padded_msg = self.pad_msg()
        key_list = self.get_keys_list()
        encrypted_msg_list = [""] * len(padded_msg)
        letter_pos_to_move = 0
        
        for x in key_list:
            encrypted_msg_list[x-1] = padded_msg[letter_pos_to_move]
            letter_pos_to_move += 1
            
        return "".join(encrypted_msg_list)

    def decrypt_msg(self, encrypted_msg):
        key_list = self.get_keys_list()
        encrypted_msg_list = list(encrypted_msg)
        msg_list = [""] * len(encrypted_msg)
        letter_pos_to_place = 0

        for x in key_list:
            msg_list[letter_pos_to_place] = encrypted_msg_list[x-1]
            letter_pos_to_place += 1
        
        return "".join(msg_list)[:len(encrypted_msg) - self.paddings]

    def create_key(self):
        keys_list = list(range(1, len(self.msg)+ self.paddings + 1))
        keys = []
        while keys_list != []:
            keys.append(keys_list.pop(random.randint(0, len(keys_list)-1)))

        return "p" + str(self.paddings) + "[" +\
               ("-".join(list(map(lambda x: str(x), keys)))) + "]"
        
    def pad_msg(self):
        if self.paddings == 0:
            return self.msg
        
        #english letters(lowercase & uppercase) and all digits (0-9)
        all_chars = string.ascii_letters + string.digits
        pads = ""
        for x in range(self.paddings):
            pads += all_chars[random.randint(0, len(all_chars)-1)]

        return self.msg + pads

    def get_keys_list(self):
        #just breaking through the format of the key to get the needed
        #key values
        return list(map(int, self.key[1:].split("[")[1][:-1].split("-")))





"""
FINDINGS
---------
*1 key can be used to make variations of encryption of a particular message
so that all of them decrypts to the same original message

*Higher length of encrypted message (incl. padding) = higher encryption
"""

"""
HOW TO USE
------------
Code runs on Python 3.7

TO ENCRYPT;
------------
* object = LFE(message_to_encrypt, paddings_of_choice)
* object.encrypt_msg() => to get the encrypted message
* object.key => to get the encryption key
*
    SAVE ENCRYPTED MESSAGE AND KEY PROPERLY
    DON'T ADD EVEN A SINGLE CHARACTER WHEN SAVING, EVEN A SINGLE SPACE
    DON'T FORGET TO GET/SAVE THE ENCRYPTION KEY ALSO

TO DECRYPT;
------------
* object = LFE("", paddings_from_the_key, key)
    MESSAGE_TO_ENCRYPT IS NOT NEEDED HERE
    
* object.decrypt_msg(message_to_decrypt) => to get the original message from
    the encrypted message
"""





                    
