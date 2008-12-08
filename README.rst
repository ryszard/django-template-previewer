=========================
Django Template Previewer
=========================

The Django template language is really great, but the life of a
template designer isn't so easy. In order to be able to view if her
newly designed template set is working, she must have

 * A working Django installation

 * A correctly setup and working Django project (which means having
   views putting correct types of objects in the context, etc.).

Not much can be done about the former problem, but the second one
should be fairly easy to deal with, and this is the aim of this
project. It consists in its main part of a view allowing to render
templates with the context populated with data from a yaml file.

-------------------------
Installation
-------------------------

 $ python setup.py install

... or just copy the folder ``previewer`` someplace Python will be
able to see it.

-------------------------
Settings
-------------------------

You should should add ``previewer`` to your ``INSTALLED_APPS`` and set
``TEMPLATE_FIX`` to the path where you want to keep the fixtures for
your templates (for example
``"/Users/richard/Projects/template_viewer/template_fix.yaml"``)

-----------------
Url configuration
-----------------

Include ``previewer.urls`` under a sensible prefix in the urls.py file of
your project (I use the prefix templates, so my ``urls.py`` looks like

::

    urlpatterns = patterns('',
                       ...
                       ('templates', include('template_viewer.previewer.urls')),
                       ...
                       )

More to come...