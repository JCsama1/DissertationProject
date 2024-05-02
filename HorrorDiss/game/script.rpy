label start:

    # Set the background to a placeholder image
    scene bg placeholder_bg

    # Play background music with looping
    play music "audio/horror_bg.mp3" volume 0.5 loop

    "I have always been uneasy driving alone at night. It was worst the first few times when I had just gotten my license, but the nagging fear has never gone away to this day."

    "It’s disorienting to look into the mirrors and see nothing, and I mean nothing but the consuming blackness of the night."

    # Transition to a dark mirror image with a smoother dissolve
    with dissolve
    scene bg void

    "It makes me hesitant to check the mirrors should I see this dark void, or worse,"

    "..."

    # Transition to the protagonist looking into the car mirror with a smoother dissolve
    with dissolve
    show protagonist normal

    play sound "audio/lowgrowl.mp3"    

    "someone sitting in my back seat staring at me."

    # Transition to a dark car exterior image with a smoother dissolve
    with dissolve
    scene bg car ext

    # Play car engine sound with looping and assign it to channel 'engine'
    play sound "audio/car_engine.mp3"

    "In the summer of 2013, I found myself driving home alone on highway 902 from a party. It was almost midnight, and needless to say it was pitch black."

    "As was usual at night, I was on edge."

    # Transition to the highway at night background with a smoother dissolve
    with dissolve
    scene bg car int

    "I had the radio off, and could hear nothing but the muffled roar of tires on pavement and the dull hum of the engine."

    "I stole a glance into the middle rearview mirror, and saw nothing but darkness through the back window."

    "I know that I looked backward and saw nothing."

    # Transition to a dark mirror image with a smoother dissolve
    with dissolve

    "Just the seemingly endless blackness of the night. I remember it so clearly because not ten seconds later a car passed me to the left. Headlights on."

    play sound "audio/carfast.mp3" 

    # Transition to a highway background with another car with a smoother dissolve
    with dissolve
    scene bg highway_with_car

    "I had one of those sudden adrenaline rushes like when you think you see a person outside your bedroom window when it’s just a tree, or when you start awake at night with the feeling of falling."

    "Ten seconds earlier, nothing had been behind me. Suddenly, a car. I drove all the way home shivering and knowing something was off."

    # Stop the car engine sound
    stop sound fadeout 2.0

    # Transition to a dark road with protagonist driving with a smoother dissolve
    with dissolve
    scene bg car int

    "The next morning, I found two sets of scratches near the back of my van."

    "One was on the left rear,"

    "one was on the right."

    # Transition to the van with scratches with a smoother dissolve
    with dissolve
    scene bg van_with_scratches
    play sound "audio/scratch.mp3"

    "The car was pretty old. They could have been there for months, but that was the first time that I distinctly remembered seeing them."

    "In hindsight, there are two possibilities for what happened that night."

    "Possibility one."

    "By some glitch in reality, or something paranormal, this other car had somehow appeared behind me within ten seconds of me checking my mirror."

    play sound "audio/ghost.mp3"

    "Like some weird ghost or something."

    "However, the second option is what makes my blood run cold whenever I consider it."

    "Possibility two."

    "The car was normal. It had approached me from the rear and passed me to my left."

    "However,"

    with dissolve
    scene bg monster

    play music "audio/lowgrowl.mp3" volume 0.5 loop

    "something large, and wide, and as black as the night had been clinging to the rear of my car, obscuring my view through the window and leaving deep scratches on the sides."

    stop sound fadeout 2.0

    "And I had inadvertently driven it home with me."

    # Transition to a black screen with a smoother fade out
    with dissolve
    scene black

    return