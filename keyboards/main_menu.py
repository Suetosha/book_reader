from aiogram import Bot
from aiogram.types import BotCommand
from lexicon.lexicon import LEXICON_COMMANDS


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command='/help',
                   description=LEXICON_COMMANDS['help_menu']),
        BotCommand(command='/bookmarks',
                   description=LEXICON_COMMANDS['bookmarks']),
        BotCommand(command='/continue',
                   description=LEXICON_COMMANDS['continue']),
        BotCommand(command='/beginning',
                   description=LEXICON_COMMANDS['beginning']),
    ]
    await bot.set_my_commands(main_menu_commands)
