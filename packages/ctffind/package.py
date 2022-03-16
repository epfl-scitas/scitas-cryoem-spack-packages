# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ctffind(AutotoolsPackage):
    """Fast and accurate defocus estimation from electron micrographs."""

    homepage = "https://grigoriefflab.umassmed.edu/ctf_estimation_ctffind_ctftilt"
    url      = "https://grigoriefflab.umassmed.edu/system/tdf?path=ctffind-4.1.14.tar.gz&file=1&type=node&id=26"

    version('4.1.14', sha256='db17b2ebeb3c3b2b3764e42b820cd50d19ccccf6956c64257bfe5d5ba6b40cb5', extension='tar.gz')
    version('4.1.13', sha256='48231f8511b222176ea39b80c58ae8fb8a6bac5e0da247c54f5a84b52c8750cf', extension='tar.gz',
             url='https://grigoriefflab.umassmed.edu/system/tdf?path=ctffind-4.1.13.tar.gz&file=1&type=node&id=26')
    version('4.1.10', sha256='c3756e20fc4693240453ca4b6d9920c8c485184ce0a1d1c2d1e71ab32edbf770', extension='tar.gz',
             url='https://grigoriefflab.umassmed.edu/system/tdf?path=ctffind-4.1.10.tar.gz&file=1&type=node&id=26')
    version('4.1.8', sha256='bec43c0b8d32878c740d6284ef6d9d22718c80dc62270be18d1d44e8b84b2729', extension='tar.gz',
             url='https://grigoriefflab.umassmed.edu/system/tdf?path=ctffind-4.1.8.tar.gz&file=1&type=node&id=26')

    depends_on('wxwidgets')
    depends_on('fftw@3:')
