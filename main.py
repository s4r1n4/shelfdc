import os, sys, traceback
from os import system
import discord
from discord.ui import Button,View
import datetime
from keep_alive import keep_alive
intents = discord.Intents.default()
intents.messages = True
activity=discord.Activity(type=discord.ActivityType.watching, name="you learn | /help")
bot=discord.Bot(intents=intents, activity=activity)
next_button=Button(emoji="⏩", )
prev_button=Button(emoji="⏪")
@bot.slash_command(description="Shows help for the bot.")
async def help(ctx):
  view=View()
  pageview=View()
  pageview.add_item(prev_button)
  view.add_item(next_button)
  embed=discord.Embed(title="Welcome to Shelf!", description="Shelf is a completely public library that aspires to bring together, collect and sort useful information by the means of a virtual library that can be easily accessed and modified by anyone.", color=0x964B00)
  embed.set_image(url="https://i.pinimg.com/originals/42/88/b0/4288b0367a47ca15e89aeab9862717c8.gif")
  embed.add_field(name="`collection`", value="Access the library.", inline=False)
  embed.add_field(name="`add`", value="Add to the library.",inline=False)
  embed.add_field(name='`delete`',value="Delete a field.", inline=False)
  embed.add_field(name="`update`", value="Update a field's title/link using its original title which can be extracted using `search` or `uploads`.",inline=False)
  embed.add_field(name="`search`", value="Search for a file in the library.", inline=False)
  embed.add_field(name="`uploads`", value="Get a list of user's uploads.",inline=False)
  embed.add_field(name='`suggestions`',value="Send suggestions for the bot.", inline=False)
  
  embed.timestamp=datetime.datetime.now()
  await ctx.respond(embed=embed, view=view)
  async def next_button_callback(interaction):
    pageembed=discord.Embed(title="A word.", description="Since Shelf is completely public across all servers, you are requested to be mindful of what you add to the library. There are currently no restrictions on who can add. If you'd like to send suggestions, kindly do so using `/suggestions`. Thank you!",color=0x964B00)
    await interaction.response.edit_message(embed=pageembed,view=pageview)
  async def prev_button_callback(interaction):
    await interaction.response.edit_message(embed=embed,view=view)
  prev_button.callback=prev_button_callback
  next_button.callback=next_button_callback
extensions=['shelf']
if __name__=='__main__':
  for extension in extensions:
    try:
      bot.load_extension(extension)
    except Exception as e:
      print(f"Error loading {extension}", file=sys.stderr)
      traceback.print_exc()
keep_alive()
try:
    bot.run(os.environ['TOKEN'])
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    system('kill 1')