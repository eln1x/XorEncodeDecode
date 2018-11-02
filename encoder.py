#!/usr/bin/env python
#Author : Ahmad Mahfouz

import sys
import binascii,os
from binascii import unhexlify,hexlify,b2a_hex
chunk_size = 100000000 #100MB

try:
	filename = sys.argv[1]
except:
	print "[-] misisng a filename to encode and split"
	sys.exit(1) 
key =  b2a_hex(os.urandom(1))
print "[+] random byte selection [ %s ]"  %key
print "[+] reading %s"  %filename
data = open(filename,'rb')
print "[+] building array of %s"  %filename
encoded = bytearray(data.read())
i=0
for b in encoded:             
        nbyte = b ^ ord(unhexlify(key))
        encoded[i] = nbyte
        i+=1
        sys.stdout.write("[+] %s byte XORed with byte 0x%s\r" %(i,key) )
        sys.stdout.flush()
        if i == 2000000:
                break


filewrite = filename 
z = 1
for i in range(0, len(encoded), chunk_size):
                chunk = encoded[i:i+chunk_size]
                outfile = filewrite + "." + str(z) + ".txt"
                print "[+] writing chuck size %s on file %s" %(i, outfile)
                obj = open(outfile,'wb')
                obj.write(chunk)
                obj.close()
                z+=1
