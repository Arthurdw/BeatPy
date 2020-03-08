import discord
import random
import datetime
from ..util.core import Process

default_layout = {None: ("", "{content}", None)}


def block(text: str):
    """Converts text to discord block letters!"""
    return Process.ltb(text)


class Embed:
    def __init__(self, layout_set=None, layout=None, footer=False, footer_icon=discord.Embed.Empty, color=None,
                 colour=None, footer_message=discord.Embed.Empty, timestamp=True, title=False):
        if layout_set is not None:
            default_layout.update(layout_set)
        self.layout_set = default_layout
        self.layout = layout
        self.footer = footer
        self.footer_icon = footer_icon
        self.footer_message = footer_message
        self.timestamp = timestamp
        self.title = title
        self.color = color or colour

    def create(self, content="", title=None, layout=None, footer=None, color=None, colour=None, footer_icon=None,
               footer_message=None, image=None, author=None, timestamp=None, thumbnail=None, fields=None, extra=None):
        """
        Create a discord embed.

        :param content: String: Message (description).
        :param title: String: Embed title.
        :param layout: String: If a layout has been set, select one of your layouts.
        :param footer: Boolean: Do you want to have a footer?
        :param color: String(Hexadecimal): The embed its color.
        :param colour: String(Hexadecimal): The embed its colour. (Alias for `color`)
        :param footer_icon: String(URL): The footer icon url, if none given it will display no icon.
        :param footer_message: String: Give a footer string, if none has been given it will display the given one with the setup.
        :param image: String(URL): Set an image for the embed.
        :param author: String: Set a embed author.
        :param timestamp: Boolean: Would you like to have a timestamp in your footer?
        :param thumbnail: String(URL): The embed thumbnail url.
        :param fields: Array/List/Tuple: Add fields, these fields are fields from the `Field` object.
        :param extra: String: Extra argument for when a custom layout is used that is optional.
        :return: A valid discord embed.
        """
        embed_title, embed_content, embed_color = self.layout_set.get(layout or self.layout)
        emb_content = embed_content.format(content=content, extra=extra or "")
        title = title or self.title or embed_title
        color = color or colour or self.color or embed_color or discord.Color(int(hex(random.randint(0, 16581375)), 0))
        embed = discord.Embed(title=title, color=color, description=emb_content)
        if image is not None:
            embed.set_image(url=image)
        if author is not None:
            embed.set_author(name=author.name, url=author.url, icon_url=author.icon_url)
        if footer or self.footer:
            embed.set_footer(text=footer_message or self.footer_message,
                             icon_url=footer_icon or self.footer_icon)
        if self.timestamp if timestamp is None else timestamp:
            embed.timestamp = datetime.datetime.utcnow()
        if thumbnail is not None:
            embed.set_thumbnail(url=thumbnail)
        if fields is not None:
            for field in fields:
                embed.add_field(name=field.name, value=field.value, inline=field.inline)
        return {"embed": embed}


class Author:
    def __init__(self, name, url, icon_url):
        self.name = name
        self.url = url
        self.icon_url = icon_url


class Field:
    def __init__(self, name, value, inline=True):
        self.name = name
        self.value = value
        self.inline = inline
