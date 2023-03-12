init:
    $ import time
    $ year, mounth, day, hour, minute, second, dow, doy, dst = time.localtime()

    define slowdissolve = Dissolve(1.0)
    define mediumdissolve = Dissolve(2.0)
    define fastdissolve = Dissolve(3.0)
    define circleirisout = ImageDissolve("imagedissolve circleiris.png", 1.0, 8)

    define m = Character(('[main]'), color="#ff9100")
    define e = Character(('Emilia'), color="#FF57E8")
    define d = Character(('Delphinium'), color="#8202B2" )
    define nobody = Character((' '), color="#000000")

    
label start:
    




