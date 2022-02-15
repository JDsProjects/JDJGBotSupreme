import discord
from discord import ButtonStyle, SelectOption, interactions
from discord.ext import commands
from discord.ui import Button, Select, View



class Dropdown(discord.ui.Select):
    def __init__(self,options,ctx):
        self.bot = ctx.bot  # one thing fixed...

        # Set the options that will be presented inside the dropdown
        #options = [
        #THIS IS PURE PLACEHOLDER , PLEASE EDIT TO WHATEVER THE FINAL BOT WILL HAVE
            #SelectOption(label="Placeholder", value="Placeholder"),
            
            #SelectOption(label="Close", value="Close"),
        #]

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(placeholder="Select a category",
                         min_values=1,
                         max_values=1,
                         options=options)

    async def callback(self, interaction: discord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's
        # selected options. We only want the first one.

        # print(f"{interaction.author.name} with ID {interaction.author.id} just clicked something in the select menu")
        label = self.values[0]
        print(label)
        for cog in self.bot.cogs:  # fixed
            if label == cog:  # -------------------[1]
                await get_help(self, interaction, CogToPassAlong=cog)
                print(str(cog))
        if label == "Close":
            embede = discord.Embed(
                title=f"{self.bot.user.name} Help",
                description=f"",
                color = discord.Color.blurple()
            )
            embede.set_footer(text="Use help [command] or help [category] for more information | <> is required | [] is optional")
            await interaction.response.edit_message(embed=embede, view=None)


class DropdownView(discord.ui.View):
    def __init__(self, options,ctx):
        super().__init__()

        # Adds the dropdown to our view object.
        self.bot = ctx
        self.add_item(Dropdown(options,self.bot))


async def get_help(self, interaction, CogToPassAlong):
    # if CogToPassAlong == "NSFW":
    # if not interaction.channel.is_nsfw():
    # embed = discord.Embed(title="Non-NSFW channel 🔞", description=f"Find yourself an NSFW-Channel and retry from there.", color=discord.Colour.red())
    # embed.set_footer(text=f"set_your_footer_here")
    # await interaction.respond(embed=embed)
    # return
    # else:
    # pass

    for _ in self.bot.get_cog(CogToPassAlong).get_commands():
        pass
    # making title - getting description from doc-string below class
    emb = discord.Embed(
        title=f"{CogToPassAlong} - Commands",
        description=self.bot.cogs[CogToPassAlong].__doc__,
        color = discord.Color.blurple()
    )
    emb.set_author(name="Help System")
    # getting commands from cog
    for command in self.bot.get_cog(CogToPassAlong).get_commands():
        # if cog is not hidden
        if not command.hidden:
            emb.add_field(name=f"`{command.name}`",
                          value=command.help,
                          inline=True)
    # found cog - breaking loop
    await interaction.response.edit_message(embed=emb)


"""class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(slash_command=True,
                      message_command=True,
                      description="Help Command")
    async def help(self, ctx):
        embed = discord.Embed(title="SELECTION TEST",
                              description="Testing our embeds",
                              color=0xFF8000)
        embede = discord.Embed(
            title=":books: Help System",
            description=f"Welcome To {self.bot.user.name} Help System",
        )
        embede.set_footer(text="PLACEHOLDER")
        view = DropdownView(self.bot)

        done_components = [
            Button(style=ButtonStyle.secondary, label="·", disabled=True),
        ]

        # async def callback(interaction):
        # await interaction.send(embed=embed)

        await ctx.send(embed=embede, view=view)"""

class Help(commands.Cog):
    "The Help Menu Cog"

    def __init__(self, bot):
        self.bot = bot
        
        self.bot.help_command = MyHelp()
        

class HelpEmbed(discord.Embed): # Our embed with some preset attributes to avoid setting it multiple times
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.timestamp = discord.utils.utcnow()
        text = "Use help [command] or help [category] for more information | <> is required | [] is optional"
        self.set_footer(text=text)
        self.color = discord.Color.blurple()

class MyHelp(commands.HelpCommand):
    def __init__(self):
     
     super().__init__(command_attrs={
                "help": "The help command for the bot"
            })# create our class with some aliases and cooldown
            
        
    
    async def send(self, **kwargs):
        """a short cut to sending to get_destination"""
        await self.get_destination().send(**kwargs)

    async def send_bot_help(self, mapping):
        """triggers when a `<prefix>help` is called"""
        ctx = self.context
        embed = HelpEmbed(title=f"{ctx.me.display_name} Help")
        #embed.set_thumbnail(url=ctx.me.avatar)
        usable = 0 
        myoptions = []
        view = DropdownView(myoptions,ctx)

        for cog, commands in mapping.items(): #iterating through our mapping of cog: commands
            if filtered_commands := await self.filter_commands(commands): 
                # if no commands are usable in this category, we don't want to display it
                amount_commands = len(filtered_commands)
                usable += amount_commands
                if cog: # getting attributes dependent on if a cog exists or not
                    name = cog.qualified_name
                    description = cog.description or "No description"
                else:
                    name = "No Category"
                    description = "Commands with no category"

                #embed.add_field(name=f"{name} Category [{amount_commands}]", value=description)
                myoptions.append(SelectOption(label=name, value=name))

        #embed.description = f"{len(bot.commands)} commands | {usable} usable" 
        myoptions.append(SelectOption(label="Close", value="Close"))

        await self.send(embed=embed,view=view)

    async def send_command_help(self, command):
        """triggers when a `<prefix>help <command>` is called"""
        signature = self.get_command_signature(command) # get_command_signature gets the signature of a command in <required> [optional]
        embed = HelpEmbed(title=signature, description=command.brief or "No help found...")

        if cog := command.cog:
            embed.add_field(name="Category", value=cog.qualified_name)

        can_run = "No"
        # command.can_run to test if the cog is usable
        with contextlib.suppress(commands.CommandError):
            if await command.can_run(self.context):
                can_run = "Yes"
            
        embed.add_field(name="Usable", value=can_run)

        if command._buckets and (cooldown := command._buckets._cooldown): # use of internals to get the cooldown of the command
            embed.add_field(
                name="Cooldown",
                value=f"{cooldown.rate} per {cooldown.per:.0f} seconds",
            )

        await self.send(embed=embed)

    async def send_help_embed(self, title, description, commands): # a helper function to add commands to an embed
        embed = HelpEmbed(title=title, description=description or "No help found...")

        if filtered_commands := await self.filter_commands(commands):
            for command in filtered_commands:
                embed.add_field(name=self.get_command_signature(command), value=command.brief or "No help found...")
           
        await self.send(embed=embed)

    async def send_group_help(self, group):
        """triggers when a `<prefix>help <group>` is called"""
        title = self.get_command_signature(group)
        await self.send_help_embed(title, group.help, group.commands)

    async def send_cog_help(self, cog):
        """triggers when a `<prefix>help <cog>` is called"""
        title = cog.qualified_name or "No"
        await self.send_help_embed(f'{title} Category', cog.description, cog.get_commands())

def setup(bot):
    bot.add_cog(Help(bot))
