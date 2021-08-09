import ccrypt512 as crypt

def findPass(passhash, dictfile):
    salt = passhash[3:11]
    with open(dictfile, 'r') as dfile:
        for word in dfile.readlines:
            word = word.strip('\n')
            cryptwd = crypt.sha512_crypt(word,salt)
            if cryptwd == passhash:
                return word
    return ''

def main():
    dictfile = 'dictonary.txt'
    with open('passwords.txt', 'r') as passFile:
        for line in passFile.readlines():
            data  = line.split(':')
            user = data[0].strip()
            passwd = data[1].strip()
            word = findPass(passwd, dictfile)
            if word:
                print('FOUND Password: ID [%s] password [%s]' %(user, word))
            else:
                print('Password Not Found!')