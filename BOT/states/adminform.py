from aiogram.dispatcher.filters.state import State, StatesGroup

class AdminForm(StatesGroup):
    adminmenu = State()
    choose_leader = State()
    choose_group = State()
    waiting_name_group = State()
    MainShedule = State()
