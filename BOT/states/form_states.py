from aiogram.dispatcher.filters.state import State, StatesGroup

class Form(StatesGroup):
    start = State()
    login = State()
    password = State()
    verification = State()
    mainmenu= State()