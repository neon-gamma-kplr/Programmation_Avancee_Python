class Product:
    def __init__(self, cout, prix, marque):

        self.cost = cout

        self.price = prix

        self.marque = marque




class Meubles(Product):

    def __init__(self, cost, price, marque, materiaux, couleur, dimensions):

        super().__init__(cost, price, marque)

        self.materiaux = materiaux

        self.couleur = couleur

        self.dimensions = dimensions




class Canape(Meubles):

    def __init__(self, cost, price, marque, materiaux, couleur, dimensions, made_in):

        super().__init__(cost, price, marque, materiaux, couleur, dimensions)

        self.madein = made_in




class Chaise(Meubles):

    def __init__(self, cost, price, marque, materiaux, couleur, dimensions, made_in, nb_pied ):

        super().__init__(cost, price, marque, materiaux, couleur, dimensions)

        self.nbpied = nb_pied

        self.made_in=made_in




class Table(Meubles):

    def __init__(self, cost, price, marque, materiaux, couleur, dimensions):

        super().__init__(cost, price, marque, materiaux, couleur, dimensions)




TypeScandinav = Canape(150, 999.99, "IKEA", "Bois/Tissu", "Gris", "L 150 x l 120", "Italy")

MalOCul = Chaise(0.20, 570,"Zara Home","Bois de cagette", 'Jaune de Damas',

                 "L 25000 X l 500 x H 1200", "USA", 2 )