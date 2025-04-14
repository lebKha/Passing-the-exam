## @file script.rpy
# @brief Основной сценарий визуальной новеллы "Passing the exam"
# @details Содержит все диалоги, сцены и игровую логику

init python:
    ## @brief Настройки игры
    # @details Инициализация игровых переменных
    config.window_title = "Passing the exam"
    config.version = "1.0"

## @section characters
# @brief Определение персонажей игры
# @details Каждый персонаж имеет имя и цвет текста

## @var b
# @brief Персонаж Башлыкова А.А.
define b = Character('Башлыкова А.А.', color="#c8ffc8")

## @var l
# @brief Персонаж Лёха
define l = Character('Лёха', color="#c8ffc8")

## @var g
# @brief Персонаж Глеб
define g = Character('Глеб', color="#c8ffc8")

## @var a
# @brief Персонаж Артём
define a = Character('Артём', color="#c8ffc8")

## @var n
# @brief Персонаж Настя
define n = Character('Настя', color="#c8ffc8")

## @var v
# @brief Внутренний голос главного героя
define v = Character('Внутренний голос', color="#c8ffc8")

## @var h
# @brief Безымянный главный герой
define h = Character(' ', color="#c8ffc8")

## @section transforms
# @brief Трансформации для позиционирования персонажей

## @var left
# @brief Позиция слева на экране
transform left:
    xalign 0.2 yalign 0.6
    xysize (416, 474)

## @var right
# @brief Позиция справа на экране
transform right:
    xalign 0.8 yalign 0.6
    xysize (416, 474)

## @label start
# @brief Точка входа в игру
# @details Содержит вступительную сцену и первый выбор игрока
label start:
    scene black
    "Три дня. Ровно 72 часа отделяют тебя от экзамена у Анны Александровны Башлыковой..."
    
    scene obshegi:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0

    show hero at left
    v "Сейчас четверг. Экзамен — в понедельник..."
    hide hero

    ## @menu prepare
    # @brief Первый важный выбор
    menu prepare:
        "Начать подготовку к экзамену?"
        
        "Да. Открыть учебник и начать с теории графов":
            jump prepareyes 
            
        "Нет. Ещё три дня — как три вечности. Лучше завтра":
            jump prepareno

## @label prepareyes
# @brief Ветка подготовки к экзамену
label prepareyes:
    scene fail with dissolve
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0

    show characterleha at left
    l "Эй, идём пиццу заказывать!"
    hide characterleha

    menu prepare_dance:
        "Пойти вместе с Лёхой?"
        
        "На пять минут. И всё":
            jump prepare_danceyes 
            
        "Не сейчас. Мне надо учить":
            jump prepare_danceno

## @label prepare_danceyes
# @brief Ветка отвлечения на вечеринку
label prepare_danceyes:
    scene zonaotdeha with fade
    play music "club.mp3" fadeout 2.0 fadein 3.0

    show characternasty at left
    n "Держи мои заметки по эмерджентности!"
    hide characternasty

    menu prepare_danceyes_note:
        "Взять заметки?"
        
        "Спасибо! Это спасение":
            jump prepare_danceyes_noteyes 
            
        "Не надо, я сам разберусь":
            jump prepare_danceyes_noteno

[Остальные label и сцены продолжаются в том же стиле...]

## @label finish1
# @brief Финал с хорошей оценкой
label finish1:
    scene office with fade
    play music "office.mp3" fadeout 2.0 fadein 3.0

    show characterbashlikova at left
    b "Четвёрка"
    hide characterbashlikova

    jump end_of_story

## @label finish2
# @brief Финал с пересдачей
label finish2:
    scene office with fade
    play music "office.mp3" fadeout 2.0 fadein 3.0

    show characterbashlikova at left
    b "Пересдача в среду"
    hide characterbashlikova

    jump end_of_story

## @label end_of_story
# @brief Завершение игры
label end_of_story:
    return