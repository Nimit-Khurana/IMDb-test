$(document).ready(function () {
         var callback = function() {
            var inputValue = $("#query_input").val();
	    if(inputValue.length == 0) {
		    $('.required').show();
		    return;
	    }
	    $('.card').remove();

    		// Output the value

    		$.ajax({
                    'type': "GET",
                    'url': "/moviejson?query=" + inputValue,
                    contentType:  'application/json;charset=UTF-8',
                    beforeSend: function() {
                    },
			   	    success: function(response) {
					    console.log(response);
                        const data = JSON.parse(JSON.parse(response));
                        // debug**
                        //console.log(typeof(data));
                        //console.log(data[0]);

                        // looping through items in 'response' object which is a list of objects here..
                        for(i=0;i<data.length;i++) {
                            const imdblink = "https://www.imdb.com/title/" + data[i]['id']
                            const movieposter = data[i]['image']
                            const moviename = data[i]['name']
                            const myHtml = "<div class='card'><img alt='No image available' class='poster' src='"+movieposter+"' ><a target='_blank' href='"+imdblink+"'><p id='card_p' style='text-align:center;color:white;'>"+moviename+"</p></a></div>";
                            // console.log(typeof(myHtml));
                            if (data) {
                                $('#main_div').append(myHtml);
                            }
                        }
                   },
                    complete: function() {
                        $(".loading-div").show().delay(500).fadeOut('slow');
                        $('html, body').animate({
                            scrollTop: $("#main_div").offset().top
                          }, 2000);
			$('.required').hide();

                    }
            })
                
            $("#query_input").val("");
         };

         $('#ajax_button').click(callback);
});
