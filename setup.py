import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012023S1LDO1',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description="# The Amending Order Tool\r\n\r\nThe Amending Order Tool was created by Flinders University Students in collaboration with the Legislative Drafting Office of Jersey, to assist their drafters with creating 'Amending Orders' - the official documents that codify amendments to legislation.\r\n\r\n## Key Features\r\n\r\n* Utilises the Legislative Drafting Office's standard amending language to prepare textual amendments to existing legislation, including the simple insertion, deletion or substitution of text. \r\n* Generates Amending Orders that adhere to the legal formatting required by the Government of Jersey, and contain the amendments entered by the user. \r\n* Minimises the occurrence of human error and inconsistencies within Amending Orders.\r\n* Reduces the time required to draft Amending Orders. \r\n\r\n## Authors\r\nIsabella Trigwell\r\nJames Tsiounamis\r\nSophia Zachos\r\nSumedha Mujamadar \r\n\r\n",
      long_description_content_type='text/markdown',
      author='Isabella Trigwell',
      author_email='trig0040@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012023S1LDO1/', package='docassemble.LLAW33012023S1LDO1'),
     )

