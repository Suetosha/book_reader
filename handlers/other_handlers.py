from aiogram.types import Message
from aiogram import Router
from lexicon.lexicon import LEXICON

router = Router()


@router.message()
async def process_other_command(message: Message):
    await message.answer(LEXICON['other'])



