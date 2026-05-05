import random
jog = str(input('Escolha entre par ou impar: ')).lower().strip()
dado = random.randint(1, 20)
escolha = 'par' if jog == 'impar' else 'impar'
print ('Certo, eu escolho {}!'.format(escolha))

class par:
    def __init__(self, dado):
        self.dado = dado

    def roll(self):
        if self.dado % 2 == 0:
            print ('Voce venceu!! o numero sorteado foi {}, um numero par!'.format(self.dado))
        else:
            print ('Voce perdeu, o numero sorteado foi {}, um numero impar!'.format(self.dado))

class impar:
    def __init__ (self, dado):
        self.dado = dado
        
    def roll (self):
        if self.dado % 2 != 0:
            print ('Voce venceu!! o numero sorteado foi {}, um numero impar!'.format(self.dado))
        else:
            print ('Voce perdeu, o numero sorteado foi {}, um numero par!'.format(self.dado))

if jog == 'impar':
    jogo = impar(dado)
    jogo.roll()
elif jog == 'par':
    jogo = par(dado)
    jogo.roll()
else:
    print ('Apenas par ou impar!')
    exit
