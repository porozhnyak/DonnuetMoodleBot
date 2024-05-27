from states.adminform import AdminForm
from aiogram import types



async def choose_leader_start(message: types.Message):
    await message.answer("Введите ID пользователя, которого хотите назначить старостой:")
    await AdminForm.choose_leader.set()