from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import constants.callback_data as callback_data
from lexicon.lexicon import LEXICON_KB_BTN


def create_bookmarks_kb(bookmarks):
    bookmarks_buttons = [[InlineKeyboardButton(text=f'{page} - {preview}',
                          callback_data=str(page))] for page, preview in bookmarks.items()]

    options_buttons = [InlineKeyboardButton(text=LEXICON_KB_BTN['edit'], callback_data=callback_data.EDIT),
                       InlineKeyboardButton(text=LEXICON_KB_BTN['cancel'], callback_data=callback_data.CANCEL)]

    inline_bookmarks_kb = InlineKeyboardMarkup(inline_keyboard=bookmarks_buttons + [options_buttons])

    return inline_bookmarks_kb


def edit_bookmarks_kb(bookmarks):
    edit_bookmarks_buttons = [[InlineKeyboardButton(text=f"{LEXICON_KB_BTN['x']} {page} - {preview}",
                               callback_data=callback_data.DELETE + str(page))] for page, preview in bookmarks.items()]

    cancel_btn = [InlineKeyboardButton(text=LEXICON_KB_BTN['cancel'], callback_data=callback_data.CANCEL)]

    inline_edit_bookmarks_kb = InlineKeyboardMarkup(inline_keyboard=edit_bookmarks_buttons + [cancel_btn])

    return inline_edit_bookmarks_kb
