DEPLOYER
========

### This webdeployer allows you to deploy fast and easy to your webserver.
Automate deployments of your webapps using :

-   GUNICORN
-   NGINX
-   SUPERVISORD

You need to use a directory format like : ```/projects/client/client_name/project/source```

requirements :
- Python 2.7
- Fabric
- Jinja2


On your server you need to have already installed and running:
-   nginx
-   gunicorn(not realy only you need to have the package installed)
-   supervisord


This is being set free from Private so it may take time to free out all the mess from my private repo


TO INSTALL
==========

```
pip install webdeployer
```

to initialize your project :
go into your project dir and type the following command : `webdeployer init`

a folder named "webdeployer-config" will be created in your project dir
edit the file project-config inside that dir

example :
```
[Settings]
# for now only python
project_language = "python"
# for now only django or flask
project_framework = "flask"
client_name = "Royendgel Silberie"
project_name = "Website"
app_name = "Website"
"""
 The directory_server var is for setting the
 if you leave directory empty it will be something like /projects/client_name/app_name/source/
"""
directory_server = ""

servers = ["sweet.techprocur.com"]
server_uses_password = False
server_password ""
# change this to the correct user if you don't know usualy you are using root as login change it
server_user_name = "website"
```



If you are deploying for the first time :
go in your project directory and type : webdeployer init

edit the webdeployer-config.py

then type webdeployer deploy

MILESTONE/ROADMAP

- I want to make it more customizable
- make use of chef-solo to deploy to all os with dependecies
- want to make it usable for : rails, php , wordpress, unicorn , apache, passanger, uswsgi etc
- make an option that users can store settings global