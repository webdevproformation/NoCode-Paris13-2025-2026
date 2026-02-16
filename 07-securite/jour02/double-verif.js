document.querySelectorAll(".js-btn-suppr").forEach(function(btn){
    btn.addEventListener("click" , function(){
        return confirm("confirmez la supprimer de ce profil dans un fichier externe")
    })
})