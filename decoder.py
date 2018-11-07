#!/usr/bin/env python
#Author : Ahmad Mahfouz
import sys
from binascii import unhexlify,hexlify,b2a_hex

chunk_size = 100000000 #100MB

key =  raw_input("[+] random byte selected  [ ?? ] ")


filename = raw_input("[+] Orignal file name? ")

number_of_chunks = raw_input("[+] Number of chunks? ")


print "[+] Reconstructing the files in the memory"

payload = ''
for x in range(1 , int(number_of_chunks)+1):
        target_file_name = filename + "." + str(x) + ".txt"
        tmp = open(target_file_name,'rb')
        payload += tmp.read()
        tmp.close()

print "[+] building array of %s bytes"  %len(payload)
decoded = bytearray(payload)

i=0
for b in decoded:            
        nbyte = b ^ ord(unhexlify(key))
        decoded[i] = nbyte
        i+=1
        sys.stdout.write("[+] %s byte XORed with byte 0x%s\r" %(i,key) )
        sys.stdout.flush()
        if i == 2000000:
                break


print "[+] rewriting original status for %s" %filename
obj = open(filename,'wb')
obj.write(decoded)
obj.close()


               