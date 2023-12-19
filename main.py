import sys, logging, asyncio
from aiogram import Bot, Dispatcher
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.utils import markdown
from aiogram import types
from aiogram.types import FSInputFile


keyboardmain = [
    [InlineKeyboardButton(text='Система Linux', callback_data='linux')],
    [InlineKeyboardButton(text='Docker', callback_data='docker')],
    [InlineKeyboardButton(text='Система Git', callback_data='git')]
    ]
keyboardmain = InlineKeyboardMarkup(inline_keyboard=keyboardmain)

back = [
    [InlineKeyboardButton(text='Вернуться назад', callback_data='back')]
]
back = InlineKeyboardMarkup(inline_keyboard=back)

TOKEN = 'TOKEN'

async def main():
    bot = Bot(token=TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Добро пожаловать')
    await message.answer(text='Выберите тему:', reply_markup=keyboardmain)

@router.callback_query(lambda call: call.data == "back")
async def go_back(callback: CallbackQuery):
    await callback.message.delete()

@router.callback_query(lambda call: call.data == "linux")
async def get_linux(callback: CallbackQuery):
    website_link = "https://neoserver.ru/help/kak-prosmotret-nagruzku-na-processor-v-linux"
    website_link2 = "https://losst.pro/zagruzka-protsessora-linux"
    website_link3 = "https://www.linuxcenter.ru"
    website_link4 = "https://selectel.ru/blog/basic-linux-commands/"
    website_link5 = "https://journal.sweb.ru/amp/article/shpargalka-bazovye-komandy-dlya-terminala-linux"
    website_link6 = "https://habr.com/ru/companies/ruvds/articles/445270/"
    photo = FSInputFile("c:\\Users\\света\\Desktop\\bot\\photo_7.jpg")
    await callback.message.answer_photo(photo)
    await callback.message.answer(f"Полезные ссылки по данной теме:\n➖➖➖➖➖➖➖➖➖➖\n<a href='{website_link}'>Нагрузка на проц</a>\n<a href='{website_link2}'>Нагрузка на процессор 2</a>\n<a href='{website_link3}'>Статьи</a>\n<a href='{website_link4}'>Основные команды</a>\n<a href='{website_link5}'>Основные команды 2</a>\n<a href='{website_link6}'>Полезные команды для bash</a>", disable_web_page_preview=True, parse_mode="html",reply_markup=keyboardmain)

@router.callback_query(lambda call: call.data == "docker")
async def get_docker(callback: CallbackQuery):
    website_link = "https://habr.com/ru/articles/253877/"
    website_link2 = "https://blog.skillfactory.ru/glossary/docker/"
    website_link3 = "https://itproger.com/course/docker/2"
    photo = FSInputFile("c:\\Users\\света\\Desktop\\bot\\photo_6.jpg")
    await callback.message.answer_photo(photo)
    await callback.message.answer(f"Полезные ссылки по данной теме:\n➖➖➖➖➖➖➖➖➖➖\n<a href='{website_link}'>Общая информация про DOCKER</a>\n<a href='{website_link2}'>Что такое DOCKER?</a>\n<a href='{website_link3}'>Все про DOCKER-контейнеры</a>", disable_web_page_preview=True, parse_mode="html",reply_markup=keyboardmain)

@router.callback_query(lambda call: call.data == "git")
async def get_git(callback: CallbackQuery):
    website_link = "https://git.wiki.kernel.org/index.php/Main_Page"
    website_link2 = "https://git-scm.com/book/ru/v2/Git-%D0%B8%D0%B7%D0%BD%D1%83%D1%82%D1%80%D0%B8-%D0%A1%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B2-Git"
    photo = FSInputFile("c:\\Users\\света\\Desktop\\bot\\photo_4.jpg")
    await callback.message.answer_photo(photo)
    await callback.message.answer(f"Полезные ссылки по данной теме:\n➖➖➖➖➖➖➖➖➖➖\n<a href='{website_link}'>Общая информация про GIT</a>\n<a href='{website_link2}'>Ссылки в GIT</a>", disable_web_page_preview=True, parse_mode="html", reply_markup=keyboardmain)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try: asyncio.run(main())
    except KeyboardInterrupt: print('Exit')