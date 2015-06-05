# -*- coding: utf-8 -*-
# Inits
from distutils.core import setup


# Infos
version = '0.1'
description = 'Fortran language extensions to sphinx'
long_description = "Fortran (90) language domain and auto-documenter for the Sphinx python documenter"
author = 'Actimar / IFREMER'
author_email = 'raynaud@actimar.fr'
maintainer = "Actimar / IFREMER"
maintainer_email = "raynaud@actimar.fr"
plateform = 'Linux/UNIX/BSD'
license="CeCiLL"
url="http://www.ifremer.fr/vacumm"
classifiers = ["Development Status :: 4 - Beta",
               "Intended Audience :: Science/Research",
               "License :: CeCiLL",
               "Programming Language :: Python :: 2",
               "Topic :: Scientific/Engineering :: Physics",
               "Topic :: Scientific/Engineering :: Mathematics",
               "Topic :: Scientific/Engineering :: Atmospheric Science",
               "Topic :: Software Development :: Libraries :: Python Modules",
               "Operating System :: POSIX",
               "Operating System :: UNIX",
               "Operating System :: MacOS :: MacOS X",
               ]

packages=[  'sphinxfortran' \
         ]
package_dir={  'sphinxfortran': 'sphinxfortran'\
              ,}



if __name__ == '__main__':

    # Lauch setup
    setup(name='sphinxfortran',
        version = version,
        description = description,
        long_description = long_description,
        author = author,
        author_email = author_email,
        maintainer = author,
        maintainer_email = author_email,
        license = license,
        url=url,
        classifiers = classifiers,
        packages = packages,
        package_dir = package_dir

    )



