from func.Enc import ENC
from func.GEN import Gen

path = "./key"
Gen = Gen(path)
gen = Gen.Gen_pub()
if gen:
    print("[+] DONE")
else:
    print(gen)

