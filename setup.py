#from ez_setup import use_setuptools
#use_setuptools()
from setuptools import setup, find_packages

setup(name="DjangoTemplatePreviewer",
      version="0.1",
      description="Django app making life easier for template designers.",
      long_description="""

""",
      author="Ryszard Szopa",
      author_email="ryszard.szopa@gmail.com",
      url="http://sample.host/mypackage.html",
      packages=['previewer'],
      install_requires=['pyyaml'],
      )
