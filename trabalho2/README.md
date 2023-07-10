# Trabalho 2: relatório e instruções 

## AES

Não implementado.

## RSA

1 - escolha p, q:

2 - calcule N = p * q:

3 - calcule phi(N) = (p - 1) * (q - 1):

4 - escolha um inteiro e tal que 1 < e < phi(N) e que 'e' e phi(N) sejam primos entre si:

5 - calcule d tal que d * e (mod phi(N)) = 1 :

### Miller-Rabin

Uma das principais vantagens desse teste é que ele é executado em tempo polinomial, o que nos garante que quando a entrada aumenta, o tempo de espera não cresça demasiadamente como nos teste não polinomiais.

### Gerador de primos

A função usada `gen_prime` gera ímpares aleatórios e os submete ao teste de primalidade (Miller Rabin) por `k` rounds (k=40). Caso o teste retorne `True`, o número é retornado pela função geradora de primos.

### Inversos modulares

##### Função embutida Python: `pow(base, exp[, mod])`

`Pow` retorna base à potência de exp; se mod estiver presente, retorna base à potência exp, módulo mod (calculado com mais eficiência do que `pow(base, exp) % mod`).

Para operandos `int` `base` e `exp`, se mod estiver presente, mod também deve ser do tipo inteiro e `mod` deve ser diferente de zero. Se mod estiver presente e exp for negativo, base deve ser relativamente primo para mod. Nesse caso, `pow(inv_base, -exp, mod)` é retornado, onde inv_base é um inverso ao base módulo mod.
Aqui está um exemplo de computação de um inverso para 38 módulo 97:

    >>> pow(38, -1, mod=97)
    23
    >>> 23 * 38 % 97 == 1
    True

## Referências

<https://docs.python.org/pt-br/3.10/library/functions.html?=pow#pow>

<https://en.wikipedia.org/wiki/Modular_multiplicative_inverse>

<https://acervolima.com/modular-multiplicativo-inverso-de-1-a-n/>

<https://www.mentebinaria.com.br/artigos/tudo/introdu%C3%A7%C3%A3o-ao-rsa-r80/>

<https://www.youtube.com/watch?v=4zahvcJ9glg>

<https://www.youtube.com/watch?v=zmhUlVck3J0>

<https://pycryptodome.readthedocs.io/en/latest/src/util/util.html>

<https://pypi.org/project/pycrypto/>
