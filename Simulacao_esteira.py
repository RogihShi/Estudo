import random

caixas = ['grande', 'media', 'pequena']

def simulacao(num_caixas):
    
    for i in range(num_caixas):
        tipo_caixa = random.choice(caixas)
        
        print(f"\nCaixa {i+1} chegou. Tipo: {tipo_caixa}")
        
        if tipo_caixa == 'grande':
            print(f"Direcionada ao caminho A (grandes). Separada com sucesso.")
            
        elif tipo_caixa == 'media':
            print(f"Direcionada ao caminho B (médias). Separada com sucesso.")
            
        else: 
            print(f"Direcionada ao caminho C (pequenas). Separada com sucesso.")

    print("\nSimulação concluída!")

simulacao(9)