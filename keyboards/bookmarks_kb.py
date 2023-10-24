from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import constants.callback_data as callback_data_types
from lexicon.lexicon import LEXICON_KB_BTN
from utils.callback_factories import DeleteCallbackFactory, EditCallbackFactory


def create_bookmarks_kb(bookmarks):
    bookmarks_buttons = [[InlineKeyboardButton(text=f'{page} - {preview}',
                          callback_data=EditCallbackFactory(page=page).pack())] for page, preview in bookmarks.items()]

    options_buttons = [InlineKeyboardButton(text=LEXICON_KB_BTN['edit'], callback_data=callback_data_types.EDIT),
                       InlineKeyboardButton(text=LEXICON_KB_BTN['cancel'], callback_data=callback_data_types.CANCEL)]

    inline_bookmarks_kb = InlineKeyboardMarkup(inline_keyboard=bookmarks_buttons + [options_buttons])

    return inline_bookmarks_kb


def edit_bookmarks_kb(bookmarks):
    edit_bookmarks_buttons = [[InlineKeyboardButton(text=f"{LEXICON_KB_BTN['x']} {page} - {preview}",
                               callback_data=DeleteCallbackFactory(page=page).pack())] for page, preview in bookmarks.items()]

    cancel_btn = [InlineKeyboardButton(text=LEXICON_KB_BTN['cancel'], callback_data=callback_data_types.CANCEL)]

    inline_edit_bookmarks_kb = InlineKeyboardMarkup(inline_keyboard=edit_bookmarks_buttons + [cancel_btn])

    return inline_edit_bookmarks_kb
