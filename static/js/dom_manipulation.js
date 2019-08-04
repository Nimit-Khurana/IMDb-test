$(document).ready(function () {

		 $('#ajax_button').click(function(){
			var inputValue = $("#query_input").val();

    		// Output the value

    		$.ajax({
				  'type': "GET",
				  'url': "/about?query=" + inputValue,
			   	   success: function(response) {
                        const data = JSON.parse(JSON.parse(response));
                        // debug
                        console.log(typeof(data));
                        console.log(data[0]);

                        // looping through items in 'response' object which is a list of dicts here..
                        for(i=0;i<data.length;i++) {
                            const myHtml = "<div class='card'>" + "<a href='https://www.imdb.com/title/" + data[i]['id'] + "'><img class='poster' src='"+ data[i]['image'] +"' ></a>" + "<p style='text-align:center;'>"+data[i]['name']+"</p></div>";
                            // console.log(typeof(myHtml));
                            if (data) {
                                $('#main_div').append(myHtml);
                            }
                        }
				   }
			});
         });
});