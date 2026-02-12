# en javascript pour créer une fonction 
# vous allez utiliser la syntaxe suivante

# function nom_fontion( a, b ){
# }

def nom_fonction( a, b ) :
    pass 

# créer ma fonction 

def calcul( a, b ):
    return a + b 

# exécuter la fonction ou utiliser 

calcul( 1, 2 ) 

# il est possible d'ajouter une annotation après les paramètres de la fonction 
# ces annotations sont facultatives 
def calcul( a : int, b : int ) -> int : 
    """ fonction qui va effectuer une addition """
    return a + b 

calcul()
