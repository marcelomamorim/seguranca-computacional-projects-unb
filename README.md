# seguranca-computacional-projects-unb
Projetos da matéria de segurança computacional

## Parte 1

- Para executar o cifrador e o decifrador

Na pasta ./app/parte-1 ::: Executar o seguinte comando

> python main.py

```python
if __name__ == '__main__':
    generated_key = generate_key_with_the_same_size_of_input(entrada, chave)
    # CIFRANDO O TEXTO - PARTE 1 DO TRABALHO
    ciphed_text = generate_ciphed_text(entrada, generated_key)
    # DECIFRANDO O TEXTO - PARTE 1 DO TRABALHO
    original_text = generate_original_text(ciphed_text, generated_key)
    print('GENERATING CIPHER ::::::::::::::> CIPHER -> ' + ciphed_text)
    print('DECODING TEXT ::::::::::::::> ORIGINAL -> ' + original_text)
```

## Parte 2 

Na pasta ./app/parte-2 ::: Executar o seguinte comando

> python main.py

-Nessa parte deve ser escolhido o texto 1 ou 2
Exemplo:
Escolha entre o texto 1 e o texto 2 [1 ou 2]::> 1


Em seguida, o tamanho da chave (não finalizamos a implementação dessa parte):
Escolha o tamanho da chave :::> Colocar números de 0 a 10
Por tentativa e erro, descobrimos que a chave pro texto um tem tamanho 5 e pro texto 2 tamanho 8.

