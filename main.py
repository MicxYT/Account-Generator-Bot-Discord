credits="""
        _      _              
  /\/\ (_) ___| | _____ _   _ 
 /    \| |/ __| |/ / _ \ | | |
/ /\/\ \ | (__|   <  __/ |_| |
\/    \/_|\___|_|\_\___|\__, |
                        |___/ 
ADD ME ON DISCORD  The Young Mickey#0139
OR JOIN THE DISCORD SERVER https://discord.gg/ZPXrpjUJkC
IF YOU WANT A BETTER BOT, WE CAN PROVIDE. THIS IS FOR FREE AND NOT MUCH WORK WAS PUT INTO IT
"""







#ACCOUNT FILE NAMES NEED TO BE LOWERCASED
print(credits)
import discord,json,os,random
from discord.ext import commands

with open("config.json") as file: # Load the config file
    info = json.load(file)
    token = info["token"]
    delete = info["autodelete"]
    prefix = info["prefix"]

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Bot Running!")
@bot.command() # Stock command
async def stock(ctx):
    stockmenu = discord.Embed(title="Account Stock",description="") # Define the embed
    for filename in os.listdir("Accounts"):
        with open("Accounts\\"+filename) as f: # Open every file in the accounts folder
            ammount = len(f.read().splitlines()) # Get the ammount of lines
            name = (filename[0].upper() + filename[1:].lower()).replace(".txt","") #Make the name look nice
            stockmenu.description += f"*{name}* - {ammount}\n" # Add to the embed
    await ctx.send(embed=stockmenu) # Send the embed



@bot.command() #Gen command
async def gen(ctx,name=None):
    if name == None:
        await ctx.send("Specify the account you want!") # Say error if no name specified
    else:
        name = name.lower()+".txt" #Add the .txt ext
        if name not in os.listdir("Accounts"): # If the name not in the directory
            await ctx.send(f"Account does not exist. `{prefix}stock`")
        else:
            with open("Accounts\\"+name) as file:
                lines = file.read().splitlines() #Read the lines in the file
            if len(lines) == 0: # If the file is empty
                await ctx.send("These accounts are out of stock") #Send error if lines = 0
            else:
                with open("Accounts\\"+name) as file:
                    account = random.choice(lines) # Get a random line
                try: #Try to send the account to the sender
                    await ctx.author.send(f"`{str(account)}`\n\nThis message will delete in {str(delete)} seconds!",delete_after=delete)
                except: # If it failed send a message in the chat
                    await ctx.send("Failed to send! Turn on ur direct messages")
                else: # If it sent the account, say so then remove the account from the file
                    await ctx.send("Sent the account to your inbox!")
                    with open("Accounts\\"+name,"w") as file:
                        file.write("") #Clear the file
                    with open("Accounts\\"+name,"a") as file:
                        for line in lines: #Add the lines back
                            if line != account: #Dont add the account back to the file
                                file.write(line+"\n") # Add other lines to file
bot.run(token)