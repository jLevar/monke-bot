import os

import discord
import time
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix='Monke, ', intents=intents)
pass_context = True


DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")


@client.event
async def on_ready():
    print('Monke Bot is online!')


### Role Commands ###
@client.command(name="addrole")
async def _role(ctx, role: discord.Role):
    if role in ctx.author.roles:
        await ctx.send('You already have this role. To remove a role,do: Monke, removerole')
    else:
        await ctx.author.add_roles(role)
        await ctx.send("Role given")


@client.command(name="removerole")
async def _rrole(ctx, role: discord.Role):
    if role in ctx.author.roles:
        await ctx.author.remove_roles(role)
        await ctx.send("Role removed")
    else:
        await ctx.send("You don't have this role. To add a role, do: Monke, addrole")


# @client.event
# async def on_member_join(member):
#    role = get(member.server.roles, name='Bourgeoisie')
#    await client.add_roles(member, role)


### Misc. Commands ###
@client.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(client.latency * 1000)}ms')


### Chat Commands ###
@client.command()
async def speak(ctx):
    random_var = random.randint(0, 1);
    if random_var == 0:
        await ctx.send('OOOH OOOH AAAH AAAH')
    elif random_var == 1:
        await ctx.send('AAAH AAAH OOOH OOOH')


@client.command()
async def insult(ctx, target):
    await ctx.send(f'{target} is the worst feces thrower in the entire Animal Kingdom!')


# @client.command()
# async def jokeTime(ctx):


@client.command()
async def grape(ctx, target):
    role = discord.utils.get(ctx.guild.roles, name="Primates")
    if role in ctx.author.roles:
        for x in range(0, 3):
            await ctx.send(f'THIS IS GRAPES! {target}')
            time.sleep(1)
    else:
        await ctx.send(f'I only grape on behalf of my fellow primates')


@client.command()
async def roles(ctx):
    guild = ctx.guild
    _roles = [role for role in guild.roles if role != ctx.guild.default_role]
    embed = discord.Embed(title="Server Roles", description=f"\n".join([role.mention for role in _roles]))
    await ctx.send(embed=embed)


### Moderator Commands ###
@client.command()
async def purge(ctx, amount=0):
    role = discord.utils.get(ctx.guild.roles, name="Zookeepers")
    if role in ctx.author.roles:
        if amount == 0:
            await ctx.send('You didn\'t give me an amount. I have now returned you back to monke')
        else:
            await ctx.channel.purge(limit=amount)
            await ctx.channel.send(f'I have returned {amount} messages back to monke')
    else:
        await ctx.send(f'I only purge on behalf of the Zookeepers')


@client.command()
async def ape(ctx, target):
    role = discord.utils.get(ctx.guild.roles, name="Zookeepers")
    if role in ctx.author.roles:
        for x in range(0, 10):
            await ctx.send(f'THIS IS BANANAS! {target}')
            time.sleep(1)
    else:
        await ctx.send(f'I only ape on behalf of the Zookeepers')


@client.command()
@commands.has_role("Zookeepers")
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await ctx.member.add_roles(role)
    await ctx.send(f'{member} was muted for violating the rules. To learn more, look up discord rule 34.')

client.run(DISCORD_API_SECRET)
