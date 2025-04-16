import string

def is_palindrome(word: str) -> bool:
    cleaned = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    palabra = input("Ingresá una palabra o frase: ")
    if is_palindrome(palabra):
        print(f'"{palabra}" es un palíndromo')
    else:
        print(f'"{palabra}" no es un palíndromo')

#if __name__ == "__main__":
    #palabra = input("Ingresá una palabra o frase: ")
    #if is_palindrome(palabra):
        #print(f'"{palabra}" es un palíndromo')
    #else:
        #print(f'"{palabra}" no es un palíndrmo"
