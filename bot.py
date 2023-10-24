import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import commands_handlers, other_handlers, book_handlers
from keyboards.main_menu import set_main_menu


async def main() -> None:
    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher()

    await set_main_menu(bot)

    dp.include_router(commands_handlers.router)
    dp.include_router(book_handlers.router)
    dp.include_router(other_handlers.router)
    dp.startup.register(set_main_menu)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
