if message.content.startswith(discordprefix+"exportPfp") and not message.author.bot:
    GetPfp.DownloadAllPfp(message)
    return