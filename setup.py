from setuptools import setup,find_packages

install_requires = [
    'boto3>=1.5.0',
    'jmespath>=0.7.1,<1.0.0',
    'termcolor>=1.1.0',
    'python-dateutil>=2.4.0'
]

setup(
    name='dpa-awslogs',
    version='0.1.0',
    url='https://github.com/xinhuagu/dpa-awslogs',
    author='Xinhua Gu',
    author_email='xinhua.gu@gmail.com',
    license='LICENSE.txt',
    description='aws logs dump and analytics tool',
    long_description=open('README.md').read(),
    packages=find_packages(),
    platforms='any',
    python_requires=">=3.5.*",
    install_requires=install_requires,
    test_suite='tests',
    entry_points={
        'console_scripts': [
           'dumplogs=dumplogs.bin:main',
        ],
    },
    zip_safe=False
)
