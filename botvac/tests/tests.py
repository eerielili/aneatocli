#!/usr/bin/env python
from unittest import TestCase
from docopt import docopt
import aneatocli


class TestAneatoCLI(TestCase):
    def thelogTest(self):
        loginSuccess=aneatocli.logTest()
        self.assertTrue(isinstance(loginSuccess, basestring))


if __name__ == "__main__":
    unittest.main()
