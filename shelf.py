import discord
import math
import asyncio
from discord.ext import commands
from discord.ui import View,Button
from discord import Option
from replit import db
import sqlite3
import json
import os
from os import system
import utils
intents = discord.Intents.default()
intents.messages = True
bot=discord.Bot(intents=intents)
connection=sqlite3.connect('shelf.sqlite')
cursor=connection.cursor()
connection.execute("CREATE TABLE IF NOT EXISTS Computer_Science_Notes (ID INTEGER PRIMARY KEY AUTOINCREMENT, Title STRING, Link STRING, User STRING, User_ID STRING, Guild STRING);")
connection.execute("CREATE TABLE IF NOT EXISTS Computer_Science_Short_Notes (ID INTEGER PRIMARY KEY AUTOINCREMENT, Title STRING, Link STRING, User STRING, User_ID STRING, Guild STRING);")
connection.execute("CREATE TABLE IF NOT EXISTS Computer_Science_Books (ID INTEGER PRIMARY KEY AUTOINCREMENT, Title STRING, Link STRING, User STRING, User_ID STRING, Guild STRING);")
connection.execute("CREATE TABLE IF NOT EXISTS Computer_Science_QA (ID INTEGER PRIMARY KEY AUTOINCREMENT, Title STRING, Link STRING, User STRING, User_ID STRING, Guild STRING);")
connection.execute("CREATE TABLE IF NOT EXISTS Computer_Science_Misc (ID INTEGER PRIMARY KEY AUTOINCREMENT, Title STRING, Link STRING, User STRING, User_ID STRING, Guild STRING);")
connection.execute("CREATE TABLE IF NOT EXISTS Maths_Notes (ID INTEGER PRIMARY KEY AUTOINCREMENT, Title STRING, Link STRING, User STRING, User_ID STRING, Guild STRING);")
connection.execute("CREATE TABLE IF NOT EXISTS Maths_Short_Notes (ID INTEGER PRIMARY KEY AUTOINCREMENT, Title STRING, Link STRING, User STRING, User_ID STRING, Guild STRING);")
connection.execute("CREATE TABLE IF NOT EXISTS Maths_Books (ID INTEGER PRIMARY KEY AUTOINCREMENT, Title STRING, Link STRING, User STRING, User_ID STRING, Guild STRING);")
connection.execute("CREATE TABLE IF NOT EXISTS Maths_QA (ID INTEGER PRIMARY KEY AUTOINCREMENT, Title STRING, Link STRING, User STRING, User_ID STRING, Guild STRING);")
connection.execute("CREATE TABLE IF NOT EXISTS Maths_Misc (ID INTEGER PRIMARY KEY AUTOINCREMENT, Title STRING, Link STRING, User STRING, User_ID STRING, Guild STRING);")
connection.execute("CREATE TABLE IF NOT EXISTS Suggestions (ID INTEGER PRIMARY KEY AUTOINCREMENT, Feedback STRING, User STRING, Guild STRING);")
connection.close()
shelf_embed=discord.Embed(title="**Welcome to your library!**", description="Where would you like to go?", color=0x00d5ff)
shelf="https://i.imgur.com/tBDoGsY.gif"
shelf_embed.set_image(url="https://i.imgur.com/tBDoGsY.gif")
cs_button=Button(label="Computer Science",emoji="<:CS:1013859376899051530>")
maths_button=Button(label="Mathematics", emoji="<:MATHS:1013859471015034910>")
cs_catalog=Button(label="Look through CS collection", emoji="<:CS:1013859376899051530>",style=discord.ButtonStyle.blurple)
maths_catalog=Button(label="Look through Maths collection", emoji="<:MATHS:1013859471015034910>",style=discord.ButtonStyle.blurple)
back_to_start=Button(emoji="🔙",style=discord.ButtonStyle.danger)
look_thru_cs=Button(emoji="🔙", style=discord.ButtonStyle.danger)
look_thru_math=Button(emoji="🔙", style=discord.ButtonStyle.danger)
select_cs=Button(emoji='🔙',style=discord.ButtonStyle.danger)
select_math=Button(emoji='🔙',style=discord.ButtonStyle.danger)
Cnts=Button(emoji="🔴")
Csnts=Button(emoji="🟠")
Cbook=Button(emoji="🟡")
Cqa=Button(emoji="🟢")
Cmisc=Button(emoji="🟣")
nts=Button(emoji="🔴")
snts=Button(emoji="🟠")
book=Button(emoji="🟡")
qa=Button(emoji="🟢")
misc=Button(emoji="🟣")


###
csn_next=Button(emoji='⏩')
csn_prev=Button(emoji='⏪')
csn_titles=[]
csn_links=[]
csn_index=0

cssn_next=Button(emoji='⏩')
cssn_prev=Button(emoji='⏪')
cssn_titles=[]
cssn_links=[]
cssn_index=0

csb_next=Button(emoji='⏩')
csb_prev=Button(emoji='⏪')
csb_titles=[]
csb_links=[]
csb_index=0

csqa_next=Button(emoji='⏩')
csqa_prev=Button(emoji='⏪')
csqa_titles=[]
csqa_links=[]
csqa_index=0

csmisc_next=Button(emoji='⏩')
csmisc_prev=Button(emoji='⏪')
csmisc_titles=[]
csmisc_links=[]
csmisc_index=0

mn_next=Button(emoji='⏩')
mn_prev=Button(emoji='⏪')
mn_titles=[]
mn_links=[]
mn_index=0

msn_next=Button(emoji='⏩')
msn_prev=Button(emoji='⏪')
msn_titles=[]
msn_links=[]
msn_index=0

mb_next=Button(emoji='⏩')
mb_prev=Button(emoji='⏪')
mb_titles=[]
mb_links=[]
mb_index=0

mqa_next=Button(emoji='⏩')
mqa_prev=Button(emoji='⏪')
mqa_titles=[]
mqa_links=[]
mqa_index=0

mmisc_next=Button(emoji='⏩')
mmisc_prev=Button(emoji='⏪')
mmisc_titles=[]
mmisc_links=[]
mmisc_index=0


###
css=False
mafs=False
cs_misc=[]
back=False
class Shelf(commands.Cog):
      def __init__(self, bot):
        self.bot = bot
      @commands.Cog.listener()
      async def on_ready(self):
        print("Bot is online!")
        connection=sqlite3.connect('shelf.sqlite')
        print('Ready!')
        print('Logged in as ---->', self.bot.user)
        print('ID:', self.bot.user.id)
      @commands.slash_command(description="Opens virtual library.")
      async def collection(self, ctx):
          global csn_index, cssn_index, csb_index, csqa_index, csmisc_index
          global mn_index, msn_index, mb_index, mqa_index, mmisc_index
          csn_index, cssn_index, csb_index, csqa_index, csmisc_index=0,0,0,0,0
          mn_index, msn_index, mb_index, mqa_index, mmisc_index = 0,0,0,0,0
          csn_titles.clear()
          csn_links.clear()
          cssn_titles.clear()
          cssn_links.clear()
          csb_titles.clear()
          csb_links.clear()
          csqa_titles.clear()
          csqa_links.clear()
          csmisc_titles.clear()
          csmisc_links.clear()
          mn_titles.clear()
          mn_links.clear()
          msn_titles.clear()
          msn_links.clear()
          mb_titles.clear()
          mb_links.clear()
          mqa_titles.clear()
          mqa_links.clear()
          mmisc_titles.clear()
          mmisc_links.clear()
          csn_view=View()
          csn_firstpage_view=View()
          csn_firstpage_view.add_item(csn_next)
          csn_firstpage_view.add_item(look_thru_cs)
          csn_lessthanten=View()
          csn_lessthanten.add_item(look_thru_cs)
          csn_view.add_item(csn_prev)
          csn_view.add_item(csn_next)
          csn_view.add_item(look_thru_cs)
          csn_lastpage_view=View()
          csn_lastpage_view.add_item(csn_prev)
          csn_lastpage_view.add_item(look_thru_cs)
          cssn_view=View()
          cssn_firstpage_view=View()
          cssn_firstpage_view.add_item(cssn_next)
          cssn_firstpage_view.add_item(look_thru_cs)
          cssn_lessthanten=View()
          cssn_lessthanten.add_item(look_thru_cs)
          cssn_view.add_item(cssn_prev)
          cssn_view.add_item(cssn_next)
          cssn_view.add_item(look_thru_cs)
          cssn_lastpage_view=View()
          cssn_lastpage_view.add_item(cssn_prev)
          cssn_lastpage_view.add_item(look_thru_cs)
          csb_view=View()
          csb_firstpage_view=View()
          csb_firstpage_view.add_item(csb_next)
          csb_firstpage_view.add_item(look_thru_cs)
          csb_lessthanten=View()
          csb_lessthanten.add_item(look_thru_cs)
          csb_view.add_item(csb_prev)
          csb_view.add_item(csb_next)
          csb_view.add_item(look_thru_cs)
          csb_lastpage_view=View()
          csb_lastpage_view.add_item(csb_prev)
          csb_lastpage_view.add_item(look_thru_cs)
          csqa_view=View()
          csqa_firstpage_view=View()
          csqa_firstpage_view.add_item(csqa_next)
          csqa_firstpage_view.add_item(look_thru_cs)
          csqa_lessthanten=View()
          csqa_lessthanten.add_item(look_thru_cs)
          csqa_view.add_item(csqa_prev)
          csqa_view.add_item(csqa_next)
          csqa_view.add_item(look_thru_cs)
          csqa_lastpage_view=View()
          csqa_lastpage_view.add_item(csqa_prev)
          csqa_lastpage_view.add_item(look_thru_cs)
          csmisc_view=View()
          csmisc_view.add_item(csmisc_prev)
          csmisc_view.add_item(csmisc_next)
          csmisc_view.add_item(look_thru_cs)
          csmisc_firstpage_view=View()
          csmisc_firstpage_view.add_item(csmisc_next)
          csmisc_firstpage_view.add_item(look_thru_cs)
          csmisc_lessthanten=View()
          csmisc_lessthanten.add_item(look_thru_cs)
          csmisc_lastpage_view=View()
          csmisc_lastpage_view.add_item(csmisc_prev)
          csmisc_lastpage_view.add_item(look_thru_cs)
          mn_view=View()
          mn_firstpage_view=View()
          mn_firstpage_view.add_item(mn_next)
          mn_firstpage_view.add_item(look_thru_math)
          mn_lessthanten=View()
          mn_lessthanten.add_item(look_thru_math)
          mn_view.add_item(mn_prev)
          mn_view.add_item(mn_next)
          mn_view.add_item(look_thru_math)
          mn_lastpage_view=View()
          mn_lastpage_view.add_item(mn_prev)
          mn_lastpage_view.add_item(look_thru_math)
          msn_view=View()
          msn_view=View()
          msn_firstpage_view=View()
          msn_firstpage_view.add_item(msn_next)
          msn_firstpage_view.add_item(look_thru_math)
          msn_lessthanten=View()
          msn_lessthanten.add_item(look_thru_math)
          msn_view.add_item(msn_prev)
          msn_view.add_item(msn_next)
          msn_view.add_item(look_thru_math)
          msn_lastpage_view=View()
          msn_lastpage_view.add_item(msn_prev)
          msn_lastpage_view.add_item(look_thru_math)
          mb_view=View()
          mb_view=View()
          mb_firstpage_view=View()
          mb_firstpage_view.add_item(mb_next)
          mb_firstpage_view.add_item(look_thru_math)
          mb_lessthanten=View()
          mb_lessthanten.add_item(look_thru_math)
          mb_lastpage_view=View()
          mb_lastpage_view.add_item(mb_prev)
          mb_lastpage_view.add_item(look_thru_math)
          mb_view.add_item(mb_prev)
          mb_view.add_item(mb_next)
          mb_view.add_item(look_thru_math)
          mqa_view=View()
          mqa_view=View()
          mqa_firstpage_view=View()
          mqa_firstpage_view.add_item(mqa_next)
          mqa_firstpage_view.add_item(look_thru_math)
          mqa_lessthanten=View()
          mqa_lessthanten.add_item(look_thru_math)
          mqa_view.add_item(mqa_prev)
          mqa_view.add_item(mqa_next)
          mqa_view.add_item(look_thru_math)
          mqa_lastpage_view=View()
          mqa_lastpage_view.add_item(mqa_prev)
          mqa_lastpage_view.add_item(look_thru_math)
          mmisc_view=View()
          mmisc_view=View()
          mmisc_firstpage_view=View()
          mmisc_firstpage_view.add_item(mmisc_next)
          mmisc_firstpage_view.add_item(look_thru_math)
          mmisc_lessthanten=View()
          mmisc_lessthanten.add_item(look_thru_math)
          mmisc_view.add_item(mmisc_prev)
          mmisc_view.add_item(mmisc_next)
          mmisc_view.add_item(look_thru_math)
          mmisc_lastpage_view=View()
          mmisc_lastpage_view.add_item(mmisc_prev)
          mmisc_lastpage_view.add_item(look_thru_math)
          view=View()
          view.add_item(maths_button)
          view.add_item(cs_button)
          cscollectionview=View()
          cscollectionview.add_item(look_thru_cs)
          mafcollectionview=View()
          mafcollectionview.add_item(look_thru_math)
          mathcat_view=View()
          mathcat_view.add_item(maths_catalog)
          mathcat_view.add_item(back_to_start)
          cscat_view=View()
          cscat_view.add_item(cs_catalog)
          cscat_view.add_item(back_to_start)
          category_view=View()
          category_view.add_item(nts)
          category_view.add_item(snts)
          category_view.add_item(book)
          category_view.add_item(qa)
          category_view.add_item(misc)
          category_view.add_item(select_math)
          Ccategory_view=View()
          Ccategory_view.add_item(Cnts)
          Ccategory_view.add_item(Csnts)
          Ccategory_view.add_item(Cbook)
          Ccategory_view.add_item(Cqa)
          Ccategory_view.add_item(Cmisc)
          Ccategory_view.add_item(select_cs)
          cne=discord.Embed(title="Computer Science - 🔴 Notes", color=0xFF0000)
          csne=discord.Embed(title="Computer Science - 🟠 Short Notes", color=0xFFA500)
          cbe=discord.Embed(title="Computer Science - 🟡 Books", color=0xFFFF00)
          cqae=discord.Embed(title="Computer Science - 🟢 Question & Answer", color=0x00FF00)
          cmisce=discord.Embed(title="Computer Science - 🟣 Miscellaneous", color=0xA020F0)
          mne=discord.Embed(title="Mathematics - 🔴 Notes", color=0xFF0000)
          msne=discord.Embed(title="Mathematics - 🟠 Short Notes", color=0xFFA500)
          mbe=discord.Embed(title="Mathematics - 🟡 Books", color=0xFFFF00)
          mqae=discord.Embed(title="Mathematics - 🟢 Question & Answer", color=0x00FF00)
          mmisce=discord.Embed(title="Mathematics - 🟣 Miscellaneous", color=0xA020F0)
          await ctx.respond(embed=shelf_embed, view=view)
          connection=sqlite3.connect('shelf.sqlite')
          cursor=connection.cursor()
          len_csn=cursor.execute("SELECT COUNT(ID) FROM Computer_Science_Notes;")
          len_csn=len_csn.fetchone()[0]
          len_csn=int(len_csn)
          csnpages = (len_csn // 10) + 1
          len_cssn=cursor.execute("SELECT COUNT(ID) FROM Computer_Science_Short_Notes;")
          len_cssn=len_cssn.fetchone()[0]
          len_cssn=int(len_cssn)
          cssnpages = (len_cssn // 10) + 1
          len_csb=cursor.execute("SELECT COUNT(ID) FROM Computer_Science_Books;")
          len_csb=len_csb.fetchone()[0]
          len_csb=int(len_csb)
          csbpages = (len_csb // 10) + 1

          len_csqa=cursor.execute("SELECT COUNT(ID) FROM Computer_Science_QA;")
          len_csqa=len_csqa.fetchone()[0]
          len_csqa=int(len_csqa)
          csqapages = (len_csqa // 10) + 1
          len_csmisc=cursor.execute("SELECT COUNT(ID) FROM Computer_Science_Misc;")
          len_csmisc=len_csmisc.fetchone()[0]
          len_csmisc=int(len_csmisc)
          csmiscpages = (len_csmisc // 10) + 1
          len_mn=cursor.execute("SELECT COUNT(ID) FROM Maths_Notes;")
          len_mn=len_mn.fetchone()[0]
          len_mn=int(len_mn)
          mnpages = (len_mn // 10) + 1
          len_msn=cursor.execute("SELECT COUNT(ID) FROM Maths_Short_Notes;")
          len_msn=len_msn.fetchone()[0]
          len_msn=int(len_msn)
          msnpages = (len_msn // 10) + 1
          len_mb=cursor.execute("SELECT COUNT(ID) FROM Maths_Books;")
          len_mb=len_mb.fetchone()[0]
          len_mb=int(len_mb)
          mbpages = (len_mb // 10) + 1
          len_mqa=cursor.execute("SELECT COUNT(ID) FROM Maths_QA;")
          len_mqa=len_mqa.fetchone()[0]
          len_mqa=int(len_mqa)
          mqapages = (len_mqa // 10) + 1
          len_mmisc=cursor.execute("SELECT COUNT(ID) FROM Maths_Misc;")
          len_mmisc=len_mmisc.fetchone()[0]
          len_mmisc=int(len_mmisc)
          mmiscpages = (len_mmisc // 10) + 1
          
          cursor_csn=connection.execute(f"SELECT Title FROM Computer_Science_Notes;")
          cursor_cssn=connection.execute(f"SELECT Title FROM Computer_Science_Short_Notes;")
          cursor_b=connection.execute(f"SELECT Title FROM Computer_Science_Books;")
          cursor_qa=connection.execute(f"SELECT Title FROM Computer_Science_QA;")
          cursor_misc=connection.execute(f"SELECT Title FROM Computer_Science_Misc;")
          cursor_msn=connection.execute(f"SELECT Title FROM Maths_Notes;")
          cursor_mssn=connection.execute(f"SELECT Title FROM Maths_Short_Notes;")
          cursor_mb=connection.execute(f"SELECT Title FROM Maths_Books;")
          cursor_mqa=connection.execute(f"SELECT Title FROM Maths_QA;")
          cursor_mmisc=connection.execute(f"SELECT Title FROM Maths_Misc;")
          l1=list(cursor_csn.fetchall())
          l2=list(cursor_cssn.fetchall())
          l3=list(cursor_b.fetchall())
          l4=list(cursor_qa.fetchall())
          l5=list(cursor_misc.fetchall())
          l6=list(cursor_msn.fetchall())
          l7=list(cursor_mssn.fetchall())
          l8=list(cursor_mb.fetchall())
          l9=list(cursor_mqa.fetchall())
          l10=list(cursor_mmisc.fetchall())
          total_len=len_csn+len_cssn+len_csb+len_csqa+len_csmisc+len_mn+len_msn+len_mb+len_mqa+len_mmisc
          cs_col_embed=discord.Embed(title="Computer Science Collection", description="You have the following categories to view from!", color=0xc7696e)
          cs_col_embed.set_image(url="https://i.pinimg.com/originals/fd/44/1c/fd441c8242af6ec35ada94496feb0901.gif")
          cs_col_embed.add_field(name="🔴", value="Notes", inline=False)
          cs_col_embed.add_field(name="🟠", value="Short Notes", inline=False)
          cs_col_embed.add_field(name="🟡", value="Books", inline=False)
          cs_col_embed.add_field(name="🟢", value="Q/A", inline=False)
          cs_col_embed.add_field(name="🟣", value="Miscellaneous", inline=False)
          
          maf_col_embed=discord.Embed(title="Mathematics Collection", description="You have the following categories to view from!", color=0xd19fae)
          maf_col_embed.add_field(name="🔴", value="Notes", inline=False)
          maf_col_embed.add_field(name="🟠", value="Short Notes", inline=False)
          maf_col_embed.add_field(name="🟡", value="Books", inline=False)
          maf_col_embed.add_field(name="🟢", value="Q/A", inline=False)
          maf_col_embed.add_field(name="🟣", value="Miscellaneous", inline=False)
          maf_col_embed.set_image(url="https://i.pinimg.com/originals/fd/44/1c/fd441c8242af6ec35ada94496feb0901.gif")
          for i in range(len_csn):
            element=l1[i]
            element=str(element)
            element=element[2:]
            element=element[:-3]
            linker=cursor.execute("SELECT Link from Computer_Science_Notes WHERE Title=:Tit", {'Tit': element})
            link = linker.fetchone()[0]
            link=str(link)
            csn_titles.append(element)
            csn_links.append(link)
          if len_csn<10:
            element=csn_titles[i]
            link=csn_links[i]
            cne.add_field(name=f"{i+1}. {element}", value=f"[Click here]({link})", inline=False)
          else:
            for i in range(10):
              element=csn_titles[i]
              link=csn_links[i]
              cne.add_field(name=f"{i+1}. {element}", value=f"[Click here]({link})", inline=False)
            
          for i in range(len_cssn):
            element=l2[i]
            element=str(element)
            element=element[2:]
            element=element[:-3]
            linker=cursor.execute("SELECT Link from Computer_Science_Short_Notes WHERE Title=:Tit", {'Tit': element})
            link = linker.fetchone()[0]
            link=str(link)
            cssn_titles.append(element)
            cssn_links.append(link)
          if len_cssn<10:
            for i in range(len_cssn):
              element=cssn_titles[i]
              link=cssn_links[i]
              csne.add_field(name=f"{i+1}. {element}", value=f"[Click here]({link})", inline=False)       
          else:
            for i in range(10):
              element=cssn_titles[i]
              link=cssn_links[i]
              csne.add_field(name=f"{i+1}. {element}", value=f"[Click here]({link})", inline=False)
          for i in range(len_csb):
            element=l3[i]
            element=str(element)
            element=element[2:]
            element=element[:-3]
            linker=cursor.execute("SELECT Link from Computer_Science_Books WHERE Title=:Tit", {'Tit': element})
            link = linker.fetchone()[0]
            link=str(link)
            csb_titles.append(element)
            csb_links.append(link)
          if len_csb<10:
            for i in range(len_csb):
              element=csb_titles[i]
              link=csb_links[i]
              cbe.add_field(name=f"{i+1}. {element}", value=f"[Click here]({link})", inline=False)
          else:
            for i in range(10):
              element=csb_titles[i]
              link=csb_links[i]
              cbe.add_field(name=f"{i+1}. {element}", value=f"[Click here]({link})", inline=False)
          for i in range(len_csqa):
            element=l4[i]
            element=str(element)
            element=element[2:]
            element=element[:-3]
            linker=cursor.execute("SELECT Link from Computer_Science_QA WHERE Title=:Tit", {'Tit': element})
            link = linker.fetchone()[0]
            link=str(link)
            csqa_titles.append(element)
            csqa_links.append(link)
          if len_csqa<10:
            for i in range(len_csqa):
              element=csqa_titles[i]
              link=csqa_links[i]
              cqae.add_field(name=f"{i+1}. {element}", value=f"[Click here]({link})", inline=False)
          else:
            for i in range(10):
              element=csqa_titles[i]
              link=csqa_links[i]
              cqae.add_field(name=f"{i+1}. {element}", value=f"[Click here]({link})", inline=False)
          for i in range(len_csmisc):
            element=l5[i]
            element=str(element)
            element=element[2:]
            element=element[:-3]
            linker=cursor.execute("SELECT Link from Computer_Science_Misc WHERE Title=:Tit", {'Tit': element})
            link = linker.fetchone()[0]
            link=str(link)
            csmisc_titles.append(element)
            csmisc_links.append(link)
          if len_csmisc<10:
            for i in range(len_csmisc):
              element=csmisc_titles[i]
              link=csmisc_links[i]
              cmisce.add_field(name=f"{i+1}. {element}", value=f"[Click here]({link})", inline=False)
          else:
            for i in range(10):
              element=csmisc_titles[i]
              link=csmisc_links[i]
              cmisce.add_field(name=f"{i+1}. {element}", value=f"[Click here]({link})", inline=False)
          ###
          for i in range(len_mn):
            element=l6[i]
            element=str(element)
            element=element[2:]
            element=element[:-3]
            linker=cursor.execute("SELECT Link from Maths_Notes WHERE Title=:Tit", {'Tit': element})
            link = linker.fetchone()[0]
            link=str(link)
            mn_titles.append(element)
            mn_links.append(link)
          if len_mn<10:
            for i in range(len_mn):
              element=mn_titles[i]
              link=mn_links[i]
              mne.add_field(name=f"{i+1}. {element}", value=f"[Click here]({link})", inline=False)
          else:
            for i in range(10):
              element=mn_titles[i]
              link=mn_links[i]
              mne.add_field(name=f"{i+1}. {element}", value=f"[Click here]({link})", inline=False)
          for i in range(len_msn):
            element=l7[i]
            element=str(element)
            element=element[2:]
            element=element[:-3]
            linker=cursor.execute("SELECT Link from Maths_Short_Notes WHERE Title=:Tit", {'Tit': element})
            link = linker.fetchone()[0]
            link=str(link)
            msn_titles.append(element)
            msn_links.append(link)
          if len_msn<10:
            for i in range(len_msn):
              element=msn_titles[i]
              link=msn_links[i]
              msne.add_field(name=f"{i+1}. {element}", value=f"[Click here]({link})", inline=False)
          else:
            for i in range(10):
              element=msn_titles[i]
              link=msn_links[i]
              msne.add_field(name=f"{i+1}. {element}", value=f"[Click here]({link})", inline=False)
          for i in range(len_mb):
            element=l8[i]
            element=str(element)
            element=element[2:]
            element=element[:-3]
            linker=cursor.execute("SELECT Link from Maths_Books WHERE Title=:Tit", {'Tit': element})
            link = linker.fetchone()[0]
            link=str(link)
            mb_titles.append(element)
            mb_links.append(link)
          if len_mb<10:
            for i in range(len_mb):
              element=mb_titles[i]
              link=mb_links[i]
              mbe.add_field(name=f"{i+1}. {element}", value=f"[Click here]({link})", inline=False)
          else:
            for i in range(10):
              element=mb_titles[i]
              link=mb_links[i]
              mbe.add_field(name=f"{i+1}. {element}", value=f"[Click here]({link})", inline=False)
          for i in range(len_mqa):
            element=l9[i]
            element=str(element)
            element=element[2:]
            element=element[:-3]
            linker=cursor.execute("SELECT Link from Maths_QA WHERE Title=:Tit", {'Tit': element})
            link = linker.fetchone()[0]
            link=str(link)
            mqa_titles.append(element)
            mqa_links.append(link)
          if len_mqa<10:
            for i in range(len_mqa):
              element=mqa_titles[i]
              link=mqa_links[i]
              mqae.add_field(name=f"{i+1}. {element}", value=f"[Click here]({link})", inline=False)
          else:
            for i in range(10):
              element=mqa_titles[i]
              link=mqa_links[i]
              mqae.add_field(name=f"{i+1}. {element}", value=f"[Click here]({link})", inline=False)
          for i in range(len_mmisc):
            element=l10[i]
            element=str(element)
            element=element[2:]
            element=element[:-3]
            linker=cursor.execute("SELECT Link from Maths_Misc WHERE Title=:Tit", {'Tit': element})
            link = linker.fetchone()[0]
            link=str(link)
            mmisc_titles.append(element)
            mmisc_links.append(link)
          if len_mmisc<10:
            for i in range(len_mmisc):
              element=mmisc_titles[i]
              link=mmisc_links[i]
              mmisce.add_field(name=f"{i+1}. {element}", value=f"[Click here]({link})", inline=False)
          else:
            for i in range(10):
              element=mmisc_titles[i]
              link=mmisc_links[i]
              mmisce.add_field(name=f"{i+1}. {element}", value=f"[Click here]({link})", inline=False)
          async def cs_callback(interaction):
            shelf_embed1=discord.Embed(title="Welcome to the Computer Science shelf!", description="What would you like to do?")
            shelf_embed1.set_image(url="https://data.whicdn.com/images/320858485/original.gif")
            await interaction.response.edit_message(embed=shelf_embed1, view=cscat_view)
          cs_button.callback=cs_callback
          async def maf_callback(interaction):
            global mafs 
            mafs=True
            shelf_embed2=discord.Embed(title="Welcome to the Mathematics library!", description="What would you like to do?")
            shelf_embed2.set_image(url="https://media0.giphy.com/media/Mmh3uG0srGGqFm5Vmw/giphy.gif")
            await interaction.response.edit_message(embed=shelf_embed2, view=mathcat_view)
          maths_button.callback=maf_callback
          
          async def maf_collection(interaction):
            await interaction.response.edit_message(embed=maf_col_embed, view=category_view)
          maths_catalog.callback=maf_collection
          async def cs_collection(interaction):
            await interaction.response.edit_message(embed=cs_col_embed, view=Ccategory_view)
          cs_catalog.callback=cs_collection
          async def comp_red(interaction):
            if len(csn_titles) <=10:
              await interaction.response.edit_message(embed=cne, view=csn_lessthanten)
            if len(csn_titles) > 10 and csn_index==0:
              await interaction.response.edit_message(embed=cne, view=csn_firstpage_view)
            if len(csn_titles)>10 and len(csn_titles)-csn_index>=10 and csn_index !=0:
              await interaction.response.edit_message(embed=cne, view=csn_view)
            if len(csn_titles)>10 and len(csn_titles)-csn_index<10:
              await interaction.response.edit_message(embed=cne, view=csn_lastpage_view)

          async def csn_next_callback(interaction):
            global csn_index
            csn_index+=10
            for i in range(10):
              cne.remove_field(0)
            len_elements=len(csn_titles)
            len_csn_elements=len_elements-csn_index
            if len_csn_elements <= 10:
              for j in range(csn_index,len_elements):
                title=csn_titles[j]
                link=csn_links[j]
                cne.add_field(name=f"{csn_index+j-9}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=cne, view=csn_lastpage_view)
            else:
              for j in range(csn_index,csn_index+10):
                title=csn_titles[j]
                link=csn_links[j]
                cne.add_field(name=f"{csn_index+j-9}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=cne, view=csn_view)
          async def csn_prev_callback(interaction):
            global csn_index
            csn_index-=10
            for i in range(10):
              cne.remove_field(0)
            len_elements=len(csn_titles)
            len_csn_elements=len_elements-csn_index
            if len_csn_elements >=10 and csn_index == 0:
              for j in range(csn_index,csn_index+10):
                title=csn_titles[j]
                link=csn_links[j]
                cne.add_field(name=f"{csn_index+j+1}. {title}", value=f"[Click here]({link})",inline=False)  
              await interaction.response.edit_message(embed=cne, view=csn_firstpage_view)
            if len_csn_elements >=10 and csn_index > 0:
              for j in range(csn_index,csn_index+10):
                title=csn_titles[j]
                link=csn_links[j]
                cne.add_field(name=f"{csn_index+j+1}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=cne, view=csn_view)
          csn_prev.callback=csn_prev_callback
          csn_next.callback=csn_next_callback
          Cnts.callback=comp_red
          async def comp_orange(interaction):
            if len(cssn_titles) <=10:
              await interaction.response.edit_message(embed=csne, view=cssn_lessthanten)
            if len(cssn_titles) > 10 and cssn_index==0:
              await interaction.response.edit_message(embed=csne, view=cssn_firstpage_view)
            if len(cssn_titles)>10 and len(cssn_titles)-cssn_index>=10 and cssn_index !=0:
              await interaction.response.edit_message(embed=csne, view=cssn_view)
            if len(cssn_titles)>10 and len(cssn_titles)-cssn_index<10:
              await interaction.response.edit_message(embed=csne, view=cssn_lastpage_view)
          Csnts.callback=comp_orange
          async def cssn_next_callback(interaction):
            global cssn_index
            cssn_index+=10
            for i in range(10):
              csne.remove_field(0)
            len_elements=len(cssn_titles)
            len_cssn_elements=len_elements-cssn_index
            if len_cssn_elements <= 10:
              for j in range(cssn_index,len_elements):
                title=cssn_titles[j]
                link=cssn_links[j]
                csne.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)   
              await interaction.response.edit_message(embed=csne, view=cssn_lastpage_view)
            else:
              for j in range(cssn_index,cssn_index+10):
                title=cssn_titles[j]
                link=cssn_links[j]
                csne.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=csne, view=cssn_view)
          async def cssn_prev_callback(interaction):
            global cssn_index
            cssn_index-=10
            for i in range(10):
              csne.remove_field(0)
            len_elements=len(cssn_titles)
            len_cssn_elements=len_elements-cssn_index
            if len_cssn_elements >=10 and cssn_index == 0:
              for j in range(cssn_index,cssn_index+10):
                title=cssn_titles[j]
                link=cssn_links[j]
                csne.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)     
              await interaction.response.edit_message(embed=csne, view=cssn_firstpage_view)
            if len_cssn_elements >=10 and cssn_index > 0:
              for j in range(cssn_index,cssn_index+10):
                title=cssn_titles[j]
                link=cssn_links[j]
                csne.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=csne, view=cssn_view)
          cssn_prev.callback=cssn_prev_callback
          cssn_next.callback=cssn_next_callback
          async def comp_yellow(interaction):
            if len(csb_titles) <=10:
              await interaction.response.edit_message(embed=cbe, view=csb_lessthanten)
            if len(csb_titles) > 10 and csb_index == 0:
              await interaction.response.edit_message(embed=cbe, view=csb_firstpage_view)
            if len(csb_titles)>10 and len(csb_titles)-csb_index>=10 and csb_index !=0:
              await interaction.response.edit_message(embed=cbe, view=csb_view)
            if len(csb_titles)>10 and len(csb_titles)-csb_index<10:
              await interaction.response.edit_message(embed=cbe, view=csb_lastpage_view)
          async def csb_next_callback(interaction):
            global csb_index
            csb_index+=10
            print(csb_index)
            for i in range(10):
              cbe.remove_field(0)
            len_elements=len(csb_titles)
            print(len_elements)
            len_csb_elements=len_elements-csb_index
            print(len_csb_elements)
            if len_csb_elements <= 10:
              for j in range(csb_index,len_elements):
                title=csb_titles[j]
                link=csb_links[j]
                cbe.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)     
              await interaction.response.edit_message(embed=cbe, view=csb_lastpage_view)
            else:
              for j in range(csb_index, csb_index+10):
                title=csb_titles[j]
                link=csb_links[j]
                cbe.add_field(name=f"{csb_index+j-9}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=cbe, view=csb_view)
          async def csb_prev_callback(interaction):
            global csb_index
            csb_index-=10
            print(csb_index)
            for i in range(10):
              cbe.remove_field(0)
            len_elements=len(csb_titles)
            print(len_elements)
            len_csb_elements=len_elements-csb_index
            print(len_csb_elements)
            if len_csb_elements>=10 and csb_index == 0:
              for j in range(csb_index,csb_index+10):
                title=csb_titles[j]
                link=csb_links[j]
                cbe.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)    
              await interaction.response.edit_message(embed=cbe, view=csb_firstpage_view)
            if len_csb_elements >=10 and csb_index > 0:
              for j in range(csb_index, csb_index+10):
                title=csb_titles[j]
                link=csb_links[j]
                cbe.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=cbe, view=csb_view)
          csb_prev.callback=csb_prev_callback
          csb_next.callback=csb_next_callback
          Cbook.callback=comp_yellow
          async def comp_green(interaction):
            if len(csqa_titles) <=10:
              await interaction.response.edit_message(embed=cqae, view=csqa_lessthanten)
            if len(csqa_titles) > 10 and csqa_index==0:
              await interaction.response.edit_message(embed=cqae, view=csqa_firstpage_view)
            if len(csqa_titles)>10 and len(csqa_titles)-csqa_index>=10 and csqa_index !=0:
              await interaction.response.edit_message(embed=cqae, view=csqa_view)
            if len(csqa_titles)>10 and len(csqa_titles)-csqa_index<10:
              await interaction.response.edit_message(embed=cqae, view=csqa_lastpage_view)
          Cqa.callback=comp_green
          async def csqa_next_callback(interaction):
            global csqa_index
            csqa_index+=10
            for i in range(10):
              cqae.remove_field(0)
            len_elements=len(csqa_titles)
            len_csqa_elements=len_elements-csqa_index
            if len_csqa_elements <= 10:
              for j in range(csqa_index,len_elements):
                title=csqa_titles[j]
                link=csqa_links[j]
                cqae.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)  
              await interaction.response.edit_message(embed=cqae, view=csqa_lastpage_view)
            else:
              for j in range(csqa_index,csqa_index+10):
                title=csqa_titles[j]
                link=csqa_links[j]
                cqae.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=cqae, view=csqa_view)
          async def csqa_prev_callback(interaction):
            global csqa_index
            csqa_index-=10
            for i in range(10):
              cqae.remove_field(0)
            len_elements=len(csqa_titles)
            len_csqa_elements=len_elements-csqa_index
            if len_csqa_elements >=10 and csqa_index == 0:
              for j in range(csqa_index,csqa_index+10):
                title=csqa_titles[j]
                link=csqa_links[j]
                cqae.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)     
              await interaction.response.edit_message(embed=cqae, view=csqa_firstpage_view)
            if len_csqa_elements >=10 and csqa_index > 0:
              for j in range(csqa_index,csqa_index+10):
                title=csqa_titles[j]
                link=csqa_links[j]
                cqae.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=cqae, view=csqa_view)
          csqa_prev.callback=csqa_prev_callback
          csqa_next.callback=csqa_next_callback
          async def comp_purple(interaction):
            if len(csmisc_titles) <=10:
              await interaction.response.edit_message(embed=cmisce, view=csmisc_lessthanten)
            if len(csmisc_titles) > 10 and csmisc_index==0:
              await interaction.response.edit_message(embed=cmisce, view=csmisc_firstpage_view)
            if len(csmisc_titles)>10 and len(csmisc_titles)-csmisc_index>=10 and csmisc_index !=0:
              await interaction.response.edit_message(embed=cmisce, view=csmisc_view)
            if len(csmisc_titles)>10 and len(csmisc_titles)-csmisc_index<10:
              await interaction.response.edit_message(embed=cmisce, view=csmisc_lastpage_view)
          Cmisc.callback=comp_purple
          async def csmisc_next_callback(interaction):
            global csmisc_index
            csmisc_index+=10
            for i in range(10):
              cmisce.remove_field(0)
            len_elements=len(csmisc_titles)
            len_csmisc_elements=len_elements-csmisc_index
            if len_csmisc_elements <= 10:
              for j in range(csmisc_index,len_elements):
                title=csmisc_titles[j]
                link=csmisc_links[j]
                cmisce.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=cmisce, view=csmisc_lastpage_view)
            else:
              for j in range(csmisc_index,csmisc_index+10):
                title=csmisc_titles[j]
                link=csmisc_links[j]
                cmisce.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=cmisce, view=csmisc_view)
          async def csmisc_prev_callback(interaction):
            global csmisc_index
            csmisc_index-=10
            for i in range(10):
              cmisce.remove_field(0)
            len_elements=len(csmisc_titles)
            len_csmisc_elements=len_elements-csmisc_index
            if len_csmisc_elements >=10 and csmisc_index == 0:
              for j in range(csmisc_index,csmisc_index+10):
                title=csmisc_titles[j]
                link=csmisc_links[j]
                cmisce.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)     
            if len_csmisc_elements >=10 and csmisc_index > 0:
              for j in range(csmisc_index,csmisc_index+10):
                title=csmisc_titles[j]
                link=csmisc_links[j]
                cmisce.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=cmisce, view=csmisc_firstpage_view)
          csmisc_prev.callback=csmisc_prev_callback
          csmisc_next.callback=csmisc_next_callback
          async def maf_red(interaction):
            if len(mn_titles) <=10:
              await interaction.response.edit_message(embed=mne, view=mn_lessthanten)
            if len(mn_titles) > 10 and mn_index==0:
              await interaction.response.edit_message(embed=mne, view=mn_firstpage_view)
            if len(mn_titles)>10 and len(mn_titles)-mn_index>=10 and mn_index !=0:
              await interaction.response.edit_message(embed=mne, view=mn_view)
            if len(mn_titles)>10 and len(mn_titles)-mn_index<10:
              await interaction.response.edit_message(embed=mne, view=mn_lastpage_view)
          nts.callback=maf_red
          async def mn_next_callback(interaction):
            global mn_index
            mn_index+=10
            for i in range(10):
              mne.remove_field(0)
            len_elements=len(mn_titles)
            len_mn_elements=len_elements-mn_index
            if len_mn_elements <= 10:
              for j in range(mn_index,len_elements):
                title=mn_titles[j]
                link=mn_links[j]
                mne.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=mne, view=mn_lastpage_view)
            else:
              for j in range(mn_index,mn_index+10):
                title=mn_titles[j]
                link=mn_links[j]
                mne.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=mne, view=msn_view)
          async def mn_prev_callback(interaction):
            global mn_index
            mn_index-=10
            for i in range(10):
              mne.remove_field(0)
            len_elements=len(mn_titles)
            len_mn_elements=len_elements-mn_index
            if len_mn_elements >=10 and mn_index == 0:
              for j in range(mn_index,mn_index+10):
                title=mn_titles[j]
                link=mn_links[j]
                mne.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=mne, view=mn_firstpage_view)
            if len_mn_elements >=10 and mn_index > 0:
              for j in range(mn_index,mn_index+10):
                title=mn_titles[j]
                link=mn_links[j]
                mne.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)
            await interaction.response.edit_message(embed=mne, view=mn_view)
          mn_prev.callback=mn_prev_callback
          mn_next.callback=mn_next_callback
          async def maf_orange(interaction):
            if len(msn_titles) <=10:
              await interaction.response.edit_message(embed=msne, view=msn_lessthanten)
            if len(msn_titles) > 10 and msn_index==0:
              await interaction.response.edit_message(embed=msne, view=msn_firstpage_view)
            if len(msn_titles)>10 and len(msn_titles)-msn_index>=10 and msn_index !=0:
              await interaction.response.edit_message(embed=msne, view=msn_view)
            if len(msn_titles)>10 and len(msn_titles)-msn_index<10:
              await interaction.response.edit_message(embed=msne, view=msn_lastpage_view)
          snts.callback=maf_orange
          async def msn_next_callback(interaction):
            global msn_index
            msn_index+=10
            for i in range(10):
              msne.remove_field(0)
            len_elements=len(msn_titles)
            len_msn_elements=len_elements-msn_index
            if len_msn_elements <= 10:
              for j in range(msn_index,len_elements):
                title=msn_titles[j]
                link=msn_links[j]
                msne.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=msne, view=msn_lastpage_view)
            else:
              for j in range(msn_index,msn_index+10):
                title=msn_titles[j]
                link=msn_links[j]
                msne.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=msne, view=msn_view)
          async def msn_prev_callback(interaction):
            global msn_index
            msn_index-=10
            for i in range(10):
              msne.remove_field(0)
            len_elements=len(msn_titles)
            len_msn_elements=len_elements-msn_index
            if len_msn_elements >= 10 and msn_index ==0:
              for j in range(msn_index,msn_index+10):
                title=msn_titles[j]
                link=msn_links[j]
                msne.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)  
              await interaction.response.edit_message(embed=msne, view=msn_firstpage_view)
            if len_msn_elements >= 10 and msn_index>0:
              for j in range(msn_index,msn_index+10):
                title=msn_titles[j]
                link=msn_links[j]
                msne.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=msne, view=msn_view)
          msn_prev.callback=msn_prev_callback
          msn_next.callback=msn_next_callback

          async def maf_yellow(interaction):
            if len(mb_titles) <=10:
              await interaction.response.edit_message(embed=mbe, view=mb_lessthanten)
            if len(mb_titles) > 10 and mb_index==0:
              await interaction.response.edit_message(embed=mbe, view=mb_firstpage_view)
            if len(mb_titles)>10 and len(mb_titles)-mb_index>=10 and mb_index !=0:
              await interaction.response.edit_message(embed=mbe, view=mb_view)
            if len(mb_titles)>10 and len(mb_titles)-mb_index<10:
              await interaction.response.edit_message(embed=mbe, view=mb_lastpage_view)
          book.callback=maf_yellow
          async def mb_next_callback(interaction):
            global mb_index
            mb_index+=10
            for i in range(10):
              mbe.remove_field(0)
            len_elements=len(mb_titles)
            len_mb_elements=len_elements-mb_index
            if len_mb_elements < 10:
              for j in range(mb_index,len_elements):
                title=mb_titles[j]
                link=mb_links[j]
                mbe.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False) 
              await interaction.response.edit_message(embed=mbe, view=mb_lastpage_view)
            else:
              for j in range(mb_index, mb_index+10):
                title=mb_titles[j]
                link=mb_links[j]
                mbe.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=mbe, view=mb_view)
          async def mb_prev_callback(interaction):
            global mb_index
            mb_index-=10
            for i in range(10):
              mbe.remove_field(0)
            len_elements=len(mb_titles)
            len_mb_elements=len_elements-mb_index
            if len_mb_elements >=10 and mb_index==0:
              for j in range(mb_index,mb_index+10):
                title=mb_titles[j]
                link=mb_links[j]
                mbe.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)   
              await interaction.response.edit_message(embed=mbe, view=mb_firstpage_view)
            if len_mb_elements >=10 and mb_index>0:
              for j in range(mb_index, mb_index+10):
                title=mb_titles[j]
                link=mb_links[j]
                mbe.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=mbe, view=mb_view)
          mb_prev.callback=mb_prev_callback
          mb_next.callback=mb_next_callback
        
          async def maf_green(interaction):
            if len(mqa_titles) <=10:
              await interaction.response.edit_message(embed=mqae, view=mqa_lessthanten)
            if len(mqa_titles) > 10 and mqa_index==0:
              await interaction.response.edit_message(embed=mqae, view=mqa_firstpage_view)
            if len(mqa_titles)>10 and len(mqa_titles)-mqa_index>=10 and mqa_index !=0:
              await interaction.response.edit_message(embed=mqae, view=mqa_view)
            if len(mqa_titles)>10 and len(mqa_titles)-mqa_index<10:
              await interaction.response.edit_message(embed=mqae, view=mqa_lastpage_view)
          qa.callback=maf_green
          async def mqa_next_callback(interaction):
            global mqa_index
            mqa_index+=10
            for i in range(10):
              mqae.remove_field(0)
            len_elements=len(mqa_titles)
            len_mqa_elements=len_elements-mqa_index
            if len_mqa_elements <= 10:
              for j in range(mqa_index,len_elements):
                title=mqa_titles[j]
                link=mqa_links[j]
                mqae.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)  
              await interaction.response.edit_message(embed=mqae, view=mqa_lastpage_view)
            else:
              for j in range(mqa_index,mqa_index+10):
                title=mqa_titles[j]
                link=mqa_links[j]
                mqae.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=mqae, view=mqa_view)
          async def mqa_prev_callback(interaction):
            global mqa_index
            mqa_index-=10
            for i in range(10):
              mqae.remove_field(0)
            len_elements=len(mqa_titles)
            len_mqa_elements=len_elements-mqa_index
            if len_mqa_elements >=10 and mqa_index == 0:
              for j in range(mqa_index,mqa_index+10):
                title=mqa_titles[j]
                link=mqa_links[j]
                mqae.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False) 
              await interaction.response.edit_message(embed=mqae, view=mqa_firstpage_view)
            if len_mqa_elements >=10 and mqa_index > 0:
              for j in range(mqa_index,mqa_index+10):
                title=mqa_titles[j]
                link=mqa_links[j]
                mqae.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=mqae, view=mqa_view)
          mqa_prev.callback=mqa_prev_callback
          mqa_next.callback=mqa_next_callback
          async def maf_purple(interaction):
            if len(mmisc_titles) <=10:
              await interaction.response.edit_message(embed=mmisce, view=mmisc_lessthanten)
            if len(mmisc_titles) > 10 and mmisc_index==0:
              await interaction.response.edit_message(embed=mmisce, view=mmisc_firstpage_view)
            if len(mmisc_titles)>10 and len(mmisc_titles)-mmisc_index>=10 and mmisc_index !=0:
              await interaction.response.edit_message(embed=mmisce, view=mmisc_view)
            if len(mmisc_titles)>10 and len(mmisc_titles)-mmisc_index<10:
              await interaction.response.edit_message(embed=mmisce, view=mmisc_lastpage_view)
          misc.callback=maf_purple
          async def mmisc_next_callback(interaction):
            global mmisc_index
            mmisc_index+=10
            for i in range(10):
              mmisce.remove_field(0)
            len_elements=len(mmisc_titles)
            len_mmisc_elements=len_elements-mmisc_index
            if len_mmisc_elements <= 10:
              for j in range(mmisc_index,len_elements):
                title=mmisc_titles[j]
                link=mmisc_links[j]
                mmisce.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False) 
              await interaction.response.edit_message(embed=mmisce, view=mmisc_lastpage_view)
            else:
              for j in range(mmisc_index, mmisc_index+10):
                title=mmisc_titles[j]
                link=mmisc_links[j]
                mmisce.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=mmisce, view=mmisc_view)
          async def mmisc_prev_callback(interaction):
            global mmisc_index
            mmisc_index-=10
            for i in range(10):
              mmisce.remove_field(0)
            len_elements=len(mmisc_titles)
            len_mmisc_elements=len_elements-mmisc_index
            if len_mmisc_elements >=10 and mmisc_index == 0:
              for j in range(mmisc_index,mmisc_index+10):
                title=mmisc_titles[j]
                link=mmisc_links[j]
                mmisce.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)     
              await interaction.response.edit_message(embed=mmisce, view=mmisc_firstpage_view)
            if len_mmisc_elements >=10 and mmisc_index>0:
              for j in range(mmisc_index, mmisc_index+10):
                title=mmisc_titles[j]
                link=mmisc_links[j]
                mmisce.add_field(name=f"{j+1}. {title}", value=f"[Click here]({link})",inline=False)
              await interaction.response.edit_message(embed=mmisce, view=mmisc_view)
          mmisc_prev.callback=mmisc_prev_callback
          mmisc_next.callback=mmisc_next_callback
          async def start_cs_int(interaction):
            shelf_embed1=discord.Embed(title="Welcome to the Computer Science shelf!", description="What would you like to do?")
            shelf_embed1.set_image(url="https://data.whicdn.com/images/320858485/original.gif")
            await interaction.response.edit_message(embed=shelf_embed1, view=cscat_view)
          select_cs.callback=start_cs_int
          async def start_maf_int(interaction):
            shelf_embed2=discord.Embed(title="Welcome to the Mathematics library!", description="What would you like to do?")
            shelf_embed2.set_image(url="https://media0.giphy.com/media/Mmh3uG0srGGqFm5Vmw/giphy.gif")
            await interaction.response.edit_message(embed=shelf_embed2, view=mathcat_view)
          select_math.callback=start_maf_int
          async def cscatalog_callback(interaction):
            await interaction.response.edit_message(embed=cs_col_embed, view=Ccategory_view)
          look_thru_cs.callback=cscatalog_callback
          async def mafcatalog_callback(interaction):
            await interaction.response.edit_message(embed=maf_col_embed, view=category_view)
          look_thru_math.callback=mafcatalog_callback    
          async def back_to_start_callback(interaction):
            await interaction.response.edit_message(embed=shelf_embed, view=view)
          back_to_start.callback=back_to_start_callback
          connection.close()


      @commands.slash_command(description="Add a file to collection.")
      async def add(self,ctx:discord.ApplicationContext, subject:Option(str, "Which subject best suits the addition to your collection?", required=True, choices=["Computer Science", "Mathematics"]),collection:Option(str, "Which collection will your addition best fit in?", required=True, choices=["Notes","Short Notes", "Books", "Q/A", "Miscellaneous"]), title:Option(str, "What would you like to call your addition?", required=True), link:Option(str, "Link to your file.", required=True)):
        connection=sqlite3.connect('shelf.sqlite')
        cursor=connection.cursor()
        if subject == "Computer Science":
          if collection=="Notes":
            connection.execute(f"INSERT INTO Computer_Science_Notes(Title,Link,User,User_ID,Guild) VALUES('{title}','{link}','{ctx.author}','{ctx.author.id}','{ctx.guild.id}')")
          if collection=="Short Notes":
            connection.execute(f"INSERT INTO Computer_Science_Short_Notes(Title,Link,User,User_ID,Guild) VALUES('{title}','{link}','{ctx.author}','{ctx.author.id}','{ctx.guild.id}')")
          if collection=="Books":
            connection.execute(f"INSERT INTO Computer_Science_Books(Title,Link,User,User_ID,Guild) VALUES('{title}','{link}','{ctx.author}','{ctx.author.id}','{ctx.guild.id}')") 
          if collection=="Q/A":
            connection.execute(f"INSERT INTO Computer_Science_QA (Title,Link,User,User_ID,Guild) VALUES('{title}','{link}','{ctx.author}','{ctx.author.id}','{ctx.guild.id}')")
          if collection=="Miscellaneous":
            connection.execute(f"INSERT INTO Computer_Science_Misc(Title,Link,User,User_ID,Guild) VALUES('{title}','{link}','{ctx.author}','{ctx.author.id}','{ctx.guild.id}')")
        if subject=="Mathematics":
          if collection=="Notes":
            connection.execute(f"INSERT INTO Maths_Notes(Title,Link,User,User_ID,Guild) VALUES('{title}','{link}','{ctx.author}','{ctx.author.id}','{ctx.guild.id}')")  
          if collection=="Short Notes":
            connection.execute(f"INSERT INTO Maths_Short_Notes(Title,Link,User,User_ID,Guild) VALUES('{title}','{link}','{ctx.author}','{ctx.author.id}','{ctx.guild.id}')")
          if collection=="Books":
            connection.execute(f"INSERT INTO Maths_Books(Title,Link,User,User_ID,Guild) VALUES('{title}','{link}','{ctx.author}','{ctx.author.id}','{ctx.guild.id}')")
          if collection=="Q/A":
            connection.execute(f"INSERT INTO Maths_QA(Title,Link,User,User_ID,Guild) VALUES('{title}','{link}','{ctx.author}','{ctx.author.id}','{ctx.guild.id}')")
          if collection=="Miscellaneous":
            connection.execute(f"INSERT INTO Maths_Misc(Title,Link,User,User_ID,Guild) VALUES ('{title}','{link}','{ctx.author}','{ctx.author.id}','{ctx.guild.id}')")     
        await ctx.respond(f"Added `{title}` to your `{subject} {collection}`!")
        connection.commit()
        connection.close()
      @commands.slash_command()
      async def search(self,ctx, query:Option(str, "Please specify what you'd like to search for...", required=True), subject:Option(str, "What subject is the file?", required=True, choices=["Computer Science", "Mathematics"])):
        embed=discord.Embed(title="`Searching... 🔎`", description=f"You searched for `{query}` in `{subject}`.")
        await ctx.send(embed=embed, delete_after=2)
        await asyncio.sleep(2)
        connection=sqlite3.connect('shelf.sqlite')
        cursor=connection.cursor()
        if subject == "Computer Science":
          cursor_csn=connection.execute(f"SELECT Title FROM Computer_Science_Notes WHERE Title LIKE '%{query}%';")
          cursor_cssn=connection.execute(f"SELECT Title FROM Computer_Science_Short_Notes WHERE Title LIKE '%{query}%';")
          cursor_b=connection.execute(f"SELECT Title FROM Computer_Science_Books WHERE Title LIKE '%{query}%';")
          cursor_qa=connection.execute(f"SELECT Title FROM Computer_Science_QA WHERE Title LIKE '%{query}%';")
          cursor_misc=connection.execute(f"SELECT Title FROM Computer_Science_Misc WHERE Title LIKE '%{query}%';")
          l1=list(cursor_csn.fetchall())
          l2=list(cursor_cssn.fetchall())
          l3=list(cursor_b.fetchall())
          l4=list(cursor_qa.fetchall())
          l5=list(cursor_misc.fetchall())
          result=discord.Embed(title=f"🔎 Search Result for `{query}` in `{subject}`.", description="---------------------------------------------------------------------------------------------", color=0x964B00)
          for i in range(len(l1)):
            element=l1[i]
            element=str(element)
            element=element[2:]
            element=element[:-3]
            linker=cursor.execute("SELECT Link from Computer_Science_Notes WHERE Title=:Tit", {'Tit': element})
            link = linker.fetchone()
            link=str(link)
            link=link[2:]
            link=link[:-3]
            result.add_field(name=f"🔎 {element} `found in Computer Science 🔴 Notes`", value=f"[Click here]({link})",inline=False)
          for i in range(len(l2)):
            element=l2[i]
            element=str(element)
            element=element[2:]
            element=element[:-3]
            linker=connection.execute("SELECT Link from Computer_Science_Short_Notes WHERE Title=:Tit", {'Tit': element})
            link = linker.fetchone()
            link=str(link)
            link=link[2:]
            link=link[:-3]
            result.add_field(name=f"🔎 {element} `found in Computer Science 🟠 Short Notes`", value=f"[Click here]({link})",inline=False) 
          for i in range(len(l3)):
            element=l3[i]
            element=str(element)
            element=element[2:]
            element=element[:-3]
            linker=cursor.execute("SELECT Link from Computer_Science_Books WHERE Title=:Tit", {'Tit': element})
            link = linker.fetchone()
            link=str(link)
            link=link[2:]
            link=link[:-3]
            result.add_field(name=f"🔎 {element} `found in Computer Science 🟡 Books`", value=f"[Click here]({link})",inline=False)
          for i in range(len(l4)):
            element=l4[i]
            element=str(element)
            element=element[2:]
            element=element[:-3]
            linker=cursor.execute("SELECT Link from Computer_Science_QA WHERE Title=:Tit", {'Tit': element})
            link = linker.fetchone()
            link=str(link)
            link=link[2:]
            link=link[:-3]
            result.add_field(name=f"🔎 {element} `found in Computer Science 🟢 Q/A`", value=f"[Click here]({link})",inline=False)
          for i in range(len(l5)):
            element=l5[i]
            element=str(element)
            element=element[2:]
            element=element[:-3]
            linker=cursor.execute("SELECT Link from Computer_Science_Misc WHERE Title=:Tit", {'Tit': element})
            link = linker.fetchone()
            link=str(link)
            link=link[2:]
            link=link[:-3]
            result.add_field(name=f"🔎 {element} `found in Computer Science 🟣 Miscellaneous`", value=f"[Click here]({link})",inline=False)
          await ctx.respond(embed=result)
        if subject == "Mathematics":
          cursor_msn=connection.execute(f"SELECT Title FROM Maths_Notes WHERE Title LIKE '%{query}%';")
          cursor_mssn=connection.execute(f"SELECT Title FROM Maths_Short_Notes WHERE Title LIKE '%{query}%';")
          cursor_mb=connection.execute(f"SELECT Title FROM Maths_Books WHERE Title LIKE '%{query}%';")
          cursor_mqa=connection.execute(f"SELECT Title FROM Maths_QA WHERE Title LIKE '%{query}%';")
          cursor_mmisc=connection.execute(f"SELECT Title FROM Maths_Misc WHERE Title LIKE '%{query}%';")
          l1=list(cursor_msn.fetchall())
          l2=list(cursor_mssn.fetchall())
          l3=list(cursor_mb.fetchall())
          l4=list(cursor_mqa.fetchall())
          l5=list(cursor_mmisc.fetchall())
          result=discord.Embed(title="Search Result", color=0x964B00)
          for i in range(len(l1)):
            element=l1[i]
            element=str(element)
            element=element[2:]
            element=element[:-3]
            linker=cursor.execute("SELECT Link from Maths_Notes WHERE Title=:Tit", {'Tit': element})
            link = linker.fetchone()
            link=str(link)
            link=link[2:]
            link=link[:-3]
            result.add_field(name=f"🔎 {element} `found in Mathematics 🔴 Notes`", value=f"[Click here]({link})",inline=False)
          for i in range(len(l2)):
            element=l2[i]
            element=str(element)
            element=element[2:]
            element=element[:-3]
            linker=connection.execute("SELECT Link from Maths_Short_Notes WHERE Title=:Tit", {'Tit': element})
            link = linker.fetchone()
            link=str(link)
            link=link[2:]
            link=link[:-3]
            result.add_field(name=f"🔎 {element} `found in Mathematics 🟠 Short Notes`", value=f"[Click here]({link})",inline=False) 
          for i in range(len(l3)):
            element=l3[i]
            element=str(element)
            element=element[2:]
            element=element[:-3]
            linker=cursor.execute("SELECT Link from Maths_Books WHERE Title=:Tit", {'Tit': element})
            link = linker.fetchone()
            link=str(link)
            link=link[2:]
            link=link[:-3]
            result.add_field(name=f"🔎 {element} `found in Mathematics 🟡 Books`", value=f"[Click here]({link})",inline=False)
          for i in range(len(l4)):
            element=l4[i]
            element=str(element)
            element=element[2:]
            element=element[:-3]
            linker=cursor.execute("SELECT Link from Maths_QA WHERE Title=:Tit", {'Tit': element})
            link = linker.fetchone()
            link=str(link)
            link=link[2:]
            link=link[:-3]
            result.add_field(name=f"🔎 {element} `found in Mathematics 🟢 Q/A`", value=f"[Click here]({link})",inline=False)
          for i in range(len(l5)):
            element=l5[i]
            element=str(element)
            element=element[2:]
            element=element[:-3]
            linker=cursor.execute("SELECT Link from Maths_Misc WHERE Title=:Tit", {'Tit': element})
            link = linker.fetchone()
            link=str(link)
            link=link[2:]
            link=link[:-3]
            result.add_field(name=f"🔎 {element} `found in Mathematics 🟣 Miscellaneous`", value=f"[Click here]({link})",inline=False)
          await ctx.respond(embed=result)
        connection.close()

      @commands.slash_command(description="Update an entry. Get all your entries using /uploads.")
      async def update(self, ctx, subject:Option(str, required=True, choices=["Computer Science","Mathematics"]), collection:Option(str, "Which category does it belong to?", required=True, choices=["Notes","Short Notes", "Books", "Q/A", "Miscellaneous"]), element:Option(str, "What would you like to update?", choices=["Title", "Link"]), title:Option(str, "This is the title of the file that needs to be updated. Note that it should be word to word.", required=True), query:Option(str, "What would you like to update the 'element' to?", required=True)):
        title=str(title)
        element=str(element)
        query=str(query)
        connection=sqlite3.connect('shelf.sqlite')
        cursor=connection.cursor()
        if subject == "Computer Science":
          if collection=="Notes":
            user=cursor.execute("SELECT User_ID FROM Computer_Science_Notes WHERE Title=:Tit",{'Tit':title})
            user=user.fetchone()[0]
            link=cursor.execute("SELECT Link FROM Computer_Science_Notes WHERE Title=:Tit",{'Tit':title})
            link=link.fetchone()[0]
            link=str(link)
            UNIQUE_ID=cursor.execute("SELECT ID FROM Computer_Science_Notes WHERE Title=:Tit",{'Tit':title})
            UNIQUE_ID=UNIQUE_ID.fetchone()[0]
            UNIQUE_ID=int(UNIQUE_ID)
            findex=UNIQUE_ID-1
            user=int(user)
            print(user)
            if ctx.author.id==user and element=="Link":
              cursor.execute(f"UPDATE Computer_Science_Notes SET Link=? WHERE Title=?",(query,title))
              connection.commit()
              await ctx.respond(f"Successfully updated {title}'s {element} to {query}!")
            if ctx.author.id==user and element=="Title":
              cursor.execute(f"UPDATE Computer_Science_Notes SET Title=? WHERE Title=?",(query,title))
              connection.commit()
              await ctx.respond(f"Successfully updated {title}'s {element} to {query}!")
            if ctx.author.id!=user:
              await ctx.respond("Sorry, you don't seem to be the uploader of the file.")
          if collection=="Short Notes":
            user=cursor.execute("SELECT User_ID FROM Computer_Science_Short_Notes WHERE Title=:Tit",{'Tit':title})
            user=user.fetchone()[0]
            link=cursor.execute("SELECT Link FROM Computer_Science_Short_Notes WHERE Title=:Tit",{'Tit':title})
            link=link.fetchone()[0]
            link=str(link)
            UNIQUE_ID=cursor.execute("SELECT ID FROM Computer_Science_Short_Notes WHERE Title=:Tit",{'Tit':title})
            UNIQUE_ID=UNIQUE_ID.fetchone()[0]
            UNIQUE_ID=int(UNIQUE_ID)
            findex=UNIQUE_ID-1
            user=int(user)
            print(user)
            if ctx.author.id==user and element=="Link":
              cursor.execute(f"UPDATE Computer_Science_Short_Notes SET Link=? WHERE Title=?",(query,title))
              connection.commit()
              await ctx.respond(f"Successfully updated {title}'s {element} to {query}!")
            if ctx.author.id==user and element=="Title":
              cursor.execute(f"UPDATE Computer_Science_Short_Notes SET Title=? WHERE Title=?",(query,title))
              connection.commit()
              await ctx.respond(f"Successfully updated {title}'s {element} to {query}!")
            if ctx.author.id!=user:
              await ctx.respond("Sorry, you don't seem to be the uploader of the file.")
          if collection=="Books":
            user=cursor.execute("SELECT User_ID FROM Computer_Science_Books WHERE Title=:Tit",{'Tit':title})
            user=user.fetchone()[0]
            UNIQUE_ID=cursor.execute("SELECT ID FROM Computer_Science_Books WHERE Title=:Tit",{'Tit':title})
            UNIQUE_ID=UNIQUE_ID.fetchone()[0]
            UNIQUE_ID=int(UNIQUE_ID)
            findex=UNIQUE_ID-1
            link=cursor.execute("SELECT Link FROM Computer_Science_Books WHERE Title=:Tit",{'Tit':title})
            link=link.fetchone()[0]
            link=str(link)
            user=int(user)
            print(user)
            if ctx.author.id==user and element=="Link":
              cursor.execute(f"UPDATE Computer_Science_Books SET Link=? WHERE Title=?",(query,title))
              connection.commit()
              await ctx.respond(f"Successfully updated {title}'s {element} to {query}!")
            if ctx.author.id==user and element=="Title":
              cursor.execute(f"UPDATE Computer_Science_Books SET Title=? WHERE Title=?",(query,title))
              connection.commit()
              await ctx.respond(f"Successfully updated {title}'s {element} to {query}!")
            if ctx.author.id!=user:
              await ctx.respond("Sorry, you don't seem to be the uploader of the file.")
          if collection=="Q/A":
            user=cursor.execute("SELECT User_ID FROM Computer_Science_QA WHERE Title=:Tit",{'Tit':title})
            user=user.fetchone()[0]
            link=cursor.execute("SELECT Link FROM Computer_Science_QA WHERE Title=:Tit",{'Tit':title})
            link=link.fetchone()[0]
            link=str(link)
            UNIQUE_ID=cursor.execute("SELECT ID FROM Computer_Science_QA WHERE Title=:Tit",{'Tit':title})
            UNIQUE_ID=UNIQUE_ID.fetchone()[0]
            UNIQUE_ID=int(UNIQUE_ID)
            findex=UNIQUE_ID-1
            user=int(user)
            print(user)
            if ctx.author.id==user and element=="Link":
              cursor.execute(f"UPDATE Computer_Science_QA SET Link=? WHERE Title=?",(query,title))
              connection.commit()
              await ctx.respond(f"Successfully updated {title}'s {element} to {query}!")
            if ctx.author.id==user and element=="Title":
              cursor.execute(f"UPDATE Computer_Science_QA SET Title=? WHERE Title=?",(query,title))
              connection.commit()
              await ctx.respond(f"Successfully updated {title}'s {element} to {query}!")
            if ctx.author.id!=user:
              await ctx.respond("Sorry, you don't seem to be the uploader of the file.")
          if collection=="Miscellaneous":
            user=cursor.execute("SELECT User_ID FROM Computer_Science_Misc WHERE Title=:Tit",{'Tit':title})
            user=user.fetchone()[0]
            link=cursor.execute("SELECT Link FROM Computer_Science_Misc WHERE Title=:Tit",{'Tit':title})
            link=link.fetchone()[0]
            link=str(link)
            UNIQUE_ID=cursor.execute("SELECT ID FROM Computer_Science_Misc WHERE Title=:Tit",{'Tit':title})
            UNIQUE_ID=UNIQUE_ID.fetchone()[0]
            UNIQUE_ID=int(UNIQUE_ID)
            findex=UNIQUE_ID-1
            user=int(user)
            print(user)
            if ctx.author.id==user and element=="Link":
              cursor.execute(f"UPDATE Computer_Science_Misc SET Link=? WHERE Title=?",(query,title))
              connection.commit()
              await ctx.respond(f"Successfully updated {title}'s {element} to {query}!")
            if ctx.author.id==user and element=="Title":
              cursor.execute(f"UPDATE Computer_Science_Misc SET Title=? WHERE Title=?",(query,title))
              connection.commit()
              await ctx.respond(f"Successfully updated {title}'s {element} to {query}!")
            if ctx.author.id!=user:
              await ctx.respond("Sorry, you don't seem to be the uploader of the file.")
        if subject=="Mathematics":
          if collection=="Notes":
            user=cursor.execute("SELECT User_ID FROM Maths_Notes WHERE Title=:Tit",{'Tit':title})
            user=user.fetchone()[0]
            link=cursor.execute("SELECT Link FROM Maths_Notes WHERE Title=:Tit",{'Tit':title})
            link=link.fetchone()[0]
            link=str(link)
            UNIQUE_ID=cursor.execute("SELECT ID FROM Maths_Notes WHERE Title=:Tit",{'Tit':title})
            UNIQUE_ID=UNIQUE_ID.fetchone()[0]
            UNIQUE_ID=int(UNIQUE_ID)
            findex=UNIQUE_ID-1
            user=int(user)
            if ctx.author.id==user and element=='Link':
              cursor.execute("UPDATE Maths_Notes SET Link=? WHERE Title=?",(query,title))
              connection.commit()
              await ctx.respond(f"Successfully updated {title}'s {element} to {query}!")
            if ctx.author.id==user and element=='Title':
              cursor.execute("UPDATE Maths_Notes SET Title=? WHERE Title=?",(query, title))
              connection.commit()
              await ctx.respond(f"Successfully updated {title}'s {element} to {query}!")              
            if ctx.author.id!=user:
              await ctx.respond("Sorry, you don't seem to be the uploader of the file.")
          if collection=="Short Notes":
            user=cursor.execute("SELECT User_ID FROM Maths_Short_Notes WHERE Title=:Tit",{'Tit':title})
            user=user.fetchone()[0]
            link=cursor.execute("SELECT Link FROM Maths_Short_Notes WHERE Title=:Tit",{'Tit':title})
            link=link.fetchone()[0]
            link=str(link)
            UNIQUE_ID=cursor.execute("SELECT ID FROM Maths_Short_Notes WHERE Title=:Tit",{'Tit':title})
            UNIQUE_ID=UNIQUE_ID.fetchone()[0]
            UNIQUE_ID=int(UNIQUE_ID)
            findex=UNIQUE_ID-1
            user=int(user)
            print(user)
            if ctx.author.id==user and element=='Link':
              cursor.execute("UPDATE Maths_Short_Notes SET Link=? WHERE Title=?",(query,title))
              connection.commit()
              await ctx.respond(f"Successfully updated {title}'s {element} to {query}!")
            if ctx.author.id==user and element=='Title':
              cursor.execute("UPDATE Maths_Short_Notes SET Title=? WHERE Title=?",(query, title))
              connection.commit()
              await ctx.respond(f"Successfully updated {title}'s {element} to {query}!")           
            if ctx.author.id!=user:
              await ctx.respond("Sorry, you don't seem to be the uploader of the file.")
          if collection=="Books":
            user=cursor.execute("SELECT User_ID FROM Maths_Books WHERE Title=:Tit",{'Tit':title})
            user=user.fetchone()[0]
            link=cursor.execute("SELECT Link FROM Maths_Books WHERE Title=:Tit",{'Tit':title})
            link=link.fetchone()[0]
            link=str(link)
            UNIQUE_ID=cursor.execute("SELECT ID FROM Maths_Books WHERE Title=:Tit",{'Tit':title})
            UNIQUE_ID=UNIQUE_ID.fetchone()[0]
            UNIQUE_ID=int(UNIQUE_ID)
            findex=UNIQUE_ID-1
            user=int(user)
            print(user)
            if ctx.author.id==user and element=='Link':
              cursor.execute("UPDATE Maths_Books SET Link=? WHERE Title=?",(query,title))
              connection.commit()
              await ctx.respond(f"Successfully updated {title}'s {element} to {query}!")
            if ctx.author.id==user and element=='Title':
              cursor.execute("UPDATE Maths_Books SET Title=? WHERE Title=?",(query, title))
              connection.commit()
              await ctx.respond(f"Successfully updated {title}'s {element} to {query}!") 
            if ctx.author.id!=user:
              await ctx.respond("Sorry, you don't seem to be the uploader of the file.")
          if collection=="Q/A":
            user=cursor.execute("SELECT User_ID FROM Maths_QA WHERE Title=:Tit",{'Tit':title})
            user=user.fetchone()[0]
            link=cursor.execute("SELECT Link FROM Maths_QA WHERE Title=:Tit",{'Tit':title})
            link=link.fetchone()[0]
            link=str(link)
            UNIQUE_ID=cursor.execute("SELECT ID FROM Maths_QA WHERE Title=:Tit",{'Tit':title})
            UNIQUE_ID=UNIQUE_ID.fetchone()[0]
            UNIQUE_ID=int(UNIQUE_ID)
            findex=UNIQUE_ID-1
            user=int(user)
            print(user)
            if ctx.author.id==user and element=='Link':
              cursor.execute("UPDATE Maths_QA SET Link=? WHERE Title=?",(query,title))
              connection.commit()
              await ctx.respond(f"Successfully updated {title}'s {element} to {query}!")
            if ctx.author.id==user and element=='Title':
              cursor.execute("UPDATE Maths_QA SET Title=? WHERE Title=?",(query, title))
              connection.commit()
              await ctx.respond(f"Successfully updated {title}'s {element} to {query}!")           
            if ctx.author.id!=user:
              await ctx.respond("Sorry, you don't seem to be the uploader of the file.")
          if collection=="Miscellaneous":
            user=cursor.execute("SELECT User_ID FROM Maths_Misc WHERE Title=:Tit",{'Tit':title})
            user=user.fetchone()[0]
            link=cursor.execute("SELECT Link FROM Maths_Misc WHERE Title=:Tit",{'Tit':title})
            link=link.fetchone()[0]
            link=str(link)
            UNIQUE_ID=cursor.execute("SELECT ID FROM Maths_Misc WHERE Title=:Tit",{'Tit':title})
            UNIQUE_ID=UNIQUE_ID.fetchone()[0]
            UNIQUE_ID=int(UNIQUE_ID)
            findex=UNIQUE_ID-1
            user=int(user)
            print(user)
            if ctx.author.id==user and element=='Link':
              cursor.execute("UPDATE Maths_Misc SET Link=? WHERE Title=?",(query,title))
              connection.commit()
              await ctx.respond(f"Successfully updated {title}'s {element} to {query}!")
            if ctx.author.id==user and element=='Title':
              cursor.execute("UPDATE Maths_Misc SET Title=? WHERE Title=?",(query, title))
              connection.commit()
              await ctx.respond(f"Successfully updated {title}'s {element} to {query}!")           
            if ctx.author.id!=user:
              await ctx.respond("Sorry, you don't seem to be the uploader of the file.")     
        connection.close()

      @commands.slash_command(description="Send feedback.")
      async def suggestions(self,ctx,suggestion):
        connection=sqlite3.connect('shelf.sqlite')
        cursor=connection.cursor()
        cursor.execute(f"INSERT INTO Suggestions(Feedback,User,Guild) VALUES ('{suggestion}', '{ctx.author}', '{ctx.guild.id}');")
        connection.commit()
        await ctx.respond("Your feedback has been recorded! Thank you <3", delete_after=5)
        connection.close()

      @commands.slash_command(description="Gives a list of titles of all of user's uploads.")
      async def uploads(self,ctx):
        connection=sqlite3.connect('shelf.sqlite')
        cursor=connection.cursor()
        t1=connection.execute("SELECT Title FROM Computer_Science_Notes WHERE User_ID=:User",{'User':ctx.author.id})
        t2=connection.execute("SELECT Title FROM Computer_Science_Short_Notes WHERE User_ID=:User",{'User':ctx.author.id})
        t3=connection.execute('SELECT Title FROM Computer_Science_Books WHERE User_ID=:User',{'User':ctx.author.id})
        t4=connection.execute("SELECT Title FROM Computer_Science_QA WHERE User_ID=:User",{'User':ctx.author.id})
        t5=connection.execute("SELECT Title FROM Computer_Science_Misc WHERE User_ID=:User",{'User':ctx.author.id})      
        t6=connection.execute("SELECT Title FROM Maths_Notes WHERE User_ID=:User",{'User':ctx.author.id})
        t7=connection.execute("SELECT Title FROM Maths_Short_Notes WHERE User_ID=:User",{'User':ctx.author.id})
        t8=connection.execute("SELECT Title FROM Maths_Books WHERE User_ID=:User",{'User':ctx.author.id})
        t9=connection.execute("SELECT Title FROM Maths_QA WHERE User_ID=:User",{'User':ctx.author.id})
        t10=connection.execute("SELECT Title FROM Maths_Misc WHERE User_ID=:User",{'User':ctx.author.id})              
        t1=list(t1.fetchall())
        t2=list(t2.fetchall())
        t3=list(t3.fetchall())
        t4=list(t4.fetchall())
        t5=list(t5.fetchall())
        t6=list(t6.fetchall())
        t7=list(t7.fetchall())
        t8=list(t8.fetchall())
        t9=list(t9.fetchall())
        t10=list(t10.fetchall())
        t_all=t1+t2+t3+t4+t5+t6+t7+t8+t9+t10
        lentall=len(t_all)
        tembed=discord.Embed(title="Uploads.", description=f"Uploads for {ctx.author}", color=0x964B00)
        for i in range(lentall):
          title=t_all[i]
          title=str(title)
          title=title[2:]
          title=title[:-3]
          tembed.add_field(name=f"{i+1}. {title}", value=f"------------", inline=False)
        await ctx.respond(embed=tembed)



      @commands.slash_command()
      async def delete(self, ctx, subject:Option(str, required=True, choices=["Computer Science","Mathematics"]), collection:Option(str, "Which category does it belong to?", required=True, choices=["Notes","Short Notes", "Books", "Q/A", "Miscellaneous"]), title:Option(str, "This is the title of the file that needs to be deleted. Note that it should be word to word.", required=True)):
        connection=sqlite3.connect('shelf.sqlite')
        cursor=connection.cursor()
        if subject == "Computer Science" and collection=="Notes":
          user=cursor.execute("SELECT User_ID FROM Computer_Science_Notes WHERE Title=:Tit",{'Tit':title})
          user=user.fetchone()[0]
          UNIQUE_ID=cursor.execute("SELECT ID FROM Computer_Science_Notes WHERE Title=:Tit",{'Tit':title})
          UNIQUE_ID=UNIQUE_ID.fetchone()[0]
          UNIQUE_ID=int(UNIQUE_ID)
          findex=UNIQUE_ID-1
          user=int(user)
          if ctx.author.id==user:
            cursor.execute("DELETE FROM Computer_Science_Notes WHERE Title=?",(title,))
            await ctx.respond(f"Successfully deleted `{title}` from the library.")
            connection.commit()
          else:
            await ctx.respond("Sorry, you are not allowed to delete the file as you did not upload it.", delete_after=3)
        if subject == "Computer Science" and collection=="Short Notes":
          user=cursor.execute("SELECT User_ID FROM Computer_Science_Short_Notes WHERE Title=:Tit",{'Tit':title})
          user=user.fetchone()[0]
          UNIQUE_ID=cursor.execute("SELECT ID FROM Computer_Science_Short_Notes WHERE Title=:Tit",{'Tit':title})
          UNIQUE_ID=UNIQUE_ID.fetchone()[0]
          UNIQUE_ID=int(UNIQUE_ID)
          findex=UNIQUE_ID-1
          user=int(user)
          if ctx.author.id==user:
            cursor.execute("DELETE FROM Computer_Science_Short_Notes WHERE Title=?",(title,))
            await ctx.respond(f"Successfully deleted `{title}` from the library.")
            connection.commit()
          else:
            await ctx.respond("Sorry, you are not allowed to delete the file as you did not upload it.", delete_after=3)
        if subject == "Computer Science" and collection=="Books":
          user=cursor.execute("SELECT User_ID FROM Computer_Science_Books WHERE Title=:Tit",{'Tit':title})
          user=user.fetchone()[0]
          UNIQUE_ID=cursor.execute("SELECT ID FROM Computer_Science_Books WHERE Title=:Tit",{'Tit':title})
          UNIQUE_ID=UNIQUE_ID.fetchone()[0]
          UNIQUE_ID=int(UNIQUE_ID)
          findex=UNIQUE_ID-1
          user=int(user)
          if ctx.author.id==user:
            cursor.execute("DELETE FROM Computer_Science_Books WHERE Title=?",(title,))
            await ctx.respond(f"Successfully deleted `{title}` from the library.")
            connection.commit()
          else:
            await ctx.respond("Sorry, you are not allowed to delete the file as you did not upload it.", delete_after=3)
        if subject == "Computer Science" and collection=="Q/A":
          user=cursor.execute("SELECT User_ID FROM Computer_Science_QA WHERE Title=:Tit",{'Tit':title})
          user=user.fetchone()[0]
          UNIQUE_ID=cursor.execute("SELECT ID FROM Computer_Science_QA WHERE Title=:Tit",{'Tit':title})
          UNIQUE_ID=UNIQUE_ID.fetchone()[0]
          UNIQUE_ID=int(UNIQUE_ID)
          findex=UNIQUE_ID-1
          user=int(user)
          if ctx.author.id==user:
            cursor.execute("DELETE FROM Computer_Science_QA WHERE Title=?",(title,))
            await ctx.respond(f"Successfully deleted `{title}` from the library.")
            connection.commit()
          else:
            await ctx.respond("Sorry, you are not allowed to delete the file as you did not upload it.", delete_after=3)
        if subject == "Computer Science" and collection=="Miscellaneous":
          user=cursor.execute("SELECT User_ID FROM Computer_Science_Misc WHERE Title=:Tit",{'Tit':title})
          user=user.fetchone()[0]
          UNIQUE_ID=cursor.execute("SELECT ID FROM Computer_Science_Misc WHERE Title=:Tit",{'Tit':title})
          UNIQUE_ID=UNIQUE_ID.fetchone()[0]
          UNIQUE_ID=int(UNIQUE_ID)
          findex=UNIQUE_ID-1
          user=int(user)
          if ctx.author.id==user:
            cursor.execute("DELETE FROM Computer_Science_Misc WHERE Title=?",(title,))
            await ctx.respond(f"Successfully deleted `{title}` from the library.")
            connection.commit()
          else:
            await ctx.respond("Sorry, you are not allowed to delete the file as you did not upload it.", delete_after=3)
        if subject == "Mathematics" and collection=="Notes":
          user=cursor.execute("SELECT User_ID FROM Maths_Notes WHERE Title=:Tit",{'Tit':title})
          user=user.fetchone()[0]
          UNIQUE_ID=cursor.execute("SELECT ID FROM Maths_Notes WHERE Title=:Tit",{'Tit':title})
          UNIQUE_ID=UNIQUE_ID.fetchone()[0]
          UNIQUE_ID=int(UNIQUE_ID)
          findex=UNIQUE_ID-1
          user=int(user)
          if ctx.author.id==user:
            cursor.execute("DELETE FROM Maths_Notes WHERE Title=?",(title,))
            await ctx.respond(f"Successfully deleted `{title}` from the library.")
            connection.commit()
          else:
            await ctx.respond("Sorry, you are not allowed to delete the file as you did not upload it.", delete_after=3)
        if subject == "Mathematics" and collection=="Short Notes":
          user=cursor.execute("SELECT User_ID FROM Maths_Short_Notes WHERE Title=:Tit",{'Tit':title})
          user=user.fetchone()[0]
          UNIQUE_ID=cursor.execute("SELECT ID FROM Maths_Short_Notes WHERE Title=:Tit",{'Tit':title})
          UNIQUE_ID=UNIQUE_ID.fetchone()[0]
          UNIQUE_ID=int(UNIQUE_ID)
          findex=UNIQUE_ID-1
          user=int(user)
          if ctx.author.id==user:
            cursor.execute("DELETE FROM Maths_Short_Notes WHERE Title=?",(title,))
            await ctx.respond(f"Successfully deleted `{title}` from the library.")
            connection.commit()
          else:
            await ctx.respond("Sorry, you are not allowed to delete the file as you did not upload it.", delete_after=3)
        if subject == "Mathematics" and collection=="Books":
          user=cursor.execute("SELECT User_ID FROM Maths_Books WHERE Title=:Tit",{'Tit':title})
          user=user.fetchone()[0]
          UNIQUE_ID=cursor.execute("SELECT ID FROM Maths_Books WHERE Title=:Tit",{'Tit':title})
          UNIQUE_ID=UNIQUE_ID.fetchone()[0]
          UNIQUE_ID=int(UNIQUE_ID)
          findex=UNIQUE_ID-1
          user=int(user)
          if ctx.author.id==user:
            cursor.execute("DELETE FROM Maths_Books WHERE Title=?",(title,))
            await ctx.respond(f"Successfully deleted `{title}` from the library.")
            connection.commit()
          else:
            await ctx.respond("Sorry, you are not allowed to delete the file as you did not upload it.", delete_after=3)
        if subject == "Mathematics" and collection=="Q/A":
          user=cursor.execute("SELECT User_ID FROM Maths_QA WHERE Title=:Tit",{'Tit':title})
          user=user.fetchone()[0]
          UNIQUE_ID=cursor.execute("SELECT ID FROM Maths_QA WHERE Title=:Tit",{'Tit':title})
          UNIQUE_ID=UNIQUE_ID.fetchone()[0]
          UNIQUE_ID=int(UNIQUE_ID)
          findex=UNIQUE_ID-1
          user=int(user)
          if ctx.author.id==user:
            cursor.execute("DELETE FROM Maths_QA WHERE Title=?",(title,))
            await ctx.respond(f"Successfully deleted `{title}` from the library.")
            connection.commit()
          else:
            await ctx.respond("Sorry, you are not allowed to delete the file as you did not upload it.", delete_after=3)
        if subject == "Mathematics" and collection=="Miscellaneous":
          user=cursor.execute("SELECT User_ID FROM Maths_Misc WHERE Title=:Tit",{'Tit':title})
          user=user.fetchone()[0]
          UNIQUE_ID=cursor.execute("SELECT ID FROM Maths_Misc WHERE Title=:Tit",{'Tit':title})
          UNIQUE_ID=UNIQUE_ID.fetchone()[0]
          UNIQUE_ID=int(UNIQUE_ID)
          findex=UNIQUE_ID-1
          user=int(user)
          print(user)
          if ctx.author.id==user:
            cursor.execute("DELETE FROM Maths_Misc WHERE Title=?",(title,))
            await ctx.respond(f"Successfully deleted `{title}` from the library.")
            connection.commit()
          else:
            await ctx.respond("Sorry, you are not allowed to delete the file as you did not upload it.", delete_after=3)
        connection.close()




def setup(bot):
  bot.add_cog(Shelf(bot))