frase = str(input('Digite a frase: ')).lower().strip()
print(f'Quantidade: {frase.count("a")}. Posição: {frase.find("a")+1}. Ultima posição {frase.rfind("a")+1}')