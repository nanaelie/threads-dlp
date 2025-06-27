from setuptools import setup, find_packages

import re

def get_version():
    with open("threads_dlp/__version__.py", "r") as f:
        content = f.read()
    version_match = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Version not found")

setup(
    name='threads-dlp',
    version=get_version(),
    author='nae.devp',
    author_email='nae.devp@gmail.com',
    description="Téléchargeur de vidéos Threads (Meta) en ligne de commande",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nanaelie/threads-dlp',
    project_urls={
        "Source": "https://github.com/nanaelie/threads-dlp",
        "Bug Tracker": "https://github.com/nanaelie/threads-dlp/issues",
        "Documentation": "https://github.com/nanaelie/threads-dlp#readme",
    },
    packages=find_packages(),
    install_requires=[
        'requests',
        'selenium',
        'tqdm',
        'dottify',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Multimedia :: Video",
        "Intended Audience :: Developers",
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'threads-dlp=threads_dlp.cli:main',
        ],
    },
    license="Apache-2.0",
    include_package_data=True,
)

