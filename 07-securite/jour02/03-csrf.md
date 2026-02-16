# Cas d'école 

CSRF => Cross Server Request Forgery 

vous allez réussi à faire une action à l'administrateur du site internet SANS qu'il s'en rend compte 

vous êtes dans une page qui contient un formulaire 
ce formulaire permet à l'utilisateur de changer son mot de passe 


https://8a34-109-190-31-225.ngrok-free.app/vulnerabilities/csrf/?password_new=blabla&password_conf=blabla&Change=Change&usi=S806670411:666666666987954#

changer le mot de passe d'un utilisateur SANS qu'il s'en rende compte 

token csrf => champ masqué qui est présent dans leformulaire est dont la valeur est généré par le serveur lorsque le formulaire s'afficher

si le formulaire est soumis => ce token va être comparé et dévra être égal à celui dans le serveur


<https://04b2-212-39-129-107.ngrok-free.app>

INJECTIOn SQL 

admin' OR 1=1 --

odezhbozeubh

INJECTION XSS  dans le champ de recherche 

apple <img src="" onerror="alert('coucou')">




<h1 onload="(function(){ alert('coucou') })()">apple</h1>

function bonjour(){
}

bonjour()

(function(){
....
})()



< https://1ec4-212-39-129-107.ngrok-free.app>