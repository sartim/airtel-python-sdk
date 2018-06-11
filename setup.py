from setuptools import setup

long_description = "Airtel API REST SDK with suscription, payments integration"

setup(name='Airtel API SDK',
      version='0.1',
      description='M-Pesa API SDK',
      url='https://github.com/sartim/airtel-python-sdk',
      author='sartim',
      author_email='***REMOVED***',
      license='MIT',
      packages=['mpesa'],
      install_requires=['requests', ],
      dependency_links=['https://github.com/sartim/airtel-python-sdk/master#egg=package-1.0'],
      zip_safe=False
      )
