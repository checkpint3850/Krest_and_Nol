from aiogram import types

import info_text


inline_btn_start = [[types.InlineKeyboardButton(text='Викторина🦊', callback_data='quiz')],
                    [types.InlineKeyboardButton(text='О боте📃', callback_data='о боте')],
                    [types.InlineKeyboardButton(text='Опека🧸', callback_data='опека')],
                    [types.InlineKeyboardButton(text='Наши контакты📔', callback_data='наши контакты')],
                    [types.InlineKeyboardButton(text='Оставить отзыв📝', callback_data='оставить отзыв')]
                    ]
kb_start_in = types.InlineKeyboardMarkup(inline_keyboard=inline_btn_start)


inline_btn_custody = [[types.InlineKeyboardButton(text='Опека', callback_data='опека')]]
kb_after_custody = types.InlineKeyboardMarkup(inline_keyboard=inline_btn_custody)


# после викторины
kb_after = [
        [
            types.KeyboardButton(text="Ура! Нажми сюда✅")
        ],
    ]
keyboard_after = types.ReplyKeyboardMarkup(keyboard=kb_after, resize_keyboard=True, one_time_keyboard=True)


# большой размер
kb_big_size = [
        [
            types.KeyboardButton(text=info_text.inf_size_b[0]),
            types.KeyboardButton(text=info_text.inf_size_b[1]),
        ],
    ]
keyboard_big_size = types.ReplyKeyboardMarkup(keyboard=kb_big_size, resize_keyboard=True, one_time_keyboard=True)

# маленький размер
kb_small_size = [
        [
            types.KeyboardButton(text=info_text.inf_size_s[0]),
            types.KeyboardButton(text=info_text.inf_size_s[1]),
        ],
    ]
keyboard_small_size = types.ReplyKeyboardMarkup(keyboard=kb_small_size, resize_keyboard=True, one_time_keyboard=True)

# хижник
kb_predator = [
        [
            types.KeyboardButton(text=info_text.inf_predator[0]),
            types.KeyboardButton(text=info_text.inf_predator[1]),
        ],
    ]
keyboard_predator = types.ReplyKeyboardMarkup(keyboard=kb_predator, resize_keyboard=True, one_time_keyboard=True)

# летать
kb_fly = [
        [
            types.KeyboardButton(text=info_text.inf_fly[0]),
            types.KeyboardButton(text=info_text.inf_fly[1]),
        ],
    ]
keyboard_fly = types.ReplyKeyboardMarkup(keyboard=kb_fly, resize_keyboard=True, one_time_keyboard=True)

# рога
kb_horns = [
        [
            types.KeyboardButton(text=info_text.inf_horns[0]),
            types.KeyboardButton(text=info_text.inf_horns[1]),
        ],
    ]
keyboard_horns = types.ReplyKeyboardMarkup(keyboard=kb_horns, resize_keyboard=True, one_time_keyboard=True)

# ночной
kb_night = [
        [
            types.KeyboardButton(text=info_text.inf_night[0]),
            types.KeyboardButton(text=info_text.inf_night[1]),
        ],
    ]
keyboard_night = types.ReplyKeyboardMarkup(keyboard=kb_night, resize_keyboard=True, one_time_keyboard=True)

# подводный
kb_undwater = [
        [
            types.KeyboardButton(text=info_text.inf_underwater[0]),
            types.KeyboardButton(text=info_text.inf_underwater[1]),
        ],
    ]
keyboard_undwater = types.ReplyKeyboardMarkup(keyboard=kb_undwater, resize_keyboard=True, one_time_keyboard=True)

# лягушка
kb_frog = [
        [
            types.KeyboardButton(text=info_text.inf_frog[0]),
            types.KeyboardButton(text=info_text.inf_frog[1]),
        ],
    ]
keyboard_frog = types.ReplyKeyboardMarkup(keyboard=kb_frog, resize_keyboard=True, one_time_keyboard=True)

# панцирь
kb_shell = [
        [
            types.KeyboardButton(text=info_text.inf_shell[0]),
            types.KeyboardButton(text=info_text.inf_shell[1]),
        ],
    ]
keyboard_shell = types.ReplyKeyboardMarkup(keyboard=kb_shell, resize_keyboard=True, one_time_keyboard=True)

# зубы
kb_teeth = [
        [
            types.KeyboardButton(text=info_text.inf_teeth[0]),
            types.KeyboardButton(text=info_text.inf_teeth[1]),
        ],
    ]
keyboard_teeth = types.ReplyKeyboardMarkup(keyboard=kb_teeth, resize_keyboard=True, one_time_keyboard=True)

# кот
kb_cat = [
        [
            types.KeyboardButton(text=info_text.inf_cat[0]),
            types.KeyboardButton(text=info_text.inf_cat[1]),
        ],
    ]
keyboard_cat = types.ReplyKeyboardMarkup(keyboard=kb_cat, resize_keyboard=True, one_time_keyboard=True)

# опасность
kb_dangerous = [
        [
            types.KeyboardButton(text=info_text.inf_dangerous[0]),
            types.KeyboardButton(text=info_text.inf_dangerous[1]),
        ],
    ]
keyboard_dangerous = types.ReplyKeyboardMarkup(keyboard=kb_dangerous, resize_keyboard=True, one_time_keyboard=True)

# цвет
kb_color = [
        [
            types.KeyboardButton(text=info_text.inf_color[0]),
            types.KeyboardButton(text=info_text.inf_color[1]),
        ],
    ]
keyboard_color = types.ReplyKeyboardMarkup(keyboard=kb_color, resize_keyboard=True, one_time_keyboard=True)

# клюв
kb_beak = [
        [
            types.KeyboardButton(text=info_text.inf_beak[0]),
            types.KeyboardButton(text=info_text.inf_beak[1]),
        ],
    ]
keyboard_beak = types.ReplyKeyboardMarkup(keyboard=kb_beak, resize_keyboard=True, one_time_keyboard=True)

# ящер
kb_lizard = [
        [
            types.KeyboardButton(text=info_text.inf_lizard[0]),
            types.KeyboardButton(text=info_text.inf_lizard[1]),
        ],
    ]
keyboard_lizard = types.ReplyKeyboardMarkup(keyboard=kb_lizard, resize_keyboard=True, one_time_keyboard=True)

# конечности
kb_legs = [
        [
            types.KeyboardButton(text=info_text.inf_legs[0]),
            types.KeyboardButton(text=info_text.inf_legs[1]),
        ],
    ]
keyboard_legs = types.ReplyKeyboardMarkup(keyboard=kb_legs, resize_keyboard=True, one_time_keyboard=True)


