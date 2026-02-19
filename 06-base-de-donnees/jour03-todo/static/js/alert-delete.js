function confirm_delete(e)
{
    e.addEventListener("click", function(event){
        event.preventDefault();
        const reponse =  confirm("Etes vous sur de vouloir supprimer ce Todo ?")
        if(reponse){
            window.location.href =  e.href
        }
        //return confirm("Etes vous sur de vouloir supprimer ce Todo ?")
    });
}


document.querySelectorAll(".js-delete").forEach(confirm_delete)
