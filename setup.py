import setuptools

setuptools.setup(
    name="jurasol",
    version="0.1",
    author="Solène Ulmer-Moll",
    author_email="solene.ulmer-moll@astro.up.pt",
    description="Plot RV curves",
    packages=setuptools.find_packages(),
    install_requires = ["numpy","matplotlib"],
    classifiers=["Programming language :: Python :: 3"],
)
