from setuptools import find_packages
from setuptools import setup

setup(
    name="pycounts_lrh",
    version="0.1.0",
    description="Raster Map Handler Library",
    author="IO-Aero Team",
    author_email="info@aeronetica.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Library",
        "License :: IO-Aero",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="Raster Map, GDAL, Rasterio",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"io_raster": ["*.pyi", "py.typed"]},
    project_urls={
        "Bug Tracker": "https://github.com/io-aero/io-raster/issues",
        "Documentation": "https://io-aero.github.io/io-raster/",
        "Homepage": "https://github.com/io-aero/io-raster",
        "Release History": "https://io-aero.github.io/io-raster/release_history/",
        "Release Notes": "https://io-aero.github.io/io-raster/release_notes/",
        "Source": "https://github.com/io-aero/io-raster",
    },
    python_requires=">=3.10",
    url="https://github.com/io-aero/io-raster",
)

