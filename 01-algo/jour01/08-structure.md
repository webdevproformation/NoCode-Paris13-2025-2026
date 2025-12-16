# structure de controle

- par défaut lorsque l'on écrit un programme informatique
- il s'exécute dans l'ordre dans lequel on l'a écrit 

en informatique, il existe 3 structures qui, lorsqu'elles sont présentes dans le code, changent l'ordre d'exécution 

1. condition
2. boucle 
3. fonction / procédure
 

```txt
algo is_majeur

variables
    age : int
    verif : bool 

debut
    Ecrire("Quel est votre age ???")
    Lire(age)
    
    verif <- age < 18 
    

    // la condition
    Si verif Alors
        // traitement 1
        Ecrire("Vous êtes Mineur")
    Sinon
        // traitement 2
        Ecrire("Vous êtes Majeur")

fin 
```



