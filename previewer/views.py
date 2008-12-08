# Create your views here.
from django.views.generic.simple import direct_to_template
from django.conf import settings
import yaml

special = ['_extends']

class FixError(Exception): pass

def get_fixes(the_yaml, template):
    """
    Return a dictionary populated from the_yaml (which may be anything
    that yaml.load will accept).
    """
    fixes = yaml.load(the_yaml)
    context = {}
    try:
        our_fixes = fixes[template]
    except (KeyError, TypeError):
        return context
    else:
        try:
            inheritance_list = our_fixes['_extends']
        except KeyError:
            pass
        else:

            if isinstance(inheritance_list, (unicode, str)):
                inheritance_list = [inheritance_list]
            for ancestor in inheritance_list:
                if ancestor == template:
                    raise FixError, "Cyclical inheritance in %s" % template
                try:
                    context.update(fixes[ancestor])
                except KeyError:
                    raise FixError, "You are trying to inherit from a fixture that does not exist: %s" % ancestor
        context.update(our_fixes)
        for x in special:
            try:
                del context[x]
            except KeyError:
                pass
    return context


def template_with_fix(request, template, extra_context=None, mimetype=None, **kwargs):
    """
    Works like django.views.generic.simple.direct_to_template except
    that the context is updated by the data found in the file whose
    name is stored in the setting TEMPLATE_FIX. If there's no such
    setting, the context is left alone.
    """
    if extra_context is None:
        extra_context = {}
    fixed = extra_context.update(get_fixes(open(settings.TEMPLATE_FIX), template))

    return direct_to_template(request, template, extra_context, mimetype, **kwargs)

