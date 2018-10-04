"""
Created on Thu Sep 13 11:01:36 2018

@author: ricar
"""


#Tentativa de implementar o json, que por algum motivo não funcionou.
#import json

#with open("Comandas.json", "r") as dados:
 #   comandas = json.load(dados)
#with open("cardapio.json","r") as dados1:
 #   cardapio = json.load(dados1)



comandas = {1: {}, 2: {}, 3: {}}
cardapio = {"jujuba": 10.00, "pipoca gourmet": 60.00, "suco de tomate": 15.00, "água":2.50}

rodando_geral = True
while rodando_geral:
    
    escolha_1 = input("O que deseja acessar? (Menu, Comanda ou 0 para sair) :  ")
    
    
    if escolha_1 == "Comanda":
        escolha_2 = input("O que deseja fazer? (add Comanda (add), ou acessar Comanda existente? (Comandas)) :  ")
        if escolha_2 == "Comandas":
            Comanda = int(input("Digite o numero da comanda:"))
            while Comanda not in comandas or Comanda < 1:
                Comanda = input("Comanda inválida, digite o número correto:")
        elif escolha_2 == "add":
            nova_comanda = int(input("Escolha um número para a nova comanda:"))
            comandas[nova_comanda] = {}
            print("Comanda adicionada")
    
    
        rodando = True
    
        while rodando:
        
            print("0: Sair")
            print("1: adicionar item")
            print("2: remover item")
            print("3: imprimir comanda")
            print("4: Adicionar uma nova comanda")
        
        
            escolha = int(input("Faça a sua escolha: "))
        
        
            if escolha == 0:
                print("Até logo!")
                rodando = False
        
            elif escolha == 1:
                novo_produto = input("Novo Produto:")
                novo_produto = novo_produto.lower()
            
                while novo_produto not in cardapio:
                    print("Não temos este item no cardápio.")
                    novo_produto = input("Novo Produto:")
                    
                quantidade = int(input("Quantidade: "))
                preco_unitario = cardapio[novo_produto]
                preco_total = quantidade*preco_unitario
                comandas[Comanda][novo_produto] = quantidade
                print("Item Adicionado")  
                
            elif escolha == 2:
            
                remove_produto = input("Retirar o Profuto: ")
                remove_produto = remove_produto.lower()
                while remove_produto not in comandas[Comanda]:
                    print("Produto não encontrado!")
                    remove_produto = input("Nome do Produto: ")
                    del comandas[Comanda][remove_produto]
                    print("Item removido")
            
           
            elif escolha == 3:
                if len(comandas[Comanda])<=0:
                    print("Nem um item na comanda.")
         
            
                Total = 0
                for e in comandas[Comanda]:
                    
                    print("")
                    print("Produto: {0}".format(e))
                    print("Quantidade: {0}".format(comandas[Comanda][e]))
                    print("")
                    
                    for i in cardapio:
                        if i == e:
                            print("Preço unitário: {0}".format(cardapio[e]))
                            print("Preço total: {0}" .format(cardapio[e]*quantidade))
                    print("")
                for produto in cardapio:
                    if produto in comandas[Comanda]:
                        Total = Total + preco_total
                        
                Taxa = Total*0.10
                Total_com_taxa = Total + Taxa
                print("Total: {0}".format(Total))
                print("Total com 10%: {0}".format(Total_com_taxa))
            
      
            
            
    
    
    
    elif escolha_1 == "Menu":
        rodando2 = True
        while rodando2:
            print("0: Sair")
            print("1: imprimir cardápio")
            print("2: Adcionar item ao cardápio")
            print("3: Modificar preço de produto")
            c = int(input("O que deseja fazer?"))
            
            
            if c == 0:
                rodando2 = False
        
            elif c ==1:
                for i in cardapio:
                    print("{0} (R$ {1})".format(i, cardapio[i]))
                
                
            elif c == 2:
                novo_item = input("Qual produto deseja adicionar?")
                preco_novo_item = input("Qual o preço unitário?")
                cardapio[novo_item] = preco_novo_item
                print("produto adcionado ao cardapio.") 
            
            
            elif c == 3:
                product = input("Qual produto você deseja alterar? ")
                while product not in cardapio:
                    product = input("Qual produto você deseja alterar? ")
                novo_preco = input("Qual o novo preço?")
                cardapio[product] = novo_preco
                print("preço alterado!")
        
            
#with open("Comandas.json", "w") as dados:
 #   nova_comanda = json.dumps(comandas, indent=2, sort_keys=True)
  #  dados.write(nova_comanda)
    
#with open("cardapio.json","w") as dados1:
 #   novo_produto = json.dumps(cardapio, indent=2, sort_keys=True)
  #  dados1.write(novo_produto)
        
    
    
                
                
                
                        
                 
                
    
        
        
             
                
        
     
         
        