# The script of the game goes in this file.



##pick between one of the two and add an # to the other to keep it

##regular taps, medium intervals
#define sounds = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg']

##light taps, smaller intervals
#define sounds = ['audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']


##both combined
define sounds = ['audio/Sound/A1.ogg', 'audio/Sound/A2.ogg', 'audio/Sound/A3.ogg', 'audio/Sound/A4.ogg', 'audio/Sound/A5.ogg', 'audio/Sound/B1.ogg', 'audio/Sound/B2.ogg', 'audio/Sound/B3.ogg', 'audio/Sound/B4.ogg', 'audio/Sound/B5.ogg']

init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v
            #don't mind comment on top



        elif event == "slow_done" or event == "end":
            renpy.sound.stop()



# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Character Name Tags part 1
define narrator = Character("", callback=type_sound)
define JR = Character("Jose", color = "#badc58", callback=type_sound)
define L = Character("Lola", color = "#e84393", callback=type_sound)
define Q = Character("???", callback=type_sound)
define PA = Character("Paciano", color = "#16a085", callback=type_sound)
define MAR = Character("Mariano", color = "#22a6b3", callback=type_sound)
define MAR2 = Character("Mariano Katigbak", color = "#22a6b3", callback=type_sound)
define MAN = Character("Manuel", color = "#686de0", callback=type_sound)
define S = Character("Segunda", color = "#4834d4", callback=type_sound)
define F = Character("Francisco", color = "#81ecec", callback=type_sound)
define SOL = Character("Soledad", color = "#fdcb6e", callback=type_sound)
define SAT = Character("Saturnina", color = "#ff7675", callback=type_sound)
define OLI = Character("Olimpia", color = "#00b894", callback=type_sound)
define YSA = Character("Ysabel", color = "#fab1a0", callback=type_sound)
define VEN = Character("Vendor", color = "#636e72", callback=type_sound)

#Character Name Tags part 2
define MARC = Character("Marco Soriano", color = "#fc5c65", callback=type_sound)
define MAC = Character("Marco", color = "#fc5c65", callback=type_sound)
define LV = Character("Leonor Valenzuela", color = "#fd9644", callback=type_sound)
define LR = Character("Leonor Rivera", color = "#fed330", callback=type_sound)
define CJ = Character("Capt. Juan", color = "#26de81", callback=type_sound)
define CSAN = Character("Capt. Sanday", color = "#2bcbba", callback=type_sound)
define DCON = Character("Dona Concha", color = "#eb3b5a", callback=type_sound)
define GARD = Character("Gardener", color = "#fa8231", callback=type_sound)
define TAN = Character("Tiyo Antonio", color = "#f7b731", callback=type_sound)
define TSI = Character("Tiya Silvestre", color = "#20bf6b", callback=type_sound)
define GD1 = Character("Guardia 1", color = "#0fb9b1", callback=type_sound)
define GD2 = Character("Guardia 2", color = "#45aaf2", callback=type_sound)
define JC = Character("Jose Cecilio", color = "#4b7bec", callback=type_sound)
define CE = Character("Cecilio", color = "#4b7bec", callback=type_sound)
define FA = Character("FATHER(?)", color = "#4b7bec", callback=type_sound)
define ME = Character("ME", color = "#45aaf2", callback=type_sound)
define JA = Character("Javier Lizares", color = "#cd84f1", callback=type_sound)
define JL = Character("Javier", color = "#cd84f1", callback=type_sound)
define DA = Character("Daniel Sevilla", color = "#ffcccc", callback=type_sound)
define DS = Character("Daniel", color = "#ffcccc", callback=type_sound)
define IA = Character("Ignacio Aran", color = "#ff4d4d", callback=type_sound)
define IG = Character("Ignacio", color = "#ff4d4d", callback=type_sound)
define PSA = Character("Paul Sagahun", color = "#ffaf40", callback=type_sound)
define PS = Character("Paul", color = "#ffaf40", callback=type_sound)
define GVD = Character("Gravedigger", color = "#32ff7e", callback=type_sound)
define CLK = Character("Clerk", color = "#7efff5", callback=type_sound)
define FAS = Character("Father Salvacion", color = "#18dcff", callback=type_sound)



#Affection Variables
default valenzuela_affection = 0
default rivera_affection = 0

#Gifts for the Ladies
default acquiredPaperFan = False
default acquiredHandkerchief = False
default acquiredBrooch = False
default acquiredSewingKit = False

#Endings
default valenzuela_pick = False
default rivera_pick = False

#Hero path
default valenzuela_epi3 = False
default rivera_epi3 = False


#Character Sprites part 1
image YJose = "Young Jose Sprite.webp"
image YPaciano = "Young Paciano.webp"
image Lola = "Lola Sprite.webp"
image Jose = "Jose Sprite.webp"
image Mariano = "Mariano Sprite.webp"
image Segunda = "Segunda Sprite.webp"
image Manuel = "Manuel Sprite.webp"
image Paciano = "Paciano Sprite.webp"
image Francisco = "Francisco Sprite.webp"
image Soledad = "Soledad Sprite.webp"
image Saturnina = "Saturnina Sprite.webp"
image Olimpia = "Olimpia Sprite.webp"
image Ysabel = "Ysabel Sprite.webp"
image Vendor = "Chinese Vendor Sprite.webp"

#Character Sprites part 2
image LValenzuela = "L. Valenzuela Sprite.webp"
image LRivera = "L. Rivera Sprite.webp"
image CaptVa = "Capt Valenzuela Sprite.webp"
image Daniel = "Daniel Sprite.webp"
image Ignacio = "Ignacio Sprite.webp"
image Javier = "Javier Sprite.webp"
image JCecilio = "Jose Cecilio Sprite.webp"
image Marco = "Marco Sprite.webp"
image Paul = "Paul Sprite.webp"
image TSilvestre = "Tiya Silvestre.webp"
image TAntonio = "Tiyo Antonio Sprite.webp"
image DonConcha = "Dona Concha Sprite.webp"
image Gardener = "Gardener Sprite.webp"
image PSalvacion = "Padre Salvacion Sprite.webp"

#Backgrounds for the Scenes Part 1
image bgRHwRain = Movie(play="Rizal House with Rain.webm")
image bgDR1 = "Dirt Road 1.webp"
image bgDR2 = "Dirt Road 2.webp"
image bgBnBEx = "Bahay na Bato Exterior.webp"
image bgLV = "Bahay na Bato Living Room F.webp"
image bgAZ = "Azotea.webp"
image bgBR = "bedroom.webp"
image bgCF = "Cafe.webp"
image bgDN = "Diner.webp"
image bgCdC = "Colegio de Concordia.webp"
image bgEC = "Escolta.webp"
image bgBlack = "Black BG.webp"

#Backgrounds for the Scenes Part 2
image bgBRD = "Bedroom_Day.webp"
image bgBRN = "Bedroom_Night.webp"
image bgBHD = "Boarding_House_Day.webp"
image bgBHN = "Boarding_House_Night.webp"
image bgCT = "Casa_Tomasina.webp"
image bgCTN = "Casa_Tomasina_Night.webp"
image bgEK = "Eskinita.webp"
image bgLB = "Library.webp"
image bgSAI = "SanAgustinChurchInterior.webp"
image bgSAD = "SanAgustinChurchDim.webp"
image bgSAL = "SanAgustinChurchLight.webp"
image bgSTO = "Santo_Tomas.webp"
image bgSTR = "Street.webp"
image bgVHD = "Valenzuela_House_Day.webp"
image bgVHN = "Valenzuela_House_Night.webp"
image bgPS = "Plaza_Sampalucan.webp"
image bgPSN = "Plaza_Sampalucan_Night.webp"
image bgLMD = "Lizares_Mansion_Day.webp"
image bgLMF = "Lizares_Mansion_Night_On_Fire.webp"

#CGIs for Part 1
image cgCTH = "Cards_touching_hands.webp"
image cgHE = "Hero_Ending.webp"
image cgJRH = "Jose_Removes_Hair.webp"
image cgMC = "Manuel_Chess.webp"
image cgPRH = "Paper_Rose_Hat.webp"
image cgSCL = "Segunda_crying-laughing.webp"
image cgSE = "Segunda_Ending.webp"

#CGIs for Part 2
image cgCMT = "Churchmates.webp"
image cgFP = "Feeding_program.webp"
image cgJA = "Javier_Arson.webp"
image cgKBD = "Kabedon.webp"
image cgKNLNNM = "Kapatid_na_lalake_ng_nanay_mo.webp"
image cgRC = "Rivera_Crazy.webp"
image cgSCR = "Scissors.webp"

#CGIs for Interlude
image cgINT1-1 = "INT1-1.webp"
image cgINT1-2 = "INT1-2.webp"
image cgINT2-1 = "INT2-1.webp"
image cgINT2-2 = "INT2-2.webp"
image cgINT3-1 = "INT3-1.webp"
image cgINT3-2 = "INT3-2.webp"

#Splash Screen of Logos
image logo = "SplashScreen.webp"
image disclaimer = "Disclaimer.webp"

#Pre-Epi
image PreELV = "LV_epi_1.webp"
image PreELR = "LR_epi_1.webp"

#Title Cards
image ttlP1 = "Title_Card_Part_1.webp"
image ttlP2 = "Title_Card_Part_2.webp"
image ttlP2LV = "Title_Card_Part_2_LV.webp"
image ttlP2LR = "Title_Card_Part_2_LR.webp"



#Transform Coordinates For Characters
transform leftYJR:
    xoffset -700
    yoffset -110

transform rightYPA:
    xoffset 78
    yoffset -36

transform leftLol:
    xoffset -693
    yoffset -48

transform leftMar:
    xoffset -698
    yoffset -36

transform rightMar:
    xoffset 50
    yoffset -36

transform semirightS:
    xoffset -86
    yoffset -36

transform rightMan:
    xoffset 70
    yoffset -36

transform semileftS:
    xoffset -436
    yoffset -36

transform semirightMar:
    xoffset -100
    yoffset -36

transform leftMan:
    xoffset -716
    yoffset -36

transform rightLol:
    xoffset 50
    yoffset -48

transform rightS:
    xoffset 72
    yoffset -36

transform leftS:
    xoffset -678
    yoffset -36

transform leftPA:
    xoffset -665
    yoffset -28

transform leftF:
    xoffset -685
    yoffset -36

transform rightSOL:
    xoffset 64
    yoffset -36

transform leftSAT:
    xoffset -679
    yoffset -36

transform leftOLI:
    xoffset -701
    yoffset -36

transform leftYSA:
    xoffset -708
    yoffset -36

transform leftVEN:
    xoffset -700
    yoffset -38

transform rightOLI:
    xoffset 64
    yoffset -36

transform leftMarc:
    xoffset -700
    yoffset -36

transform leftLV:
    xoffset -680
    yoffset -36

transform rightCV:
    xoffset 100
    yoffset -36

transform leftDCON:
    xoffset -700
    yoffset -36

transform leftGARD:
    xoffset -665
    yoffset -36

transform leftTAN:
    xoffset -665
    yoffset -36

transform rightTSI:
    xoffset 65
    yoffset -36

transform semirightLR:
    xoffset -100
    yoffset -38

transform leftJC:
    xoffset -700
    yoffset -36

transform leftLR:
    xoffset -692
    yoffset -38

transform rightJA:
    xoffset 65
    yoffset -36

transform semirightDAN:
    xoffset -200
    yoffset -36

transform leftIG:
    xoffset -700
    yoffset -36

transform leftPAUL:
    xoffset -700
    yoffset -36

transform rightMARC:
    xoffset 65
    yoffset -36

transform leftMARC:
    xoffset -700
    yoffset -36

transform rightJC:
    xoffset 70
    yoffset -36

transform leftDAN:
    xoffset -700
    yoffset -36

transform semileftIG:
    xoffset -450
    yoffset -36

transform leftCV:
    xoffset -665
    yoffset -36

transform rightLV:
    xoffset 40
    yoffset -36

transform leftJA:
    xoffset -700
    yoffset -36

transform semileftJC:
    xoffset -450
    yoffset -36

transform rightLR:
    xoffset 48
    yoffset -38

transform leftPSAL:
    xoffset -700
    yoffset -36

transform leftTSI:
    xoffset -700
    yoffset -36


# The game starts here.

label start:

    #+++++++++   SCENE 1 BOI   +++++++++++++++++++++++++++++++++++++++++++Pages 1-3 of the Script+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    scene bgRHwRain
    play music "audio/Music/Plaint.mp3" loop
    with dissolve


    play Rain "audio/Voice/Rain.mp3"



    "The sound of rain pattered tirelessly against the window sill."
    "I laid in my bed, surrounded by my fluffy pillows and blankets."
    "A loud banging at the door downstairs roused me awake."

    play BANG "audio/Voice/BANG.mp3"
    "BANG BANG BANG" with hpunch

    play Footstep "audio/Voice/Footsteps.mp3"
    "Hurried footsteps rushed to the entrance."
    "I could hear the deep voice of a man speaking in harsh tones."

    "I got out of bed and peered out the window."

    play ShoutWoman "audio/Voice/Shouting.mp3"
    "There is a convoy stopped in front of the house, with armored men holding weapons and lanterns. I heard a loud cry and saw one of them pull my mother out into the pouring rain."

    show YJose at leftYJR
    with easeinleft
    with None

    JR "Mama?"

    play Footstep "audio/Voice/Footsteps.mp3"
    "I rushed down the stairs to see my father running out the door and my sisters crying amongst themselves."
    "My brother, Paciano, stood stoically by the wayside. He laid a hand on my shoulder."

    show YPaciano at rightYPA
    with easeinright
    with None

    PA "Pepe, don’t follow them."

    JR "I don’t understand. What’s happening? Where are they taking mama?"

    PA "The {i}Guardia Civil{/i} came just now to arrest her. They said that she and uncle Alberto tried to poison his wife."

    JR "But… But there’s no way they’d do that!"

    PA "I know, Pepe, I know. Come with me for a second."

    "I looked back anxiously at the commotion at the front entrance, and then nodded."

    play DoorCL "audio/Voice/DoorCL.mp3"
    "Paciano gently led me past the foyer and into our father’s study. He closed the door behind us, muffling the sound of arguing on the other side."
    "I fidgeted uncomfortably in front of my brother."

    PA "Have I ever told you about my friend, Father Jose Burgos?"

    "I shook my head."

    PA "He was executed along with two other priests: Mariano Gomez and Jacinto Zamora. All for a crime none of them committed."
    PA "We live under the occupation of the Spanish {i}peninsulares{/i} and the friars. As long as that continues to be so, they may do with us however they please."

    "I thought back to my mother being dragged outside by the guard, and my heart sank."

    JR "Is that what’s going to happen to Mama too? Is she… going to be executed?"

    PA "Probably not, but they’ll keep her imprisoned for as long as they can. The accusation of attempted murder is just a sham."
    PA "If you ask me, I think the real reason was because Papa refused the {i}Guardia{/i} horse fodder the other week."

    JR "What...? Are you serious? All this happened because of some stupid petty slight? They can't do that! How is that even supposed to hold up in court?"

    PA "Hey, I never said the reason had to make sense. Besides, it was to send a message. Knowledge is power, and perception shapes that."
    PA "If the {i}Guardia Civil{/i} allowed her to disrespect them, it might make other people think they could do the same."
    PA "The hammer that sticks out gets beaten down. Is it fair? No, obviously not. But I don't think they care very much about what’s ‘fair’."
    PA "The only reason they can do that is because they have the power to back it up."

    JR "I can't believe this. Is there any justice at all?"

    PA "This is the real world, and it’s full of injustice fueled by the greed of others."
    PA "Look at me, Pepe. I can tell you are angry and I want you to hold on to that feeling for now. Remember this day…"

    "Paciano held me by the shoulders, his stare burning with conviction. The weight of its intensity pinned me in place. I had never seen my brother look so enraged before."

    PA "…and you’ll remember who your true enemy is."


    #STOP SOME UNNECESSARY SFX######
    stop BANG
    stop Footstep
    stop ShoutWoman
    stop DoorCL
    stop Rain
    stop music
    with None
    #STOP SOME UNNECESSARY SFX######


    scene ttlP1
    with fade
    pause (3.0)
    with None


    #+++++++++   SCENE 2 BOI   +++++++++++++++++++++++++++++++++++++++++++Pages 3-5 of the Script+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    scene bgDR1
    with fade
    with None

    # For hiding unnessary characters
    hide YJose
    hide YPaciano
    # For hiding unnessary characters

    play WalkGravel "audio/Voice/WalkGravel.mp3"
    "The streets are almost empty as the heat of the sun compelled the townsfolk to stay in-doors. "
    "I regretted donning one of my more expensive looking attires that is not at all suitable with the weather."
    "Mariano continued to chatter beside me as we walked to my Lola's house."

    "I once again looked down at my tailored jacket and buttoned up shirt and cursed the sweltering heat. I looked more like a used-up rag,"
    "{i}\“My disappointment is immeasurable and my day is ruined.\”{/i}"
    "I wasn't paying attention at all to Mariano until he said something that caught my attention."

    JR "Wait, what do you mean Isidro is dead?!"

    show Mariano at leftMar
    with easeinleft

    MAR2 "I didn’t say he’s DEAD. I said he was caught in an encounter with the {i}guardia civil{/i}."
    MAR2 "According to reports, he was carrying propaganda materials and a gun. A gun, Jose! Can you believe that?"

    JR "Then he’s as good as dead."
    JR "Poor Isidro, he would have had a bright future ahead of him. He was a much better mathematician than I will ever be."

    "I recalled Isidro gladly lending me his notes in mathematics when I skipped school due to a cough. Quite a rare sight especially in a highly competitive environment."

    MAR2 "Reserve your sympathy for someone else. He’s an enemy of the state."
    MAR2 "He branded himself a traitor the moment he carried that gun, but that doesn’t mean they’ll kill him."
    MAR2 "Only the worst of criminals get that treatment. They aren’t as bad as you think they are."

    "Something inside me snapped. I could once more hear the distant sound of rain, and the cries of my mother being dragged across the street."

    JR "You seriously believe that?"
    JR "{i}Dios mio{/i} Mariano, you think the {i}guardia civil{/i} aren’t capable of planting false evidence on our poor classmate?!"

    "Mariano looked caught by surprise at my sudden outburst."

    MAR2 "They vowed to protect us, Jose! It is their duty."

    JR "They will kill him and display his corpse to make an example out of him!"
    JR "This! This is what’s going to happen to the people who choose to disobey!"

    "The both of us fell into a tense silence, the dirt path making way to show Lola's house nearby. "
    "Mariano just didn't get it. He had no idea about the lengths the {i}peninsulares{/i} will go to keep us all in line."
    "I kept those thoughts to myself."
    "Mariano slowed down just as I was a few paces ahead of him."

    MAR2 "Jose…you’re blowing this all out of proportion."

    "I ignored him and continued walking. Mariano stopped me with a hand to my shoulder."

    MAR2 "Trust me when I say Isidro will not die"

    stop WalkGravel
    play StopWalk "audio/Voice/StopWalk.mp3"
    "I stopped in my tracks and looked at Mariano from my shoulder, a grim expression on my face."

    JR "I hope you’re right."



    #+++++++++   SCENE 3 BOI   +++++++++++++++++++++++++++++++++++++++++++Pages 5-9 of the Script++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    scene bgBnBEx
    play music "audio/Music/Almost New.mp3" loop
    with fade
    with None

    # For hiding unnessary characters
    hide Mariano
    # For hiding unnessary characters

    play KnockDoor "audio/Voice/KnockDoor.mp3"
    "I knocked on the door. Not long after that, my lola received us both into her home as guests with a kind smile on her old face."

    show Lola at leftLol
    with easeinleft

    L "{i}Apo!{/i} You made it!"

    "I grabbed my lola’s hand placed it against my forehead as a sign of respect."

    JR "Of course, lola. I wouldn’t miss your birthday for the world."

    "I motioned for Mariano to move forward."

    JR "And I brought a friend, do you still remember Mariano?"

    "Mariano took her hand and repeated the {i}mano{/i} I did earlier."

    show Mariano at rightMar
    with easeinright

    MAR "{i}Mano po{/i} lola, and Happy Birthday!"

    L "Yes, yes how could I forget."
    L "Mariano, my, you’ve grown to be quite a handsome young man. Well…not as handsome as my {i}apo{/i} that is."

    play LaughingUs "audio/Voice/LaughingUs.mp3"
    "We all laughed with amusement, when suddenly..."

    show Segunda at semirightS
    with easeinright

    Q "{i}Kuyaaa!!!{/i}"

    "A girl a couple of years younger than me approached the group. Mariano, to be precise. "
    "I couldn't make out the features of her face with her back turned to me."

    Q "Tell me it isn’t true."

    MAR "What is?"

    "The girl leaned forward in a whisper. Mariano obliged, moving his torso towards to hear clearly."

    Q "That you’re a part of a secret society that recruits men that do dangerous secret society stuff?"

    play Chuckled "audio/Voice/Chuckled.mp3"
    "Mariano pondered on the question and chuckled at the absurdity of it."

    Q "Why are you laughing? What’s so funny?"

    MAR "Now where did you hear that, dear sister?"

    "{i}\“Ah yes, Mariano’s sister.\”{/i} I realized who the interesting character was. "
    "Mariano once mentioned to me that she was already engaged to be married to a certain relative of theirs."

    Q "I’m a KATIGBAK, {i}kuya{/i}. I have the means to know things."

    MAR "Oh, sister…you must’ve been so bored."
    MAR "Mother says you’ve been neglecting your needlework in favor of reading novels in your spare time."

    "A girl…that reads books in her spare time? Why, she’s not like other girls!"

    Q "You say that as if it’s a cause for concern."

    MAR "It is. No girl should be wasting her time on such activities when she should be learning how to be a good wife to her husband, more so an even better mother to her children."
    MAR "Need I remind you, your future is already set in stone with the engagement."

    "The girl winced hopelessly at the blunt statement, her brow furrowed in displeasure. "
    "As much as I believed that men and women should have equal access to opportunities education-wise, I couldn’t help but agree with Mariano’s latter statement."

    Q "Just tell me my worries aren’t misplaced."

    MAR "I assure you, you have nothing to worry about. My schedule is already filled with academics."

    L "That’s right, dear. Mariano’s studies are of utmost importance. Students like him don’t have time to spare for such pointless activities."
    L "They have big dreams to fulfill, isn’t that right, {i}apo{/i}?"

    "All attention went to me and the stranger finally turned to take notice of my presence."
    "At that moment, the supposed main character of the day, my lola, faded into the background. "
    "Even Mariano who I've known for years felt almost like a disposable side character right next to the girl. Suddenly, I was self-conscious."
    "The girl was short, with expressive ardent eyes and rosy cheeks. Her provocative smile lent her the air of a slyph. "
    "I thought to myself that while she was not the most beautiful woman I had seen, I had never seen one more enchanting and alluring."

    JR "Ah, um, er…yes."

    "I had the sudden urge to punch myself in the face. I was usually quite well-spoken but in the presence of an attractive girl, I am reduced to a bumbling idiot."

    hide Lola
    hide Mariano
    hide Segunda

    menu:
        "Agree with her":
            jump C1_yes

        "Disagree":
            jump C1_no

    label C1_done:

    show Lola at leftLol
    show Mariano at rightMar
    show Segunda at semirightS

    "The girl looked at me thoughtfully. I saw this as an opportunity to hold her attention and lock in her gaze."
    "I took a confident step forward."

    JR "I assure you, my lady, Mariano does not indulge in any sort of business that could potentially put himself in danger or bring shame upon your family."
    JR "Take my words as true as I am with him most of the time."

    "The girl relaxed, looking visibly relieved. I mentally patted myself on the back."

    JR "Jose Protasio Rizal Mercado y Alonso Realonda. If I may, my lady…"

    "I gave out my hand. A shade of red forms on the girl's cheek as she realized the situation. "
    "She placed her dainty hand on mine, and I leaned down to give it a small kiss."

    Q "Oh, dear. How rude of me. Please excuse such an inappropriate display from my part. "
    Q "I should have introduced myself earlier. Segunda Solis Katigbak. Um…Sir?"

    "She was no longer just a stranger. I finally have a name to her innocent face. I smiled."

    MAR "Dear, you don’t have to be so formal."

    JR "Just Jose is fine."

    S "Right…Jose."

    "Segunda smiled politely. And just like that, I am struck with something inexplicable."
    "My name sounded good coming from her lips. My day didn’t feel as though it was initially ruined and am consumed with immediate gratitude towards my foresight."
    "{i}\“Thank heavens, I wore my best suit.\”{/i}"


    #STOP SOME UNNECESSARY SFX######
    stop Chuckled
    stop KnockDoor
    stop LaughingUs
    #STOP SOME UNNECESSARY SFX######
    #+++++++++   SCENE 4 BOI   +++++++++++++++++++++++++++++++++++++++++++Pages 9-12 of the Script++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    scene bgLV
    stop music
    play music "audio/Music/Tango de Manzana.mp3" loop
    with fade
    with None

    # For hiding unnessary characters
    hide Lola
    hide Mariano
    hide Segunda
    # For hiding unnessary characters



    play ChatterPips "audio/Voice/ChatterPips.mp3"
    "The house was bustling with the sound of festivities. Guests gathered at one side enjoying each other's company while some attended to the food."
    "Segunda, who previously excused herself after interrogating her brother, stood at the table where the beverages were placed."
    "The venue was filled with familiar faces, from distant relatives to family friends to neighbors. I nodded in acknowledgement to whoever asked for my attention."
    "There is one figure, however, that I didn't recognize. A broad shouldered, tall and slender young man, only a couple of years older than me, was socializing with another guest. "
    "Mariano approached the figure."

    show Mariano at leftMar
    with easeinleft
    MAR "Manuel! You made it!"


    show Manuel at rightMan
    with easeinright
    MAN "Mariano!"


    "The two boys seemed to be very close, I wondered. They hugged each other in greeting."


    MAN "Look at you all grown up."
    MAN "Is that the beginnings of a mustache I’m seeing?"



    MAR "Manuel, stop it!"
    MAR "Ah, Manuel. Let me introduce you to Jose. He’s a friend and a classmate."



    MAN "So you’re the famous Jose? I heard stories about you from your grandmother. I'm Manuel Luz."


    "Manuel looked at me with interest, a welcoming smile on his face. He offered his hand for a shake and I took it, returning a smile of my own."


    JR "Just Jose is fine."





    MAR "Stories? Care sharing it with the rest of us, Manuel?"



    MAN "Oh, it’s nothing of the embarrassing sort. Just that this gentleman right here is basically the golden child of the family."
    MAN "A writer, artist, academic achiever with an aptitude for fencing? What an honor it is to finally meet you."
    hide Mariano
    hide Manuel

    menu:
        "Show Gratitude":
            jump C2_yes

        "Keep Distant":
            jump C2_no

    label C2_done:
    show Mariano at leftMar
    show Manuel at rightMan

    "I had to admit, Manuel was very charismatic. No wonder Mariano liked him. "
    "It's a quality I'd like to have for myself someday but for now, I have to deal with what’s left of my own self esteem. How I wished Segunda was around to hear this."
    show Segunda at semileftS
    with easeinleft

    "Not even a moment later, my wish came true. Segunda approached our group, a glass of what appeared to be cerveza in her hand. Segunda handed the glass to Manuel."


    MAN "Thank you, sweetie."


    "{i}“Sweetie?”{/i} I resisted the urge to grimace and looked at Manuel questioningly but he was busy smiling at her. Segunda tucked a stray hair behind her ear." with hpunch



    S "I told you not to call me that."



    MAN "You told me not to call you {i}honey cake.{/i}"


    "{i}“Honey cake?!”{/i} I couldn't help the awkward tilt of my mouth as I heard that embarrassing name." with hpunch



    S "Ugh, Manuel stop it. You’re embarrassing me in front of the guests."


    "Segunda glanced at my direction, a mixture of worry and panic."



    MAN "What guests? You mean Jose and your brother?"


    "Seeing these two act so sweet and comfortable with each other made an uncomfortable feeling bubble up in my stomach."



    MAR "Oh, right. I forgot to mention. Jose, Manuel is Segunda’s fiance."


    "That feeling in my stomach lodged itself in my chest. I was so caught up in admiring Segunda's beauty that I didn't realize the signs that she and Manuel were already together. "
    "I tried my best to mask my disappointment."
    hide Mariano
    hide Manuel
    hide Segunda

    menu:
        "Feign Politeness":
            jump C3_yes

        "Say Nothing":
            jump C3_no

    label C3_done:

    show Manuel at rightMan
    show Mariano at leftMar
    show Segunda at semileftS
    with None
    MAN "See? Jose isn’t bothered at all. Don’t fret."


    "Segunda glared at Manuel and walked away."


    hide Segunda at semileftS
    with easeoutleft





    MAN "She wasn’t always this grouchy. She used to follow me around like a lost puppy when we were younger."


    "Despite knowing better, I couldn't help but feel Manuel was bragging about his closeness with Segunda, which irked me. My face remained passive, the perfect image of a polite guest."
    "How could I get in the way of two people destined to be with each other when my mother taught me the value of integrity. To ignore that would mean dishonoring her teachings."



    MAN "Well, gentlemen. If you all could excuse me. I have a fiance to pacify."

    hide Manuel at rightMan
    with easeoutleft


    "As Manuel walked away, I could've sworn I saw him turn around for a moment to give me a knowing look."



    stop ChatterPips


    #+++++++++   SCENE 5 BOI   +++++++++++++++++++++++++++++++++++++++++++Pages 12-14 of the Script++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    scene bgLV
    stop music
    play music "audio/Music/Promises to Keep.mp3" loop
    with fade
    with None

    # For hiding unnessary characters
    hide Mariano
    # For hiding unnessary characters

    play ISketch "audio/Voice/ISketch.mp3"
    "A week later, I found myself seated in one of the bamboo chairs in {i}Lola's{/i} living room. Somehow Mariano had convinced me to show off my drawing skills to the other guests here."
    "I would've refused, had it not been for Segunda wholeheartedly agreeing to it."
    "So here I was, pencil and paper in hand, lightly drawing strokes across the page. Across me was the beautiful Segunda, sitting prettily with a shy expression on her face."

    JR "I’m not very comfortable with people hovering over me as I draw."

    show Lola at leftLol
    with easeinleft
    with None
    L "Don’t mind us, {i}apo{/i}. Think of us as invisible."

    show Manuel at rightMan
    with easeinright
    with None
    MAN "I didn’t know Jose could draw."

    show Mariano at semirightMar
    with easeinright
    with None
    MAR "He’s good, trust me. I still have the portrait he made of me in my bedroom."

    L "Yes! My {i}apo{/i} always does his best at what he does."

    MAR "I can tell it’ll turn out great and he hasn’t even made that many marks yet."

    MAN "Jose, did you have formal training or are you self—-"

    show Segunda at semileftS
    with easeinleft
    with None
    S "EVERYONE!!!" with hpunch

    "The group turned their attention to Segunda in sync."

    S "I don’t think Jose could concentrate with his drawing when there are people surveying his every move."
    S "I heard artists get anxious and make more mistakes in the process."

    "The three looked at me."

    MAR "Why didn’t you say so?"

    hide Lola
    with easeoutleft
    with None

    hide Manuel
    with easeoutright
    with None
    "{i}\“But I did, you weren’t listening\”{/i}, They backed away and decided to settle at a nearby table just a couple of meters away. "
    "My lola called one of her helpers to prepare merienda. Mariano looked at me before he sat on the chair."

    MAR "Don’t embarrass me when I vouched for you."

    hide Mariano
    with easeoutright
    with None
    "Segunda rolled her eyes at her brother's statement. I found her reactions interesting, not removing my gaze from her."
    "I wanted her to look at me…and she did just that. I mouthed a ‘thank you’. Segunda smiled shyly, tucking a stray strand of hair and nodding. I frowned."

    S "Oh, I’m sorry. Did I move too much?"

    stop ISketch
    JR "No, no. It’s fine. Maybe if you could just adjust the angle a little bit. Can you turn a little to the left?"

    S "Like this?"

    JR "No, that’s too much."

    S "What about now?"

    JR "No…"

    play WalkWood4 "audio/Voice/WalkWood4.mp3"
    "I stood up, leaving my art materials on top of my chair and walked toward Segunda. I motioned both of my hands in an angle that Segunda could follow."

    S "Now?"

    JR "Okay, that’s better. Wait…"

    "I noticed a section of hair dangling from her shoulder. Out of place. Distracting. I raised my hand in an attempt to get it out of the way but I hesitated."

    hide Segunda

    menu:
        "Tuck her hair away":
            jump C4_yes

        "Leave it be":
            jump C4_no

    label C4_done:

    #STOP SOME UNNECESSARY SFX######
    stop WalkWood4
    #STOP SOME UNNECESSARY SFX######
    #+++++++++   SCENE 6 BOI   +++++++++++++++++++++++++++++++++++++++++++Pages 14-18  of the Script++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    scene bgLV
    stop music
    play music "audio/Music/Almost New.mp3" loop
    show Segunda at semileftS
    with fade
    with None

    # For hiding unnessary characters
    hide Manuel
    # For hiding unnessary characters
    play ISketch "audio/Voice/ISketch.mp3"
    "A couple of minutes has passed since I embarrassed myself in front of Segunda. I have since adopted a very serious facade, one molded to impress. "
    "My lola, Mariano and Manuel were busy chatting over the table to give us attention."


    S "So, uhm…"

    JR "Hmmm…?"

    S "Are you with a lover?"

    stop ISketch
    play SnapPen "audio/Voice/SnapPen.mp3"
    "The lead of my pencil snapped."

    JR "A what?"

    S "Do you have a lover?"

    "I became increasingly aware of my heartbeat. {i}\“What does she mean, do I have a lover?\”{/i}. "

    play PenCase "audio/Voice/PenCase.mp3"
    "I looked at the broken lead of my pencil and rummaged through my satchel for my sharpener."

    JR "No, never."

    "I kept rummaging through my satchel, avoiding eye contact."

    S "Oh… I wonder why."

    JR "I’m not very smart or tall or rich or even handsome you see."

    stop PenCase
    "I gave up. I must have left my sharpener on top of my desk. {i}\“Could this day get any worse?\”{/i}"
    "To embarrass myself because of my presumptuousness is one thing, Segunda finding out that I was a sore loser for not having had lovers is mortifying."
    "I looked at my sketchbook and frowned."

    S "Is it done?"

    JR "…perhaps?"

    S "Perhaps?"

    JR "My pencil broke…and it’s not my best work so…"

    S "Can I take a look?"

    play RipPage "audio/Voice/RipPage.mp3"
    "I ripped the page as carefully as I could and showed it to Segunda."

    S "I don’t understand…"

    "I suddenly felt nervous. Did she not like the drawing after all?"

    JR "What?"

    S "You said this isn’t your best work. Are you perhaps jesting? Because this looks beautiful."

    "I was surprised at the positive reception. I wasn't sure whether Segunda said that out of sheer kindness or if she just wasn’t as exposed to great art the way I was. "
    "Nevertheless, I was glad Segunda somehow appreciated it."

    show Mariano at semirightMar
    with easeinright
    with None
    MAR "Yep. This definitely isn’t your best work."

    S "Kuya Mariano!"

    MAR "What? It’s true. I look prettier than you in the portrait he drew and I’m supposed to be the less-attractive sibling."

    S "Kuya, are you insinuating that all along my appearance was rather deficient?"

    MAR "What? No! Where did you get that?"

    S "You just said that you were prettier than me!"

    MAR "You misunderstood, sister. That’s not what I meant!"

    S "I heard you clearly!"

    JR "My lady! Please! Don’t get angry at Mariano."

    "They halt their squabble as they turned their attention to me, silently pressuring me to continue."

    JR "I-it was my lack of skill that he was criticizing. I promise to hone my skill so I would be someday worthy of your praise."

    "I looked at Segunda, meaningfully."

    JR "And…there is absolutely nothing deficient about your appearance. Nothing."

    "Both Segunda and I blushed at the admission. I had the sudden urge to strap myself to a chair and stuff a dirty cloth inside my mouth."
    "I deserved such treatment. How low could I possibly be, admitting that I found an engaged girl attractive and right in front of her brother and fiance."
    "Mariano didn't seem to mind though, in fact he looked downright unaffected. Maybe I was putting too much meaning on things that should be taken at face value."

    show Manuel at rightMan
    with easeinright
    with None

    play GrabPage "audio/Voice/GrabPage.mp3"
    "Manuel grabbed the drawing and inspected it."

    MAN "Hmmm…Mariano, I don’t know what you’re talking about. This seems good for what was drawn in such a short time."

    MAR "I complimented him! He could do better because I’ve seen it. Dios Mio, people keep on misinterpreting me."

    S "It would do you good to think before you utter your words, kuya. Just a suggestion though."

    "Segunda plastered a sarcastic smile and crooked her head sideways. Mariano glowered at her."

    show Lola at leftLol
    with easeinleft
    with None
    L "Apo, Segunda. Have some merienda while it's still warm."

    "My lola ushered the both of us to take a seat."

    L "Your drawing turned out fine, apo. No one in this universe would be able to draw the same way you do."

    "She patted my shoulder and offered me a sweet smile, which I also returned. I was reminded of why I continued to do what I do. "
    "It's because people believe in me and that is enough reason to keep me going."

    #STOP SOME UNNECESSARY SFX######
    stop SnapPen
    stop RipPage
    stop GrabPage
    #STOP SOME UNNECESSARY SFX######
    #+++++++++   SCENE 7 BOI   +++++++++++++++++++++++++++++++++++++++++++Pages 18-21  of the Script++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    scene bgAZ
    stop music
    play music "audio/Music/Tango de Manzana.mp3" loop
    with fade
    with None

    # For hiding unnessary characters
    hide Segunda
    hide Mariano
    hide Manuel
    hide Lola
    # For hiding unnessary characters

    play Chess "audio/Voice/Chess.mp3"
    "Mariano, Segunda and my lola were at the side of the room drinking coffee and talking. I sat facing Manuel, a chessboard between us."
    "I was initially determined to beat my opponent. What with the previous disaster that was a week ago, I was set on making up for my foolishness."
    "But with the way things are, it looked like I would have to deal with the short end of the stick once again. Manuel was relaxed in his chair. "
    stop Chess
    play TapFoot "audio/Voice/TapFoot.mp3"
    "I impatiently tapped my feet on the wooden floor."

    show Manuel at leftMan
    with easeinleft
    with None
    MAN "We still have plenty of time."

    "I glanced at him and immediately shifted my focus back at the chessboard. {i}\“He’s good, he’s plenty good\”.{/i}"

    play ChessS "audio/Voice/ChessS.mp3"
    "I made my move. Manuel tried his best to control the slight tug forming on the corner of his mouth. "
    play ChessM "audio/Voice/ChessM.mp3"
    "I knew I did terribly. Manuel moved his piece. Mariano stood beside the chessboard."

    show Mariano at semirightMar
    with easeinright
    with None
    MAR "You look like you’re in a tight spot there, mate."

    JR "Oh hush Mariano, I’m concentrating."

    "Mariano shrugged."

    show Lola at rightLol
    with easeinright
    with None
    L "Looks like we’re running out of snacks. Segunda, dear. Can you accompany me to the kitchen?"

    "Segunda nodded and set her cup on the table. She looked at my direction and found me looking at her too. "
    "We both turned away quickly. I was met with Manuel’s knowing smile. I tensed up."

    hide Lola
    with easeoutright
    with None
    MAR "Oh, I’ll go too!"

    show Segunda at rightS
    with easeinright
    with None
    S "You just want to see Rosario."

    MAR "What? No, of course not."

    hide Mariano
    hide Segunda
    with easeoutright
    "Their voices faded. I focused on the chessboard and pretended as if Manuel didn’t just catch me exchanging looks with his fiancee."

    MAN "It looks like you’ve gotten closer with Segunda."

    "I tried my best to not look bothered, or nervous for that matter."

    JR "We’re friends."

    MAN "I can see that."

    play ChessS "audio/Voice/ChessS.mp3"
    pause (0.5)
    play ChessM "audio/Voice/ChessM.mp3"
    "We move our respective pieces. The game was getting tougher."

    MAN "Segunda is a nice girl and I’m happy to see her gain new friends."

    JR "I’m glad to hear that."

    "An uncomfortable silence ensued. Manuel shatterd it just as quickly as it materialized."

    MAN "When I was your age, I did plenty of things that could potentially threaten the family honor. In secret, of course. The Katigbaks have no idea."

    "Manuel chuckled. I had no idea how to react to that."

    MAN "I’ve long since learned my lesson and decided that if you have no better use of your time, the best course of action is no action at all."

    play ChessM "audio/Voice/ChessM.mp3"
    "I had no idea where this conversation was heading which made me more anxious by the minute. Manuel moved his chess piece."

    MAN "You know of my relationship with her, right?"

    JR "Yes."

    MAN "Then you know that it is my responsibility to look out for her for any potential…concerns."

    play ChessS "audio/Voice/ChessS.mp3"
    "I hummed in acknowledgement, hovering my hand over a chess piece. Manuel observed my movements."

    MAN "Think about how your single move could affect the outcome."

    show cgMC
    with fade
    with None
    "I paused and looked at him. Manuel didnt look angry or even frightening for that matter. He gestured for me to go ahead."

    play ChessS "audio/Voice/ChessS.mp3"
    "I moved my chess piece. Manuel smiled, a wide smile. Almost sinister. He moved his piece. "
    "I inspected the chessboard even further, wondering where I could possibly go wrong. {i}‘There it is’{/i}"
    "I was now able to see the whole picture. I couldn't believe I got myself caught in Manuel’s web. "
    "I seriously thought I could see the game through to the end with only minor setbacks. {i}‘Why did it take me so long to see it?’{/i}"
    "It's as if I was hit with the force of a sledgehammer."

    "Manuel was playing the waiting game all along. "
    "With his level of skill he could have destroyed me in a matter of a few moves but he chose to wait and strike me down when I was most vulnerable."
    "Manuel planned to trap me from the start. I was now surrounded and any movement from my side would ultimately cost me my queen. "
    "I could feel a rising panic from the depths of my stomach. How cruel."
    hide cgMC
    with fade
    with None

    show Segunda at rightS
    with easeinright
    with None
    S "We’re ba–"

    JR "I concede!" with hpunch

    "Everyone was surprised by my outburst. Including myself."

    JR "...I– I concede…"

    "Manuel offered an understanding smile. He raised his hand for a handshake and I accepted."

    MAN "It was a good game, Jose. It was the most entertaining game I played in a while."

    JR "Yeah, haha…I’m glad to be of service…"

    "Segunda offered the both of us a mug of warm coffee. The kind gesture was enough to make me feel at ease."

    MAN "I talked to Jose. He would make a good friend."

    "Segunda tensed up in alarm."

    S "What did you tell him? Manuel, tell me at once."

    hide Manuel
    hide Segunda
    with easeoutleft
    with None

    show Mariano at rightMar
    with easeinright
    with None
    "Manuel walked inside the house, teasingly ignoring Segunda's pleas. Mariano patted me on the shoulder in an attempt to comfort me."

    MAR "He’s good, huh?"

    JR "Better than I expected. He can also be quite…scary."

    MAR "Ahhh, yes. Manuel likes his games. Especially his mind games. That’s why father likes him. "
    MAR "He knows how to deal with his cards. Says he’s the most suitable candidate to continue the family legacy. Kinda stings, to be honest."

    "I patted him on the back in return. It was quite laughable, my attempts to keep the queen when I was doomed from the very start. "
    "Manuel isn’t someone people should cross and he made that clear. All I knew is that I refuse to be a pawn in Manuel’s game of chess."

    #STOP SOME UNNECESSARY SFX######
    stop TapFoot
    stop ChessS
    stop ChessF
    stop ChessM
    #STOP SOME UNNECESSARY SFX######
    #+++++++++   SCENE 8 BOI   +++++++++++++++++++++++++++++++++++++++++++Pages 21-25  of the Script++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    scene bgLV
    stop music
    play music "audio/Music/Easy Lemon.mp3" loop
    with fade
    with None

    # For hiding unnessary characters
    hide Mariano
    # For hiding unnessary characters


    "I wasn’t able to shrug the feeling of anxiety from the events that transpired last week. "
    "Actually, every week since I met Segunda. I wonder when did I pick up embarrassing myself as a hobby."
    "I started slipping, and stumbling, and spilling. So unlike the calm and composed character I carefully constructed."
    "While Segunda made me nervous in a mildly acceptable way, Manuel was just plain terrifying. "
    "It was less a judgment on his character but more of him being able to see straight through me that terrified me the most."
    "That cruel game of chess I had with him was enough to make me re-evaluate my decisions. "
    "And so, for the sake of preserving my honor and integrity, I decided to block any intrusive thoughts of sweet Segunda."

    play CarriageS "audio/Voice/CarriageS.mp3"
    "Mariano and I were busy playing cards when we heared the sound of a carriage. "

    stop CarriageS
    play DoubleDoor "audio/Voice/DoubleDoor.mp3"
    play WalkWood5 "audio/Voice/WalkWood5.mp3"
    "I steeled my nerves. The double doors opened and Segunda walked in. A bright smile on her face."

    show Segunda at leftS
    with easeinleft
    with None
    S "I brought pancit."

    show Mariano at rightMar
    with easeinright
    MAR "About time you arrived. Where is it?"

    "Mariano got up from his seat, leaving me to focus on the cards in my hands. I cowered, afraid I’d be greeted by hostility from the tall fiancee."

    S "Greetings to you too, dear brother. What a way to spoil this pleasant afternoon with your rough manners."

    MAR "I don’t see the pancit. And I don’t see anyone with you. Did you come here alone?"

    S "It’s with Rosario. I asked her to bring it to the kitchen."

    "Segunda smiled at Mariano teasingly."

    S "And Manuel wasn’t able to accompany me. He had urgent business to attend. So it’s just me and Rosario and the pancit."

    "My ears perked up. My shoulders dropped, releasing the tension. Mariano walked away leaving the two of us alone."

    MAR "I’ll go look."

    S "For Rosario?"

    MAR "For the pancit."

    hide Mariano
    with easeoutright
    with None

    play GirlChuckled "audio/Voice/GirlChuckled.mp3"
    "Segunda laughed. I wondered when was the last time this house had heard something so pure in its joy. "
    "If I could, I would greedily bottle it up and save it for all the times I felt remotely depressed."
    "I was on the verge of losing my mind."

    "She scanned the room and her attention landed on me. I was in the process of assembling the cards back into the deck. "
    "I looked at Segunda and smiled at her. Controlled. Just enough to make her feel less awkward in my presence. "
    "The hours we spent in each other's company weren’t enough to dissolve our inhibitions."

    JR "Cards?"

    play ShufCard "audio/Voice/ShufCard.mp3"
    "Segunda returned the smile, taking it as an invitation to sit down. I shuffled the deck as skillfully as I could. "
    "At last, a moment alone with her. And no Lola, Mariano or Manuel on sight. Just me, Segunda and her pretty smile."

    stop ShufCard
    "She picked one card after another with her hands. Shapely, fine, almost delicate. The kind that was never subjected to any sort of manual labor. "
    "I idly wondered what it would feel like to touch it, hold it, intertwine it with mine. I mentally shook myself, recognizing the error of that thought. "
    "I had pledged that I would not entertain any intrusive thoughts regarding Segunda and so far, I was doing a terrible job of preventing it."

    play ScatCard "audio/Voice/ScatCard.mp3"
    "I may have tossed a card with a little more force than necessary. It fell off the table and landed on the floor. "
    "Segunda reached for the card but I was quick to offer help."

    JR "My lady, let me-"

    S "Oh no, it’s fine-"

    show cgCTH
    stop music
    play music "audio/Music/Promises to Keep.mp3" loop
    with fade
    with None
    "We both end up on the floor, reaching for the card at the same time. Our heads were just a hair's breadth apart. Segunda’s fingertips grazed my knuckles."
    "I became increasingly aware of Segunda’s presence. "
    "The smell of her perfume, the stray hair that dangled on the foreground of my vision, the rhythm of her breathing, the warmth emanating from her fingertips. "
    "I never intended to enter her personal space."

    hide Segunda

    menu:
        "Turn Away":
            jump C5_yes

        "Look At Her":
            jump C5_no

    label C5_done:

    hide cgCTH
    show Segunda at leftS
    with fade



    JR "I-I apologize-"

    "I slowly withdrew my hand but Segunda took hold of it, wholly. The certainty of it overwhelmed me; I almost wanted to cry."
    "I snapped my head up at her, and just like that, I cast aside my doubts and fears and relished in Segunda."
    "Her eyebrows kept twitching ever so slightly. I don’t know if she’s fighting against it, lips pressed in a thin line, eyes begging me to understand."
    "I didn’t know how to make sense of her expression whether it is of determination or of hurt or something else entirely. "
    "Whatever it was, it completely dismantled any defenses I had built in the name of reason."

    JR "I need you to tell me to stop."

    "I had fought with arrogant professors, competitive classmates and overly-aggressive fencing opponents. I always came prepared, equipped with the finest armor I could assemble. "
    "But not once had I ever felt so raw and exposed and... defenseless."
    "Segunda took a sharp inhale of breath and I braced myself for the revelation."

    S "I-"

    show Mariano at rightMar
    with easeinright
    MAR "I found the pancit! But I couldn’t find Rosario. I was about to ask her to-" with hpunch

    "Mariano spotted us on the floor. Quite a distance apart."

    MAR "Uh…What are you two doing?"

    S "Picking up cards…It got blown by the wind."

    "Mariano looked at me curiously."

    JR "Right. Troublesome wind…"

    MAR "Okay…? Segunda do you know where Rosario could possibly be? The pancit has gone cold."

    S "Oh, Mariano, why don’t you look with your eyes instead of your mouth?"

    MAR "What’s {i}your{/i} problem?"

    hide Mariano
    hide Segunda
    with easeoutright
    with None
    "They both walked away. I sat down. It took me quite a while to process everything that transpired. "
    "I felt…lighter. I didn’t think my pent up romantic frustrations were weighing me down."
    "Mariano’s unwelcome interruption actually saved me from doing something that would have cost me my spot in the family tree."
    "I could finally breathe. The sun didn’t seem so much as a bother and the sky appeared a more vibrant shade of blue. "
    "There was nothing fogging up my vision anymore."
    "I was still afraid but honestly, it felt good. The pleasure rooted from rebellion. "
    "I had enough of lying to myself and hiding behind honor, integrity and being chained to familial expectations. I welcomed the surge of emotions I'd tried so hard to subdue."
    "I was hopelessly in love with an engaged woman. And I finally let myself admit it."

    #STOP SOME UNNECESSARY SFX######
    stop DoubleDoor
    stop WalkWood5
    stop GirlChuckled
    stop ScatCard
    stop ShufCard
    #STOP SOME UNNECESSARY SFX######
    #+++++++++   SCENE 9 BOI   +++++++++++++++++++++++++++++++++++++++++++Pages 25-28  of the Script++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    scene bgBR
    stop music
    with fade
    with None

    "It was a hot sunny day when I skipped down the stairs of my family home."
    "Just as I was about to take a left turn from the hallway, I heard something from Paciano’s room. The door was left slightly ajar, and I caught a glimpse of my brother conversing with a stranger."
    "I should probably get going already… but the curiosity burned in me to know what Paciano was up to."

    menu:
        "Evesdrop on them":
            jump C6_yes

        "Leave it be":
            jump C6_no

    label C6_done:


    scene bgDN
    with fade
    with None

    # For hiding unnessary characters
    hide Paciano
    # For hiding unnessary characters

    "Reluctantly, I made my way back to the kitchen where the rest of my family were dining at the table, the smell of eggs and pan de sal waking me up immediately. "

    play TummyRum "audio/Voice/TummyRum.mp3"
    "I felt my stomach grumble." #grumbling stomach sound effect
    "My father caught my eye and waved his hand towards an empty seat."

    show Francisco at leftF
    with easeinleft
    with None

    play music "audio/Music/Almost New.mp3" loop

    F "It’s about time you finally woke up! Come on, eat something before you go to school."
    hide Francisco
    with easeoutleft
    with None

    play BTable "audio/Voice/BTable.mp3"
    "I took a seat in between Saturnina and Olimpia. In front of me was a plate of rice and tocino with eggs. "
    "I hadn’t realized how hungry I was until I finally took a bite."
    "The sweetness of the tocino bursts in my mouth and I sighed. The youngest, Soledad, raised her hands excitedly as she talked with Olimpia and Saturnina."

    show Soledad at rightSOL
    with easeinright
    with None
    SOL "–And now that you and Olimpia are in the same school as me, I won’t have to worry about those stupid bullies bothering me anymore. I’ll tell them that you’ll beat them up."

    "Saturnina rolled her eyes fondly."

    show Saturnina at leftSAT
    with easeinleft
    with None
    SAT "We’re probably going to be in different classes anyway so I don’t think we’ll be able to see each other except for in between breaks. "
    SAT "I don’t want to hear any complaints from the teachers that you’re starting trouble, understood?"

    SOL "Whatever. You’ll help me if I asked you to, right {i}kuya?{/i}"

    JR "Huh? Sure. You’re all going to Concordia now, right?"

    SOL "Yep!"

    hide Soledad
    with easeoutright
    with None

    hide Saturnina
    with easeoutleft
    with None

    "Olimpia shifted uncomfortably beside me."

    show Olimpia at leftOLI
    with easeinleft
    with None
    OLI "I-I don’t know anyone there. You’ll really come to visit us sometimes?"

    JR "Of course. If you’re worried about making friends, I know someone whose sister goes to school there too. In fact, I think she’s around the same age as you are."

    "Olimpia’s face brightened immediately."

    OLI "Really? Thank you, Kuya!"

    "I nodded genially at my sister, the pleasant expression on my face hiding the worry that gnawed inside me."
    "The grim conversation I overheard in Paciano’s room… I wasn’t even supposed to be there at the time, so I couldn’t confront my brother about it without admitting that I was eavesdropping."
    "I wasn’t ignorant. I knew that there were groups that entertained a revolutionary aim, and I wasn’t sure what to think about it. "
    "While I did agree with the premise that the Spaniards were a parasitic force that oppressed the Filipinos, I wasn’t sure if it was really a good idea to go against them directly."


    "My thoughts darkened as I remembered my poor mother being dragged through the streets—- all for daring to disrespect our masters. "
    "If it wasn’t for my sister appealing to the Governor-General, our mother would’ve continued to rot in jail."
    "The idea of being at the mercy of the whims of an external force brought a bitter taste to my mouth, like my entire body was rebelling against the thought."
    "But if keeping my head down meant I could live a normal life without any trouble… How bad could it be? It’s not like I could take up a gun and shoot my way to victory. "
    "Things weren’t simple like that, and I was no Isidro."
    "I just didn’t know what to think, except that I hoped Paciano wasn’t going to get himself killed."

    #STOP SOME UNNECESSARY SFX######
    stop BTable
    stop WalkWood6
    stop WalkWoodStop
    stop TableBang
    stop TummyRum
    #STOP SOME UNNECESSARY SFX######
    #+++++++++   SCENE 10 BOI   +++++++++++++++++++++++++++++++++++++++++++Pages 28-30  of the Script++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    scene bgDR1
    stop music
    play music "audio/Music/Easy Lemon.mp3" loop
    with fade
    with None

    "It was another sunny afternoon but this time, I welcomed the heat. Olimpia sent me a letter days ago, going over the events of the past week."
    "My sister hadn’t fully adjusted yet but I was glad to hear that she’s coping better than expected. She ended it with a request to pay her a visit on visiting day."
    "I obliged, a little more excited than I would dare admit. I was on my way to see Olimpia but the excitement came from knowing that ‘she’ would be there too."

    show Mariano at leftMar
    with easeinleft
    with None
    MAR "I’m not very thrilled to see my sister…what about you?"

    hide Mariano

    menu:
        "Yes":
            jump C7_yes

        "No":
            jump C7_no

    label C7_done:

    scene bgCdC
    with fade
    with None

    # For hiding unnessary characters
    hide Mariano
    # For hiding unnessary characters

    "We arrived at our destination. The nuns ushered us to the waiting area and we sat, taking in the scenery. "
    "I thought about what Mariano said, about me being a great brother."
    "I had intended to see my sister and yet, it wasn’t her that I looked forward to. It wasn’t her that made my heart beat in sheer excitement. "
    "It wasn’t her that made me feel at home."
    "I felt bad for Olimpia, she didn’t deserve a brother that put his romantic life first before family."

    play BRang "audio/Voice/BRang.mp3"
    "The bell rang and the students slowly filled the corridors. I stood by, watching out for my sister’s familiar face."

    "Olimpia came into view. "
    "And for whatever reason, I didn’t care as much as I should even if I forced myself to, "
    "Because it was ultimately the girl behind her that made my lungs constrict, my knees weak and my stomach a dwelling for butterflies."
    "I didn’t know it was remotely possible for her to look even more attractive than the last time I saw her."
    "{i}She’s too much.{/i}"

    show Olimpia at leftOLI
    with easeinleft
    with None
    OLI "Kuya! You came to see me."

    JR "Of course, how could I not when you basically harassed me to come?"

    OLI "You exaggerate. You don’t know how glad I am to see you."

    "Olimpia engulfed me in a big hug. Instead of bringing comfort, it made me feel worse."

    hide Olimpia
    with easeoutleft
    with None

    show Mariano at rightMar
    with easeinright
    with None
    MAR "Segunda…dear, how are you faring?"

    show Segunda at semileftS
    with easeinleft
    with None
    S "I am fine, brother."

    "Mariano hummed in response. Segunda turned to me and smiled in greeting. Mariano eyed the girl beside Segunda."

    MAR "And who might this be?"

    S "Kuya, Jose. This is our friend, Ysabel."

    show Ysabel at leftYSA
    with easeinleft
    with None
    YSA "Greetings."

    "She stood tall with quiet confidence and eyes that could turn anyone to stone. She seemed like the type that had better things to do elsewhere and wouldn’t spare Mariano the time of the day."
    "Someone out of his league. It only took Mariano one good look at her to decide she was definitely his type."

    MAR "Mariano. Son of Don Norberto, the Gobernadorcillo of Batangas. Potential heir to the renowned Katigbak Clan. Segunda’s favorite sibling. "
    MAR "And this is Jose, but he isn’t as interesting as I am. May I?"

    "Mariano offered his hand and plastered on his best smile which unfortunately resembled a smiling donkey more than a handsome person. Ysabel accepted and Mariano kissed her hand."

    YSA "Isn’t he supposed to talk about his personal achievements outside of being born to the right family?"

    S "That’s because he doesn’t have any. Let’s move to the sheds, the weather isn’t as hot there as it is here."


    #STOP SOME UNNECESSARY SFX######
    stop BRang
    #STOP SOME UNNECESSARY SFX######
    #+++++++++   SCENE 11 BOI   +++++++++++++++++++++++++++++++++++++++++++Pages 30-34  of the Script++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    scene bgCdC
    with fade
    with None

    # For hiding unnessary characters
    hide Mariano
    hide Segunda
    hide Ysabel
    # For hiding unnessary characters

    "I found myself quite detached from the conversation that ensued. The group had already established chemistry and I felt so much like a transferee. Like I didn’t belong in this class."

    show Segunda at leftS
    with easeinleft
    with None
    S "Are you okay?"

    JR "Yes. I’m good."

    S "You’ve been quiet…"

    "I just smiled in response. I didn’t want to blame Olimpia for dampening my mood. "
    "After all, it was my doing. Olimpia hugging me just reinforced the idea that I am, in fact, a terrible brother."
    "I wished Paciano was nearby, I needed his brotherly advice more than ever."
    "It wasn't clear if Paciano would have empathized with my predicament because as far as I knew, Paciano has never had a lover. "
    "But I didn’t care, I just wanted someone to vent to…Did Paciano ever have a lover?"

    show Mariano at rightMar
    with easeinright
    with None
    MAR "Jose here is a writer. He’s won several essay writing contests in school. Tell us your writing process, Jose."

    JR "Um, there isn’t much to tell…"

    MAR "You always say that. Come on, tell us."

    JR "Well, you just have to read lots and the words will keep on spilling."

    S "Tell us about your favorite books."

    "I thought about all my favorite books that would appeal to my favorite girl. I wanted to say Count of Monte Cristo to appear smart but perhaps it was too vengeful for her taste?"
    "I scrambled my mind for more options. A collection of poems? Mythologies? Short stories? I finally narrowed my choices down to one."
    "A light read about a boy who fought monsters and dragons and sailed through deathly seas, who faced whatever trial the universe threw at him just to meet the girl of his dreams."

    play BRang "audio/Voice/BRang.mp3"
    "We talked about books with the remaining time we had. The clock struck seven and it signaled a farewell. Olimpia approached me."

    hide Segunda
    with easeoutleft
    with None

    hide Mariano
    with easeoutright
    with None

    show Olimpia at leftOLI
    with easeinleft
    with None

    stop music
    play music "audio/Music/SCP x6x Hopeful.mp3" loop
    OLI "Kuya, there’s something I wanted to ask…"

    JR "What is it Olimpia?"

    OLI "Do you have any idea what Kuya Paciano is up to?"

    "I internally cursed Paciano for not being discreet."

    JR "…I don’t think I follow…?"

    OLI "You see, mother sent Saturnina a letter. The frequencies of Kuya Paciano’s ‘nightly ventures’ have increased at an alarming rate. Mother is worried he might be…"

    JR "Might be...?"

    "I tensed. I wished Paciano would just abandon whatever underground group he is in."

    OLI "He might be indulging in a tryst."

    "It took me a bit to process the information. Huh, so I was anxious for nothing. Kuya Paciano? Meeting a potential lover at night?"

    JR "Are we talking about the same Kuya Paciano here?"

    OLI "See, even you find it unbelievable."

    JR "I don’t think that’s a cause for concern Olimpia. It is much more concerning that Kuya Paciano is past marriage age with no clear prospects in sight."

    OLI "That’s the thing. Kuya Paciano has no space for romance in his heart. What sort of love was offered for him to embark on nightly trysts."

    JR "What Kuya Paciano does is none of our business. He’s old, he knows what he’s doing."

    hide Olimpia
    with easeoutleft
    with None

    "I closed the conversation. Whatever it was that Paciano was up to should not involve our family."
    "I just wished Paciano really does know what he’s getting himself into. We bid each other farewell. But before departing, I took the chance to thank Segunda."

    JR "Segunda!"

    show Segunda at leftS
    with easeinleft
    with None
    S "Yes?"

    JR "I would like to say thank you. For taking care of my sister. She was afraid she’d be left alone but you made her feel like she belonged. Thank you."

    S "I was merely being friendly. She'd fit in just fine even without me."

    JR "Still…Um, I’ll see you again?"

    S "Yes. May the universe conspire and make way for our next meeting, Jose."

    JR "I’ll have the universe at my mercy, Segunda."

    "Segunda smiled shyly. She seemed like she had something else to say."

    JR "Is there…anything else?"

    S "Can you give me your hat?"

    show cgPRH
    with fade
    with None
    "I obliged, wondering what Segunda could possibly do with my hat. She revealed a white paper rose hidden underneath her shawl, placing it in the band of my hat."
    "She put my hat back on my head, admiring the stark contrast between black fabric and white paper. Her eyes scanned her work and went down to meet mine."
    "She didn’t realize she had stepped in so close. I was sure that I was the color of a tomato and Segunda had seen me the same way I had seen her, red."
    hide cgPRH
    with fade
    with None

    S "Goodbye."

    hide Segunda
    with easeoutleft
    with None

    play BriskWalk "audio/Voice/BriskWalk.mp3"
    "Segunda turned her back and walked away briskly. I stood there stunned, taking it in. "
    "A tug slowly formed on the corners of my lips. I bit back a full smile. What did they call it again…{i}kilig?{/i} "
    "Mariano appeared at my side."

    show Mariano at leftMar
    with easeinleft
    with None
    MAR "No matter what happens, we have to be here every visiting day."

    "I agreed. I just have to sort out my feelings and get rid of the guilt eating me whole. I noticed a paper rose on Mariano’s breast pocket."

    JR "I thought you liked Rosario?"

    MAR "I do, but with Ysabel…its something else. I have to see where this takes me."

    "I had no objections, convinced that the paper rose was a development of sorts. Just like Mariano, I had to see it through to the end."
    "That night, I slept with a huge smile on my face and in my dreams, I obsessed over the meaning of roses the color white."

    #STOP SOME UNNECESSARY SFX######
    stop BRang
    stop BriskWalk
    #STOP SOME UNNECESSARY SFX######
    #+++++++++   SCENE 12 BOI   +++++++++++++++++++++++++++++++++++++++++++Pages 34-37  of the Script++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    scene bgEC
    stop music
    play music "audio/Music/Easy Lemon.mp3" loop
    with fade
    with None

    # For hiding unnessary characters
    hide Mariano
    # For hiding unnessary characters

    play Market "audio/Voice/Market.mp3"
    play HCarriage "audio/Voice/HCarriage.mp3"
    "I found myself venturing the busy streets of Manila. "
    "On any normal day, I would’ve chosen to stay indoors and study but I couldn’t brush off the memory of Segunda and the paper roses I had hidden inside my desk drawer."
    "I thought it would only be proper to get her a gift in return. And what better place to find her one than in the shopping district?"
    "I turned to the other direction away from the scent of meat products. "
    "This area was lined with small shops selling from various selections of pastries, breads and local delicacies all the way to fabrics, accessories, and basic household necessities."
    "I was scanning the shops when I noticed a tall figure being pestered by a Chinese vendor."

    show Vendor at leftVEN
    with easeinleft
    with None
    VEN "You buy three, three textiles for only twenty pesos, eh? Good deal."

    show Manuel at rightMan
    with easeinright
    with None

    stop music
    play music "audio/Music/Tango de Manzana.mp3" loop
    MAN "I don’t need it…"

    VEN "I tell you a secret, this textile was from Ming Dynasty passed by ancestors. It’s rare edition but I sell it to you cheap. Good deal, eh?"

    MAN "Uhhh…I’ll pass."

    VEN "This is very popular with the ladies. You have wife? Your wife love you more if you give her these. Eh? Eh?"


    "Manuel sighed and gave the vendor twenty pesos. The vendor jumped in delight and went away. Manuel examined the textiles."

    hide Vendor
    with easeoutleft
    with None

    JR "You know you were scammed, right?"

    "A couple of weeks ago, I wouldn’t have been able to talk to Manuel in that tone. "
    "The word ‘wife’ and the idea of Manuel buying supposed wife a present triggered me enough to cast aside etiquette. Manuel turned around."

    MAN "Jose, what a surprise. It’s good to see you."

    "I ignored him on purpose and stepped closer to inspect the textile. It’s pretty, woven with intricate designs and the colors complement each other perfectly."
    "I would have bought the same exact present regardless of the lie if only I had a spare twenty pesos lying around."
    "I was filled with a sudden inexplicable rage at my current financial situation compared to Manuel’s. He’s tall, rich and is engaged to the girl of my dreams."
    "Manuel’s face never looked so punchable before."

    JR "That’s not from the Ming Dynasty."

    "Surely, Segunda’s fiance can’t be {i}this{/i} stupid"

    MAN "I know."

    "Manuel tried to suppress his laughter which irritated me even more."

    JR "Then why did you buy it? "
    JR "I know you have expendable amounts of cash sitting in your drawers but its unfair to gift Segunda something bought out of a lie as ridiculous as a textile passed down from the Ming Dynasty."

    "..."
    "Too late I realized my mistake. I should have taken hold of my emotions."

    MAN "Jose, I know you’re {i}good friends{/i} with my fiance and I like that you care for her. But I didn’t plan on giving these to her so you don’t have to be so angry."

    "I stepped out of bounds. I shouldn’t have said that."

    MAN "And to answer your other question, I do have expendable amounts of cash which is precisely why I willingly bought into his {i}ridiculous{/i} lie. Because he needs the money more than I do."

    "That completely shut me up. I felt a mixture of rage and jealousy at the fact that Manuel is tall, rich, engaged to the girl of my dreams and is now a better human being than I am. "
    "Life is unfair."

    JR "You could have just ignored him instead of getting yourself scammed."

    MAN "How could I when he called me handsome?"

    #STOP SOME UNNECESSARY SFX######
    stop Market
    stop HCarriage
    #STOP SOME UNNECESSARY SFX######
    #+++++++++   SCENE 13 BOI   +++++++++++++++++++++++++++++++++++++++++++Pages 37-43  of the Script++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    scene bgCF
    with fade
    with None

    # For hiding unnessary characters
    hide Manuel
    # For hiding unnessary characters

    play CrowdChatter "audio/Voice/CrowdChatter.mp3"
    "I was seated right across Manuel, a cup of freshly brewed coffee in front of me. Very much hot."
    "Manuel invited me to a nearby cafe he frequented. He offered to pay of course or I would have declined him otherwise. I only had enough money for a gift and a ride to my boarding house."
    "I looked at Manuel examining the textile. I was reminded of our conversation before I got invited to coffee."
    "The vendor called him handsome."

    "Manuel was everything that I wasn't. It made me want to grab the mug and splash its contents on Manuel’s face just to see if he’s still handsome after that."
    "I was aware that it was all just a marketing strategy, just a tool scammers use for their targets to concede but that still sent violent, savage urges pulsing through my veins."
    "I took a sip of my coffee. Bitter. Just like me."

    show Manuel at leftMan
    with easeinleft
    with None
    MAN "So Jose, what are you here for?"

    JR "Oh, just looking for a present."

    MAN "A present? I’m good with selecting presents. I can help you with that."

    "I thought about the offer. No one knew Segunda better than her fiance considering that Mariano wasn’t much of a help. "
    "I took a moment to weigh my options."
    "On one hand, I didn’t want Manuel to find out that I took time off my schedule just to look for a present for his fiance, it would seem disrespectful to their relationship."
    "On the other hand, I wanted to disrespect him and gloat about Segunda presenting me with a paper rose."

    JR "Actually…it’s for Segunda."

    "Manuel looked surprised. That reaction was enough to satisfy me."

    MAN "Oh? I don’t think Segunda’s birthday was right around the corner."

    JR "It’s not a birthday present. You see…Segunda gave me paper roses that she made herself. "
    JR "I thought it would be appropriate to give her something in return. As thanks…"

    "I made sure to study every stretch and tension in his expression. Manuel’s eyes widened and his brows pulled slightly upward. I fought a smirk."

    stop music
    MAN "I don’t think a present is necessary, Jose."

    "My internal happy dance was short-lived."

    JR "What do you mean?"

    MAN "Segunda is rich. Richer than you and me combined. "
    MAN "She cares less about material gifts when she could buy this whole shop with just her pocket money."

    "My expression dropped. What Manuel said made sense. "
    "Of course Segunda would be richer than both of us combined, I didn’t have anything to my name."
    "The fact that Segunda belonged to a wealthy clan never left my mind. Mariano had a maid come over to his boarding house to clean up after his mess."
    "He rented the whole Panciteria so we could do our paired homework in peace and tipped his classmate ten pesos after he let Mariano copy his essay."

    "The only reason Mariano even chose to travel by foot under the scorching heat of the sun was because he knew there were instances where I couldn’t afford to pay the transportation fee."
    "I was grateful that Mariano had the decency to spare me the shame."

    play music "audio/Music/Promises to Keep.mp3" loop
    MAN "Give her something money can’t buy. She would appreciate it more."

    JR "What do you mean?"

    MAN "Write her a poem or draw her portrait. Just about anything that you spent time and effort on."

    "My mouth formed an ‘O’ at the realization. Manuel chuckled at my reaction."

    MAN "How could you not have thought about that?"

    JR "Well, I-, I couldn’t think straight."

    MAN "You wanted to impress her."

    JR "No I didn’t! I just didn’t want to appear ungrateful."

    MAN "So you care about her opinion of you."

    JR "I do not! Propriety dictates that if someone gave you a present then it is only right to give something in return. Stop putting words in my mouth."

    "Manuel’s mouth tugged slightly at the corners, his eyes hooded. It’s the same expression he used when he walked away to pacify Segunda on their first meeting."
    "The same look he gave when he caught me stealing glances at Segunda."
    "It was that look that bathed me in cold sweat and made me feel like a sewer rat hiding my stench from a starved snake."
    "He {i}knows{/i}."

    MAN "I know you like my fiance. More than you think you do."

    "I swore my soul left my body. I didn’t think Manuel would let the world hear what remained silent for the past weeks."
    "No amount of mental preparation could have braced me for this confrontation. I conceded, no point in hiding."

    JR "What gave me away."

    MAN "I see how you look at her."

    "I didn’t think I was obvious. I could feel a panic rising deep within the crevices of my stomach."

    JR "…"

    MAN "I’ve been there. I know the signs."

    "I couldn't help but wonder what Manuel had to sacrifice in the name of familial obligations... But that’s beyond the point. "
    "I wanted to address the question that’s been bothering me for weeks."

    JR "Do you love her?"

    MAN "Yes."

    "Manuel didn’t even think about his answer. He said it with no second thoughts or hesitation. "
    "He loved her with ruthless conviction."

    JR "Does she love you back?"

    "I braced myself for the pain and disappointment."

    MAN "Yes. We love each other."

    "My heart dropped. Of course she does. Whatever tiny space I managed to occupy in Segunda’s heart stands irrelevant compared to the one in front of me."
    "I looked down at my coffee. It would be great to drown in its bitterness."

    MAN "But we don’t know how to get past the love that we grew up knowing."

    "I slowly raised my head to meet Manuel’s eyes. A tinge of hope forcing its way through the surface. Hope is a sewer rat."

    JR "I’m confused."

    MAN "We’ve only ever known each other as family. I wake up one day and my niece is now going to be my wife."

    "That does sound terrible. I could only guess Manuel grieved the wholesome relationship they once had. I racked my brain for comforting words."

    JR "Marriage within families isn’t {i}that{/i} uncommon."

    MAN "That doesn’t make me feel any better at the fact that I practically raised my wife. I held her as a toddler, Jose!"

    "I would have loved to hold a baby Segunda. I bet she was cute."

    JR "No need to make me feel jealous."

    "Manuel scrunched his face in disbelief."

    MAN "I seriously want to strangle you right now."

    "I should’ve kept my mouth shut. I was still processing this new information. "
    "They love each other but only as family. That means they don’t have romantic feelings for each other…which means {i}I{/i} still have a chance."

    JR "I’m just wondering…if marrying Segunda makes you feel…uncomfortable. Why push through?"

    "Manuel sighed. A deep sigh that sounded like he’d been holding it in for years."

    MAN "I just realized there are some things in life that you can’t break free of. For instance, the weight of family expectations."
    MAN "All my choices are tied to my family. I was conceived with the purpose of being a potential heir and I don’t know who I am outside of the boxes they confined me."
    MAN "Accepting the role of the future head means accepting the responsibilities and sacrifices that come with it…and all that it entails."

    JR "Including marrying your niece."

    MAN "Exactly."

    "I may have to retract my previous statement. Life is fair. "
    "I didn’t expect Manuel to be dealing with anguish. His life seemed so perfect on the outside."
    "I could relate, I too carried the weight of my family’s expectations. "
    "Being the golden child, as people put it, sounds rewarding but all rewards come with varying degrees of sacrifice that is obscured from other people’s views."
    "They only see the success, not the sacrifice. Not all sacrifices are voluntary."

    JR "How do you feel about that?"

    MAN "Like a sore loser. A coward. Look at me, the merciless game strategist that can’t get himself out of this mess."

    JR "…"

    MAN "It feels terrible that my cowardice robbed an innocent girl her agency, dreams and aspirations."

    JR "They would have still married her off to someone else."

    MAN "I know. If only she could stand up to her father…"

    "I didn’t like that Manuel was pushing that responsibility unto Segunda. Voicelessness is a condition of her gender, what power does she have over a patriarch?"

    JR "You’re a coward."

    "Manuel smiled. The same smile that told you he’s aware. This time with sadness."

    MAN "I know."

    #STOP SOME UNNECESSARY SFX######
    stop CrowdChatter
    #STOP SOME UNNECESSARY SFX######
    #+++++++++   SCENE 14 BOI   +++++++++++++++++++++++++++++++++++++++++++Pages 43-44  of the Script++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    scene bgEC
    stop music
    with fade
    with None

    # For hiding unnessary characters
    hide Manuel
    # For hiding unnessary characters

    play Market "audio/Voice/Market.mp3"
    play HCarriage "audio/Voice/HCarriage.mp3"
    "I called for a {i}kalesa.{/i} Manuel offered to pay and I would have accepted though I still had enough money to pay the fare. "
    "Contrary to my intentions, I hadn't bought anything today."

    JR "Hey, I’m sorry I was a bit…unrestrained to you earlier."

    show Manuel at leftMan
    with easeinleft
    with None
    MAN "I prefer you being your most authentic self, Jose. Talking to you was a breath of fresh air."

    hide Manuel
    with easeoutleft
    with None
    "That genuinely rendered a smile on my face. We bid each other farewell. "
    "The perfect image that I had of Manuel was shattered by no one else but Manuel himself."
    "He was tall, rich, kind and handsome for sure, but he was also lost, confused, and cowardly as he puts it."

    "Earlier, I had easily forgotten that Manuel was the future patriarch of a well respected clan as well as Segunda’s fiance. "
    "I had reduced him to the only hurdle stopping me from pursuing the girl of my dreams."
    "Now, I was convinced that I should just stay in my lane. Stealing Segunda away would probably do them a favor but I was sure that would also hurt them in the long run."
    "It would most of all hurt my mother. I couldn’t take that."
    "Whatever conviction I developed after talking to Manuel, I hoped would not waver. God knows how weak I am when it came to Segunda."


    #STOP SOME UNNECESSARY SFX######
    stop Market
    stop HCarriage
    #STOP SOME UNNECESSARY SFX######
    #+++++++++   SCENE 15 BOI   +++++++++++++++++++++++++++++++++++++++++++Pages 44-48  of the Script++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    scene bgCdC
    with fade
    with None

    "I brought with me the charcoal portrait of Segunda that I had copied from a photograph she had given me from weeks before."
    "I did not expect to receive another rose, a red paper rose. But this time, it was from my sister. "
    "Mariano also received one from Segunda and was now bragging to Ysabel about what a good brother he is."
    "It was folded carefully, no unnecessary creases in sight. More work was evidently put into crafting this piece. "
    "My sister had never given me a handmade gift before, I wondered what changed."

    "I admired the craftsmanship and smiled at my sister. My sister whom I realized held no inclination towards the arts."

    JR "You didn’t do this."

    show Olimpia at rightOLI
    with easeinright
    with None
    OLI "What are you talking about?"

    JR "You are anything but artistic, Olimpia."

    OLI "Anyone can acquire the necessary skills to make art, Kuya."

    JR "You don’t have the patience required to be an artist."

    "Olimpia looked at Segunda,and that gave it away. Segunda blushed a pretty shade of red."
    "My heart fluttered. I immediately forced myself to stamp down whatever physiological reaction my heart was doing. Deep breaths. I can’t keep doing this."

    show Segunda at leftS
    with easeinleft
    with None

    play music "audio/Music/Disquiet.mp3" loop
    S "I-I did it."

    "That admission was all it took for my walls to unravel. I was supposed to hold back. For Manuel,for Segunda, for my mother, for reason."
    "And then it occurred to me. I've always done things for other people, never for myself."

    JR "Do you know how painful it is for me to lose you now that I’ve got to know you?"

    "I said it before I could take it back. Olimpia gasped. Segunda’s face scrunched, she tried her best to prevent the emotions from spilling but it was too much."
    play BriskWalk "audio/Voice/BriskWalk.mp3"
    hide Segunda
    with easeoutleft
    with None

    show Mariano at leftMar
    with easeinleft
    with None
    "She made one last pleading look at me before she ran away. Olimpia called her and that got Mariano’s attention. He faced me, the brotherly instinct taking over."

    MAR "What did you do to her?"

    OLI "My brother didn’t do anything…"

    MAR "What do you mean? My sister ran away!"

    hide Mariano
    with easeoutleft
    with None

    hide Olimpia
    with easeoutright
    with None
    "I took that moment of distraction as a sign to leave. I chased after Segunda like how I chased validation. "
    "With vigor, certainty, no turning back. Sure that whatever waited at the end of the tunnel was worth the sacrifice."

    play Sob "audio/Voice/Sob.mp3"
    "I found her at a bench, sobbing. In different circumstances I would have left a maiden to her own devices. "
    "I sat next to her and offered my handkerchief. She accepted and wiped away the tears."

    show Segunda at leftS
    with easeinleft
    with None
    S "I’m not getting married."

    JR "You are."

    "Segunda let out a small painful sound. There are things Segunda could not run away from too."
    "I wanted to pat her back in comfort but that would be scandalous. Instead, I sat there like a complete idiot."
    "An idea popped in my head. How could I have forgotten? I opened my satchel and grabbed my sketchbook."
    "Tucked between the pages was a portrait I did of Segunda. Like her, I put in more effort with this one too."

    "I worked till the crack of dawn, making sure the values were correct and that I captured her likeness. The last one I did was disastrous, a stain on my perfectly clean track record. "
    "It embarrassed me to even sign that garbage."

    S "Jose…this is…"

    "Segunda continued scanning the portrait. I was convinced that she loved it. I mentally patted myself in the back."

    S "I’m out of words is this… Is this how you see me?"

    JR "That’s how the world sees you."

    show cgSCL
    with fade
    with None
    "Segunda cracked a genuine smile. I would have done anything on the spot to immortalize that sight. "
    "She started crying again but this time it was in between laughs."
    "Segunda composed herself, embarrassed at displaying vulnerability. She smiled but her eyes said anything but happy."
    hide cgSCL
    with fade
    with None

    S "Jose…I don’t want to go home. I’m not ready. I want to stay here for five more years."

    "I didn't know what that meant but I wanted to believe it was Segunda’s way of telling me she didn’t want to marry."

    JR "Say it and your parents might just grant it."

    "Of course I encouraged her to go against her family’s wishes. "
    "Aside from the fact that words of encouragement are the only thing that would make her feel better about her situation, "
    "I’d be lying if I said those words came from a place of friendship, I wanted more than what she could offer."

    S "You think so?"

    "I did not just think so, I was certain. Certain that Manuel would back her up in the event that she rebelled. The three of us might just get what we wanted."

    JR "Absolutely."

    "Segunda nodded her head with a tight-lipped smile. She continued staring at the distance as if my answer didn’t satisfy her. "
    "I was certain that’s what she wanted to hear, perhaps I gave her false hope? "

    S "I wonder…"

    "I inched myself forward. I wanted to give her what she needed."

    JR "Yes?"

    S "It’s nothing, it’s just-"

    JR "Please go on, I’d like to hear your thoughts."

    "I gave her the little push she needed to continue. Segunda appreciated the gesture, she smiled at me before she braced herself and took the words out of her mouth."

    S "Why do girls have to adjust to a society that they themselves conceived?"

    "I had prepared answers for questions that could alleviate her feelings towards her predicament. This was not one of those. "
    "It required me to actually sit and think for hours. Maybe draft an essay to point me towards the right answer."

    S "I was hoping you could give me insight."

    "I felt disappointed with myself. But no matter, I had more excuse to talk to Segunda later."

    JR "I can’t answer your question as I am now. But one day, when I’m old enough to understand the ills of society, I’ll come for you and tell you what you need to hear."

    "Segunda nodded."

    S "I’m glad you don’t think I’m overreacting or thinking too much, Jose."

    "It didn’t matter to Segunda that I didn’t have the answer, it mattered to her that I’ve listened and didn’t dismiss her question as trivial considering her background. "
    "It hurt me to think about Segunda as a tool to make the bonds of two families stronger."

    hide Segunda
    with easeoutleft
    with None

    play BRang "audio/Voice/BRang.mp3"
    "The both of us returned just before the clock struck seven. I was met with an annoyed Mariano and I told him the details leaving the part where I blurted out a confession of sorts to Segunda. "
    "Mariano didn’t seem convinced but he didn’t push any further."

    show Mariano at rightMar
    with easeinright
    with None
    MAR "Well if there’s anything, I got to walk around campus alone with Ysabel looking for you. She didn’t look like she enjoyed it though."
    hide Mariano
    with easeoutright
    with None

    "We both turned to Ysabel’s direction. She may have glared at me behind her fan. I left to approach Segunda to bid farewell."

    show Segunda at leftS
    with easeinleft
    with None
    S "I’m leaving this Saturday. My father wants me to go home for the holidays."

    "I didn’t understand why Segunda looked tense. I was to leave on Friday and that meant I wouldn’t be able to see her off. "
    "It’s not like this will be the last we’ll see each other, right?"

    JR "Oh, then I wish you well on your travel. Have fun. We’ll still see each other."

    "There it was again, the sad smile she wore a while ago on the bench. She opened her mouth to say something but-"

    show Olimpia at rightOLI
    with easeinright
    with None
    OLI "Segunda! Let’s go! We’ll be late for dinner." with hpunch

    "Segunda turned to me, her lips in a thin line. She looked at me, breathing me in, my features, imperfections, my insecurities. "
    "I felt self conscious. Raw and exposed."

    S "Goodbye, Jose."

    hide Segunda
    with easeoutleft
    with None

    hide Olimpia
    with easeoutright
    with None

    "The girl of my dreams turned away and never looked back. If only I knew this was our last conversation, I would have subjugated Chronos and forced him to stop time."

    #STOP SOME UNNECESSARY SFX######
    stop BriskWalk
    stop Sob
    stop BRang
    #STOP SOME UNNECESSARY SFX######
    #+++++++++   SCENE 16 BOI   +++++++++++++++++++++++++++++++++++++++++++Pages 48-55  of the Script++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    scene bgDR2
    stop music
    play music "audio/Music/Bittersweet.mp3" loop
    with fade
    with None

    play HCarriage "audio/Voice/HCarriage.mp3"
    "I was in the middle of a highway where horse drawn carriages passed through to reach Batangas. "
    "The past couple of days, I had agonized over the fact that this may be the last time I will ever see Segunda."
    "Was it? I wasn't sure, I was hoping some things may change over the course of the vacation."
    "Manuel expressed his support in the event that Segunda would stand up to her father but Mariano made it clear that their father was ecstatic to ‘hand over’ Segunda to Manuel."
    "One thing I was sure of was that Segunda held feelings for me too. The paper roses, the blushing, the intimate walks on the colegio. "
    "It had to mean something. We loved each other without having declared it clearly except that we understood each other through glances."


    "Right? One second I was certain, the next second I was trying my hardest to convince myself that Segunda loved me too."
    "What if all those kind and romantic gestures were done out of friendship and I just assumed things that were unclear from the very beginning?"
    "I hated this. If only Segunda had made it clear that she loved me too, that she did not care that I was unnatractive or poor, that her love did not rest on fragile foundations."
    "If that was the case then I would have rode in a white horse, climbed a castle and saved her from imprisonment."


    "I sighed. Love is hard. I didn’t think it could physically hurt me to think about it."
    "Somewhere in the pit of my stomach, there was a gnawing pain, probably a symptom of lovesickness. "
    "Sometimes, I wished my spirit could just walk out of my body and smack me in the face to get my act together. Being messy was unlike me."
    "Suddenly the air stilled and the sound of horse hooves against dirt road can be heard from a distance, enveloped in a cloud of dust. "
    "I had anticipated this, rehearsed what I was about to do a hundred times in my head."


    "I walked back a short distance to where I tied my horse and rode at the edge of the highway. The first carriage was close, I scanned the passengers. No one I knew of."
    "The second carriage was close by. 20 meters. 15 meters. 10 meters. It was close enough for me to look for familiar faces."
    "And there she was, my sweet Segunda. Hair frizzy with the heat and dust. Beautiful in her yellow-purple traje."
    "She spotted me and immediately surged forward to get a better look at me. The other passengers reprimanded her to stay put but Segunda ignored them. She didn’t care."
    "She smiled, of equal parts relieved to have seen me maybe for the last time and sad for the same reason. She took a handkerchief and waved it."

    show Segunda at leftS
    with easeinleft
    with None
    S "Goodbye, Jose!"

    hide Segunda
    with easeoutleft
    with None
    "She said loudly over the noise. Farewells were temporary, goodbyes were eternal. "
    "I hated goodbyes. I had expected for the carriage to stop, it would have if only Segunda weren’t surrounded by friends and family."
    "We could have talked but the actors deviated from the script. "
    "The anxiety I've been feeling for the past couple of days dissipated, replaced by disappointment that it didn’t turn out the way I wanted to."
    "This didn’t have to be that last time We saw each other. I was well-mounted. "
    "The carriage was just a couple of meters away. I still had a chance to forge my own path, abandon the weight of expectations forced upon me and chase after the girl of my dreams."


    "I could do that though I was paralyzed by indecision. Every second wasted on hesitation was a moment with my first love lost to time forever. The distance continued to stretch."

    "Should I?"


    menu:
        "Chase After Her":
            jump C8_yes

        "Let Her Go":
            jump C8_no




    #Choice@ of Scene @
    label C8_yes:

        stop music
        stop HCarriage
        play music "audio/Music/Dream Culture.mp3" loop
        play Hitya "audio/Voice/Hitya.mp3"
        queue RideHorse "audio/Voice/RideHorse.mp3"
        "I made my choice. Gripping the reins with my hands I urged my horse foward towards the departing carriage."

        JR "Segunda!"

        "The coach carried forward, heedless to my cry."
        play HartBeat "audio/Voice/HartBeat.mp3"
        "All I could hear was my heartbeat and the sound of hooves hitting dirt and stone with a thundering clack. I saw Segunda's wide eyed surprise from the passenger window."

        show Segunda at leftS
        with easeinleft
        with None
        S "What are you doing, Jose! It's dangerous! Let me stop the car--"

        JR "I need to talk to you!"

        S "Jose-"

        JR "I LOVE YOU!!! " with hpunch

        "I blurted months of repressed romantic feelings before I could take them back. "
        "My cheeks warmer than when I bathed in the sun, my heartbeat more erratic than when I was first called for detention. It’s too much. "
        "I have kept those three words hidden, shiny and new. I had never found a use for it until I laid my eyes on Segunda on that fateful day in my lola’s front door."

        S "W-what?"

        "I had become even more embarrassed by the second. "

        stop HartBeat
        stop RideHorse
        play HorseStop "audio/Voice/HorseStop.mp3"
        "Segunda ordered the coachman to stop and I brought my horse to a halt. Segunda got off the carriage the same time I went down my horse. I knew what was to come. "
        "I had crossed forbidden territory and there was no coming back."

        "Segunda waited for me to gather myself. I pretended to be calm. "
        "I hoped it appeared to be that way as I was dying inside clawing my way out of the pits of anxiety and utter humiliation. "
        "I pulled out the words that had kept me in line for the past several months. "

        JR "I’m just a simple guy."

        "I croaked those words out; I almost slapped myself for wanting to cry. "
        "I had never found myself in a situation where I willingly let myself be vulnerable and exposed to get my point across."

        JR "I have nothing to my name. No monuments dedicated to me, nor plaques to appreciate me. My name will soon be just a distant memory and my flesh and bones rendered to dust. "
        JR "But if there is one thing that I want people to remember me by, it is that I have learned to love so ardently that the idea of death didn’t scare me at all."

        "I heard squeals of excitement from Segunda’s relatives. I saw one of them gently push Segunda forward in encouragement. "
        "Segunda, beautiful in sweat and disheveled hair, was speechless. I couldn’t channel whatever fake confidence I had developed in school."

        "We were embarrassed to look at each other. Impatient, Segunda’s relative screamed for her to say something."

        S "Um…I don’t know what to say. I don’t think anyone has confessed to me before."

        JR "I don’t think I’ve confessed to anyone before."

        "We both looked at each other and as if on cue; chuckled at the awkwardness and novelty of the situation."

        JR "Can I come closer?"

        S "Yes…"

        "I walked over towards Segunda, ignorant of her relatives' squeals. "

        S "You’re standing too close, Jose."

        JR "You weren’t clear with your instructions."

        show cgSE
        with fade
        with None
        "I outstretched my hand and looked at Segunda as if asking for permission. Segunda gave her hand. I was holding her, but only by the fingertips. "
        "I didn’t know how much of her I could hold."
        hide cgSE
        with fade
        with None

        JR "Tell me what you need me to do."

        "Segunda had a thoughtful look on her face. I waited, and I would wait for much longer if it meant I would be with her."

        S "…Steal me away."

        "I didn’t know what my decisions cost back then…or how it would ultimately alter the course of history, but I was happy and contented and very much in love. "
        "And in that moment, my decision, no matter how crucial; had been with her."


        #STOP SOME UNNECESSARY SFX######
        stop HCarriage
        stop Hitya
        stop RideHorse
        stop HartBeat
        stop HorseStop
        #STOP SOME UNNECESSARY SFX######

        #First Choice Ending BOI
        scene bgBlack
        with fade
        with None

        # For hiding unnessary characters
        hide Segunda
        # For hiding unnessary characters


        "Years Later..."

        scene bgCF
        stop music
        play music "audio/Music/Almost New.mp3" loop
        with fade
        with None

        play CrowdChatter "audio/Voice/CrowdChatter.mp3"
        "I sat at a quaint outdoor cafe, sipping coffee as I read that morning's newspaper. On the front page cover was emblazoned the headline:"
        "{i}Indio revolt suppressed in Western Visayas{/i}"
        "A sense of nausea and unease built up inside me. The state of the country had been rapidly declining these days, with the Filipino people rising up to revolt in large numbers. "
        "But none of it was enough to shake off the overbearing power of Spain."
        "As much as I wanted to do something about it, I now had responsibilities that required my attention and things I couldn't afford to lose."

        show Segunda at leftS
        with easeinleft
        with None
        S "Jose? Is everything alright? You're doing that thing where you scrunch up your face when you read something unpleasant."

        "I looked up at my lovely wife seated across me, a cup of coffe in her hand. Her doe-like eyes were wide with concern. "
        "I took in the features of her cute round face and felt myself feeling once more at ease."

        JR "It's nothing, dear."
        JR "(ROMANCE ENDING ACHIEVED)"

        stop CrowdChatter

        jump end_game




        jump C8_done


    label C8_no:

        show cgHE
        with fade
        with None
        "I didn’t. I could no longer find the resolve to chase after her. I just stood there, I might as well replace the nearby lamppost. "
        "It was moments like these, crucial and possibly life changing, that courage decided to abandon me."
        hide cgHE
        with fade

        show Mariano at leftMar
        with easeinleft
        with None
        MAR "Hey."

        "Mariano appeared next to me. He had ordered the coachman to stop. How I wished it was Segunda."

        MAR "You could come with us if you like."

        "I considered that. I could but…but I can’t. I felt it was wrong. I knew it was wrong, I was just looking for excuses to push me further at the edge."

        "Mariano frowned. He studied me."

        MAR "So that’s it? You’re just gonna give up on her like that?"

        "My eyes widened in horror and my jaw dropped. I could not believe what I was hearing."

        JR "What?"

        MAR "Come on. Between the two of us, you may be the smart kid but that doesn’t automatically make me stupid."

        JR "How did you-"

        MAR "Figure out? Easy, I just have to take one look at you to know."

        "I couldn't believe this. Manuel was sharp but Mariano? No offense to the guy but I didn't take him to be an observant one."

        JR "I’m not going…"

        MAR "So you’re not gonna steal her away?"

        JR "Tempting."

        MAR "What?"

        JR "Thinking."

        "‘Steal her away’, was that what I was about to do? I saw it as saving her."

        JR "You sound like you want me to."

        MAR "Well, my sister still wants to continue school. Marriage is the only thing stopping her from pursuing it."
        MAR "And maybe I want to see Manuel lose one of his games. The one that gets to marry my sister gets to be the head of the clan."

        "I had no plans of being the head of someone else’s clan. That would make me an usurper of sorts."
        "I knew Manuel and Mariano were competing for the spot and Manuel was favored. Mariano probably didn’t know Manuel saw it more as a curse rather than a game to be won."

        JR "I don’t think I can…"

        MAR "You sure you don’t want to be my brother-in-law?"

        "I smiled at the thought of it. In another universe maybe when I wasn’t so much of a coward, I would entertain the idea. Mariano would make a great brother-in-law."

        JR "You’ll end up resenting me."

        "Mariano grinned. I knew him alright because he would have eventually."

        MAR "You may be right."

        "And maybe not chasing after Segunda was the right choice if it meant my relationship with Mariano wouldn’t be at risk of being ruined. "
        "He settled back in his seat and ordered the coachman to go."

        MAR "So long Jose, I have a feeling there's going to be a long and rough road ahead of you. Good luck."

        hide Mariano
        with easeoutleft
        with None
        "I watched as they drove away. I didn’t know it at that time but what Mariano said to me disguised as farewell was actually a thinly veiled prophecy. "
        "A cruel one. I needed that luck."
        "When time had long passed and the dust of the horse-drawn carriage had settled, "
        "What was left was the sound of my horse’s hooves on dirt road going the opposite direction of where my heart desires."
        "END PART 1"

        stop HCarriage
        stop music



        jump C8_done

    label C8_done:

    # For hiding unnessary characters
    hide Segunda
    # For hiding unnessary characters






    #+++++++++   START OF PART 2   +++++++++++++++++++++++++++++++++++++++++++ LDR PART 2 MEEEENNNNN +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++   START OF PART 2   +++++++++++++++++++++++++++++++++++++++++++ LDR PART 2 MEEEENNNNN +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++   START OF PART 2   +++++++++++++++++++++++++++++++++++++++++++ LDR PART 2 MEEEENNNNN +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++   START OF PART 2   +++++++++++++++++++++++++++++++++++++++++++ LDR PART 2 MEEEENNNNN +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #+++++++++   START OF PART 2   +++++++++++++++++++++++++++++++++++++++++++ LDR PART 2 MEEEENNNNN +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




    scene ttlP2
    with fade
    pause (3.0)
    with None


    #+++++++++   LOVE DOCTOR RIZAL   +++++++++++++++++++++++++++++++++++++++++++ Pages 1-28  of the Script +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    scene bgBHN
    with fade
    with None

    "There is a certain level of cruelty in remembering a past buried deep in an attempt to forget. "
    "In my case, it was the pain of mourning a love left unsaid that forced myself to recall in an attempt to inspire a poem to be passed by tomorrow."

    "My creativity had dissipated from constant overuse that left me with no choice but to subject myself to pain. "
    "I've been staring at this blank piece of paper for hours and it's already half past two in the early morning."
    "My fault, really, as I chose to be happy all day thinking the night would help me become productive. I tried to mindlessly scribble in the hopes of coming up with something, anything. "
    "My brain tried to conjure an image from a long time ago when I first learned how to love but it was of no use."
    "I had long forgotten her face, or her voice, her touch. That memory had been rendered to ash, together with the paper rose and the photograph."

    "I grabbed whatever book and began skimming through the pages. For the longest time, My life revolved around burying my nose in a book and collecting awards from the academe. "
    "As tedious as it may sound, it was the one thing that gave my life purpose...Until I met Leonor."

    "Leonor, the love of my life, the blood that fills my veins, the point at which everything intersects, my sweet Leonor, my greatest downfall, my original sin, the destroyer of men. "

    "I could start at any point in time but it was when I was sixteen when I experienced my first heartbreak that ultimately dictated the course of history. "
    "I spent most of my days agonizing over the what-could-have-beens that I had managed to amass more than enough romantic literary content to last a few months."
    "For fear of being made fun of, my notebook containing poems, short stories, essays and drafts was left in a small corner of my room to accumulate dust. Hidden. Or so I thought."

    show Marco at leftMarc
    with easeinleft
    with None
    MARC "I read your writing. It's good, it hurt me."

    "What I initially thought of as a cause for social suicide quickly made me famous among my close knit group of illustrado friends. "
    "The compliments inflated my ego and somewhere down the line I developed a hyperfixation to gather as much material for my magnum opus as possible."
    "And so, I flirted and got involved with as many binibinis as I desired. I enticed them with sweet words, love letters, and romantic poems. "
    "I would send them flowers illegally picked hanging from some random Spaniard's gate."
    "I would offer to draw their likeness and carve hearts out of a block of wood. In my own made up world, I was the epitome of a romantic and I intended to uphold the title. "
    "I found out that I could charm my way through any binibini I wanted…except for the tall girl next door."

    "Myself, now on the cusp of adulthood, had transferred to a boarding house owned by Doña Concha Leyva. I was next door neighbors with a kind couple that would invite me over for snacks. "
    "I refused out of courtesy but it had more to do with the fact that I didn’t want to appear as {i}‘patay-gutom’{/i}."

    scene bgVHD # I think this must be afternoon
    stop music
    play music "audio/Music/Danse Morialta.mp3" loop
    with fade
    with None

    # For hiding unnessary characters
    hide Marco
    # For hiding unnessary characters

    "That was until one afternoon when the scent of champorado had overpowered my resistance where I found myself outside their doorstep. "
    "The kind and overly hospitable couple welcomed me in, satisfied that I finally gave in. There I saw for the first time the tall girl which I later found out to be their daughter."
    "It wasn’t that she was tall that made an impression but the combination of her stature and how she carried herself with such grace and elegance that really drew me in. "
    "Ever since then I would visit their house even on days devoid of any occasion."

    play KnockDoor "audio/Voice/KnockDoor.mp3"
    "I knocked on the door. I heard footsteps approaching."

    show LValenzuela at leftLV
    with easeinleft
    with None
    LV "Jose! You’re here.\nAgain… Earlier than usual. Mother has not prepared snacks yet. Come in. " #put a next line after again...

    JR "Leonor, good to see you too."

    "I said a little louder. I surveyed my surroundings and inched myself closer for a whisper."

    JR "Are your parents here?"

    LV "No, they’re out for work. They’ll be returning shortly."

    play DoorClose "audio/Voice/DoorClose.mp3"
    "Leonor closed the door. She came face to face with me as she turned her back against the hard wood. "
    show cgKBD
    with fade
    with None
    "I gently placed a hand on the flat surface just inches beside her neck, cornering her. I wanted to make her feel as if I had the power in this situation. "
    "Appear imposing. I would have if only she wasn’t a couple of centimeters taller than me."
    "It was moments like this that I cursed my kuya Paciano for inheriting the taller gene. Good thing I stuffed my shoe with my spare sock."

    JR "Good…Orang?"

    "I said her nickname softly, laced with tenderness."

    LV "…Yes?"

    "She held my gaze. Impressive. Other girls would have melted on the spot. "

    JR "About my proposal…"

    "I took advantage of Leonor’s firm gaze. I looked at her lips a second too long hoping she wasn’t dim enough to misread my intentions. "
    "She stiffened, eyes wide, breath hitched. Good."

    JR "What do you think?"
    hide cgKBD
    with fade
    with None

    "She glared at me and walked forward purposely bumping me on the shoulder. I let out a small ‘ow’. "
    "Only Leonor, a lady of good standing, would have the audacity to bump into me. we started off as playfully good friends."

    LV "Other men would have just courted a lady instead of asking for permission."

    "I was feeling my shoulder. It didn’t hurt of course but I wanted to make her feel slightly sorry."

    JR "Perhaps."

    LV "Perhaps you want to save yourself the trouble of courting me in case I reject your proposal of being your sweetheart? "

    "I thought about what she said. I asked permission to make her feel safe and that she had a choice. "

    JR "Perhaps I just didn’t want to make you feel uncomfortable. "

    "Leonor stayed silent. A slight wrinkle on her forehead."

    LV "Leonor stayed silent. A slight wrinkle on her forehead."

    JR "You’re different."

    "And I meant it. Leonor was different. Other girls I've met would have thrown themselves at me the minute I showed interest. "
    "Leonor was a challenge. I liked a good challenge."

    LV "How many ladies have you said those words to?"

    "I smiled. Leonor was a tough cookie to crack. I put on the most dramatic voice I could muster and braced myself for my embarrassing theatrics."

    JR "Oh, Orang. My dearest Orang. You hurt me with your presumptions! Your words cut deep you might as well just grab a knife and stab me straight through the heart." #might need some new line spacing and alignment of center

    "I flailed my arms around like a mad man and made my best impression of one of those theater actors I saw in school."

    JR "Thou art hurt thee or thy shall die lonelieth death."

    "I pretended to be dead by closing my eyes, cocking my head to the side with that last line. Leonor let out a suppressed laugh. Good. My plan worked. I composed myself."

    LV "Just because you don’t understand Shakespeare doesn’t mean you can just go and make fun of him."

    JR "Okay, now I’m offended."

    "We looked at each other seriously and then broke out in laughter. This is why I liked Leonor, she was hard to get but easy to be with. "
    "She was serious but knew how to crack a joke every now and then."

    LV "I’m not helping you when Shakespeare decides to rise from the dead to curse you."

    JR "Shakespeare knows very well not to exact revenge. The last time his character did that, everyone died. Including the main character."

    "I walked closer to Leonor. I held her by her fingertips maintaining a featherlike touch."

    JR "So…what do you say?"

    LV "Let me think about it."

    play KnockDoor "audio/Voice/KnockDoor.mp3"
    "A knock on the door alerted us both. It was Leonor’s parents. Capitan Juan and Capitana Sanday Valenzuela."

    show CaptVa at rightCV
    with easeinright
    with None

    CJ "Jose, you’re here!"

    CSAN "Sorry we’re late. We brought home snacks."

    CJ "I hope our daughter was on her best behavior."

    JR "Oh no, Leonor was rather kind to me."

    "I flashed Leonor a teasing grin. Leonor rolled her eyes."

    JR "I was just showing her the new hand tricks I learned."

    CJ "Well, son. Show it to the rest of us!"

    "That afternoon, I had impressed the Valenzuela household with my hand tricks over cake and hot chocolate. "
    "I would glance at Leonor and catch her glancing at me too accompanied by a warm smile on her face."
    "I had a feeling that things will go the way I wanted to. Good."


    #STOP SOME UNNECESSARY SFX######
    stop KnockDoor
    stop DoorClose
    #STOP SOME UNNECESSARY SFX######

    #PLACE ====== INT. BOARDING HOUSE - NIGHT

    scene bgBHN
    stop music
    play music "audio/Music/Easy Lemon.mp3" loop
    with fade
    with None

    # For hiding unnessary characters
    hide LValenzuela
    hide CaptVa
    # For hiding unnessary characters

    "I didn’t anticipate how fast things would spiral into disarray. When I got to my boarding house, Doña Concha Leyva broke the bad news to me."

    show DonConcha at leftDCON
    with easeinleft
    with None

    DCON "I’m so sorry Jose, my son decided he would finally come home to me. You understand how we haven’t seen each other in years, do you?"

    "And that’s the story of how I became homeless."

    JR "When is he arriving?"

    DCON "In two days."

    "I was supposed to vacate the room and find a new place in two days. Nice."

    JR "I don’t understand, why didn’t you tell me earlier?"

    DCON "I didn’t know how to break the news to you! You are so sweet and kind and agreeable. You helped me with chores and made my life easier. "
    DCON "You’re like a son to me. I couldn’t stand seeing you distressed."

    "But she could stand throwing her sweet, kind and agreeable ‘son’ on the streets in favor of some man that abandoned her years ago. Mother of the year."

    JR "How am I supposed to find a new boarding house in two days?"

    "I considered sleeping on the floor of my classmates' boarding house until I could find a new place to stay but I was afraid the house rules were being strictly implemented. "
    "No freeloaders. Besides, their rent was quite expensive."
    "Or…I could ask the Valenzuela’s to take me in temporarily. Maybe I finally had a good enough reason to be in close proximity to Leonor. "
    "And I liked Capitana Sanday’s cooking. Perhaps…this is a blessing in disguise? Is the Lord Almighty finally favoring me?"

    DCON "Oh don’t worry Jose, I contacted Paciano a week ago. He’s already arranged a place for you to stay."

    "She gave a piece of paper to me. Oh, how I would love to rip it to shreds and feed it to the flames."

    DCON "That contains the address of your new boarding house."

    "She smiled apologetically. Well, I supposed I could forgive her for being a terrible stand-in mother. "
    "Refusing her son would mean keeping me but losing family instead. She made the decision that would be the least damaging, by keeping them both. "
    "I respected that. I unfolded the paper to check the address."

    "Calle 6 Santo Tomas, Intramuros\n{space=80}Casa Tomasina\n{space=80}Antonio Rivera" #needs align center or centered at align left

    "Tiyo Antonio? Of course, how could I forget? It's been years since we last saw each other and it ended up with me getting reprimanded by my kuya Paciano for throwing fists at arrogant Spanish boys."

    "\“In Spain, Indios are just zoo animals\”\n\n\“In the Philippines, Spanish is just bread\”" #check if this is a correct alignment for new line spacing and inserting double quotations

    "I cringed at the memory. I would see his silhouette sometimes on the street but I was quick to either hide or avoid my tiyo. "
    "I didn’t like my tiyo reporting my every move. Living under his roof would be a problem."

    "I bid my landlady goodnight and packed my belongings. I went to bed thinking about how my plans of courting Leonor were ruined. "
    "Maybe it would be best if she outright rejected me. My thoughts wandered to the other girl sharing Leonor’s name, my cousin."
    "How was she doing? With the way things were in school, the tension between the Spaniards and my brown brothers were growing by the day, "
    "It wouldn’t be a surprise if I found myself in another round of a fist fight. "
    "Maybe she could help me cover up for my foolishness." # check if this is correct underbrothers



    #PLACE ====== EXT. STREET - MORNING

    scene bgLMD
    with fade
    with None

    # For hiding unnessary characters
    hide DonConcha
    # For hiding unnessary characters

    "I was walking along the streets of Intramuros when I saw a familiar building housed by some Spanish scoundrel I didn’t bother remembering the name of. "
    "Just outside his gate hung beautiful bougainvillea in pretty shades of pink and orange."

    show Gardener at leftGARD
    with easeinleft
    with None
    GARD "Jose, you’re here."

    "I looked at the speaker. Manong, the gardener, was a thin middle-aged man. For reasons unknown to me, he was somehow always so tense with a slight shaky voice."
    "In the past, I would see me picking flowers and just let me be. Later on, I would voluntarily snip the best looking flowers in exchange for food. We sometimes talked in passing."

    JR "Manong, good morning. Just passing by."

    "I admired the flowers. They looked more vibrant than usual. I looked at the gardener and smiled."

    GARD "Oh, I don’t like the look on your face."

    play RustlingPap "audio/Voice/RustlingPap.mp3"
    "I walked towards the gardener. I stuck my hand inside the paper bag I was holding in my other arm."

    JR "I don’t think I’m that ugly, am I?"

    "In my hand were two pieces of warm pandesal. The gardener stared at the bread. He hesitated but snatched it anyway."

    GARD "Well, I guess you’re sort of cute."

    JR "Manong?!" with hpunch

    GARD "What??? That’s what the girls say."

    play PruShears "audio/Voice/PruShears.mp3"
    "The gardener gobbled up the bread, keeping the last piece in his pocket. He grabbed the pruning shears from his toolbelt and began snipping. He handed the bouquet to me."

    hide Gardener

    menu:
        "Accept the bouquet out of spite for his Spanish employer": #Choice A: No Affection Added
            jump C9_yes

        "Accept the bouquet because its pretty and Leonor would love it": #Choice B: Orang Affection +1
            $ valenzuela_affection += 1
            jump C9_no

    label C9_done:

    show Gardener at leftGARD

    GARD "Jose, I don’t think I’ll be able to help you next time."

    "I wondered what he meant but quickly dismissed it, I had other things to worry about like Leonor and the girls who said they found me cute. "

    play RustlingPap "audio/Voice/RustlingPap.mp3"
    "I stuck my hand again inside the bag and offered the gardener another piece of bread."

    JR "I’ll keep giving you food when I have extra."

    "The gardener munched on the bread and grinned at me as thanks. I bid him farewell and walked towards the direction of my boarding house, armed with a bag of bread, flowers and a plan."

    #STOP SOME UNNECESSARY SFX######
    stop RustlingPap
    stop PruShears
    #STOP SOME UNNECESSARY SFX######

    #PLACE ====== EXT. VALENZUELA HOUSE - MORNING

    scene bgVHD
    stop music
    play music "audio/Music/Danse Morialta.mp3" loop
    with fade
    with None

    # For hiding unnessary characters
    hide Gardener
    # For hiding unnessary characters

    "I was outside the Valenzuela household’s doorstep. I had been pacing back and forth for what felt like hours."
    "Is this how Dona Concha felt when she broke the news to me? Because for some reason I was nervous. And scared. "
    "For what could possibly be the first formal rejection I will ever receive. No girl would want to entertain an absent suitor."
    play DoorOpen "audio/Voice/DoorOpen.mp3"

    show LValenzuela at leftLV
    with easeinleft
    with None
    LV "Jose!"

    "I yelped. I found Leonor looking at me from the window. She walked away to open the door. She examined the flowers and the paper bag I was holding."

    LV "I don’t remember agreeing to your proposal."

    "She hadn't officially rejected me yet but it still stung. I scrambled my head to find the right words to say."

    JR "Well, you see… I have to… You know…"

    LV "Yes…?"

    "I took a deep breath to calm my nerves. I looked at Leonor with purpose. It’s now or never."

    JR "I’m leaving."

    "Leonor stared at me in confusion."

    LV "Is this about yesterday? Jose I told you, I just need more time-"

    JR "That’s the thing. There is no time left."

    "I looked down on my shoes. I felt smaller. Literally. I had no spare socks left at my disposal; I couldn't stuff my shoe to add height. Today was supposed to be laundry day."

    LV "Wait, what do you mean there is no time left?"

    "She spoke a little louder, temper rising. I peeked at her. Her brows furrowed."

    JR "I’m leaving. Dona Concha’s son is coming back. He needs the room. Are your parents there?"

    "I scanned the room inside. Anywhere to not meet her gaze."

    LV "No…they left to run errands. When are you leaving?"

    "She asked me softly. It turned my insides into mush."

    JR "This noon. I can’t stay for long I still have to pack my things."

    LV "Oh…"

    "I had nothing else to pack. My luggage was already sitting outside my bedroom door ready to go. "
    "I just came up with whatever excuse to avoid staying and prevent any opportunity she could find to reject me. I couldn’t take another heartbreak. "

    JR "This is for you."

    "I forced the bouquet and the bag into her hands."

    JR "Tell your parents thank you for everything and that I appreciated their kindness and hospitality."

    "I turned my back to Leonor, ready to make a leave. I was a coward like that."

    LV "Jose, wait!" with hpunch

    "I stopped on my tracks. I couldn’t face her."

    LV "Write me letters."

    "I turned around to look at her. Her eyes had become glassy."

    LV "The past couple of months I spent with you was fun. More than I would ever dare admit. I don’t think I’m fine with you leaving me behind."

    "I absorbed her words. I scanned her face for any sign of a joke. None."

    JR "Are you saying…"

    LV "Yes. Don’t make me say it a second time."

    "I stared at her. Taking it all in, and then I started laughing. The butterflies bursting with happiness in my stomach. "
    "I covered my face with my hand, hiding my excitement (kilig)."

    LV "Don’t laugh at me."

    JR "I’m not, I promise."

    "I wiped a tear at the corner of my eye, laughter dying down. "
    "I studied her face, took in her entirety. She’s pretty, not the kind where she lights up every room she enters but the kind where you have to get to know her to see it."
    "We just stood there in silence, facing each other. Just existing in what could possibly be our last moments together."

    LV "Don’t forget about me."

    JR "I won’t, I promise."

    #STOP SOME UNNECESSARY SFX######
    stop DoorOpen
    #STOP SOME UNNECESSARY SFX######

    #PLACE ====== EXT. CASA TOMASINA - NOON

    scene bgCT
    stop music
    play music "audio/Music/Easy Lemon.mp3" loop
    with fade
    with None

    # For hiding unnessary characters
    hide LValenzuela
    # For hiding unnessary characters

    "I wouldn’t have made such a big of a deal moving away if I only knew my new boarding house was just over two kilometers away. "
    "I lived in Intramuros for quite some time but I didn't exactly explored every nook and cranny."
    "Casa Tomasina was neat. It looked like one of those expensive boarding houses my classmates resided in. "
    "Dona Concha’s boarding house was a level far lower than Casa Tomasina but I was contented. It provided me the space I needed and I grew fond of it. I missed the leaky roof already."

    play DoubleDoor "audio/Voice/DoubleDoor.mp3"
    "I saw my Tiyo Antonio come out of the double doors from where he was standing. A boy which I could only assume to be a helper, trailed behind him."

    show TAntonio at leftTAN
    with easeinleft
    with None
    TAN "Bring his luggage to Room 203. Jose!"

    "My Tiyo walked to me with a huge grin and open arms."

    JR "Tiyo Antonio, it’s nice to see you. Thank you for having me."

    "I hugged my Tiyo. Another figure approached us."

    JR "Tiya."

    show TSilvestre at rightTSI
    with easeinright
    with None
    TSI "Jose."

    "My Tiya Silvestre regarded me up and down."

    TSI "You’ve grown since the last time I saw you."

    "I hoped that wasn’t an insult. She stretched her arm forward. I took it and pecked the back of her hand. "
    "I never really liked my tiya, she looked like she hid secret information she could use against me inside her sleeves. My tiya withdrew her hand."

    TSI "Leonor, darling, come greet your cousin."

    stop music
    play music "audio/Music/Dream Culture.mp3" loop
    "I shifted my gaze to the doorway, there I saw a girl peeking from behind the door. She gasped, eyes wide in surprise as if she were caught stealing food. Cute."

    "The girl stood straighter and wiped her hands on her tapis. She breathed in and out. I held back a smile. She walked towards our direction."

    show LRivera at semirightLR
    with easeinright
    with None
    LR "Kuya Jose."

    "She extended her arm with elegance that could only have been acquired through practice. I kissed her hand. "
    "I never really thought much about her, she was still very much a child the last time I saw her."

    JR "You’re taller. How old are you again?"

    LR "I’m 13."

    JR "Goodness how fast time flies."

    TAN "Right? They grow up so fast!"

    "Tiyo Antonio looked at his wife for approval. She didn’t look as pleased, which is probably her default expression so I didn’t really mind it much. "
    "Tiyo Antonio cleared his throat, swallowing the disappointment."

    TAN "Jose, let me tour you around the casa."

    JR "Alright."

    "As Tiyo Antonio was leading me inside, I heard murmurs behind me. I took a peek and saw Tiya Silvestre reprimanding Leonor in hushed tones."

    #STOP SOME UNNECESSARY SFX######
    stop DoubleDoor
    #STOP SOME UNNECESSARY SFX######

    #PLACE ====== EXT. ESKINITA - NIGHT

    scene bgEK
    stop music
    with fade
    with None

    # For hiding unnessary characters
    hide LRivera
    hide TSilvestre
    hide TAntonio
    # For hiding unnessary characters

    "A few days have passed since I arrived at the Casa. Nothing eventful happened. Go to school, casually hurl insults at my Spanish classmates, go home. "
    "My days went on as usual, aside from one little inconvenience that later turned out to be quite endearing."
    "I pretended not to notice my cousin spying on me. I let her have her game of fun and I was a willing participant. It was cute. "
    "Later that night, I sneaked out of the Casa to deliver a letter to the post office addressed to Leonor Valenzuela."

    "It was dark at half past eight save for a couple of lamp posts when I heard shouting and hurried footsteps approaching. "
    "I could make out a couple of “Stop!” and “Catch him!” from a distance. I had stepped out of an alley when a person crashed into me." with hpunch

    JR "Hey, watch where you’re–"

    "The figure aggressively pulled me into the darkness and covered my mouth. I tried fighting back but I was overpowered by the tall figure."

    show JCecilio at leftJC
    with easeinleft
    with None
    Q "Shhh, shut up. Shut up!"

    "He half whispered, half yelled at me. From the limited lighting, I could make out a busted lip and a black eye. "
    "I decided to cooperate, I didn’t know what this runaway criminal was capable of."

    GD1 "Where did he go?"

    GD2 "He went that way, sir."

    GD1 "You, follow me. The rest go that way. Get moving!"

    "We controlled our breathing, careful not to get caught as we listened to the sound of fading footsteps. The tall figure finally let go of me, sighing in relief."
    "I watched as he stepped towards the edge of the alley where the light could hit him. He was young, tall with a scrawny build and tan skin. "
    "His wounds also looked a lot more terrible under the light. He looked like someone I could take on in a fist fight."

    Q "The coast is clear."

    JR "And you’re telling me that because?"

    "The boy turned his head to take a good look at me."

    Q "Hey man, I’m sorry for dragging you into this."

    "I softened at his apology. I remembered my mother. Was he one of those people that got wrongly accused of a crime?"

    JR "Careful, the guardias are more vigilant at night. They patrol the streets armed with batons. May catch yourself facing one."

    "I didn’t know why I was helping him. I heard talks about an underground radical group in passing and it alarmed the guardias."
    "I didn't have anything to do with him but I had a feeling he was innocent. The boy nodded and removed himself from the light. "
    "He continued scanning the surroundings from his obscured spot."

    Q "You live around here?"

    JR "Yeah, just around the corner."

    Q "What’s your name?"

    "I paused. I didn’t know how much of my personal information I could trust with the boy. My mouth ran before I could regret telling him."

    JR "Jose. Jose Rizal."

    "The boy stiffened. He asked in a controlled voice."

    Q "Jose, do you happen to like flowers? Particularly the pink and orange ones?"

    "I remembered the bougainvillea from a couple of days ago."

    JR "Yes. They look even more beautiful now that they are in full bloom."
    #put punch sound effects after this

    play Punchy "audio/Voice/Punchy.mp3"
    "The events that followed were too fast for my brain to process. The boy went berserk and punched me on the face. I held on to the wall for support." with hpunch

    stop music
    play music "audio/Music/Clash Defiant.mp3" loop
    Q "It’s you! You asshole…"

    "He said those words filled with the rage and accusation of a hurt boy. And I decided I didn’t care. I shouldn’t have extended understanding."
    #put punch sound effects after this
    play Punchy "audio/Voice/Punchy.mp3"
    "The boy prepared to land another blow but I was quick to see the attack. I dodged it with the speed of an experienced brawler and punched him straight to the nose. " with hpunch
    "He tumbled to the ground."

    Q "Ow!!!"

    "I was ready to pounce on him one more time but paused in realization."

    JR "Sorry!"

    "I hurried to his side to inspect the damage."

    Q "Ow! Watch it!"

    JR "Sorry…why are we fighting again?"

    "Tears spilled from his eyes along with blood dripping from his nose."

    Q "‘Cause you’re an asshole!"
    stop music

    "I kneeled on his side, took a handkerchief from my pocket and offered it to the boy. He accepted it without any fuss and started dabbing on his nose. "
    "I thought back to the other girls I had sent flowers to."

    JR "Is this about Esperanza? Are you her lover?"

    "The boy was busy tending to his nose to give me his full attention."

    Q "Who?"

    JR "Esperanza, I sent her flowers."

    "The boy glared at me."

    Q "You send flowers to girls who are already in a committed relationship? How low can you possibly go?"
    #put slam wall sound effect
    "His condescension had completely dissolved the little patience I had left. I grabbed the boy on his shirt collar and pulled him up to full height. I slammed him hard on the wall." with hpunch

    JR "Listen here, you pig. And I want your undivided attention."

    "The clanking of metal alerted the both of us. We looked to the side. A cat. I slammed him again to get my attention." with hpunch

    JR "You think you can just attack me and throw insults like some wartfaced buffoon and expect no repercussions? "
    JR "I can rearrange your face with my fist; the guardia civil won’t be able to recognize you. You tell me what is going on and I might just let you go."

    "The boy looked alarmed. Terrified even but I may have been mistaken. It was too dark to tell. The boy sighed in defeat."

    Q "It’s Lizares."

    JR "Who?"

    Q "Lizares. The Spanish dude with the obnoxious garden at the end of Calle Paloma. They mistook me for you."

    "I let him go. Lizares? Could it be? I shook my head no and focused on the situation at hand. How could a mistaken identity be possible when we looked nothing alike?"

    JR "Why, I didn’t do anything…"

    "The boy scoffed at me."

    Q "Oh yeah? What about stealing his prized flowers you flower thief. You almost got Luisito fired."

    JR "Luisito?"

    "The boy let out a breath of frustration."

    Q "And now I find out you don’t even know the gardener’s name? I didn’t think you could go any lower than that. Oops. "

    "The boy covered his mouth with both hands. He muttered ‘sorry’ in mock sincerity and sat down on the concrete floor with his back against the wall. The blood had stopped dripping."

    JR "What happened to manong?"


    play music "audio/Music/Disquiet.mp3" loop
    Q "His boss noticed something wrong with how the flowers were arranged and forced Luisito to confess."

    "I didn’t want to think what ‘forced’ implied. I hoped that wasn’t the case."

    JR "He willingly gave the flowers to me."

    "I omitted the part where I did illegally pick flowers in the beginning and that Luisito had known but just let me be."

    Q "You bribed him with food. Don’t paint yourself a saint."

    JR "He was hungry."

    Q "How convenient."

    JR "It’s the truth."

    Q "You took advantage of him. You’re not fooling anyone."

    "I had enough. Luisito had been a willing participant in this mess and I won’t allow this brat to pin all the blame on me."

    JR "Have you seen how frail he looks? He could die from a simple cough. Making it seem like a barter spared him the shame of begging for food"

    "I waited for the brat to disagree with me. We stared at each other waiting for the other to concede. The brat sighed in surrender."

    Q "Alright, I believe you."

    "I slumped on the wall and let myself slide in a sitting position beside the brat. I buried my head in my hands. "
    "The turn of events was simply unbelievable. I thought back to the brat beside me."

    JR "What’s your name?"

    JC "Jose Cecilio."

    "Realization struck me. I looked at the boy in disbelief. "
    "Of course, how could I not realize sooner? His name was quite common, I even shared it with my tiyo from my mother’s side. I blurted words I didn’t mean to."

    JR "He snitched me."

    JC "I would too if it meant keeping my job."

    "The boy said it nonchalantly. I was hurt at the betrayal and it seemed the boy noticed."

    JC "Listen. He has a sick mother. He’s saving money to send her to a decent hospital, you can’t blame him."

    "I could empathize with that. I was currently studying to be a doctor in hopes of curing my mother’s failing eyesight. "
    "If my mother were here, she would reprimand me for stealing flowers to impress unsuspecting binibinis."

    JR "I’m a thief."

    JC "Yeah."

    "The boy snorted and agreed in between giggles."

    JR "Why do you sound so happy?"

    "The boy shrugged."

    JC "Hey, I just think that Spaniard deserved it. He’s an abusive asshole."

    JR "That doesn’t make me feel any better. I’m still a thief."

    "The boy sat up straighter and looked at me pointedly."

    JC "This is the problem with you illustrados. Your lot only see the world in black and white when we’re painted with grays. "
    JC "Lizares? He’s the real thief. He’s stolen money from Luisito by not compensating him exactly for his labors worth. "
    JC "He’s built a house in a soil that doesn't belong to him, basically stealing land that should’ve been ours. Now that, that is stealing."

    "The boy continued dabbing on his nose as if he didn’t just say anything profound. I thought about what he said. "
    "The boy had a point, he did. But I still couldn’t shake the feeling of error. "
    "The act of stealing had primarily been an act of petty rebellion. When Luisito negotiated with me, it turned into an act of compassion."
    "Now, it was just that…an awful case of miscalculation. "
    "Lizares may have stolen on a larger scale, but my guilt wouldn’t let me reconcile with the fact that no matter how miniscule the gravity my crime had been, "
    "It wasn’t enough to absolve me of any responsibility as I had hurt people in the process."

    #STOP SOME UNNECESSARY SFX######
    stop Punchy
    #STOP SOME UNNECESSARY SFX######

    #PLACE ====== EXT. CASA TOMASINA - LATER

    scene bgCTN  #must be night though
    stop music
    with fade
    with None

    # For hiding unnessary characters
    hide JCecilio
    # For hiding unnessary characters

    "I was lost in my own thoughts when I arrived at the casa. The faint glow of a lamp inside the house alerted me. "
    "Someone was awake and I was about to get into more trouble than I could handle."

    play DoubleDoor "audio/Voice/DoubleDoor.mp3"
    "I circled the casa and looked for the backdoor. I planned on entering the house as stealthily as I could when the door swung open." #sound of door opening fast

    show TAntonio at leftTAN
    with easeinleft
    with None
    TAN "Jose? What are you doing here?"

    "I stiffened. I masked my surprise."

    JR "I was getting some fresh air. I couldn’t sleep."

    "I smiled sheepishly. Tiyo Antonio looked panicked. He walked closer to me."

    TAN "Well now that you’re finally here, help us boy!"

    "He grabbed my shoulder and shook me." with hpunch

    TAN "My daughter is missing!"

    "I processed his words. My heartbeat rose more than when I’d arrived."

    JR "What!?" with hpunch

    TAN "We’ve been looking for her for almost half an hour. My sweet daughter, gone!"

    "Tiyo Antonio tightened his grip on my shoulder. He looked destroyed. I guided him inside the house and made him sit on a chair."

    play DoorOpen "audio/Voice/DoorOpen.mp3"
    "My Tiya Silvestre was weeping when the creaking sound of a door opening caught their attention. There she was, my cousin, looking shocked at the scene. " #sound creaking sound of a door
    "Tiya Silvestre stopped crying and went to her daughter."

    show TSilvestre at rightTSI
    with easeinright
    with None

    play music "audio/Music/Promises to Keep.mp3" loop
    TSI "Leonor! Where have you been!?"

    TAN "My sweet child, we’ve been looking for you!"

    "Leonor hadn’t recovered from her shocked expression. Suspicious."

    show LRivera at semirightLR
    with easeinright
    with None
    LR "I saw a cat. He sounded like he was crying so I went outside to see him."

    "Tiya Silvestre looked satisfied at the lame explanation and hugged her. She didn’t care about the circumstances. Seeing her daughter safe was enough."
    "I sized Leonor and that’s when I noticed the cat. The cat. I couldn’t explain it but it felt like something wasn’t clicking. "
    "Like I missed something and I couldn’t see the full picture yet."

    "Once Tiya Silvestre gathered herself, she began reprimanding Leonor. Tiyo Antonio ordered everyone to retire to their bedrooms to dismiss the situation. "
    "Before I could go, Tiyo Antonio approached me."

    TAN "Jose, you have dirt on your cheek."



    "I covered it with my hand. My bruised cheek had slipped my mind. As I was walking down the hall, I couldn’t shake the feeling of having forgotten something important. "

    #STOP SOME UNNECESSARY SFX######
    stop DoubleDoor
    stop DoorOpen
    #STOP SOME UNNECESSARY SFX######


    scene bgBRN
    with fade
    with None

    # For hiding unnessary characters
    hide LRivera
    hide TSilvestre
    hide TAntonio
    # For hiding unnessary characters


    "When I entered my room and saw the papers on my desk, I figured out it was the letter I was supposed to deliver to the post office."
    "I immediately looked for it in my coat pockets and found them empty except for my handkerchief soiled with some annoying brat’s blood. I threw it in the trash and began preparing for bed."

    "That night, when I was lying in bed, I kept rewinding the events in my head. The feeling of something amiss hadn’t left me. "
    "The cat. The lost letter. I reached for the lamp when my hand accidentally hit an empty tin can and fell off the side of the desk, making a metallic clang as it hit the floor."
    "The sound had triggered my memory that had me sitting stiffly upright in cold sweat. "
    "A while ago in the alley when I was using force to intimidate the boy, a metallic clang had alerted me of an intruder that happened to be just a cat."
    "The same cat that my cousin Leonor had brought home. Leonor has been following me the whole time during my stay in the Casa. "
    "She wasn’t missing, she intentionally sneaked out to follow me. The cat had been an alibi and Leonor had bore witness to my spectacular display of violence."



    #PLACE ====== INT. BEDROOM - DAY

    scene bgBRD
    stop music
    with fade
    with None

    "I didn’t sleep a wink. I went to school earlier to avoid any interrogations from my Tiyo and Tiya. "
    "When I arrived home, my Tiya had been on her bedroom window watching me tiptoe my way inside the Casa and caught me just as I entered the backdoor."

    "I really should stop using the backdoor."

    "As anticipated, she asked me about the bruise on my cheek."

    menu:
        "Tell her Leonor slapped you impulsively when you accidentally stepped on her cat's tail so you can have an excuse to talk to her privately.":
            #Choice A: Rivera Affection -1
            $ rivera_affection -= 1

            jump C10_yes

        "Tell her your Spanish classmate pulled a terrible prank that injured one of your classmates and left you with a bruise.":
            #Choice B: Rivera Affection +1
            $ rivera_affection += 1

            jump C10_no

    label C10_done:


    # check for new line spacing \\\nnn
    play WritePap "audio/Voice/WritePap.mp3"
    "{i}Dearest Orang,\nI hope this letter finds you well. Unforeseeable events have occurred that prevented me from contacting you sooner and for that, I apologize. I hope-{/i}"
    stop WritePap

    play KnockDoor "audio/Voice/KnockDoor.mp3"
    pause (1)
    queue DoorOpen "audio/Voice/DoorOpen.mp3"
    "A knock on the door disrupted my writing. I got up from my chair and opened it. "
    "There I saw my cousin Leonor, and in her arms lay the cat comfortably. The cat screeched at the sight of me. Offended, I made a mental note to make a siopao out of him later."

    show LRivera at leftLR
    with easeinleft
    with None
    JR "Is there anything I can do to help you?"

    play music "audio/Music/Dream Culture.mp3" loop
    "I searched Leonor’s face for any sign of guilt from the night before. "
    "None. Instead, I noticed her blemish free skin, the fringe that pleasantly framed her face and how the color of her eyes weren’t the deep brown, almost black that was ascribed to our ethnicity."
    "I could already envision the line of suitors hoping to win her. Tiya Silvestre did a splendid job taking care of her."

    LR "It’s Ramoncito, he’s hurt"

    "I looked at the cat. He had gone docile. Of course he would, smart animal. "
    "I motioned for them to come inside. I pointed at the empty bed. I kneeled on the side of the bed and began inspecting the cat’s body."

    JR "So…you named him Ramoncito?"

    "I asked in an attempt to make light conversation."

    LR "I think it's cute."

    "I spotted a dry patch of blood on the side of his leg. "

    JR "There’s nothing to worry about."

    LR "What do you mean? He was clearly hurt last night."

    JR "That was last night. His blood has already coagulated. Not much medical attention needed."

    LR "So that’s it? Nothing to give him to make sure he returns to health?"

    JR "I wouldn’t know. I’m a medical student, not a veterinarian."

    "Leonor pursed her lips in frustration. I felt an unexplainable pang of guilt."

    JR "Listen, it’s just a small wound. Nothing serious. "
    JR "If you brought him to me immediately then I could have patched him up to make sure the wound doesn’t get infected. Luckily for Ramoncito, he–"

    "And just like that, I found the final piece of the puzzle that I never knew was missing. "
    "She followed me last night in hopes I would heal Ramoncito. It made perfect sense."

    LR "Are you okay?"

    "Leonor looked at me with concern."

    JR "Oh, I’m fine I just realized something-"

    LR "No, I meant your cheek."

    "I had forgotten all about my bruised cheek, I suddenly felt self-conscious with her intent gaze. "
    "Leonor pushed her torso forward and began reaching her hand out."
    "I just knelt there, paralyzed in my position, just waiting for the events to unfold. I gulped down the familiar feeling of excitement. "
    "It wasn’t right. I had to get back to writing to the only Leonor my heart opened up to."

    "I caught her wrist before she could touch me. I felt her pulse. Leonor’s eyes widened with realization."

    LR "I’m sorry."

    "I released her hand. I was sick to even welcome the idea of a woman other than the one I had committed to pursuing from days back. "
    "A woman in close proximity, young and beautiful with the grace of a trained ballerina."

    JR "It’s fine. It hurts when you touch it."

    LR "I presume as well. It’s a terrible color."

    "I hoped that alley brat looked somewhat disfigured. "

    LR "I can help you."

    JR "What?"

    LR "You’re a brawler. Getting hurt is inevitable. You can teach me first-aid."

    "I shook my head in amusement. Of course that’s how she perceived me."

    JR "I don’t exactly participate in fights because I enjoy it."

    "My position was getting uncomfortable. I stood up and brushed invisible dust off of my pants."

    JR "What do you get out of this?"

    "Leonor stood up to match my height. Her short stature made me feel secure in ways Leonor Valenzuela couldn’t. "
    "It wasn’t her fault, but I liked that with my cousin, there was no need to overcompensate, no room for backhanded compliments. I was brilliant with no doubts."

    LR "I want to become a healer."

    "I didn’t know if she meant a doctor or a nurse. Either way it was impossible for her to achieve it."

    JR "Your mother will never allow you."

    LR "Exactly. You can help me. I can help you. I’ll even cover for you. We can be partners in crime."

    "Leonor picked up clueless Ramoncito from the bed and brought him up close to my face."

    LR "Please. Please. Please."

    "I liked the idea. It didn’t require much thinking. It sure didn’t require a cat shoved in my face to convince me. "
    "After all, the conditions were all in my favor. I took one last look at Ramoncito before agreeing."

    hide LRivera

    menu:
        "Agree to get closer to Leonor":
            #Choice A: Rivera Affection +1
            $ rivera_affection += 1
            pass

        "Agree just in case you get into more trouble":
            #Choice B: No Affection Added
            pass

    label C11_done:

    show LRivera at leftLR

    JR "Deal."

    "When our agreement had long passed and the day faded into night, I went out discreetly to send the letter long overdue to Leonor Valenzuela. "
    "Written inside were instructions on how to write using invisible ink."

    #STOP SOME UNNECESSARY SFX######
    stop WritePap
    stop KnockDoor
    stop DoorOpen
    #STOP SOME UNNECESSARY SFX######

    #+++++++++   LOVE DOCTOR RIZAL (INTERLUDE)   +++++++++++++++++++++++++++++++++++++++++++ Pages 28-39  of the Script +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    #PLACE ====== EXT. ???? - NIGHT???

    scene cgINT1-1
    stop music
    play music "audio/Music/SCP-x3x I am not OK.mp3" loop
    with fade
    with None

    # For hiding unnessary characters
    hide LRivera
    # For hiding unnessary characters

    play WalkLeaves "audio/Voice/WalkLeaves.mp3"
    "That night, I dreamed."

    "I found myself traversing a dark road in the middle of the night. My feet moved mechanically, compelled by an invisible force to keep moving forward. "
    "Each step gave an accentuated crack, as leaves and twigs snapped and were crushed."
    "There was not a single sound to be heard in that forest. No birds to sing, no insects to feed. No whistling breeze and no groaning trees, heaving under the weight of their ancient pasts. "
    "There was only silence. A silence so loud that it rang in my ears, making the sound of my heartbeat even louder still."

    stop WalkLeaves
    "I stopped in front of a giant rubber tree. Its gnarled roots splayed outward before me, beckoning me inside its dark embrace. "

    "Cold light seeped through the clouds, the moon stretching across the pitch black sky. I stared up at the arms of the unforgiving god, where a lone rope dangled downward. "
    "Its knot gave way to flesh and bone, the body of an old Spaniard adorning the branch like a Christmas decoration."

    scene cgINT1-2
    with fade
    with None
    "Father looked down on me, eyeing the bolo I had in my hand."

    FA "Have you come to finally kill me?"

    ME "It would be a waste of time to kill a dead man."

    "I laughed. So did Father. "

    ME "I have come to make this place my home. This is where I will make work, and rest my head. I’ll eat here, and find a wife. "
    ME "We’ll have a son and then I will die. They’ll bury my body where they found you."

    FA "And what will they put on your gravestone?"

    ME "Ibarra."

    #STOP SOME UNNECESSARY SFX######
    stop WalkLeaves
    #STOP SOME UNNECESSARY SFX######

    #PLACE ====== INT. SANTO TOMAS - DAY

    scene bgSTO
    stop music
    play music "audio/Music/Tango de Manzana.mp3" loop
    with fade
    with None

    "Tensions were high in my class that day. "
    "The fat priest babbling away at the front pretended to blissfully not notice it, but even I in my exhaustion ridden state could feel the glares of my Spanish classmates at the back of my head."

    "There was a clear distinction in social ranks that could be discerned by the way the seating plan was arranged. "
    "Peninsulares, or those from the Mainland kept to themselves in the front."
    "Insulares occupied the row behind them, Mestizos the row after that. "
    "And dead at the back were the so-called Indios– Students of only native descent who either had the money or connections to get into a prestigious university like Santo Tomas."

    "Now, by no means was my uniform shabby or my supplies of low quality. "
    "But compared to the expensive custom uniforms and plumed dipping pens of my Spanish counterparts, I sure did feel like a pauper. And boy, did they never let me forget it."

    "On days where I’d shine my shoes, some of my classmates would ‘accidentally’ step on my feet and make them dusty again."

    "At first I tried my best to just leave it be. It was important to learn when to pick your battles, as chances are that the teachers and faculty would side with ‘one of their own’ anyway. "
    "No use getting angry when a Spaniard cuts in line before you at lunch time. Nope, I wasn’t bothered by that at all. Not at all."

    "Fortunately, most of the Spaniards considered me as too far beneath their notice to bother with me. That was, until Javier Lizares came along."

    "Fucking Lizares and his stupid smug powedered face, stupid shined shoes, stupid puffed up hair and the stupid way he looked at me like I was a bug. "
    "It had been a while since I felt this same kind of implacable irritation I had felt all those years ago with Manuel Luz. At least Manuel hadn’t been trying to antagonize me on purpose."

    "I was about to pick up my bag to follow my friends out of class when just within earshot I heard Javier and his pack of goons loudly conversing."

    show Javier at rightJA
    with easeinright
    with None
    JA "–And just the other day, my father had that gardener whipped and thrown into prison. But that was only after he first confessed to who kept stealing mother’s prized flowers."


    show Daniel at semirightDAN
    with easeinright
    with None
    DA "Was he able to give a name?"

    JL "He sure did! And would you believe it if I told you his name was “Jose”?"

    "The group suddenly turned to look at me."

    show Ignacio at leftIG
    with easeinleft
    with None
    IA "What are the odds it’s our Jose over here, huh? "

    "I did my best to hide the pensive expression on my face."

    JR "You know Jose is a common name, right? At any given point you’d be able to find a dozen men with the same one."

    JL "True. But what exactly differentiates one rat from another? You might as well look and sound the same."

    "Javier’s minions laughed along."

    JR "I could say the same for every Spaniard I’ve ever met."

    "The room suddenly devolved into silence, with my classmates throwing me dirty looks. I ignored them."

    "A part of me wanted to admit it really was me, just to wipe the smirk off this guy’s face. But the punishment of doing so outweighed any possible satisfaction I might have felt for a moment. "
    "Javier was right— he just had no proof. I forced a laugh, hoping to God it came out more confident than I felt."

    JR "Well good luck with finding that thief or whatever. It’s been nice talking to you all but I’ve really got to go."

    JL "Of course, when my father gets his hands on that thief, he’ll make sure the poor bastard won’t get to keep his hands afterwards."

    "I couldn’t have gotten out of there any faster. "



    #PLACE ====== EXT. SANTO TOMAS FOOD HALL - NOON

    scene bgSTO  #must be food hall
    stop music
    play music "audio/Music/Easy Lemon.mp3" loop
    with fade
    with None

    # For hiding unnessary characters
    hide Daniel
    hide Ignacio
    hide Javier
    # For hiding unnessary characters

    "Hours later, when I ate my lunch with my friends, I would think back to that interaction and wonder if I had given myself away. "
    "There was something sinister about the way Javier talked about the supposed thief. "
    "It was less about the desire to pay the perpetrator back for stealing his mother’s possessions, or the idea of perhaps “restoring” his family’s honor. "
    "No, what I saw in the other boy’s eyes was a desire to hurt someone he saw as less than him. A shudder ran down my spine, I hoped that Cecilio boy was okay. "
    "My attention was brought back to reality when I heard my two mates mentioning girls."

    show Paul at leftPAUL
    with easeinleft
    with None
    PSA "And what about Leonor Valenzuela?"

    show Marco at rightMARC
    with easeinright
    with None
    MAC "She’s pretty, I’ll give her that. Though kind of… unapproachable? Gives me the impression of an ice queen,like one wrong move will set her off."

    PS "But that’s the appeal isn’t it? She’s “hard to get”-- cold until you melt her heart, then she’ll be as sweet as a kitten. It adds a bit of thrill to the chase."

    MAC "To each his own I suppose. Personally I prefer Leonor Rivera. She’s sweet and cute as a button, to boot. Being around her is like a breath of fresh air…!"

    "Marco looked off into the distance wistfully."

    JR "What are you guys going on about?"

    PS "The fiesta dance, of course! It’s all anyone could keep talking about these days."

    MAC "You got any plans of inviting someone, lover boy?"

    "I contemplated it for a second. There was Orang… though curiously my mind wandered to Rivera as well. Well, it’s always good to have backup right?"

    JR "Not at the moment, no."

    PS "You know, somehow I don’t believe a word of it."

    MAC "Yeah! Why don’t you leave some for the rest of us sorry fucks? We need all the help we can get. I can’t remember a time when a woman even looked at me without turning in disgust…"

    "Paul patted his depressed friend sympathetically."

    JR "Truth be told, I’m not sure if she’ll accept"

    PS "So what? Plenty of fish in the sea."

    MAC "Easy for you guys to say…"

    PS "Shut up, Marco. So, anyone you got in mind?"

    JR "I’ll… think about it some more and then get back to you on that."

    hide Paul
    hide Marco

    menu:
        "Orang":
            #Choice A: Orang Affection +1
            $ valenzuela_affection += 1
            pass

        "Rivera":
            #Choice B: Rivera Affection +1
            $ rivera_affection += 1
            pass

        "Neither":
            #Choice c: No Affection Added
            pass

    label C12_done:

    show Paul at leftPAUL
    show Marco at rightMARC

    PS "Whatever you say, Pepe. Speaking of which, what’s that you’ve been working on?"

    "I looked down at the stack of papers I was writing on."

    JR "It’s a collection of essays I’m planning to submit to the student paper."

    PS "Essays, huh? Can’t say I’ve ever read an essay from you. Though if they’re anything like your poems I’m sure they’ll get accepted."

    "Marco leaned closer to look over my shoulder."

    MAC "What’s it about?"

    JR "I was thinking a little bit about the way things are run here–"

    "I thought hard about how to word what I wanted to say without sounding too subversive. I had to lay on the ‘good boy’ act really thick. "
    "It wasn’t that I thought my friends would rat me out to a friar or anything like that, but I would rather not repeat the argument I had with Mariano again."

    JR "–Could be done better. The preferential treatment the faculty gives to Spanish students does a disservice to this prestigious institution."

    "Marco and Paul gave each other an unsure look."

    MAC "Well… you’re not wrong…"

    PS "But are you sure they’re going to allow you to publish this?"

    JR "I don’t see why not. All I’m saying is that if everyone can be on the same page here that the learning process is going to go a lot smoother. "
    JR "They don’t even teach Filipino students Spanish– which is required for most of our subjects. We had to learn that ourselves!"

    PS "I agree with you completely. Don’t get me wrong, it’s just I’m a bit worried they’ll accuse you of trying to undermine the school admin."

    JR "Well if they think so then they can just talk to me about it and I’ll clear it up for them. "
    JR "If I don’t say anything, then who will? And if they tell me that they won’t publish the article then I’ll just find another way to get people to read it."

    PS "Heh, you’re really something else, you know what? With that kind of attitude you’re going to get yourself in trouble one of these days."

    "I looked my friend straight in the eye."

    JR "Then that is an outcome I am willing to accept."

    PS "Alright, count me in! You need someone to find people to read your essays, I’m your guy. We’re not gonna let you do this all on your own, right Marco?"

    MAC "W-what? Why me?"

    PS "Don’t tell me all those times you said you’d give those old geezers a piece of your mind was just a load of hot air?"

    MAC "O-of course not! I meant every word of it! It’s just– Ah! What am I even saying? Fine! I’m coming too."

    "Paul came up behind me and Marco and wrapped both arms around our necks, bringing us all closer together."

    PS "Look at us, just a bunch of guys heading straight first for disaster. They better call us like some kind of Three Musketeers."

    JR "I didn’t know you read the works of Dumas."

    PS "I don’t. But that’s beside the point. We’re all in this together, right?"

    "I couldn’t help but smile at that moment, touched by the sentiment."

    JR "Right, together."



    #PLACE ====== INT. CASA TOMASINA - NIGHT

    scene bgBRN #is this correct?
    stop music
    play music "audio/Music/Almost New.mp3" loop
    with fade
    with None

    # For hiding unnessary characters
    hide Paul
    hide Marco
    # For hiding unnessary characters

    "I rubbed my tired eyes as I stared at the piles of paper on my desk. At the top of the figurative mountain was the essay I was supposed to submit to the student paper. "
    "I looked over it once more, finding myself unsatisfied with how it looked. Under it were some notes I made for class, each page scribbed with a hurried but legible cursive script."

    "It was until I looked to the edge of the table that I noticed the letters I had received that week but forgot to open. "

    play RustlingPap "audio/Voice/RustlingPap.mp3"
    "The first were from my parents, the usual small talk asking how I was and if I was doing well in school. “Give my regards to your Tiyo!” my father had said. "
    "Each one of my siblings sent me letters too, to varying lengths. Paciano just gave me a curt note and told me to study well."

    "When I had finished reading, I was surprised to find an envelope with no return address in the back. "

    play RustlingPap "audio/Voice/RustlingPap.mp3"
    "It had the vague smell of flowers wafting from it and the stationary looked decidedly feminine. I unfolded the letter."

    "{i}Dear Pepe,\nI hope this letter finds you well. I am told that today you will have settled down in your new boarding house.{/i}"
    "{i}Are you getting along with your boardmates? I find that it is important to develop connections with the people around you, as they may eventually help you in the future.{/i}"
    "{i}I am looking forward to the next time we meet. If you are free anytime soon, I’d like to see you.{/i}"
    "{i}Thank you as well for the flowers, they are lovely. How were you able to obtain the same type grown in the gardens of Doña Lizares? It must’ve been really expensive.{/i}"
    "{i}Speaking of Doña Lizares, my father informed me that recently there have been complaints from her about someone stealing her flowers.{/i} "
    "{i}You wouldn’t have anything to do with that, would you? I merely jest, of course.{/i}"
    "{i}Stay safe, Jose.\n\n{space=250}Yours always,\n{space=250}Orang.{/i}"
    #check the spacing again

    play WritePap "audio/Voice/WritePap.mp3"
    "I sighed. It seems like nothing can escape her sharp perception. I picked up my pen and quickly wrote a reply. "
    "As much as I’d like to say I was free immediately to meet with her, I wasn’t sure now that I had also agreed to spend time with Rivera. I hoped Orang would understand."
    stop WritePap

    "I also made sure not to answer her question about the flowers. Satisfied with my reply, I placed the newly written letter in the “To Send” pile and promptly went to bed."

    stop music

    #STOP SOME UNNECESSARY SFX######
    stop RustlingPap
    stop WritePap
    #STOP SOME UNNECESSARY SFX######

    #+++++++++   LEONOR VALENZUELA ROUTE: EPISODE 1   +++++++++++++++++++++++++++++++++++++++++++ Pages 39-47  of the Script +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    #"Playful songs of Love's delight,\nHe, too, murmurs his love's feeling\nIn the tongue he learned at birth."

    scene PreELV
    with dissolve
    pause(10.0)
    with None


    scene ttlP2LV
    with fade
    pause(3.0)
    with None


    #PLACE ====== EXT. CASA TOMASINA - DAWN

    scene bgBRN  #is this correct?
    stop music
    play music "audio/Music/Easy Lemon.mp3" loop
    with fade
    with None

    "That weekend, I woke up earlier than I expected. When I pushed aside the curtains of my window, I could barely see the sun peeking through the horizon, the sky still a dark shade of blue."

    "Yet despite that, I could not find it in myself to go back to sleep. Without anything else to do, I dressed myself, put on my shoes, and went downstairs."

    "To my surprise, I came down to find my boardmates shifting around furniture and trunks. It seemed that everyone had already woken up and were hard at work. "
    "Marco looked up from the heavy trunk he placed on the floor and waved to me."

    show Marco at leftMARC
    with easeinleft
    with None
    MAC "Hey, Pepe! Mind lending us a hand?"

    JR "What’s going on here?"

    MAC "We’re helping the new guy move into his dorm."

    JR "Is he someone we know?"

    MAC "I don’t think… so? Does the name Jose Cecilio ring a bell for you?"

    "I couldn’t help but laugh. Really, what were my odds? I did in fact know of him. Not that I could explain the circumstance of how we met."

    JR "Can’t say it does."

    MAC "Cool. So… are you gonna help out or…?"

    hide Marco

    menu:
        "Go to church":
            #Choice A: Orang Affection +1
            #Jose can say he has to go to church -> proceed to Leonor V's route.
            $ valenzuela_affection += 1
            pass

        "I'm free right now":
            #Choice B: Rivera Affection +1
            #if he says "I'm free right now" then he goes to Leonor R's route
            $ rivera_affection += 1
            jump LV_epi_1

    label C13_done:

    show Marco at leftMARC

    JR "Ah, sorry I gotta go to church today."

    "I did not need to go to church that Sunday, but I also didn’t want to carry furniture all day."

    MAC "Oh, I hear the barangay captain’s daughter always goes there too around this time."

    JR "Valenzuela?"

    MAC "That’s the one."

    "Without anything to do, I was sure she’d make better company than being by my lonesome like I originally intended."

    JR "In that case, I’m heading out. See you later."

    MAC "Don’t try to pull anything funny at church!"

    "I pointedly ignored Marco’s last statement."



    #PLACE ====== EXT. SAN AGUSTIN CHURCH - DAWN

    scene bgSAD
    with fade
    with None

    # For hiding unnessary characters
    hide Marco
    # For hiding unnessary characters

    play WalkCobble "audio/Voice/WalkCobble.mp3"
    "The walk to the church had been uneventful. It was still too early for any of the shops to be open, and only a few people could be seen on the streets. "
    "The sky was a little brighter than the near-night it had been a few minutes earlier."

    "The church was situated in the middle of a plaza, the cobblestone and dirt road crossing paths under the myriad of trees that dotted the area. "
    "The church was by no means as large as some of the other ones I had seen in Manila, but it still bore an imposing and solemn visage. "
    "Its edifices were carved into likeness of medieval saints, trapped between Corinthian pillars, and staring blankly down at me. "
    stop WalkCobble


    "I stared back into their eyes for a moment, and found that they too were dead. I pushed aside the giant wooden doors."

    #STOP SOME UNNECESSARY SFX######
    stop WalkCobble
    #STOP SOME UNNECESSARY SFX######


    scene bgSAI
    play ChurchDOC "audio/Voice/ChurchDOC.mp3"
    with fade
    with None

    "The exterior did not do justice to the sheer splendor of the interior of that church. "
    "Inside, one could find themselves teleported to a remnant of a bygone age, far away from the rustic locale of the Philippines. "
    "Crystal chandeliers hung from the majestic domed roof, and religious artifacts gilded in gold were displayed alongside the pews. "
    "It was far more luxurious than anything one would find on the outside, where beggars and thieves would scrape for food. "
    "I wasn’t sure if what I felt in that moment was awe or revulsion for it all."


    play music "audio/Music/Danse Morialta.mp3" loop
    "I could make out the dark outline of a woman kneeling before the golden altar, her hands clasped together with a rosary. "
    "Leonor Valenzuela was as still as a statue, and the sharp lines of her face gave her the quality of being one too. "
    "Below her, the maroon fabric of her skirt pooled outward like blood on the marble floor."

    "I kneeled alongside her, and neither said a word. I could see a priest scurrying off to the side of the hall. The two were alone."

    JR "I never took you to be a pious type."

    show LValenzuela at leftLV
    with easeinleft
    with None
    LV "And I never took you to be the type to stalk a woman during her time of prayer."

    "The light of the candles illuminated the smirk she had on her face."

    JR "What can I say, there’s a lot about me you don’t know."

    LV "I could say the same for myself."

    JR "They call you the ‘dutiful daughter of the respected barangay captain’, you know."

    LV "Is that so? And perhaps it was from one of these people that you learned of my ventures here?"

    JR "It’s not like it’s a well-kept secret."

    LV "How typical."

    "Her face became blank once more."

    LV "So why have you come here, Jose? I don’t assume you wish to pay respects to the Virgin Mary."

    JR "To see you, of course."

    LV "I thought you were busy."

    JR "Ah… Right–"

    show cgCMT
    with fade
    with None
    "From the corner of my eye I saw her shoulders shake with restrained laughter."
    hide cgCMT
    with fade
    with None

    LV "I’m just messing with you, Pepe. There’s no need to be so tense. I’ve missed you too."

    "I pouted in mock offense."

    JR "You can be quite cruel, my lady. Do you not have it in you to show me some mercy, sometimes?"

    LV "And where’s the fun in that?"

    JR "Do you really come here often?"

    "She paused for a moment, looking straight ahead at the statue of Mary in front of us."

    LV "Well you see, good girls of good standing are taught that they must pray daily to the good Lord Jesus Christ. "
    LV "They must always recite their prayers and be docile and submissive so that they might attract a good husband, who will grant his seed and give them children. "
    LV "Then her purpose will have been fulfilled as a good woman."

    "Leonor sounded remarkably bored as she parroted what sounded like the words of someone else."

    JR "That doesn’t really answer my question."

    LV "That depends, are you really interested in knowing what I think? Or are you just asking to humor me?"

    "I wasn’t sure what came over Orang at this time. Normally she would be a bit standoffish towards my advances, but it wasn’t anything like this. "
    "This somehow felt like a test, like the church walls have stripped away the pleasant and polite shell of Leonor Valenzuela to reveal her true self– A woman who was always watching you. "
    "Whose gaze pierced through your flesh and tore you open for examination. At that moment, I felt not unlike the frogs I dissected in Natural Science class. "
    "It was… unsettling. I turned to stare at her dark impassive eyes, searching."

    JR "Now you’ve got me really curious."

    "Orang laughed quietly, her lips curving into a sly smile."

    LV "Then come with me to the back gardens. But make sure you pray aloud a single Hail Mary before you do so, we cannot be seen leaving the doors at the same time."

    JR "Very well."

    hide LValenzuela at leftLV
    with easeoutleft
    with None
    "Orang stood up and left. I did exactly what was instructed, reciting the verses I learned from childhood without thinking much about it at all. "
    "While my lips moved in holy prayer, my mind took instead to sordid matters. The smile she gave me flashed in my head again, and the unspoken agreement between us."


    #STOP SOME UNNECESSARY SFX######
    stop ChurchDOC
    #STOP SOME UNNECESSARY SFX######

    scene bgSAL
    with fade
    with None

    "Once I was done, I headed out from the backdoor into the gardens beside the church. Orang sat demurely on a stone bench, in her hand was the rosary she clutched whilst she prayed. "
    "It was made up of fifty wooden beads in total with a cross at the end of it. Orang stared at it intently before looking up at me."

    show LValenzuela at leftLV
    with easeinleft
    with None
    LV "I had to believe a great deal in God, because I had already lost my belief in men."

    "I stared at her in surprise, not expecting such a cynical response."

    JR "You say that as if most people you’ve met are bad."

    LV "Not bad, or even evil. Just selfish. At the end of the day, people will hear only what they want to hear. If it has nothing to do with them, then they care not to know about it. "
    LV "The flimsy house of cards holding up their worldview works fine just for them. But that does not make them evil– it makes them ignorant. "
    LV "The only ones who would say all men are evil would be this fine establishment."

    JR "You’re right, I do agree with you. After all, if we were made just to go to hell like the church says then we wouldn’t have the capability to do good things."

    LV "You think hell is a place."

    JR "What else would it be?"

    LV "Hell is a state of mind. It isn’t a place you can go to or escape. "
    LV "When a person commits a sin, or has a sin committed against them– then they are in hell. If you wish, you may even create your own hell wherever you go. "
    LV "The gospel of God, Gold, and Glory created the hell we currently live in."

    "The might of Spain that crushed them all like a mace…"

    JR "You know, when I came out here I didn’t expect this would be the kind of conversation we would have."

    LV "Disappointed?"

    JR "Not at all, it’s actually a relief. I know for sure now that I am in good company."

    "For the first time that day, Orang gave me a sweet smile."

    LV "I’m glad."



    #PLACE ====== INT. CASA TOMASINA - NIGHT

    scene bgBRN #might be casa tomasina at night or I'm correct
    with fade
    with None

    # For hiding unnessary characters
    hide LValenzuela
    # For hiding unnessary characters

    "That night, I looked down at the wooden rosary in my hand and was reminded once more of the events that transpired that day. Was Orang opening up to me more? I felt that was the case."

    "I didn’t know what to make of her statements in the garden, it seemed that she was inviting me to question everything she said. It was like a puzzle I couldn’t wrap my head around."

    "On one hand was the carefully cultivated image of a well-mannered and bred lady, befitting of the status of a Valenzuela. "
    "On the other hand, there was a curious lack of respect for the status quo, a deep bitterness that colored her tone whenever she spoke of the things that were expected of her."

    "I wanted to understand her more."

    stop music


    #+++++++++   LEONOR VALENZUELA ROUTE: END EPISODE 1   +++++++++++++++++++++++++++++++++++++++++++ Pages 47-52  of the Script +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    #PLACE ====== INT. SANTO TOMAS - DAY

    scene bgLB
    play music "audio/Music/Tango de Manzana.mp3" loop
    with fade
    with None

    "Class was dismissed earlier than usual, much to my relief. It seemed that Friar Balsemo didn’t even want to bother teaching any lessons and just assigned us some readings in history that day. "
    "I had gone to the library shortly thereafter to borrow a book relating to the topic that I had to study for, but found that Lizares had gotten to it first."

    show Javier at rightJA
    with easeinright
    with None
    JL "Oh, it’s you."

    "I looked at the book in Javier’s hand."

    JL "Here for the assigned reading too?"

    JR "Unfortunately, I do not have untold riches for which to buy my books."

    "For some reason, that jab looked like it annoyed the other boy more than usual. Javier’s eye twitched. "

    JL "Tch. You’re a real piece of work, you know that Rizal?"

    JR "I try my best. Besides, what are you doing here anyway? I would’ve assumed you already read the material."

    JL "What? Can’t I use the school facilities in peace without some know-it-all questioning my every motive?"

    "I rolled my eyes."

    JR "Alright, since we’re both here and we both need that book– how about I propose a truce? Let’s put aside our differences because I honestly would rather not get into a fight with you right now."

    JL "Funny, that’s the smartest thing you’ve said all day. Agreed."

    "We both dropped our bags on one of the tables that lined the university library and sat across from each other. Javier placed the book between us."

    JL "You go first. You need it more than I do."

    JR "Your generosity knows no bounds, my liege."

    JL "Just get on with it already."

    "Didn’t need to tell me twice. I got straight to opening the relevant chapter. Predictably, the lesson was about the ‘glorious’ history of Spain’s rule in the Philippines. "
    "There wasn’t much on the Philippines prior to that, or if there was it had probably been destroyed by the {i}conquistadors{/i} that landed on our shores all those years ago. "
    "So many things had been lost to the abyss of time, out of the reach of the people of today who look back and saw our ancestors as merely primitive."

    "The following chapter dealt with the landing of the Portuguese explorer Magellan and his circumnavigation across the world. "
    "An impressive feat, admittedly, but not the focus of the lesson. What was more interesting was what he found at the end of his journey: The Philippines."

    "At the time, the Philippines was less a nation and more of a collection of interconnected but disparate ethnic groups ruled by Datus or chieftains. "
    "The exception to this was the southern largest island, Mindanao, which was instead ruled by a Sultan and followed the teachings of Islam."

    JR "To say that the subjugation of the Philippines by Spain is a result of natural racial superiority is a mistake."

    JL "Huh? What are you talking about?"

    JR "Oh I was just thinking out loud."

    JL "No, I meant by what you said."

    JR "Exactly that. The author of this book made an error in his interpretation of the events of the Battle of Mactan."

    "Javier didn’t look convinced or impressed."

    JL "Oh yeah? And I bet you’re about to tell me what it is."

    JR "The way the events are written here leads the reader to believe that the conquistadors just walked into the Philippines, "
    JR "Crushed all resistance, and claimed the country in the name of King Philip II. "
    JR "That it was the will of God that they succeeded."

    JL "And?"

    JR "But the truth of the matter was that they had played local politics to gain dominance over the natives. "
    JR "Lapulapu, the Datu of Mactan who would come to kill Magellan, was the rival of another chieftain Raja Humabon. "
    JR "Magellan’s party acted like neighbors, accepted the hospitality of the Filipinos, and then offered to ‘deal’ with their enemies as a token of goodwill. "
    JR "They had the opportunity to ingratiate themselves to the people they would soon subjugate, it had nothing to do with moral or racial superiority."

    JL "You call yourself a Filipino, you and the other natives of this country."

    JR "That’s right."

    JL "The reason you can call yourself that is only because of Spain. The term itself was named after a Spanish king and given originally to Spaniards born in the Philippines. "
    JL "One could argue that the fact the people were so regionalistic and constantly warred amongst themselves necessitated just cause to unite them under one nation. "
    JL "Otherwise, regional differences would’ve ensured that they’d be divided and weak– ripe for the picking of another sovereign nation if not Spain."

    JR "There was no way for the Filipinos to become united because of the ‘divide and conquer’ strategy that was employed on the Spanish side."

    JL "That’s exactly right. Because there was no reason for the groups to work together. In the first place, it wasn’t something they anticipated to be a sufficient threat. They were wrong."

    "My face scrunched in distaste."

    JR "It sounds like you are arguing that colonization was the catalyst for the birth of a national identity."

    "Javier shrugged."

    JL "Who knows? Maybe it is, maybe it isn’t. What’s important is that we are a part of Spain, isn’t it?"

    JR "Are we, really? The mainland would claim that to be so, and yet refuse to grant us the same rights and privileges enjoyed by Spaniards from the peninsula. "
    JR "The extent that the Philippines ‘belongs to Spain’ only goes as far as how it can exploit us."

    "Javier’s blue eyes narrowed dangerously then."

    JL "Careful, Rizal. If I didn’t know any better I’d say you’re suggesting a revolution would be the solution, right?"

    "I looked at him for a moment, before laughing."

    JR "Not at all. That’s not the kind of fight we can win."

    JL "Good to know you’re smarter than you look."

    "The both of us fell into uneasy silence then, before Javier took out his pocket watch and balked at the time."

    JL "Damn it. I’m going to be late! Here, you can have the book."

    JR "Got somewhere to be?"

    JL "Yeah, it’s called {i}\“none of your business\”{/i}."

    hide Javier at rightJA
    with easeoutright
    with None

    "I waved a hand dismissively at the other boy, and flicked through another page of the history book. From the corner of my eye I could see Javier looking almost… nervous. "
    "But it held a tinge of excitement that manifested in the curve of Javier’s mouth. Was that a smile I could see?"

    "{i}‘Maybe he’s meeting with his girlfriend or something. Not that I care.’{/i}"

    "Javier took one look at me and left without saying another word. Typical. I wasn’t even surprised anymore at the antipathy the other boy felt for me."

    "And yet, the conversation we had also got me to think about what he meant about a ‘national identity’. "
    "Even if it wasn’t something that existed before the Spaniards, it didn’t feel right to simply accept an identity that is foisted upon us by the same powers that oppressed us. "
    "According to them, the indio is indolent, lazy, and backwards when that couldn’t be farther from the truth."

    "Self determination is something that should be decided by the individual themselves, and in the case of the group– by the group. Not by an outside third party that had an obvious agenda."

    "I smiled sardonically. Javier was kind of right, just not for the reasons he thought he was."

    stop music

    jump LV_Interlude


    #+++++++++   LEONOR RIVERA ROUTE: EPISODE 1   +++++++++++++++++++++++++++++++++++++++++++ Pages 52-67  of the Script +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    #"For I am a plant immature,\nTorn out of the Orient where\nThe perfumes sleep on the air\nAnd life is a dream to allure.\nAh, memories ever endure,\n"





    #PLACE ====== EXT. CASA TOMASINA - DAWN

    scene bgBRN
    with fade
    with None

    "That weekend, I woke up earlier than I expected. When I pushed aside the curtains of my window, I could barely see the sun peeking through the horizon, the sky still a dark shade of blue."

    "Yet despite that, I could not find it in myself to go back to sleep. Without anything else to do, I dressed myself, put on my shoes, and went downstairs."

    "To my surprise, I came down to find my boardmates shifting around furniture and trunks. It seemed that everyone had already woken up and were hard at work. "
    "Marco looked up from the heavy trunk he placed on the floor and waved to me."

    show Marco at leftMARC
    with easeinleft
    with None
    MAC "Hey, Pepe! Mind lending us a hand?"

    JR "What’s going on here?"

    MAC "We’re helping the new guy move into his dorm."

    JR "Is he someone we know?"

    MAC "I don’t think… so? Does the name Jose Cecilio ring a bell for you?"

    "I couldn’t help but laugh. Really, what were his odds? I did in fact know of him. Not that I could explain the circumstance of how we met."

    JR "Can’t say it does."

    MAC "Cool. So… are you gonna help out or…?"



    #JUMP JUMP JUMP here from Valenzuela Route

    label LV_epi_1:

    show Marco at leftMARC

    "Although I didn’t feel like carrying heavy furniture all day, a part of me felt a little awkward to be standing around while everyone else worked."

    stop music
    play music "audio/Music/Tango de Manzana.mp3" loop
    JR "…Sure. Hand me that trunk."

    "I bent down to grab the handles of the trunk and pulled. "
    "To my despair, I found that I had to expend considerable effort just to even lift the damn thing. Since when was I so out of shape? "
    "Marco looked at me with an amused smile."

    MAC "Doing alright there, buddy?"

    "I gritted my teeth, unable to admit defeat."

    JR "Never been better."

    MAC "Great! Then you can help me bring it upstairs to Cecilio’s room. Don’t give me that look, I’ll be carrying the other end."

    "The other boy took half the load from me as we started our arduous trek to the second floor. By the time we reached there, I was already winded and breathing heavily. "
    "I gave an incredulous glare at Marco who seemed just fine. I made a quiet promise to myself to exercise more in the future."

    "We dropped the trunk at the threshold of Cecilio’s room when the door swung open to reveal the man himself." # creaking sound of a door opening

    show JCecilio at rightJC
    with easeinright
    with None
    CE "Hey thanks for helping me carry my luggage and all– JOSE?!"

    MAC "Well look at this, Jose meet Jose. Now both of you must duel to the death to assert who’s the dominant one."

    JR "As if, I’m obviously the cooler Jose."

    CE "This is crazy, man. I had no idea you were boarding here too."

    MAC "Wait, you two know each other? But you said you never met him."

    "I glared at Cecilio, silently pleading with my eyes to ‘just go along with it!’. Thankfully, Cecilio caught on quickly enough before laughing in an obviously forced way."

    CE "Well… uhh… I know of him but we’ve never actually gotten to talk until now."

    MAC "Oh? And where did you two meet?"

    JR "The market."

    CE "What he said. He was looking at eggplants to give to his lady friend."

    "My eyes nearly popped out of their sockets. What is this idiot saying? Cecilio looked entirely unrepentant even as Marco burst into laughter."

    MAC "You’re pretty funny, man! The name’s Marco. If you ever feel like hanging out with me and the boys, we’d love to have you around."

    CE "Thanks. Pleasure is all mine."

    "I resisted the urge to groan even as the two shook hands. I couldn’t even contradict the statement because it’d completely undermine the bullshit we’re trying to spin. "
    "There was no two ways about it, I owed Cecilio and we both knew it. So if Cecilio wanted to be petty and embarrass me then let him do it. "

    hide Marco at leftMARC
    with easeoutleft
    with None
    "After a short moment of chitchat, Marco went back downstairs, leaving me and Cecilio alone."

    JR "Eggplants."

    CE "Sure beats getting smashed by the Guardia."

    JR "Fair."

    CE "If you’re worried that I’m going to rat you out, don’t be."

    "And I was, what? Supposed to just take him at his word? Not like I had a choice but to trust the boy."

    JR "If I didn’t know any better I’d think you were stalking me."

    CE "You wish. I’m not one of your many girlfriends that tail after you. Speaking of which– how exactly are you so popular?"

    JR "What’s {i}that{/i} supposed to mean?"

    CE "What I mean is that– hey no offense— is that you’re not exactly a tall rich handsome guy."

    JR "I really don’t want to hear something like that from you."

    CE "And yet you’ve got women flocking. How do you do it? You’re like 5 foot 3. Even I’m taller than you."

    JR "Wouldn’t you like to know, garden boy?"

    CE "C’mon. Tell me."

    JR "I don’t know. What will I get out of it if I do? All this time you’ve just been antagonizing me."

    CE "Hey, you’re gonna want to be friends with me. I can be a very useful ally whenever you need it."

    JR "And in exchange you want me to tell you my “secrets” for attracting women?"

    CE "That’s right."

    JR "Pfft..!"

    "I couldn’t help it. It was like a dam bursting open and I couldn’t hold back my laughter."

    JR "You-! Aha, you can’t be serious!"

    "The serious expression on Cecilio’s face told otherwise."

    JR "Good lord. You really must be desperate to be asking me about this."

    CE "And so what if I am?! Do you have any idea what it's like to be sad and lonely? To never feel the pleasure of a warm bosom on your cheeks?! Don't you have a heart?"

    "I gave the other boy a look of contempt."

    JR "Can't say I have."

    CE "And that's exactly why you can never understand the common man's struggle."

    JR "Look, alright, enough of this. I'll help you out."

    CE "You will?!"

    JR "Keep in mind that I won't be doing this for free."

    CE "You're going to charge this poor boy money?"

    JR "No, we'll be exchanging information. I tell you what I know and if I need your help you'll oblige."

    CE "Heh, that's it, then? You got a deal."

    "Cecilio reached a hand forward, I took it in my own in a shake."

    JR "Really hope I won't end up regretting this."

    "The other boy gave me an easy assured smile."

    CE "You won't."

    stop music


    #PLACE ====== INT. CASA TOMASINA - NIGHT

    scene PreELR
    with dissolve
    pause(10.0)
    with None

    scene ttlP2LR
    with fade
    pause(3.0)
    with None

    scene bgBRN
    stop music
    with fade
    with None

    # For hiding unnessary characters
    hide JCecilio
    # For hiding unnessary characters

    "I threw myself onto my bed, shoes and all. I didn’t have the energy to move at that moment. "
    "A dull ache throbbed on my lower back and I groaned, regretting the moment I agreed to help Marco carry heavy furniture. "
    "I really overestimated myself this time and pushed my body way too hard."

    play KnockDoor "audio/Voice/KnockDoor.mp3"
    queue KnockDoor "audio/Voice/KnockDoor.mp3"
    "A tentative knock came from my door. I didn’t feel like getting up to answer it. Another knock."

    JR "Yeah just come in already!"

    play DoorOpen "audio/Voice/DoorOpen.mp3"
    "The door cracked open slightly, where I saw a pair of big brown eyes peeking through it. " #creaking sound of a door opening

    show LRivera at leftLR
    with easeinleft
    with None

    play music "audio/Music/Dream Culture.mp3" loop
    LR "Jose? If you’re busy, I can come back another time?"

    "I immediately jumped out of bed, the whiplash of the action causing my back to crack painfully. I winced."

    JR "No! No, not at all. I’m not busy right now."

    LR "Okaayy…"

    "Leonor stayed outside my room, a tray of snacks in hand. I rifled through my drawers and pulled out a first aid kit. "

    #AZOTEA BG????????????
    #AZOTEA BG????????????
    #AZOTEA BG????????????
    #AZOTEA BG????????????

    "The two of us then took the short walk to the next room which was the azotea."

    "Ramoncito followed shortly after, his white furry tail standing straight up as he strutted in like he owned the place. Leonor looked a bit out of place as she shuffled awkwardly."

    LR "I brought you these snacks… as a way to y’know, pay you back for agreeing to teach me some first aid. But it seems like you’re really tired right now, are you sure it’s okay?"

    "Ah… right. I had almost forgotten about my agreement with Leonor what with all the stuff happening lately. "
    "Although a part of me just wanted to go to sleep already, I couldn’t bring myself to say no when my cousin was giving me those watery big doe eyes."

    JR "Right, yeah it’s no problem at all. Just put the tray on the table over there and then we can start. Do you have any ideas for what you want to learn first?"

    "As Leonor placed the tray of biscuits on the table, she paused with her back to me."

    LR "Umm… Just the basics first."

    JR "The basics, huh."

    "It was clear then that Leonor had no idea what she was talking about."

    JR "Let’s start with sprains first. A sprain is what happens when an injury tears the fibers of a ligament. "
    JR "The most common type of sprain are ankle sprains and they swell rapidly and are painful. If it's minor you can treat it yourself."

    "Leonor nodded and pulled up a chair in front of me, listening with rapt attention as she pulled a notebook and pencil from the pocket of her skirt."

    "I pulled one of my first aid kit open to reveal a first aid kit I kept for emergency situations. I took out an empty cold compress and a roll of bandage for demonstration."

    JR "To easily remember the steps, it’s helpful to shorten the procedure to the abbreviation ‘R.I.C.E’"

    LR "Rice?"

    JR "Yes! It’s short for \“Rest, Ice, Compression, and Elevation.\”"

    "Leonor scribbled furiously on her notebook."

    JR "In fact, I think it’d be better if I showed you through a demonstration."

    LR "Demonstration? What do you mean?"

    JR "If you’ll act as my patient for a bit, I can show you all the steps in a way that’s easy to remember."

    "Leonor froze, her face taking on an interesting shade of red."

    LR "What would you have me do? Lie on your bed!? Are you going to do something lewd to me?"

    "I sputtered. I didn’t think of that until she mentioned it!"

    JR "What? No! I’ll keep my hands to myself, okay? Just put your ankle on the edge of the stool so that I can elevate it."

    LR "Ahhhh, you better keep your promise! I’m trusting you this time!"

    show cgKNLNNM
    with fade
    with None
    "She plopped her dainty foot on the edge of the a stool, her long skirt pulled back very slightly to reveal her pale bare ankle. "
    "Her lips were pulled into an embarrassed pout, her head turned away to look anywhere else except me. There was something about it that endeared me greatly."

    JR "I’m going to touch your foot, okay?"

    "She nodded, still determined not to meet my eye. I sighed."

    JR "If you’re to look somewhere else instead of paying attention then I don’t see the point of doing this at all."

    LR "Fine! But don’t you feel embarrassed at all by this?"

    JR "What kind of doctor would I be if the sight of another person’s body was enough to make me nervous?"

    LR "…Point taken."

    "Another thing for me to file away later."

    JR "Right, so the first step is pretty obvious. "
    JR "It stands for Rest. You should avoid putting any weight on the injured area for 48-72 hours, so you might need the help of crutches, a splint, or brace. "
    JR "Don't forget to keep moving the muscle though to minimize deconditioning, just make sure to keep the exercise light and easy so you don't worsen the injury."

    "The initial nervousness that showed in her face melted and her expression took on a more inquisitive look."

    JR "The next step is to use a cold pack."

    "I brought the empty cold compress and placed it above Leonor's foot."

    JR "Ice the area by applying a slush bath or compression sleeve filled with cold water to help limit swelling after an injury. "
    JR "It's important to do this as soon as possible after the injury for about 15-20 minutes, four to eight times a day, for the first 48 hours until it improves. "
    JR "Another thing to remember is to not use the ice for too long or else you'll cause tissue damage."

    "As I held the compress with one hand and her foot with the other, I couldn’t help but notice how soft her skin was. "
    "As much as I said that I was planning to become a doctor–a professional!-- I also wasn’t being completely honest in denying that the sight of her lower leg didn’t affect me at all. "
    "I tried my best to keep my eye from roaming anywhere else."
    hide cgKNLNNM
    with fade
    with None

    "My eye caught Leonor’s and I quickly coughed. Leonor stared at me with a blank yet searching expression."

    JR "Next is compression. Wrap the area tightly– tho not too much– with a bandage."

    LR "What happens if you don’t have any in hand?"

    JR "A strip of cloth will do. Not ideal, of course, but if you have no choice then at least make sure it’s sterilized first."

    LR "Got it."

    "I picked up the roll of bandages from the bed and gestured in a way that looked like I was wrapping it around her foot. "
    "I didn’t literally do it as it would be a waste of perfectly good bandages just for a demonstration."

    "All the while, Leonor seemed genuinely interested in the lecture– to my surprise. I initially thought of her request to learn first aid as a passing fancy of a bored upper class girl. "
    "Something to occupy her attention before she inevitably got bored and moved on to something else like sewing or whatever."

    "Still, it was too soon to say whether she would stick around to learn more. I couldn’t help but realize I was having fun too. "
    "There was something to be said about how teaching someone helped you remember your lessons better."

    JR "Last step is to elevate the injured limb above your heart whenever possible to limit swelling. That’s about it. Simple, right?"

    LR "Yes! I didn’t expect it to be so simple. When you see doctors work it almost looks like what they’re doing is magic. But it’s far from it."

    JR "Don’t get too excited now, I’m only teaching you basic first aid. If things get really serious then you’re still going to have to consult a real doctor anyway. "
    JR "There’s a whole lot more to medicine than just this, and it requires years of study just to learn even one discipline. "

    LR "I understand. Thank you for taking the time to teach me all this. I feel like I understand you a bit better now."

    "That made me pause. When I looked up at her I found her smile to be too brilliant. It was like I had given her a beautiful gift, just the simple act of spending time with her. "
    "The sparkle in her eyes held such a wholesome joy at learning something new that I found myself getting embarrassed. "

    "When I learned things in school it always felt like a chore. "
    "I wanted to become a doctor to help my ailing mother’s poor eyesight, so the tedious act of studying for tests and exams was just a means of doing that. "
    "But it was rare that I ever found myself to be as happy to have learned something new as what I saw in Leonor now. Perhaps when I was a child I did, but overtime the magic faded when I grew up. "
    "Things became predictable, boring even. Information was collected for functional use later, and not just for the simple desire to learn for its own sake."

    "I couldn’t help but feel like I had taken it all for granted. I should be grateful that I got to study at a good school and get an education instead of feeling annoyed at all my workload. "
    "Not everyone had the opportunity to do so. In fact, the average Filipino didn’t even get to pursue higher education."

    "And despite how beautiful Leonor looked in that moment, I couldn’t bear to stare at her any longer for shame at myself."

    JR "No, thank you. I’ve also learnt some important things today."

    LR "Hehe! It’s the least I can do. If we’re learning things from each other then that means we’re getting along."

    JR "Right, though I wonder what makes you think we’re not."

    LR "Well, it’s kind of hard to talk to you sometimes. I’m not sure how to strike up a conversation."

    JR "Are you shy to talk to others?"

    "Leonor blushed."

    LR "It’s not that exactly… just that I haven’t gotten the chance to talk to others who aren’t girls my age. "
    LR "I’ve been too busy with school and going to after-class tutoring lessons that I haven’t had the time to meet new people."

    JR "I can introduce some of my friends to you, I think you’d like them– they’re all good guys."

    LR "Really? I’d love to!"

    "I thought of the group of boys I hung out with, “The Three Musketeers” as Paul put it. Well, I supposed it would actually be four musketeers now since Cecilio is part of the group. "
    "Though now that I thought about it, I’d really rather Leonor not meet Marco after remembering the weird love-struck speech he made about her a few days ago."

    JR "It’s no problem at all."

    play Crack "audio/Voice/Crack.mp3" volume 5
    "The both of us made to stand from where we were seated, only for me to stand up too quickly that an audible ‘crack’ was heard. "
    "I winced painfully and groaned, rubbing my lower back like a terminally old man."

    LR "Pepe? Are you okay?"

    JR "It’s… It’s nothing."

    "It was not nothing. It hurt like hell!"

    LR "It’s not nothing if you’re looking like that! Here, let me help you."

    "Before I could react, Leonor was already behind me. She grabbed my left shoulder with one hand and pressed the other to my spine and pushed."

    play Crack "audio/Voice/Crack.mp3" volume 7
    "{i}CRAAACK!{/i}"

    "I involuntarily let out a low moan, to my complete and utter embarrassment. We both froze at the sound."

    LR "Anyway I gotta go, bye!"

    hide LRivera at leftLR
    with easeoutleft
    with None
    "The girl practically ran out of the room, leaving behind the tray of snacks and even Ramoncito. The cat stared at me from its perch on the table, almost as if in judgment. my face burned."

    "I twisted my shoulder a bit and found to my surprise that it no longer ached. I chuckled in amusement. Guess she had a few tricks up her sleeves too."


    #STOP SOME UNNECESSARY SFX######
    stop KnockDoor
    stop DoorOpen
    stop Crack
    #STOP SOME UNNECESSARY SFX######

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++[END EPISODE 1]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    #+++++++++   LEONOR RIVERA ROUTE: (INTERLUDE)   +++++++++++++++++++++++++++++++++++++++++++ Pages 68-75  of the Script +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    label LV_Interlude:

    #PLACE ====== EXT. ??? - NIGHT???

    scene cgINT2-1
    stop music
    play music "audio/Music/SCP-x3x I am not OK.mp3" loop
    with fade
    with None

    # For hiding unnessary characters
    hide Javier
    # For hiding unnessary characters


    "That night, I dreamed."

    play Shovel "audio/Voice/Shovel.mp3"
    "I stood above the crumbled earth, eerily still, as the shovel hit the soil again and again with a ‘clack’. "
    "The lantern in my hand illuminated the harsh frown on my face, the flickering of the candlelight morphing the shadows into inhuman shapes. "

    "Clack. Clack. Clack."

    "I snarled."

    ME "What have you done with my father, you ingrate?"

    scene cgINT2-2
    with fade
    with None

    stop Shovel
    play Shovel2 "audio/Voice/Shovel2.mp3" volume 5
    "The gravedigger stopped what he was doing, stabbing the shovel into the ground as he wiped the sweat from his temple. He gave me a hideous yellowed smile."

    GVD "Threw him into the river, I did."

    ME "You were ordered to transfer him to the Chinese cemetary."

    "The old man spat on the ground beside my shoe."

    GVD "It’s bad enough he was born a Filipino, but to be buried with the Chinese is worse."

    "The both of us watched as Father’s body was carried away by the currents. After a brief moment, it finally succumbed to the depths."

    #STOP SOME UNNECESSARY SFX######
    stop Shovel
    stop Shovel2
    #STOP SOME UNNECESSARY SFX######

    #PLACE ====== INT. SANTO TOMAS - DAY

    scene bgSTO
    stop music
    play music "audio/Music/Tango de Manzana.mp3" loop
    with fade
    with None

    play WintaBells "audio/Voice/WintaBells.mp3" volume 5
    "My train of thought was broken when I heard the ringing of bells that signaled the start of noon prayer. "
    "The rest of the class stopped what they were doing to fall into silence and form the sign of the cross on their chests. "
    "I did the same, if only not to stand out like a sore thumb, though my mind was elsewhere."

    "As the prayer ended, I was about to pick up my notes and bag when I once again caught the tail end of what seemed like an argument between Javier and his minions. "
    stop WintaBells
    "It would’ve been unusual by itself, since Daniel and Ignacio were such suck ups that I was sure they must’ve had their spines surgically removed right before enrolling in this school. "
    "What made it more surprising was what Daniel had said."

    show Daniel at leftDAN
    with easeinleft
    with None
    DS "Ehh?? What do you mean you won’t {i}libre{/i} us today?"

    show Javier at rightJA
    with easeinright
    with None
    JL "You heard me, I can’t just keep treating you guys to free food all the time. Don’t you have your own money anyway?"

    show Ignacio at semileftIG
    with easeinleft
    with None
    IG "Wow, never took you to be such a stingy guy."

    DS "Though I guess I should’ve expected it from a guy who comes from a family like yours."

    JL "Watch your tongue!"

    DS "Or what? You’re not on top in class anymore, Lizares. "
    DS "I thought I’d keep you company out of pity but since you won’t even show any gratitude for my friendship I don’t see why I should bother anymore."

    hide Daniel at leftDAN
    with easeoutleft
    with None
    "Daniel left."

    JL "Tch. Let me guess, you’re also the same, Ignacio?"

    IG "Eh, my parents told me to leave you be. Speaks badly of our reputation to be seen with you these days. Try not to take it so personally."

    JL "You really got some fucking nerve. Go, I don’t need you two stooges anyway."

    IG "Pride can only get you so far, Javier. One day you’ll find yourself alone with no one to call your ally."

    hide Ignacio at semileftIG
    with easeoutleft
    with None
    "This time it was Ignacio’s turn to make his leave. I saw Javier silently fuming in his seat, a lacquered wooden box in his lap. "
    "‘Never thought a guy like him would need to bring boxed lunches to school’."

    "As interesting as that exchange was– “interesting” being a generous way to describe it– I didn’t find it in myself to be particularly invested in what I saw. "
    "It was only a matter of time before Javier’s rat bastard friends would show their true ugly colors. Javier had no one but himself to blame for choosing such terrible company."

    "I gave one last side eye to the sullen boy before leaving the class."

    #STOP SOME UNNECESSARY SFX######
    stop WintaBells
    #STOP SOME UNNECESSARY SFX######

    #PLACE ====== EXT. PUBLIC MARKET - DAY

    scene bgSTR  # check if this is correct or it needs to be Public Market?
    stop music
    play music "audio/Music/Easy Lemon.mp3" loop
    with fade
    with None

    # For hiding unnessary characters
    hide Javier
    # For hiding unnessary characters

    play Market "audio/Voice/Market.mp3"
    "Cecilio and I had planned the other day to meet up in the public market after classes. "
    "I had a bit of spare cash left to spend on other things aside from school supplies and food so I decided now would be a good time to buy some presents for my special girl. "
    "Cecilio just decided to tag along for whatever reason, citing the ‘importance of learning from a master at work’ or some nonsense like that."

    "By the time I had arrived at the meeting spot, Cecilio was already there and waved back at me. "

    show JCecilio at leftJC
    with easeinleft
    with None
    CE "Hey, you ready to go or what?"

    JR "How long have you been waiting here?"

    CE "Just a couple of minutes I think."

    JR "Alright then. Let’s go, Cecilio."

    CE "There’s no need to be so formal haha"

    JR "I can't just call you ‘Jose’. It’d get confusing for both of us to have the same name."

    CE "Then call me “Chenggoy”. That’s what my friends call me."

    JR "That’s a pretty weird sounding name. Makes you sound like a monkey."

    CE "Hey! Don’t be rude! My mother gave it to me. I would’ve thought a guy like you who goes to a fancy high-class school woulda learned some manners. But you’re just as rude as a hoodrat."

    JR "I really don’t know what to tell you. You could probably say that I’ve progressively lost it in me to care anymore about propriety."

    CE "So it’s just a front, then? You clean up real nice with your suits, shiny shoes and fancy degrees but on the inside you’re no different from me."

    JR "If you say so."

    CE "So anyway, why are we here again?"

    JR "To get a present for someone."

    "“Chenggoy” gave me a cheeky smile."

    CE "Oh? So which is it, Leonor or Leonor?"

    JR "Leonor."

    CE "HAH! Good one. It’s kind of genius, in a way. If you were to accidentally cry out the other woman’s name, they would be none the wiser."

    "I gave a long suffering sigh."

    JR "Leave it to Chenggoy to lead his mind to the gutter."

    CE "What? So you never thought about it? Sounds like a load of bull."

    JR "There’s a lot more to romance than scheming to get under women’s skirts."

    CE "Like what?"

    JR "Like getting to know them. You know, their personalities and hobbies and likes and dislikes."

    "Chenggoy didn’t look too convinced."

    CE "So what you’re trying to say is that you like the Leonors for their personalities and not their looks."

    JR "I didn’t say that either…"

    CE "Then?"

    JR "They’re both pretty girls, there’s no competition. What makes them different and unique is how they act. "
    JR "Like, uh, Valenzuela is industrious and hardworking. She also has an easy confidence that is hard to emulate. "
    JR "Rivera is docile and sweet and is generally very cute. It’d be like comparing apples and oranges."

    CE "Eh? Then if they’re all different how do you know what to impress them with?"

    JR "Haven’t you been listening? There is no special secret, just don’t act like a horny loser."

    CE "Damn, this is a lot harder than I thought."

    "I rolled my eyes. I caught a glimpse of something shiny in one of the market stalls and stopped in front of it. "
    "It looked to be something of a gift shop, with the front display showcasing different kinds of handmade jewelry and accessories for women like handkerchiefs and fans. "
    "Admittedly, it wasn’t anything too fancy but the pricing was affordable and the quality was decent. "
    "Cecilio picked up one of the colorful fans and jokingly pretended to be a coquettish lady, his voice taking an exaggerated feminine pitch."

    CE "You really are nothing but a dog, Jose! First I hear you’ve been sleeping with my best friend, then my sister, then my aunt, then my own mother! What say you in your defense?"

    "Cecilio fanned himself even harder. The store clerk gave both of us a bemused glare."

    CLK "Is there anything you’d like to buy?"

    JR "Please ignore this idiot. How much for these?"

    "I picked out a few of the items on display. One was {b}a maroon paper fan{/b} painted on the front side with scenery of mountains and cherry blossoms. "
    "It wasn’t a painting style I was familiar with, which lent it a kind of foreign and exotic appeal. "

    "The next item was a white {b}embroidered handkerchief{/b}, its borders were hemmed with delicate lace and lavender swirls."

    "I grabbed one of the {b}brooches{/b} on the rack and held it up to the light. "
    "The stone in the middle was a deep shade of green that reminded me of the verdant forests that lay beyond the walled boundaries of Intramuros. "

    "The last item was a {b}sewing kit{/b} inside of a tiny painted wooden box. "
    "It wasn’t what one would traditionally give to a lady as a courting present, but I could see the appeal in giving something that she could use often in the future. "
    "Plus the design of the box wasn’t bad either, it was minimalist and depicted colorful fishes in the front."

    CLK "Oh, those? They’re 50 pesos each."

    JR "50 pesos?!"

    "No way. That was too much! I felt doubt sink into my mind as fears of being scammed of my meager allowance surfaced."

    JR "I guess that means I have to pick one."

    CLK "How about this, if you take two items I’ll charge you 80 pesos."

    JR "It’s really not that much of a difference."

    CE "So why not take both?"

    JR "I know you think I’m some sort of rich kid but I really am not."

    CE "What’s the harm then? If she doesn’t like one gift you can always give her the other."

    JR "It’s kind of overkill to be honest."

    CE "Fine, suit yourself."

    hide JCecilio at leftJC

    menu:
        "Paper Fan":
            #Choice A: Valenzuela Affection +1
            $ valenzuela_affection += 1
            $ acquiredPaperFan = True
            pass

        "Handkerchief":
            #Choice B: Rivera Affection +1
            $ rivera_affection += 1
            $ acquiredHandkerchief = True
            pass

        "Brooch":
            #Choice C: Valenzuela Affection +2
            $ valenzuela_affection += 2
            $ acquiredBrooch = True
            pass

        "Sewing Kit":
            #Choice D: Rivera Affection +2
            $ rivera_affection += 2
            $ acquiredSewingKit = True
            pass

    label C14_done:

    show JCecilio at leftJC


    CLK "A fine choice. Here you go, sir. Come again next time."

    JR "Thank you, we’ve got what we came here for."

    CE "So what’s next?"

    JR "What else? To give this to the recipient of course."

    stop Market




    label EPISODE2GENERATOR:
        if acquiredPaperFan == True:
            jump EPISODE2GENERATORLV

        elif acquiredBrooch == True:
            jump EPISODE2GENERATORLV

        elif acquiredHandkerchief == True:
            jump EPISODE2GENERATORLR

        elif acquiredSewingKit == True:
            jump EPISODE2GENERATORLR

        else:
            pass









    #+++++++++   LEONOR VALENZUELA ROUTE: EPISODE 2   +++++++++++++++++++++++++++++++++++++++++++ Pages 75-84  of the Script +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    label EPISODE2GENERATORLV:
    #PUBLIC MARKET BG?????????
    #PUBLIC MARKET BG?????????
    #PUBLIC MARKET BG?????????
    #PUBLIC MARKET BG?????????


    # For hiding unnessary characters
    hide JCecilio
    # For hiding unnessary characters

    scene bgSTR
    stop music
    play music "audio/Music/Easy Lemon.mp3" loop
    with fade
    with None

    play Market "audio/Voice/Market.mp3"
    "As I looked at the prize I had in my hands, I felt a tap on my shoulder from Cecilio, who pointed right behind him. I turned, not at all expecting what I ended up seeing."

    "In a street food stall adjacent to us was none other than Javier Lizares, scion of the Lizares name and wealth, ordering a shanghai lumpia in a public market. "
    "I couldn’t believe my eyes."

    show JCecilio at leftJC
    with easeinleft
    with None
    CE "Hey, isn’t that the guy from the house where you stole those flowers?"

    JR "Not so loud!" with hpunch

    "Thankfully, the devil in question was too occupied to have heard us. The sight was so absurd that it looked comedic. "
    "Javier stood out like a sore thumb, his off white school uniform suit pressed and spotless. It stood at odds with his dirty and muddy surroundings."

    "And what exactly did someone like him have any business to do there? Javier bought an exorbitant number of lumpias that the food stall cook hastily shoved into a paper bag. "
    "The boy examined the fried treat as he took a tentative bite. The crispy wrapping gave a loud ‘crack’ and his expression changed from mild skepticism to pleasant delight."

    "Javier looked up at the stall worker."

    show Javier at rightJA
    with easeinright
    with None
    JL "How do you make something like this?"

    "And now he’s taking recipe lessons? This day was getting too weird."

    JR "Come on, Chenggoy. Let’s get out of here before he realizes we’re gawking at him."

    CE "Don’t have to tell me twice."

    "We both left."

    stop Market

    #PLACE ====== EXT. BOARDING HOUSE - NOON

    scene bgBHD
    with fade
    with None

    # For hiding unnessary characters
    hide JCecilio
    hide Javier
    # For hiding unnessary characters

    "It had been two days since. I had taken my gift to be wrapped up nicely in a small box and tied with a red and white ribbon. Now was the time to give it to Leonor."

    scene bgVHD
    with fade
    with None

    "I walked down the familiar pathway to the Valenzuela household where I once dormed at. I took the scenic route through the clearing of trees at the back of the house. "
    "I didn’t yet want to make my presence known to her parents, as it would make it difficult for us to find some time alone afterwards."

    "As I neared the back gate, I heard voices from the gardens. My hand froze on the handle. "
    "The first was the familiar lilting voice of Leonor Valenzuela while the other was…"

    stop music
    play music "audio/Music/Tango de Manzana.mp3" loop
    "Javier!?" with hpunch

    "Confusion and indignation filled me. "
    "Why is this guy appearing everywhere these days? And around Leonor no less? I had to stamp down the impulse to just rush in there and demand to know what Javier’s business was. "
    "As it was, I stood there motionless in bewilderment."

    "I took a peek inside and every thought about the propriety of eavesdropping was thrown out the window when I saw Javier and Leonor sitting on a stone bench together. "
    "Granted, they were still a respectable distance apart but somehow I doubted Javier was here just for a nice chat."

    "Speaking of which, that was the exact moment I also noticed a huge lacquer wooden box by the boy’s feet. "
    "Javier said something to Leonor before picking it up on his lap and handing it to her. Inside were even smaller boxes filled with… lumpia. "
    "Just so much lumpia that it would’ve probably been enough to supply an entire town fiesta. "

    "Leonor stared at the pile of boxes in front of her, before bursting into laughter. "
    "The sound of it rang like the twinkling of small bells, loud and clear but somehow also elegant. Javier’s face burst crimson."

    show LValenzuela at leftLV
    with easeinleft
    with None
    LV "So I tell you once that lumpia is my favorite and you decided to buy this many just for me?"

    show Javier at rightJA
    with easeinright
    with None
    JL "Ah… Well… I didn’t buy these."

    "Javier stammered like a schoolgirl."

    JL "I actually made these."

    "{i}Really?!{/i}"

    LV "Really? My, that’s a surprise. You didn’t have to put all this effort just for me."

    JL "Well it’s not a big deal."

    "Leonor looked like a cat who had caught its meal. She put a finger under her lip in mock contemplation."

    LV "‘Not a big deal’ huh? Prior to our conversation before, you had not heard of lumpia. And this many, it must’ve taken you hours right? "
    LV "Have you always known how to cook, or did you learn it just so you could impress me?"

    "She smiled, but it was the kind that made Javier burn up with embarrassment."

    LV "That’s very cute, I didn’t know you held such strong feelings for me. It’s enough to touch my heart."

    JL "It’s not…"

    "She interrupted him when she cupped a hand to his face. His words died in his throat before he could say it. Javier’s mouth opened and closed like a fish."

    LV "Your face looks very red, have you become shy all of a sudden?"

    "Javier stood up so abruptly that he almost dropped all the boxes of lumpia he was carrying. "
    "He scrambled with the watch in his pocket, making a gesture as if he was looking at the time when in reality he was looking at Leonor and her assured smile."

    JL "Ah, would you look at the time! I’m very sorry but I didn’t anticipate that I’d have prior engagements to this. I bid you well, Lady Valenzuela."

    "Leonor giggled, flicking her wrist to open her paper fan."

    LV "Goodbye, Javier."

    hide Javier at rightJA
    with easeoutright
    with None
    "Javier escaped before she could say another word. I had never seen the man act so cowardly–and in front of a woman no less. I had to stifle my own chuckle as I revealed myself to Leonor."

    LV "So it was you the whole time."

    JR "You knew?"

    LV "No, but thank you for confirming it for me."

    "{i}Damn it. Fell right into that one.{/i}"

    JR "So… Javier Lizares."

    LV "Good afternoon to you too, Jose. What about him?"

    JR "Is he courting you?"

    LV "If you call that sad attempt “courting” then sure."

    "OUCH."

    JR "Not to tell you what to do or anything, but you should really pick better company."

    "Leonor rested her chin in her free palm."

    LV "Hmm… Much like you, right?"

    JR "Pardon?"

    LV "If I recall, you also have a habit of keeping ‘good company’ yourself right? It’s okay though, I’m not the type to get jealous."

    "I sighed as I took the seat right next to her."

    JR "My lady, when you accuse me of such things it wounds my heart."

    LV "Please. It’s not like we’re engaged to each other so there’s no need to be so sentimental. "
    LV "You and I both know that courting is just a bit of fun, just a song and dance we all agree to play before we tie ourselves down to one another for eternity."

    JR "Not exactly something I am used to hearing from a woman."

    LV "Oh and why’s that? Should I silently pine and long for you while staring off into the distance when we are not around each other?"

    JR "Alright, I get it."

    stop music
    play music "audio/Music/Danse Morialta.mp3" loop
    "I felt something poke my cheek. It was the lumpia Javier made."

    LV "Come now, Pepe. Don’t be upset. Here, have some of this. It’s good."

    JR "I’m not upset–mph!"

    show cgFP
    with fade
    with None

    play Crunch "audio/Voice/Crunch.mp3"
    "The moment my mouth opened, Leonor took the opportunity to shove the fried treat into my mouth. "
    "My initial irritation melted away when the flavors of the meat and vegetables touched my tongue. "
    "Despite myself, I had to admit that Leonor was right– it was good. Damn it, who would’ve thought Javier would be a good cook of all things? Leonor’s grin was contagious."
    hide cgFP
    with fade
    with None

    LV "See?"

    JR "Are you sure it’s okay to feed me with a gift another man gave you?"

    LV "I don’t see why not. It’s not like he said I couldn’t share."

    "Oh! Speaking of gifts, I had almost forgotten about hers."

    JR "I got this for you."


    hide LValenzuela at leftLV


    label gift_givingLV_continue:
        if acquiredPaperFan == True:
            jump C15_yes

        elif acquiredBrooch == True:
            jump C15_no

    label C15_done:

    label gift_givingLV_no:

    show LValenzuela at leftLV



    LV "Now that you’ve had your share, why don’t you try to feed me next?"

    JR "Ehh?"

    "I held the lumpia awkwardly in my hand as I saw Leonor close her eyes and open her mouth slightly. Her pink lips parted and I couldn’t help but notice how they glistened. "
    "I swallowed hard, the two of us leaning nearer to each other."

    JR "Okay, here it comes."

    play Crunch "audio/Voice/Crunch.mp3"
    "My trembling hand brought the treat to her lips, where she took a big bite of the whole thing. "
    "I had to quickly remove my fingers or otherwise risk losing them to her teeth. She giggled."

    LV "Not bad! I’ll give it a 4/10."

    JR "Aw, come on. I think I did pretty good there."

    LV "You did, up until you froze up like a scared rabbit. Reminds me of poor Javier."

    JR "What do you even like about Javier, anyway? He’s… well–"

    "I ran out of nice ways to say exactly what I thought of the boy."

    JR "He’s an asshole."

    LV "True. But I think he more than makes up for it by providing me with an endless source of entertainment. "
    LV "He’s so easy to tease, everytime I look at his face on the verge of tears I feel like I want to torment him more. "
    LV "I thought he would stop coming after a while but he always returns. Adorable, isn’t it?"

    JR "…"

    "I felt like I just heard something I wasn’t supposed to. Women… women were scary, I concluded."

    LV "Do you want some kalamansi juice to go with this?"

    JR "…Yeah, sure why not."

    #STOP SOME UNNECESSARY SFX######
    stop Crunch
    #STOP SOME UNNECESSARY SFX######

    jump Interlude3
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++[END EPISODE 2]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    #+++++++++   LEONOR RIVERA ROUTE: EPISODE 2   +++++++++++++++++++++++++++++++++++++++++++ Pages 84-90  of the Script +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    label EPISODE2GENERATORLR:

    #PLACE ====== INT. CASA TOMASINA - NIGHT

    scene bgBRN
    with fade
    with None

    # For hiding unnessary characters
    hide LValenzuela
    # For hiding unnessary characters

    "I threw my shoes and bag in the corner of the room, too tired to pick them up and put them in their proper place. "
    "By the time I and Cecilio parted ways, the sun had already reached the horizon. On the walk towards home, I looked up at the sky to find stars peeking out from the clouds. "
    "I didn’t expect how fun it would be to hang out with Cecilio, considering the terrible first impression we had of each other. "
    "But somehow once we got talking, time would fly by until it was already late at night."

    "The gift I had gotten for Leonor was tucked safely in the pocket of my overcoat, and I took it out to gently place it atop my desk so that I didn’t forget later."

    "I had the oddest feeling of being watched. Even as I walked up the stairs to my room that burning sensation in the back of my head remained. "
    "It was only when I closed the door did it finally cease."

    "I thought maybe it was Leonor up to her usual antics, but I was always able to catch her in the act of following me, just little things that gave her position away. "
    "This time felt different from that– and it was enough to put me on edge."

    play KnockDoor "audio/Voice/KnockDoor.mp3"
    "A light knock rapped on my door. I stumbled out of bed to answer." #light Knock sound effect

    show LRivera at leftLR
    with easeinleft
    with None
    LR "Hello…"

    JR "Leonor? What are you doing up this late?"

    play DoorOpen "audio/Voice/DoorOpen.mp3"
    pause (1)
    play DoorClose "audio/Voice/DoorClose.mp3"
    "I stepped outside and closed the door behind me."

    stop music
    play music "audio/Music/Almost New.mp3" loop
    LR "I heard you come up."

    JR "Ahh… sorry if I disturbed you."

    LR "Oh you didn’t wake me, don’t worry. I was waiting for you to return. You seem… tired than usual."

    JR "Yeah I was out with Cecilio… wait just a second."

    "I went back to retrieve the box."


    hide LRivera at leftLR

    label gift_givingLR_continue:
        if acquiredHandkerchief == True:
            jump C16_yes

        elif acquiredSewingKit == True:
            jump C16_no

    label C16_done:

    show LRivera at leftLR

    label gift_givingLR_no:


    JR "You ready for your next lesson?"

    LR "Truly? I’d love to!"

    JR "But it’d be better for me if you tell me what you’re interested in first."

    LR "Hmm… well I did have a couple of questions for you."

    JR "Shoot."

    LR "Let’s say a man is wounded – like from a stab wound – and he is bleeding. How long does he have left to live?"

    JR "Hmm… well that would depend on a number of factors like the size of the wound, the placement of the wound, if it hit an artery–"

    LR "So how long would it take for him to die?"

    JR "If the wound doesn’t stop bleeding it can take as long as five minutes. Shorter if their wounds are severe. The average human adult has around five liters of blood. "
    JR "If you lose 40 percent of that, you will die. That’s about… 2.4 liters I’d say."

    LR "I see… that’s awful. And which parts of his body would be more susceptible to that?"

    "I was glad I got to flex a little of what I studied to the girl I liked."

    JR "The jugular on the side of the neck or even the Adam’s apple would be the most dangerous I’d say. The others I can think of are also the wrists and the inside of your forearm."

    LR "Oh god! That sounds really gruesome!"

    JR "Yeah it is, just be thankful you’ll probably never have to see it for yourself."

    LR "I really hope so too."

    JR "Hey, I’ve been wondering…"

    LR "Yes?"

    JR "You said you wanted to become a healer, but you never told me why. "

    stop music
    play music "audio/Music/The Complex.mp3" loop
    LR "…"

    "The smile on Leonor’s face disappeared in an instant and was replaced by an eerie blankness. Her tone was devoid of emotion."

    LR "You know, I’m not really sure why either."

    JR "Huh?"

    LR "Do you know what it’s like to always be watched? To have the gaze of others constantly trained on every single move you make? "
    LR "Have you ever felt the weight of a hundred eyes crawling over your skin, Pepe, have you?"

    JR "Uhh… I’m not sure, I guess I have."

    LR "No you haven’t. You don’t know anything. You’re just like everyone else, Pepe. Always thinking so well of me, like I am a good girl but I’m not. "
    LR "I’m a fraud. I’m not nice at all– it’s all just pretend."

    JR "I think you should calm down a little–"

    LR "Mother always decides everything for me and I’m sick of it I’m sick of it I’m sick of it I’m sick of it I’m sick of it I’m sick of it I’m sick of it I’m sick of it I’m–" with hpunch

    JR "LEONOR!" with hpunch

    "She stopped, her anguished expression calming just a bit."

    LR "I have one last question."

    "I swallowed the unsettled lump in my throat, worried for what other outburst would come out of her."

    JR "Are you sure you’re okay?"

    LR "The Lord once said that if your hands cause you to sin, then you must cut it off. And if your eyes cause you to sin, you must pluck them out. "
    LR "So tell me, if you had to choose: Which one would you rather give up on? Your hands or your eyes?"

    "I couldn’t comprehend the words she was saying anymore. What kind of insanity has gripped poor sweet Leonor? Sweat dripped down my temple and I couldn’t formulate a reply."

    LR "Answer me, Jose. Your eyes or your hands?"

    JR "I– uhh… I’d need both to perform my work. I think I would give up one eye and one hand so that at least I could still see and hold a scalpel."

    LR "Hehe. You’re so smart, Pepe! You always know the right things to say."

    "She laughed, and I found myself laughing nervously as well. After a brief moment she composed herself and looked as if nothing had happened at all."

    LR "Thank you for tonight. I’m sorry for my outburst, I shouldn’t have been so mean to you. After all, I like you a lot!! So I’ll just leave now so you can rest, okay?"

    "I nodded shakily. Leonor left not long after that. I scrambled up from my bed and looked out the window. "
    "Right across from where I was, I could see another window adjacent to mine that had a clear view of the gate leading up to the front door. "
    "The same room also led to the staircase that oversaw the reception room and the stairs which came up to my room."

    "That was Leonor’s window."

    #STOP SOME UNNECESSARY SFX######
    stop KnockDoor
    stop DoorOpen
    #STOP SOME UNNECESSARY SFX######

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++[END EPISODE 2]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    #+++++++++   LEONOR RIVERA ROUTE: (INTERLUDE 2)   +++++++++++++++++++++++++++++++++++++++++++ Pages 90-91  of the Script +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    label Interlude3:

    #PLACE ====== INT. ??? - NIGHT???

    scene cgINT3-1
    stop music
    play music "audio/Music/SCP-x3x I am not OK.mp3" loop
    with fade
    with None

    # For hiding unnessary characters
    hide LRivera
    # For hiding unnessary characters

    "That night, I dreamed."

    "My red rimmed eyes stared at the open flame of the candle, watching it flicker and dance erratically through the night. "
    "I did not feel its warmth on my cheek, but my whole body froze in that shivering darkness. All around me were repurposed jewelry making tools and beakers holding unknown liquid."

    "I imagined the faces of Paulita Gomez and Juanito Palaez, at the joy and laughter of their friends and family as they celebrated their wedding reception in the late Capitan Tiago’s house. "
    "Everybody who was anybody was sure to be invited– important political figures and even the clergy."

    "I imagined giving this kerosene lamp as a wedding present. ‘What a thoughtful gift’ the guests would say. "
    "They’d admire the glittering jewels that dangled from its body, and be overcome with envy at its sheer magnificence."

    "I imagined the expressions they’d make when they’d turn on the knob and be engulfed in flames, "
    "The mechanism inside sparking a tinder that activates the kerosene– creating an explosion that would consume the entire living room and everyone therein. "

    "I imagined the screams of every corrupt priest as they burned in a hell of their creation."

    "I smiled."

    scene cgINT3-2
    with fade
    with None
    "What will you do?"


    menu:
        "Kill them all":
            pass

        "Kill them all":
            pass

        "Kill them all":
            pass

        "Kill them all":
            pass

    label C17_done:

    stop music

    #PLACE ====== PLAZA SAMPALUCAN - NIGHT

    ## PLAZA NIGHTTTTTTTTTT????????????
    ## PLAZA NIGHTTTTTTTTTT????????????
    ## PLAZA NIGHTTTTTTTTTT????????????
    ## PLAZA NIGHTTTTTTTTTT????????????

    scene bgPSN
    play PartyPips "audio/Voice/PartyPips.mp3" volume 0.3
    with fade
    with None

    "Tonight was the night of the long-awaited fiesta dance, where everybody could come and unwind in the name of some random long-dead saint. "
    "Tonight would define the course of my life, if I was to finally find a girlfriend or to remain forever alone. Everybody in Santo Tomas has been tearing their hair out over who to invite as a date. "
    "Not I though, I already had it all figured out."

    "From the looks of things, Marco Soriano was to be the latter. I stifled a snicker as I saw the poor guy get rejected for the nth time that night. "
    "Paul gave him a sad pat on the back as they rejoined the group of lonely men in the corner, gazing longingly at the pretty girls on the dance floor."

    "The fiesta was a special thing, it brought a sense of community to the town where everyone would share food and talk and dance and drink the night away. "
    "Though, despite the merrymaking, one could not ignore the signs of disparity and social hierarchy from the placement of every group. "
    "High class people stayed in their own circles and the poor stayed in theirs. Same story, different day."

    "I sighed, cynicism dulling my mood in a way that even the bright lights and loud music couldn’t remedy. It was time I found my date."

    "WHO WILL YOU GO TO?"


    menu:
        "Leonor Valenzuela":
            $ valenzuela_pick = True
            pass

        "Leonor Rivera":
            $ rivera_pick = True
            pass

    label C18_done:




    #Episode 3 Choice thru points
    label episode3_path:
        if valenzuela_affection > rivera_affection:
            jump valenzuela_epi3
        elif rivera_affection > valenzuela_affection:
            jump rivera_epi3


    #+++++++++   LEONOR VALENZUELA ROUTE: EPISODE 3   +++++++++++++++++++++++++++++++++++++++++++ Pages 92-102  of the Script +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    label valenzuela_epi3:
    $ valenzuela_epi3 = True

    #PLACE ====== EXT. PLAZA SAMPALUCAN - NIGHT

    ## PLAZA NIGHTTTTTTTTTT????????????
    ## PLAZA NIGHTTTTTTTTTT????????????
    ## PLAZA NIGHTTTTTTTTTT????????????
    ## PLAZA NIGHTTTTTTTTTT????????????

    scene bgPSN
    with fade
    with None

    "I looked out into the crowd of partygoers when I spotted the Valenzuelas making conversation with the Lizares family. Orang was there, lovely as ever, in a maroon dress and matching fan. "
    "She had a bored expression on her face until her eyes met mine. Javier was thankfully absent from the occasion. "

    "I waited until the two families had parted ways before I approached them."

    JR "Good evening, Capitan Juan and Sanday Valenzuela. I hope you and your family are having a good time at the fiesta."

    show CaptVa at leftCV
    with easeinleft
    with None
    CJ "All is well, Pepe! I hear you’re making a name for yourself in the university. My daughter has been asking about you ever since you left."

    show LValenzuela at rightLV
    with easeinright
    with None
    LV "Father…"

    CSAN "Oh won’t you spend some time with us this evening? It’s been a while since we’ve talked like this."

    JR "I’d love to but maybe some other time."

    CSAN "Oh is that so! Well then don’t let us stop you. "

    hide CaptVa at leftCV
    with easeoutleft
    with None
    "The couple were then approached by another figure, an affluent Spaniard by the looks of it. Leonor rolled her eyes and I gave her a meaningful wink. "

    hide LValenzuela at rightLV
    with easeoutright
    with None
    "I stealthily left their side and waited in a quiet spot away from their earshot. A few moments later, Leonor arrived."

    "I raised my elbow and Leonor gracefully took it."

    show LValenzuela at rightLV
    with easeinright
    with None
    LV "You came right on time. I was starting to get sick of all this noise. I’d have been stuck with A chaperone for the rest of the night."

    JR "Then let’s go somewhere quieter."

    stop PartyPips
    #PLACE ====== EXT. STREET - NIGHT

    scene bgEK
    with fade
    with None

    # For hiding unnessary characters
    hide LValenzuela
    # For hiding unnessary characters

    play WalkCobble "audio/Voice/WalkCobble.mp3"
    "The two of us walked arm and arm in relative silence as the noise of the fiesta grew muffled from distance. "
    "I remembered this part of Intramuros as being the street where I used to make my rounds to Manong gardener."

    "I wondered how that man was doing now."

    show LValenzuela at rightLV
    with easeinright
    with None
    LV "Jose, do you smell something?"

    JR "Huh? What is it?"

    LV "It’s coming from over there."

    "Leonor pointed in the direction of the Lizares manor. Now that I paid attention to it, I could pick up a whiff of the faint smell of kindling and… oil."
    stop WalkCobble
    #LIZARES MANOR FIREEEEEE?????????
    #LIZARES MANOR FIREEEEEE?????????
    #LIZARES MANOR FIREEEEEE?????????
    #LIZARES MANOR FIREEEEEE?????????
    #LIZARES MANOR FIREEEEEE?????????

    scene bgLMF
    show LValenzuela at rightLV
    with fade
    with None

    #sound effect fire crackling

    play Fire "audio/Voice/Fire.mp3"
    "The both of us rushed over to the scene and the smell became more pungent as well. When we made the turn, I saw the once magnificent gardens of the Lizares manor was in flames. "
    "What once housed the priceless collection of imported and local flora was devoured into ashes."

    "A lone figure stood above the inferno, their silhouette standing starkly against the harsh light."

    JR "Javier…?"

    show cgJA
    with fade
    with None
    "The boy stood still, turning his head only slightly to look upon me. Dark circles covered his red rimmed eyes, a look of confused mania in his expression and the tilt of his smile."
    hide cgJA
    with fade
    with None

    show Javier at leftJA
    with easeinleft
    with None
    JL "Ah, it’s you. Have you come to witness the fall of this decadent house?"

    LV "Javier, what’s gotten into you? Did you do this?"

    JL "It’s kind of funny really, all this time I thought I was someone special. That I was destined for greater things than being stuck in this washed up country."

    JL "But you want to know the truth? I’m just a fucking nobody. Just like you. Just like everybody else."

    LV "I don’t… understand."

    JL "I’m a bastard. My father slept with some Filipino maid and got me! HAhaha. HAHAHAHAHA!"

    JL "It all makes sense now, can’t you see? Why everybody’s been avoiding me all of a sudden, treating me like some kind of invalid. "
    JL "It’s because they knew! They were just waiting for me to find out, like some kind of half baked joke. "
    JL "A laughing stock! And it’s so funny because I get it now. I get it, I GET IT!"

    JL "Don’t you find it funny too, Orang?"

    LV "Javier… I’m sorry."

    JL "You were always too kind to me. Even when I didn’t deserve it. Even when I never really had a future to begin with. My family is done. "
    JL "We’re all broke thanks to my mother’s excessive spending for this stupid garden. So this, all of this."

    "He gestured out into the burning fields."

    JL "This is all just payback. I’m sick of having to sink or swim for this family. Sick of my bitch mother treating me like shit– she probably knew the truth and that’s why. "
    JL "So I’m going to take away the one thing she treasured most and see how she likes it. Hope she just keels over in embarrassment when everybody finds out that her husband is an adulterous whore."

    JR "Javier, I know we haven’t gotten along in the past, but you’ve got to stop this. You’re going mad!"

    JL "I KNOW RIGHT!? I’VE NEVER FELT BETTER IN MY LIFE!"

    "Javier suddenly stopped when he felt himself being embraced by a familiar warmth."

    LV "Javier… Please stop."

    JL "Leonor…"

    play WalkCobble "audio/Voice/WalkCobble.mp3"
    "Jose heard the sounds of boots hitting cobblestone."

    JR "This is all very touching and all but can we speed things up before the {i}Guardia{/i} arrive!? In case you forgot, we’re right in front of a walking arson case!"

    JL "Oh."

    JR "\“Oh\” is right! "


    stop music
    play music "audio/Music/Clash Defiant.mp3" loop
    stop WalkCobble
    GD1 "Hey, you there! What’s going on here?"

    LV "Run!"

    stop Fire



    scene bgEK
    with fade
    with None

    # For hiding unnessary characters
    hide LValenzuela
    hide Javier
    # For hiding unnessary characters

    play DropBod "audio/Voice/DropBod.mp3"
    "I made a beeline for the other side of the street, but before I could get away I tumbled forward to land face first on the cobblestone. "

    play Punchy "audio/Voice/Punchy.mp3"
    "I felt myself being picked up by the collar of my shirt before a powerful punch smacked me right in the face." with hpunch

    GD1 "Filthy Indios having to ruin a perfectly good drinking night. You’re the one who did this, didn’t you!"

    JR "Bwuah? Why me! I had nothing to do with this!"

    show Javier at leftJA
    with easeinleft
    with None
    JL "He’s right! It was me… I was the one who set fire to the gardens. So please, let him go."

    GD1 "Is that so, huh?"

    play DropBod "audio/Voice/DropBod.mp3"
    "The guard dropped me unceremoniously on the ground. I rubbed my aching cheek and stumbled back."

    play Punchy "audio/Voice/Punchy.mp3"
    "Next thing I knew, I saw Javier eating dirt too when the guard rammed his fist into Javier’s torso. Spittle flew out of the boy’s mouth as he fell to his knees."

    GD1 "Then how about this? I’ll arrest you both for fucking up my night. Serves you bastards right."

    JL "Hngg..! You brute!"

    Q "Hey, why don’t you try looking elsewhere for a fight, buddy?"

    "The entire group was caught off guard by the sound of another voice. "

    play Punchy "audio/Voice/Punchy.mp3"
    "It was enough to have the guard pause long enough for a brick to hit him in the face. The man fell to the ground with an exaggerated ‘thud’!" with hpunch

    show JCecilio at semileftJC
    with easeinleft
    with None
    CE "What are you guys waiting for, an instruction manual? Let’s fucking go!"

    show LValenzuela at rightLV
    with easeinright
    with None
    LV "And it looks like we’ve got company!"

    GD2 "You there, stop!"

    play Run "audio/Voice/Run.mp3"
    "The group ran towards the darkness of the alleyways. Groups of armed guards passed where they last stood, a couple of them examining the downed guard from earlier. "
    "Cecilio ‘tsked’ in annoyance."

    CE "What I say, eh? Told you that you’d be glad to have me as your friend."

    JR "Can’t say I disagree with you there. You sure are a sight for sore eyes."

    CE "And look who we have here, Javier Lizares in the flesh. Last I saw you, you didn’t have as many loose screws on."

    JL "Who are you? Nevermind that, I had the situation under control had that guard not acted so impudently. I never would’ve thought they would engage in such brutish behavior."

    CE "Guardia being brutes? {i}Welcome to the real world, asshole!{/i} "
    CE "Without your money protecting you it becomes really clear now who these pigs are serving, huh? "
    CE "Last time I had a run in with them, they gave me a black eye for a crime I didn’t even commit– courtesy of this dipshit over here."

    JR "Hey!"

    CE "So I’ve been waiting to get one of my own back, heh. Feels good."

    LV "Can we cut the chit chat? They’re still looking for us."

    JR "Right. Cecilio, can you take Leonor safely home?"

    CE "Aye aye, {i}Capitan!{/i}"

    LV "And what about you? What if you get caught?"

    JR "I’ll figure a way out. It’s safer that we’re not together if they do."

    "Leonor pursed her lips in obvious disagreement. But for whatever reason, she decided not to push the subject."

    LV "Fine. But you stay safe. You too, Javier."

    JR "Goodbye, Leonor. May we meet again."

    hide LValenzuela at rightLV
    hide JCecilio at semileftJC
    with easeoutright
    with None
    "She took my hand in hers quickly before leaving with Cecilio. Javier stood there watching in silence."

    JL "Do you love her?"

    JR "Well that came out of nowhere. Do you really think now’s the right time to talk about this?"

    JL "I have to know if you love her. Otherwise I can’t let myself back down."

    hide Javier at leftJA

    menu:
        "Say you love her":
            #CHOICE A: Valenzuela +2 Affection points
            $ valenzuela_affection += 2
            jump C19_yes

        "You’re unsure":
            #CHOICE B: Valenzuela -2 Affection points
            $ valenzuela_affection -= 2
            jump C19_no

    label C19_done:

    show Javier at leftJA


    JR "I see."

    JL "Maybe if things were different. Maybe if I was a different person…"

    JR "No point wishing for the impossible."

    JL "Wow you’re really not good at this comforting thing."

    JR "Who says I’m trying to comfort you? I’m saying it like it is. If you want to be a coward and not pursue the girl of your dreams because of your insecurities or whatever then that’s on you. "
    JR "Just don’t be mad if some other man sweeps her off her feet before you come to your senses."

    JL "Grr.. why you..!"

    "I laughed and felt the tension of that night melt away a little."

    JR "If you don’t somehow end up in a cell before this night is over, you should go to her. Tell her how you really feel. "
    JR "If she says yes then I’ll gladly back off and let you two do your thing. But if she says no then I’ll give it my best shot. Deal?"

    JL "But I thought you hated me."

    JR "Oh I do. But I feel sorry for you too."

    JL "Tch. Fine, it’s a deal."

    "We both shook hands."

    JR "Now let’s get out of here."

    stop music

    #STOP SOME UNNECESSARY SFX######
    stop DropBod
    stop Punchy
    stop Run
    #STOP SOME UNNECESSARY SFX######

    jump valenzuela_epi3_skip
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++[END EPISODE 3]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    #+++++++++   LEONOR RIVERA ROUTE: EPISODE 3   +++++++++++++++++++++++++++++++++++++++++++ Pages 102-109  of the Script +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    label rivera_epi3:
    $ rivera_epi3 = True

    #PLACE ====== EXT. PLAZA SAMPALUCAN - NIGHT

    ## PLAZA NIGHTTTTTTTTTT????????????
    ## PLAZA NIGHTTTTTTTTTT????????????
    ## PLAZA NIGHTTTTTTTTTT????????????
    ## PLAZA NIGHTTTTTTTTTT????????????

    # For hiding unnessary characters
    hide Javier
    # For hiding unnessary characters

    "I hesitated, unable to forget our last conversation. Something about Leonor felt… off. "
    "I didn’t think much of it at first how she asked all of a sudden about blood loss and stabbings but now I couldn’t help but think back on it again. "
    "What made her ask such specific questions? And what was that whole thing about cutting off hands about!?"

    "I decided to check on her to be sure."

    "I waded through the crowded streets, passing by drunkards and musicians playing on their guitars. "
    "A few blocks in the direction of Casa Tomasina I found Leonor’s mother, Tiya Silvestra, looking around her wildly."

    show TSilvestre at leftTSI
    with easeinleft
    with None
    TSI "Pepe! There you are, have you seen Leonor?"

    JR "No, I haven’t. Why, what’s the matter?"

    stop music
    play music "audio/Music/The Complex.mp3" loop
    TSI "She’s gone missing!"

    "Missing…?"

    JR "What?"

    TSI "I went upstairs to tell her to get ready for the fiesta but she didn’t answer. And when I opened the door, she was missing! Oh, Jose, you have to help us!"

    JR "What about the {i}Guardia Civil?{/i}"

    TSI "Your Tiyo Antonio is contacting them now. But if there’s anything you know about where she may be, it would really help."

    "I honestly had no idea. Intramuros wasn’t a small place and she could be anywhere. Maybe she might’ve even gotten in trouble– murdered, kidnapped even!"

    "I scrambled through my past interactions with her. Think Jose, think! Was there any clue that she left when she talked to me?"

    "{i}‘The Lord once said that if your hands cause you to sin, then you must cut it off. And if your eyes cause you to sin, you must pluck them out.’{/i}"

    "Could it be?"

    JR "I have to go."

    TSI "Pepe, where are you going? {i}PEPE!{/i}"

    stop PartyPips
    #PLACE ====== INT. SAN AGUSTIN CHURCH - NIGHT

    scene bgEK
    with fade
    with None

    # For hiding unnessary characters
    hide TSilvestre
    # For hiding unnessary characters

    play Run "audio/Voice/Run.mp3"
    "My lungs burned as I ran through the streets of Intramuros. "
    "There was no time to call a calesa, the streets were crowded with people anyway and it wouldn’t be fast enough to make it to the church. "
    "I pushed aside festival goers, which elicited a couple of angry insults thrown my way but I didn’t care. I didn’t know what would happen if I had arrived too late."

    "There were a few passerbys when I arrived at the church doors, though most of them would be heading to the center of the festivities in the plaza. "

    #STOP SOME UNNECESSARY SFX######
    stop Run
    #STOP SOME UNNECESSARY SFX######

    scene bgSAI
    play ChurchDOC "audio/Voice/ChurchDOC.mp3"
    with fade
    with None

    "I crept inside, noticing that the interior was mostly empty save for two figures down the aisle."

    "I snuck forward and hid behind one of the confessional booths to have a closer look at the two. It was Leonor… and a young handsome priest."

    show LRivera at rightLR
    with easeinright
    with None
    LR "Father Salvacion"

    show PSalvacion at leftPSAL
    with easeinleft
    with None
    FAS "Yes, my child?"

    LR "There is something that occupies my mind that I can’t quite seem to figure out. I figured you’d be able to help me since you know so much!"

    FAS "Of course, ask me anything."

    LR "You asked me once if I wanted to join the convent here and I told you I’d give it some thought. "
    LR "I said I’d tell you my answer today, but I’m thinking I will only after you clear some things up for me."

    "Father Salvacion's initial eagerness was quelled by the sudden questioning"

    FAS "And that is?"

    "Leonor walked up to the priest, closer than what would’ve normally been deemed acceptable. The innocent smile remained plastered on her face as she reached up on her tip toes and whispered."

    #insert eerie sound effect
    LR "{b}{i}THE LORD ONCE SAID THAT IF YOUR HANDS CAUSE YOU TO SIN, THEN YOU MUST CUT IT OFF. AND IF YOUR EYES CAUSE YOU TO SIN, THEN YOU MUST PLUCK THEM OUT. {/i}{/b}"
    LR "{b}{i}TELL ME, FATHER, IF YOU HAD TO CHOOSE. WHICH WOULD YOU GIVE UP, YOUR EYES OR YOUR HANDS?{/i}{/b}"

    show cgSCR
    with fade
    with None
    "From under her long sleeves, the light caught a shiny glint of a pair of scissors from behind her back."
    hide cgSCR
    with fade
    with None

    JR "LEONOR STOP!"

    "I had jumped just in time to catch her wrist before she could pull her arm back to stab the priest. Thankfully the blade was still hidden in her sleeve, but Leonor struggled wildly." with hpunch

    LR "JOSE LET GO OF ME! Ugh–" with hpunch

    FAS "What is the meaning of this!" with hpunch

    LR "Father, help me this man just assaulted me out of nowhere – AH!" with hpunch

    JR "That’s enough out of you!" with hpunch

    FAS "I don’t really understand what’s going on but don’t worry, I’ll get you some help, Leonor."

    LR "Hehe."

    FAS "Leonor…?"

    LR "“Help me”. That’s what everyone always says. They think they’re helping me but they’re just making everything worse. "
    LR "You make me sick. I hate the way you stare at me like I’m just a piece of meat. Something to lust after and ogle."

    FAS "Don’t say that, it’s not true"

    LR "It’s true. I hope one day your eyes and hands fall off."

    "The concerned look in the priest’s face disappeared and was replaced with a cold and calculating look."

    FAS "It’s clear that you’re not yourself at the moment so I will forgive you this time. Boy, make sure she reaches home safely. "

    JR "Come on, Leonor."

    #STOP SOME UNNECESSARY SFX######
    stop ChurchDOC
    #STOP SOME UNNECESSARY SFX######


    #PLACE ====== EXT. STREET - NIGHT

    scene bgEK
    stop music
    play music "audio/Music/Plaint.mp3" loop
    with fade
    with None

    # For hiding unnessary characters
    hide LRivera
    hide PSalvacion
    # For hiding unnessary characters

    "Leonor was silent throughout the trip. I brought her to an isolated spot in our neighborhood and made her face me."

    JR "Hey. What was that? Were you really planning on killing that man!?"

    show LRivera at leftLR
    with easeinleft
    with None
    LR "Why did you stop me."

    JR "Because it’s madness! What you were about to do– you can’t take that back!"

    LR "So what? At least I’d be free then."

    JR "Free of what?"

    show cgRC
    with fade
    with None
    LR "FREE OF EVERYTHING! Free of this stupid shell I am supposed to inhabit! Of this docile, sweet, weak woman I’m made to become! "
    LR "I hate this, I wish I could just disappear. Why wasn’t I born as a man instead…? Then I could do whatever I want. "
    LR "I wouldn’t have to attend dance and singing lessons, or be made to sit and be quiet while some disgusting worm leers at me!"

    LR "The problem is that I have to live in a world with other people! And because these other people are always looking at me, I become a subject to their gaze. "
    LR "I have to always look at myself from the perspective of someone else. Who even am I anymore? I bet you’re disgusted with me now. "
    LR "Because I’m just a filthy sinner and I nearly killed someone right? I’m not the person you thought I was, right?"
    hide cgRC
    with fade
    with None

    "I grabbed her by the shoulders."

    JR "Leonor, it’s not like that. I am in no way disgusted."

    LR "But why?"

    hide LRivera at leftLR

    menu:
        "Because I have come to love you":
            #CHOICE A: Rivera +2 Affection points
            $ rivera_affection += 2
            jump C20_yes

        "Because that’s what family are for":
            #CHOICE B: Rivera -2 Affection points
            $ rivera_affection -= 2
            jump C20_no

    label C20_done:


    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++[END EPISODE 3]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    label valenzuela_epi3_skip:

    #+++++++++   LEONOR RIVERA ROUTE: (INTERLUDE)   +++++++++++++++++++++++++++++++++++++++++++ Pages 109  of the Script +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    scene bgBlack
    with fade
    with None

    # For hiding unnessary characters
    hide LRivera
    # For hiding unnessary characters

    "I no longer dreamt at night. Ibarra was dead."


    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++[END INTERLUDE]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    label rivera_end_route:
        if rivera_epi3 == True:
            jump rivera_route_end
        elif valenzuela_epi3 == True:
            jump valenzuela_route_end


    #+++++++++   LEONOR VALENZUELA ROUTE: ENDING   +++++++++++++++++++++++++++++++++++++++++++ Pages 109-110  of the Script +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    label valenzuela_route_end:

    #PLACE ====== INT. CASA TOMASINA - DAY

    scene bgCT
    stop music
    play music "audio/Music/Bittersweet.mp3" loop
    with fade
    with None

    "Despite my wishes, the entire arson debacle did not die down the next day. If anything, it got worse. "
    "Lots of accusations were thrown around, from rumors about revolutionaries to claims of the {i}Guardia Civil’s{/i} lax security of the event. "
    "The blaze had left the entirety of the Lizares’s front manor in shambles, though thankfully nobody was around at home during the fiesta."

    "News of possible suspects had been scarce, and I chose to stay at home the following day– hoping that the darkness of that night was able to conceal my features. "
    "The last thing I needed was to get arrested!"

    "Stupid Javier. I hadn’t heard of what happened to him since that night, and my letters sent to Leonor confirmed that she didn’t either."

    show LValenzuela at rightLV
    with easeinright
    with None
    LV "I tried talking to everyone he knew of where he could be but none of them have seen him. Do you think he could have ran to avoid arrest?"

    JR "Had he spoken to you at all before going missing?"

    "She shook her head."

    JR "Then he didn’t run away. I’m sure of it."

    LV "What makes you say that?"

    "{i}Because he hadn’t told you how he felt yet.{/i}"

    JR "I just know it."

    LV "Do you think… that something bad happened to him"

    "Her voice became almost inaudible. I grabbed her hand."

    JR "We’ll find him, that’s a promise. There’s something I still have to settle with that guy."

    LV "Thank you."

    jump end_of_all_endings
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++[END VALENZUELA ENDING]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    #+++++++++   LEONOR RIVERA ROUTE: ENDING   +++++++++++++++++++++++++++++++++++++++++++ Pages 111-112  of the Script +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    label rivera_route_end:

    #PLACE ====== INT. CASA TOMASINA - DAY

    scene bgCT # or this must be bedroom day?
    stop music
    play music "audio/Music/Bittersweet.mp3" loop
    with fade
    with None

    # For hiding unnessary characters
    hide LValenzuela
    # For hiding unnessary characters

    "Despite my wishes, the debacle with Leonor the other day did not subside or merely fade into the background. Father Salvacion contacted Leonor’s parents, exaggerating the role of my involvement. "
    "Tiya Silvestre couldn’t believe her daughter would act in such a way. It was absurd she said, there was no way."

    "So naturally the blame fell on the person who came at the opportune moment that her behavior started to change: me."

    "Tiyo Antonio sent word for Paciano to come and pick me up. It seemed that I was no longer welcome here."

    show LRivera at leftLR
    with easeinleft
    with None
    LR "Jose, I’m so sorry."

    JR "It’s not your fault."

    LR "But it is my fault. If you weren’t there to stop me then I would’ve done something unforgivable. And because you stopped me, now you’re in trouble."

    "I sighed, as much as I didn’t want to say it– she was right. But seeing her on the verge of tears tugged at my heartstrings and I patted her on the head."

    JR "There, there."

    LR "No fair. Shouldn’t I be the one comforting you?"

    "I opened my arms expectantly, and Leonor jumped straight into them. She hugged me tight."

    LR "Please don’t go…"

    JR "Trust me, I don’t want to. But I also don’t want to be the reason you and your parents aren’t on good terms."

    LR "We’ll see each other again right?"

    JR "Of course, I won’t be far anyway."

    LR "Make sure to write me lots of letters, okay? And come visit when you have the time! And-and-"

    JR "Alright haha, I get it."

    play DoorBell "audio/Voice/DoorBell.mp3" volume 0.3
    "The doorbell downstairs rang. That was my cue to leave. I hesitantly let go of Leonor and picked up my suitcase."

    "The girl looked suddenly very small, alone in the space of that room. The sight made me feel lonely, but I still gave her one last smile."

    "I opened that door for the final time."

    #STOP SOME UNNECESSARY SFX######
    stop DoorBell
    #STOP SOME UNNECESSARY SFX######

    jump end_of_all_endings
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++[END RIVERA ENDING]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    label end_of_all_endings:


    #If chosen girl with high points
    label choose_girlpoints:
        if valenzuela_affection > rivera_affection and valenzuela_pick == True:
            jump end_game
        elif rivera_affection > valenzuela_affection and rivera_pick == True:
            jump end_game
        else:
            jump seen_ending

    #This hero ending is just for the player who choose a girl with low points.
    label seen_ending:
        if valenzuela_epi3 == True and rivera_pick == True:
            jump valenzuela_seen_end
        elif rivera_epi3 == True and valenzuela_pick == True:
            jump rivera__seen_end
        else:
            jump end_game


    #+++++++++   HERO ROUTE: ENDING   +++++++++++++++++++++++++++++++++++++++++++ Pages 112-118  of the Script +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



    #IF SEEN VALENZUELA ENDING:
    label valenzuela_seen_end:

    scene bgCT
    show LValenzuela at rightLV
    with fade
    with None


    play KnockDoor "audio/Voice/KnockDoor.mp3"
    "A knock came on the azotea door. When I opened it, I was surprised to find Tiyo Antonio on the other side."

    show TAntonio at leftTAN
    with easeinleft
    with None
    TAN "Pepe, your brother has come to see you."

    JR "What? Why all of a sudden?"

    TAN "I’m not sure but he says it’s urgent."

    "I and Leonor gave each other a bewildered look before I nodded."

    JR "Alright, I’ll be going."

    #STOP SOME UNNECESSARY SFX######
    stop KnockDoor
    #STOP SOME UNNECESSARY SFX######

    jump hero_mode


    #IF SEEN RIVERA ENDING:
    label rivera__seen_end:

    scene bgCT #Bedroom day????
    with fade
    with None

    play DoorOpen "audio/Voice/DoorOpen.mp3"
    "When I opened the door, I saw Tiyo Antonio standing right in front of me. The older man grabbed me by the shoulder."

    show TAntonio at leftTAN
    with easeinleft
    with None
    TAN "Before you leave, your brother is in the other room. He says he wants to talk."

    "I nodded, stunned. "

    #STOP SOME UNNECESSARY SFX######
    stop DoorOpen
    #STOP SOME UNNECESSARY SFX######






    #----------------------------------------------------------------------------------------------------------------------
    label hero_mode:

    scene bgCT #Guest Room????
    with fade
    with None

    # For hiding unnessary characters
    hide LValenzuela
    hide LRivera
    hide TAntonio
    # For hiding unnessary characters

    stop music
    play music "audio/Music/Disquiet.mp3" loop
    "I excused myself from the room and went downstairs to the guest room where my brother presumably was staying. "
    "I breathed in and out. Why was Paciano here? I couldn’t recall receiving a letter in advance of his arrival so this must’ve been a spontaneous visit. "

    "Did he know? He couldn’t have."

    play DoorOpen "audio/Voice/DoorOpen.mp3"
    "Only one way to find out. I opened the door."

    "On the other end of the room, sitting on his bed, was my older brother Paciano. Somehow he looked older than when I last saw him– more haggard looking too. "
    "The grim expression on his face didn’t look promising."

    show Paciano at leftPA
    with easeinleft
    with None
    PA "I found out about your little stunt last night."

    JR "What? But how-"

    PA "How I know is irrelevant. What matters is that I’m not the only one. Did you know there’s a warrant out for your arrest?"

    "My mouth became dry."

    JR "But I– I didn’t do anything wrong."

    "Paciano gave me a look of pity."

    PA "Pepe, haven’t I told you before? The truth is not what matters in this country. Someone of greater power has deemed that you have wronged him, and now you’re going to pay for it."

    JR "Oh god… What should I do?"

    "My older brother put his hands on my shoulders in a comforting way before tucking a ticket in my breast pocket."

    PA "You’re going to listen to what I have to say. I’ve already booked you a ticket to sail to Europe. Your schedule is tonight. Don’t miss it."

    JR "Wait wait, but this is all so sudden! What about my studies here, my friends, what about–"

    PA "Did you not hear a word I just said? If you want to continue living like a free man you’ll leave this country immediately. "
    PA "You won’t become a doctor at this rate."

    JR "If you wanted a doctor in the family so much, why don’t you become one?!" with hpunch

    PA "You know the answer to that!!!" with hpunch

    "I zipped my mouth shut. Of course I knew. Paciano sacrificed so much for me and our family. I intended to match that sacrifice by being a good student. That’s the least I could do. "
    "And I did, I was smart and talented, I exceeded expectations. The medals weighed me down but Paciano didn’t know that. "

    PA "I’ve always known I would be the one to inherit the hacienda. I till the land, plant seeds. It’s noble work, feeds the people, eases their hunger. "
    PA "Our history is rooted in reclaiming our soil, Pepe. I choose to stay…but you. You are far too intelligent to be stuck here in this country. "
    PA "Your talents are better off being used elsewhere. I contacted our Tiyo, he made sure your travel will be smooth. Pack your bags, you’re leaving."

    JR "You just lectured me about how our history is rooted in reclaiming oursoil, how do you expect me to leave right after hearing that?!" with hpunch

    PA "You don’t have much time."

    JR "But Kuya, listen. I intend to stay and serve the country. Our country. Just like you. Isn’t that as noble and patriotic as it could get?"

    PA "Patriotism has no room when our survival is being threatened."

    JR "Kuya please, I can’t just leave Leonor. I love her too much I don’t know where else to put it."

    PA "Put it somewhere the future generations will thank you for."

    "I felt unheard."

    PA "What are you still standing there? Let’s go."

    JR "I refuse to be a pawn in your game of chess, Kuya."

    PA "You…how selfish."

    "I took offense."

    PA "I did not just get out of my way to raise someone who has no resistance to the slightest display of affection. You don’t know where to put that love? Look around you, Jose. "
    PA "Children are starving. "
    PA "Their ribs poking out of their torsos and yet they are forced to build these churches that we worship and celebrate for its disgustingly unapologetic beauty and extravagance. "
    PA "All the while our countrymen are dying of hunger…They deserve just as much love as Lucia."

    JR "Leonor"

    PA "Whatever"

    "I had a feeling my kuya Paciano was annoying me on purpose. We waited for the tension to subside and quietly sat at the edge of the bed. "
    "I thought back to many years ago and the stories I heard about my kuya. Never once had I confronted him about it."

    JR "Have you ever fallen in love?"

    "Paciano looked at me. A sad, lonely look in his eyes. For some reason, I already knew the answer and my heart ached for the only brother I ever knew."

    PA "I have, once…"

    JR "What happened?"

    PA "Our values didn’t align. I wanted to do many great things. She wanted peace and stability. I couldn’t give her that."

    JR "I don’t know how you could love this country so fiercely."

    PA "They can steal away our lands, revise our history, feed us a false narrative where they’re the heroes burdened with saving us from being savage subhumans. "
    PA "But they can never take away our hopes. We won’t let them."

    JR "You’ll get yourself killed."

    PA "Every drop of blood will water the seeds of a growing revolution, Pepe. Remember that."

    JR "I want to help, I really do. But I don’t think I have it in me to become a hero."

    PA "I’m not asking you to become a hero, Pepe. I’m asking you to open your eyes from the bubble you’ve been living in. "
    PA "While you’ve been here dancing and chasing skirts, our country is being ravaged by a social cancer. "
    PA "Tell me, is that the life you want to live? Stop thinking of only yourself."

    "I didn’t really know what to say. Although I felt angry and frustrated, I knew my brother was right. There really was no option left."

    JR "Fine… I’ll go."

    PA "I hope one day you’ll come to forgive me."

    JR "I won’t have to, because I was never really angry at you in the first place. Just myself."

    "That night, I left for Europe."


    #STOP SOME UNNECESSARY SFX######
    stop DoorOpen
    #STOP SOME UNNECESSARY SFX######















    label end_game:
    # This ends the game. ((((((((((((((((((((((())))))))))))))))))))))))))) This ends the game. (((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))  This ends the game.
    # This ends the game. ((((((((((((((((((((((())))))))))))))))))))))))))) This ends the game. (((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))  This ends the game.
    # This ends the game. ((((((((((((((((((((((())))))))))))))))))))))))))) This ends the game. (((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))  This ends the game.
    # This ends the game. ((((((((((((((((((((((())))))))))))))))))))))))))) This ends the game. (((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))  This ends the game.

    return
#CHOICES FOR PART 1 LDR BOI++++++++++++++++++++++++++++++---------------------------------------------------------------================================================
#CHOICES FOR PART 1 LDR BOI++++++++++++++++++++++++++++++---------------------------------------------------------------================================================
#CHOICES FOR PART 1 LDR BOI++++++++++++++++++++++++++++++---------------------------------------------------------------================================================

#Choice1 of Scene 3
    label C1_yes:
        show Lola at leftLol
        show Mariano at rightMar
        show Segunda at semirightS

        JR "Yes, of course. We students are occupied with school."

        hide Lola
        hide Mariano
        hide Segunda



        jump C1_done


    label C1_no:
        show Lola at leftLol
        show Mariano at rightMar
        show Segunda at semirightS

        JR "I don't think that being more actively involved in social issues is necessarily a bad thing, though of course studies must take precedence."

        hide Lola
        hide Mariano
        hide Segunda


        jump C1_done


#Choice2 of Scene 4
    label C2_yes:
        show Manuel at rightMan
        show Mariano at leftMar
        JR "You flatter me with your words, sir. I am merely doing my best."

        hide Mariano
        hide Manuel

        jump C2_done


    label C2_no:
        show Manuel at rightMan
        show Mariano at leftMar

        JR "I am honored you think so, but it's nothing special for me."


        MAN "Oh don't be so humble! You've really made a name for yourself here, and that's not an easy feat to achieve."

        hide Mariano
        hide Manuel

        jump C2_done


#Choice3 of Scene 4
    label C3_yes:
        show Mariano at leftMar
        show Manuel at rightMan
        show Segunda at semileftS

        JR "Oh…how nice."

        hide Mariano
        hide Manuel
        hide Segunda

        jump C3_done


    label C3_no:
        show Mariano at leftMar
        show Manuel at rightMan
        show Segunda at semileftS

        "I said nothing, unable to fully process what I had heard. Manuel's inquisitive stare burned a hole through me."

        hide Mariano
        hide Manuel
        hide Segunda

        jump C3_done


#Choice4 of Scene 5
    label C4_yes:


        show cgJRH
        with fade
        with None
        "{i}\“It’s okay. This is what professional artists do. This doesn’t mean anything…\”{/i}"
        "I leaned closer, bending slightly, resting my palm on top of my knee to meet Segunda eye-level."
        "I raised my free hand and gathered her hair behind her back. A piece of hair spilled and I cursed myself for being sloppy."

        "I do another attempt, this time, gentler. My finger grazed the side of her ear."
        "No negative response. I see this as a sign to continue. The tips of my fingers lightly traced the corner behind her ear. Intimately. Deliberately."
        "Segunda quivered."

        JR "I’m sorry, I shouldn’t have–"

        S "No, it’s alright. It’s just that I was surprised. It’s okay, really. It’s not a big deal."

        "I was embarrassed. Not pressing any further, I just nodded. I returned to my seat, turned the page and started with the rough sketch."


        MAN "..."

        hide cgJRH
        with fade



        jump C4_done


    label C4_no:

        show Segunda at semileftS
        "As much as I wanted to, I couldn't help but feel Manuel's stare boring on my back. I became hyper-aware of being watched by everyone else and I lost my nerve. "
        "I returned to my seat, turning a page, and then started a rough sketch."




    jump C4_done


#Choice5 of Scene 8
    label C5_yes:




        "I froze, swallowing heavily. Every impulse within me screamed to look at her, like a moth to a burning flame. "
        "I closed my eyes, I couldn't do it. What would happen if I lost my restraint here and break the promise I made to myself a week ago?"
        "Doing the right thing was really so difficult."





        jump C5_done


    label C5_no:



        "I knew that raising my head would mean entering forbidden territory. I did it anyway. Honor and integrity be damned. "
        "Segunda was already looking at me. Eyes glassy, mouth slightly parted, blush creeping from her neck."

        "She’s beautiful."

        "And I knew I shouldn’t allow myself to think that. "
        "Heck, I shouldn’t be in the same space as her, much less in a proximity so close I basically betrayed my mother, Manuel and the promise I made to himself a week before."

        "I tried though... I really tried clearing those ideas out of my system but it just kept leaking through the cracks."

        "When did I become so weak?"

        "I couldn't bear looking at her anymore. My mistakes kept piling up and I didn’t know how to face myself in the mirror in the event that I abandon what little restraint I have left. "
        "It felt so much like slowly setting myself up on fire. Nothing good comes out of the ashes."


        jump C5_done



#Choice6 of Scene 9
    label C6_yes:


        "If I was caught eavesdropping here, I was sure that I would get a stern scolding. Those thoughts disappeared instantly when I caught the voice of the unknown man speaking."

        Q "You and I both know that there is only one way this can end."

        show Paciano at leftPA
        with easeinleft
        with None
        PA "You realize you’re asking me to endanger my own family, right?"

        play music "audio/Music/SCP x6x Hopeful.mp3" loop
        Q "Perhaps I was mistaken in your dedication to the cause."

        play TableBang "audio/Voice/TableBang.mp3"
        "A loud bang came from the fist that Paciano slammed against the table." with hpunch

        PA "{i}You don’t know shit about me.{/i}"

        Q "The time of the Spaniards has come to an end. Either you’re with us, or you’ll get out of our way."
        Q "I’ll give you some time to think on it. But I want an answer by next week. Until then."

        play WalkWood6 "audio/Voice/WalkWood6.mp3"
        "Footsteps grew louder as it approached the door I was leaning on, and I scrambled to get away from it. I hurridly hid myself behind a corner and watched as an older man exited Paciano’s room."
        stop WalkWood6

        play WalkWoodStop "audio/Voice/WalkWoodStop.mp3"
        "The stranger paused at the threshold, and I ducked behind cover. I could've sworn that for a second that the man had made eye contact with me."
        "When I peeked out from his spot, the man had already left."
        "{i}What was that? It sounded kind of suspicious…”{/i}"
        stop music






        jump C6_done


    label C6_no:

        #NONE



        jump C6_done

#Choice7 of Scene 10
    label C7_yes:

        show Mariano at leftMar

        JR "Yes..."

        MAR "What a great brother you are."

        "I smiled inwardly. Mariano didn’t realize the double-meaning behind his question. It was these moments of petty rebellion that I lived for."

        hide Mariano





        jump C7_done


    label C7_no:

        show Mariano at leftMar

        JR "Not so much. Still, I promised to come anyway."

        MAR "Hah! You and me both, mate. Still, it's a nice thing for you to do. You're a good brother"

        "I kept my cool, nodding serenely. I just didn't want to give myself away."

        hide Mariano




        jump C7_done






#CHOICES FOR PART 2 LDR BOI++++++++++++++++++++++++++++++---------------------------------------------------------------================================================
#CHOICES FOR PART 2 LDR BOI++++++++++++++++++++++++++++++---------------------------------------------------------------================================================
#CHOICES FOR PART 2 LDR BOI++++++++++++++++++++++++++++++---------------------------------------------------------------================================================
#CHOICES FOR PART 2 LDR BOI++++++++++++++++++++++++++++++---------------------------------------------------------------================================================

#Choice9 of OUTLINE LOVE DOCTOR RIZAL
    label C9_yes:







        jump C9_done


    label C9_no:






        jump C9_done


#Choice10 of OUTLINE LOVE DOCTOR RIZAL
    label C10_yes:


        "I lied as if my cousin slapping me was a reasonable response to me stepping on her cat’s tail. "
        "She raised a brow, not even questioning her daughter’s actions and proceeded to tell me to ask for her apology. I obliged of course, I had a score to settle. "
        "But first, I had to draft a letter. So I went and did just that."




        jump C10_done

    label C10_no:


        "I lied as if it's the most natural thing that one of my Spanish classmates pulled a terrible prank on me. She accepted it with no questions and dismissed me. "
        "I went to my room and sat down on my desk, grabbed a paper and quill to pen a letter to Leonor Valenzuela."




        jump C10_done


#Choice15 of OUTLINE LEONOR VALENZUELA ROUTE: EPISODE 2
    label C15_yes:

        show LValenzuela at leftLV
        LV "Oh, Jose…I don’t know what to say. You didn’t have to go so far as to Purchase me a gift."

        JR "It’s no problem. Do you…?"

        LV "Like it? I love it!"

        JR "I’m glad to hear that."

        hide LValenzuela at leftLV


        jump C15_done


    label C15_no:

        show LValenzuela at leftLV

        LV "…!"

        "She cradled the brooch in her hands, bringing it up to the light of the sun to admire the way it shimmered in differing shades of blue and green."

        JR "Do you like it?"

        LV "I love it. It reminds me a lot of the province where my parents were from. I never got to see the outside of Intramuros, but someday I would like to."

        JR "I’m sure that someday you will."

        hide LValenzuela at leftLV



        jump C15_done


#Choice16 of OUTLINE LEONOR RIVERA ROUTE: EPISODE 2
    label C16_yes:

        show LRivera at leftLR
        LR "Aww, Jose! You really shouldn’t have!"

        JR "It’s no problem at all, I just wanted to see you smile."

        LR "That’s very sweet of you."

        hide LRivera at leftLR





        jump C16_done


    label C16_no:

        show LRivera at leftLR
        LR "How did you know this is exactly what I wanted?"

        JR "I didn’t, but hey it’s a pretty good coincidence isn’t it? Figured you’d appreciate something practical."

        LR "Yes! I love it!"

        "There was a glint in Leonor’s eyes as she examined the blade of the pair of scissors"

        hide LRivera at leftLR






        jump C16_done


#Choice19 of OUTLINE LEONOR VALENZUELA ROUTE: EPISODE 3
    label C19_yes:

        show Javier at leftJA

        JR "I do love her."

        "Javier gave a long suffering sigh."

        JL "I see…"

        JR "And it seems that you do too."

        JL "Yes. Even though I know I shouldn’t. Even though I know I can’t give her the life she deserves."

        JR "Then why continue to see her?"

        JL "Because… Because when I’m around her I don’t feel like I have to fulfill any expectations. "
        JL "Like I can just be myself and not keep putting up this self-important front. I just feel so tired."

        hide Javier at leftJA




        jump C19_done


    label C19_no:

        show Javier at leftJA
        JR "I might come to love her someday, but I’ll have to wait and see."

        JL "Leonor deserves better than some playboy treating this as if it’s a game."

        JR "Oh yeah? Well she can tell me that herself if she likes. She doesn’t need you playing white knight for her. Let me guess, you love her?"

        JL "Yes. Even though I know I shouldn’t. Even though I know I can’t give her the life she deserves."

        JR "Then why continue to see her?"

        JL "Because… Because when I’m around her I don’t feel like I have to fulfill any expectations. "
        JL "Like I can just be myself and not keep putting up this self-important front. I just feel so tired."

        hide Javier at leftJA






        jump C19_done


#Choice20 of OUTLINE LEONOR RIVERA ROUTE: EPISODE 3
    label C20_yes:

        show LRivera at leftLR
        JR "Because I have come to love you, Leonor."

        "Tears filled Leonor’s eyes."

        LR "Why is that so hard to believe?"

        "The sight of Leonor wiping her tears broke something inside of me. "
        "Broken people had sharp edges, they cut and make you bleed but they were also fragile that ought to be handled delicately. "
        "I couldn’t stop myself from putting together the shards, to make something whole again."

        JR "You don’t have to believe me right now. But someday, I hope you heal from the things you don’t tell me and allow yourself to accept the love that you deserve."

        "Leonor let out a sob and broke down. I didn’t know how to comfort a lady without seeming inappropriate, so I just let her be true to her feelings and cry herself towards clarity."



        jump C20_done


    label C20_no:

        show LRivera at leftLR
        JR "Because that’s what family are for, Leonor."

        "Tears filled Leonor’s eyes."

        LR "Family… "

        JR "Even then. I know you’re going through something heavy now but I want you to know that I’ll be there for you."

        "She looked up at me with a sad smile on her face."

        LR "Thank you, Jose."

        "The both of us made the rest of the way back home in silence."



        jump C20_done



    label splashscreen:
        scene black with dissolve
        pause (3)
        show logo with dissolve
        pause (5)
        hide logo with dissolve
        pause (3)
        show disclaimer with dissolve
        pause (7)
        hide disclaimer with dissolve
        pause (3)
        return
