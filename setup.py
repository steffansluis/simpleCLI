from distutils.core import setup
setup(
	name="simpleCLI",
	version="0.1",
	author="Steffan Sluis",
    url='http://github.com/steffansluis/simpleCLI',
	author_email="steffansluis@gmail.com",
	license="MIT",
	packages=["simpleCLI"],
	data_files=[('/usr/bin/', [
	])],
	install_requires=[
		"argparse",
		"argcomplete",
		
	],
)