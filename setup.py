from distutils.core import setup 
import py2exe 
 
setup(name="Calcula Diego Sentanda", 
 version="1.0", 
 description="Solamente calcula", 
 author="Erickkkkk", 
 author_email="nope", 
 url="nope", 
 license="Erick Copyright", 
 scripts=["calculadora.py"], 
 console=["calculadora.py"], 
 options={"py2exe": {"bundle_files": 1}}, 
 zipfile=None,
)