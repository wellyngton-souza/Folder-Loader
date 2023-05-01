import os

def calculaEspaco(caminho, space):
    try:
        meus_arquivos = os.listdir(caminho)

        for arquivo in meus_arquivos:
            nome_completo = caminho + "\\" + arquivo
            tamanho = os.path.getsize(nome_completo)

            if "." in arquivo:
                print( space + arquivo + " " + str( round( tamanho / 1000000, 2)) + " MBs")
            else:
                print( space[:-4] + " -> " + arquivo)
                calculaEspaco(caminho + "\\" + arquivo, space + " - ")
    except:
        print("Digite um diretorio valido")

os.system('cls')
caminho = input("Diga o diretorio da Pasta:\n")
calculaEspaco(caminho, "")
input()