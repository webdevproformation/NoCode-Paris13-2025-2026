# CPS

Content Policy Security 

- clé du header transmis dans la réponse du serveur 


content-security-policy-report-only
	object-src 'none';
    base-uri 'self';
    script-src 'nonce-boG6BlP92RuztPZAsdenDA' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;
    report-uri https://csp.withgoogle.com/csp/gws/other-hp

Donner des directives (consignes) au navigateur pour lister les codes qu'il PEUT exécuter / Où le navigateur pour exécuter du code 

<script src="http://hastebin.com/script.js">

script-src 'self';


content-security-policy
	script-src 'self' https://pastebin.com hastebin.com example.com code.jquery.com https://ssl.google-analytics.com ;



https://1ec4-212-39-129-107.ngrok-free.app/vulnerabilities/csp/
https://1ec4-212-395465496846grok-free.app/hackable/uploads/script.js