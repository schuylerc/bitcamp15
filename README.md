# bitcamp15
Our BitCamp project for 2015!

## Deploy Webapp

Execute the following

    $ cd django-docker-starter
    $ vagrant up
    $ vagrant ssh
    $ cd /srv/www
    $ sudo su
    # docker-compose up
    # docker-compose run web python manage.py migrate

## Mobile Application

Execute the following

    $ cd mobile
    $ npm install -g bower
    $ cd www
    $ bower install bower.json

You can now see your changes in the browser by executing the following command
and visiting [http://localhost:8000](http://localhost:8000)

    $ python -m SimpleHTTPServer

Once you are ready, you can build an Android app by executing the following
code

    $ cordova build android
