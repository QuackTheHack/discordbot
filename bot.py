import discord
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '.')
status = cycle(['Prefix "."', 'But if you close your eyes', 'Add my owner :D KittyCatDev#7285'])
client.remove_command('help')

@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready!')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1    )}ms')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention} *poof*')

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')

@client.command()
async def code(ctx):
    await ctx.send(f'yeah, no your not getting this code loser')

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )
    embed.set_author(name='Help')
    embed.add_field(name='.ping', value='Returns pong!', inline=False)
    embed.add_field(name='.ban', value='Bans user selected to ban!', inline=False)
    embed.add_field(name='.kick', value='Kicks user selected to kick!', inline=False)
    embed.add_field(name='.clear', value='Clears the amount of messages you want to clear! *requires manage messages role*', inline=False)

    await ctx.send(embed=embed)

client.run('ODE4NDM4NTEyMTk3NTAwOTI4.YEYEQw.BMxSXB2dSErywoEV3BKQsvY1cCE')
