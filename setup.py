from distutils.core import setup

pack_name='pyconstants'
pack_version='0.4'
pack_description='Important physical constants'
pack_author='Simon Zeller, Adrian Schlatter'

setup(	name=pack_name,
	version=pack_version,
	description=pack_description,
	author=pack_author,
	py_modules=[ 'constants' ], )

