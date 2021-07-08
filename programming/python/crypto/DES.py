from Crypto.Cipher import DES3
from Crypto.Hash import SHA256 as SHA

class myDES():
    def __init__(self, keytext, ivtext):
        hash = SHA.new()
        hash.update(keytext.encode('utf-8')) # 해시 생성
        key = hash.digest() # 해시 값 변수에 할당
        self.key = key[:24] # 24바이트 슬라이싱 해 3DES 키로 사용

        hash.update(ivtext.encode('utf-8')) # 해시 생성
        iv = hash.digest() # 해시값을 변수에 담는다.
        self.iv = iv[:8] # 초기화 벡터 생성

    def enc(self, plaintext):
        plaintext = make8string(plaintext)
        des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv) # 키, 운영모드, 초기화 벡터 / 3DES 객체 생성
        encmsg = des3.encrypt(plaintext.encode()) # 암호화 , ECB,CTR 모드는 초기화 벡터가 필요없다.
        return encmsg
    
    def dec(self, ciphertext):
        des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv) 
        decmsg = des3.decrypt(ciphertext) # 복호화
        return decmsg

def make8string(msg): 
    msglen = len(msg)
    filler = ''
    if msglen % 8 != 0:
        filler = '0'*(8 - msglen%8)
    msg += filler
    return msg



def main():
    keytext = 'samsjang'
    ivtext = '1234'
    msg = 'python3xab' # python3x >> 암호화 메시지 길이는 8바이트 배수여야 한다. 따라서 수정필요

    myCipher = myDES(keytext, ivtext)
    ciphered = myCipher.enc(msg)
    deciphered = myCipher.dec(ciphered)
    print(f"original : {msg}")
    print(f"ciphered : {ciphered}")
    print(f"deciphered : {deciphered}")

main()