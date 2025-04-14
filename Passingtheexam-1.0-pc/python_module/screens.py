## @file screens.rpy
# @brief Файл экранов интерфейса игры
# @details Содержит все экраны интерфейса для Ren'Py игры, включая главное меню, диалоги, настройки и другие элементы UI

init offset = -1

## @section Styles
# @brief Стили интерфейса
# @details Определения стилей для всех элементов интерфейса

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

[... остальные стили остаются без изменений ...]

## @section Game Screens
# @brief Основные игровые экраны

## @screen say
# @brief Экран отображения диалога
# @param who Имя говорящего персонажа (может быть None)
# @param what Текст диалога
screen say(who, what):
    window:
        id "window"
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
        text what id "what"

[... аналогично документируются все остальные экраны ...]

## @screen quick_menu
# @brief Экран быстрого меню в игре
# @details Отображается поверх игрового экрана для быстрого доступа к основным функциям
screen quick_menu():
    zorder 100
    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0
            textbutton _("Назад") action Rollback()
            textbutton _("История") action ShowMenu('history')
            [...]

## @screen navigation
# @brief Экран навигации по меню
# @details Используется в главном и игровом меню для перехода между разделами
screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing
        if main_menu:
            textbutton _("Начать") action Start()
        [...]

## @screen main_menu
# @brief Экран главного меню
# @details Отображается при запуске игры
screen main_menu():
    tag menu
    add gui.main_menu_background
    frame:
        style "main_menu_frame"
    use navigation
    [...]

## @screen game_menu
# @brief Базовый экран игрового меню
# @param title Заголовок меню
# @param scroll Тип прокрутки (None, "viewport" или "vpgrid")
# @param yinitial Начальная позиция прокрутки
# @param spacing Расстояние между элементами
screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):
    style_prefix "game_menu"
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background
    [...]

## @screen file_slots
# @brief Экран слотов сохранения/загрузки
# @param title Заголовок экрана ("Сохранить" или "Загрузить")
screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("{} страница"), auto=_("Автосохранения"), quick=_("Быстрые сохранения"))
    use game_menu(title):
        fixed:
            order_reverse True
            [...]

## @screen preferences
# @brief Экран настроек игры
# @details Позволяет настроить звук, скорость текста и другие параметры
screen preferences():
    tag menu
    use game_menu(_("Настройки"), scroll="viewport"):
        vbox:
            hbox:
                box_wrap True
                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Режим экрана")
                        [...]

## @screen history
# @brief Экран истории диалогов
# @details Показывает предыдущие реплики персонажей
screen history():
    tag menu
    predict False
    use game_menu(_("История"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):
        style_prefix "history"
        for h in _history_list:
            [...]

## @section Additional Screens
# @brief Дополнительные служебные экраны

## @screen confirm
# @brief Экран подтверждения действия
# @param message Текст сообщения
# @param yes_action Действие при подтверждении
# @param no_action Действие при отказе
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    [...]

## @screen skip_indicator
# @brief Индикатор режима пропуска
# @brief Показывает, что игра находится в режиме пропуска текста
screen skip_indicator():
    zorder 100
    style_prefix "skip"
    frame:
        hbox:
            spacing 9
            text _("Пропускаю")
            [...]

## @screen notify
# @brief Экран уведомлений
# @param message Текст уведомления
screen notify(message):
    zorder 100
    style_prefix "notify"
    frame at notify_appear:
        text "[message!tq]"
    [...]

## @section Mobile Variants
# @brief Мобильные версии экранов

## @screen quick_menu
# @brief Мобильная версия быстрого меню
# @variant touch Вариант для сенсорных устройств
screen quick_menu():
    variant "touch"
    zorder 100
    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0
            [...]
