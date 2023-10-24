from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon import LEXICON_KB_BTN
import constants.callback_data as callback_data_types


def create_inline_kb(page, book_len):

    btn1 = InlineKeyboardButton(text=LEXICON_KB_BTN['backward'], callback_data=callback_data_types.BACKWARD)
    btn2 = InlineKeyboardButton(text=f"{page}/{book_len}", callback_data=callback_data_types.ADD_BOOKMARK)
    btn3 = InlineKeyboardButton(text=LEXICON_KB_BTN['forward'], callback_data=callback_data_types.FORWARD)

    inline_kb = InlineKeyboardMarkup(
        inline_keyboard=[[btn1, btn2, btn3]])

    return inline_kb
