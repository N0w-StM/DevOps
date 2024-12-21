@zinder
from base64 import b64encode,b64decode
import os
class Enc:
    def __init__(self,path):
        self.path = path
    def enct(self):
        if os.path.isfile(self.path):
            enc_data = open(self.path,'r').read()
            print(f"{self.path} must be a file")
        else:
            print(f"{self.path} must be a file")
            return
        enc_data = b64encode(enc_data.encode('ascii'))
        with open(self.path,'wb') as f:
            f.write(enc_data)
            f.close()
        return "ENC DONE"
    def dec(self):
            if os.path.isfile(self.path):
                dec_data = open(path,'r').read()
            else:
                print(f"{self.path} must be a file")
                return
        dec_data = b64decode(self.path.encode('ascii'))
        with open(self.path,'wb') as f:
            f.write(dec_data)
            f.close()
        return "DEC DONE"
