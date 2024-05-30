from aiogram.dispatcher.filters.state import State, StatesGroup

class AdminForm(StatesGroup):
    adminmenu = State()
    choose_leader = State()
    waiting_name_group = State()
