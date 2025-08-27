# Solicita uma palavra
palavra = input("Digite uma palavra: ")

# Converte a palavra para minúsculas e remove espaços para uma verificação mais robusta
palavra_limpa = palavra.lower().replace(" ", "")

# Inverte a palavra
palavra_invertida = palavra_limpa[::-1]

# Compara a palavra original com a invertida
if palavra_limpa == palavra_invertida:
    print(f'"{palavra}" é um palíndromo.')
else:
    print(f'"{palavra}" não é um palíndromo.')