# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label intro:
    play music "audio/Aspiration from universal_soundbank.mp3"
    "The years go by..., times flows..."
    "But it's so unfortunate how nothing seem..."
    "changed."
    "How many times..."
    "Did I hear these words... Again and again? "
    stop music
    "Again..."
    play music play_once("audio/rire_femme.mp3")
    $ time.sleep(1.0)
    "Is that so..."
    stop music
    "Everything is just an eternal beginning."
    jump opening

label opening:
    jump gender
    
label gender:
    "Before the begnning..."
    "Are you a man or a girl?"
    return
