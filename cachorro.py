class Cachorro:
    def __init__(self, nome, raca, comida):
        self.cachorro = Cachorro
        self.nome = nome
        self.raca = raca
        self.comida = comida
        self.acordado = False
        self.feliz = False

    def acordar (self):
        self.acordado = True
        print(f"{self.nome} está acordado!")
    
    def dormir (self):
        self.acordado = False
        print(f"{self.nome} está dormindo!")
        
    def brincar (self):
        self.feliz = True
        print(f"{self.nome} está brincando e feliz!")

    def ignorar (self):
        self.feliz = False
        print(f"{self.nome} está triste!")

    def latir (self):
        if self.acordado:
         print(f"{self.nome} está latindo!")  
         
        else:
         print(f"{self.nome} não está latindo porque está dormindo!")

    def comida (self):
       self.acordado is True
       self.comida -=1
       print(f"{self.nome} está comemdo!")
       

cachorro1 = Cachorro("Sylus","Doberman")

cachorro1.exibirstatus()
cachorro1.dormirr()
cachorro1.acordar()
cachorro1.brincar()
