from setuptools import setup, find_packages

version = '1.0.0'

setup(name="helga-winks",
      version=version,
      description=('winks @ u'),
      classifiers=['Development Status :: 1 - Beta',
                   'Environment :: IRC',
                   'Intended Audience :: Twisted Developers, IRC Bot Developers',
                   'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: IRC Bots'],
      keywords='irc bot winks',
      author='michael orr',
      author_email='michael@orr.co',
      url='https://github.com/michaelorr/helga-winks',
      license='LICENSE',
      packages=find_packages(),
      include_package_data=True,
      py_modules=['helga-winks'],
      zip_safe=True,
      entry_points = dict(
          helga_plugins = [
              'winks= helga_winks:winks',
          ],
      ),
)
