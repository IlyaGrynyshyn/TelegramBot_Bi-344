from aiogram.dispatcher.filters.state import StatesGroup, State


class StatesOfBot(StatesGroup):
    start_state = State()
    choose_subgroup = State()
    main_menu = State()
