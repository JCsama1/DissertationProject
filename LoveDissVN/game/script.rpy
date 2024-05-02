define n = Character("Nellie")
define m = Character("Maid")
define me = Character("Mell")
define a = Character("Arthur")

label start:
    play music "audio/Luciole.mp3" volume 0.5 loop
    scene black
    show nelliesad with dissolve

    "With her dampened eyes, Nellie looked around and watched people enjoying themselves to the fullest. Yet none of that gave her any joy."
    "She was playing her conversation with Arthur over and over again."

    hide nelliesad with dissolve
    show arthur with dissolve
    play sound "audio/crowd.mp3" volume 0.5 loop

    a "Are you really going to be like that? I went out of my way to take you to your favorite play. The least you could do is be a little kinder to me."
    a "What was it called again... Romeo and Juliet?"
    a "It's been running for six or seven years now."
    a "A family like yours or mine could pay to have a brand new script written. So why should we have to see an old play at a theater full of commoners?"
    a "It may be private, but even so... Haah... I would rather just have a show put on at my estate—"

    hide arthur
    show nellietoarthur
    n "Stop talking already!"
    n "Why should I - Why should I have to marry someone like you?! I have ab-so-lutely no desire to marry you! Whatever it takes, I will put a stop to this! I'll talk to Father as many times as I must!"

    hide nellietoarthur
    show arthur
    a "Please, don't make such a scene. It's shameful."
    a "There are people around; remember, you represent your family. Besides, our families are hardly strangers to one another."
    a "Try as you might, I doubt you can get rid of me. No matter what you say, you can't break this engagement."

    hide arthur
    show nellietoarthur
    n "You don’t-!"

    hide nellietoarthur
    show arthur
    a "Your parents gave you too much freedom, and look at what a spoiled little girl you became because of it. Goodness, you're going to be quite the handful."

    hide arthur
    show nellietoarthur
    n "Oh, get off your high horse!"

    hide nellietoarthur
    show arthur
    a "No, you're the one on a high horse, Nellie."

    a "You are going to be my wife; you could at least put some effort into liking me."

    hide arthur
    show nellietoarthur
    n "…!"

    play sound "audio/running.mp3" volume 0.5 fadeout 2.0

    hide nellietoarthur
    show arthur
    a "Hey, where are you running off to?"

    play sound "audio/door.mp3" volume 0.5

    hide arthur with dissolve
    show nelliesad with dissolve
    play music "audio/Petalouda.mp3" volume 0.2 loop

    "Suffering from a terrible feeling, she sat alone, hiding her sobbing face behind her palms. The next moment, she heard a friendly voice."

    hide nelliesad
    show happymaidtonellie
    m "Is everything alright?"

    hide happymaidtonellie
    show nellietomaid 
    n "Yeah… I am… I am okay,"
    "Nellie avoided the question as she wiped the tears from her face."

    hide nellietomaid
    show maidtonellie 
    m "Do you mind if I sit next to you? My legs are killing me."

    hide nellietomaid 
    show maidtonellie
    m "So, is everything really okay?"

    hide maidtonellie
    show nellietomaid 
    n "My engagement partner said some hurtful things. He was right for the most part, but I just don't want to be married to him. It sickens me to think I'm going to be his wife one day."

    hide nellietomaid 
    show maidtonellie 
    m "I know it's hard, but you'll be okay."
    m "Life is too short to cry over something that isn't meant to be."

    hide maidtonellie 
    show nellietomaid 
    n "But for me, it means a lot. I'm going to spend my whole life with him."

    hide nellietomaid 
    show maidtonellie
    m "If you think about it that way, then your situation is quite depressing."
    n "…" 
    m "Do you have any happy moments that you think back on fondly? Perhaps with your brother?"
    m "I know you love him a lot."

    hide maidtonellie with dissolve
    show beforechflashback with dissolve
    n "I do. I wish he was here now."

    hide beforechflashback with dissolve
    show nellietomellchflashback with dissolve
    play music "audio/Cetoniinae.mp3" volume 0.0 loop

    n "Oh, dearest Mell, please..."
    "The young girl approached her brother, who was consumed by the text. In her hands, she carried a large pile of rose petals."

    play sound "audio/page.mp3" volume 0.3 loop
    hide nellietomellchflashback with dissolve
    show melltonelliechflashback with dissolve
    me "…"

    play sound "audio/leaves.mp3" volume 0.4

    me "Ahh!"

    play music "audio/horrorlove.mp3" volume 0.3 loop
    hide melltonelliechflashback
    show nellietomellchflashback
    n "Hehe. Look, your head is covered in roses, Mell!"

    hide nellietomellchflashback 
    show melltonelliechflashback 
    me "Oh, Nellie... You got petals on the book. This isn't mine. I can't afford to let it get dirty."

    hide melltonelliechflashback
    show nellietomellchflashback
    n "It's your fault, dearest Mell. I tried to get your attention."
    n "And besides, flowers won't get a book dirty!"

    hide nellietomellchflashback 
    show melltonelliechflashback
    me "I must raise the white flag. When did my little lady find herself such a sharp wit?"

    hide melltonelliechflashback
    show nellietomellchflashback
    n "While waiting for you, dearest Mell. I waited, and I waited, and you didn't so much as glance at me. I'll be an adult by the time you're done reading that book."

    hide nellietomellchflashback 
    show melltonelliechflashback
    me "Wow, that soon?"

    hide melltonelliechflashback
    show nellietomellchflashback
    n "That soon."
    n "Mother says girls grow up fast."

    hide nellietomellchflashback with dissolve
    show diffcolourchflashback with dissolve
    n "Haha, she may be right."
    
    hide diffcolourchflashback with dissolve
    show melltonelliechflashback with dissolve
    me "In that case, we should do something together before you're all grown up. Surely you won't play with me any longer when you become an adult."

    hide melltonelliechflashback
    show nellietomellchflashback
    n "That's not true! I'll still play with you, even when I'm grown up!"

    hide nellietomellchflashback 
    show melltonelliechflashback
    me "But grown-ups don't play, Nellie."

    hide melltonelliechflashback
    show nellietomellchflashback
    n "F-Fine! I'll stay a child forever, then!"

    hide nellietomellchflashback 
    show melltonelliechflashback
    me "Didn't you just say you were about to grow up?"

    hide melltonelliechflashback
    show nellietomellchflashback
    n "Nnh... You're so mean, Mell."

    show blackk with dissolve

    play music "audio/Petalouda.mp3" volume 0.2 loop
    hide nellietomellchflashback with dissolve
    hide blackk with dissolve
    show maidtonellie with dissolve
    m "There's an important point you brought up."

    hide maidtonellie
    show nellietomaid 
    n "What do you mean?"

    play music "audio/horror.mp3" volume 0.3
    show maidtonellie with dissolve
    m "You expressed a desire to remain a child forever. Is that still your wish?"

    play music "audio/Petalouda.mp3" volume 0.2 loop
    hide maidtonellie
    show nellietomaid 
    n "Honestly, yes, but I know it's impossible."

    hide nellietomaid
    show happymaidtonellie 
    m "Not entirely. The only distinction between adults and children is that children lack responsibilities and are carefree, which is why they're often happier."

    hide happymaidtonellie
    show nellietomaid 
    n "I'm listening."

    hide nellietomaid
    show happymaidtonellie 
    m "As an important person and soon-to-be adult, you'll inevitably face responsibilities. However, this can be advantageous."
    m "You can choose not to care and live life on your terms instead of being bound to a man you don't love."
    m "Of course, you'll have to play the role of a wife at events like this, but once you return to your normal life, you're free to do as you please."
    m "Since he doesn't care about you beyond events, this situation works to your advantage."

    hide happymaidtonellie
    show nellietomaid 
    n "Interesting."
    n "..."
    n "Thank you very much. Your message, albeit a bit unconventional, has come across, and I appreciate it."

    hide nellietomaid
    show happymaidtonellie
    m "Of course. I'm glad I could provide some form of assistance."

    hide happymaidtonellie
    show nellietohappymaid
    n "I wish we could talk more, but I have an important errand to run."

    hide nellietohappymaid with dissolve
    scene black
    return