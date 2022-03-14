# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *


class Eman2(CMakePackage):
    """A scientific image processing software suite with a focus on CryoEM and CryoET."""

    homepage = "https://blake.bcm.edu/emanwiki"
    url = "https://github.com/cryoem/eman2/archive/refs/tags/v2.3.tar.gz"

    version(
        "2.91",
        sha256="7a82cdc1621fc9fae6fbe585e7626b5d40428b4597eef9ff56351e8db93b0427",
    )
    version(
        "2.31",
        sha256="897fe536d3240300a7d3009e8e1ec44c6651265b8410ccfee3c536cd8ce5e967",
    )

    variant("mpi", default=False, description="Enable MPI support")
    variant("cuda", default=False, description="Enable CUDA support")

    depends_on("py-numpy", type=["build", "run"])
    depends_on("hdf5")
    depends_on("boost+python+numpy")
    depends_on("libjpeg")
    depends_on("libpng")
    depends_on("libtiff")
    depends_on("gsl")
    depends_on("fftw+mpi", when="+mpi")
    depends_on("fftw", when="~mpi")
    depends_on("ftgl")

    # This dependencies where taken from the "eman2-deps" recipe for conda
    depends_on("py-bsddb3", type=["run"])
    depends_on("py-future", type=["run"])
    depends_on("py-matplotlib", type=["run"])
    depends_on("py-mpi4py", type=["run"], when="+mpi")
    depends_on("py-nose", type=["run"])
    depends_on("py-pandas", type=["run"], when="+cuda")
    depends_on("py-scikit-learn", type=["run"])
    depends_on("py-scipy", type=["run"])
    depends_on("py-tensorflow", type=["run"], when="~cuda")
    depends_on("py-tensorflow+cuda", type=["run"], when="+cuda")
    depends_on("py-tqdm", type=["run"])

    patch("cmake_detection.patch")

    extends("python")

    def cmake_args(self):
        args = [
            "-DENABLE_RT:BOOL=OFF",
            self.define_from_variant("ENABLE_EMAN_CUDA", "cuda"),
            self.define_from_variant("ENABLE_SPARX_CUDA", "cuda"),
        ]
        return args
