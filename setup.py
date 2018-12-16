from setuptools import setup

setup(name='neatocontrols',
      version='0.9',
      description='A GUI for controlling your Neato Robotics device. Based on pybotvac',
      classifiers=[
      	'Environment :: X11 Applications',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: English',
        'Topic :: Home Automation'
      ],
      keywords='neat neato cli robotics botvac neatocontrols pybotvac',
      url='http://github.com/MIQUELLIONEL/neatocontrols',
      author='Miquel Lionel',
      author_email='lionelmiquel@sfr.fr',
      license='GPLv3.0',
      packages=['botvac'],
      include_package_data=True,
      install_requires=[
          'pybotvac',
          'docopt==0.6.2',
      ],
      zip_safe=False)
