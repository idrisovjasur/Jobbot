from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🌫 Biz haqimizda',callback_data='about'),
            InlineKeyboardButton(text='✍ ️Ariza qoldirish',callback_data='send'),
        ]
    ]
)

about_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Олий талим',callback_data='oliy'),
            InlineKeyboardButton(text='Ўрта талим',callback_data='orta'),
        ]
    ]
)

about_bridge = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Турмуш қурган',callback_data='uylangan'),
            InlineKeyboardButton(text='Турмуш қурмаган',callback_data='uylanmagan'),
        ]
    ]
)

play = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Аризангизни Тасдиқланг',callback_data='tastiqlash'),

        ]
    ]
)