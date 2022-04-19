import lightbulb

bot = lightbulb.BotApp(
    token='',
    default_enabled_guilds=(951623877258260560)
)


@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')


@bot.command
@lightbulb.command()





bot.run()