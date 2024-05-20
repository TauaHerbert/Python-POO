class Pessoa():
    def __init__(self, nomePessoa, idadePessoa, pesoPessoa,dormindo=False,falando=False,comendo=False):
        self.nome = nomePessoa
        self.idade = idadePessoa
        self.peso = pesoPessoa

        self.dormindo = dormindo
        self.falando = falando
        self.comendo = comendo


    def comer(self, comendo):
        if self.dormindo == True:
            print(f"{self.nome} está dormindo!")
        elif self.falando == True:
            print(f"{self.nome} ja está falando!")
        elif self.comendo == True:
            print(f"{self.nome} ja está comendo!")
        else:
            print(f"{self.nome}, está comendo {comendo}")
            come = self.comendo
            self.comendo = True


    def pararComer(self):
        if self.comendo == False:
            print(f"{self.nome} não esta comendo!")
        else:
            print(f"{self.nome} parou de comer!")
            self.comendo = False


    def dormir(self):
        if self.comendo == True:
            print(f"{self.nome} está comendo!")
        elif self.falando == True:
            print(f"{self.nome} ja está falando!")
        elif self.dormindo == True:
            print(f"{self.nome} ja está dormindo!")
        else:
            print(f"{self.nome} está Dormindo!")
            self.dormindo = True

    def pararDormir(self):
        if self.dormindo == False:
            print(f"{self.nome} não esta dormindo!")
        else:
            print(f"{self.nome} parou de Dormir!")
            self.dormindo = False



    def falar(self, falando):
        if self.dormindo == True:
            print(f"{self.nome} está dormindo!")
        elif self.comendo == True:
            print(f"{self.nome} está comendo!")
        elif self.falando == True:
            print(f"{self.nome} ja está falando!")
        else:
            print(f"{self.nome} está falando: '{falando}'")
            self.falando = True

    def pararFalar(self):
        if self.falando == False:
            print(f"{self.nome} não esta falando!")
        else:
            print(f"{self.nome} parou de falar!")
            self.falando = False


