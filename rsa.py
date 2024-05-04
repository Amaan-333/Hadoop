import math

def is_prime(num):
    flag = 0
    if num<2:
        flag = 1
    else:
        for i in range(2,int((num/2)+1)):
            if num%i==0:
                flag = 1
                break

    if flag == 1:
        return False
    else:
        return True

def get_prime_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            if is_prime(num) and num!=2:
                return num
            else:
                print("Please enter a prime number.")
        except ValueError:
            print("Please enter a valid integer.")

p = get_prime_input("Enter prime number p: ")
q = get_prime_input("Enter prime number q: ")

n = p * q
phi = (p - 1) * (q - 1)

e = int(input("Enter public exponent e (such that gcd(e, phi) = 1): "))
while math.gcd(e, phi) != 1:
    print("Please enter a valid public exponent e such that gcd(e, phi) = 1.")
    e = int(input("Enter public exponent e: "))

msg = int(input("Enter the message to encrypt: "))

d = pow(e, -1, phi)

C = pow(msg, e, n)
decrypted_message = pow(C, d, n)
print(d)
print("Encrypted message:", C)
print("Decrypted message:", decrypted_message)
