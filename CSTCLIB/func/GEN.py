from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import base64
class Gen:
    def __init__(self,path):
        self.path = path
        self.key = RSA.generate(2048)
    def Gen_pub(self):
        pub_key=self.key.publickey().exportKey()
        try:
            f = open(self.path+"_pub.pem","w")
            f.write(pub_key.decode('ascii'))
            f.close()
            return True
        except Exception as e:
            return e
    def Gen_prv(self):
        prv_key=self.key.exportKey()
        try:
            fi = open(self.path+"_prv.pem","w")
            fi.write(prv_key.decode('ascii'))
            fi.close()
            return True
        except Exception as e:
            return e
