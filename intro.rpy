# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.



label intro:
    $ import time
    "The years go by..., times flows..."
    "But it's so unfortunate how nothing seem..."
    "changed."
    "How many times..."
    "Did I hear these words... Again and again? "
    $ time.sleep(0.5)
    "Again..."
    play music "audio/rire_femme.mp3"
    $ time.sleep(2.0)
    "Is that so..."
    stop music
    "Everything is just an eternal beginning."
    return
        

    
