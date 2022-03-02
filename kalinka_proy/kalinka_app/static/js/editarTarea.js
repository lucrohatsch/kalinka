
function botones(){
    botones_editar = document.querySelectorAll("a[data-target='#editaTarea']");
    botones_eliminar = document.querySelectorAll("a[data-target='#eliminarTarea']");

    botones_editar.forEach(boton => {
        boton.addEventListener('click', leertarea, true);
    });

    botones_eliminar.forEach(boton => {
        boton.addEventListener('click', eliminartarea, true);
    });

    function leertarea(){
        var url = this.getAttribute('href')
        var myRequest=new Request(url)
        fetch(myRequest)
            .then(response => {
                return response.json()
            })
            .then(data => {
                document.querySelector("#editarForm input[name='titulo']").value = data[0]['titulo'];
                document.querySelector("#editarForm textarea[name='descripcion']").value = data[0]['descripcion'];
                document.querySelector("#editarForm select[name='prioridad']").value = data[0]['prioridad'];
                document.querySelector("#editarForm input[name='color']").value = data[0]['color'];
                document.querySelector("#editarForm input[name='f_deseada']").value = data[0]['f_deseada'];
                document.querySelector("#editarForm").action = "editarTarea/"+data[0]['id']

            })
            
}

    function eliminartarea(){
        var url = this.getAttribute('href')
        var myRequest=new Request(url)
        fetch(myRequest)
            .then(response => {
                return response.json()
            })
            .then(data => {
                document.querySelector("#eliminarForm span[name='tarea']").innerHTML = data[0]['titulo'];
                document.querySelector("#eliminarForm").action = "borrarTarea/"+data[0]['id']

            })
            
}
        



}





window.onload = botones;
