import random
jog = str(input('Escolha entre par ou impar: ')).lower().strip()
dado = random.randint(1, 20) #Rola um numero aleatorio de 1 a 20
escolha = 'par' if jog == 'impar' else 'impar' #Caso 'jog' seja par, escolha = impar, e vice versa.
print ('Certo, eu escolho {}!'.format(escolha))

class par: #Se 'jog' for par.
    def __init__(self, dado):
        self.dado = dado

    def roll(self):
        if self.dado % 2 == 0: #Se a divisao de 'dado' por 2, restar 0, então quem escolheu par vence.
            print ('Voce venceu!! o numero sorteado foi {}, um numero par!'.format(self.dado))
        else:
            print ('Voce perdeu, o numero sorteado foi {}, um numero impar!'.format(self.dado))

class impar: #Se 'jog' for impar.
    def __init__ (self, dado):
        self.dado = dado
        
    def roll (self):
        if self.dado % 2 != 0: #Se a divisao de 'dado' por 2, não restar 0, então quem escolheu impar vence.
            print ('Voce venceu!! o numero sorteado foi {}, um numero impar!'.format(self.dado))
        else:
            print ('Voce perdeu, o numero sorteado foi {}, um numero par!'.format(self.dado))

if jog == 'impar':
    jogo = impar(dado) 
    jogo.roll() #Inicia o roll da class impar, caso a escolha de 'jog' seja impar.
elif jog == 'par':
    jogo = par(dado)
    jogo.roll() #Inicia o roll da class par, caso a escolha de 'jog' seja par.
else:
    print ('Apenas par ou impar!') #Impede que qualquer outra string seja escrita, e termina o programa.
    exit
