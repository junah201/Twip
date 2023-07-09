from setuptools import setup, find_packages

README = open("README.md", 'r', encoding="utf-8").read()

setup(
    name='twip-api',
    version='1.0.0',
    description='Parses the things provided by twip such as donation, follow',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Junah201',
    author_email='junah.dev@gmail.com',
    url='https://github.com/junah201/Twip',
    install_requires=["websocket-client", "requests"],
    packages=find_packages(exclude=[]),
    keywords=['twip', 'twip.kr', 'twitch'],
    python_requires='>=3',
    license='MIT',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
