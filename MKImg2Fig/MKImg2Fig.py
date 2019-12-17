# MK-Img2Fig: Markdown Img to Figure
#
# Copyright (c) 2019 Mandaris Moore
#
# GNU License
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
# from xml.etree import ElementTree


class Img2Figprocessor(Treeprocessor):
    """docstring for Img2Figprocessor"""

    def __init__(self, md, stripTitle, figureClass, figcaptionClass):
        self.md = md
        self.stripTitle = stripTitle
        self.figureClass = figureClass
        self.figcaptionClass = figcaptionClass
        super(Img2Figprocessor, self).__init__()

    def run(self, root):
        pass


class MKImg2FigExtension(Extension):
    def __init__(self, **kwargs):
        self.config = {
            "stripTitle": [False, "Strip the title from the <img />."],
            "figureClass": ["", "CSS class to add to the <figure /> element."],
            "figcaptionClass":
                ["", "CSS class to add to the <figcaption /> element."],
        }
        super(MKImg2FigExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md):
        md.treeprocessors.register(
            Img2Figprocessor(
                md,
                stripTitle=self.getConfig("stripTitle"),
                figureClass=self.getConfig("figureClass"),
                figcaptionClass=self.getConfig("figcaptionClass"),
            ),
            "Img2figprocessor",
            15)


def makeExtension(**kwargs):
    return MKImg2FigExtension(**kwargs)
