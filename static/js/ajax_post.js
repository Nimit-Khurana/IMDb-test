$(document).ready(function () {
         var callback = function() {
            $('.card').remove();
            var inputValue = $("#query_input").val();

    		// Output the value

    		$.ajax({
				  'type': "GET",
                  'url': "/moviejson?query=" + inputValue,
			   	   success: function(response) {
					   console.log(response)
                            }
                        })
            $("#query_input").val("");
         };

         $('#ajax_button').click(callback);
});
