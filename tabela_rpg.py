print('='*26)
print('   TABELA DE RPG 2019   ')
print('='*26)

players = int(input('Quantidade de jogadores: '))

vet_players = []
vet_classes = []
vet_defeitos = []

for i in range(players):
    nome = input(f'Nome do personagem {i+1}: ')
    vet_players.append(nome)
    classe = input(f'Nome da classe do personagem {i+1}: ')
    vet_classes.append(classe)

print('-'*20)
print('Nome','Classe',sep='|')
print('-'*20)

for i in range(players):
    print(vet_players[i],vet_classes[i], sep='|')
    print('-'*20)

vet_historias = []

def cria_historias(vet_historias,i):
    historia = input('Digite sua historia: ')
    vet_historias.insert(i,historia)

indice = int(input('Digite o numero do personagem que deseja escrever a historia [-1 para sair]: '))
while indice != -1:
    cria_historias(vet_historias,indice)
    indice = int(input('Digite o numero do personagem que deseja escrever a historia [-1 para sair]: '))


vet_forca = []
vet_destreza = [] 
vet_carisma = []
vet_inteligencia = [] 
vet_manuseio = []

# Atributos , Itens , Pontos e Habilidades

def atribut(players,vet_players):
    print('='*26)
    print('   DISTRUIBUIR ATRIBUTOS   ')
    print('='*26)
    atributo = []
    for i in range(0, players):
        linha = []
        print(f'Atributos do jogador {vet_players[i]}')
        for j in range(0, 5):
            ndatributo = input(f'Atributo {j+1}: ')
            linha.append(ndatributo)

        atributo.append(linha)
    
    return atributo

matriz = atribut(players,vet_players)


def mat_itens(players,vet_players):
    print('='*26)
    print('   DISTRUIBUIR ATRIBUTOS   ')
    print('='*26)
    itens = []
    for i in range(0, players):
        linha = []
        print(f'Itens do jogador {vet_players[i]}')
        for j in range(0, 5):
            ndatributo = input(f'Item {j+1}: ')
            linha.append(ndatributo)

        itens.append(linha)
    
    return itens

matriz2 = mat_itens(players,vet_players)

def mat_habilidades(players,vet_players):
    print('='*26)
    print('   DISTRUIBUIR HABILIDADES   ')
    print('='*26)
    habilidades = []
    for i in range(0, players):
        linha = []
        print(f'Habilidades do jogador {vet_players[i]}')
        for j in range(0, 3):
            ndatributo = input(f'Habilidade {j+1}: ')
            linha.append(ndatributo)

        habilidades.append(linha)
    
    return habilidades

matriz3 = mat_habilidades(players,vet_players)


print('='*26)
print('   DISTRUIBUIR PONTOS   ')
print('='*26)

def distri_pontos(players,vet_players):
    for i in range(players):

        print(f'PERSONAGEM {vet_players[i]}')
        forca = int(input('Forca: '))
        destreza = int(input('Destreza: '))
        carisma = int(input('Carisma: '))
        inteligencia = int(input('Inteligencia: '))
        manuseio = int(input('Manuseio: '))

        vet_forca.append(forca)
        vet_destreza.append(destreza)
        vet_carisma.append(carisma)
        vet_inteligencia.append(inteligencia)
        vet_manuseio.append(manuseio)

distri_pontos(players,vet_players)

# Impressões 

def imprime(vet,vet2,vet3,vet4,vet5,players,vet_players):
        
    for i in range(players):
        print(f'PERSONAGEM {vet_players[i]} PONTOS')
        print('FORCA','DESTREZA','CARISMA','MANUSEIO','INTELIGENCIA', sep='|')
        print(vet[i],vet2[i],vet3[i],vet5[i],vet4[i], sep='       ')

def imprime_tributos(matriz,players,vet_players):
    for i in range(players):
        print(f'ATRIBUTOS DO PERSONAGEM {vet_players[i]}')
        for j in range(5):
            print(f'ATRIBUTO {j+1}) {matriz[i][j]}')

def imprime_itens(matriz,players,vet_players):
    for i in range(players):
        print(f'ITENS DO PERSONAGEM {vet_players[i]}')
        for j in range(5):
            print(f'ITEM {j+1}) {matriz[i][j]}')

def imprime_habilidades(matriz,players,vet_players):
    for i in range(players):
        print(f'HABILIDADES DO PERSONAGEM {vet_players[i]}')
        for j in range(3):
            print(f'HABILIDADE {j+1}) {matriz[i][j]}')


imprime(vet_forca,vet_destreza,vet_carisma,vet_inteligencia,vet_manuseio,players,vet_players)
imprime_tributos(matriz,players,vet_players)
imprime_itens(matriz2,players,vet_players)
imprime_habilidades(matriz3,players,vet_players)
