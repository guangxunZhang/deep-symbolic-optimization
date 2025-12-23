from setuptools import setup
import os

# Try to import numpy and Cython, but don't fail if they're not available yet
# They will be installed via setup_requires
try:
    import numpy
    from Cython.Build import cythonize
    HAS_BUILD_DEPS = True
except ImportError:
    HAS_BUILD_DEPS = False
    numpy = None

required = [
    "pytest",
    "cython",
    "numpy<1.20",  # Allow numpy 1.19.x including 1.19.5 which has pre-built wheels
    "tensorflow>=2.5,<3.0",  # TensorFlow 1.14 no longer available; using TF 2.x with compat mode
    "numba==0.53.1",
    "sympy",
    "pandas",
    "scikit-learn",
    "click",
    "deap",
    "pathos",
    "seaborn",
    "progress",
    "tqdm",
    "commentjson",
    "PyYAML",
    "prettytable"
]

extras = {
    "control": [
        "mpi4py",
        "gym[box2d]==0.15.4",
        "pybullet",
        "stable-baselines[mpi]==2.10.0"
    ],
    "regression": []
}
extras['all'] = list(set([item for group in extras.values() for item in group]))

# Prepare extension modules - only if build dependencies are available
ext_modules = None
include_dirs = []
if HAS_BUILD_DEPS:
    ext_modules = cythonize([os.path.join('dso','cyfunc.pyx')])
    include_dirs = [numpy.get_include()]

setup(  name='dso',
        version='1.0dev',
        description='Deep symbolic optimization.',
        author='LLNL',
        packages=['dso'],
        setup_requires=["numpy", "Cython"],
        ext_modules=ext_modules, 
        include_dirs=include_dirs,
        install_requires=required,
        extras_require=extras
        )
