from discordbot.commands.command import Command
from discordbot.user.variables import Variables
from minigames.Minigames.blackjack import BlackJack


class BlackjackCommand(Command):
    bot = None
    name = "blackjack"
    help = Variables.BJRULES
    brief = "Start a game of blackjack"
    args = ""
    category = "minigame"

    @classmethod
    async def handler(cls, context, *args):
        msg = await context.channel.send("Starting a game of Blackjack...")
        tmp = BlackJack(cls.bot, "blackjack", msg, context.author.id)
        await tmp.start_game()