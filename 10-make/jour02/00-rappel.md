# make 

- logiciel d'automatisation, `scénario`
- module 
    - le 1er module `trigger`
    - les autres modules du scénario `action`

- dans Zapier => outil A (Google Doc / Formulaire) => mapping => outil B (Base Row / Gmail / Airtable ...) 
- dans make => mapping et en plus on peut faire des transformations en + via des formules
    
- les différentes catégories de formules :
    - générale => if / switch / get
    - mathématique => formatNumber()
    - texte  => split() / replace() / ...
    - date   => now / formatDate() ...
    - tableau => first() / slice() ...

- attention dans les formules sur make , les opérateurs de math doivent être entourées de {{-}}  {{*}}

- Bundle : l'information une fois récupérée dans les modules va être transmis sous forme de Bundle  (lot)  => l'unité de facturation dans l'outil 

- Module A 10 Bundles   =>    rassembler 1 tableau => module `Aggregate Array`
- Module qui contient 1 bundle qui contient un tableau => parcourir le tableau `for`
                        => module `Iterator`

- pour bien utiliser make, il faut OBLIGATOIREMENT comprendre le format JSON 
- les données en INPUT / OUTPUT sont dans ce format entre les modules 

