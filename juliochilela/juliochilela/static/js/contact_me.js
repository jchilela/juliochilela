function submeter(){
  $(function(){

            var name = document.getElementById("name").value;
            var email =document.getElementById("email").value;
            var phone = document.getElementById("phone").value;
            var message = document.getElementById("message").value;


alert(name);
            
    $.ajax({
      type: "POST",
      url: 'http://localhost/contact_me.php',
      data: ({name: name, email: email, phone: phone, message: message}),
      success: function(data) {
        alert(data);
      }

    });
  });

alert("Saved")

}