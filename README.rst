=========================
Django Template Previewer
=========================

The Django template language is really great. However, it is not so
easy for a Designer to use it for prototyping, because in order to see
the templates rendered you need a functioning Django project. This may
not be practical for several reasons:

 * The designer may be using an OS not supported by a library on which
   the project depends on.

 * Bugs in the model and view code will scare the designer.

 * The designer will be at times blocked by the programmer.

 * etc.

Django Template Previewer tries to solve some of these problems:

 * You can browse a list of available templates

 * Fully render a template, with inheritance and stuff

 * Populate the context of the template with some mock data (which is
   stored in a YAML file).

 * You can do all this without any serious knowledge of Python (and
   the installation is quite straightforward).


-------------------------
Installation
-------------------------

 $ python previewer/setup.py install

or

 $ easy_install previewer

The latter will also take care of the dependencies (at the moment,
only PyYAML).

Alternatively, you can just copy the folder ``previewer`` someplace
Python will be able to see it.

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

).
------------
Template fix
------------

A template fix is simply a YAML file which contains a mapping between
template files and the context we want to pass them. For example:::

    404.html:
      _inherits:
        - blog/base.html
        - foo
      domain: example.com
      text: we are very sorry

    500.html:
      _inherits:
        - 404.html
      v: 2

    blog/base.html:
       c: c
       d: d

If a template file name is not included in this mapping, it will be
passed an empty dictionary as additional context. Each file may have a
magical property, ``_inherits``. It should contain a list of file
names (though the app will try to do The Right Thing if you give it
just a string). The context will be augmented with values from all the
ancestors. Values from defined explicitly always take precedence over inherited values.

Note that not all fields must have keys naming existing files. It
would be perfectly OK to have a field named ``"error"`` or something
like that, just for inheritance.

--------
Usage
--------

Just browse the url under which you included the url
configuration. Choose a template you want to see and click it.