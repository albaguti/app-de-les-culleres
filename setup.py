from setuptools import find_packages, setup

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='app-de-les-culleres',
      version="1.0",
      description="Programa de suport per analitzar comportaments i els seus resultats",
      packages=find_packages(),
      install_requires=requirements,
      test_suite='tests',
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      zip_safe=False)
