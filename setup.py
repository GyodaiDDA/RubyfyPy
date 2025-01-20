from setuptools import setup, find_packages

setup(
    name="RubyfyPy",
    version="0.1.0",
    packages=find_packages(),
    description="Ruby-like methods for Python objects",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Gyodai",
    author_email="rodrigo.gyodai@gmail.com",
    url="https://github.com/GyodaiDDA/RubyfyPy",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
