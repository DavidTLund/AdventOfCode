import hashlib

secret_key = 'bgvyzdsv'

# initializing string
str2hash = secret_key + "0000001"
  
str2hash = 'abcdef609043'
# encoding GeeksforGeeks using encode()
# then sending to md5()
result = hashlib.md5(str2hash.encode())
  
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())
