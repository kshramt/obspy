#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The libgse1 test suite.
"""

from obspy.gse2 import libgse1
from obspy.gse2.libgse2 import ChksumError
import os
import unittest


class LibGSE1TestCase(unittest.TestCase):
    """
    Test cases for libgse1.
    """
    def setUp(self):
        # directory where the test files are located
        self.path = os.path.join(os.path.dirname(__file__), 'data')

    def test_verifyChecksums(self):
        """
        Tests verifying checksums for CM6 encoded GSE1 files.
        """
        #1
        fh = open(os.path.join(self.path, 'acc.gse'), 'rb')
        libgse1.read(fh, verify_chksum=True)
        fh.close()
        #2
        fh = open(os.path.join(self.path, 'y2000.gse'), 'rb')
        libgse1.read(fh, verify_chksum=True)
        fh.close()
        #3
        fh = open(os.path.join(self.path, 'loc_STAU20031119011659.z'), 'rb')
        libgse1.read(fh, verify_chksum=True)
        fh.close()
        #4 - second checksum is wrong
        fh = open(os.path.join(self.path, 'GRF_031102_0225.GSE.wrong_chksum'),
                  'rb')
        libgse1.read(fh, verify_chksum=True)  # correct
        self.assertRaises(ChksumError, libgse1.read, fh, verify_chksum=True)
        fh.close()


def suite():
    return unittest.makeSuite(LibGSE1TestCase, 'test')


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
