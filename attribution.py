import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Role attribution bot ready.')

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    guild_id = payload.guild_id
    if message_id == 707272448596377631:
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == '4️⃣':
            role = discord.utils.get(guild.roles, name='R4')
        elif payload.emoji.name == '5️⃣':
            role = discord.utils.get(guild.roles, name='R5')
        elif payload.emoji.name == '⏸️':
            role = discord.utils.get(guild.roles, name='R5 double Team')
        else:
            print(payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print('Role attributed.')
            else:
                print('Member not found')
        else:
            print('Role not found')








client.run('NzA3NzAzNDMwNjUwNzg5OTA4.XrMqUw.VqkMoGh2ZvTCyRWlIcs70YAg9s8')