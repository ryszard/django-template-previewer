=========================
Django Template Previewer
=========================


-------------------------
Installation
-------------------------

 $ python setup.py install

... or just copy the folder `previewer` someplace Python will see it.

-------------------------
Settings
-------------------------

You should should add "previewer" to your INSTALLED_APPS set
TEMPLATE_FIX to the path where you want to keep the fixtures for your
templates (for example
'/Users/richard/Projects/template_viewer/template_fix.yaml')

-----------------
Url configuration
-----------------

Include previewer.urls under a sensible prefix in the urls.py file of
your project (I use the prefix templates, so my urls.py looks like
::
    urlpatterns = patterns('',
                       ...
                       ('templates', include('template_viewer.previewer.urls')),
                       ...
                       )