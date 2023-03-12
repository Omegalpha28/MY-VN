
init:  
    $ import time
    $ year,mounth,day,hour,minute,second,dow,doy,dst = time.localtime()

    define slowdissolve = Dissolve(1.0)
    define mediumdissolve = Dissolve(2.0)
    define fastdissolve = Dissolve(3.0)
    define circleirisout = ImageDissolve("imagedissolve circleiris.png", 1.0, 8)

    define n = Character(('Sus'), color="#ABB2B9")
    define no = Character((' '), color="#17202A")
    define m = Character(('[main]'), color="#1F618D")
    define inc = Character (('???'), color="#2ECC71")
    define e = Character (('Emilia'), color='#F1948A')
    
    

# Le jeu commence ici
label start:
    "Levez vous, nouveaux héros."
    "Le monde n'attend que vous."
    $ time.sleep(1)
    jump begin
  

# intro de l'histoire  
label begin:
    scene bg studyroom2
 
    
    n "..."
    n "......"
    n "........."
    show shadowguy at center
    n "Hmmm ?"
    n "Tiens donc..."
    n "Je..."
    n "Je ne m'attendais pas à vous voir ici."
    n "Je n'attendais personne d'ailleurs."
    n "Généralement les gens évitent de venir me voir."
    n "Mais...."
    n "Pas vous."
    "..."
    "......"
    "........."
    n "Allo?"
    n "Eh bien, êtes vous muet?"
    "..."
    n "Vous semblez... Un peu débousollé." 
    n "je me trompe?"
    n "Votre venue ici me laisse perplexe. Se pourrait-il que..."
    n "Cela devienne... Comment dire... "
    n "Intéréssant."
    n "Si vous êtes bien la personne à laquelle je pense..."
    n "Bref, Oubliez ce que je viens de dire. Parlons peu mais parlons bien."
    n "Que faites vous ici?"
    n "Cela ne me semble peu judicieux pour vous de venir me voir. Je vous le dis très clairement."
    n "Je me demande sincèrement si..."
    n "Vous ne seriez pas fou."
    "..."
    n "Hum oui. Ce mot vous représente bien."
    n "Ou si..."
    n "Quoique, si vous êtes ici c'est que vous avez vos propres raisons."
    n "Après tout qui suis-je vous juger."
    n "Qui suis-je..."
    n "..."
    n "Ah!"
    n "Je constate que ne me suis même pas présenté."
    n "Mon nom est..."
    "..."
    n "Non."
    n "Cela sera plus marrant de rester dans l'anonymat."
    n "Pour vous comme pour moi."
    "..."
    n "Surtout pour moi."
    n "Bref."
    n "Commençons par le commencement voulez vous bien?"
    n "Vous allez être dans la peau d'une personne assez spéciale. Je vous laisse deviner de qui cela peut bien être."
    n "Mais vous le connaissez bien, n'est ce pas?"
    n "Bon."
    n "Premièrement..."
    n "Devinons son sexe voulez vous bien?"
    $ genre_male = False
    menu:
        "Alors dis moi, Est-ce un garçon ou une fille?"
        "Je dirais que c'est un garçon.":
            $ genre_male = True
            n "..."
            n "Vous n'avez pas l'air très certain de votre choix..."    
            n "Eh bien... Bravo!"    
            n "Eh oui c'est un jeune homme."    
            n "Mais vous savez que vous n'avez pas besoin de douter quand vous connaisez déja la réponse. C'est juste un conseil que je vous donne comme ça."   
            n "Poursuivons, voulez vous bien?"
            n "Cette question c'est juste pour être certains d'être en bonne compagnie et pas avec un idiot."
            n "Comment se nomme notre jeune homme?"
            $ time.sleep(1)
            $ m = renpy.input("Entrez un nom.")
            $ m = m.strip()
            n "..."
            n "Malheureusement oui c'est bien son nom."
            n "Pas très fameux nous sommes d'accord."
            n "Bref."
            n "Vous allez l'incarner et vivre son histoire mais avec une subtilité."
            n "Vos choix auront des répercussions sur sa destiné et le sort des personne qui vous entoureront."
            n "Aucune pression."
            m "Comment ça?"
            n "Ah ben tiens. Vous l'incarnez déja. Que vous êtes jeune et encore inculte des évènement qui vont vous arriver."
            m "Mais de quoi tu parles? Et puis-je savoir tu es qui?"
            n "..."
            n "Vous verrez bien."
            m "Et votre nom?"
            n "..."
            n "Je viens de vous répondre ma parole."
            m "Absolument p..."
            n "Bref."
            n "Je ne vais pas vous retenir plus longtemps. Vous verrez par vous même de quoi je voulais parler."
            m "Attends j'ai des question à te po..."
            n "Bonne chance."
            hide shadowguy
            jump Chapitre1Garçon
        "C'est évident, c'est une fille.":
            n "..."
            n "Hmm..."
            n "Si c'était aussi évident je ne vous aurez pas posé la question car voyez vous... Vous me semblez un peu... Stupide."
            n "Mais je suis mauvaise langue et vous avez raison, c'est bien une belle jeune fille."
            n "Au moins vous avez compris que le doute n'était pas nécessaire lorsque nous conaissons la réponse "
            n "Poursuivons, voulez vous bien?"
            n "Cette question c'est juste pour être certains de ne pas être face à une personne stupide."
            n "Comment se nomme notre jeune fille?"
            $ time.sleep(1)
            $ m = renpy.input("Entrez un nom.")
            $ m = m.strip()
            n "..."
            n "C'est exact."
            n "Dix points pour le serpent que vous êtes."
            n "..."
            n "Bref."
            n "Vous allez l'incarner et vivre son histoire mais avec une subtilité."
            n "Vos choix auront des répercussions sur sa destiné et le sort des personne qui vous entoureront."
            n "Aucune pression."
            m "Comment ça?"
            n "Ah ben tiens. Vous l'incarnez déja. Que vous êtes jeune et encore inculte des évènement qui vont vous arriver."
            m "Mais de quoi tu parles? Et d'ailleurs tu es qui?"
            m "Où est-ce que je suis?"
            n "..."
            n "Vous verrez bien."
            n "Bref."
            n "Je ne vais pas vous retenir plus longtemps. Vous verrez par vous même de quoi je voulais parler."
            n "Nous nous reverrons bien assez vite, vous avez ma parole."
            m "Attends j'ai des question à te po..."
            n "Bonne chance."
            hide shadowguy
            jump Chapitre1Fille   

# Chapitre 1            

label Chapitre1Garçon:
    scene white
    with fastdissolve
    scene bg bedroom2
    with mediumdissolve
    $ time.sleep(2)
    $ savoir_ecole = False

    m "..." 
    m "(Mais...)"
    m "(Où suis-je?)"
    m "..."
    m "(Cette endroit... Elle ressemble à une chambre.)"
    m "(Elle est... bien mieux rangé que la mienne.)"
    m "Putain."
    m "(Dans quel endroit ais-je atteri? C'est quoi ce merdier?)"
    m "(Ce gars il m'a dit que... Attends c'était vraiment un mec?)"
    m "(Maintenant que j'y pense je n'ai pas vu son visage.)"
    m "(Et sa voix... je n'arrive plus à me la distinguer dans ma tête. C'est comme si il ne m'avait jamais parlé. Comme si je n'avais jamais entendu sa voix.)"
    m "(Cependant je me souviens de ses paroles.)"
    m "..."
    m "(En partie je suppose.)"
    m "(Tout ce que je me souviens c'est d'avoir répondu à des questions et qu'il me disait que...)"
    m "(Attends deux seconde.)"
    m "(Ne me dis pas que...)"
    m "..."
    m "(Je suis... Dans le corps de ce garçon?)"
    m "Allo, il y'a quelqu'un?"
    m "(Attends deux secondes. Ce n'est absolument pas ma voix.)"
    m "(Ne faisons pas de conclusions hatives le mieux ce serait de trouver un mirroir pour que je puisse me rassurer."
    m "(Il doit bien en avoir un quelque part.)"
    inc "Oui? J'arrive [m]."
    m "(Attends. Quoi???)"
    m "(Qui viens me voir?)"
    m "(Je suis mal.)" 
    $ Rencontre_Emilia = False
    menu:
        "(Que dois-je faire?)"
        "Je me cache sous le lit tel le monstre de mon enfance. Logique.":
            jump Chapitre1GarçonLit
        "Je restes immobile. Il est possible qu'il ne parle pas de moi.":
            $ Rencontre_Emilia = True
            m "(Elle n'ouvrira jamais la porte, c'est un rêve.)"
            m "(Il faut juste reste le plus calme et silencieux possible."
            m "(Calme)"
            inc "Bouh"
            m "Ahhhhhhh!"
            m "(Aie. Quel idiot je suis tombé à la renverse.)"
            jump Chapitre1GarçonImmobile
        "Je lui répond et... J'improviserai.":
            $ Rencontre_Emilia = True
            jump Chapitre1GarçonChad

label Chapitre1Fille:
    scene white
    with fastdissolve
    scene bg chambrefillemain
    with fastdissolve
    $ time.sleep(2)
    $ savoir_ecole = False
    
    m "..." 
    m "Mais..."
    m "Où suis-je?"
    m "..."
    m "Cette endroit... Elle ressemble à une chambre."
    m "J'aime bien. C'est assez spacieux."
    m "(Cependant, dans quel endroit ais-je atteri? Elle ne m'est pas familier?)"
    m "(Ce gars il m'a dit que... Attends étais-ce vraiment un homme?)" 
    m "(Maintenant que j'y pense je n'ai vu qu'une ombre.)"
    m "(Et sa voix... je n'arrive plus à me la distinguer dans ma tête. C'est comme si il ne m'avait jamais parlé. Comme si je n'avais jamais entendu sa voix.)"
    m "(Cependant je me souviens de ses paroles.)"
    m "(C'était un truc du genre...)"
    m "..."
    m "(Hum?)"
    m "(Mince alors.)"
    m "(Tout ce que je me souviens c'est d'avoir répondu à des questions et qu'il me disait que...)"
    m "(Attends deux seconde.)"
    m "(Ne me dis pas que...)"
    m "..."
    m "(Je suis...)"
    m "(ON M'AURAIT KIDNAPPÉE??????)"
    m "Allo, il y'a quelqu'un?"
    m "(Attends deux secondes. Ce n'est absolument pas ma voix.)"
    m "(C'est quoi ce délire?)"
    m "(Qu'est-ce qu'il se passe ici?)"
    inc "Oui? J'arrive [m]."
    m "(Attends. Quoi???)"
    m "(Qui viens me voir?)"
    m "(C'est pas bon du tout.)"
    m "(Attends... on dirait la voix d'un fille.)"
    m "(Non! reste sur tes gardes.)"
    m "(Elle est possiblement hostile.)"
    $ Rencontre_Emilia = False
    $ Cachette = False
    menu:
        "(Que dois-je faire?)"
        "Je cherche une cachette. N'importe quoi.":
            $ Cachette = True
            jump Chapitre1FilleLit
        "Je ne dit rien.":
            m "(J'ai peur...)"
            $ Rencontre_Emilia = True
            jump Chapitre1FilleImmobile
        "Je lui répond et... Je verrais.":
            $ Rencontre_Emilia = True
            jump Chapitre1FilleChad

label Chapitre1GarçonLit:
    m "(Go go go.)"
    m "Hop!"
    m "(Hehe, je suis introuvable.)"
    m "(Maintenant je ne fais aucun bruit...)"
    inc "[m]? Je suis là."
    m "(Qui c'est ce [m]?)"
    inc "..."
    inc "J'ai des cookies."
    m "(Tiens... Elle ne me semble plus trop hostile cette voix.)"
    inc "Ben... Il est passé où? Je l'ai bien entendu pourtant..."
    menu: 
        "(Je reste caché? Il est possible que je tombe dans un piège si je sors.)"
        "Oui, et j'ai l'air un peu con sous ce lit.":
            $ Rencontre_Emilia = True
            m "(Bon... Je sors.)"
            m "(...)"
            m "(Je ne vois personne.)"
            inc "Donc... C'est ici que tu te cachais."
            m "AHHHHHH!"
            jump Chapitre1GarçonImmobile
        "Jamais vu un piège aussi évident. Je reste ici.":
            m "(Non!)"
            m "(Je reste en position)"
            m "(Qui pourrait tomber dans un piège aussi bas.)"
            inc "..."
            inc "Ohh je vois..."
            inc "Bon je n'ai pas que cela à faire donc je m'en vais espèce d'idiot."
            m "(Ma statégie à marché.)"
            inc "Oh et une chose [m]..."
            m "..."
            inc "Quand tu sortira de ta cachette. Va prendre une douche." 
            inc "J'arrive à te sentir à des kilomètres. Poah l'odeur. Tu reviens d'une décheterie ou quoi?"
            m "(Pardon?)"
            inc "Et dépêche toi de te changer si ce n'est pas déja le cas. C'est la rentrée je te signale."
            m "..."
            m "(Elle est partie.)"
            m "(Bon je peux sortir.)"
            m "(Je suppose.)"
            m "(Tout vas bien je suis biel et bien seul.)"
            m "(Bon...)"
            m "(Que dois-je faire?)"
            m "(Elle a semblé me prendre pour quelqu'un d'autre)"
            m "(Elle a dit un nom je crois que c'était [m].)"
            m "(Cela prouve que je ne suis pas à l'endroit où je devrait être.)"
            m "..."
            m "(Quel est mon but?)"
            m "(Comment dois-je m'y prendre pour rentrer?)"
            m "..."
            m "(Je me sens faible.)"
            m "(Je crois que je vais... Dormir un instant...)"
            m "..."
            m "Non, mauvaise idée."
            m "Mieux vaut pas que je dorme maintenant. Essayons de chercher des indices sour notre situation à la place."
            m "Je crois que je vois un miroir par là-bas."
            m "Voyons voir..."
            jump Chapitre1Garçonmatin

label Chapitre1GarçonImmobile:
    show emilia school heh
    inc "Bwahahaha quel boulet."
    m "Aïe..."
    inc "[m], tu vas bien?"
    inc "Ne me dis pas que tu t'es fait mal tout de même."
    inc "Aussi solideque du verre fin."
    inc "Attends je vais t'aider à te relever."
    m "(Purée j'ai mal.)"
    m "(J'ai pas besoin de ton aide.)"
    inc "Tu as toujours besoin de mon aide ma parole."
    m "(Ben voyons.)"
    m "(Tiens mais c'est qu'elle est belle ma parole.)"
    m "Comment tu t'appelle?"
    hide emilia school heh
    show emilia school unhappy
    inc "Pardon?"
    m "Ben je demande juste à savoir ton nom."
    inc "Sérieusement?"
    m "(Je suis censé la connaître?)"
    m "(En tout cas l'inverse semble vrai.)"
    m "(Ou alors... On me joue une mauvaise blague.)"
    inc "..."
    inc "Tu vas vraiment faire semblant d'avoir oublié mon nom..."
    $ oubli_nom = False
    menu:
        m "(Je me comporte comment?)"
        "Je fais mine d'avoir oublié son nom.":
            $ oubli_nom = True
            m "Désolé."
            m "J'ai du mal à m'en souvenir."
            m "Il se peut que je me sois cogné la tête en tombant."
            inc "..."
            m "(Elle ne se laisse pas facilement avoir aparemment.)"
            m "Maintenant que j'y pense j'ai mal ouch."
            inc "Pff..."
            hide emilia school unhappy
            show emilia school angry
            inc "Je ne sais pas à quoi tu joue mais..."
            m "(Moi non plus)"
            m "(Il faut avouer que ma technique n'est de loin pas la meilleure.)"
            hide emilia school angry
            show emilia school unhappy
            inc "..."
            inc "Emilia."
            m "Hein?"
            e "Voila j'ai répondu. Tu es content?"
            jump Chapitre1GarçonImmobileSuite
        "Je lui réponds que je connais bel bien son nom.":
            m "Quoi? Mais de quoi parles-tu?"
            inc "Pardon?"
            m "Bien sûr que je connais ton nom je plaisantais."
            inc "Heureusement."
            $ answer = "Emilia"
            $ z = renpy.input("Tu t'appelles...")
            if answer == z:
                $ oubli_nom = False
                e "..."
                m "???"
                hide emilia school unhappy
                show emilia school happy
                e "Ben voila quand tu veux."
                m "(Pardon? J'avais vu juste?)"
                m "(Non elle me fait une farce ce n'est pas possible autrement. C'est comme si...)"
                m "(J'avais triché.)"
                m "(Ou un truc du genre.)"
                hide emilia school happy
                show emilia school unhappy
                jump Chapitre1GarçonImmobileSuite
            else:
                inc "..."
                hide emilia school unhappy
                show emilia school angry
                inc "Mouais."
                inc "Bref j'ai pas le temps pour tes connerie. C'est Emilia mon nom."
                hide emilia school angry 
                show emilia school unhappy
                e "C'est pas possible d'être aussi débile."
                m "Pardon?"
                e "Tu m'as très bien entendu"
                jump Chapitre1GarçonImmobileSuite

label Chapitre1GarçonImmobileSuite:
    m "(Elle s'appelle donc Emilia.)"
    e "D'ailleurs, tu voulais quelques choses?"
    e "Je ne sais pas ce qu'il t'arrive mais je vais m'en aller si tu n'a rien de plus à dire."
    m "(C'est vrai que je l'avais appelé au départ.)"
    m "Ouais en fait je parlais à moi même."
    hide emilia school unhappy
    show emilia school angry
    e "Ah... Je vois..."
    m "(Pourquoi ai-je dit cela?)"
    e "Tu n'est pas net des fois [m]."
    hide emilia school angry
    show emilia school unhappy
    e "Bon je vais dire que c'est à cause du trac."
    m "(Comment ça?)"
    m "Je ne vois pas de quoi tu parles. Et d'ailleurs où suis..."
    e "COMMENT PEUX-TU DIRE CELA?"
    m "(Mais pourquoi crie-t'elle tout d'un coup?)"
    e "Tu n'est vraiment pas net [m]."
    hide emilia school unhappy
    show emilia school heh
    e "Nous sommes quel jour aujourd'hui?"
    m "Aucune idée et cela m'importe p..."
    hide emilia school heh
    show emilia school angry
    e "TU FAIS EXPRÈS D'ÊTRE AUSSI STUPIDE OU EST-CE UN DON DE LA NATURE?"
    m "(Mais stop! Calme toi.)"
    e "..."
    e "C'est la rentrée pour toi et moi."
    e "J'ai vraiment affaire à un imbécile."
    e "Maintenant ne m'importune plus. Surtout si c'est pour si peu."
    e "Et changes toi vite ou tu vas être en retard"
    e "En ce qui me concerne je pars."
    hide emilia school angry
    m "(Elle est partie.)"
    m "..."
    m "(Que dois-je faire?)"
    m "(Quel est mon but?)"
    m "(Comment dois-je m'y prendre pour rentre chez moi?)"
    m "..."
    m "(Je me sens faible.)"
    m "(Je crois que je vais... Dormir un instant...)"
    m "..."
    m "Non, mauvaise idée."
    m "Mieux vautque je ne dorme pas maintenant. Essayons de chercher des indices sour notre situation à la place."
    m "Je crois que je vois un miroir par là-bas."
    m "Voyons voir..."
    jump Chapitre1Garçonmatin

label Chapitre1GarçonChad:
    m "Qui est là?"
    inc "Ne t'inquiètes pas c'est juste moi Emilia."
    m "(Une jeune fille entra dans la chambre.)"
    show emilia school happy
    e "Coucou [m]. Tu m'as appelé?"
    m "(Elle semble pleine de vie.)"
    m "..."
    e "Oh je vois..."
    m "(Que veux tu que je te dise aussi.)"
    m "(Je suis dans quel endroit moi.)"
    m "(Possible que tout ça ne soit qu'un simple rêve.)"
    m "(Si je me pinçait un peu...)"
    m "Ouch"
    m "(Ah ben ca n'a pas marché.)"
    e "Tu vas bien? Tu voulais faire quoi?"
    hide emilia school happy
    show emilia school unhappy
    m "Ne cherche pas je voulais seulement vérifier un truc."
    e "..."
    e "Bon si tu le dis."
    hide emilia school unhappy
    show emilia school happy
    e "Au fait tu es prêt pour partir"
    m "Partir?"
    e "Ben oui. Tu n'as pas oublié?"
    m "(Oublié quoi?)"
    m "Mais...tu es qui à la fin?"
    hide emilia school happy
    show emilia school unhappy
    e "Comment ça?"
    m "Eh bien... Où sommes nous?"
    e "..."
    e "Ben chez nous pourquoi?"
    m "(Hein!!!)"
    e "Pourquoi cette question si soudainement?"
    e "Tu vas bien?"
    m "..."
    e "Tu es vraiment étrange des fois. Bref, je ne vais pas chercher la raison. Elle doit être stupide comme d'habitude."
    e "Donc..."
    e "Revenons à nos moutons."
    hide emilia school unhappy
    show emilia school happy
    e "Alors?"
    m "Alors quoi?"
    e "Tu te sens comment?"
    m "(Mal! Je ne sais pas où je me trouve et en plus elle me sort que c'est chez nous?)"
    m "(Bref... Pour l'instant, entrons dans son jeu.)"
    m "Comme d'habitude je dirais."
    m "(C'est quoi l'origine de la question pour commencer?)"
    m "(Et plus important.)"
    m "(Qui est cette fille merde.)"
    e "Ah bon? C'est étonnant de ta part?"
    m "(Mais de quoi parle t'elle à la fin bordel.)"
    m "En quoi?"
    hide emilia school happy
    show emilia school noice
    e "Eh bien... C'est rare de te voir aussi calme le jour d'une rentrée voila tout."
    m "(Une rentrée?)"
    m "Je ne comprends pas tout."
    m "(C'est un euphémisme.)"
    e "C'est juste mon impression rien de plus."
    m "On peut revenir au moment..."
    hide emilia school noice
    show emilia school happy
    e "Tu vois des fois tu peux être disons... éxcité."
    m "(M'as t'elle entendu?)"
    m "C'est à dire?"
    hide emilia school happy
    show emilia school shy
    e "..."
    e "Oublie ce que je viens de dire."
    hide emilia school shy
    show emilia school unhappy
    e "Pourquoi suis-je ici au final?"
    m "C'est toi qui es venue."
    e "Et c'est toi qui m'a appelé."
    m "(C'est pas comme si je l'avais invoqué non plus.)"
    m "Ouais tu as raison."
    m "Désolé du dérangement."
    hide emilia school unhappy
    show emilia school shy
    e "..."
    $ time.sleep(1)
    e "Ne t'inquètes pas tu ne m'as pas dérangé plus que cela. Je ne fesais rien de toute façon."
    e "..."
    m "..."
    e "..."
    m "(Elle est calme tout d'un coup?)"
    m "Dis j'aurais une question. Je suis où plus sérieusement?"
    e "..."
    e "......"
    e "........."
    m "Allo?"
    hide emilia school shy
    show emilia school unhappy
    e "Tu disais?"
    m "(Houla c'était quoi ça?)"
    m "(Il vient de se passer quoi là?)"
    m "..."
    m "Je t'ai posé une question et puis..."
    e "Ah. Je n'ai plus trop la tête à ça, je crois que je vais plutôt retourner me préparer pour partir."
    e "..."
    m "(Elle semble soucieuse de quelque chose.)"
    $ Emilia_soucis = False
    menu:
        "j'essaie de savoir ce qu'il se passe?"
        "Oui":
            $ Emilia_soucis = True
            m "Quelque chose ne vas pas?"
            hide emilia school unhappy
            show emilia school shy
            e "Hein?"
            e "Non rien c'est juste que..."
            e "Je n'arrive pas à réfléchir correctement c'est tout." 
            e "Je pense à tout ce qu'il peut arriver."
            m "C'est à dire?"
            e "Eh bien..."
            e "Tu sais nous sommes amis toi et moi."
            m "(Première nouvelle.)"
            e "Et on se connait depuis toujours."
            m "(Non.)"
            e "Et on est toujours resté ensemble"
            m "(Absolument pas.)"
            e "Mais cette fois-ci..."
            e "On risque d'être séparé."
            e "Et..."
            e "Bref! Disons que je dois me préparer à cela."
            e "De plus..."
            m "Oui?"
            e "Eh bien... Tu sais..."
            e "Je suis..."
            e "..."
            m "(...Batman?)"
            m "(Un vampire, un troll des montagnes, une tueuse en série?)"
            m "Oui?"
            hide emilia school shy
            show emilia school happy
            e "Non. Oublie ce que je viens de dire."
            e "Tu n'as pas besoin de savoir cela."
            m "(QUOI???)"
            m "(Parle bordel tu m'intéresse.)"
            m "Tu peux parler sans crainte."
            hide emilia school happy
            show emilia school unhappy
            e "Enfin..."
            m "Oui?"
            m "(On est presque au but.)"
            e "Je devrais aller me reposer. C'est plus judicieux."
            m "(MAIS C'EST PAS VRAI!)"
            m "Non!"
            hide emilia school unhappy
            show emilia school angry
            e "Pardon?"
            e "Ah oui c'est vrai on doit bientôt partir."
            m "(Hein quoi?)"
            m "Pour aller où?"
            hide emilia school angry
            show emilia school happy
            e "Ha! Tu n'arrête donc jamais tes idioties."
            e "Enfin cette fois ci cela aura eu le mérite de me faire rire."
            m "..."
            m "Je suppose?"
            hide emilia school happy
            show emilia school noice
            e "Au final, je pense que je vais partir plus tôt. Tu peux m'accompagner si tu le souhaite."
            e "Quand tu sera prêt, j'aimerai que tu me retrouve au parc au coin de la rue puis on ira ensemble au lycée."
            $ rdv_avec_Emilia1 = False
            menu:
                "Alors?"
                "D'accord":
                    $ rdv_avec_Emilia1 = True
                    e "Comme quoi tu es vraiment étrange. Depuis quand tu accepte ce genre de choses. Tu as changé un peu."
                    m "(Je suis juste perdu.)"
                    m "(J'ai besoin de récolter le plus d'informations possible. J'ai pas pu vraiment l'interroger mais c'est peut-être mon seul moyens d'avoir des informations.)"
                    m "Ah bon?"
                    m "Ben écoute je me sens comme un homme nouveau actuellement."
                    m "Voila tout."
                    hide emilia school noice
                    show emilia school happy
                    e "Ha!"
                    e "Un homme nouveau dit-il."
                    e "Après vu comment tu semble avoir changé ça me donne envie de connaître ton secret."
                    e "Bon, je t'attendrais là-bas! Tu as intérêt à ne pas être en retard hihi."
                    m "(Cela l'a mise de bonne humeur aparemment.)"
                    m "D'accord, je ferais de mon mieux."
                    m "Mais... Tu peux m'expliquer à quel endroit on va aller au final?"
                    e "Ben je te l'ai déja dit."
                    e "Faut suivre un peu."
                    m "..."
                    m "Ouch"
                    m "(Elle vient de me donner un gros coup dans le dos.)"
                    m "(Ça fait un mal de chien.)"
                    e "Bon je te laisse [m]."
                    e "À plus hihi."
                    m "(J'ai mal. Elles sont fait en quoi ses main? En métal?)"
                    m "Ouais c'est ça..."
                    hide emilia school happy
                    m "(Elle est partie...)"
                    m "..."
                    m "(Je ne comprends pas tout.)"
                    m "(Qui est-ce ce [m]?)."
                    m "..."
                    m "(Est-ce possible que ce soit moi?)"
                    m "(Non, impossible.)"
                    m "..."
                    m "(Faites que tout cela ne soit qu'un rêve...)"
                    m "(J'aurais surement mes réponse au parc.)"
                    m "(Restons calme pour l'instant.)"
                    m "Calme..."
                    m "(Comment dois-je m'y prendre pour rentrer?)"
                    m "(Je me sens faible.)"
                    m "(Je crois que je vais... Dormir un instant...)"
                    m "Hum..."
                    m "Non, mauvaise idée."
                    m "Mieux vaut pas que je dorme maintenant. Essayons de chercher des indices sour notre situation à la place."
                    m "Je crois que je vois un miroir par là-bas."
                    m "Voyons voir..."
                    jump Chapitre1Garçonmatin
                "Non, j'ai la flemme.":
                    hide emilia school noice
                    show emilia school unhappy
                    e "Ah."
                    e "Bon c'est toi qui décide."
                    e "Tu as intérêt à ne pas être en retard."
                    e "Sinon tu auras affaire à moi."
                    m "Et ma question alors?"
                    e "C'était sympa d'avoir pu discuter un peu avec toi même si tu est étrange aujourd'hui."
                    m "..."
                    m "Tu le fais exprès de ne pas répondre?"
                    hide emilia school unhappy
                    show emilia school happy
                    e "En effet."
                    e "Bref je vais te laisser. Salut [m]."
                    m "..."
                    m "Mais..."
                    m "NON! Tu dois d'abord répondre à mes questions."
                    hide emilia school happy
                    show emilia school angry  
                    e "Pourquoi es-tu aussi aigri aujourd'hui [m]?"
                    e "On doit aller au lycée."
                    e "Logique non?"
                    m "Et c'est à quel endroit?"
                    e "..."
                    e "Tu me fatigues."
                    e "Comment ça tu ne sais pas te rendre là-bas?"
                    e "Tu le fais exprès, avoue-le."
                    m "Hein? Bien sûr que non."
                    hide emilia school angry
                    show emilia school unhappy
                    e "Demande à Delphi, elle saura t'emmener là-bas."   
                    m "Qui?"
                    e "..."
                    e "J'abandonne."      
                    e "Salut."
                    hide emilia school unhappy 
                    m "Non attends!" 
                    m "(Elle est partie.)"
                    m "(Purée mais que dois-je faire?)"
                    m "(Comment dois-je m'y prendre pour rentrer chez moi?)"
                    m "..."
                    m "(Je me sens faible.)"
                    m "(Je crois que je vais... Dormir un instant...)"
                    m "..."
                    m "Non, mauvaise idée."
                    m "Mieux vaut pas que je dorme maintenant. Essayons de chercher des indices sour notre situation à la place."
                    m "Je crois que je vois un miroir par là-bas."
                    m "Voyons voir..."
                    jump Chapitre1Garçonmatin
        "Nope":
            e "..."
            e "Bon... J'y vais."
            m "Attends, pour aller à quel endroit?"
            e "Sérieusement?"
            e "Ben devine."
            m "Comment?"
            m "(Et comment je fais...)"
            e "..."
            $ endroit_fail = False 
            jump endroit 

label endroit:                   
    menu:
        "(De quel endoit parle t'elle?)"
        "D'un centre commercial":
            m "On doit aller dans un centre commerciale."
            e "Pardon?"
            m "Ce n'est pas ça?"
            e "Je vais faire comme si je n'avais rien entendu."
            hide emilia school unhappy
            show emilia school angry
            m "Et son nom, tu ne l'aurais pas oublié non plus...."
            e "À force de t'entendre..."
            e "J'ai l'impression de régresser intellectuellement."
            m "Ben merci."
            hide emilia school angry
            show emilia school unhappy
            e "..."
            e "Et son nom?"
            m "Je te demande pardon?"
            e "Tu m'as très bien entendu"
        "D'une église":
            $ endroit_fail = True
            m "On doit aller dans une église, je présume."
            e "..."
            e "C'est ça."
            m "Ah bon?"
            hide emilia school unhappy
            show emilia school angry
            e "Bien sûr que non!"
            e "Je vais faire comme si je n'avais rien entendu."
            hide emilia school angry
            show emilia school unhappy
            m "..."
            hide emilia school unhappy
            show emilia school angry
            m "Et son nom, tu ne l'aurais pas oublié non plus...."
            e "À force de t'entendre..."
            e "J'ai l'impression de régresser intellectuellement."
            m "Ben merci."
            hide emilia school angry
            show emilia school unhappy
            e "..."
            e "Et son nom?"
            m "Je te demande pardon?"
            e "Tu m'as très bien entendu"
        "Un lycée":
            m "Dans un lycée, c'est logique."
            e "..."
            e "Ben oui."
            m "(Je suis trop forte.)"
            hide emilia school unhappy
            show emilia school happy
            e "Comme quoi tu sais au moins ou on doit aller."
            m "Bien entendu."
            e "Et son nom?"
            m "Je te demande pardon?"
            e "Je parle du lycée."
    menu:
        "C'est quoi le nom du lycée?"
        "L'académie du pic de l'espoir.":
            $ savoir_ecole = True
            e "..."
            hide emilia school happy
            show emilia school unhappy
            e "Tu t'es cru dans Danganronpa ma parole..."
            e "C'est pas ça du tout."
            e "C'est le lycée Archipel."
            e "Je préfère que tu me dise que tu en as aucune idée que de me sortir des conneries pareils la prochaine fois."
        "Le lycée Kouo.":
            $ savoir_ecole = True
            hide emilia school happy
            show emilia school unhappy
            e "..."
            e "Mais..."
            e "Pourquoi?"
            m "Ben quoi?"
            e "Non c'est pas ça du tout."
            e "C'est le lycée Archipel."
            e "Je préfère que tu me dise que tu en as aucune idée que de me sortir des conneries pareils la prochaine fois."
        "C'est le lycée Meishu.":
            $ savoir_ecole = True
            e "..."
            e "Tu voudrais bien. Certains profs ont l'air sympa."
            e "Mais non. Ce n'est pas cela."
            e "C'est le lycée Archipel."
            e "Je préfère que tu me dise que tu en as aucune idée que de me sortir des conneries pareils la prochaine fois."
        "Je ne sais pas":
            $ savoir_ecole = True
            e "..."
            hide emilia school unhappy
            show emilia school happy
            e "Enfin une réponse sincère."
            e "C'est le lycée Archipel son nom."
            e "Je pensais que tu le savais."
            hide emilia school happy
            show emilia school unhappy
    hide emilia school unhappy
    show emilia school happy
    e "Je te laisse, salut [m]."
    m "Atends..."
    hide emilia school happy 
    m "Non attends!" 
    m "(Elle est partie.)"
    m "(Purée mais que dois-je faire?)"
    m "(Comment dois-je m'y prendre pour rentrer chez moi?)"
    m "..."
    m "(Je me sens faible.)"
    m "(Je crois que je vais... Dormir un instant...)"
    m "..."
    m "Non, mauvaise idée."
    m "Mieux vaut pas que je dorme maintenant. Essayons de chercher des indices sour notre situation à la place."
    m "Je crois que je vois un miroir par là-bas."
    m "Voyons voir..."
    jump Chapitre1Garçonmatin
           
label Chapitre1FilleLit:
    m "(Alors...)"
    m "(Si je me cache dans cette armoire...)"
    m "(On ne me trouvera pas.)"
    m "..."
    m "(Hehe, je suis introuvable.)"
    m "(Maintenant je ne fais aucun bruit...)"
    inc "[m]? Je suis là."
    m "(J'entends quelqu'un.)"
    inc "Ben... Elle est passé où? Je l'ai bien entendu pourtant..."
    m "..."
    m"(C'est la voix d'une fille.)"
    inc "..."
    inc "..."
    inc "Ohh je vois..."
    inc "Tu veux jouer."
    m "Absolument pas. Casse toi."
    inc "Tu sais que à ce ryhme on va être en retard."
    inc "Je ne sais pas pourquoi tu m'as appelé mais la prochaine fois, trouve un autre cachette que l'armoire."
    m "(Ah!)"
    m "(ma statégie n'a pas marché.)"
    inc "Ciao [m]. Oh et une chose..."
    m "..."
    inc "Tu sais que tu n'a jamais été très bonne pour me berner." 
    inc "Dépêche toi de te changer nous allons être en retard par ta faute à ce rythme."
    inc "Enfin..."
    inc "Je pense que je vais partir plus tôt donc bouge toi."
    m "(Pardon?)"
    inc "Pas envie d'être en retard le jour de la rentrée."
    m "..."
    m "(Elle est partie.)"
    m "..."
    m "(C'est qui ce [m]?)"
    m "(Ce nom me dit quelque chose...)"
    m "(Mais impossible de savoir quoi.)"
    m "(En tout cas, elle a du me prendre pour elle.)"
    m "(Bon... Où suis-je tombé?)"
    m "(Que dois-je faire?)"
    m "(Quel est mon but?)"
    m "(Comment dois-je m'y prendre pour rentrer?)"
    m "..."
    m "(Je me sens faible.)"
    m "(Je crois que je vais... Dormir un instant...)"
    m "..."
    m "Non, mauvaise idée."
    m "Mieux vaut pas que je dorme maintenant. Essayons de chercher des indices sour notre situation à la place."
    m "Je crois que je vois un miroir par là-bas."
    m "Voyons voir..."
    jump Chapitre1Fillematin

label Chapitre1FilleImmobile:
    m "..."
    m "(Bon...)"
    m "(Essayons de garder son calme.)"
    m "(Je n'ai pas entendu mon nom cela veut donc dire que ce n'est pas moi qui est appelé.)"
    m "(Calme)"
    inc "Bouh"
    m "Ahhhhhhh!"
    m "(Aie. Quelle idiote. Je suis tombée à la renverse.)"
    inc "Hihi, bien joué."
    show emilia school happy
    inc "[m], tu vas bien?"
    inc "Ne me dis pas que tu t'es fait mal tout de même."
    m "(Quelle gentilesse de sa part.)"
    inc "Même un vase en verre fin est plus solide que toi."
    m "..."
    inc "Attends deux secondes."
    inc "Je vais t'aider."
    m "(Purée j'ai mal.)"
    m "Je vais bien"
    inc "bien sûr."
    inc "Cela se voit à ta réaction quelque peu disproportionné."
    m "(Mais c'est elle qui est venu par derrière m'effrayer.)"
    m "(Tiens, je n'ai pas l'impression qu'elle soit une vraie menace vu de plus près.)"
    m "Comment tu t'appelle?"
    hide emilia school happy
    show emilia school unhappy
    inc "Pardon?"
    m "Ben je demande juste à savoir ton nom."
    hide emilia school unhappy
    show emilia school angry
    inc "Tu n'est pas sérieuse?"
    inc "[m] est-tu sûr que tout vas bien?"
    m "Pardon? [m]?"
    inc "Ben oui, toi."
    m "(Merde attends elle doit me prendre pour cette [m].)"
    m "(Mais elle doit bien voir que je suis une autre personne non?)"
    m "(Quoique il est possible que je suis en train de tomber dans un piège.)"
    m "(Une mauvaise blague sûrement.)"
    m "(Donc... Comment pourrais-je réagir?)"
    inc "[m]?"
    inc "Dis tu m'écoute?"
    m "Oui bien sûr."
    m "(Que faire?)"
    $ oubli_nom = False
    menu:
        m "(Je dois trouver un moyen de m'en sortir.)"
        "Je fais mine d'avoir oublié son nom.":
            $ oubli_nom = True
            m "Désolé."
            m "J'ai du mal à m'en souvenir."
            m "Il se peut que je me sois cogné la tête en tombant."
            m "La faute à qui?"
            hide emilia school angry
            show emilia school unhappy
            inc "..."
            m "Maintenant que j'y pense."
            m "J'ai mal ouch."
            inc "Pff..."
            inc "À d'autres [m]."
            hide emilia school unhappy
            show emilia school angry
            inc "Je ne sais pas à quoi tu joue mais on dirait seulement une idiote."
            inc "Et cela me te ressemble pas."
            m "..."
            m "En quoi?"
            inc "..."
            inc "Qu'importes."
            hide emilia school angry
            show emilia school unhappy
            inc "Emilia."
            m "Hein?"
            e "Voila j'ai répondu. Tu es contente?"
            jump Chapitre1FilleImmobileSuite
        "J'essaie de faire semblant de m'en souvenir.":
            $ oubli_nom = True
            m "Bien sûr que je connais ton nom."
            inc "Heureusement."
            inc "Le plus drôle c'est que tu puisse oublier ton propre nom."
            m "..."
            m "Bien sûr que non."
            m "Cela serait totalement stupide de ma part."
            m "Mon nom c'est [m]."
            m "Et toi, tu es..."
            inc "Perdue."
            m "Certes."
            m "Mais surtout..."
            $ answer = "Emilia"
            $ z = renpy.input("Ton nom c'est...")
            if answer == z:
                $ oubli_nom = False
                e "..."
                m "???"
                hide emilia school unhappy
                show emilia school happy
                e "Ben voila quand tu veux."
                m "(Pardon? J'avais vu juste?)"
                m "(Non elle me fait une farce ce n'est pas possible autrement. C'est comme si...)"
                m "(J'avais triché.)"
                m "(Ou un truc du genre.)"
                hide emilia school happy
                show emilia school unhappy
                jump Chapitre1GarçonImmobileSuite
            else:
                inc "..."
                hide emilia school unhappy
                show emilia school angry
                inc "Mouais."
                inc "Bref j'ai pas le temps pour tes connerie. C'est Emilia mon nom."
                m "(Ah.)"
                m "(Ben comment aurais-je pu le savoir moi?)"
                hide emilia school angry 
                show emilia school unhappy
                e "C'est pas possible d'être aussi débile."
                m "Pardon?"
                e "Tu m'as très bien entendu"
                jump Chapitre1GarçonImmobileSuite

label Chapitre1FilleImmobileSuite:
    m "(Elle s'appelle donc Emilia.)"
    hide emilia school unhappy
    show emilia school noice
    e "Bon... Pourquoi m'as tu appelé d'ailleurs?"
    m "(C'est vrai que je l'avais appelé au départ.)"
    m "Ouais en fait je parlais à moi même."
    hide emilia school noice
    show emilia school shy
    e "Ah... Je vois..."
    m "(Pourquoi ai-je dit cela?)"
    hide emilia school shy
    show emilia school unhappy
    e "Tu n'est pas net des fois [m]."
    e "Bon on va dire que c'est à cause du trac."
    m "(Comment ça?)"
    m "Il se passe quoi?"
    e "Tu n'est vraiment pas net [m]."
    e "Dis moi pas que tu as oublié."
    m "je pense que si malheureusement."
    e "..."
    e "Eh bien c'est la rentrée pour toi et moi."
    e "..."
    e "Bref."
    e "Maintenant ne m'importune plus. Surtout si c'est pour si peu. Bonne nuit."
    hide emilia school unhappy
    m "(Elle est partie.)"
    m "..."
    m "(Je ne comprends pas tout.)"
    m "(Qui est-ce ce [m]?)."
    m "..."
    m "(Est-ce possible que ce soit moi?)"
    m "(Non, impossible.)"
    m "..."
    m "(Faites que tout cela ne soit qu'un rêve...)"
    m "(Restons calme pour l'instant.)"
    m "Calme..."
    m "(Comment dois-je m'y prendre pour rentrer?)"
    m "(Je me sens faible.)"
    m "(Je crois que je vais... Dormir un instant...)"
    m "Hum..."
    m "Non, mauvaise idée."
    m "Mieux vaut pas que je dorme maintenant. Essayons de chercher des indices sour notre situation à la place."
    m "Je crois que je vois un miroir par là-bas."
    m "Voyons voir..."
    jump Chapitre1Fillematin
    
label Chapitre1FilleChad:
    m "Qui est là?"
    inc "Ne t'inquiètes pas c'est juste moi Emilia."
    show emilia school happy
    e "Coucou [m]. Tu m'as appelée?"
    m "(Elle semble pleine de vie.)"
    m "(Attends elle vient de m'appeler comment?)"
    m "Heu..."
    m "Non, disons que je parlais à moi même."
    e "Oh je vois..."
    m "(C'est moi ou elle semble déçu? Après il est vrai que j'ai du la déranger.)"
    m "(Le truc qui me fait peur c'est qu'elle vient de m'appeler [m].)"
    m "(Elle doit me prendre pour quelqu'un d'autre.)"
    m "(Maintenant que j'y pense.)"
    m "(Il est possible que si je me pince, tout cela s'arrête.)"
    m "(Cela ne coûte rien d'essayer.)"
    m "Ouch"
    m "(Ah ben ca n'a pas marché.)"
    e "Tu vas bien? Tu voulais faire quoi?"
    m "Ne cherche pas... Je voulais seulement vérifier quelque chose."
    e "..."
    hide emilia school happy
    show emilia school noice
    e "Bon si tu le dis."
    e "Au fait, es tu prête pour partir?"
    m "Pour quoi?"
    e "Ben, pour partir quoi. Tu n'as pas oublié j'espère?"
    m "Il se passe quoi?"
    e "Eh bien..."
    hide emilia school noice
    show emilia school happy
    e "J'ai compris."
    e "J'avoue que ma question était un peu idiote."
    m "(Mais de quoi tu parles?)"
    e "Alors?"
    m "Alors quoi?"
    e "Tu te sens comment?"
    m "(Perdu. Je suis où pour commencer?)"
    m "(Je vais rentrer dans son jeu pour l'instant.)"
    m "Comme d'habitude je suppose."
    m "(Je parles comme si je la conaissais depuis lontemps.)"
    m "(Mais qui est cette fille plus sérieusement?)"
    e "Ah bon? C'est étonnant de ta part?"
    m "En quoi?"
    e "Eh bien... C'est rare de te voir aussi calme le jour d'une rentrée."
    e "Enfin je dis cela mais il est possible que ce soit tout l'inverse et que je me fasse de fausses idées."
    m "..."
    m "On va dire que c'est ça. Mais plus sérieusement, où suis..."
    e "D'ailleurs, pourquoi suis-je ici?"
    m "(Hein?)"
    m "Pardon?"
    e "Eh bien tu m'as appelé pour une certaine raison n'est-ce pas?"
    m "Laisse moi finir mes phrase."
    hide emilia school happy
    show emilia school unhappy
    e "Comment ça?"
    m "Eh bien..."
    e "Bref."
    hide emilia school unhappy
    show emilia school happy
    e "Tu n'a pas répondu à ma question je te signale."
    e "Pourquoi m'as tu appelé?"
    m "(Mais je ne t'ai pas appelé bordel.)"
    m "C'est toi qui es venue."
    hide emilia school happy
    show emilia school unhappy
    e "Et c'est toi qui m'a appelé."
    m "(Mais... Elle le fait exprès!)"
    m "(C'est pas comme si je l'avais invoqué non plus.)"
    m "Si tu veux."
    m "Désolé du dérangement."
    e "..."
    m "(Elle est pas net du tout elle)."
    hide emilia school unhappy
    show emilia school shy
    e "Ne t'inquètes pas tu ne m'as pas dérangé plus que cela. Je ne fesais rien de toute façon."
    e "..."
    m "(Elle semble soucieuse de quelque chose.)"
    $ Emilia_soucis = False
    menu:
        "j'essaie de savoir ce qu'il se passe?"
        "Oui":
            $ Emilia_soucis = True
            m "Quelque chose ne vas pas?"
            hide emilia school unhappy
            show emilia school shy
            e "Hein?"
            e "Non rien c'est juste que..."
            e "Je n'arrive pas à réfléchir correctement c'est tout." 
            e "Je pense à tout ce qu'il peut arriver."
            m "C'est à dire?"
            e "Eh bien..."
            e "Tu sais nous sommes amis toi et moi."
            m "(Première nouvelle.)"
            e "Et on se connait depuis toujours."
            m "(Non.)"
            e "Et on est toujours resté ensemble"
            m "(Absolument pas.)"
            e "Mais cette fois-ci..."
            e "On risque d'être séparé."
            e "Et..."
            e "Bref! Disons que je dois me préparer à cela."
            e "De plus..."
            m "Oui?"
            e "Eh bien... Tu sais..."
            e "Je suis..."
            e "..."
            m "(...Batman?)"
            m "(Un vampire, un troll des montagnes, une tueuse en série?)"
            m "Oui?"
            hide emilia school shy
            show emilia school happy
            e "Non. Oublie ce que je viens de dire."
            e "Tu n'as pas besoin de savoir cela."
            m "(QUOI???)"
            m "(Parle bordel tu m'intéresse.)"
            m "Tu peux parler sans crainte."
            hide emilia school happy
            show emilia school unhappy
            e "Enfin..."
            m "Oui?"
            m "(On est presque au but.)"
            e "Je devrais aller me reposer. C'est plus judicieux."
            m "(MAIS C'EST PAS VRAI!)"
            m "Non!"
            hide emilia school unhappy
            show emilia school angry
            e "Pardon?"
            e "Ah oui c'est vrai, on doit bientôt partir."
            m "(Hein quoi?)"
            m "Pour aller où?"
            hide emilia school angry
            show emilia school happy
            e "Ha! Tu n'arrête donc jamais tes idioties."
            e "Enfin cette fois ci cela aura eu le mérite de me faire rire."
            m "..."
            m "Je suppose?"
            hide emilia school happy
            show emilia school noice
            e "Au final, je pense que je vais partir plus tôt. Tu peux m'accompagner si tu le souhaite."
            e "Quand tu sera prêt, j'aimerai que tu me retrouve au parc au coin de la rue puis on ira ensemble au lycée."
            $ rdv_avec_Emilia1 = False
            menu:
                "Alors?"
                "D'accord":
                    $ rdv_avec_Emilia1 = True
                    e "Comme quoi tu es vraiment étrange. Depuis quand tu accepte ce genre de choses. Tu as changé un peu."
                    m "(Je suis juste perdu.)"
                    m "(J'ai besoin de récolter le plus d'informations possible. J'ai pas pu vraiment l'interroger mais c'est peut-être mon seul moyens d'avoir des informations.)"
                    m "Ah bon?"
                    m "Ben écoute je me sens comme une nouvelle personne actuellement."
                    m "Voila tout."
                    hide emilia school noice
                    show emilia school happy
                    e "Ha!"
                    e "Bien sûr."
                    e "Bon, je t'attendrais là-bas! Tu as intérêt à ne pas être en retard hihi."
                    m "(Cela l'a mise de bonne humeur aparemment.)"
                    m "D'accord, je ferais de mon mieux."
                    m "Mais... Tu peux m'expliquer à quel endroit on va aller au final?"
                    e "Ben je te l'ai déja dit."
                    e "Faut suivre un peu."
                    m "..."
                    m "Ouch"
                    m "(Elle vient de me donner un gros coup dans le dos.)"
                    m "(Ça fait un mal de chien.)"
                    e "Bon je te laisse [m]."
                    e "À plus hihi."
                    m "(J'ai mal. Elles sont fait en quoi ses main? En métal?)"
                    m "Ouais c'est ça..."
                    hide emilia school happy
                    m "(Elle est partie...)"
                    m "..."
                    m "(Je ne comprends pas tout.)"
                    m "(Qui est-ce ce [m]?)."
                    m "..."
                    m "(Est-ce possible que ce soit moi?)"
                    m "(Non, impossible.)"
                    m "..."
                    m "(Faites que tout cela ne soit qu'un rêve...)"
                    m "(J'aurais surement mes réponse au parc.)"
                    m "(Restons calme pour l'instant.)"
                    m "Calme..."
                    m "(Comment dois-je m'y prendre pour rentrer?)"
                    m "(Je me sens faible.)"
                    m "(Je crois que je vais... Dormir un instant...)"
                    m "Hum..."
                    m "Non, mauvaise idée."
                    m "Mieux vaut pas que je dorme maintenant. Essayons de chercher des indices sour notre situation à la place."
                    m "Je crois que je vois un miroir par là-bas."
                    m "Voyons voir..."
                    jump Chapitre1Fillematin
                "Non, j'ai la flemme.":
                    hide emilia school noice
                    show emilia school unhappy
                    e "Ah."
                    e "Bon c'est toi qui décide."
                    e "Tu as intérêt à ne pas être en retard."
                    e "Sinon tu auras affaire à moi."
                    m "Et ma question alors?"
                    e "C'était sympa d'avoir pu discuter un peu avec toi même si tu est étrange aujourd'hui."
                    m "..."
                    m "Tu le fais exprès de ne pas répondre?"
                    hide emilia school unhappy
                    show emilia school happy
                    e "En effet."
                    e "Bref je vais te laisser. Salut [m]."
                    m "..."
                    m "Mais..."
                    m "NON! Tu dois d'abord répondre à mes questions."
                    hide emilia school happy
                    show emilia school angry  
                    e "Pourquoi es-tu aussi énervée aujourd'hui [m]?"
                    e "On doit aller au lycée."
                    e "Logique non?"
                    m "Et c'est à quel endroit?"
                    e "..."
                    e "Tu me fatigues."
                    e "À ton avis?"
                    m "..."
                    e "Comment ça? Tu ne sais pas te rendre là-bas?"
                    e "Tu le fais exprès."
                    m "Hein? Bien sûr que non."
                    hide emilia school angry
                    show emilia school unhappy
                    e "Demande à Delphi, elle saura t'emmener là-bas."   
                    m "Qui?"
                    e "..."
                    e "J'abandonne."      
                    e "Salut."
                    hide emilia school unhappy 
                    m "Non attends!" 
                    m "(Elle est partie.)"
                    m "(Purée mais que dois-je faire?)"
                    m "(Comment dois-je m'y prendre pour rentrer chez moi?)"
                    m "..."
                    m "(Je me sens faible.)"
                    m "(Je crois que je vais... Dormir un instant...)"
                    m "..."
                    m "Non, mauvaise idée."
                    m "Mieux vaut pas que je dorme maintenant. Essayons de chercher des indices sour notre situation à la place."
                    m "Je crois que je vois un miroir par là-bas."
                    m "Voyons voir..."
                    jump Chapitre1Fillematin
        "Nope":
            $ savoir_ecole = False
            e "..."
            e "Bon... J'y vais."
            m "Attends, pour aller à quel endroit."
            e "Sérieusement?"
            e "Ben devine."
            m "Comment?"
            e "..."
            $ endroit_fail = False 
            jump endroitf

label endroitf:          
    menu:
        "(De quel endoit parle t'elle?)"
        "D'un centre commercial":
            m "On doit aller dans un centre commerciale."
            e "Pardon?"
            m "Ce n'est pas ça?"
            e "Je vais faire comme si je n'avais rien entendu."
            hide emilia school unhappy
            show emilia school angry
            m "Et son nom, tu ne l'aurais pas oublié non plus...."
            e "À force de t'entendre..."
            e "Tu es vraiment idiote aujourd'hui."
            m "Ben merci."
            hide emilia school angry
            show emilia school unhappy
            e "..."
            e "Et son nom?"
            m "Je te demande pardon?"
            e "Tu m'as très bien entendu"
        "D'une église":
            $ endroit_fail = True
            m "On doit aller dans une église, je présume."
            e "..."
            e "C'est ça."
            m "Ah bon?"
            hide emilia school unhappy
            show emilia school angry
            e "Bien sûr que non!"
            e "Je vais faire comme si je n'avais rien entendu."
            hide emilia school angry
            show emilia school unhappy
            m "..."
            hide emilia school unhappy
            show emilia school angry
            m "Et son nom, tu ne l'aurais pas oublié non plus...."
            e "À force de t'entendre..."
            e "Tu es vraiment idiote aujourd'hui."
            m "Ben merci."
            hide emilia school angry
            show emilia school unhappy
            e "..."
            e "Et son nom?"
            m "Je te demande pardon?"
            e "Tu m'as très bien entendu"
        "Un lycée":
            m "Dans un lycée, c'est logique."
            e "..."
            e "Ben oui."
            m "(Je suis trop forte.)"
            hide emilia school unhappy
            show emilia school happy
            e "Comme quoi tu sais au moins ou on doit aller."
            m "Bien entendu."
            e "Et son nom?"
            m "Je te demande pardon?"
            e "Je parle du lycée."
    menu:
        "C'est quoi le nom du lycée?"
        "L'académie du pic de l'espoir.":
            $ savoir_ecole == True
            e "..."
            hide emilia school happy
            show emilia school unhappy
            e "Tu t'es cru dans Danganronpa ma parole..."
            e "C'est pas ça du tout."
            e "C'est le lycée Archipel."
            e "Je préfère que tu me dise que tu en as aucune idée que de me sortir des conneries pareils la prochaine fois."
        "Le lycée Kouo.":
            $ savoir_ecole == True
            hide emilia school happy
            show emilia school unhappy
            e "..."
            e "Mais..."
            e "Pourquoi?"
            m "Ben quoi?"
            e "Non c'est pas ça du tout."
            e "C'est le lycée Archipel."
            e "Je préfère que tu me dise que tu en as aucune idée que de me sortir des conneries pareils la prochaine fois."
        "C'est le lycée Meishu.":
            $ savoir_ecole == True
            e "..."
            e "Tu voudrais bien. Certains profs ont l'air sympa."
            e "Mais non. Ce n'est pas cela."
            e "C'est le lycée Archipel."
            e "Je préfère que tu me dise que tu en as aucune idée que de me sortir des conneries pareils la prochaine fois."
        "Je ne sais pas":
            $ savoir_ecole == True
            e "..."
            hide emilia school unhappy
            show emilia school happy
            e "Enfin une réponse sincère."
            e "C'est le lycéee Archipel son nom."
            e "Je pensais que tu le savais."
            hide emilia school happy
            show emilia school unhappy
    hide emilia school unhappy
    show emilia school happy
    e "Je te laisse, salut [m]."
    m "Atends..."
    hide emilia school happy 
    m "Non attends!" 
    m "(Elle est partie.)"
    m "(Purée mais que dois-je faire?)"
    m "(Comment dois-je m'y prendre pour rentrer chez moi?)"
    m "..."
    m "(Je me sens faible.)"
    m "(Je crois que je vais... Dormir un instant...)"
    m "..."
    m "Non, mauvaise idée."
    m "Mieux vaut pas que je dorme maintenant. Essayons de chercher des indices sour notre situation à la place."
    m "Je crois que je vois un miroir par là-bas."
    m "Voyons voir..."
    jump Chapitre1Fillematin

label Chapitre1Fillematin:
    scene white 
    with mediumdissolve
    $ time.sleep(1)
    m "Il doit être par ici, si je me souviens bien."
    m "Alors..."
    scene me 
    with slowdissolve
    $ time.sleep(3)
    m "(Wahou.)"
    m "(C'est moi?)"
    m "(C'est pas croyable.)"
    m "(Je suis une toute autre personne.)"
    scene bg chambrefillemain
    with mediumdissolve
    $ time.sleep(1)
    m "..."
    m "Donc..."
    m "Je ne sais pas par quels moyens cela est arrivé mais je suis dans le corps de quelqu'un d'autre."
    m ""

   
label Chapitre1Garçonmatin:
    scene white
    $ time.sleep(2)
    m "Il doit être par ici, si je me souviens bien."
    m "Alors..."

    return
