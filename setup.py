import os
import sys
import re
from setuptools import setup, Extension, dist

# --- Ensure NumPy is available ---
try:
    import numpy as np
except ImportError:
    dist.Distribution().fetch_build_eggs(['numpy'])
    import numpy as np

# --- Optional Cython compilation ---
cmdclass = {}
try:
    from Cython.Distutils import build_ext
    cmdclass = {'build_ext': build_ext}
    use_cython = True
except ImportError:
    use_cython = False

# --- Define extensions ---
if use_cython:
    ext_modules = [
        Extension(
            "tfcomb.counting",
            ["tfcomb/counting.pyx"],
            include_dirs=[".", np.get_include()]
        )
    ]
else:
    if os.path.exists("tfcomb/counting.c"):
        ext_modules = [
            Extension(
                "tfcomb.counting",
                ["tfcomb/counting.c"],
                include_dirs=[".", np.get_include()]
            )
        ]
    else:
        sys.exit("Cython is required to compile TF-COMB from source.")

# --- Version finder ---
def find_version(init_file):
    with open(init_file) as f:
        version_file = f.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

# --- Read long description ---
def readme():
    with open("README.md", encoding="utf-8") as f:
        return f.read()

# --- Setup configuration ---
setup(
    name='tfcomb-custom',
    version=find_version(os.path.join("tfcomb", "__init__.py")),
    description='Custom TF-COMB: Fixed pandas var_name error and enhanced TF co-occurrence analysis.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/Rakesh8050/tfcomb-custom',
    author='Rakesh Kumar (Modified from Mette Bentsen)',
    author_email='',
    license='MIT',
    packages=['tfcomb'],
    ext_modules=ext_modules,
    cmdclass=cmdclass,
    python_requires='>=3.8',
    setup_requires=['numpy'],
    install_requires=[
        'numpy',
        'scipy',
        'pysam',
        'matplotlib>=2',
        'pandas>=2.3.0',   # fixed for var_name issue
        'tobias>=0.11',
        'networkx>=2.4',
        'python-louvain',
        'graphviz',
        'statsmodels',
        'goatools',
        'uropa',
        'qnorm',
        'dill',
        'seaborn',
        'tqdm',
        'IPython'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 3'
    ],
    include_package_data=True,
    zip_safe=False
)
