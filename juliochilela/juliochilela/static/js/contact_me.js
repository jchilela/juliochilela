function submeter(){
  $(function(){

            var name = document.getElementById("name").value;
            var email =document.getElementById("email").value;
            var phone = document.getElementById("phone").value;
            var message = document.getElementById("message").value;
            var hoje = Date();

alert("Thank you");

            
    $.ajax({
      type: "POST",
      url: 'http://52.89.105.19/contact_me.php',
      data: ({name: name, email: email, phone: phone, message: message, hoje: hoje}),
      success: function(data) {
       
      }

    });
  });

limpar();
}

function limpar(){
document.getElementById("name").value="";
document.getElementById("email").value="";
 document.getElementById("phone").value="";
 document.getElementById("message").value="";


}