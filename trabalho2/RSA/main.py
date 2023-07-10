#1 - escolha p, q:
#2 - calcule N = p * q:
#3 - calcule phi(N) = (p - 1) * (q - 1):
#4 - escolha um inteiro e tal que 1 < e < phi(N) e que 'e' e phi(N) sejam primos entre si:
#5 - calcule d tal que d * e (mod phi(N)) = 1 :
import miller_rabin
import mdc
import time
import base64
#from Crypto.Util.number import long_to_bytes, bytes_to_long


#1 - escolha p, q:
bits = input("Digite o número de bits da chave: ")
startTime = time.time()
bits = int(bits)
p = miller_rabin.gen_prime(bits)
while True:
    q = miller_rabin.gen_prime(bits)
    if p != q:
        break

print(f"\np = {p}")
print(f"\nq = {q}")

#2 - calcule N = p * q:
N = p * q
print(f"\nN = {N}")

#3 - calcule phi(N) = (p - 1) * (q - 1):
phi_N = (p - 1) * (q - 1)       # Função totiente de Euler ou função Phi
print(f"\nphi_N = {phi_N}")

#4 - escolha um inteiro 'e' tal que 1 < e < phi(N) e que 'e' e phi(N) sejam primos entre si:
while True:                         
    e = miller_rabin.gen_prime(bits)
    if 1 < e < phi_N:
        if e != p and e != q:
            if mdc.mdc(e, phi_N) == 1:
                if mdc.mdc(e, N) == 1:
                    break
    
print(f"\ne = {e}")

encripting_key = (e, N)
print(f"\nChave pública: {encripting_key}")


#5 - calcule d tal que d * e (mod phi(N)) = 1 :

"""
a=38
m=97
res = pow(a, -1, m)

"""
def inverso_modular(e, phi_N):
    d = pow(e, -1, phi_N)
    return d

d = inverso_modular(e, phi_N)

print(f"\nd = {d}")

decrypting_key = (d, N)
print(f"\nChave privada: {decrypting_key}")

print(f"Tempo Total: Completado em {time.time() - startTime} segundos.")


print("\nTeste das chaves: \n")
msg = b"dados bancarios de Mauro Fernandes de Almeida"
print(msg)
m = base64.b64encode(msg)
print("\nstr msg to base64: \n", m)

m_to_int = int.from_bytes(m, byteorder='big')
m = m_to_int
print("\nbase64 to int: \n", m)
ciphertext = pow(m, e, N)
print(f"\nciphertext (encrypted msg): {ciphertext}\n")


plaintext = pow(ciphertext, d, N)
print(f"Decrypted msg (int): ", plaintext)

int_to_base64 = base64.b64encode(plaintext.to_bytes((plaintext.bit_length() + 7) // 8, byteorder='big'))
print("\nplaintext(int) to b64 decoding: \n", base64.b64decode(int_to_base64))

# int_to_bytes = plaintext.to_bytes((plaintext.bit_length() + 7) // 8, byteorder='big')
# print(f"int to bytes: {int_to_bytes}")
# int_to_bytes = base64.b64encode(int_to_bytes)

# print(f"\nint to bytes to base64: {int_to_bytes}")

# print("\nplaintext(int) to b64 decoding: \n", base64.b64decode(int_to_bytes))

