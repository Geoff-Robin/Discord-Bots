import discord
from discord.ext import commands
from datetime import timedelta

class aclient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents = intents)
        self.anti_spam = commands.CooldownMapping.from_cooldown(5,15,commands.BucketType.member)
        self.too_many_violations = commands.CooldownMapping.from_cooldown(4,60,commands.BucketType.member)


    async def on_ready(self):
        print(f"Logged in as {self.user}.")

    async def on_message(self, message):
        if type(message.channel) is not discord.TextChannel or message.author.bot: return
        bucket = self.anti_spam.get_bucket(message)
        retry_after = bucket.update_rate_limit()
        if retry_after:
            await message.delete()
            await message.channel.send(f"{message.author.mention}, don't spam!", delete_after = 10)
            violations = self.too_many_violations.get_bucket(message)
            check = violations.update_rate_limit()
            if check:
                await message.author.timeout(timedelta(minutes = 10), reason = "Spamming")
                try: await message.author.send("You have been muted for spamming")
                except : pass
client = aclient()
client.run('MTEzNzAxNDkwMzExOTU1NjY3OA.GwkAtv.YYYFmF21Pb5ewx1T1PeoQXtmhG1O1ZIdEazD78')
