"""
>>> fixtures = '{404.html: {a: "a", b: "b"}}'

>>> get_fixes(fixtures, '404.html') == {'a': 'a', 'b': 'b'}
True

>>> fixtures = '{404.html: {a: "a", b: "b", _inherits: base.html}, base.html: {c: "c"}}'

>>> get_fixes(fixtures, '404.html') == {'a': 'a', 'b': 'b', 'c': 'c'}
True

>>> fixtures = '{404.html: {a: "a", b: "b", _inherits: base.html}}'

>>> get_fixes(fixtures, '404.html')
Traceback (most recent call last):
  ...
FixError: You are trying to inherit from a fixture that does not exist: base.html

>>> fixtures = '{404.html: {a: "a", c: "c", _inherits: base.html}, base.html: {c: "cccccc"}}'

>>> get_fixes(fixtures, '404.html') == {'a': 'a', 'c': 'c'}
True

>>> fixtures = '{404.html: {a: "a", b: "b", _inherits: [base.html, d.html]}, base.html: {c: "c"}, d.html: {d: "d"}}'

>>> get_fixes(fixtures, '404.html') == {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd'}
True

>>> get_fixes('{a: {_inherits: a}}', 'a')
Traceback (most recent call last):
   ...
FixError: Cyclical inheritance in a

>>> get_fixes('', 'a')
{}

"""
from views import get_fixes

