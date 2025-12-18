# image

https://placehold.co/400x200

image a des dimensions : largeur 400px et une hauteur 200px

vous voulez intégrer une image qui est dans mon ordinateur dans ma page web

on veut que l'image quelque soit ses dimensions rentre dans une zone de mon design 
ET je ne sais pas à l'avance la largeur et la hauteur de la zone 

lorsque on n'a travaillé avec Bootstrap  `w-100` => l'image doit prendre 100% de la largeur de la zone DANS laquelle elle est 

Dans webflow :

https://placehold.co/400x200

zone colonne elle a comme dimensions  300x150

image{
    width:100%; => 300px
    height : 250px ; 250px
    object-fit: cover ; => qui va faire en sorte que image ne soit pas déformée
                        => rogner l'image pour quelle rentre dans la zone sans déforme
}
