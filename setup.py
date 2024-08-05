from setuptools import setup, find_packages

setup(
    name='tube-saverx',
    version='1.0',
    author='Wuhan Raccoon Network',
    author_email='xhxdeveloper@163.com',
    description='A shortvideo parse download support 1000+ site',
    url="https://skylands.cn",
    packages=find_packages(),
    python_requires='>=3.9',
    install_requires=[
        'fastapi',
        'requests',
        'networking',
        'parsel',
        'lxml',
        'PyExecJS',
        'redis',
        'ffmpeg',
    ],
)

