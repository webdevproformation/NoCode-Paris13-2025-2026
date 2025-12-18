# Rappels 


## Grille responsive

### le fait de changer la largeur de colonnes des grilles

```html
<section class="row">
    <div class="col-6"></div> toujours 6/12 largeur de l'écran
    <div class="col-md-6"></div> 
        si écran < 768px largeur fait 100% 
        si l'écran >= 768px largeur 6/12
</section>
```

### le fait de faire apparaitre / disparaitre des élements de fonction de la largeur de l'écran

si je suis sur un petit écran j'affiche uniquement une icone
si je suis sur un grand écran j'affiche icone + texte

```html
<button>
    <svg></svg>
    <span class="d-none d-sm-block">text</span>
</button>

```

### Composant bootstrap

élément visuel que l'on va retrouver sur quasiment tous les sites internet

- diaporama / barre de menu / formulaire ... 
- ce sont des élements qui nécessitent du html un peu spécial ET pour certain du Javascript
- toujours la même idée il faut connaitre les bonnes class et le bonne ordre de balise