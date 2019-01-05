from __future__ import absolute_import
import Scrapy
from Scrapy.Item import Item, Field


class StackItem(Scrapy.Item):
    title = Field()
    url = Field()
