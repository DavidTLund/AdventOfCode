import hashlib


def find_first_MD5(key):
    # initializing string
    index = 0
    keepLooking = True
    hashPrefix = "000000"
    hashToTest = ""
    while keepLooking:
        index += 1
        str2hash = key + str(index)
        result = hashlib.md5(str2hash.encode())
        hashToTest = result.hexdigest()
        if hashPrefix == hashToTest[0:6]:
            print("hash string", str2hash)
            print("The hexadecimal equivalent of hash is : ", end ="")
            print(result.hexdigest())
            keepLooking = False
            return index
    return -1

        

secret_key = 'abcdef'
secret_key = 'pqrstuv'

# David Lund Knowit key. Funny thing the answer was the same for both
secret_key = 'bgvyzdsv'
# David hotmail key
secret_key = 'ckczppom'

index = find_first_MD5(secret_key)

print("The smallest int:", index)
