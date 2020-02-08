import discord
from discord.ext import commands
from BeatPy.Discord import formatter


custom_layout = {"example": ("Example layout title",
                             "{content}\n\nThis uses the example layout.\n"
                             "We can even add extra content ayy.\n{extra}", 0x00FB00),
                 "error": ("Error:", "{content}", 0xFF0000)}

setup = formatter.Embed(footer=True,
                        footer_message="This message will always appear!",  # except when overwritten
                        layout_set=custom_layout)
em = setup.create
author = formatter.Author
field = formatter.Field


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!",
                         description="Basic example bot for BeatPy its discord formatter!",
                         case_insensitive=True,
                         help_attrs=dict(hidden=True))
        self.add_cog(BeatPy(self.user))

    def run(self):
        super().run("NjQwNjI1NjgzNzk3NjM5MTgx.XhjZeQ.p_BLARO5aiSu56sp9iw2R_lnDZk", reconnect=True)

    async def on_ready(self):
        print('Logged in as:')
        print(f'Name: {self.user.name}#{self.user.discriminator}')
        print(f'ID: {self.user.id}')

    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)

    async def on_command_error(self, ctx, exception):
        if isinstance(type(exception), discord.ext.commands.errors.CommandNotFound):
            pass


class BeatPy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="example")
    async def example(self, ctx):
        await ctx.send(**em(content="BeatPy embed formatter.\n^^",
                            title="BeatPy is great!",
                            footer_icon=ctx.author.avatar_url,
                            author=author(ctx.author, "https://github.com/Arthurdw", ctx.author.avatar_url),
                            image="https://image.flaticon.com/icons/png/512/125/125768.png",
                            thumbnail="https://imageog.flaticon.com/icons/png/512/46/46010.png",
                            fields=[field("Example inline Field", "Example inline Field description."),
                                    field("Example second inline Field", "Example second inline Field description."),
                                    field("Example third non inline Field", "Example third Field description.", False),
                                    field("Example fourth non inline Field", "Example fourth Field desc.", False)],
                            timestamp=True))

    @commands.command(name="layout")
    async def layout(self, ctx):
        await ctx.send(**em(content="Create your own custom layouts.",
                            layout="example",
                            extra="This content is added using the `extra` param from your custom layout."))

    @commands.command(name="block")
    async def ltb(self, ctx, *, text: str = None):
        if text is None:
            return await ctx.send(**em(content="Missing the `text` parameter. :(", layout="error"))
        await ctx.send(**em(formatter.block(text)))


if __name__ == '__main__':
    Bot().run()
