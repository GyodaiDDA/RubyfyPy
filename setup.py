from setuptools import setup, find_packages

setup(
    name="RubyfyPy",
    version="0.1.0",
    packages=find_packages(),
    description="Ruby-like methods for Python objects",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Gyodai",
    author_email="rodrigo.gyodai@gmail.com",
    url="https://github.com/GyodaiDDA/RubyfyPy",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.x",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.3",
    extras_require={
        "dev": ["pytest>=8.3.4"],
    },
)
