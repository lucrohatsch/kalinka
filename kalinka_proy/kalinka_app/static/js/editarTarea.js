
function cargarForm(){
    botones = document.querySelectorAll("a[data-toggle='modal']");

    botones.forEach(boton => {
        boton.addEventListener('click', leertarea, true);
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


        



}





window.onload = cargarForm;
