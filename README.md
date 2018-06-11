# DressCode

### Run Instructions

#### Dependencies:
- Install Python3 (https://www.python.org/downloads/)
- Install Django (https://www.djangoproject.com/download/)
  - Developed on Django 2.0.5
- Install ActivityStream (http://django-activity-stream.readthedocs.io/en/latest/installation.html)
> pip install django-activity-stream
- Install Django-Notifications (https://github.com/django-notifications/django-notifications)
> pip install django-notifications-hq
- Instal Django Rest Framework (http://www.django-rest-framework.org/)
> pip install djangorestframework

#### Run Development Server (Linux, probs similar for windows)
1. Clone the repo
2. Open a terminal in the root directory
> $ python manage.py runserver
3. Assuming no errors in console, open a browser
4. Navigate to "localhost:8000"

All subdirectories are available on port 8000

### File Structure (front-end themed)

#### Top Level Directory (root, src):
This holds the SQLite database (holds users, all site data). You'll also see 'manage.py' which is how you manage the project (see how to run the server above). Lastly and most importantly, you'll see the "accounts" app.

#### Accounts, Design (and any django app)
You see quite a few files in here, I'll keep it limited to what's front-end relevant.

Starting as far toward the back-end as necessary, you might want to take a peek at "views.py". This is where I define which HTML templates are associated with which views (like /index, /account/register, whatever).

"Forms.py" is where I define some custom forms to use in the HTML templates. I don't understand it yet, but it makes creating complicated HTML forms super easy.

The most relevant section is the "Templates" subdirectory.

#### Templates subdirectory

This is where the actual HTML templates are stored. In the top level of /templates you'll see "base.html". You'll want to read up on "Django Templating", watch a couple of Youtube Videos on it. It's not too complicated, just gotta figure the syntax out. In a couple of sentences, "base" defines the basic structure that the entire website will follow. For instance, when we have a navigation bar, that will be in base.html so that it's displayed identically on every page. In "base", you'll also see that I defined two blocks, the "head" and "body" blocks.

To design the actual pages (found under /templates/accounts), all you have to do is define the HTML that will replace the "head" and "body" blocks in "base.html". A good example is in /templates/accounts/home.html. You can see that it _extends base.html_, or in other words it's going to use the Base template. Then, all I do after that is define a Title in the _head_ block, and some content in the _body_ block. Home is also a good example because it shows how you can use the template language to give dynamic content (shows something different when the user is logged out vs logged in).



## Run Instructions
1. Start dev server:
$ python manage.py runserver
2. If you wish to use the password reset, start a local SMTP server on port 1025
$ python -m smtpd -n -c DebuggingServer localhost:1025


