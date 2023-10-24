book: dict[int, str] = {}
PAGE_SIZE = 1050
BOOK_PATH = 'book/book.txt'


def prepare_book(path: str) -> None:

    with open(path, 'r', encoding='utf-8') as text:
        text = ''.join([i for i in text.readlines()])

    start = 0
    arr = []

    while start < len(text):
        page, l = _get_part_text(text, start, PAGE_SIZE)
        start += l
        arr.append(page.lstrip())

    for k, v in enumerate(arr, start=1):
        book[k] = v


def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    symbols = ',.!:;?'
    page = text[start:][:page_size]

    if len(page) < page_size:
        return page, len(page)

    if page[-2] in symbols:
        page = page.rstrip(symbols)

    if page[-1] not in symbols:
        near_symbol_index = max([page.rfind(elem) for elem in symbols]) + 1
        page = page[:near_symbol_index]

    return page, len(page)


prepare_book(BOOK_PATH)




