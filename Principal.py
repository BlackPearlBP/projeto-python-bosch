from Ferramenta import Ferramenta
import Limpeza
import Funcoes
from re import match
import Verificacao
import os 

if __name__ == "__main__":
    Limpeza.limpar_tela()
    lista_ferramentas = []
    opcao=0
    while(opcao != 11):
        opcao = int(input("Selecione uma tela:\n[1] Cadastrar\n[2] Mostrar\n[3] Editar\n[4] Adicionar no Estoque\n[5] Remover do Estoque\n[6] Excluir\n[7] Perquisar por Marca\n[8] Perquisar por Tensão\n[9] Verificar Necessidade de Compra\n[10] Perquisar por Código\n[11] Sair\n"))
        match opcao:
            case 1:
                #cadastrar ferramenta
                Limpeza.limpar_tela()
                tensao = ""
                lista_ferramentas.append(Funcoes.cadastrar_ferramenta(tensao))
                Limpeza.limpar_tela()
            case 2:
                #mostrar ferramenta
                if len(lista_ferramentas) > 0:
                        Limpeza.limpar_tela()
                        Funcoes.exibir_informacoes(lista_ferramentas)
                else:
                    print("\033[31;1mNão há ferramentas\033[m")
                    Limpeza.limpar_tela_timer()
            case 3:
                #editar ferramenta
                if len(lista_ferramentas) > 0:
                    codigo=Verificacao.verificar_inteiro("Informe o código: ")
                    Limpeza.limpar_tela()
                    Funcoes.edita_ferramenta(codigo,lista_ferramentas)
                else:
                    print("\033[31;1mNão há ferramentas\033[m")
                    Limpeza.limpar_tela_timer()
                Limpeza.limpar_tela_timer()
            case 4:
                #adicionar no estoque
                if len(lista_ferramentas) > 0:
                    codigo=Verificacao.verificar_inteiro("Informe o código: ")
                    Limpeza.limpar_tela()
                    Funcoes.adiciona_ferramenta(codigo,lista_ferramentas)
                else:
                    print("\033[31;1mNão há ferramentas\033[m")
                    Limpeza.limpar_tela_timer()
                Limpeza.limpar_tela_timer()
            case 5:
                #remover do estoque
                if len(lista_ferramentas) > 0:
                    codigo=Verificacao.verificar_inteiro("Informe o código: ")
                    Limpeza.limpar_tela()
                    Funcoes.remove_ferramenta(codigo,lista_ferramentas)
                else:
                    print("\033[31;1mNão há ferramentas\033[m")
                    Limpeza.limpar_tela_timer()
                Limpeza.limpar_tela_timer()
            case 6:
                #excluir xd
                if len(lista_ferramentas) > 0:
                    codigo=Verificacao.verificar_inteiro("Informe o código: ")
                    Limpeza.limpar_tela()
                    Funcoes.excluir_ferramenta(codigo,lista_ferramentas)
                else:
                    print("\033[31;1mNão há ferramentas\033[m")
                    Limpeza.limpar_tela_timer()
                Limpeza.limpar_tela_timer()
            case 7:
                #consultar marca
                if len(lista_ferramentas) > 0:
                        Limpeza.limpar_tela()
                        Funcoes.exibir_marca(lista_ferramentas)
                else:
                    print("\033[31;1mNão há ferramentas\033[m")
                    Limpeza.limpar_tela_timer()
            case 8:
                #consultar tensao
                if len(lista_ferramentas) > 0:
                        Limpeza.limpar_tela()
                        Funcoes.exibir_tensao(lista_ferramentas)
                else:
                    print("\033[31;1mNão há ferramentas\033[m")
                    Limpeza.limpar_tela_timer()
            case 9:
                #verificar necessidade de compra
                if len(lista_ferramentas) > 0:
                        Limpeza.limpar_tela()
                        Funcoes.verifica_necessidade_compra(lista_ferramentas)
                else:
                    print("\033[31;1mNão há ferramentas\033[m")
                    Limpeza.limpar_tela_timer()
            case 10:
                #consultar codigo
                if len(lista_ferramentas) > 0:
                        Limpeza.limpar_tela()
                        Funcoes.exibir_codigo(lista_ferramentas)
                else:
                    print("\033[31;1mNão há ferramentas\033[m")
                    Limpeza.limpar_tela_timer() 
            case 11:
                print("Logoff...")
                Limpeza.limpar_tela_timer()