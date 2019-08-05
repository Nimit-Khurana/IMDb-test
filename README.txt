WORKFLOW OF A FLASK PROJECT--
	* creating a hello world flask app
	* creating a py script to get data from imdb api
	* integrate above steps to run on route '/'
	* movie name as user input in search bar search parameter
	* creating a bootstrap loaded html page and rendered it in flask
	* defining a search bar that takes in the movie name as search parameter instead of
	  adding manually in the url
	* add jquery and ajax to handle the request
	* add jquery dom maipulation and css for the results
	* deploy it to a server
--------------------------------------------------------------------------------------------
What you get to learn throughout--
    Know how HTML CSS and JS works for getting familiar with bootstrap.
    How APIs work(HTTP methods).
    Work in a virtual environment (venv)
    Using Git.
        GIT comms to push commits--
        check the status: git status
        track and stage a single file: git add [filename]
        track and stage all files: git add .
        commit with a message: git commit -m "description of commit"
        view the log: git log
        push changes: git push [remotename] [branchname]
    Server handling

    <==>Issues faced in api response-->
        *Use only IMDb api not any other. Using that gives a JSON-p response.
        *You need to create templates and static folders in your project folder, put all .html
         files in templates folder and all other files (CSS, JS, JPG, etc) in static folder
         and then in your html. file use url_for to load the static files, instead of the
         default HTML way i.e bootstrap looks into templates folder for user templates 'by
         default' and in static folder for all other files.
    Here in this project-->
    -imdb
        flaskk.py
        script.py
        venv/
        - templates
            |strap.html
        -static
            -css
              |style.css
            -js
              |main.js
            -img
              |example.jpg



    Know AJAX--
    AJAX is a technique for creating better, faster, and more interactive web applications with the help of XML, HTML, CSS, and Java Script.
    XML is commonly used as the format for receiving server data, although any format, including plain text, can be used.
    With AJAX, when you hit submit, JavaScript will make a request to the server, interpret the results, and update the current screen.
    In the purest sense, the user would never know that anything was even transmitted to the server.
    Ajax is a technique for creating interactive web applications.

    jquery and flask (link="https://www.w3schools.com/jquery/jquery_intro.asp")
        With the jQuery AJAX methods, you can request text, HTML, XML, or JSON from a remote
        server using both HTTP Get and HTTP Post - And you can load the external data directly
        into the selected HTML elements of your web page!
        jQuery is a fast, small, and feature-rich JavaScript library. It makes things like
        HTML document traversal and manipulation, event handling, animation, and Ajax much
        simpler with an easy-to-use API that works across a multitude of browsers. With a
        combination of versatility and extensibility, jQuery has changed the way that millions
        of people write JavaScript.
        link="https://www.youtube.com/watch?v=vtiiO5I90Tc"

    jquery---passing form data to a variable and appending it to a <p> tag.
        link="https://stackoverflow.com/questions/42078242/store-html-form-data-in-js-variable
	-using-jquery-serializearray"

    DOM (Document Object Model)
        link="https://www.w3.org/TR/WD-DOM/introduction.html"
        link="https://www.tutorialsteacher.com/jquery/jquery-dom-manipulation"

    <==>Learn in-browser editing html and css-->
	localhost cache
	browser console

    Server handling(ubuntu)--
        server is of 2 types: physical and application server(flask, django, ssh, etc)
        To check all kinds of ports, their services and protocols: less /etc/services or grep
        buy a server and ssh into it: ssh root@<ip addr> -p <port>
                        (-p if listening port changed)
        add a user
        make it a sudoer: useradd -aG <name>
        change the listening port of the ssh server: vi /etc/ssh/sshd_config
            find port 22, uncoment and replace it with the port not running service(p575)
            check if firewall activated..
            change firewall settings and restart the sshd server and firewall.
            upadte firewall to accept ssh port<name>: sudo ufw allow <name>/protocol
        There are 2 ways to authenticate sshing into a server- password and ssh key.
            check in /etc/ssh/sshd_config file for PubkeyAuthentication and
            PasswordAuthentication and change their values accordingly.

        installing nginx
        'a records' in DomainNameSystem.
            now create nameserver on domain host's website to create your URL.
    link="https://medium.com/@jgefroh/a-guide-to-using-nginx-for-static-websites-d96a9d034940"
        push your files to the server and run your flask app at 0.0.0.0:80 in tmux.
        Why tmux?  tmux creates a session and not ends it when you log out of your server or
               close your terminal unless tmux is ended.
        <==>Issues faced when starting app-->
            1.) flask wont run as a user on port 80, which is universal port for listening
                default port for flask is 5000
            2.) app won't run on root user at port 80
                link="https://github.com/pallets/flask/issues/1756"

        install TMUX on server and push the directory on server.
        virtual host in linux


Tricks-->
	ctrl + shift + r in browser to load page w/o cache.
	jquery .one() method to limit number of clicks.
