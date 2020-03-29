$(document).ready(function() {
    var callback = function() {
        var inputValue = $("#query_input").val();
        $('.card').remove();
        $(".loading-div").show();

        // Output the value

        $.ajax({
            'type': "GET",
            'url': "/moviejson?query=" + inputValue,
            contentType: 'application/json;charset=UTF-8',
            beforeSend: function() {},
            success: function(response) {

                const data = JSON.parse(JSON.parse(response));
                //console.log(response);
                // debug**
                //console.log(typeof(data));
                //console.log(data[0]);

                // looping through items in 'response' object which is a list of objects here..
                for (i = 0; i < data.length; i++) {
                    const imdblink = "https://www.imdb.com/title/" + data[i]['id']
                    const movieposter = data[i]['image']
                    const moviename = data[i]['name']
                    const myHtml = "<div class='card'><img class='poster' src='" + movieposter + "' src='static/img/noimage.jpg'><a target='_blank' href='" + imdblink + "'><p id='card_p' style='text-align:center;color:white;'>" + moviename + "</p></a></div>";
                    // console.log(typeof(myHtml));
                    if (data) {
                        $('#main_div').append(myHtml);
                    }
                }
            },
            complete: function() {
                $(".loading-div").hide();
                $('html, body').animate({
                    scrollTop: $("#main_div").offset().top
                }, 2000);
            }
        })

        $("#query_input").val("");
    };
    $("#ajax_button").click(callback);
});