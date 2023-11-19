$(document).ready(function(){
    $("#submit").click(function(){
      var message = $("#message").val();
      $("#messages").append("<li>" + message + "</li>");
      $.ajax({
          type: "GET",
          url: "/query/" + message,
          success: function(response) {
            console.log(response);
            $("#answers").append("<li>" + response + "</li>");
           },
          error: function(xhr) {
              //Handel error
          }
        });
    });
});


