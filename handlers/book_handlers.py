from aiogram.types import CallbackQuery
from lexicon.lexicon import LEXICON
from aiogram import Router, F
from database.database import db
from keyboards.pagination_kb import create_inline_kb
from keyboards.bookmarks_kb import edit_bookmarks_kb
from services.file_handling import book
import constants.callback_data as callback_data

router = Router()


@router.callback_query(F.data == callback_data.FORWARD)
async def process_forward_press(callback: CallbackQuery):
    try:
        user = db.get_user_by_id(callback.from_user.id)
        user.next_page()
        await callback.message.edit_text(text=book[user.page], reply_markup=create_inline_kb(user.page, len(book)))
    except Exception:
        pass
    finally:
        await callback.answer()


@router.callback_query(F.data == callback_data.BACKWARD)
async def process_backward_press(callback: CallbackQuery):
    try:
        user = db.get_user_by_id(callback.from_user.id)
        user.previous_page()
        await callback.message.edit_text(text=book[user.page], reply_markup=create_inline_kb(user.page, len(book)))
    except Exception:
        pass
    finally:
        await callback.answer()


@router.callback_query(F.data == callback_data.ADD_BOOKMARK)
async def process_add_bookmark_press(callback: CallbackQuery):
    try:
        user = db.get_user_by_id(callback.from_user.id)
        user.add_bookmark()
        await callback.answer(text=LEXICON['add_bookmark'])
    except Exception:
        await callback.answer(text=LEXICON['bookmark_exists'])


@router.callback_query(F.data == callback_data.CANCEL)
async def process_cancel_press(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON['offer_to_read'])


@router.callback_query(F.data == callback_data.EDIT)
async def process_edit_press(callback: CallbackQuery):
    user = db.get_user_by_id(callback.from_user.id)
    await callback.message.edit_text(text=LEXICON['edit_bookmarks'], reply_markup=edit_bookmarks_kb(user.bookmarks))


@router.callback_query(F.data.startswith(callback_data.DELETE))
async def process_del_bookmark_press(callback: CallbackQuery):
    user = db.get_user_by_id(callback.from_user.id)
    page = int(callback.data.split(' ')[1])
    user.delete_bookmark(page)

    if user.bookmarks:
        await callback.message.edit_text(text=LEXICON['edit_bookmarks'], reply_markup=edit_bookmarks_kb(user.bookmarks))
    else:
        await callback.message.edit_text(text=LEXICON['no_bookmarks'])


@router.callback_query(F.data.isdigit())
async def process_bookmark_press(callback: CallbackQuery):
    user = db.get_user_by_id(callback.from_user.id)
    page = int(callback.data)
    user.update_page(page)
    await callback.message.edit_text(text=book[user.page], reply_markup=create_inline_kb(user.page, len(book)))


