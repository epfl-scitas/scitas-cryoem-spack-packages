# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os


class Unblur(AutotoolsPackage):
    """Unblur is used to align the frames of movies recorded on an electron
    microscope to reduce image blurring due to beam-induced motion."""

    homepage = "https://grigoriefflab.janelia.org/unblur"
    url = "https://grigoriefflab.umassmed.edu/system/tdf?path=unblur_1.0.2.tar.gz&file=1&type=node&id=4902"

    version(
        "1.0.2",
        sha256="1aa72b1f944114987ede644e1866eaebc08e191ecc566b3461409449360931e2",
        extension=".tar.gz",
    )

    variant("openmp", default=True, description="Enable OpenMP support")
    variant("shared", default=True, description="Dynamic linking")

    depends_on("zlib")
    depends_on("jpeg")
    depends_on("libtiff")
    depends_on("gsl")
    depends_on("jbigkit")
    depends_on("intel-mkl")
    depends_on("fftw@3.3:")

    conflicts("%pgi")
    conflicts("%apple-clang")
    conflicts("%clang")
    conflicts("%cce")
    conflicts("%xl")
    conflicts("%xl_r")

    configure_directory = "src"
    build_directory = "src/build"
    parallel = False

    depends_on('autoconf', type='build', when='@1.0.2')
    depends_on('automake', type='build', when='@1.0.2')
    depends_on('libtool', type='build', when='@1.0.2')

    force_autoreconf = True
    
    def patch(self):
        filter_file(r"<<<<<<<.*", "", "src/missing")
        if 'gfortran' in self.compiler.fc:
            filter_file(r'FCFLAGS=""',
                        'FCFLAGS="-cpp -ffree-line-length-none -I{}"'.format(self.spec["fftw"].prefix.include),
                        "src/configure.ac")

    def configure_args(self):
        spec = self.spec

        # the configure does not consider the full path...
        compiler = os.path.basename(self.compiler.fc)

        return [
            "FC={}".format(compiler),
            "--with-gsl-libdir={}".format(spec["gsl"].prefix.lib),
            "--with-fftw-libdir={}".format(spec["fftw"].prefix.lib),
            "--enable-static={0}".format("yes" if "~shared" in spec else "no"),
            "--enable-openmp={0}".format("yes" if "+openmp" in spec else "no"),
            "--enable-optimisations=yes",
        ]
