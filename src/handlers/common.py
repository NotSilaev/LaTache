import sys
sys.path.append('../') # src/

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from i18n import language_detector
from exceptions import exceptions_catcher
from utils import respondEvent


router = Router(name=__name__)


@router.message(CommandStart())
@router.callback_query(F.data == 'start')
@router.message(F.text & (~F.text.startswith("/")))
@language_detector
@exceptions_catcher()
async def start(event: Message | CallbackQuery, _ = str) -> None:
    await respondEvent(event, text=_('Hello, World!'))
