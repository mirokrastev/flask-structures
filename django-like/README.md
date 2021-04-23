# Django-like
This is a project structure similar to the Django framework.<br>
<br><hr>
This is a walkthrough of how Flask is started:
  - Flask Apps are defined by creating a new python package.<br>
  Every Flask App will need to have this code inside ```__init__.py``` to work:
  ```python
  from flask import Blueprint
  
  <app>_bp = Blueprint('<app>', __name__)
  
  from <app> import urls
  ```
  where ```app``` is your Flask App name (python package)
  
  * Instance of Flask is created in ```app.py```
  * ```settings.py``` is importing the instance
    * It's importing every Flask App blueprint
    * The keys in ```apps``` dict could be changed to be variables, but I like it like that
      * One key-pair is holding the Flask App name and lambda function with optional kwargs.<br>
    * In ```urlpatterns``` you can config paths that are not bond to any app.<br>
      Also you need to call the lambda functions (your apps that you have declared) from the ```apps``` dict to register them (to be valid Flask code)
      * You can give url_prefix kwarg argument to imitate ```include()``` function in Django
