# Aventurine Bot for Discord 
# Created Sept. 5 2024
# --------------------------------------------------

# ctrl + / to comment out highlighted 


import asyncio 
import discord 
import os
import random
import webserver 
from discord.ext import commands 
from dotenv import load_dotenv 



def run_bot():
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)
    
    @bot.event 
    async def on_ready():
        await bot.tree.sync()
        print ("x")

    # Coin flip functions. Created Sept. 5 2024 - Updated Sept. 10 2024
    @bot.tree.command(name = "flip", description= "How about a game? Nothing fancy, just a game of heads or tails to gauge today's luck.") 
    async def coin_flip(interaction: discord.Interaction): 
        coin = ("Heads", "Tails")
        results = (coin[random.randint(0, 1)])

        await interaction.response.send_message(results)

    @bot.tree.command(name = "flips", description= "Flips a coin multiple times.")
    async def flip_multi(interaction: discord.Interaction, flips: int):
        flips_results = []
        coin = ("Heads", "Tails")
        while flips > 0:
            flips_results.append((coin[random.randint(0, 1)]))
            flips = flips - 1
        
        #print (flips_results)
        await interaction.response.send_message(tally_flips(flips_results))

    def tally_flips(flips_results):
        total_heads = 0 
        total_tails = 0
        i = 0
        for i in range(len(flips_results)):
            if flips_results[i] == "Heads":
                total_heads = total_heads + 1
            else: 
                total_tails = total_tails + 1
            i = i + 1  

        #print("In", len(flips_results), "flips there was", total_heads, "heads and", total_tails, "tails")
        return f"In {len(flips_results)} flips there was {total_heads} heads and {total_tails} tails"
    # --------------------------------------------------
    

    # 50-50. Created Sept 10 2024
    @bot.tree.command(name = "50-50", description= "Feeling lucky?")
    async def fifty_fifty(interaction: discord.Interaction):
        if random.randint(0, 1) == 1:
            result = "Trust me, this is a guaranteed win."
        else: 
            result = "Better hedge your bets. (Lose)"

        await interaction.response.send_message(result)
    

    # Dice Function. Created Sept 10 2024 
    # @bot.tree.command(name = "Dice", description= "The dice have been cast.")
    # async def dice(interaction: discord.Interaction, roll: str):
    #     if random.randint(0, 1) == 1:
    #         result = "Trust me, this is a guaranteed win."




    webserver.keep_alive()
    bot.run(TOKEN)

if __name__ == "__main__":
    run_bot()

        
