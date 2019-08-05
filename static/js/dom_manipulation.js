$(document).ready(function () {
         var callback = function() {
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

                        // looping through items in 'response' object which is a list of objects here..
                        for(i=0;i<data.length;i++) {
                            const imdblink = "https://www.imdb.com/title/" + data[i]['id']
                            const movieposter = data[i]['image']
                            const moviename = data[i]['name']
                            const myHtml = "<div class='card'><img alt='No image available' class='poster' src='"+movieposter+"' ><a target='_blank' href='"+imdblink+"'><p id='card_p' style='text-align:center;'>"+moviename+"</p></a></div>";
                            // console.log(typeof(myHtml));
                            if (data) {
                                $('#main_div').append(myHtml);
                            }
                        }
				   }
            })
         };

         $('#ajax_button').one('click',callback);

         // check connection status...
         setTimeout(()=> {
         if (navigator.onLine) {
            $('#connect').append("<span class='dot'></span>");
        }
        else { 
            $('.dot').remove();
            $('#connect').append("Offline"); 
        }
        },3000 );
});