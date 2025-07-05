from aiogram import F, Router

from aiogram.filters import CommandStart, Command

from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Bot is working!(CommandStart)")


