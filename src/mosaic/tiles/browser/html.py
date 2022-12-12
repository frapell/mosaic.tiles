from plone.app.standardtiles import _PMF as _
from plone.app.textfield import RichText
from plone.subrequest import ISubRequest
from plone.supermodel.directives import primary
from plone.supermodel.model import Schema
from plone.tiles import Tile
from plone.tiles.directives import ignore_querystring
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from zope import schema


class IHTMLTile(Schema):

    content1 = RichText(
        title=_("HTML 1"),
        required=False,
    )
    content2 = RichText(
        title=_("HTML 2"),
        required=False,
    )


class HTMLTile(Tile):
    """
    """

    def __call__(self):
        content1 = self.data.get("content1")
        content2 = self.data.get("content2")

        results = f"<html><body>"
        for content in [content1, content2]:
            if content:
                results += "<h2>Content:</h2><p>"
                results += content.output
                results += "</p>"

        results += f"</body></html>"
        return results
