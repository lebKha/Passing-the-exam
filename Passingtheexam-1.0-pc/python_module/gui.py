## @file gui.rpy
# @brief Конфигурация графического интерфейса игры
# @details Содержит все настройки интерфейса: цвета, шрифты, размеры элементов и позиционирование

## @section Initialization
# @brief Инициализация графической системы
init offset = -2

## @brief Инициализация GUI с разрешением 1920x1080
init python:
    gui.init(1920, 1080)

## @brief Включение проверки конфликтующих свойств
define config.check_conflicting_properties = True

## @section Colors
# @brief Цветовая схема интерфейса

## @var gui.accent_color
# @brief Акцентный цвет для заголовков и выделения
define gui.accent_color = '#66cc00'

## @var gui.idle_color
# @brief Цвет неактивных элементов
define gui.idle_color = '#888888'

[... аналогично документируются все цветовые переменные ...]

## @section Fonts
# @brief Настройки шрифтов интерфейса

## @var gui.text_font
# @brief Основной шрифт для текста диалогов
define gui.text_font = "AnimeAcev05.ttf"

## @var gui.name_text_font
# @brief Шрифт для имен персонажей
define gui.name_text_font = "AnimeAcev05.ttf"

[... остальные настройки шрифтов ...]

## @section Main Menu
# @brief Настройки главного меню

## @var gui.main_menu_background
# @brief Фон главного меню
define gui.main_menu_background = "gui/main_menu.png"

## @var gui.game_menu_background
# @brief Фон игрового меню
define gui.game_menu_background = "gui/game_menu.png"

## @section Dialogue
# @brief Настройки окна диалога

## @var gui.textbox_height
# @brief Высота текстового окна
define gui.textbox_height = 278

## @var gui.textbox_yalign
# @brief Вертикальное позиционирование текстового окна (1.0 - низ)
define gui.textbox_yalign = 1.0

[... остальные настройки диалога ...]

## @section Buttons
# @brief Настройки кнопок интерфейса

## @var gui.button_width
# @brief Ширина кнопок (None для авторазмера)
define gui.button_width = None

## @var gui.button_height
# @brief Высота кнопок
define gui.button_height = None

[... остальные настройки кнопок ...]

## @section Choice Buttons
# @brief Настройки кнопок выбора в меню

## @var gui.choice_button_width
# @brief Ширина кнопок выбора
define gui.choice_button_width = 1185

## @var gui.choice_button_height
# @brief Высота кнопок выбора
define gui.choice_button_height = None

[... остальные настройки кнопок выбора ...]

## @section Slots
# @brief Настройки слотов сохранения

## @var gui.slot_button_width
# @brief Ширина кнопки слота
define gui.slot_button_width = 414

## @var gui.slot_button_height
# @brief Высота кнопки слота
define gui.slot_button_height = 309

[... остальные настройки слотов ...]

## @section Positioning
# @brief Позиционирование элементов интерфейса

## @var gui.navigation_xpos
# @brief Горизонтальная позиция кнопок навигации
define gui.navigation_xpos = 60

## @var gui.skip_ypos
# @brief Вертикальная позиция индикатора пропуска
define gui.skip_ypos = 15

[... остальные настройки позиционирования ...]

## @section Frames
# @brief Настройки рамок интерфейса

## @var gui.frame_borders
# @brief Границы стандартной рамки
define gui.frame_borders = Borders(6, 6, 6, 6)

## @var gui.confirm_frame_borders
# @brief Границы рамки подтверждения
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

[... остальные настройки рамок ...]

## @section Bars and Sliders
# @brief Настройки полос прокрутки и слайдеров

## @var gui.bar_size
# @brief Размер горизонтальных полос
define gui.bar_size = 38

## @var gui.scrollbar_size
# @brief Размер полосы прокрутки
define gui.scrollbar_size = 18

[... остальные настройки полос ...]

## @section History
# @brief Настройки экрана истории

## @var config.history_length
# @brief Максимальное количество хранимых записей истории
define config.history_length = 250

## @var gui.history_height
# @brief Высота области истории
define gui.history_height = 210

[... остальные настройки истории ...]

## @section NVL Mode
# @brief Настройки режима NVL

## @var gui.nvl_borders
# @brief Границы окна NVL
define gui.nvl_borders = Borders(0, 15, 0, 30)

## @var gui.nvl_list_length
# @brief Максимальное количество строк NVL
define gui.nvl_list_length = 6

[... остальные настройки NVL ...]

## @section Localization
# @brief Настройки локализации

## @var gui.language
# @brief Язык для переносов строк
define gui.language = "unicode"

## @section Mobile Variants
# @brief Настройки для мобильных устройств

## @brief Вариант для сенсорных устройств
init python:
    @gui.variant
    def touch():
        gui.quick_button_borders = Borders(60, 21, 60, 0)

## @brief Вариант для маленьких экранов
init python:
    @gui.variant
    def small():
        gui.text_size = 45
        gui.name_text_size = 54
        [... остальные изменения для мобильных ...]