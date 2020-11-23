$(document).ready(function() {
    var callback = function() {
        var inputValue = $("#user-query-input").val();

        // Output the value

        $.ajax({
            'type': "GET",
            'url': "/twitterJsonDataEndpoint?query=" + inputValue,
            contentType: 'application/json;charset=UTF-8',
            beforeSend: function() {},
            success: function(response) {

                const data = JSON.parse(response);
                //console.log(response);
                // debug**
                //console.log(typeof(data));
                console.log(data['data']['followers']);

                d = data['data']
                const id = d['id'];
                const name = d['name'];
                const username = d['username'];
                const description = d['description'];
                const profileImage = d['profile_image_url'];
                const entities = d['entities'];
                const url = entities['url']['urls'][0]['expanded_url'];
                const publicMetrics = d['public_metrics'];
                const followers = publicMetrics['followers_count'];
                const following = publicMetrics['following_count'];
                const tweets = publicMetrics['tweet_count'];
                const ifVerified = d['verified'];
                const myHtml = "<h3 style='color:black;text-align:center'>Your Search Results..</h3><div class='search-result-flex'><div style='width: 20%;background-color: #182430;display:flex;flex-direction:column;justify-content: center;text-align:center;'><p><img style='width:64px;height:64px;border-radius:50%;'src='" + profileImage + "'></p><h4>" + name + "</h4><p>Verified: " + ifVerified + "</p></div><div style='display:flex;flex-direction:column;width: 40%;background-color: #AAB8C2;'><div style='color:black;padding:10px;'><strong>" + description + "</strong></div><div style='display:flex;justify-content:center;color:black'><div style='margin:20px;display:flex;flex-direction:column;justify-content:center;'><p style='color:#1da1f2;line-height:1px;'>" + followers + "</p><p>Followers</p></div><div style='margin:20px;display:flex;flex-direction:column;justify-content:center;'><p style='color:#1da1f2;line-height:1px;'>" + following + "</p><p>Following</p></div><div style='margin:20px;display:flex;flex-direction:column;justify-content:center;'><p style='color:#1da1f2;line-height:1px;'>" + tweets + "</p><p>Tweets</p></div></div></div><div style='width: 40%;background-color: #182430;'><p>tweets</p></div></div>"
                console.log(myHtml);
                if (data) {
                    $('#search-result').append(myHtml);
                }
            },
            complete: function() {
                $(".loading-div").hide();
                $('html, body').animate({
                    scrollTop: $("#search-result").offset().top
                }, 2000);
            }
        })

        $("#user-query-input").val("");
    };
    $(".twitter-search").click(callback);
});