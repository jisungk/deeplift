from distutils.core import setup

if __name__== '__main__':
    setup(include_package_data=True,
          description='Interpretable deep learning',
          url='NA',
          download_url='NA',
          version='0.3',
          packages=['deeplift'],
          setup_requires=[],
          install_requires=['numpy>=1.9', 'theano>=0.8'],
          scripts=[],
          name='deeplift')
