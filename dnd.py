from values import *
import discord
from discord.ext import commands
import datetime, time
import random


class DND(commands.Cog):
    def __init__(self, client):
        self.client = client
        global startTime
        startTime = time.time()

    @commands.Cog.listener()
    async def on_ready(self):
        print("dnd.py is loaded. P2")

    @commands.command()
    async def DNDCommands(self, ctx):
        if DNDCommands >= 1:
            embedVar = discord.Embed(title="DND Commands:", description="Prefix: %", color=0xD90000)
            embedVar.add_field(name="NewCivilianBlock:", value="Aliases: NewCivBlock, NewCivB, NewCB . Makes you a Civilian stat block based off a 1d6 roll to decide the highest stat, Example: %NewCB 12(highest the high stat can be) 4(lowest the high stat can be) 8(highest the lower stats can be) 6(lowest the lower stats can be)", inline=False)
            embedVar.add_field(name="NewCharacter:", value='Aliases: NewChar, NewC, NC . This command creates you a DND character based off the "Basic Rules" document, ', inline=False)
            embedVar.add_field(name="DNDCredits:", value='Links the "Basic Rules" document on DND Beyond, if there are any legal issues please contact the bots maintainer/owner on discord or any platform.', inline=False)
            await ctx.send(embed=embedVar)
        else:
            await ctx.send("Sorry but this command is disabled.")

    @commands.command()
    async def DNDCredits(self, ctx):
        if DNDCommands >= 1:
            embedVar = discord.Embed(title="DND Commands Credits:", description="Shows all the credits for the DND Commands in this bot.", color=0xD90000)
            embedVar.add_field(name="Wizards of the Coast(WOTC):", value='Credits for making DND 5E and the ["Basic Rules"](https://media.wizards.com/2018/dnd/downloads/DnD_BasicRules_2018.pdf) all rights to them over the "Basic Rules" the command "NewCharacter" is based off of. If there are any legal issues please contact the bots maintainer/owner on discord or any platform.', inline=False)
            embedVar.add_field(name="OneOwen:", value='Creator of all current commands, and the current owner/maintainer of the bot.', inline=False)
            embedVar.add_field(name="Discord.py docs:", value='Credit for being an amazing rescource along the way while learning python.', inline=False)
            embedVar.add_field(name="Stack Overflow community:", value='Credit for being amazing people who are willing to help new people and veterants in the community.', inline=False)
            await ctx.send(embed=embedVar)
        else:
            await ctx.send("Sorry but this command is disabled.")

    @commands.command(aliases=["NewCivBlock", "NewCivB", "NewCB"])
    async def NewCivilianBlock(self, ctx, maxHighStat : int, lowestHighStat : int, maxLowStat : int, lowestLowStat : int):
        if DNDCommands >= 1:
            AlignmentRoll = random.randint(1, 12)
            if AlignmentRoll == 1:
                Alignment = r'True Evil'
            elif AlignmentRoll == 2:
                Alignment = r'True Neutral'
            elif AlignmentRoll == 3:
                Alignment = r'True Good'
            elif AlignmentRoll == 4:
                Alignment = r'Chaotic Evil'
            elif AlignmentRoll == 5:
                Alignment = r'Chaotic Neutral'
            elif AlignmentRoll == 6:
                Alignment = r'Chaotic Good'
            elif AlignmentRoll == 7:
                Alignment = r'Neutral'
            elif AlignmentRoll == 8:
                Alignment = r'Neutral'
            elif AlignmentRoll == 9:
                Alignment = r'Neutral'
            elif AlignmentRoll == 10:
                Alignment = r'Lawful Evil'
            elif AlignmentRoll == 11:
                Alignment = r'Lawful Neutral'
            elif AlignmentRoll == 12:
                Alignment = r'Lawful Good'
            PersonalityRoll = random.randint(1, 8)
            if PersonalityRoll == 1:
                Personality = r'Overly Greedy'
            elif PersonalityRoll == 2:
                Personality = r'Grumpy'
            elif PersonalityRoll == 3:
                Personality = r'Slightly Greedy'
            elif PersonalityRoll == 4:
                Personality = r'Normal'
            elif PersonalityRoll == 5:
                Personality = r'Normal'
            elif PersonalityRoll == 6:
                Personality = r'Normal'
            elif PersonalityRoll == 7:
                Personality = r'Nice'
            elif PersonalityRoll == 8:
                Personality = r'Overly Nice'
            HighestStatRoll = random.randint(1, 6)
            if HighestStatRoll == 1:
                MainStat = r'Strength'
                Strength = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
                if Strength > maxHighStat:
                    Strength = maxHighStat
                if Strength < lowestHighStat:
                    Strength = lowestHighStat
                Dexterity = random.randint(1, 6) + random.randint(1, 6)
                if Dexterity > maxLowStat:
                    Dexterity = maxLowStat
                if Dexterity < lowestLowStat:
                    Dexterity = lowestLowStat
                Constitution = random.randint(1, 6) + random.randint(1, 6)
                if Constitution > maxLowStat:
                    Constitution = maxLowStat
                if Constitution < lowestLowStat:
                    Constitution = lowestLowStat
                Intelligence = random.randint(1, 6) + random.randint(1, 6)
                if Intelligence > maxLowStat:
                    Intelligence = maxLowStat
                if Intelligence < lowestLowStat:
                    Intelligence = lowestLowStat
                Wisdom = random.randint(1, 6) + random.randint(1, 6)
                if Wisdom > maxLowStat:
                    Wisdom = maxLowStat
                if Wisdom < lowestLowStat:
                    Wisdom = lowestLowStat
                Charisma = random.randint(1, 6) + random.randint(1, 6)
                if Charisma > maxLowStat:
                    Charisma = maxLowStat
                if Charisma < lowestLowStat:
                    Charisma = lowestLowStat
            elif HighestStatRoll == 2:
                MainStat = r'Dexterity'
                Strength = random.randint(1, 6) + random.randint(1, 6)
                if Strength > maxLowStat:
                    Strength = maxLowStat
                if Strength < lowestLowStat:
                    Strength = lowestLowStat
                Dexterity = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
                if Dexterity > maxHighStat:
                    Dexterity = maxHighStat
                if Dexterity < lowestHighStat:
                    Dexterity = lowestHighStat
                Constitution = random.randint(1, 6) + random.randint(1, 6)
                if Constitution > maxLowStat:
                    Constitution = maxLowStat
                if Constitution < lowestLowStat:
                    Constitution = lowestLowStat
                Intelligence = random.randint(1, 6) + random.randint(1, 6)
                if Intelligence > maxLowStat:
                    Intelligence = maxLowStat
                if Intelligence < lowestLowStat:
                    Intelligence = lowestLowStat
                Wisdom = random.randint(1, 6) + random.randint(1, 6)
                if Wisdom > maxLowStat:
                    Wisdom = maxLowStat
                if Wisdom < lowestLowStat:
                    Wisdom = lowestLowStat
                Charisma = random.randint(1, 6) + random.randint(1, 6)
                if Charisma > maxLowStat:
                    Charisma = maxLowStat
                if Charisma < lowestLowStat:
                    Charisma = lowestLowStat
            elif HighestStatRoll == 3:
                MainStat = r'Constitution'
                Strength = random.randint(1, 6) + random.randint(1, 6)
                if Strength > maxLowStat:
                    Strength = maxLowStat
                if Strength < lowestLowStat:
                    Strength = lowestLowStat
                Dexterity = random.randint(1, 6) + random.randint(1, 6)
                if Dexterity > maxLowStat:
                    Dexterity = maxLowStat
                if Dexterity < lowestLowStat:
                    Dexterity = lowestLowStat
                Constitution = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
                if Constitution > maxHighStat:
                    Constitution = maxHighStat
                if Constitution < lowestHighStat:
                    Constitution = lowestHighStat
                Intelligence = random.randint(1, 6) + random.randint(1, 6)
                if Intelligence > maxLowStat:
                    Intelligence = maxLowStat
                if Intelligence < lowestLowStat:
                    Intelligence = lowestLowStat
                Wisdom = random.randint(1, 6) + random.randint(1, 6)
                if Wisdom > maxLowStat:
                    Wisdom = maxLowStat
                if Wisdom < lowestLowStat:
                    Wisdom = lowestLowStat
                Charisma = random.randint(1, 6) + random.randint(1, 6)
                if Charisma > maxLowStat:
                    Charisma = maxLowStat
                if Charisma < lowestLowStat:
                    Charisma = lowestLowStat
            elif HighestStatRoll == 4:
                MainStat = r'Intelligence'
                Strength = random.randint(1, 6) + random.randint(1, 6)
                if Strength > maxLowStat:
                    Strength = maxLowStat
                if Strength < lowestLowStat:
                    Strength = lowestLowStat
                Dexterity = random.randint(1, 6) + random.randint(1, 6)
                if Dexterity > maxLowStat:
                    Dexterity = maxLowStat
                if Dexterity < lowestLowStat:
                    Dexterity = lowestLowStat
                Constitution = random.randint(1, 6) + random.randint(1, 6)
                if Constitution > maxLowStat:
                    Constitution = maxLowStat
                if Constitution < lowestLowStat:
                    Constitution = lowestLowStat
                Intelligence = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
                if Intelligence > maxHighStat:
                    Intelligence = maxHighStat
                if Intelligence < lowestHighStat:
                    Intelligence = lowestHighStat
                Wisdom = random.randint(1, 6) + random.randint(1, 6)
                if Wisdom > maxLowStat:
                    Wisdom = maxLowStat
                if Wisdom < lowestLowStat:
                    Wisdom = lowestLowStat
                Charisma = random.randint(1, 6) + random.randint(1, 6)
                if Charisma > maxLowStat:
                    Charisma = maxLowStat
                if Charisma < lowestLowStat:
                    Charisma = lowestLowStat
            elif HighestStatRoll == 5:
                MainStat = r'Wisdom'
                Strength = random.randint(1, 6) + random.randint(1, 6)
                if Strength > maxLowStat:
                    Strength = maxLowStat
                if Strength < lowestLowStat:
                    Strength = lowestLowStat
                Dexterity = random.randint(1, 6) + random.randint(1, 6)
                if Dexterity > maxLowStat:
                    Dexterity = maxLowStat
                if Dexterity < lowestLowStat:
                    Dexterity = lowestLowStat
                Constitution = random.randint(1, 6) + random.randint(1, 6)
                if Constitution > maxLowStat:
                    Constitution = maxLowStat
                if Constitution < lowestLowStat:
                    Constitution = lowestLowStat
                Intelligence = random.randint(1, 6) + random.randint(1, 6)
                if Intelligence > maxLowStat:
                    Intelligence = maxLowStat
                if Intelligence < lowestLowStat:
                    Intelligence = lowestLowStat
                Wisdom = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
                if Wisdom > maxHighStat:
                    Wisdom = maxHighStat
                if Wisdom < lowestHighStat:
                    Wisdom = lowestHighStat
                Charisma = random.randint(1, 6) + random.randint(1, 6)
                if Charisma > maxLowStat:
                    Charisma = maxLowStat
                if Charisma < lowestLowStat:
                    Charisma = lowestLowStat
            elif HighestStatRoll == 6:
                MainStat = r'Charisma'
                Strength = random.randint(1, 6) + random.randint(1, 6)
                if Strength > maxLowStat:
                    Strength = maxLowStat
                if Strength < lowestLowStat:
                    Strength = lowestLowStat
                Dexterity = random.randint(1, 6) + random.randint(1, 6)
                if Dexterity > maxLowStat:
                    Dexterity = maxLowStat
                if Dexterity < lowestLowStat:
                    Dexterity = lowestLowStat
                Constitution = random.randint(1, 6) + random.randint(1, 6)
                if Constitution > maxLowStat:
                    Constitution = maxLowStat
                if Constitution < lowestLowStat:
                    Constitution = lowestLowStat
                Intelligence = random.randint(1, 6) + random.randint(1, 6)
                if Intelligence > maxLowStat:
                    Intelligence = maxLowStat
                if Intelligence < lowestLowStat:
                    Intelligence = lowestLowStat
                Wisdom = random.randint(1, 6) + random.randint(1, 6)
                if Wisdom > maxLowStat:
                    Wisdom = maxLowStat
                if Wisdom < lowestLowStat:
                    Wisdom = lowestLowStat
                Charisma = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
                if Charisma > maxHighStat:
                    Charisma = maxHighStat
                if Charisma < lowestHighStat:
                    Charisma = lowestHighStat
            embedVar = discord.Embed(title="Civilian block", description=f"**Extra stuff:** Alignment: {Alignment}, Personality: {Personality}", color=discord.Color.dark_blue())
            embedVar.add_field(name="STR:", value=f"{Strength}", inline=False)
            embedVar.add_field(name="DEX:", value=f"{Dexterity}", inline=False)
            embedVar.add_field(name="CON:", value=f"{Constitution}", inline=False)
            embedVar.add_field(name="INT:", value=f"{Intelligence}", inline=False)
            embedVar.add_field(name="WIS:", value=f"{Wisdom}", inline=False)
            embedVar.add_field(name="CHA:", value=f"{Charisma}", inline=False)
            embedVar.set_footer(text=f"Main stat: {MainStat}, maxHighStat: {maxHighStat}, lowestHighStat: {lowestHighStat}, maxlowStat: {maxLowStat}, lowestLowStat: {lowestLowStat}", icon_url=None)
            await ctx.send(embed=embedVar)
        else:
            await ctx.send("Sorry but this command is disabled.")

    @commands.command(aliases=["NewChar", "NewC", "NC"])
    async def NewCharacter(self, ctx, characterClass : int, characterRace : int, characterSubRace : int):
        if DNDCommands >= 1:
            AlignmentRoll = random.randint(1, 12)
            if AlignmentRoll == 1:
                Alignment = r'True Evil'
            elif AlignmentRoll == 2:
                Alignment = r'True Neutral'
            elif AlignmentRoll == 3:
                Alignment = r'True Good'
            elif AlignmentRoll == 4:
                Alignment = r'Chaotic Evil'
            elif AlignmentRoll == 5:
                Alignment = r'Chaotic Neutral'
            elif AlignmentRoll == 6:
                Alignment = r'Chaotic Good'
            elif AlignmentRoll == 7:
                Alignment = r'Neutral'
            elif AlignmentRoll == 8:
                Alignment = r'Neutral'
            elif AlignmentRoll == 9:
                Alignment = r'Neutral'
            elif AlignmentRoll == 10:
                Alignment = r'Lawful Evil'
            elif AlignmentRoll == 11:
                Alignment = r'Lawful Neutral'
            elif AlignmentRoll == 12:
                Alignment = r'Lawful Good'
            
            PersonalityRoll = random.randint(1, 8)
            if PersonalityRoll == 1:
                Personality = r'Greedy'
            elif PersonalityRoll == 2:
                Personality = r'Grumpy'
            elif PersonalityRoll == 3:
                Personality = r'Normal'
            elif PersonalityRoll == 4:
                Personality = r'Normal'
            elif PersonalityRoll == 5:
                Personality = r'Normal'
            elif PersonalityRoll == 6:
                Personality = r'Normal'
            elif PersonalityRoll == 7:
                Personality = r'Nice'
            elif PersonalityRoll == 8:
                Personality = r'Very Kind'

            Strength = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
            Dexterity = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
            Constitution = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
            Intelligence = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
            Wisdom = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
            Charisma = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)

            if characterRace == 0:
                    characterRace = random.randint(1, 4)
            elif characterRace >= 5:
                    characterRace = random.randint(1, 4)

            if characterClass == [1, 2, 3, 4]:
                if characterClass == 1:
                    CharacterClass2 = r'Cleric'
                    Health = random.randint(1, 8)
                    SavingThrowProf = r'Wisdom & Charisma'
                    ArmorWeaponProf = r'Light and medium armor, shields, simple weapons'
                elif characterClass == 2:
                    CharacterClass2 = r'Fighter'
                    Health = random.randint(1, 10)
                    SavingThrowProf = r'Strength & Constitution'
                    ArmorWeaponProf = r'All armor, shields, simple and martial weapons'
                elif characterClass == 3:
                    CharacterClass2 = r'Rogue'
                    Health = random.randint(1, 8)
                    SavingThrowProf = r'Dexterity & Intelligence'
                    ArmorWeaponProf = r'Light armor, simple weapons, hand crossbows, longswords, rapiers, shortswords'
                elif characterClass == 4:
                    CharacterClass2 = r'Wizard'
                    Health = random.randint(1, 6)
                    SavingThrowProf = r'Intelligence & Wisdom'
                    ArmorWeaponProf = r'Daggers, darts, slings, quarterstaffs, light crossbows'

            if characterRace == 0:
                    characterRace = random.randint(1, 4)
            elif characterRace >= 5:
                    characterRace = random.randint(1, 4)
                    
            if characterRace == [1, 2, 3, 4]:
                if characterRace == 1:
                    CharacterRace2 = r'Dwarf'
                    Constitution = Constitution + 2
                    Darkvision = r'60ft'
                    Size = r'Medium'
                    Speed = r'25'
                    Languages = r'Common and Dwarvish'
                    ExtraRaceStats = r'Stonecunning. Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.'
                    D3 = random.randint(1, 3)
                    if D3 == 1:
                        RaceToolProf = r'smiths tools'
                    elif D3 == 2:
                        RaceToolProf = r'brewers supplies'
                    elif D3 == 1:
                        RaceToolProf = r'masons tools'
                    if characterRace == 0:
                         characterRace = random.randint(1, 2)
                    elif characterRace >= 2:
                        characterRace = random.randint(1, 2)
                    if characterSubRace == 1:
                        characterSubRace2 = r'Hill Dwarf'
                        Wisdom = Wisdom + 1
                        Health = Health + 1
                        ExtraSubRaceStats = r'None.'
                    elif characterSubRace == 2:
                        characterSubRace2 = r'Mountain Dwarf'
                        Strength = Strength + 2
                        SubRaceArmorWeaponProf = r'light and medium armor'
                        ExtraSubRaceStats = r'Dwarven Toughness. Your hit point maximum increases by 1, and it increases by 1 every time you gain a level.'

                elif characterRace == 2:
                    CharacterRace2 = r'Elf'
                    Dexterity = Dexterity + 2
                    Size = r'Medium'
                    Darkvision = r'60ft'
                    Speed = r'30ft'
                    Languages = r'Common and Elvish'
                    ExtraRaceStats = r'Stonecunning. Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.'
                    if characterRace == 0:
                         characterRace = random.randint(1, 2)
                    elif characterRace >= 2:
                        characterRace = random.randint(1, 2)
                    if characterSubRace == 1:
                        characterSubRace2 = r'High Elf'
                        Intelligence = Intelligence + 1
                        SubRaceArmorWeaponProf = r'longsword, shortsword, shortbow, and longbow'
                        ExtraSubRaceStats = r'Cantrip, You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it, and Extra Language. You can speak, read, and write one extra language of your choice.'
                    elif characterSubRace == 2:
                        characterSubRace2 = r'Wood Elf'
                        Strength = Strength + 2
                        SubRaceArmorWeaponProf = r'longsword, shortsword, shortbow, and longbow'
                        Speed = r'35ft'
                        ExtraSubRaceStats = r'Mask of the Wild. You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.'
                    
                elif characterRace == 3:
                    CharacterRace2 = r'Halfling'
                    Dexterity = Dexterity + 2
                    Size = r'Small'
                    Darkvision = r'None'
                    Speed = r'25ft'
                    Languages = r'Common and Halfing'
                    ExtraRaceStats = r'Lucky. When you roll a 1 on the d20 for an attack roll, ability check, or saving throw, you can reroll the die and must use the new roll. Brave. You have advantage on saving throws against being frightened. Halfling Nimbleness. You can move through the space of any creature that is of a size larger than yours.'
                    if characterRace == 0:
                         characterRace = random.randint(1, 2)
                    elif characterRace >= 2:
                        characterRace = random.randint(1, 2)
                    if characterSubRace == 1:
                        characterSubRace2 = r'Lightfoot'
                        Charisma = Charisma + 1
                        ExtraSubRaceStats = r'Naturally Stealthy. You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you.'
                    elif characterSubRace == 2:
                        characterSubRace2 = r'Stout'
                        Constitution = Constitution + 1
                        ExtraSubRaceStats = r'Stout Resilience. You have advantage on saving throws against poison, and you have resistance against poison damage.'

                elif characterRace == 4:
                    CharacterRace2 = r'Human'
                    Strength = Strength + 1
                    Dexterity = Dexterity + 1
                    Constitution = Constitution + 1
                    Intelligence = Intelligence + 1
                    Wisdom = Wisdom + 1
                    Charisma = Charisma + 1
                    Size = r'Small'
                    Darkvision = r'None'
                    Speed = r'25ft'
                    Languages = r'Common'
                    ExtraRaceStats = r'Humans typically learn the languages of other peoples they deal with, including obscure dialects. They are fond of sprinkling their speech with words borrowed from other tongues: Orc curses, Elvish musical expressions, Dwarvish military phrases, and so on. Learn one other language.'
                    if characterRace == 0:
                         characterRace = random.randint(1, 2)
                    elif characterRace >= 2:
                        characterRace = random.randint(1, 2)
                    if characterSubRace == 1:
                        characterSubRace2 = r'Lightfoot'
                        Charisma = Charisma + 1
                        ExtraSubRaceStats = r'Naturally Stealthy. You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you.'
                    elif characterSubRace == 2:
                        characterSubRace2 = r'Stout'
                        Constitution = Constitution + 1
                        ExtraSubRaceStats = r'Stout Resilience. You have advantage on saving throws against poison, and you have resistance against poison damage.'

            embedVar = discord.Embed(title="Character Block", description=f"**Extra stuff:** Alignment: {Alignment}, Personality: {Personality}, Health: {Health}, Size:{Size}, Speed: {Speed}, Darkvision: {Darkvision}, Languages: {Languages}, Extra Race stats: {ExtraRaceStats}, Extra SubRace stats: {ExtraSubRaceStats}", color=discord.Color.dark_blue())
            embedVar.add_field(name="Race:", value=f"{CharacterRace2}", inline=False)
            embedVar.add_field(name="SubRace:", value=f"{characterSubRace2}", inline=False)
            embedVar.add_field(name="Saving Throw Proficiencies:", value=f"{SavingThrowProf}", inline=False)
            embedVar.add_field(name="Armor and Weapon Proficiencies:", value=f"{ArmorWeaponProf}, and {RaceToolProf}, and {SubRaceArmorWeaponProf}", inline=False)
            embedVar.add_field(name="Class:", value=f"{CharacterClass2}", inline=False)
            embedVar.add_field(name="STR:", value=f"{Strength}", inline=False)
            embedVar.add_field(name="DEX:", value=f"{Dexterity}", inline=False)
            embedVar.add_field(name="CON:", value=f"{Constitution}", inline=False)
            embedVar.add_field(name="INT:", value=f"{Intelligence}", inline=False)
            embedVar.add_field(name="WIS:", value=f"{Wisdom}", inline=False)
            embedVar.add_field(name="CHA:", value=f"{Charisma}", inline=False)
            await ctx.send(embed=embedVar)
        else:
            await ctx.send("Sorry but this command is disabled.")

    @commands.command(name='DNDUptime')
    async def _uptime(self, ctx):
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        await ctx.send(uptime)

async def setup(client):
    await client.add_cog(DND(client))