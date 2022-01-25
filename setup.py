from setuptools import setup, find_packages
 
setup(
    name                = 'Twip',
    version             = '0.0.1',
    description         = 'parses the things provided by twip such as donation, follow',
    author              = 'Junah201',
    author_email        = 'junah.dev@gmail.com',
    url                 = 'https://github.com/junah201/Twip',
    install_requires    =  ["websocket", "requests"],
    packages            = find_packages(exclude = []),
    keywords            = ['twip', 'twitch'],
    python_requires     = '>=3',
    # 파이썬 파일이 아닌 다른 파일을 포함시키고 싶다면 package_data에 포함시켜야 합니다.
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)