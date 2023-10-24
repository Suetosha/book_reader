from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_COMMANDS, LEXICON
from aiogram import Router
from database.database import db
from keyboards.pagination_kb import create_inline_kb
from keyboards.bookmarks_kb import create_bookmarks_kb

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    user_id = message.from_user.id
    if not db.is_user_exist(user_id):
        db.add_user(user_id)
    await message.answer(LEXICON_COMMANDS['start'])


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON_COMMANDS['help'])


@router.message(Command(commands='beginning'))
async def process_beginning_command(message: Message):
    book = db.get_book_by_user_id(message.from_user.id)
    book.update_page(1)
    await message.answer(text=book.text[book.page], reply_markup=create_inline_kb(book.page, book.book_len))


@router.message(Command(commands='continue'))
async def process_continue_command(message: Message):
    book = db.get_book_by_user_id(message.from_user.id)
    await message.answer(text=book.text[book.page], reply_markup=create_inline_kb(book.page, book.book_len))


@router.message(Command(commands='bookmarks'))
async def process_bookmarks_command(message: Message):
    book = db.get_book_by_user_id(message.from_user.id)

    if book.bookmarks:
        await message.answer(text=LEXICON['your_bookmarks'], reply_markup=create_bookmarks_kb(book.bookmarks))
    else:
        await message.answer(text=LEXICON['no_bookmarks'])













