# Определение персонажей должно быть ВНЕ label start
define e = Character('Эйлин', color="#c8ffc8")

label start:
    scene bg room
    show eileen happy
    e "Вы создали новую игру Ren'Py."
    jump minigame_test

label minigame_test:
    e "Теперь мы в мини-игре!"
    e "Кликайте чтобы заполнить шкалу!"

    $ result = renpy.call_screen("click_challenge")
    
    if result:
        e "Успех! Шкала полностью заполнена."
    else:
        e "Неудача! Не удалось удержать прогресс."
    
    jump start