from Crypto.Cipher import DES3
from Crypto.Hash import SHA256 as SHA
from os import path # getsize 이용하고자 import 함
KSIZE = 1024 # 전역변수

class myDES():
    def __init__(self, keytext, ivtext):
        hash = SHA.new()
        hash.update(keytext.encode('utf-8'))
        key = hash.digest()
        self.key = key[:24]

        hash.update(ivtext.encode('utf-8'))
        iv = hash.digest()
        self.iv = iv[:8] # 벡터 생성

    def makeEncInfo(self, filename):
        fillersize = 0
        filesize = path.getsize(filename) # file size return
        if filesize % 8 != 0:
            fillersize = 8-filesize%8
        filler = '0'*fillersize
        header = '%d' % (fillersize)
        gap = 8 - len(header)
        header += '#'*gap
        
        return header, filler

    def enc(self, filename):
        encfilename = filename + '.enc'
        header, filler = self.makeEncInfo(filename)# header, 0 문자열

        des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv)

        h = open(filename, 'rb')
        hh = open(encfilename, 'wb+')
        enc = header.encode('utf-8')
        content = h.read(KSIZE)
        content = enc + content
        
        while content:
            if len(content) < KSIZE:
                content += filler.encode('utf-8')
            enc = des3.encrypt(content)
            hh.write(enc)
            content = h.read(KSIZE)
        h.close
        hh.close

    def dec(self, encfilename):
        fileanme = encfilename + '.dec'
        des3 = DES3.new(self.key, DES3.MODE_CBC, self.iv)

        h = open(filename, 'wb+')
        hh = open(encfilename, 'rb')

        content = hh.read(8)
        dec = des3.decrypt(content)
        header = dec.decode()
        fillersize = int(header.split('#'[0]))

        content = hh.read(KSIZE)
        while content:
            dec = des3.decrypt(content)
            if len(dec) < KSIZE:
                if fillersize != 0:
                    print(f"dec : {dec[:-fillersize]}")
                    dec = dec[:-fillersize]
            h.write(dec)
            content = hh.read(KSIZE)
        h.close()
        hh.close()

def main():
    keytext = 'samsjang'
    ivtext = '1234'
    filename = 'plain.txt'
    encfilename = filename + '.enc'

    myCipher = myDES(keytext, ivtext)
    myCipher.enc(filename)
    myCipher.dec(encfilename)

    if __name__ == '__main__':
        main()