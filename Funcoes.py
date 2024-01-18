import random
from Ferramenta import Ferramenta
from Ferramenta110 import Ferramenta110
from Ferramenta220 import Ferramenta220
import Verificacao
import Limpeza

def cadastrar_ferramenta(tensao):
        nome = str(input("Digite o nome da ferramenta: "))
        descricao = str(input("Digite o descricao da ferramenta: "))
        marca = str(input("Digite o marca da ferramenta: "))
        codigo = random.randint(0,1000)
        preco = Verificacao.verificar_float("Digite o preço da ferramenta: ")
        quantidade_minima = Verificacao.verificar_inteiro("Digite a quantidade mínima: ")
        quantidade_atual = 0
        
        escolha = 0
        while escolha != "1" or escolha != "2":
            escolha = input("Selecione o tipo de tensão da ferramemnta:\n[1] 110V\n[2] 220V\n")
            if escolha == "1":
                tensao = "110V"
                return Ferramenta110(nome, descricao, preco, marca, codigo,quantidade_minima, quantidade_atual, tensao)
            elif escolha == "2":
                tensao = "220V"
                return Ferramenta220(nome, descricao, preco, marca, codigo,quantidade_minima, quantidade_atual, tensao)
            else:
                print("\033[31;1mResposta inválida!\033[m")
                Limpeza.limpar_tela_timer()

def edita_ferramenta(codigo_informado, lista_ferramentas):
    for ferramenta in lista_ferramentas:
        if codigo_informado == Ferramenta.get_codigo(ferramenta):
            nome = str(input("Digite o nome da ferramenta: "))
            descricao = str(input("Digite o descricao da ferramenta: "))
            marca = str(input("Digite o marca da ferramenta: "))
            preco = Verificacao.verificar_float(("Digite o preço da ferramenta: "))
            quantidade_minima = Verificacao.verificar_inteiro("Digite a quantidade mínima: ")
 
            Ferramenta.set_nome(ferramenta, nome)
            Ferramenta.set_descricao(ferramenta, descricao)
            Ferramenta.set_preco(ferramenta, preco)
            Ferramenta.set_marca(ferramenta, marca)
            Ferramenta.set_quantidade_minima(ferramenta, quantidade_minima)
            return print("Alterado! ")
    return print("\033[31;1mCódigo não encontrado!\033[m")

def adiciona_ferramenta(codigo_informado, lista_ferramentas):
    for ferramenta in lista_ferramentas:
        if codigo_informado == Ferramenta.get_codigo(ferramenta):
            quantidade_nova = Verificacao.verificar_inteiro("Digite a quantidade a ser adicionada: ")
            quantidade_anterior = Ferramenta.get_quantidade_atual(ferramenta)
            quantidade_final = quantidade_anterior + quantidade_nova
            Ferramenta.set_quantidade_atual(ferramenta, quantidade_final) 
 
            return print("Adicionado! ")
    return print("\033[31;1mCódigo não encontrado!\033[m")

def remove_ferramenta(codigo_informado, lista_ferramentas):
    for ferramenta in lista_ferramentas:
        if codigo_informado == Ferramenta.get_codigo(ferramenta):
            quantidade_remover = Verificacao.verificar_inteiro("Digite a quantidade a ser removida: ")
            if quantidade_remover <= Ferramenta.get_quantidade_atual(ferramenta):
                quantidade_anterior = Ferramenta.get_quantidade_atual(ferramenta)
                quantidade_final = quantidade_anterior - quantidade_remover
                Ferramenta.set_quantidade_atual(ferramenta, quantidade_final)
                return print("Removido! ")
            else:
                return print("Não pode remover uma quantidade maior que a atual! ")
    return print("\033[31;1mCódigo não encontrado!\033[m")

def excluir_ferramenta(codigo_informado,lista_ferramentas):
    for ferramenta in lista_ferramentas:
        if(codigo_informado==Ferramenta.get_codigo(ferramenta)):
            if Ferramenta.get_quantidade_atual(ferramenta) == 0:
                lista_ferramentas.remove(ferramenta)
                return print("Excluído! ")
            else:
                return print("Ainda há quantidade em estoque!")
    return print("\033[31;1mCódigo não encontrado!\033[m")

def exibir_marca(lista_ferramentas):
    marca_procurada = input("Digite a marca a ser pesquisada: ")
    for ferramenta in lista_ferramentas:
        if Ferramenta.get_marca(ferramenta) == marca_procurada:
            print("=== Produtos da Marca ===")
            print(f"Codigo: {ferramenta.get_codigo()}")
            print(f"Nome: {ferramenta.get_nome()}")
            print(f"Descrição: {ferramenta.get_descricao()}")
            print(f"Marca: {ferramenta.get_marca()}")
            print(f"Preço: R${ferramenta.get_preco()}")
            print(f"Quantidade minima: {ferramenta.get_quantidade_minima()}")
            print(f"Quantidade atual: {ferramenta.get_quantidade_atual()}")
            print(f"Tensão: {ferramenta.get_tensao()}")
            print("==================================")

def exibir_tensao(lista_ferramentas):
    escolha = input("Selecione o tipo de tensão da ferramemnta para procurar:\n[1] 110V\n[2] 220V\n")
    while escolha != "1" or escolha != "2":
        if escolha == "1":tensao_procurada = "110V"
        elif escolha=="2":tensao_procurada = "220V"
        else:print("\033[31;1mResposta inválida!\033[m")        
        for ferramenta in lista_ferramentas:
            if ferramenta.get_tensao() == tensao_procurada:
                print("=== Produtos da Marca ===")
                print(f"Codigo: {ferramenta.get_codigo()}")
                print(f"Nome: {ferramenta.get_nome()}")
                print(f"Descrição: {ferramenta.get_descricao()}")
                print(f"Marca: {ferramenta.get_marca()}")
                print(f"Preço: R${ferramenta.get_preco()}")
                print(f"Quantidade minima: {ferramenta.get_quantidade_minima()}")
                print(f"Quantidade atual: {ferramenta.get_quantidade_atual()}")
                print(f"Tensão: {ferramenta.get_tensao()}")
                print("==================================")    
            elif len(lista_ferramentas) == 0:
                print("\033[31;1mNão há ferramentas cadastradas com essa tensão!\033[m")
            elif ferramenta.get_tensao() != tensao_procurada:
                continue
            else:
                print("\033[31;1mOpção selecionada inexistente!\033[m")
        break 
                    

def verifica_necessidade_compra(lista_ferramentas):
    for ferramenta in lista_ferramentas:
        if Ferramenta.get_quantidade_atual(ferramenta) <= Ferramenta.get_quantidade_minima(ferramenta):
            print("=== Necessita Repôr Estoque ===")
            print(f"Codigo: {ferramenta.get_codigo()}")
            print(f"Nome: {ferramenta.get_nome()}")
            print(f"Descrição: {ferramenta.get_descricao()}")
            print(f"Marca: {ferramenta.get_marca()}")
            print(f"Preço: R${ferramenta.get_preco()}")
            print(f"Quantidade minima: {ferramenta.get_quantidade_minima()}")
            print(f"Quantidade atual: {ferramenta.get_quantidade_atual()}")
            print(f"Tensão: {ferramenta.get_tensao()}")
            print("==================================")

def exibir_codigo(lista_ferramentas):
    codigo_procurado = Verificacao.verificar_inteiro(int(input("Digite o código do produto: ")))
    for ferramenta in lista_ferramentas:
        if Ferramenta.get_codigo(ferramenta) == codigo_procurado:
            print("=== Informações do Produto ===")
            print(f"Codigo: {ferramenta.get_codigo()}")
            print(f"Nome: {ferramenta.get_nome()}")
            print(f"Descrição: {ferramenta.get_descricao()}")
            print(f"Marca: {ferramenta.get_marca()}")
            print(f"Preço: R${ferramenta.get_preco()}")
            print(f"Quantidade minima: {ferramenta.get_quantidade_minima()}")
            print(f"Quantidade atual: {ferramenta.get_quantidade_atual()}")
            print(f"Tensão: {ferramenta.get_tensao()}")
            print("==================================")

def exibir_informacoes(lista_ferramentas):
    Limpeza.limpar_tela()
    for ferramenta in lista_ferramentas:
        print("=== Informações da Ferramenta ===")
        print(f"Codigo: {ferramenta.get_codigo()}")
        print(f"Nome: {ferramenta.get_nome()}")
        print(f"Descrição: {ferramenta.get_descricao()}")
        print(f"Marca: {ferramenta.get_marca()}")
        print(f"Preço: R${ferramenta.get_preco()}")
        print(f"Quantidade minima: {ferramenta.get_quantidade_minima()}")
        print(f"Quantidade atual: {ferramenta.get_quantidade_atual()}")
        print(f"Tensão: {ferramenta.get_tensao()}")
        print("==================================")