## @file options.rpy
# @brief Основные настройки игры
# @details Содержит конфигурационные параметры, влияющие на поведение игры

## @section Basic Settings
# @brief Основные параметры игры

## @var config.name
# @brief Название игры (для отображения в заголовке окна)
define config.name = _("Passing the exam")

## @var gui.show_name
# @brief Показывать ли название на главном экране
define gui.show_name = False

## @var config.version
# @brief Версия игры
define config.version = "1.0"

## @var gui.about
# @brief Текст для экрана "Об игре"
define gui.about = _p("""""")

## @var build.name
# @brief Короткое имя для исполняемых файлов (без пробелов и спецсимволов)
define build.name = "Passingtheexam"

## @section Audio Settings
# @brief Настройки звука и музыки

## @var config.has_sound
# @brief Включены ли звуковые эффекты
define config.has_sound = True

## @var config.has_music
# @brief Включена ли фоновая музыка
define config.has_music = True

## @var config.has_voice
# @brief Включены ли голосовые реплики
define config.has_voice = True

## @var config.main_menu_music
# @brief Музыка для главного меню
define config.main_menu_music = "MusicMenu.mp3"

## @section Transitions
# @brief Настройки переходов между экранами

## @var config.enter_transition
# @brief Переход при входе в игровое меню
define config.enter_transition = dissolve

## @var config.exit_transition
# @brief Переход при выходе из игрового меню
define config.exit_transition = dissolve

## @var config.intra_transition
# @brief Переход между экранами меню
define config.intra_transition = dissolve

## @var config.after_load_transition
# @brief Переход после загрузки сохранения
define config.after_load_transition = None

## @var config.end_game_transition
# @brief Переход при завершении игры
define config.end_game_transition = None

## @section Window Management
# @brief Управление диалоговым окном

## @var config.window
# @brief Поведение диалогового окна ("show", "hide" или "auto")
define config.window = "auto"

## @var config.window_show_transition
# @brief Переход при показе диалогового окна
define config.window_show_transition = Dissolve(.2)

## @var config.window_hide_transition
# @brief Переход при скрытии диалогового окна
define config.window_hide_transition = Dissolve(.2)

## @section Preferences
# @brief Стандартные настройки игры

## @var preferences.text_cps
# @brief Скорость отображения текста (символов в секунду)
default preferences.text_cps = 20

## @var preferences.afm_time
# @brief Задержка авточтения (в кадрах)
default preferences.afm_time = 15

## @section System Settings
# @brief Системные настройки

## @var config.save_directory
# @brief Директория для сохранений
define config.save_directory = "Passingtheexam-1744287684"

## @var config.window_icon
# @brief Иконка приложения
define config.window_icon = "gui/window_icon.png"

## @section Build Configuration
# @brief Настройки сборки дистрибутива

init python:
    ## @brief Исключаемые из сборки файлы
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## @brief Файлы документации
    build.documentation('*.html')
    build.documentation('*.txt')

## @section Google Play License (commented)
# define build.google_play_key = "..."

## @section Itch.io Project (commented)
# define build.itch_project = "renpytom/test-project"