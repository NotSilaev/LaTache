import sys
sys.path.append('../') # src/

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from utils import respondEvent
from i18n import language_detector


router = Router(name=__name__)


@router.message(CommandStart())
@router.callback_query(F.data == 'start')
@router.message(F.text & (~F.text.startswith("/")))
@language_detector
async def start(event: Message | CallbackQuery, _ = str) -> None:
    await respondEvent(event, text=_('Hello, World!'))
