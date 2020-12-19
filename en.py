from cryptography.fernet import Fernet

"""
Modo de uso:

    Use apenas encrypt(), decrypt() ou imprimir().           |
                                                             |
    - encript():  irá  imprimir  o  arquivo  criptografado  e| 
    impresso  no diretório  atual,  com  o  mesmo nome.  Caso|
    precise recuperá-lo, use o impimir()                     |
                                                             |
    - decrypt():  te retorna  o arquivo  descriptografado, em|
    bytes,  não string. Para  imprimir o arquivo no  console,|
    use print(decrypt(arg).decode())                         |
                                                             |
    - imprimir(): irá  imprimir o arquivo no diretório atual.|
    Para usá-lo, você precisa da função decrypt() no terceiro|
    argumento.                                               |
"""


## Class
class En:

    # Gera uma chave
    def gen_key():
        # Key é um objeto gerado pelo Fernet
        # Sempre que executado a chave será resetada
        key = Fernet.generate_key()

        # Escreve a chave, como "mykey.key", na pasta do arquivo
        with open("mykey.key", "wb") as gen_my_key:
            gen_my_key.write(key)

    def encrypt(arquivo):

        # Atualiza a chave a cada encriptação
        En.gen_key()

        # Lê a chave
        with open("mykey.key", "rb") as mk:
            key = mk.read()
        # f é a chave no Fernet
        f = Fernet(key)

        with open(arquivo, "rb") as read_file:
            og = read_file.read()

        # Fecha o arquivo com a chave
        encrypted = f.encrypt(og)

        with open(arquivo, "wb") as enc:
            enc.write(encrypted)

    def decrypt(arquivo):

        with open("mykey.key", "rb") as mk:
            key = mk.read()
        f = Fernet(key)

        with open(arquivo, "rb") as enc_file:
            en_cont = enc_file.read()

        decrypted = f.decrypt(en_cont)

        return decrypted
        
        # Para imprimir o arquivo descriptografado, use:
        """
        with open(f"descrypt_{nome_arquivo}", 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
        """
    
    def imprimir(nome, extensão, decrypted):
        with open(f"{nome}.{extensão}", "wb") as write:
            write.write(decrypted)
        ## Modo de uso:
        ### En.imprimir(nome, extensão, En.decrypt(arquivo))
