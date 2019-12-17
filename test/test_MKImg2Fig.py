# MK-Img2fig: Markdown Img to Figure
#
# Copyright (c) 2019 Mandaris Moore
#
# GNU License
import markdown
import unittest

import MKImg2Fig


class MKImg2FigTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty_input(self):
        inString = ""
        outString = markdown.markdown(
            inString, extensions=[MKImg2Fig.MKImg2FigExtension()])
        self.assertEqual(inString, outString)

    def test_simple(self):
        pass
