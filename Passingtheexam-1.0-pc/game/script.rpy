
define b = Character('Башлыкова А.А.', color="#c8ffc8")
define l = Character('Лёха', color="#c8ffc8")
define g = Character('Глеб', color="#c8ffc8")
define a = Character('Артём', color="#c8ffc8")
define n = Character('Настя', color="#c8ffc8")
define v = Character('Внутренний голос', color="#c8ffc8")
define h = Character(' ', color="#c8ffc8")


transform left:
    xalign 0.2 yalign 0.6
    xysize (416, 474)

transform right:
    xalign 0.8 yalign 0.6
    xysize (416, 474)

label start:
    #Начало и введение в курс дело
    scene black
    "Три дня. Ровно 72 часа отделяют тебя от экзамена у Анны Александровны Башлыковой. Ты сидишь в своей комнате в общаге, и взгляд упорно цепляется за учебник, прикрытый ноутбуком с запущенной игрой."
    hide black

    scene obshegi:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0

    "За окном — вечер, но тишины нет: из соседних комнат доносятся крики «Я не сдам!» и гулкие удары головой о стол."
    
    "Одногруппник Артем уже второй час звонит всем подряд, спрашивая: «Ты вообще что-нибудь учил?». А Лиза из 317-й комнаты, как обычно, шуршит конспектами так громко, что кажется, она перепишет весь учебник за ночь."
    
    "На столе — памятка от старшекурсников:
    1) Не пытайся врать — сожжёт взглядом;
    2) Если не уверен — молчи;
    3) Лучше зубри, чем плачь у деканата»."
    
    "Ты листаешь чат группы. Там уже третий день горит обсуждение:"

    show characterartem at left
    a "Она же спросит про эмерджентность! В прошлом году у всех падал интернет, когда она давала допвопросы!"
    hide characterartem at left
  
    show charactergleb at right
    g "Кто-нибудь знает, почему её называют “Железная Анна”?"
    hide charactergleb
  
    show characterartem at left
    a "Потому что её “неуд” — как клеймо на всю сессию"
    hide characterartem

    show hero at left
    v "Сейчас четверг. Экзамен — в понедельник. Если начать сегодня, можно успеть всё… "
    v "Или нет? Вон, Семён из 409-го три дня готовился и всё равно завалил. А Марина вчера забила и ушла в клуб — говорит, “авось повезёт”. Может, и мне…"
    hide hero
    
    play music "vibration.mp3" fadeout 3.0 fadein 0.5
    "Твой телефон вибрирует. Это сообщение от одногруппницы Насти"
    play music "backgroundmusic.mp3" fadein 2.0

    show characternasty at left
    n "Прикинь, Башлыкова сегодня на лекции сказала: “Кто придет без знаний, будет мыть доски в аудиториях до сентября”. Это шутка? Или нет?"
    hide characternasty   

    play music "wind.mp3" fadeout 2.0 fadein 3.0
    "За окном завывает ветер, словно сама Анна Александровна напоминает: время тикает"

    #Выбор готовиться к экзамену или нет
    menu prepare:
            "Начать подготовку к экзамену?"
            "Да. Открыть учебник и начать с теории графов":
                jump prepareyes 
            "Нет. Ещё три дня — как три вечности. Лучше завтра":
                jump prepareno

label prepareyes:
    scene fail:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0

    "Ты вгрызаешься в материал. Первые темы кажутся логичными, но к полуночи глаза слипаются. Из соседней комнаты доносится: «Эй, идём пиццу заказывать! Успеешь завтра!"
    "Ты открываешь учебник на разделе «Теория графов». Первые страницы пестрят формулами и схемами, но через полчаса в голове начинает вырисовываться логика: узлы, рёбра, циклы… Кажется, даже Башлыкова оценила бы твоё упорство."
    "Но тут в дверь стучит Лёха — твой сосед по общаге, мастер по созданию хаоса из ничего."

    show characterleha at left
    l "Эй, ты чего тут как монах в келье? Слышал, Глеб в холле гирлянды развесил и кричит"

    show charactergleb at right
    g "Сессия — не вечность, давайте танцевать!"
    hide charactergleb 

    "Пошли с нами!"  
    hide characterleha   
   
    menu prepare_dance:
            "Пойти вместе с Лёхой?"
            "На пять минут. И всё":
                jump prepare_danceyes 
            "Не сейчас. Мне надо учить":
                jump prepare_danceno    

label prepare_danceyes:
    show hero at left
    h "На пять минут. И всё!"
    hide hero

    "Ты следуешь за ним."

    scene zonaotdeha:
        xysize (1980, 1080)
    play music "club.mp3" fadeout 2.0 fadein 3.0

    "В холле Глеб, обмотанный гирляндами, пытается станцевать ламбаду под крики"
    
    show charactergleb at left
    g "Эй, Башлыкова подождёт! Жизнь-то одна!"
    hide charactergleb

    scene black:
        xysize (1980, 1080)

    "Через час ты возвращаешься в комнату, чувствуя вину. Время потеряно."

    scene obshegi:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0

    "Утро пятницы. Настя стучит в дверь, держа в руках конспекты толщиной с кирпич"

    show characternasty at left
    n "Привет! Лиза сказала, ты пашешь как проклятый. Держи мои заметки по эмерджентности — там всё, что Башлыкова упоминала на семинарах."
    hide characternasty 

    menu prepare_danceyes_note:
            "Взять заметки?"
            "Спасибо! Это спасение":
                jump prepare_danceyes_noteyes 
            "Не надо, я сам разберусь":
                jump prepare_danceyes_noteno    

label prepare_danceyes_noteyes:
    show hero at left
    h "Спасибо! Это спасение"
    hide hero

    "Ты дополняешь свои записи. Оказывается, Анна Александровна обожает задавать каверзные вопросы про «неочевидные свойства систем». Теперь ты готов"
    "Воскресенье. Последняя ночь перед экзаменом. Ты повторяешь материал, когда в дверь врывается Настя с лицом, как у загнанного зверя:"

    scene obshegi:
        xysize (1980, 1080)

    show characternasty at left
    n "Ты видел, что Башлыкова выложила в СДО? Дополнительные статьи по эмерджентности! Это ловушка? Или подсказка?"
    hide characternasty 

    menu prepare_danceyes_noteyes_article:
            "Прочитать статьи?"
            "Прочитать статьи. Вдруг это ключ к “пятёрке”":
                jump prepare_danceyes_noteyes_articleyes
            "Не рисковать. Довести до конца то, что начал":
                jump prepare_danceyes_noteyes_articleno

label prepare_danceyes_noteyes_articleyes:
    
    scene fail:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0
    
    "Ты находишь связь между теорией графов и эмерджентностью. Башлыкова любит такие кросс-темы. Возможно, это билет №7…"
    
    scene koridor:
        xysize (1980, 1080)
    play music "university.mp3" fadeout 2.0 fadein 3.0

    "Утро понедельника. Ты стоишь перед аудиторией №317. В кармане — шпаргалка с формулами, которую Настя всунула тебе со словами"

    show characternasty at left
    n "На всякий случай"
    hide characternasty 

    "Из-за двери доносится голос Башлыковой"

    show characterbashlikova at left
    b "Следующий!"
    hide characterbashlikova 

    show hero at left
    v "Я сделал всё, что мог. Или нет?"
    hide hero 

    "Дверь аудитории №317 скрипит, словно предупреждая: «Поздно поворачивать назад». Ты заходишь внутрь. Воздух густой от запаха старой бумаги и тревоги. "

    scene office:
        xysize (1980, 1080)
    play music "office.mp3" fadeout 2.0 fadein 3.0
   
   
    "За столом, как монумент непоколебимости, сидит Башлыкова А.А. Её взгляд скользит по тебе, будто рентген, просвечивающий каждую невыученную тему."

    show characterbashlikova at left
    b "Фамилия?"
    hide characterbashlikova 

    "Ты отвечаешь. Она кивает, указывая на стул."

    show characterbashlikova at left
    b "Билет на столе. Пятнадцать минут. И…"
    b "не вздумайте жевать слова. Я терпеть не могу невнятицу."
    hide characterbashlikova

    "На столе лежат три билета. Ты тянешь наугад — №7"
    
    show hero at left
    h "Эмерджентность в теории систем. Связь с теорией графов. Примеры из реальных кейсов"
    v "Черт, я же пропустил статьи…"
    hide hero

    jump finish2

label prepare_danceyes_noteyes_articleno:
    scene obshegi:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0
    
    "Ты фокусируешься на базовых понятиях. Интуиция шепчет: Анна Александровна ценит фундамент больше, чем эрудицию."
    
    scene koridor:
        xysize (1980, 1080)
    play music "university.mp3" fadeout 2.0 fadein 3.0

    "Утро понедельника. Ты стоишь перед аудиторией №317. В кармане — шпаргалка с формулами, которую Настя всунула тебе со словами"

    show characternasty at left
    n "На всякий случай"
    hide characternasty 

    "Из-за двери доносится голос Башлыковой"

    show characterbashlikova at left
    b "Следующий!"
    hide characterbashlikova 

    show hero at left
    v "Я сделал всё, что мог. Или нет?"
    hide hero 

    "Дверь аудитории №317 скрипит, словно предупреждая: «Поздно поворачивать назад». Ты заходишь внутрь. Воздух густой от запаха старой бумаги и тревоги. "

    scene office:
        xysize (1980, 1080)
    play music "office.mp3" fadeout 2.0 fadein 3.0
   
   
    "За столом, как монумент непоколебимости, сидит Башлыкова А.А. Её взгляд скользит по тебе, будто рентген, просвечивающий каждую невыученную тему."

    show characterbashlikova at left
    b "Фамилия?"
    hide characterbashlikova 

    "Ты отвечаешь. Она кивает, указывая на стул."

    show characterbashlikova at left
    b "Билет на столе. Пятнадцать минут. И…"
    b "не вздумайте жевать слова. Я терпеть не могу невнятицу."
    hide characterbashlikova

    "На столе лежат три билета. Ты тянешь наугад — №7"

    show hero at left
    h "Эмерджентность в теории систем. Связь с теорией графов. Примеры из реальных кейсов"
    v "Черт, я же пропустил статьи…"
    hide hero

    jump finish2

label prepare_danceyes_noteno:
    show hero at left
    h "Не надо, я сам разберусь"
    hide hero

    "Настя пожимает плечами"

    show characternasty at left
    n "Ну, как знаешь. Не говори потом, что я не предлагала."
    hide characternasty 
    
    "Ты остаешься с учебником, но чувствуешь, что чего-то не хватает."
    "Воскресенье. Последняя ночь перед экзаменом. Ты повторяешь материал, когда в дверь врывается Настя с лицом, как у загнанного зверя:"

    scene obshegi:
        xysize (1980, 1080)

    show characternasty at left
    n "Ты видел, что Башлыкова выложила в СДО? Дополнительные статьи по эмерджентности! Это ловушка? Или подсказка?"
    hide characternasty 

    menu prepare_danceyes_noteno_article:
            "Прочитать статьи?"
            "Прочитать статьи. Вдруг это ключ к “пятёрке”":
                jump prepare_danceyes_noteno_articleyes 
            "Не рисковать. Довести до конца то, что начал":
                jump prepare_danceyes_noteno_articleno 

label prepare_danceyes_noteno_articleyes:
    
    scene fail:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0
    
    "Ты находишь связь между теорией графов и эмерджентностью. Башлыкова любит такие кросс-темы. Возможно, это билет №7…"
    
    scene koridor:
        xysize (1980, 1080)
    play music "university.mp3" fadeout 2.0 fadein 3.0

    "Утро понедельника. Ты стоишь перед аудиторией №317. В кармане — шпаргалка с формулами, которую Настя всунула тебе со словами"

    show characternasty at left
    n "На всякий случай"
    hide characternasty 

    "Из-за двери доносится голос Башлыковой"

    show characterbashlikova at left
    b "Следующий!"
    hide characterbashlikova 

    show hero at left
    v "Я сделал всё, что мог. Или нет?"
    hide hero 

    "Дверь аудитории №317 скрипит, словно предупреждая: «Поздно поворачивать назад». Ты заходишь внутрь. Воздух густой от запаха старой бумаги и тревоги. "

    scene office:
        xysize (1980, 1080)
    play music "office.mp3" fadeout 2.0 fadein 3.0
   
   
    "За столом, как монумент непоколебимости, сидит Башлыкова А.А. Её взгляд скользит по тебе, будто рентген, просвечивающий каждую невыученную тему."

    show characterbashlikova at left
    b "Фамилия?"
    hide characterbashlikova 

    "Ты отвечаешь. Она кивает, указывая на стул."

    show characterbashlikova at left
    b "Билет на столе. Пятнадцать минут. И…"
    b "не вздумайте жевать слова. Я терпеть не могу невнятицу."
    hide characterbashlikova

    "На столе лежат три билета. Ты тянешь наугад — №7"

    jump finish1

label prepare_danceyes_noteno_articleno:
    scene obshegi:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0
    
    "Ты фокусируешься на базовых понятиях. Интуиция шепчет: Анна Александровна ценит фундамент больше, чем эрудицию."
    
    scene koridor:
        xysize (1980, 1080)
    play music "university.mp3" fadeout 2.0 fadein 3.0

    "Утро понедельника. Ты стоишь перед аудиторией №317. В кармане — шпаргалка с формулами, которую Настя всунула тебе со словами"

    show characternasty at left
    n "На всякий случай"
    hide characternasty 

    "Из-за двери доносится голос Башлыковой"

    show characterbashlikova at left
    b "Следующий!"
    hide characterbashlikova 

    show hero at left
    v "Я сделал всё, что мог. Или нет?"
    hide hero 

    "Дверь аудитории №317 скрипит, словно предупреждая: «Поздно поворачивать назад». Ты заходишь внутрь. Воздух густой от запаха старой бумаги и тревоги. "

    scene office:
        xysize (1980, 1080)
    play music "office.mp3" fadeout 2.0 fadein 3.0
   
   
    "За столом, как монумент непоколебимости, сидит Башлыкова А.А. Её взгляд скользит по тебе, будто рентген, просвечивающий каждую невыученную тему."

    show characterbashlikova at left
    b "Фамилия?"
    hide characterbashlikova 

    "Ты отвечаешь. Она кивает, указывая на стул."

    show characterbashlikova at left
    b "Билет на столе. Пятнадцать минут. И…"
    b "не вздумайте жевать слова. Я терпеть не могу невнятицу."
    hide characterbashlikova

    "На столе лежат три билета. Ты тянешь наугад — №7"

    show hero at left
    h "Эмерджентность в теории систем. Связь с теорией графов. Примеры из реальных кейсов"
    v "Черт, я же пропустил статьи…"
    hide hero

    jump finish2sh

label prepare_danceno:
    show hero at left
    h "Не сейчас. Мне надо учить"
    hide hero

    "Лёха фыркает, но кивает с уважением:"

    show characterleha at left
    l "Ладно. Но если передумаешь — мы до утра бумбокс не выключим."
    hide characterleha 
    
    play music "vibration.mp3" fadeout 3.0 fadein 0.5
    "К полуночи глаза слипаются, а в чате группы всплывает новое сообщение"
    play music "backgroundmusic.mp3" fadein 2.0

    show characterleha at left
    l "Пацаны, я нашел старые билеты Башлыковой в архиве! Кидаю вам, только не говорите никому."
    hide characterleha

    "К тебе прилетает файл «Секретно_не_открывать.pdf»."

    menu prepare_danceno_fail:
            "Открыть файл?"
            "Открыть файл. Может, попадётся тот же билет":
                jump prepare_danceno_failyes 
            "Игнорировать. Доверяй только учебнику":
                jump prepare_danceno_failno 

label prepare_danceno_failyes:
    scene fail:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0

    "Ты изучаешь вопросы. Один из них — про эмерджентность в теории систем. "
    "Странно, но в учебнике об этом пара абзацев. Придётся искать доп источники."
    "Воскресенье. Последняя ночь перед экзаменом. Ты повторяешь материал, когда в дверь врывается Настя с лицом, как у загнанного зверя:"

    scene obshegi:
        xysize (1980, 1080)

    "Утро. Настя стучит в дверь, держа в руках конспекты толщиной с кирпич"

    show characternasty at left
    n "Привет! Лиза сказала, ты пашешь как проклятый. Держи мои заметки по эмерджентности — там всё, что Башлыкова упоминала на семинарах."
    hide characternasty 

    menu prepare_danceno_failyes_note:
            "Взять заметки?"
            "Спасибо! Это спасение":
                jump prepare_danceno_failyes_noteyes 
            "Не надо, я сам разберусь":
                jump prepare_danceno_failyes_noteno 

label prepare_danceno_failyes_noteyes:
    show hero at left
    h "Спасибо! Это спасение"
    hide hero

    "Ты дополняешь свои записи. Оказывается, Анна Александровна обожает задавать каверзные вопросы про «неочевидные свойства систем». Теперь ты готов"
    "Воскресенье. Последняя ночь перед экзаменом. Ты повторяешь материал, когда в дверь врывается Настя с лицом, как у загнанного зверя:"

    scene obshegi:
        xysize (1980, 1080)

    show characternasty at left
    n "Ты видел, что Башлыкова выложила в СДО? Дополнительные статьи по эмерджентности! Это ловушка? Или подсказка?"
    hide characternasty 

    menu prepare_danceno_failyes_noteyes_article:
            "Прочитать статьи?"
            "Прочитать статьи. Вдруг это ключ к “пятёрке”":
                jump prepare_danceno_failyes_noteyes_articleyes
            "Не рисковать. Довести до конца то, что начал":
                jump prepare_danceno_failyes_noteyes_articleno

label prepare_danceno_failyes_noteyes_articleyes:
    
    scene fail:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0
    
    "Ты находишь связь между теорией графов и эмерджентностью. Башлыкова любит такие кросс-темы. Возможно, это билет №7…"
    
    scene koridor:
        xysize (1980, 1080)
    play music "university.mp3" fadeout 2.0 fadein 3.0

    "Утро понедельника. Ты стоишь перед аудиторией №317. В кармане — шпаргалка с формулами, которую Настя всунула тебе со словами"

    show characternasty at left
    n "На всякий случай"
    hide characternasty 

    "Из-за двери доносится голос Башлыковой"

    show characterbashlikova at left
    b "Следующий!"
    hide characterbashlikova 

    show hero at left
    v "Я сделал всё, что мог. Или нет?"
    hide hero 

    "Дверь аудитории №317 скрипит, словно предупреждая: «Поздно поворачивать назад». Ты заходишь внутрь. Воздух густой от запаха старой бумаги и тревоги. "

    scene office:
        xysize (1980, 1080)
    play music "office.mp3" fadeout 2.0 fadein 3.0
   
   
    "За столом, как монумент непоколебимости, сидит Башлыкова А.А. Её взгляд скользит по тебе, будто рентген, просвечивающий каждую невыученную тему."

    show characterbashlikova at left
    b "Фамилия?"
    hide characterbashlikova 

    "Ты отвечаешь. Она кивает, указывая на стул."

    show characterbashlikova at left
    b "Билет на столе. Пятнадцать минут. И…"
    b "не вздумайте жевать слова. Я терпеть не могу невнятицу."
    hide characterbashlikova

    "На столе лежат три билета. Ты тянешь наугад — №7"

    jump finish1

label prepare_danceno_failyes_noteyes_articleno:
    scene obshegi:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0
    
    "Ты фокусируешься на базовых понятиях. Интуиция шепчет: Анна Александровна ценит фундамент больше, чем эрудицию."
    
    scene koridor:
        xysize (1980, 1080)
    play music "university.mp3" fadeout 2.0 fadein 3.0

    "Утро понедельника. Ты стоишь перед аудиторией №317. В кармане — шпаргалка с формулами, которую Настя всунула тебе со словами"

    show characternasty at left
    n "На всякий случай"
    hide characternasty 

    "Из-за двери доносится голос Башлыковой"

    show characterbashlikova at left
    b "Следующий!"
    hide characterbashlikova 

    show hero at left
    v "Я сделал всё, что мог. Или нет?"
    hide hero 

    "Дверь аудитории №317 скрипит, словно предупреждая: «Поздно поворачивать назад». Ты заходишь внутрь. Воздух густой от запаха старой бумаги и тревоги. "

    scene office:
        xysize (1980, 1080)
    play music "office.mp3" fadeout 2.0 fadein 3.0
   
   
    "За столом, как монумент непоколебимости, сидит Башлыкова А.А. Её взгляд скользит по тебе, будто рентген, просвечивающий каждую невыученную тему."

    show characterbashlikova at left
    b "Фамилия?"
    hide characterbashlikova 

    "Ты отвечаешь. Она кивает, указывая на стул."

    show characterbashlikova at left
    b "Билет на столе. Пятнадцать минут. И…"
    b "не вздумайте жевать слова. Я терпеть не могу невнятицу."
    hide characterbashlikova

    "На столе лежат три билета. Ты тянешь наугад — №7"

    jump finish3

label prepare_danceno_failyes_noteno:
    show hero at left
    h "Не надо, я сам разберусь"
    hide hero

    "Настя пожимает плечами"

    show characternasty at left
    n "Ну, как знаешь. Не говори потом, что я не предлагала."
    hide characternasty 
    
    "Ты остаешься с учебником, но чувствуешь, что чего-то не хватает."
    "Воскресенье. Последняя ночь перед экзаменом. Ты повторяешь материал, когда в дверь врывается Настя с лицом, как у загнанного зверя:"

    scene obshegi:
        xysize (1980, 1080)

    show characternasty at left
    n "Ты видел, что Башлыкова выложила в СДО? Дополнительные статьи по эмерджентности! Это ловушка? Или подсказка?"
    hide characternasty 

    menu prepare_danceno_failyes_noteno_article:
            "Прочитать статьи?"
            "Прочитать статьи. Вдруг это ключ к “пятёрке”":
                jump prepare_danceno_failyes_noteno_articleyes 
            "Не рисковать. Довести до конца то, что начал":
                jump prepare_danceno_failyes_noteno_articleno 

label prepare_danceno_failyes_noteno_articleyes:
    
    scene fail:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0
    
    "Ты находишь связь между теорией графов и эмерджентностью. Башлыкова любит такие кросс-темы. Возможно, это билет №7…"
    
    scene koridor:
        xysize (1980, 1080)
    play music "university.mp3" fadeout 2.0 fadein 3.0

    "Утро понедельника. Ты стоишь перед аудиторией №317. В кармане — шпаргалка с формулами, которую Настя всунула тебе со словами"

    show characternasty at left
    n "На всякий случай"
    hide characternasty 

    "Из-за двери доносится голос Башлыковой"

    show characterbashlikova at left
    b "Следующий!"
    hide characterbashlikova 

    show hero at left
    v "Я сделал всё, что мог. Или нет?"
    hide hero 

    "Дверь аудитории №317 скрипит, словно предупреждая: «Поздно поворачивать назад». Ты заходишь внутрь. Воздух густой от запаха старой бумаги и тревоги. "

    scene office:
        xysize (1980, 1080)
    play music "office.mp3" fadeout 2.0 fadein 3.0
   
   
    "За столом, как монумент непоколебимости, сидит Башлыкова А.А. Её взгляд скользит по тебе, будто рентген, просвечивающий каждую невыученную тему."

    show characterbashlikova at left
    b "Фамилия?"
    hide characterbashlikova 

    "Ты отвечаешь. Она кивает, указывая на стул."

    show characterbashlikova at left
    b "Билет на столе. Пятнадцать минут. И…"
    b "не вздумайте жевать слова. Я терпеть не могу невнятицу."
    hide characterbashlikova

    "На столе лежат три билета. Ты тянешь наугад — №7"

    show hero at left
    h "Эмерджентность в теории систем. Связь с теорией графов. Примеры из реальных кейсов"
    v "Черт, я же пропустил статьи…"
    hide hero

    jump finish2

label prepare_danceno_failyes_noteno_articleno:
    scene obshegi:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0
    
    "Ты фокусируешься на базовых понятиях. Интуиция шепчет: Анна Александровна ценит фундамент больше, чем эрудицию."
    
    scene koridor:
        xysize (1980, 1080)
    play music "university.mp3" fadeout 2.0 fadein 3.0

    "Утро понедельника. Ты стоишь перед аудиторией №317. В кармане — шпаргалка с формулами, которую Настя всунула тебе со словами"

    show characternasty at left
    n "На всякий случай"
    hide characternasty 

    "Из-за двери доносится голос Башлыковой"

    show characterbashlikova at left
    b "Следующий!"
    hide characterbashlikova 

    show hero at left
    v "Я сделал всё, что мог. Или нет?"
    hide hero 

    "Дверь аудитории №317 скрипит, словно предупреждая: «Поздно поворачивать назад». Ты заходишь внутрь. Воздух густой от запаха старой бумаги и тревоги. "

    scene office:
        xysize (1980, 1080)
    play music "office.mp3" fadeout 2.0 fadein 3.0
   
   
    "За столом, как монумент непоколебимости, сидит Башлыкова А.А. Её взгляд скользит по тебе, будто рентген, просвечивающий каждую невыученную тему."

    show characterbashlikova at left
    b "Фамилия?"
    hide characterbashlikova 

    "Ты отвечаешь. Она кивает, указывая на стул."

    show characterbashlikova at left
    b "Билет на столе. Пятнадцать минут. И…"
    b "не вздумайте жевать слова. Я терпеть не могу невнятицу."
    hide characterbashlikova

    "На столе лежат три билета. Ты тянешь наугад — №7"

    jump finish3

label prepare_danceno_failno:
    scene fail:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0

    "Ты изучаешь вопросы. Один из них — про эмерджентность в теории систем. "
    "Странно, но в учебнике об этом пара абзацев. Придётся искать доп источники."
    "Воскресенье. Последняя ночь перед экзаменом. Ты повторяешь материал, когда в дверь врывается Настя с лицом, как у загнанного зверя:"

    scene obshegi:
        xysize (1980, 1080)

    "Утро. Настя стучит в дверь, держа в руках конспекты толщиной с кирпич"

    show characternasty at left
    n "Привет! Лиза сказала, ты пашешь как проклятый. Держи мои заметки по эмерджентности — там всё, что Башлыкова упоминала на семинарах."
    hide characternasty 

    menu prepare_danceno_failno_note:
            "Взять заметки?"
            "Спасибо! Это спасение":
                jump prepare_danceno_failno_noteyes 
            "Не надо, я сам разберусь":
                jump prepare_danceno_failno_noteno 

label prepare_danceno_failno_noteyes:
    show hero at left
    h "Спасибо! Это спасение"
    hide hero

    "Ты дополняешь свои записи. Оказывается, Анна Александровна обожает задавать каверзные вопросы про «неочевидные свойства систем». Теперь ты готов"
    "Воскресенье. Последняя ночь перед экзаменом. Ты повторяешь материал, когда в дверь врывается Настя с лицом, как у загнанного зверя:"

    scene obshegi:
        xysize (1980, 1080)

    show characternasty at left
    n "Ты видел, что Башлыкова выложила в СДО? Дополнительные статьи по эмерджентности! Это ловушка? Или подсказка?"
    hide characternasty 

    menu prepare_danceno_failno_noteyes_article:
            "Прочитать статьи?"
            "Прочитать статьи. Вдруг это ключ к “пятёрке”":
                jump prepare_danceno_failno_noteyes_articleyes
            "Не рисковать. Довести до конца то, что начал":
                jump prepare_danceno_failno_noteyes_articleno

label prepare_danceno_failno_noteyes_articleyes:
    
    scene fail:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0
    
    "Ты находишь связь между теорией графов и эмерджентностью. Башлыкова любит такие кросс-темы. Возможно, это билет №7…"
    
    scene koridor:
        xysize (1980, 1080)
    play music "university.mp3" fadeout 2.0 fadein 3.0

    "Утро понедельника. Ты стоишь перед аудиторией №317. В кармане — шпаргалка с формулами, которую Настя всунула тебе со словами"

    show characternasty at left
    n "На всякий случай"
    hide characternasty 

    "Из-за двери доносится голос Башлыковой"

    show characterbashlikova at left
    b "Следующий!"
    hide characterbashlikova 

    show hero at left
    v "Я сделал всё, что мог. Или нет?"
    hide hero 

    "Дверь аудитории №317 скрипит, словно предупреждая: «Поздно поворачивать назад». Ты заходишь внутрь. Воздух густой от запаха старой бумаги и тревоги. "

    scene office:
        xysize (1980, 1080)
    play music "office.mp3" fadeout 2.0 fadein 3.0
   
   
    "За столом, как монумент непоколебимости, сидит Башлыкова А.А. Её взгляд скользит по тебе, будто рентген, просвечивающий каждую невыученную тему."

    show characterbashlikova at left
    b "Фамилия?"
    hide characterbashlikova 

    "Ты отвечаешь. Она кивает, указывая на стул."

    show characterbashlikova at left
    b "Билет на столе. Пятнадцать минут. И…"
    b "не вздумайте жевать слова. Я терпеть не могу невнятицу."
    hide characterbashlikova

    "На столе лежат три билета. Ты тянешь наугад — №7"

    jump finish1

label prepare_danceno_failno_noteyes_articleno:
    scene obshegi:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0
    
    "Ты фокусируешься на базовых понятиях. Интуиция шепчет: Анна Александровна ценит фундамент больше, чем эрудицию."
    
    scene koridor:
        xysize (1980, 1080)
    play music "university.mp3" fadeout 2.0 fadein 3.0

    "Утро понедельника. Ты стоишь перед аудиторией №317. В кармане — шпаргалка с формулами, которую Настя всунула тебе со словами"

    show characternasty at left
    n "На всякий случай"
    hide characternasty 

    "Из-за двери доносится голос Башлыковой"

    show characterbashlikova at left
    b "Следующий!"
    hide characterbashlikova 

    show hero at left
    v "Я сделал всё, что мог. Или нет?"
    hide hero 

    "Дверь аудитории №317 скрипит, словно предупреждая: «Поздно поворачивать назад». Ты заходишь внутрь. Воздух густой от запаха старой бумаги и тревоги. "

    scene office:
        xysize (1980, 1080)
    play music "office.mp3" fadeout 2.0 fadein 3.0
   
   
    "За столом, как монумент непоколебимости, сидит Башлыкова А.А. Её взгляд скользит по тебе, будто рентген, просвечивающий каждую невыученную тему."

    show characterbashlikova at left
    b "Фамилия?"
    hide characterbashlikova 

    "Ты отвечаешь. Она кивает, указывая на стул."

    show characterbashlikova at left
    b "Билет на столе. Пятнадцать минут. И…"
    b "не вздумайте жевать слова. Я терпеть не могу невнятицу."
    hide characterbashlikova

    "На столе лежат три билета. Ты тянешь наугад — №7"

    jump finish3

label prepare_danceno_failno_noteno:
    show hero at left
    h "Не надо, я сам разберусь"
    hide hero

    "Настя пожимает плечами"

    show characternasty at left
    n "Ну, как знаешь. Не говори потом, что я не предлагала."
    hide characternasty 
    
    "Ты остаешься с учебником, но чувствуешь, что чего-то не хватает."
    "Воскресенье. Последняя ночь перед экзаменом. Ты повторяешь материал, когда в дверь врывается Настя с лицом, как у загнанного зверя:"

    scene obshegi:
        xysize (1980, 1080)

    show characternasty at left
    n "Ты видел, что Башлыкова выложила в СДО? Дополнительные статьи по эмерджентности! Это ловушка? Или подсказка?"
    hide characternasty 

    menu prepare_danceno_failno_noteno_article:
            "Прочитать статьи?"
            "Прочитать статьи. Вдруг это ключ к “пятёрке”":
                jump prepare_danceno_failno_noteno_articleyes 
            "Не рисковать. Довести до конца то, что начал":
                jump prepare_danceno_failno_noteno_articleno 

label prepare_danceno_failno_noteno_articleyes:
    
    scene fail:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0
    
    "Ты находишь связь между теорией графов и эмерджентностью. Башлыкова любит такие кросс-темы. Возможно, это билет №7…"
    
    scene koridor:
        xysize (1980, 1080)
    play music "university.mp3" fadeout 2.0 fadein 3.0

    "Утро понедельника. Ты стоишь перед аудиторией №317. В кармане — шпаргалка с формулами, которую Настя всунула тебе со словами"

    show characternasty at left
    n "На всякий случай"
    hide characternasty 

    "Из-за двери доносится голос Башлыковой"

    show characterbashlikova at left
    b "Следующий!"
    hide characterbashlikova 

    show hero at left
    v "Я сделал всё, что мог. Или нет?"
    hide hero 

    "Дверь аудитории №317 скрипит, словно предупреждая: «Поздно поворачивать назад». Ты заходишь внутрь. Воздух густой от запаха старой бумаги и тревоги. "

    scene office:
        xysize (1980, 1080)
    play music "office.mp3" fadeout 2.0 fadein 3.0
   
   
    "За столом, как монумент непоколебимости, сидит Башлыкова А.А. Её взгляд скользит по тебе, будто рентген, просвечивающий каждую невыученную тему."

    show characterbashlikova at left
    b "Фамилия?"
    hide characterbashlikova 

    "Ты отвечаешь. Она кивает, указывая на стул."

    show characterbashlikova at left
    b "Билет на столе. Пятнадцать минут. И…"
    b "не вздумайте жевать слова. Я терпеть не могу невнятицу."
    hide characterbashlikova

    "На столе лежат три билета. Ты тянешь наугад — №7"

    show hero at left
    h "Эмерджентность в теории систем. Связь с теорией графов. Примеры из реальных кейсов"
    v "Черт, я же пропустил статьи…"
    hide hero

    jump finish2sh

label prepare_danceno_failno_noteno_articleno:
    scene obshegi:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0
    
    "Ты фокусируешься на базовых понятиях. Интуиция шепчет: Анна Александровна ценит фундамент больше, чем эрудицию."
    
    scene koridor:
        xysize (1980, 1080)
    play music "university.mp3" fadeout 2.0 fadein 3.0

    "Утро понедельника. Ты стоишь перед аудиторией №317. В кармане — шпаргалка с формулами, которую Настя всунула тебе со словами"

    show characternasty at left
    n "На всякий случай"
    hide characternasty 

    "Из-за двери доносится голос Башлыковой"

    show characterbashlikova at left
    b "Следующий!"
    hide characterbashlikova 

    show hero at left
    v "Я сделал всё, что мог. Или нет?"
    hide hero 

    "Дверь аудитории №317 скрипит, словно предупреждая: «Поздно поворачивать назад». Ты заходишь внутрь. Воздух густой от запаха старой бумаги и тревоги. "

    scene office:
        xysize (1980, 1080)
    play music "office.mp3" fadeout 2.0 fadein 3.0
   
   
    "За столом, как монумент непоколебимости, сидит Башлыкова А.А. Её взгляд скользит по тебе, будто рентген, просвечивающий каждую невыученную тему."

    show characterbashlikova at left
    b "Фамилия?"
    hide characterbashlikova 

    "Ты отвечаешь. Она кивает, указывая на стул."

    show characterbashlikova at left
    b "Билет на столе. Пятнадцать минут. И…"
    b "не вздумайте жевать слова. Я терпеть не могу невнятицу."
    hide characterbashlikova

    "На столе лежат три билета. Ты тянешь наугад — №7"

    show hero at left
    h "Эмерджентность в теории систем. Связь с теорией графов. Примеры из реальных кейсов"
    v "Черт, я же пропустил статьи…"
    hide hero

    jump finish2sh

label prepareno:
    show hero at left
    v "Нет. Ещё три дня — как три вечности. Лучше завтра"
    hide hero 

    "Ты закрываешь ноутбук. В голове всплывает фраза Башлыковой из прошлого семестра." 

    show characterbashlikova at left
    b "Прокрастинация — путь в академический ад. "
    hide characterbashlikova 

    "Но зачем думать об этом сейчас? Завтра точно начнёшь." 

    play music "vibration.mp3" fadeout 3.0 fadein 0.5
    "К полуночи глаза слипаются, а в чате группы всплывает новое сообщение"
    play music "backgroundmusic.mp3" fadein 2.0

    show characterleha at left
    l "Пацаны, я нашел старые билеты Башлыковой в архиве! Кидаю вам, только не говорите никому."
    hide characterleha

    "К тебе прилетает файл «Секретно_не_открывать.pdf»."

    menu prepareno_fail:
            "Открыть файл?"
            "Открыть файл. Может, попадётся тот же билет":
                jump prepareno_failyes 
            "Игнорировать. Доверяй только учебнику":
                jump prepareno_failno    

label prepareno_failyes:
    scene fail:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0

    "Ты изучаешь вопросы. Один из них — про эмерджентность в теории систем. "
    "Странно, но в учебнике об этом пара абзацев. Придётся искать доп источники."
    "Воскресенье. Последняя ночь перед экзаменом. Ты повторяешь материал, когда в дверь врывается Настя с лицом, как у загнанного зверя:"

    
    scene obshegi:
        xysize (1980, 1080)

    show characternasty at left
    n "Ты видел, что Башлыкова выложила в СДО? Дополнительные статьи по эмерджентности! Это ловушка? Или подсказка?"
    hide characternasty 

    menu prepareno_failyes_article:
            "Прочитать статьи?"
            "Прочитать статьи. Вдруг это ключ к “пятёрке”":
                jump prepareno_failyes_articleyes 
            "Не рисковать. Довести до конца то, что начал":
                jump prepareno_failyes_articleno 

label prepareno_failyes_articleyes:
    
    scene fail:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0
    
    "Ты находишь связь между теорией графов и эмерджентностью. Башлыкова любит такие кросс-темы. Возможно, это билет №7…"
    
    scene koridor:
        xysize (1980, 1080)
    play music "university.mp3" fadeout 2.0 fadein 3.0

    "Утро понедельника. Ты стоишь перед аудиторией №317. В кармане — шпаргалка с формулами, которую Настя всунула тебе со словами"

    show characternasty at left
    n "На всякий случай"
    hide characternasty 

    "Из-за двери доносится голос Башлыковой"

    show characterbashlikova at left
    b "Следующий!"
    hide characterbashlikova 

    show hero at left
    v "Я сделал всё, что мог. Или нет?"
    hide hero 

    "Дверь аудитории №317 скрипит, словно предупреждая: «Поздно поворачивать назад». Ты заходишь внутрь. Воздух густой от запаха старой бумаги и тревоги. "

    scene office:
        xysize (1980, 1080)
    play music "office.mp3" fadeout 2.0 fadein 3.0
   
   
    "За столом, как монумент непоколебимости, сидит Башлыкова А.А. Её взгляд скользит по тебе, будто рентген, просвечивающий каждую невыученную тему."

    show characterbashlikova at left
    b "Фамилия?"
    hide characterbashlikova 

    "Ты отвечаешь. Она кивает, указывая на стул."

    show characterbashlikova at left
    b "Билет на столе. Пятнадцать минут. И…"
    b "не вздумайте жевать слова. Я терпеть не могу невнятицу."
    hide characterbashlikova

    "На столе лежат три билета. Ты тянешь наугад — №7"

    jump finish1

label prepareno_failyes_articleno:
    scene obshegi:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0
    
    "Ты фокусируешься на базовых понятиях. Интуиция шепчет: Анна Александровна ценит фундамент больше, чем эрудицию."
    
    scene koridor:
        xysize (1980, 1080)
    play music "university.mp3" fadeout 2.0 fadein 3.0

    "Утро понедельника. Ты стоишь перед аудиторией №317. В кармане — шпаргалка с формулами, которую Настя всунула тебе со словами"

    show characternasty at left
    n "На всякий случай"
    hide characternasty 

    "Из-за двери доносится голос Башлыковой"

    show characterbashlikova at left
    b "Следующий!"
    hide characterbashlikova 

    show hero at left
    v "Я сделал всё, что мог. Или нет?"
    hide hero 

    "Дверь аудитории №317 скрипит, словно предупреждая: «Поздно поворачивать назад». Ты заходишь внутрь. Воздух густой от запаха старой бумаги и тревоги. "

    scene office:
        xysize (1980, 1080)
    play music "office.mp3" fadeout 2.0 fadein 3.0
   
   
    "За столом, как монумент непоколебимости, сидит Башлыкова А.А. Её взгляд скользит по тебе, будто рентген, просвечивающий каждую невыученную тему."

    show characterbashlikova at left
    b "Фамилия?"
    hide characterbashlikova 

    "Ты отвечаешь. Она кивает, указывая на стул."

    show characterbashlikova at left
    b "Билет на столе. Пятнадцать минут. И…"
    b "не вздумайте жевать слова. Я терпеть не могу невнятицу."
    hide characterbashlikova

    "На столе лежат три билета. Ты тянешь наугад — №7"

    show hero at left
    h "Эмерджентность в теории систем. Связь с теорией графов. Примеры из реальных кейсов"
    v "Черт, я же пропустил статьи…"
    hide hero

    jump finish2

label prepareno_failno:
    scene fail:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0

    "Ты продолжаешь зубрить теорию графов. За окном уже рассвет, но ты чувствуешь: эта тема теперь отскакивает от зубов. "
    "Воскресенье. Последняя ночь перед экзаменом. Ты повторяешь материал, когда в дверь врывается Настя с лицом, как у загнанного зверя:"

    scene obshegi:
        xysize (1980, 1080)

    show characternasty at left
    n "Ты видел, что Башлыкова выложила в СДО? Дополнительные статьи по эмерджентности! Это ловушка? Или подсказка?"
    hide characternasty 

    menu prepareno_failno_article:
            "Прочитать статьи?"
            "Прочитать статьи. Вдруг это ключ к “пятёрке”":
                jump prepareno_failno_articleyes 
            "Не рисковать. Довести до конца то, что начал":
                jump prepareno_failno_articleno 

label prepareno_failno_articleyes:
    scene fail:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0
    
    "Ты находишь связь между теорией графов и эмерджентностью. Башлыкова любит такие кросс-темы. Возможно, это билет №7…"
    
    scene koridor:
        xysize (1980, 1080)
    play music "university.mp3" fadeout 2.0 fadein 3.0

    "Утро понедельника. Ты стоишь перед аудиторией №317. В кармане — шпаргалка с формулами, которую Настя всунула тебе со словами"

    show characternasty at left
    n "На всякий случай"
    hide characternasty 

    "Из-за двери доносится голос Башлыковой"

    show characterbashlikova at left
    b "Следующий!"
    hide characterbashlikova 

    show hero at left
    v "Я сделал всё, что мог. Или нет?"
    hide hero 

    "Дверь аудитории №317 скрипит, словно предупреждая: «Поздно поворачивать назад». Ты заходишь внутрь. Воздух густой от запаха старой бумаги и тревоги. "

    scene office:
        xysize (1980, 1080)
    play music "office.mp3" fadeout 2.0 fadein 3.0
   
   
    "За столом, как монумент непоколебимости, сидит Башлыкова А.А. Её взгляд скользит по тебе, будто рентген, просвечивающий каждую невыученную тему."

    show characterbashlikova at left
    b "Фамилия?"
    hide characterbashlikova 

    "Ты отвечаешь. Она кивает, указывая на стул."

    show characterbashlikova at left
    b "Билет на столе. Пятнадцать минут. И…"
    b "не вздумайте жевать слова. Я терпеть не могу невнятицу."
    hide characterbashlikova

    "На столе лежат три билета. Ты тянешь наугад — №7"

    show hero at left
    h "Эмерджентность в теории систем. Связь с теорией графов. Примеры из реальных кейсов"
    v "Черт, я же пропустил статьи…"
    hide hero

    jump finish2

label prepareno_failno_articleno: 
    scene obshegi:
        xysize (1980, 1080)
    play music "backgroundmusic.mp3" fadeout 2.0 fadein 3.0
    
    "Ты фокусируешься на базовых понятиях. Интуиция шепчет: Анна Александровна ценит фундамент больше, чем эрудицию."
    
    scene koridor:
        xysize (1980, 1080)
    play music "university.mp3" fadeout 2.0 fadein 3.0

    "Утро понедельника. Ты стоишь перед аудиторией №317. В кармане — шпаргалка с формулами, которую Настя всунула тебе со словами"

    show characternasty at left
    n "На всякий случай"
    hide characternasty 

    "Из-за двери доносится голос Башлыковой"

    show characterbashlikova at left
    b "Следующий!"
    hide characterbashlikova 

    show hero at left
    v "Я сделал всё, что мог. Или нет?"
    hide hero 

    "Дверь аудитории №317 скрипит, словно предупреждая: «Поздно поворачивать назад». Ты заходишь внутрь. Воздух густой от запаха старой бумаги и тревоги. "

    scene office:
        xysize (1980, 1080)
    play music "office.mp3" fadeout 2.0 fadein 3.0
   
   
    "За столом, как монумент непоколебимости, сидит Башлыкова А.А. Её взгляд скользит по тебе, будто рентген, просвечивающий каждую невыученную тему."

    show characterbashlikova at left
    b "Фамилия?"
    hide characterbashlikova 

    "Ты отвечаешь. Она кивает, указывая на стул."

    show characterbashlikova at left
    b "Билет на столе. Пятнадцать минут. И…"
    b "не вздумайте жевать слова. Я терпеть не могу невнятицу."
    hide characterbashlikova

    "На столе лежат три билета. Ты тянешь наугад — №7"

    jump finish3

#---ФИНИШИ---
label finish1:
    scene office:
        xysize (1980, 1080)
    play music "office.mp3" fadeout 2.0 fadein 3.0

    show hero at left
    h "Эмерджентность в теории систем. Связь с теорией графов. Примеры из реальных кейсов"
    v "Это же та самая кросс-тема из статей!"
    hide hero

    scene black:
        xysize (1980, 1080)
    "Проходит 15 минут. Ты рассказиываеь, что знаешь на эту."

    scene office:
        xysize (1980, 1080)
    play music "office.mp3" fadeout 2.0 fadein 3.0

    show characterbashlikova at left
    b "Дополнительный вопрос"
    hide characterbashlikova 

    "Она берёт учебник и тычет пальцем в схему."

    show characterbashlikova at left
    b "Объясните, как здесь проявляется эмерджентность, если убрать один узел?"
    hide characterbashlikova 

    show hero at left
    h "Система потеряет устойчивость"
    hide hero 

    show characterbashlikova at left
    b "Верно. Но не учли альтернативные пути. Четвёрка"
    hide characterbashlikova 

    "Ты выходишь из аудитории. В коридоре Настя бросается к тебе"

    scene koridor:
        xysize (1980, 1080)
    play music "university.mp3" fadeout 2.0 fadein 3.0

    show characternasty at left
    n "Ну как?! Она тебя съела?"
    hide characternasty 

    show characterartem at left
    a "Если «неуд», я тебе пиво ставлю. Если «пять» — ты мне"
    hide characterartem 

    "Лиза молча протягивает тебе шоколадку. Её взгляд говорит: «Я знаю, что ты ответил»."

    jump end_of_story

label finish2sh:
    scene office:
        xysize (1980, 1080)
    play music "office.mp3" fadeout 2.0 fadein 3.0

    "Внезапно дверь приоткрывается. Это Артём суёт голову в аудиторию и шепчет"

    show characterartem at left
    a "Эй, Настя передала… — он бросает смятый листок."
    hide characterartem

    menu shpora:
            "Использовать шпаргалку?"
            "Поднять шпаргалку":
                "Ты разворачиваешь её: «Формулы по графам». Но Башлыкова уже встаёт со стула."

                show characterbashlikova at left
                b "Милостивый государь, вы что, решили проверить мою внимательность?"
                hide characterbashlikova 

                jump finish2

            "Поднять шпаргалку":
                "Ты делаешь вид, что не заметил. Артём исчезает, а ты замечаешь, как уголок губ Башлыковой дрогнул — то ли усмешка, то ли раздражение."

                jump finish2

label finish2:
    
    scene black:
        xysize (1980, 1080)
    "Проходит 15 минут. Ты рассказиываеь, что знаешь на эту."

    scene office:
        xysize (1980, 1080)
    play music "office.mp3" fadeout 2.0 fadein 3.0

    show characterbashlikova at left
    b "Дополнительный вопрос"
    hide characterbashlikova 

    "Она берёт учебник и тычет пальцем в схему."

    show characterbashlikova at left
    b "Объясните, как здесь проявляется эмерджентность, если убрать один узел?"
    hide characterbashlikova 
    
    show hero at left
    h "Э-э… Наверное, всё рухнет"
    hide hero 

    show characterbashlikova at left
    b "Наверное» — любимое слово дилетантов. Садитесь."
    b "Пересдача в среду"
    hide characterbashlikova 

    "Ты выходишь из аудитории. В коридоре Настя бросается к тебе"

    scene koridor:
        xysize (1980, 1080)
    play music "university.mp3" fadeout 2.0 fadein 3.0

    show characternasty at left
    n "Ну как?! Она тебя съела?"
    hide characternasty 

    show characterartem at left
    a "Если «неуд», я тебе пиво ставлю. Если «пять» — ты мне"
    hide characterartem

    "Ты сжимаешь зачётку с жирным «неуд»." 
    "Из чата группы уже летит мем: «Добро пожаловать в клуб мойщиков досок». Лёха хлопает тебя по плечу"

    show characterleha at left
    l "Не грусти. В сентябре отмоешься."
    hide characterleha 

    jump end_of_story

label finish3:
    scene office:
        xysize (1980, 1080)
    play music "office.mp3" fadeout 2.0 fadein 3.0

    show hero at left
    h "Эмерджентность в теории систем. Связь с теорией графов. Примеры из реальных кейсов"
    v "Черт, я же пропустил статьи…"
    hide hero

    scene black:
        xysize (1980, 1080)
    "Проходит 15 минут. Ты рассказиываеь, что знаешь на эту."

    scene office:
        xysize (1980, 1080)
    play music "office.mp3" fadeout 2.0 fadein 3.0

    show characterbashlikova at left
    b "Дополнительный вопрос"
    hide characterbashlikova 

    "Она берёт учебник и тычет пальцем в схему."

    show characterbashlikova at left
    b "Объясните, как здесь проявляется эмерджентность, если убрать один узел?"
    hide characterbashlikova 
    
    show hero at left
    h "Это зависит от типа связей"
    hide hero 

    show characterbashlikova at left
    b "..."
    b "Пять. Не ожидала"
    hide characterbashlikova 

    "Ты выходишь из аудитории. В коридоре Настя бросается к тебе"

    scene koridor:
        xysize (1980, 1080)
    play music "university.mp3" fadeout 2.0 fadein 3.0

    show characternasty at left
    n "Ну как?! Она тебя съела?"
    hide characternasty 

    show characterartem at left
    a "Если «неуд», я тебе пиво ставлю. Если «пять» — ты мне"
    hide characterartem

    "Ты смотришь на зачётку. Рядом с фамилией — аккуратная «пять». Из аудитории доносится голос Башлыковой" 
    
    show characterbashlikova at left
    b "Следующий! Не задерживайте очередь."
    hide characterbashlikova 

    "Артём хватает тебя в охапку"

    show characterartem at left
    a "Идём праздновать!"
    hide characterartem

    jump end_of_story

label end_of_story:
    return
