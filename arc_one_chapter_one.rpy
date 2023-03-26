
label arc_one_chapter_one:
    u "Hum..."
    u "Come in!"
    u "I'm waiting for you."
    scene bg office_room_i
    play music "audio/Myuu-TenderRemains.mp3"
    di "I'm Luna Zirou. The new director."
    di "Nice to meet you."
    di "Well. Are you ready my dear new student?"
    di "I've enough waited."
    di "How are you today?"
    di "Very well, I suppose."
    di "After all, you're the first fellow to join us."
    di "I hope with all my heart you'll succeed. "
    di "It matters to me but firstly it matters to you."
    di "Trust me."
    di "But before your begin next week, we'll talk a bit."
    di "I've already seen your school career but we have yet to talk just two of us before and... I want to know who my new student is."
    di "It's normal, is it?"
    di "So it'll be easy. I'm going to ask you different questions and you'll give me your answer."
    di "Okay?"
    di "Let's start. We'll begin by the most basic."
    di "Who are you?"
    di "Tell me about yourself."
    $ m = renpy.input("What's your firstname?")
    $ m = m.strip()
    $ description_1 = "nothing"
    menu:
        "Which word most describes you?"
        "Clever":
            $ description_1 = "Clever"
            $ description_1 = description_1.strip()
            jump siu
        "Ambitious":
            $ description_1 = "Ambitious"
            $ description_1 = description_1.strip()
            jump siu
        "Coward":
            $ description_1 = "Coward"
            $ description_1 = description_1.strip()
            jump siu
        "Silly":
            $ description_1 = "Silly"
            $ description_1 = description_1.strip()
            jump siu
        "Bold":
            $ description_1 = "Bold"
            $ description_1 = description_1.strip()
            jump siu
        "Funny":
            $ description_1 = "Funny"
            $ description_1 = description_1.strip()
            jump siu
        "Peaceful":
            $ description_1 = "Peaceful"
            $ description_1 = description_1.strip()
            jump siu
    
label siu:
    m "Yeah, if you want."
    m "I'm [m] and i think that my main features of my character..."
    m "I'm [description_1]?"
    di "Hum..."
    m "That's all."
    di "What? That's short."


    return
