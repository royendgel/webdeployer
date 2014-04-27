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
client_name = "Techpro And Services N.V."
project_name = "blog app"
app_name = "blog app"
directory = ""
servers = ["sweet.techprocur.com"]
```



If you are deploying for the first time :
go in your project directory and type : webdeployer init

edit the webdeployer-config.py

then type webdeployer deploy

MILESTONE/ROADMAP

- I want to make it more customizable
- make use of chef-solo to deploy to all os with dependecies
- want to make it usable for : rails, php , wordpress, unicorn , apache