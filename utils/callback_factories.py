from aiogram.filters.callback_data import CallbackData
from constants.callback_data import DELETE, EDIT


class DeleteCallbackFactory(CallbackData, prefix=DELETE):
    page: int


class EditCallbackFactory(CallbackData, prefix=EDIT):
    page: int
