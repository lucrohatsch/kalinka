function botones(){

    botones_editar = document.querySelectorAll("a[data-target='#formEditarPrioridad']");
    botones_eliminar = document.querySelectorAll("a[data-target='#formEliminarPrioridad']");

    botones_editar.forEach(boton => {
        boton.addEventListener('click', leerPrioridad, true);
    });

    botones_eliminar.forEach(boton => {
        boton.addEventListener('click', confirmacion, true);
    });



    function leerPrioridad(){
        let url = this.getAttribute('href')
        let myRequest=new Request(url)
        fetch(myRequest)
            .then(response => {
                return response.json();
                
            })
            .then(data => {
                document.querySelector("#editarForm input[name='nombre']").value = data[0]['nombre'];
                document.querySelector("#editarForm input[name='valor']").value = data[0]['valor'];
                document.querySelector("#editarForm").action = "editarPrioridad/"+data[0]['id']

            })
            
    }

    function confirmacion(){
        let url = this.getAttribute('href')
        let myRequest=new Request(url)
        fetch(myRequest)
            .then(response => {
                return response.json();
                
            })
            .then(data => {
                document.querySelector("#eliminarForm span[name='prioridad']").innerHTML = data[0]['nombre'];
                console.log(data[0]['nombre'])
                document.querySelector("#eliminarForm").action = "eliminaPrioridad/"+data[0]['id'];
            })
    }
        



}





window.onload = botones;