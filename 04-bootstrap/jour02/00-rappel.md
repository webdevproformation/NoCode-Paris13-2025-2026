# rappel 

- Bootstrap => librairie qui permet de créer des maquettes de site internet 

<h1 class="text-primary mt-5">nous contacter</h1> 

<https://getbootstrap.com/>

- section spéciale Layout => Mise en page 
- Système de grille (tableau)

- ligne => `row`
- colonnes maximum de 12 colonnes

```html
<section class="row">
    <div class="col-2"> <!-- colonne a une largeur de 2/12 15% -->
    </div>    
    <div class="col-10"> <!-- colonne a une largeur de 10/12  85% -->
    </div>    
</section>
```

lemonde.fr

```html
<section class="row">
    <div class="col-5"> 
    </div>    
    <div class="col-7"> 
        <section class="row">
            <div class="col-5"> 
            </div>  
            <div class="col-7">
            </div>
        </section>
    </div>    
</section>
```

# les colonnes responsives

```html
<section class="row">
    <div class="col-7"> </div>
    <div class="col-md-5"> </div>
</section>
```

point de rupture => breakpoint 

adapter nos design en fonction de largeur des écrans des smartphones / tablette / ordinateur 

rien / sm / md / lg / xl / xxl 

<div class="col-md-5"> </div> 
=> pour les écrans qui ont une largeur inférieur à 768px la colonne fait 100% 
=> pour les écrans qui ont une largeur supérieur à 768px la colonne fait 5/12 

mobile first 

# le système de point de rupture est utilisé

- sur les col du système de grille
- mais aussi sur le composant qui permet de faire des espaces entre les balises html =>  mt-2    mt-md-2




- 
- 
-  
