
# Définition de la fonction play_once()

init python:
    
    def play_once(music):
        music_played = False
        if not music_played:
            renpy.play(music)
            music_played = True

init:
    

    $ main_inventory = []
    $ import time
    $ year,mounth,day,hour,minute,second,dow,doy,dst = time.localtime()

    define sd  = Dissolve(1.0)
    define md  = Dissolve(2.0)
    define fd = Dissolve(3.0)
    define circleirisout = ImageDissolve("imagedissolve circleiris.png", 1.0, 8)

    define m = Character(('[main]'), color="#ff9100")
    define e = Character(('Emilia'), color="#FF57E8")
    define d = Character(('Delphinium'), color="#8202B2" )
    define nobody = Character((''), color="#000000")
    define di = Character(('Director Zirou'), color="#063971")
    define u = Character(('???'), color="#3a3e798a")
    


label start:
    stop music
    call intro
    jump begin


# intro de l'histoire 
label begin:
    call arc_one_chapter_one
    return  

     




