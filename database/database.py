from services.file_handling import book


class User:
    def __init__(self):
        self.page = 1
        self.bookmarks = {}

    def next_page(self):
        if self.page == len(book):
            raise Exception
        self.page += 1

    def previous_page(self):
        if self.page == 0:
            raise Exception
        self.page -= 1

    def add_bookmark(self):
        if self.page in self.bookmarks.keys():
            raise Exception
        self.bookmarks[self.page] = book[self.page][:50]

    def delete_bookmark(self, page):
        del self.bookmarks[page]

    def update_page(self, page):
        self.page = page


class UsersDB:
    def __init__(self):
        self.users_db = {}

    def is_user_exist(self, user_id: int) -> bool:
        return user_id in self.users_db.keys()

    def add_user(self, user_id: int) -> None:
        self.users_db[user_id] = User()

    def get_user_by_id(self, user_id: int) -> User:
        return self.users_db[user_id]


db = UsersDB()
