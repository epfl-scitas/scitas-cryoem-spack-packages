# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-topaz
#
# You can edit this file again by typing:
#
#     spack edit py-topaz
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

import os
import sys

from spack import *


class PyTopaz(PythonPackage, CudaPackage):
    """A pipeline for particle detection in cryo-electron microscopy images
    using convolutional neural networks trained from positive and unlabeled examples.
    Topaz also includes methods for micrograph and tomogram denoising
    using deep denoising models."""

    homepage = "https://github.com/tbepler/topaz"
    git      = "https://github.com/tbepler/topaz.git"

    version('master', branch='master', submodules=True)
    version('0.2.4', tag='v0.2.4', submodules=True)
    version('0.2.3', tag='v0.2.3', submodules=True)
    version('0.2.2', tag='v0.2.2', submodules=True)
    version('0.2.1', tag='v0.2.1', submodules=True)
    version('0.2.0', tag='v0.2.0', submodules=True)
    version('0.1.0', tag='v0.1.0', submodules=True)
    version('0.0.0', tag='v0.0.0', submodules=True)

    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-setuptools', type=('build'))
    depends_on('py-future', type=('build', 'run'))
    depends_on('py-torch@1.0: +cuda cuda_arch=70 ^cuda@11.1.1', type=('build', 'run'))
    depends_on('py-torchvision', type=('build', 'run'))
    depends_on('py-pillow@6.2:', type=('build', 'run'))
    depends_on('py-numpy@1.11:', type=('build', 'run'))
    depends_on('py-pandas', type=('build', 'run'))
    depends_on('py-scipy@0.17:', type=('build', 'run'))
    depends_on('py-scikit-learn@0.19:', type=('build', 'run'))
