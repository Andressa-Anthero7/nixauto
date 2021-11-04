function exibir_ocultar(){
        var valor = $("#id_tipo").val();
        if(valor == 'carro'){
             $("#id_portas").show();

         }
          else {
             $("#id_portas").hide();
         } 
       };