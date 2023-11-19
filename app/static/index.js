$(document).ready(function(){
    $('.loader').hide();
    $("#submit").click(function(){
      var message = $("#message").val();
      $(".msg-wrap").append(format_message("You", message));
      $.ajax({
          type: "GET",
          url: "/query/" + message,
          beforeSend: function(){
              $('.loader').show();
              $("#message").val("")
          },
          success: function(response) {
              $('.loader').hide();
              $(".msg-wrap").append(format_message("ChatGPT", response));
           },
          error: function(xhr) {
              //Handel error
          }
        });
    });
});


function format_message(sender, text) {
    return "<div className='media msg'>" +
            "   <div className='media-body'>" +
            "       <h5 className='media-heading'>" + sender + "</h5>" +
            "       <small className='col-lg-10'>" + text + "</small>" +
            "   </div>" +
            "</div>" +
            "<br>"
}