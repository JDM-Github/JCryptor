import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='JCryptor',
    version='0.1',
    scripts=['jcryptor'],
    author="CodeBoard",
    author_email="jdmaster888@gmail.com",
    description="JCryptor: The Encryptor and Decryptor Module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ScripNewbie/JCryptor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
)
