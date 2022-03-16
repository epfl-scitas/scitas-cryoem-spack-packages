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
#     spack install motioncorr
#
# You can edit this file again by typing:
#
#     spack edit motioncorr
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Motioncorr(MakefilePackage):
    """MotionCorr is based on the MotionCorr 2.0 release with some extensions."""

    homepage = "https://github.com/jianglab/motioncorr"
    url      = "https://github.com/jianglab/motioncorr/archive/refs/heads/master.zip"

    version('2.1.0',
            '656a8c91538796a4f61fb472831b782c050ded82bac3d2fc975de6b2ccdf3f32')

    depends_on('cuda@8.0:8', type='run')
    depends_on('fftw')
    # libtiff.so.3 is required
    depends_on('libtiff@3:', type='run')

    build_directory = 'src'

    def edit(self, spec, prefix):
        makefile = FileFilter('./src/Makefile')
        makefile.filter(r'^\s*CC\s*=.*',  'CC = '  + spack_cc)
        makefile.filter(r'^\s*CXX\s*=.*', 'CXX = ' + spack_cxx)
        makefile.filter(r'^\s*F77\s*=.*', 'F77 = ' + spack_f77)
        makefile.filter(r'^\s*FC\s*=.*',  'FC = '  + spack_fc)
        makefile.filter(r'sm_20',  'sm_70')

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install('./bin/*', prefix.bin)

