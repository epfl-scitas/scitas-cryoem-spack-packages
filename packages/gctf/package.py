# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack import *


class Gctf(Package):
    """Gctf (Kai Zhang) – Accurate estimation of the contrast transfer function
    (CTF) is critical for a near-atomic resolution cryo-EM reconstruction"""

    homepage = "https://www2.mrc-lmb.cam.ac.uk/research/locally-developed-software/"
    url = "https://www2.mrc-lmb.cam.ac.uk/download/gctf_gautomatch_cu10-1-tar-gz/"

    version("1.18", sha256="1524f40d4630dadd08560b682812bac3",
            url="https://www2.mrc-lmb.cam.ac.uk/download/gctf_gautomatch_cu10-1-tar-gz/?ind=5eaaa7c1dc4da&filename=GCTF_Gautomatch_Cu10.1.tar.gz&wpdmdl=17990&refresh=626fdca2cd62a1651498146",
            extension='tar.gz'
    )
    version(
        "1.06",
        sha256="0123456789abcdef0123456789abcdef",
        url="https://www2.mrc-lmb.cam.ac.uk/download/gctf_v1-06-and-examples/?ind=1588080936085&filename=Gctf_v1.06_and_examples.tar.gz&wpdmdl=17948&refresh=626fdcc9de7be1651498185",
    )

    depends_on("cuda@10.1.0:10.1.999", type=["run"], when="@1.18")
    depends_on("cuda@5:8.0.999", type=["run"], when="@1.06")

    @when("@1.18")
    def install(self, spec, prefix):
        with working_dir(self.stage.source_path):
            install("GCTF_v1.18_sm30-75_cu10.1", prefix.bin)

    @when("@1.06")
    def install(self, spec, prefix):
        with working_dir(self.stage.source_path):
            install(
                "bin/Gctf-v1.06_sm_10_cu{}_x86_64".format(
                    spec["cuda"].version.up_to(2).dotted
                ),
                prefix.bin,
            )
