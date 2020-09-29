label ep7:
                scene blackscreen
                with dissolve
                default ep7alice = False
                default ep7alicefriend = False
                default ep7robbery = False
                default ep7helpfromalex = False
                "..."
                "... ... ..."
                "... ... ... ..."
                show 7newalex2
                with dissolve
                " In the morning, you open your eyes."
                a "\" You're up?\""
                p "\" Yeah.\""
                a "\" I could hear the change in your breathing.\""
                p "\" You're that in tune to me, eh?\""
                hide 7newalex2
                show 7newalex3
                with dissolve
                a "\" I'd say that I'm that perceptive.\""
                p "\" You think highly of yourself.\""
                a "\" He he...\""
                a "\" Well, someone has to do it.\""
                hide 7newalex3
                show 7newalex4
                with dissolve
                a "\" Did you sleep ok?\""
                p "\" Like the dead.\""
                a "\" Don't say that.\""
                a "\" It's not appropriate for someone who does what you do.\""
                a "\" Ok. Better get up.\""
                call screen screen40

label ep7alexgo:
                scene 7newalex5
                with dissolve
                " She stands up."
                a "\" Come on, babe.\""
                a "\" We have to get up.\""
                a "\" Gotta check on Dad and Izzy.\""
                p "\" Right behind you.\""
                jump ep7cont1

label ep7holdher:
                scene 7newalex4
                with dissolve
                $ alexpoints = alexpoints + 1
                " She tries to get up, but you don't let go of her hand."
                show 7newalex6
                with dissolve
                a "\" Puppy?\""
                a "\" We have to get up.\""
                p "\" No, we don't.\""
                a "\" Yes, we do.\""
                p "\" Not without a good morning kiss.\""
                a "\" Aww... Come here.\""
                hide 7newalex6
                show 7newalex7
                with dissolve
                " She bends her neck back, and kisses you."
                hide 7newalex7
                show 7newalex6
                with dissolve
                a "\" Will you let me get up now?\""
                p "\" Hmmm...\""
                a "\" Puppy?\""
                p "\" *Sigh* Alright.\""
                hide 7newalex6
                show 7newalex8
                with dissolve
                " She stands up."
                a "\" Come on babe.\""
                a "\" We have to get up.\""
                a "\" Gotta check on Dad and Izzy.\""
                p "\" Right behind you.\""
                jump ep7cont1

label ep7cont1:
                scene 7newalex9
                with dissolve
                " You and Alex go to her bedroom."
                a "\" Sleeping with her mouth open again.\""
                a "\" Tired.\""
                a "\" Babe?\""
                a "\" Babe, wake up!\""
                show 7newalex10
                with dissolve
                " She struggles a bit, and gets up."
                i "\" Uhh...\""
                i "\" It's morning?\""
                a "\" Yeah.\""
                hide 7newalex10
                show 7newalex11
                with dissolve
                i "\" Woke up last night, and you weren't there.\""
                i "\" What happened?\""
                a "\" I had other obligations.\""
                a "\" Miss me?\""
                i "\" Always.\""
                hide 7newalex11
                show 7newalex12
                with dissolve
                a "\" I'll go check on Dad.\""
                a "\" You two can get ready on your own.\""
                if izzyin == False:
                    hide 7newalex12
                    show 7newalex13
                    with dissolve
                    " As soon as Alex leaves, Izzy rushes to the bathroom."
                    i "\" I got dibs on the shower.\""
                    p "\" *Sigh*\""
                    hide 7newalex13
                    show 7newalex25
                    with dissolve
                    " It took a while for you both to wash, change and head downstairs."
                    " Where you find Alex cooking breakfast."
                    p "\" Smells nice.\""
                    a "\" Don't ride my dick.\""
                    a "\" I know what you think of my cooking.\""
                    p "\" I wasn't.\""
                    a "\" Yeah, right.\""
                    hide 7newalex25
                    show 7newalex27
                    with dissolve
                    i "\" It does smells nice though.\""
                    a "\" Another one.\""
                    a "\" I get it. No one likes my cooking.\""
                    a "\" But unless you're volunteering to take over, you'll eat what I give you.\""
                    hide 7newalex27
                    show 7newalex33
                    with dissolve
                    " She manages to make some eggs, and you wolf it down."
                    hide 7newalex33
                    show 7newalex35
                    with dissolve
                    a "\" Have you seen Dad?\""
                    p "\" No.\""
                    a "\" He's usually up already.\""
                    a "\" I'll go check on him.\""
                    hide 7newalex35
                    show 7newalex40
                    with dissolve
                    " She comes back after a few minutes."
                    a "\" Dad is feeling sick.\""
                    p "\" Is he ok?\""
                    hide 7newalex40
                    show 7newalex41
                    with dissolve
                    a "\" Yeah.\""
                    a "\" Probably just a cold.\""
                    a "\" He wants to talk to you, though.\""
                    p "\" Alright?\""
                    a "\" Once you go upstairs it's the fourth door on the left.\""
                    p "\" Got it.\""
                    jump ep7cont2

                else:
                    hide 7newalex12
                    show 7newalex14
                    with dissolve
                    " Izzy starts yawning as soon as she leaves."
                    i "\" *Yawn*\""
                    p "\" Still sleepy?\""
                    i "\" Yeah.\""
                    hide 7newalex14
                    show 7newalex15
                    with dissolve
                    i "\" Still early, though.\""
                    i "\" Come here. We have a few minutes.\""
                    p "\" For what?\""
                    i "\" Just cuddling.\""
                    i "\" Get your head out of the gutter.\""
                    hide 7newalex15
                    show 7newalex16
                    with dissolve
                    " You lie down on the bed besides her."
                    i "\" I like this.\""
                    i "\" In my mind, the best moments in life are like this.\""
                    i "\" Sunday morning, in bed, doing crosword puzzles or sudoku. Something like that.\""
                    p "\" Lazing around?\""
                    i "\" Yeah.\""
                    hide 7newalex16
                    show 7newalex17
                    with dissolve
                    i "\" Mmmm...\""
                    i "\" Are you ok?\""
                    p "\" Sure, why do you ask?\""
                    i "\" Well...\""
                    hide 7newalex17
                    show 7newalex18
                    with dissolve
                    i "\" Other duties?\""
                    i "\" Alex came to you last night, didn't she?\""
                    p "\" Well, yeah.\""
                    i "\" She wouldn't do that. Not in this house, for no reason.\""
                    i "\" So?\""
                    i "\" What happened?\""
                    p "\" Work stuff. But I'm ok.\""
                    p "\" She worries too much.\""
                    i "\" She sees it as her job to worry about you.\""
                    i "\" You'll get used to it.\""
                    hide 7newalex18
                    show 7newalex17
                    with dissolve
                    i "\" *Sigh*\""
                    i "\" Alright.\""
                    i "\" Now we really have to get up.\""
                    hide 7newalex17
                    show 7newalex19
                    with dissolve
                    " She gets up and goes to the bathroom."
                    i "\" Are you coming?\""
                    label galleryScene4:
                    hide 7newalex19
                    show 7newalex20
                    with dissolve
                    " You follow behind her, and she gets in the shower."
                    hide 7newalex20
                    show 7newalex21
                    with dissolve
                    i "\" Are you coming in or no?\""
                    i "\" We can share, you know.\""
                    p "\" Since I'm being invited...\""
                    hide 7newalex21
                    show 7newalex22
                    with dissolve
                    i "\" Invited to shower together, not...\""
                    i "\" I mean, we have time.\""
                    i "\" But not that kind of time.\""
                    p "\" He he...\""
                    hide 7newalex22
                    show 7newalex23
                    with dissolve
                    " You get out of the shower, and get back in the bedroom."
                    p "\" Not a fan of towels?\""
                    i "\" Nothing against them. I just preffer to air dry.\""
                    i "\" Didn't feel I need to hide around you.\""
                    p "\" You don't.\""
                    hide 7newalex23
                    $ renpy.end_replay()
                    show 7newalex24
                    with dissolve
                    " You wait for Izzy to air dry, get dressed, and head downstairs."
                    hide 7newalex24
                    show 7newalex25
                    with dissolve
                    " Where you find Alex cooking breakfast."
                    p "\" Smells nice.\""
                    a "\" Don't ride my dick.\""
                    a "\" I know what you think of my cooking.\""
                    p "\" I wasn't.\""
                    a "\" Yeah, right.\""
                    hide 7newalex25
                    show 7newalex26
                    with dissolve
                    i "\" What are you talking about?\""
                    i "\" Everyone likes uncooked bacon.\""
                    a "\" You too, Brutus?\""
                    a "\" You too?\""
                    a "\" Sit your ass down.\""
                    hide 7newalex26
                    show 7newalex28
                    with dissolve
                    " She sits down at the table."
                    i "\" Where is Mr. Boris?\""
                    hide 7newalex28
                    show 7newalex29
                    with dissolve
                    a "\" Haven't seen him.\""
                    a "\" He's usually up by now.\""
                    a "\" Must've had a long night.\""
                    a "\" I'll go get him once I'm finished here.\""
                    hide 7newalex29
                    show 7newalex30
                    with dissolve
                    i "\" Yeah.\""
                    i "\" Wouldn't want him to miss out on clammy eggs.\" She sorta whispers to you."
                    a "\" I heard that!\""
                    hide 7newalex30
                    show 7newalex32
                    with dissolve
                    i "\" Better shut up, lest she sends us to school with no breakfast.\""
                    a "\" Don't make me come back there, kids.\""
                    i "\" Told you.\""
                    i "\" He he...\""
                    hide 7newalex32
                    show 7newalex33
                    with dissolve
                    " She manages to make some eggs, and you wolf it down."
                    hide 7newalex33
                    show 7newalex34
                    with dissolve
                    a "\" I see you ate it quick enough.\""
                    a "\" Despite both your protestations.\""
                    p "\" A man in the desert must take such water as he is offered.\""
                    a "\" Ass!\""
                    a "\" You're both conspiring against me now.\""
                    i "\" Well...\""
                    hide 7newalex34
                    show 7newalex35
                    with dissolve
                    a "\" Where the hell is Dad?\""
                    a "\" He's usually up already.\""
                    a "\" I'll go check on him.\""
                    hide 7newalex35
                    show 7newalex36
                    with dissolve
                    i "\" We'd better clean up.\""
                    hide 7newalex36
                    show 7newalex37
                    with dissolve
                    i "\" Give me your plate.\""
                    p "\" Ok...\""
                    hide 7newalex37
                    show 7newalex38
                    with dissolve
                    " She takes your plate and starts washing up."
                    i "\" I hope you haven't forgotten.\""
                    p "\" About what?\""
                    hide 7newalex38
                    show 7newalex39
                    with dissolve
                    i "\" Our date?\""
                    p "\" Of course I haven't.\""
                    i "\" Good.\""
                    i "\" Momma has been feeling pretty good lately.\""
                    i "\" I'm just saying. Better be sooner than later.\""
                    i "\" Later I might be busy.\""
                    p "\" How about tonight?\""
                    i "\" Can you do that?\""
                    p "\" I don't see why not.\""
                    i "\" Ok.\""
                    hide 7newalex39
                    show 7newalex40
                    with dissolve
                    " Alex comes back after a few minutes."
                    a "\" Dad is feeling sick.\""
                    p "\" Is he ok?\""
                    hide 7newalex40
                    show 7newalex41
                    with dissolve
                    a "\" Yeah.\""
                    a "\" Probably just a cold.\""
                    a "\" He wants to talk to you, though.\""
                    p "\" Alright?\""
                    a "\" Once you go upstairs it's the fourth door on the left.\""
                    p "\" Got it.\""
                    jump ep7cont2

label ep7cont2:
                scene 7newalex42
                with dissolve
                " You head upstairs."
                p "\" Boss?\""
                show 7newalex43
                with dissolve
                b "\" [player_name]?\""
                b "\" *Cough* *Cough*\""
                b "\" Come in.\""
                hide 7newalex43
                show 7newalex44
                with dissolve
                " He sits up."
                b "\" *Cough* *Cough* *Cough*\""
                p "\" Are you ok?\""
                b "\" Yes, yes, I'm fine.\""
                b "\" Just the sniffles.\""
                hide 7newalex44
                show 7newalex45
                with dissolve
                " He stands up."
                b "\" *Cough* *Cough* *Cough*\""
                p "\" Are you sure?\""
                b "\" Of course I'm sure.\""
                hide 7newalex45
                show 7newalex46
                with dissolve
                b "\" Won't be going to work today though.\""
                p "\" Alright.\""
                b "\" Should let you catch up on your little cathouse too.\""
                hide 7newalex46
                show 7newalex47
                with dissolve
                b "\" *Cough* *Cough* *Cough*\""
                p "\" Boss?\""
                b "\" *Cough* *Cough* *Cough* I'm fine.\""
                hide 7newalex47
                show 7newalex48
                with dissolve
                b "\" I'll need you to drop by Dima's for me.\""
                b "\" Tell him, he has to take care of, the thing.\""
                p "\" What thing?\""
                b "\" He'll know what I'm talking about.\""
                hide 7newalex48
                show 7newalex47
                with dissolve
                b "\" *Cough* *Cough* *Cough*\""
                hide 7newalex47
                show 7newalex49
                with dissolve
                " He sits back down."
                b "\" *Cough* *Cough* Damn it...\""
                p "\" Can I get you something?\""
                b "\" You can do what I tell you.\""
                hide 7newalex49
                show 7newalex50
                with dissolve
                " He lies back down."
                b "\" Just drop by Dima's.\""
                b "\" And take the girls to school.\""
                p "\" Done.\""
                b "\" You can go.\""
                p "\" Right.\""
                hide 7newalex50
                show 7newalex51
                with dissolve
                " You head back down, and find the girls dressed for school."
                a "\" I'm thinking about swimming.\""
                i "\" Swimming?\""
                a "\" I need a hobby. And it keeps you in shape.\""
                i "\" I guess.\""
                hide 7newalex51
                show 7newalex52
                with dissolve
                a "\" Hey.\""
                a "\" How's Dad?\""
                p "\" Coughing.\""
                a "\" I know that.\""
                p "\" Well, he's unchanged.\""
                a "\" What did he want with you?\""
                p "\" Just some instructions for today.\""
                p "\" He's not coming to work.\""
                a "\" Of course he's not.\""
                a "\" He's supposed to be resting.\""
                hide 7newalex52
                show 7newalex53
                with dissolve
                a "\" Allright, let's go.\""
                a "\" I'll call Dad this afternoon. See how he's doing.\""
                hide 7newalex53
                show back1
                with dissolve
                show 7newalex54
                with dissolve
                " While driving them, you can't help but see that Alexandra is worried."
                p "\" Everything good?\""
                a "\" Yeah.\""
                p "\" Then why that puss on your face?\""
                a "\" Thinking about Dad.\""
                hide 7newalex54
                show 7newalex55
                with dissolve
                i "\" Will you stop it?\""
                i "\" He's fine.\""
                a "\" Well...\""
                i "\" You wanna take the day off from school?\""
                i "\" Stay with him?\""
                a "\" I'm not that worried.\""
                hide 7newalex55
                show 7newalex56
                with dissolve
                " But her expression never changed."
                if izzyin == True:
                    hide 7newalex56
                    show 7newalex57
                    with dissolve
                    i "\" Wanna get cheered up?\""
                    a "\" Huh?\""
                    i "\" [player_name] and me are going on a date tonight.\""
                    hide 7newalex57
                    show 7newalex59
                    with dissolve
                    a "\" Is it tonight?\""
                    i "\" Yup.\""
                    a "\" Where is he taking you?\""
                    i "\" I have no clue.\""
                    p "\" Neither do I, if I'm honest.\""
                    hide 7newalex59
                    show 7newalex58
                    with dissolve
                    i "\" I'm sure it will be nice.\""
                    p "\" I wish I had your confidence.\""
                    hide 7newalex58
                    show 7newalex59
                    with dissolve
                    a "\" You know what he's doing right now?\""
                    a "\" He's lowering expectations.\""
                    a "\" So when he takes you to McDonald's, you'll be happy it's not the hot dog stall under the bridge.\""
                    p "\" I told you that in confidence.\""
                    a "\" He he...\""
                    hide 7newalex59
                    show 7newalex60
                    with dissolve
                    i "\" McDonald's is fine.\""
                    p "\" It won't be that.\""
                    i "\" It's fine if it is.\""
                    p "\" It won't be.\""
                    jump ep7cont3

                else:
                    jump ep7cont3

label ep7cont3:
                scene 7newalex61
                with dissolve
                " You drop the girls off, and head to Dima's."
                di "\" Well, if it isn't the former gardner.\""
                p "\" Excuse me?\""
                di "\" Just fucking with you.\""
                di "\" What news do you bring from the high castle?\""
                p "\" The boss is sick.\""
                p "\" He said that you should take care of the 'thing'.\""
                p "\" Didn't mention what 'thing' it was.\""
                p "\" But said that you'd know what he was talking about.\""
                show 7newalex62
                with dissolve
                di "\" I do know what he means.\""
                di "\" Guess you're not privy to everything then.\""
                di "\" His Daughter. But not everything.\""
                p "\" Do we have a problem?\""
                di "\" Problem? No problem.\""
                di "\" Why would there be a problem?\""
                di "\" But now, you've delivered your message little pigeon.\""
                di "\" Time for you to fly away.\""
                p "\" Fuck is wrong with you?\""
                di "\" Me? Nothing.\""
                p "\" Fuck's sake.\""
                hide 7newalex62
                show back1
                with dissolve
                show 7newalex88
                with dissolve
                " You get back to the car."
                p "\" The fuck is his problem?\""
                p "\" Alright.\""
                p "\" I have some time. Might as well take care of the cop thing.\""
                hide 7newalex88
                show 7newalex63
                with dissolve
                em "\" Hello my friend.\""
                em "\" I trust you have some good news for me.\""
                p "\" I'm ready to do what you want.\""
                em "\" Good.\""
                p "\" But how do I do it?\""
                p "\" I can't just walk up to the guy.\""
                p "\" I don't even know where I'd find him.\""
                em "\" *Sigh*\""
                em "\" Do you need me to wipe your ass for you too?\""
                em "\" Fine.\""
                em "\" Come to the house.\""
                p "\" The house?\""
                em "\" Where we first met.\""
                em "\" Be there in half an hour.\""
                " *Click*"
                p "\" Hmm...\""
                hide 7newalex63
                show 7newalex64
                with dissolve
                " You drive over there."
                em "\" You know...\""
                em "\" For a gangster, you don't have a lot of street smarts.\""
                em "\" Can't even get an introduction?\""
                em "\" What do you do? Just punch stuff?\""
                p "\" Are you going to help me, or not?\""
                em "\" Of course.\""
                em "\" Now that you see the right road.\""
                em "\" How does that song go? When you're good to Momma, Momma's good to you?\""
                em "\" This way.\""
                hide 7newalex64
                show 7newalex65
                with dissolve
                " You follow her inside."
                dar "\" Why am I here?\""
                em "\" Shut up!\""
                em "\" You're here to do what I tell you.\""
                em "\" Now, let me make the introductions.\""
                hide 7newalex65
                show 7newalex66
                with dissolve
                em "\" Darius, this is [player_name].\""
                em "\"[player_name], this is Darius.\""
                em "\" A small time dealer, who keeps getting caught.\""
                em "\" Now Darius over here would've been in prison for most of his life if it wasn't for me.\""
                em "\" You see? I can be good to you.\""
                em "\" Darius, you'll be introducing [player_name] to your friend Marcello.\""
                dar "\" He's not my friend.\""
                em "\" He's close enough.\""
                em "\" You'll tell him that [player_name] over here is looking to buy.\""
                hide 7newalex66
                show 7newalex65
                with dissolve
                dar "\" Are you kidding me?\""
                dar "\" Is he a cop?\""
                em "\" No.\""
                dar "\" Still...\""
                dar "\" I mean... If Marcello suspects I'm doing him dirty...\""
                dar "\" This is too much, Em.\""
                hide 7newalex65
                show 7newalex67
                with dissolve
                em "\" You're looking at this the wrong way.\""
                em "\" You're worried about Marcello, when you should be worried about me.\""
                em "\" If not for me, you'd be in prison.\""
                dar "\" Emma, this is too much.\""
                dar "\" You can't make me.\""
                em "\" Making you? I'm not making you do anything.\""
                em "\" But if you do let me down, I might just take it personally.\""
                em "\" Not only will you go to prison, but I'll make sure you have so much dick shoved up your ass you'll wish you were born a woman.\""
                em "\" There are a lot of men in there that would kill, for me to owe them a favor.\""
                em "\" Prison dick, Darius.\""
                em "\" You'll have so much cum up your ass, you'll be able to subsist on it.\""
                dar "\" That image...\""
                em "\" I'm not making you do anything.\""
                em "\" We all have a choice.\""
                em "\" And your choice is do what I tell you, or grab ankle.\""
                dar "\" *Sigh*\""
                em "\" I love it.\""
                hide 7newalex67
                show 7newalex68
                with dissolve
                " You all go back to the garage."
                em "\" I love it when it all comes together.\""
                em "\" Marcello here will get your foot in the door.\""
                em "\" After that it's up to you.\""
                hide 7newalex68
                show 7newalex69
                with dissolve
                dar "\" I'm still not sure this is a good idea.\""
                hide 7newalex69
                show 7newalex70
                with dissolve
                em "\" I thought I made myself clear.\""
                dar "\" Alright, alright... Jesus.\""
                hide 7newalex70
                show 7newalex68
                with dissolve
                em "\" I trust I'll hear from you soon.\""
                p "\" Yeah...\""
                hide 7newalex68
                show back1
                with dissolve
                show 7newalex72
                with dissolve
                " You go to the car."
                p "\" To Marcello's?\""
                dar "\" He hangs out at this garden.\""
                p "\" Garden?\""
                dar "\" Says he likes to make things grow.\""
                dar "\" I'll show you the way.\""
                p "\" Alright.\""
                " After a few minutes he says..."
                dar "\" Fucking cunt!\""
                p "\" Emma?\""
                dar "\" Just once.\""
                dar "\" Just once I'd like to bend her over, and show her who's boss.\""
                hide 7newalex72
                show 7newalex73
                with dissolve
                dar "\" Subsist on cum?\""
                dar "\" I'll show her how to subsist on cum.\""
                p "\" She does have an edge to her.\""
                dar "\" Yeah.\""
                hide 7newalex73
                show 7newalex74
                with dissolve
                " You arrive at the address Darius gives you."
                hide 7newalex74
                show 7newalex75
                with dissolve
                dar "\" Let me do the talking, ok?\""
                p "\" Your show, boss.\""
                hide 7newalex75
                show 7newalex76
                with dissolve
                dar "\" Vincenzo, my man!\""
                vinc "\" The fuck are you doing here.\""
                dar "\" I'm here to see the boss.\""
                dar "\" If you could get out of my way, Vinnie?\""
                hide 7newalex76
                show 7newalex77
                with dissolve
                vinc "\" Don't call me that, boy!\""
                vinc "\" You ain't going anywhere.\""
                dar "\" I promise you, he wants to see me.\""
                vinc "\" He might want to see you.\""
                vinc "\" But are you sure you want to see him?\""
                hide 7newalex77
                show 7newalex78
                with dissolve
                mar "\" Let them through.\""
                mar "\" I'm dying to hear this.\""
                hide 7newalex78
                show 7newalex79
                with dissolve
                dar "\" See?\""
                dar "\" He's dying to see me.\""
                vinc "\" Huh!\""
                vinc "\" You don't have a lot of brains, do you.\""
                hide 7newalex79
                show 7newalex80
                with dissolve
                mar "\" Darius.\""
                dar "\" Bossman.\""
                mar "\" I can only assume you've come to pay me what you owe me.\""
                dar "\" I don't have it yet, Boss.\""
                mar "\" Maybe Vincenzo is right.\""
                mar "\" You're not that bright, are you?\""
                dar "\" I don't have your money. But I have something better.\""
                mar "\" What's better than money?\""
                dar "\" This guy.\""
                hide 7newalex80
                show 7newalex81
                with dissolve
                " He looks at you."
                mar "\" You?\""
                mar "\" And who are you?\""
                p "\" [player_name].\""
                mar "\" Never heard of you.\""
                mar "\" Is Darius right? Are you better than money?\""
                p "\" I wouldn't say that.\""
                mar "\" Your friend seems to disagree with you Darius.\""
                hide 7newalex81
                show 7newalex82
                with dissolve
                dar "\" He's a buyer, Boss.\""
                dar "\" Big buyer.\""
                dar "\" He came to me, but I can't handle the size of his orders.\""
                dar "\" So, I brought him to you.\""
                dar "\" That should buy me a couple of weeks to pay you back. Right?\""
                mar "\" Shut up!\""
                hide 7newalex82
                show 7newalex83
                with dissolve
                mar "\" Is that so?\""
                mar "\" Big buyer?\""
                mar "\" How come I've never heard of you?\""
                hide 7newalex83
                show 7newalex82
                with dissolve
                dar "\" He's with Boris's crew.\""
                mar "\" Shut up!\""
                hide 7newalex82
                show 7newalex83
                with dissolve
                mar "\" Is that so?\""
                mar "\" Looking to make something extra behind you're boss' back?\""
                p "\" Well...\""
                mar "\" I see.\""
                hide 7newalex83
                show 7newalex84
                with dissolve
                mar "\" Well, I'll check you out.\""
                mar "\" If I hear good things... Well...\""
                mar "\" There's a 500k minimum order though.\""
                p "\" 500k?\""
                mar "\" Well?\""
                mar "\" Are you a real buyer or just wasting my time?\""
                mar "\" Any less than that and it's not worth the aggravation for me.\""
                p "\" That's not...\""
                mar "\" What?\""
                p "\" I'll get it.\""
                mar "\" Good.\""
                mar "\" Let me know when you do.\""
                hide 7newalex84
                show 7newalex85
                with dissolve
                vinc "\" Alright.\""
                vinc "\" It's time for both of you to go.\""
                hide 7newalex85
                show back1
                with dissolve
                show 7newalex86
                with dissolve
                " You get back to the car."
                dar "\" Easy as pie.\""
                p "\" 500k...\""
                dar "\" What?\""
                dar "\" Don't tell me you don't got it.\""
                dar "\" I thought Boris' guys were loaded.\""
                hide 7newalex86
                show 7newalex87
                with dissolve
                dar "\" That bitch though...\""
                dar "\" Threaten me with a dicking...\""
                dar "\" We'll see.\""
                p "\" Whatever man.\""
                p "\" Where do I drop you off?\""
                hide 7newalex87
                show 7newalex88
                with dissolve
                " After dropping off Darius, you're left alone in the car."
                p "\" 500k...\""
                p "\" Fuck!\""
                hide 7newalex88
                show 7newalex63
                with dissolve
                em "\" Hello?\""
                p "\" It's me.\""
                em "\" I trust the meeting went well.\""
                p "\" Well, we're still alive.\""
                p "\" But he wants five hundred thousand.\""
                em "\" So?\""
                em "\" Get it for him.\""
                p "\" Are you kidding me?\""
                em "\" I can't be wiping your ass all day.\""
                em "\" Get it done!\""
                " *Click*"
                p "\" Fuck!\""
                hide 7newalex63
                show 7newalex89
                with dissolve
                " You go to the agency."
                yuri "\" Hey Boss!\""
                yuri "\" You ok?\""
                p "\" Yeah.\""
                yuri "\" Looks like you have the weight of the world on your shoulders.\""
                p "\" I'm fine.\""
                hide 7newalex89
                show 7newalex90
                with dissolve
                yuri "\" So, I've been talking to the girls.\""
                yuri "\" They're more open to that thing than I thought.\""
                p "\" Thing? Oh, right.\""
                yuri "\" So, when are we going to get it.\""
                p "\" Soon. I'm working on it.\""
                hide 7newalex90
                show 7newalex91
                with dissolve
                p "\" Where the fuck?\""
                p "\" Where the fuck am I going to get the cash?\""
                hide 7newalex91
                show 7newalex92
                with dissolve
                " You look at your goons."
                " You suppose you could steal it."
                " But from where."
                hide 7newalex92
                show 7newalex93
                with dissolve
                " You could ask Boris for it."
                " Maybe Alexandra."
                " But that means you'd have to come clean."
                " Better cover all your bases."
                if alicehug1 == True:
                    " You'll have to call Alice."
                    hide 7newalex93
                    show 7newalex99
                    with dissolve
                    ali "\" What's up?\""
                    p "\" Let's take a ride.\""
                    ali "\" Ok.\""
                    hide 7newalex99
                    show back1
                    with dissolve
                    show 7newalex100
                    with dissolve
                    ali "\" What is it?\""
                    p "\" I need money.\""
                    ali "\" I think that's a universal issue.\""
                    p "\" I'm serious.\""
                    p "\" I need to find a lot of cash soon.\""
                    ali "\" You mean, steal it?\""
                    hide 7newalex100
                    show 7newalex101
                    with dissolve
                    ali "\" Might I suggest a bank?\""
                    p "\" Be serious.\""
                    p "\" I need a lot of cash.\""
                    p "\" From people who won't run to the law when they lose it.\""
                    ali "\" There's only one kind of people that do that.\""
                    p "\" I know.\""
                    ali "\" Alright.\""
                    ali "\" I'll show you where to go.\""
                    hide 7newalex101
                    with dissolve
                    show 7newalex97
                    with dissolve
                    " You follow her directions."
                    p "\" The hell is that?\""
                    ali "\" A laundry shop.\""
                    ali "\" But every other day, there's a poker game.\""
                    ali "\" Big money.\""
                    ali "\" One hundred thousand buy in, I hear.\""
                    p "\" Perfect.\""
                    hide 7newalex97
                    show back1
                    with dissolve
                    show 7newalex102
                    with dissolve
                    ali "\" Dangerous people.\""
                    p "\" I imagined as much.\""
                    p "\" How much do you want?\""
                    ali "\" Want?\""
                    p "\" A percentage of the take is the custom, I think.\""
                    ali "\" Oh, no.\""
                    ali "\" I don't want a dime of that money.\""
                    ali "\" When the people who it belongs to start looking for it, I don't want them to find it on me.\""
                    p "\" Are you sure?\""
                    ali "\" Positive.\""
                    hide 7newalex102
                    show 7newalex103
                    with dissolve
                    ali "\" I do want something, though.\""
                    p "\" What?\""
                    ali "\" Well...\""
                    p "\" Well?\""
                    hide 7newalex103
                    show 7newalex104
                    with dissolve
                    ali "\" I haven't heard from you in a while...\""
                    p "\" Sorry about that.\""
                    ali "\" I mean, friends should see each other more often.\""
                    ali "\" And people who are more... Or want to...\""
                    call screen screen41

                else:
                    " You'll have to call Lenny"
                    hide 7newalex93
                    show 7newalex94
                    with dissolve
                    " You call Lenny and go to your place."
                    lenny "\" What's up?\""
                    p "\" Let's take a ride.\""
                    lenny "\" Ok.\""
                    hide 7newalex94
                    show back1
                    with dissolve
                    show 7newalex95
                    with dissolve
                    lenny "\" What is it?\""
                    p "\" I need money.\""
                    lenny "\" Don't we all?\""
                    p "\" I'm serious.\""
                    p "\" I need to find a lot of cash soon.\""
                    lenny "\" You mean, steal it?\""
                    p "\" Well?\""
                    p "\" I need you to find me a score.\""
                    lenny "\" A score.\""
                    hide 7newalex95
                    show 7newalex96
                    with dissolve
                    p "\" Yeah.\""
                    p "\" A lot of cash.\""
                    p "\" From people who won't run to the law when they lose it.\""
                    lenny "\" There's only one kind of people that do.\""
                    p "\" I know.\""
                    lenny "\" Alright.\""
                    lenny "\" I'll show you where to go.\""
                    hide 7newalex96
                    show 7newalex97
                    with dissolve
                    " You follow his directions."
                    p "\" The hell is that?\""
                    lenny "\" A laundry shop.\""
                    lenny "\" But on every other day, there's a poker game.\""
                    lenny "\" Big money.\""
                    lenny "\" One hundred thousand buy in, I hear.\""
                    p "\" Perfect.\""
                    hide 7newalex97
                    show back1
                    with dissolve
                    show 7newalex98
                    with dissolve
                    p "\" How much do you want?\""
                    lenny "\" Want?\""
                    p "\" A percentage of the take is the custom, I think.\""
                    lenny "\" Oh, no.\""
                    lenny "\" I don't want a dime of that money.\""
                    lenny "\" When the people who it belongs to start looking for it, I don't want them to find it on me.\""
                    p "\" Are you sure?\""
                    lenny "\" Positive.\""
                    p "\" Ok.\""
                    p "\" Thanks.\""
                    lenny "\" No problem.\""
                    lenny "\" Or, I should say. Your problem.\""
                    lenny "\" Can you drop me off?\""
                    p "\" Sure.\""
                    jump ep7cont4

label ep7aliceapologize:
                scene back1
                with dissolve
                show 7newalex104
                with dissolve
                $ ep7alicefriend = True
                p "\" You're right.\""
                p "\" I apologize.\""
                p "\" We should see each other more often.\""
                hide 7newalex104
                show 7newalex109
                with dissolve
                ali "\" As friends?\""
                p "\" As friends.\""
                ali "\" Ok.\""
                p "\" I promise.\""
                ali "\" No problem.\""
                ali "\" Can you drop me off?\""
                p "\" Sure.\""
                ali "\" And I hope to hear from you soon.\""
                p "\" Karaoke night.\""
                ali "\" He he...\""
                ali "\" Ok.\""
                jump ep7cont4

label ep7kissalice:
                $ ep7alice = True
                scene back1
                with dissolve
                show 7newalex105
                with dissolve
                " You go closer to her."
                p "\" More?\""
                ali "\" Huh?\""
                p "\" You said more.\""
                hide 7newalex105
                show 7newalex106
                with dissolve
                " You get so close your lips are almost touching."
                ali "\" Did I?\""
                p "\" Yes.\""
                hide 7newalex106
                show 7newalex107
                with dissolve
                " You kiss her."
                hide 7newalex107
                show 7newalex108
                with dissolve
                ali "\" More, eh?\""
                p "\" Right now...\""
                ali "\" You're too busy for a relationship?\""
                p "\" Something like that.\""
                hide 7newalex108
                show 7newalex109
                with dissolve
                ali "\" But you won't always be too busy?\""
                p "\" I hope not.\""
                p "\" I'd hate to think what I'd miss out on.\""
                ali "\" He he...\""
                hide 7newalex109
                show 7newalex110
                with dissolve
                " You drive back to your place."
                hide 7newalex110
                show 7newalex111
                with dissolve
                ali "\" I haven't seen you in a while.\""
                ali "\" How are you?\""
                p "\" Pretty good.\""
                p "\" Some work problems.\""
                hide 7newalex111
                show 7newalex112
                with dissolve
                ali "\" Is that why you're looking for a score?\""
                p "\" Pretty much.\""
                ali "\" Are you in trouble?\""
                p "\" He he...\""
                p "\" I was born in trouble.\""
                hide 7newalex112
                show 7newalex113
                with dissolve
                ali "\" Listen...\""
                ali "\" I don't know much about that card game.\""
                ali "\" But I hear that the people that play in it are pretty dangerous.\""
                p "\" I figured.\""
                hide 7newalex113
                show 7newalex114
                with dissolve
                ali "\" You'll be careful, right?\""
                p "\" Of course.\""
                hide 7newalex114
                show 7newalex115
                with dissolve
                ali "\" And if you do it...\""
                p "\" Yes?\""
                ali "\" You'll call me right after, right?\""
                p "\" Why?\""
                hide 7newalex115
                show 7newalex116
                with dissolve
                " She gives you a kiss."
                hide 7newalex116
                show 7newalex115
                with dissolve
                ali "\" So I know that you're ok.\""
                p "\" I will.\""
                ali "\" Promise?\""
                p "\" Promise.\""
                hide 7newalex115
                show 7newalex117
                with dissolve
                ali "\" I have to go.\""
                ali "\" Lenny will wonder where I am.\""
                ali "\" But...\""
                p "\" But?\""
                ali "\" Take my advice, and don't do it.\""
                ali "\" The poker game.\""
                p "\" Thanks for the advice.\""
                ali "\" Bye.\""
                p "\" Bye.\""
                jump ep7cont4

label ep7cont4:
                scene 7newalex91
                with dissolve
                " You spend the rest of the day at the office, til it's time to pick up the girls."
                show back1
                with dissolve
                show 7newalex119
                with dissolve
                i "\" Will you stop worrying?\""
                a "\" I called Dad and he didn't answer.\""
                i "\" He's probably just sleeping.\""
                i "\" I think you're letting your control issues get the better of you.\""
                a "\" I don't have control issues.\""
                i "\" Yeah, right.\""
                hide 7newalex119
                show 7newalex120
                with dissolve
                a "\" Puppy?\""
                a "\" Can we stop by the drugstore?\""
                a "\" I wanna get Dad some cough syrup.\""
                p "\" Sure.\""
                hide 7newalex120
                show 7newalex121
                with dissolve
                " You stop, and she runs to get the syrup."
                if izzyin == False:
                    jump ep7noizzydate
                else:
                    jump ep7izzydate

label ep7noizzydate:
                scene back1
                with dissolve
                show 7newalex126
                with dissolve
                " And comes back five minutes later."
                p "\" All good?\""
                a "\" Yes.\""
                a "\" Let's go.\""
                hide 7newalex126
                show 7newalex127
                with dissolve
                " You get to the villa."
                a "\" Can you take care of things while I go check on Dad?\""
                i "\" Take care of things?\""
                a "\" Dinner... Whatever...\""
                i "\" Sure.\""
                hide 7newalex127
                show 7newalex128
                with dissolve
                a "\" Hey Dad.\""
                b "\" Alex.\""
                a "\" How are you?\""
                b "\" Still coughing, but better.\""
                hide 7newalex128
                show 7newalex129
                with dissolve
                a "\" I called you earlier.\""
                b "\" Huh?\""
                a "\" You didn't answer.\""
                b "\" I was probably sleeping.\""
                a "\" Got me worried.\""
                b "\" About what?\""
                a "\" Nevermind.\""
                hide 7newalex129
                show 7newalex130
                with dissolve
                a "\" Do you need anything?\" She asks you."
                p "\" Me?\""
                p "\" No.\""
                a "\" Well, Dad needs his rest.\""
                p "\" Guess that's my cue to leave.\""
                hide 7newalex130
                show 7newalex132
                with dissolve
                " With Alex busy and nothing else to do, you make yourself confortable, and just watch some TV for the rest of the day."
                hide 7newalex132
                show 7newalex208
                with dissolve
                " Til it's time to go to bed."
                hide 7newalex208
                show 7newalex226
                with dissolve
                a "\" Hey.\""
                p "\" Hey.\""
                a "\" Came to wish you good night.\""
                p "\" How is Mr. Boris.\""
                hide 7newalex226
                show 7newalex227
                with dissolve
                " She comes next to you."
                a "\" Still coughing.\""
                a "\" And you know... Putting a brave face on it.\""
                p "\" Are you really worried?\""
                hide 7newalex227
                show 7newalex228
                with dissolve
                a "\" Nah.\""
                a "\" But you know how it is.\""
                a "\" You have to take care of those close to you.\""
                a "\" Especially when they can't take care of themselves.\""
                p "\" I think your Father can take care of himself only too well.\""
                hide 7newalex228
                show 7newalex229
                with dissolve
                " She gives you a kiss."
                a "\" Good night.\""
                p "\" Good night.\""
                hide 7newalex229
                show 7newalex230
                with dissolve
                " She runs her hand down your side."
                a "\" Huh?\""
                p "\" What?\""
                hide 7newalex230
                show 7newalex231
                with dissolve
                a "\" Where's your scar?\""
                p "\" Scar?\""
                a "\" Where he stabbed you.\""
                a "\" You know... The guy...\""
                p "\" I'm a good healer.\""
                hide 7newalex231
                show 7newalex232
                with dissolve
                a "\" Still. There should be something there.\""
                a "\" I can't see anything.\""
                p "\" What would you like me to say?\""
                a "\" Strange.\""
                hide 7newalex232
                show 7newalex229
                with dissolve
                " She gives you another kiss."
                hide 7newalex229
                show 7newalex241
                with dissolve
                a "\" See you tomorrow.\""
                " If you're going to ask her for help, this is the time."
                " Do you tell her about Emma?"
                call screen screen42

label ep7izzydate:
                scene back1
                with dissolve
                show 7newalex122
                with dissolve
                i "\" Are you ok?\""
                i "\" You seem much gloomier than this morning.\""
                p "\" Just some work stuff.\""
                hide 7newalex122
                show 7newalex123
                with dissolve
                i "\" Problems?\""
                p "\" You could say that.\""
                i "\" Can I help?\""
                p "\" I don't see how.\""
                p "\" But thanks for offering.\""
                i "\" Is our date off?\""
                i "\" Are you too busy?\""
                p "\" No.\""
                i "\" You should talk to Alex.\""
                i "\" She always knows what to do.\""
                i "\" She has a mind like that.\""
                i "\" And besides... Boss' Daughter.\""
                p "\" He he...\""
                hide 7newalex123
                show 7newalex124
                with dissolve
                " She gives you a kiss."
                hide 7newalex124
                show 7newalex125
                with dissolve
                i "\" Better?\""
                p "\" He he... Yes.\""
                i "\" Glad if I helped.\""
                hide 7newalex125
                show 7newalex126
                with dissolve
                " Alex comes back five minutes later."
                p "\" All good?\""
                a "\" Yes.\""
                a "\" Let's go.\""
                hide 7newalex126
                show 7newalex127
                with dissolve
                " You get to the villa."
                a "\" Can you take care of things while I go check on Dad?\""
                i "\" Take care of things?\""
                a "\" Dinner... Whatever...\""
                i "\" Sure.\""
                hide 7newalex127
                show 7newalex128
                with dissolve
                a "\" Hey Dad.\""
                b "\" Alex.\""
                a "\" How are you?\""
                b "\" Still coughing, but better.\""
                hide 7newalex128
                show 7newalex129
                with dissolve
                a "\" I called you earlier.\""
                b "\" Huh?\""
                a "\" You didn't answer.\""
                b "\" I was probably sleeping.\""
                a "\" Got me worried.\""
                b "\" About what?\""
                a "\" Nevermind.\""
                hide 7newalex129
                show 7newalex130
                with dissolve
                a "\" Do you need anything?\" She asks you."
                p "\" Me?\""
                p "\" No.\""
                a "\" Well, Dad needs his rest.\""
                p "\" Guess that's my cue to leave.\""
                hide 7newalex130
                show 7newalex133
                with dissolve
                " You head downstairs."
                p "\" Can I help with anything?\""
                hide 7newalex133
                show 7newalex134
                with dissolve
                i "\" Not really.\""
                i "\" I can handle it.\""
                i "\" Where are we going tonight?\""
                p "\" Restaurant?\""
                p "\" Movie?\""
                hide 7newalex134
                show 7newalex135
                with dissolve
                i "\" Sounds nice.\""
                p "\" I hope so.\""
                p "\" Can I tell you something?\""
                p "\" I don't really date.\""
                i "\" Me neither.\""
                i "\" But we'll muddle through.\""
                hide 7newalex135
                show 7newalex136
                with dissolve
                " A few minutes later, Alex comes back."
                i "\" How's Mr. Boris?\""
                a "\" The same.\""
                a "\" *Sniffles*\""
                a "\" But it's hard for a man his age.\""
                hide 7newalex136
                show 7newalex137
                with dissolve
                a "\" So. Big date night?\""
                p "\" Yeah.\""
                a "\" Have you decided where you're going?\""
                p "\" Restaurant.\""
                a "\" That's a start.\""
                hide 7newalex137
                show 7newalex138
                with dissolve
                i "\" Neither of us are really experienced at this.\""
                i "\" I've mostly been with you...\""
                hide 7newalex138
                show 7newalex137
                with dissolve
                a "\" And he's a neanderthall.\""
                a "\" I get it.\""
                a "\" He's used to just grabbing a woman by the hair, give her a tumble, and tell her to raise his kids right.\""
                i "\" Family tradition.\""
                hide 7newalex137
                show 7newalex139
                with dissolve
                a "\" All I can tell you is, if he's telling he'll just put it in for five seconds, don't believe him.\""
                a "\" He's lying!\""
                i "\" How would you know?\""
                a "\" I hear things.\""
                hide 7newalex139
                show 7newalex140
                with dissolve
                a "\" Well, have fun you two.\""
                a "\" I'll stay home with Dad.\""
                p "\" Need anything?\""
                a "\" I'm good.\""
                p "\" Alright.\""
                a "\" Have fun.\""
                hide 7newalex140
                show back1
                with dissolve
                show 7newalex141
                with dissolve
                " You leave the villa."
                i "\" Mind if we drop by my place?\""
                i "\" I need to change, and check on Momma.\""
                i "\" I wanna see how she's doing. And if she's getting along with Mrs. Anabelle.\""
                p "\" Mrs. Anabelle?\""
                i "\" Mr. Boris sent her to help out.\""
                i "\" One of those living assistants.\""
                p "\" Ok.\""
                i "\" She comes for a few hours every day.\""
                p "\" Sure.\""
                hide 7newalex141
                show 7newalex142
                with dissolve
                " You go to her place."
                i "\" Momma?\""
                hide 7newalex142
                show 7newalex143
                with dissolve
                ag "\" Isabella?\""
                ag "\" Where have you been?\""
                i "\" I've been sleeping at Alex's.\""
                i "\" I called you yesterday.\""
                ag "\" No you didn't.\""
                hide 7newalex143
                show 7newalex144
                with dissolve
                i "\" Yes. Yes I did.\""
                ag "\" Well, I don't remember.\""
                ag "\" And who's this?\""
                i "\" That's [player_name], Momma.\""
                i "\" You've met him before.\""
                ag "\" Did I?\""
                hide 7newalex144
                show 7newalex145
                with dissolve
                i "\" I'm gonna go change.\""
                i "\" I'll be right back.\""
                p "\" Sure.\""
                hide 7newalex145
                show 7newalex146
                with dissolve
                ag "\" Where are you two going?\""
                p "\" Out to eat, Mrs. Agatha.\""
                ag "\" And that's all you'll be doing.\""
                ag "\" My Daughter isn't some loose blonde, you know.\""
                p "\" I know, Ma'am.\""
                hide 7newalex146
                show 7newalex147
                with dissolve
                i "\" Ready.\""
                i "\" What do you think?\""
                p "\" Wow!\""
                hide 7newalex147
                show 7newalex148
                with dissolve
                i "\" Not ashamed to be seen with me then?\""
                p "\" I'd say you pass.\""
                p "\" For now.\""
                i "\" That's very generous of you.\""
                p "\" Well, I try.\""
                hide 7newalex148
                show 7newalex149
                with dissolve
                ag "\" What are you doing?\""
                i "\" Momma?\""
                hide 7newalex149
                show 7newalex150
                with dissolve
                ag "\" You're not going anywhere dressed like that.\""
                i "\" Yes, I am.\""
                ag "\" No, you're not.\""
                ag "\" I raised you better.\""
                ag "\" Might as well dye your hair blonde.\""
                hide 7newalex150
                show 7newalex151
                with dissolve
                i "\" I'm done with this conversation Momma.\""
                ag "\" You're not going out like that.\""
                i "\" Yes I am.\""
                hide 7newalex151
                show 7newalex152
                with dissolve
                " She takes your arm."
                ag "\" Where are you going?\""
                i "\" Bye, Momma.\""
                i "\" I'll call you tomorrow.\""
                ag "\" Slut!\""
                hide 7newalex152
                show back1
                with dissolve
                show 7newalex153
                with dissolve
                i "\" I'm sorry about that.\""
                p "\" You have nothing to apologize for.\""
                i "\" She's better, you know.\""
                i "\" She's lucid.\""
                i "\" But sometime, even when she's lucid...\""
                p "\" If I don't understand, no one does.\""
                hide 7newalex153
                show 7newalex154
                with dissolve
                i "\" You really do, don't you?\""
                p "\" I've done a lot worse than her.\""
                p "\" Trust me.\""
                i "\" So you said.\""
                hide 7newalex154
                show 7newalex155
                with dissolve
                " You give her a kiss on the head."
                hide 7newalex155
                show 7newalex156
                with dissolve
                i "\" He he he...\""
                i "\" Thanks.\""
                p "\" Tonight is all about you, ok?\""
                i "\" Ok.\""
                hide 7newalex156
                show 7newalex157
                with dissolve
                " You get to the restaurant."
                i "\" This is nice.\""
                p "\" You think so?\""
                p "\" I have no clue.\""
                hide 7newalex157
                show 7newalex158
                with dissolve
                i "\" You keep saying that.\""
                p "\" Only because it's true.\""
                i "\" It's wonderful.\""
                hide 7newalex158
                show 7newalex159
                with dissolve
                " You both sit down."
                i "\" So, how come you don't date much?\""
                p "\" I don't really know.\""
                p "\" Never felt the need to.\""
                i "\" So, you lived like a hermit?\""
                p "\" Far from it, to be honest.\""
                i "\" So, sex without dating?\""
                p "\" More or less.\""
                hide 7newalex159
                show 7newalex160
                with dissolve
                i "\" He he he...\""
                i "\" If you can get away with it?\""
                p "\" Guess I've just been lucky.\""
                hide 7newalex160
                show 7newalex161
                with dissolve
                " You order, and dig in."
                hide 7newalex161
                show 7newalex162
                with dissolve
                " She looks at you with an air of innocence all througout the dinner."
                " You get the feeling that there's something very childish inside her, regardless of everything."
                p "\" What?\""
                i "\" What?\""
                p "\" Why are you looking at me like that?\""
                i "\" I'm not.\""
                hide 7newalex162
                show 7newalex163
                with dissolve
                " Dinner is soon over, and it's time to leave."
                hide 7newalex163
                show 7newalex164
                with dissolve
                i "\" Where next?\""
                p "\" I think a movie is the traditional thing.\""
                i "\" And we're nothing if not traditional.\""
                p "\" Exactly.\""
                i "\" Two girls, one guy...\""
                p "\" That's how it used to be in the really old days.\""
                i "\" So, we're REALLY traditional.\""
                p "\" Exactly.\""
                hide 7newalex164
                show 7newalex165
                with dissolve
                i "\" Give me your hand.\" She says, on your way over to the cinema."
                p "\" Ok.\""
                hide 7newalex165
                show 7newalex166
                with dissolve
                " She takes it and places it in her lap."
                p "\" Huh?\""
                p "\" What's that about?\""
                hide 7newalex166
                show 7newalex167
                with dissolve
                i "\" Nothing, really.\""
                i "\" I just enjoy the intimacy.\""
                i "\" Don't you?\""
                p "\" I think I do.\""
                hide 7newalex167
                show 7newalex168
                with dissolve
                " You get to the cinema."
                i "\" What are we going to see?\""
                p "\" Whatever you want.\""
                i "\" You don't have a preference?\""
                p "\" Sure.\""
                p "\" The dirty dozen.\""
                hide 7newalex168
                show 7newalex169
                with dissolve
                i "\" Never heard of it.\""
                p "\" Excuse me?\""
                i "\" What? Is it good?\""
                p "\" Is it good?\""
                p "\" *Sigh*\""
                p "\" We'll need a movie night.\""
                p "\" Seriously.\""
                i "\" What?\""
                p "\" Remember what you said before? About me not being embarrased to be seen with you?\""
                p "\" I take that back.\""
                i "\" He he...\""
                i "\" So, you are embarrased.\""
                p "\" I am now.\""
                i "\" Guess I'll have to see ' The Dirty Dozen', then.\""
                p "\" It's a priority.\""
                hide 7newalex169
                show 7newalex170
                with dissolve
                " Eventually you go to a typical horror movie."
                " The usual stuff."
                " Neither of you were very impressed."
                hide 7newalex170
                show 7newalex171
                with dissolve
                " At the end of it, you get back to the car."
                i "\" Do you have anything else planned?\""
                p "\" Well, not really.\""
                i "\" Good.\""
                i "\" Can we swing by my building?\""
                p "\" Sure.\""
                p "\" Why?\""
                i "\" I wanna show you something.\""
                hide 7newalex171
                show 7newalex172
                with dissolve
                " You arrive at her building."
                i "\" Here!\""
                i "\" Stop here.\""
                hide 7newalex172
                show 7newalex173
                with dissolve
                i "\" Hey!\""
                m3 "\" Isabella?\""
                m3 "\" Finally going to let me get a piece?\""
                i "\" Sorry.\""
                i "\" In 50 years. If you're still single.\""
                m3 "\" It's a date.\""
                i "\" Can I get the key?\""
                m3 "\" Sure.\""
                hide 7newalex173
                show 7newalex174
                with dissolve
                " She takes a key from him, and comes back to you."
                i "\" I want for us to have one thing that's just ours.\""
                i "\" Come with me.\""
                i "\" I wanna show you something.\""
                p "\" Lead the way.\""
                hide 7newalex174
                show 7newalex175
                with dissolve
                " After a few flights of stairs, you get to a rooftop garden."
                p "\" What is this place?\""
                hide 7newalex175
                show 7newalex176
                with dissolve
                i "\" My secret place.\""
                i "\" I've never brought anyone else here.\""
                i "\" Not even Alex.\""
                p "\" Is that so?\""
                hide 7newalex176
                show 7newalex177
                with dissolve
                " She takes off her shoes."
                i "\" You're the first person...\""
                p "\" Thank you.\""
                hide 7newalex177
                show 7newalex178
                with dissolve
                " She lies down on the pillows."
                i "\" Come.\""
                i "\" Lie with me.\""
                hide 7newalex178
                show 7newalex180
                with dissolve
                p "\" Who's place is this.\""
                i "\" The guy downstairs?\""
                p "\" Yeah?\""
                i "\" It's his Dad's.\""
                i "\" But he's in a wheelchair these days.\""
                i "\" He can't come up here anymore.\""
                i "\" I've been maintaining it.\""
                hide 7newalex180
                show 7newalex181
                with dissolve
                i "\" I'm always so relaxed here.\""
                i "\" Ever since I was a kid.\""
                hide 7newalex181
                show 7newalex182
                with dissolve
                p "\" You've been coming here since you were a kid?\""
                hide 7newalex182
                show 7newalex183
                with dissolve
                i "\" Yes.\""
                i "\" I used to run here and hide, when Momma...\""
                i "\" Well.\""
                i "\" It doesn't matter now.\""
                i "\" It's always been my secret place.\""
                hide 7newalex183
                show 7newalex184
                with dissolve
                " She turns to you."
                i "\" And now it will be ours.\""
                i "\" If you're ok with it.\""
                p "\" Sure.\""
                p "\" Maybe we could buy it.\""
                i "\" Then it wouldn't be secret anymore.\""
                i "\" And it wouldn't be special.\""
                i "\" It would just be... Property.\""
                p "\" Strange way of looking at it.\""
                i "\" I'm a strange girl.\""
                hide 7newalex184
                show 7newalex185
                with dissolve
                " You kiss."
                hide 7newalex185
                show 7newalex186
                with dissolve
                i "\" You can't tell anyone about it.\""
                i "\" Not even Alex.\""
                p "\" Got it.\""
                " *Ring* *Ring* *Ring*"
                hide 7newalex186
                show 7newalex187
                with dissolve
                i "\" Speak of the devil.\""
                i "\" Must be her.\""
                i "\" I'd better get that.\""
                hide 7newalex187
                show 7newalex188
                with dissolve
                i "\" Hello?\""
                i "\" I knew it was you.\""
                i "\" Well, what can I say.\""
                i "\" Dinner and a movie.\""
                i "\" He's taking me to meet some of his friends.\""
                i "\" He said something about a train?\""
                i "\" Never knew he was that mechanical.\""
                hide 7newalex188
                show 7newalex189
                with dissolve
                i "\" Aha?\""
                i "\" Yes?\""
                i "\" What's feltching?\""
                i "\" Babe?\""
                i "\" Babe, get off the internet.\""
                i "\" Aha...\""
                i "\" I will.\""
                hide 7newalex189
                show 7newalex190
                with dissolve
                i "\" She sends you a kiss.\""
                hide 7newalex190
                show 7newalex191
                with dissolve
                i "\" We're fine.\""
                i "\" Ok, we'll see you soon.\""
                i "\" Love you.\""
                i "\" Bye.\""
                hide 7newalex191
                show 7newalex192
                with dissolve
                " She puts her arms around you again."
                p "\" Is everything ok?\""
                i "\" Just checking up on us.\""
                i "\" Bit of a control freak, you know.\""
                i "\" Father's Daughter.\""
                hide 7newalex192
                show 7newalex193
                with dissolve
                " She turns aroud, and pull your hand around her."
                i "\" I want to ask.\""
                p "\" Yes?\""
                i "\" You said you lose control like me.\""
                p "\" Worse than you, I think.\""
                hide 7newalex193
                show 7newalex194
                with dissolve
                i "\" After you do it.\""
                i "\" Do you ever wonder if you are insane.\""
                i "\" Because...\""
                i "\" Because I wonder.\""
                hide 7newalex194
                show 7newalex195
                with dissolve
                " She turns back around."
                i "\" Do you think you're insane?\""
                i "\" Do you think I am?\""
                p "\" Me? Maybe.\""
                p "\" You're not.\""
                p "\" Insane people don't wonder if they're crazy.\""
                p "\" They're far too busy for that.\""
                hide 7newalex195
                show 7newalex196
                with dissolve
                i "\" He he he...\""
                " She rubs her nose against yours."
                i "\" Thanks.\""
                i "\" And I'm sorrry.\""
                i "\" You know... For poisoning you.\""
                p "\" That's not a phrase you hear every day.\""
                i "\" Just from us traditional people.\""
                p "\" He he...\""
                hide 7newalex196
                label galleryScene5:
                show 7newalex209
                with dissolve
                " Her hand moves down, and starts rubbing your dick."
                p "\" What are you doing?\""
                i "\" Traditional date stuff.\""
                p "\" No.\""
                hide 7newalex209
                show 7newalex210
                with dissolve
                i "\" No?\""
                p "\" Tonight is all about you.\""
                p "\" What you want to do.\""
                i "\" Is it?\""
                i "\" And what makes you think I don't want this?\""
                hide 7newalex210
                show 7newalex211
                with dissolve
                " She takes her dress off."
                i "\" Now you.\""
                p "\" Aren't you worried someone will see us?\""
                i "\" No one will see.\""
                i "\" Not here.\""
                hide 7newalex211
                show 7newalex212
                with dissolve
                " She helps you undress and gets on top of you."
                i "\" Is it about me?\""
                p "\" All about you.\""
                i "\" My nipples.\""
                i "\" I like...\""
                hide 7newalex212
                show 7newalex213
                with dissolve
                " You gently rub your lips against her nipples."
                i "\" Yes.\""
                hide 7newalex213
                show 7newalex214
                with dissolve
                i "\" *Sigh*\""
                i "\" Gently.\""
                i "\" Like that.\""
                hide 7newalex214
                show 7newalex215
                with dissolve
                " She reaches back and starts rubbing your dick."
                i "\" I like it gently.\""
                p "\" Yes Ma'am.\""
                i "\" Will you let me do it?\""
                p "\" All about you.\""
                p "\" Whatever you want.\""
                hide 7newalex215
                show 7newalex216
                with dissolve
                " She slowly inserts your dick inside her."
                i "\" Ahh...\""
                hide 7newalex216
                show 7newalex217
                with dissolve
                " Then lightly sits down on it."
                hide 7newalex217
                show 7newalex218
                with dissolve
                i "\" Don't move.\""
                i "\" Just...\""
                i "\" Just let me do it.\""
                scene izzysex2 animated with fade:
                    "6a1.webp"
                    pause 0.06
                    "6a2.webp"
                    pause 0.06
                    "6a3.webp"
                    pause 0.06
                    "6a4.webp"
                    pause 0.06
                    "6a5.webp"
                    pause 0.06
                    "6a6.webp"
                    pause 0.06
                    "6a7.webp"
                    pause 0.06
                    "6a8.webp"
                    pause 0.06
                    "6a9.webp"
                    pause 0.06
                    "6a10.webp"
                    pause 0.06
                    "6a11.webp"
                    pause 0.06
                    "6a12.webp"
                    pause 0.06
                    "6a13.webp"
                    pause 0.06
                    "6a14.webp"
                    pause 0.06
                    "6a15.webp"
                    pause 0.06
                    "6a16.webp"
                    pause 0.06
                    "6a17.webp"
                    pause 0.06
                    "6a18.webp"
                    pause 0.06
                    "6a19.webp"
                    pause 0.06
                    "6a20.webp"
                    pause 0.06
                    "6a21.webp"
                    pause 0.06
                    "6a22.webp"
                    pause 0.06
                    "6a23.webp"
                    pause 0.06
                    "6a24.webp"
                    pause 0.06
                    "6a25.webp"
                    pause 0.06
                    "6a26.webp"
                    pause 0.06
                    "6a27.webp"
                    pause 0.06
                    "6a28.webp"
                    pause 0.06
                    "6a29.webp"
                    pause 0.06
                    "6a30.webp"
                    pause 0.06
                    repeat
                " She slowly begins to ride you."
                i "\" Ahh...\""
                i "\" Ohhh...\""
                p "\" This is how you like it?\""
                i "\" Yesssss...\""
                $ renpy.pause ()
                show 7newalex220
                with dissolve
                i "\" If you need it faster...\""
                p "\" I don't.\""
                scene izzysex2 animated with fade:
                    "6a1.webp"
                    pause 0.06
                    "6a2.webp"
                    pause 0.06
                    "6a3.webp"
                    pause 0.06
                    "6a4.webp"
                    pause 0.06
                    "6a5.webp"
                    pause 0.06
                    "6a6.webp"
                    pause 0.06
                    "6a7.webp"
                    pause 0.06
                    "6a8.webp"
                    pause 0.06
                    "6a9.webp"
                    pause 0.06
                    "6a10.webp"
                    pause 0.06
                    "6a11.webp"
                    pause 0.06
                    "6a12.webp"
                    pause 0.06
                    "6a13.webp"
                    pause 0.06
                    "6a14.webp"
                    pause 0.06
                    "6a15.webp"
                    pause 0.06
                    "6a16.webp"
                    pause 0.06
                    "6a17.webp"
                    pause 0.06
                    "6a18.webp"
                    pause 0.06
                    "6a19.webp"
                    pause 0.06
                    "6a20.webp"
                    pause 0.06
                    "6a21.webp"
                    pause 0.06
                    "6a22.webp"
                    pause 0.06
                    "6a23.webp"
                    pause 0.06
                    "6a24.webp"
                    pause 0.06
                    "6a25.webp"
                    pause 0.06
                    "6a26.webp"
                    pause 0.06
                    "6a27.webp"
                    pause 0.06
                    "6a28.webp"
                    pause 0.06
                    "6a29.webp"
                    pause 0.06
                    "6a30.webp"
                    pause 0.06
                    repeat
                " She doesn't increase the pace at all."
                i "\" Ahh...\""
                " Just letting herself enjoy you."
                " Focusing solely on her own pleasure."
                i "\" Ahhh...\""
                i "\" Ahh...\""
                i "\" I'm gonna...\""
                p "\" Do it.\""
                p "\" Let go.\""
                p "\" Let go, Izzy.\""
                p "\" You're safe with me.\""
                $ renpy.pause ()
                show 7newalex219
                with dissolve
                i "\" Ahhh... Ah...\""
                p "\" Did you?\""
                i "\" Ahh...\""
                i "\" *Pant*\""
                i "\" Yes...\""
                show 7newalex220
                with dissolve
                i "\" Want to do it roughly now?\""
                i "\" More friction?\""
                p "\" I'm good.\""
                i "\" But you didn't...\""
                p "\" It's not what tonight is about.\""
                hide 7newalex220
                show 7newalex221
                with dissolve
                " She kisses your neck."
                i "\" You're too sweet, you know.\""
                p "\" I have a feeling that's what you need.\""
                i "\" It is.\""
                hide 7newalex221
                show 7newalex222
                with dissolve
                " She pulls away from you."
                i "\" But we can't have you leaving with blue balls.\""
                hide 7newalex222
                show 7newalex223
                with dissolve
                i "\" Now, let me take care of you.\""
                p "\" You don't have to.\""
                scene izzyblow2 animated with fade:
                    "7a1.webp"
                    pause 0.06
                    "7a2.webp"
                    pause 0.06
                    "7a3.webp"
                    pause 0.06
                    "7a4.webp"
                    pause 0.06
                    "7a5.webp"
                    pause 0.06
                    "7a6.webp"
                    pause 0.06
                    "7a7.webp"
                    pause 0.06
                    "7a8.webp"
                    pause 0.06
                    "7a9.webp"
                    pause 0.06
                    "7a10.webp"
                    pause 0.06
                    "7a11.webp"
                    pause 0.06
                    "7a12.webp"
                    pause 0.06
                    "7a13.webp"
                    pause 0.06
                    "7a14.webp"
                    pause 0.06
                    "7a15.webp"
                    pause 0.06
                    "7a16.webp"
                    pause 0.06
                    "7a17.webp"
                    pause 0.06
                    "7a18.webp"
                    pause 0.06
                    "7a19.webp"
                    pause 0.06
                    "7a20.webp"
                    pause 0.06
                    "7a21.webp"
                    pause 0.06
                    "7a22.webp"
                    pause 0.06
                    "7a23.webp"
                    pause 0.06
                    "7a24.webp"
                    pause 0.06
                    "7a25.webp"
                    pause 0.06
                    "7a26.webp"
                    pause 0.06
                    "7a27.webp"
                    pause 0.06
                    "7a28.webp"
                    pause 0.06
                    "7a29.webp"
                    pause 0.06
                    "7a30.webp"
                    pause 0.06
                    repeat
                " She starts sucking on your dick."
                " Slowly at first."
                $ renpy.pause ()
                scene izzyblow2 animated with fade:
                    "7a1.webp"
                    pause 0.04
                    "7a2.webp"
                    pause 0.04
                    "7a3.webp"
                    pause 0.04
                    "7a4.webp"
                    pause 0.04
                    "7a5.webp"
                    pause 0.04
                    "7a6.webp"
                    pause 0.04
                    "7a7.webp"
                    pause 0.04
                    "7a8.webp"
                    pause 0.04
                    "7a9.webp"
                    pause 0.04
                    "7a10.webp"
                    pause 0.04
                    "7a11.webp"
                    pause 0.04
                    "7a12.webp"
                    pause 0.04
                    "7a13.webp"
                    pause 0.04
                    "7a14.webp"
                    pause 0.04
                    "7a15.webp"
                    pause 0.04
                    "7a16.webp"
                    pause 0.04
                    "7a17.webp"
                    pause 0.04
                    "7a18.webp"
                    pause 0.04
                    "7a19.webp"
                    pause 0.04
                    "7a20.webp"
                    pause 0.04
                    "7a21.webp"
                    pause 0.04
                    "7a22.webp"
                    pause 0.04
                    "7a23.webp"
                    pause 0.04
                    "7a24.webp"
                    pause 0.04
                    "7a25.webp"
                    pause 0.04
                    "7a26.webp"
                    pause 0.04
                    "7a27.webp"
                    pause 0.04
                    "7a28.webp"
                    pause 0.04
                    "7a29.webp"
                    pause 0.04
                    "7a30.webp"
                    pause 0.04
                    repeat
                " Then faster."
                $ renpy.pause ()
                scene izzyblow2 animated with fade:
                    "7a1.webp"
                    pause 0.02
                    "7a2.webp"
                    pause 0.02
                    "7a3.webp"
                    pause 0.02
                    "7a4.webp"
                    pause 0.02
                    "7a5.webp"
                    pause 0.02
                    "7a6.webp"
                    pause 0.02
                    "7a7.webp"
                    pause 0.02
                    "7a8.webp"
                    pause 0.02
                    "7a9.webp"
                    pause 0.02
                    "7a10.webp"
                    pause 0.02
                    "7a11.webp"
                    pause 0.02
                    "7a12.webp"
                    pause 0.02
                    "7a13.webp"
                    pause 0.02
                    "7a14.webp"
                    pause 0.02
                    "7a15.webp"
                    pause 0.02
                    "7a16.webp"
                    pause 0.02
                    "7a17.webp"
                    pause 0.02
                    "7a18.webp"
                    pause 0.02
                    "7a19.webp"
                    pause 0.02
                    "7a20.webp"
                    pause 0.02
                    "7a21.webp"
                    pause 0.02
                    "7a22.webp"
                    pause 0.02
                    "7a23.webp"
                    pause 0.02
                    "7a24.webp"
                    pause 0.02
                    "7a25.webp"
                    pause 0.02
                    "7a26.webp"
                    pause 0.02
                    "7a27.webp"
                    pause 0.02
                    "7a28.webp"
                    pause 0.02
                    "7a29.webp"
                    pause 0.02
                    "7a30.webp"
                    pause 0.02
                    repeat
                " And faster."
                i "\" Mph...\""
                " Completely the opposite of her earlier gentleness."
                " And it doesn't take long til you blow."
                $ renpy.pause ()
                show 7newalex224
                with dissolve
                i "\" GHhhh..gg..\""
                i "\" *Gulp* *Gulp*\""
                p "\" Fuck.\""
                i "\" *Gulp* *Gulp*\""
                p "\" That's...\""
                p "\" *Whew*\""
                show 7newalex225
                with dissolve
                " Once your dick is clean, she pulls away."
                i "\" See?\""
                i "\" I can take care of you too.\""
                p "\" I never doubted you.\""
                hide 7newalex225
                show 7newalex222
                with dissolve
                i "\" We really should get going.\""
                i "\" Alex will start worrying soon.\""
                p "\" Sure.\""
                i "\" And remember... This place.\""
                p "\" My lips are sealed.\""
                i "\" Thank you.\""
                hide 7newalex222
                $ renpy.end_replay()
                show 7newalex197
                with dissolve
                " You put your clothes back on."
                i "\" I enjoyed it you know...\""
                i "\" Not just... Everything...\""
                p "\" You're a very sweet girl.\""
                hide 7newalex197
                show back1
                with dissolve
                show 7newalex198
                with dissolve
                " You drive back to the villa."
                i "\" We'll get along, won't we.\""
                i "\" I mean... The three of us.\""
                i "\" We won't...\""
                p "\" You don't need to be insecure.\""
                i "\" I can't help it.\""
                i "\" Not about this.\""
                p "\" You have nothing to be insecure about.\""
                i "\" Thanks.\""
                hide 7newalex198
                show 7newalex202
                with dissolve
                " You get to the villa."
                p "\" Hey.\""
                p "\" You're still up?\""
                hide 7newalex202
                show 7newalex203
                with dissolve
                a "\" Hey.\""
                a "\" Well Dad has been... Evacuating...\""
                p "\" Evacuating?\""
                a "\" Don't worry about it.\""
                a "\" Suffice to say, I've been playing Florence Nightingale while you two were out having fun.\""
                p "\" Jealous?\""
                a "\" A little.\""
                hide 7newalex203
                show 7newalex204
                with dissolve
                i "\" We missed you.\""
                a "\" Thanks, babe.\""
                hide 7newalex204
                show 7newalex205
                with dissolve
                a "\" Now what's this train I've been hearing about?\""
                hide 7newalex205
                show 7newalex206
                with dissolve
                i "\" Just Puppy and his friends.\""
                i "\" They're so close.\""
                i "\" So willing to share.\""
                hide 7newalex206
                show 7newalex205
                with dissolve
                a "\" I bet.\""
                hide 7newalex205
                show 7newalex207
                with dissolve
                i "\" Pretty tired.\""
                i "\" I'm going to bed.\""
                p "\" Good night.\""
                i "\" Good night.\""
                hide 7newalex207
                show 7newalex203
                with dissolve
                p "\" You?\""
                a "\" Dad is still up.\""
                a "\" You go ahead.\""
                a "\" I'll see you in the morning.\""
                p "\" Alright.\""
                hide 7newalex203
                show 7newalex208
                with dissolve
                " You head upstairs and get in bed."
                hide 7newalex208
                show 7newalex226
                with dissolve
                a "\" Hey.\""
                p "\" Hey.\""
                a "\" Just wanted to check up on you.\""
                p "\" How is Mr. Boris.\""
                hide 7newalex226
                show 7newalex227
                with dissolve
                " She comes next to you."
                a "\" Still coughing.\""
                a "\" And you know... Putting a brave face on it.\""
                p "\" Are you really worried?\""
                hide 7newalex227
                show 7newalex228
                with dissolve
                a "\" Nah.\""
                a "\" But you know how it is.\""
                a "\" You have to take care of those close to you.\""
                a "\" Especially when they can't take care of themselves.\""
                p "\" I think your Father can take care of himself only too well.\""
                hide 7newalex228
                show 7newalex229
                with dissolve
                " She gives you a kiss."
                a "\" Good night.\""
                p "\" Good night.\""
                hide 7newalex229
                show 7newalex230
                with dissolve
                " She runs her hand down your side."
                a "\" Huh?\""
                p "\" What?\""
                hide 7newalex230
                show 7newalex231
                with dissolve
                a "\" Where's your scar?\""
                p "\" Scar?\""
                a "\" Where he stabbed you.\""
                a "\" You know... The guy...\""
                p "\" I'm a good healer.\""
                hide 7newalex231
                show 7newalex232
                with dissolve
                a "\" Still. There should be something there.\""
                a "\" I can't see anything.\""
                p "\" What would you like me to say?\""
                a "\" Strange.\""
                hide 7newalex232
                show 7newalex229
                with dissolve
                " She gives you another kiss."
                hide 7newalex229
                show 7newalex228
                with dissolve
                a "\" I just wanted to say, I really appreciate what you're doing.\""
                a "\" With Izzy, you know.\""
                a "\" All the effort you're putting in.\""
                a "\" You really do love me, don't you.\""
                p "\" Do you still doubt that?\""
                a "\" I doubt everything.\""
                a "\" It's my nature.\""
                a "\" But it's becoming very hard to doubt you.\""
                hide 7newalex228
                show 7newalex233
                with dissolve
                " She kisses your stomach."
                hide 7newalex233
                label galleryScene6:
                show 7newalex234
                with dissolve
                " Then moves down to your crotch."
                p "\" What are you?\""
                a "\" What do you think?\""
                p "\" Izzy already...\""
                a "\" I'm sure.\""
                a "\" You have two girlfriends now.\""
                a "\" And are you really going to argue with me while I'm trying to eat your dick?\""
                p "\" Eat my dick?\""
                a "\" Been spending time on the internet.\""
                a "\" Bored most of the evening.\""
                hide 7newalex234
                show 7newalex235
                with dissolve
                " You pull off your pants."
                a "\" There you are.\""
                " She starts nibbling on the head of your dick."
                scene alexblow2 animated with fade:
                    "8a1.webp"
                    pause 0.05
                    "8a2.webp"
                    pause 0.05
                    "8a3.webp"
                    pause 0.05
                    "8a4.webp"
                    pause 0.05
                    "8a5.webp"
                    pause 0.05
                    "8a6.webp"
                    pause 0.05
                    "8a7.webp"
                    pause 0.05
                    "8a8.webp"
                    pause 0.05
                    "8a9.webp"
                    pause 0.05
                    "8a10.webp"
                    pause 0.05
                    "8a11.webp"
                    pause 0.05
                    "8a12.webp"
                    pause 0.05
                    "8a13.webp"
                    pause 0.05
                    "8a14.webp"
                    pause 0.05
                    "8a15.webp"
                    pause 0.05
                    "8a16.webp"
                    pause 0.05
                    "8a17.webp"
                    pause 0.05
                    "8a18.webp"
                    pause 0.05
                    "8a19.webp"
                    pause 0.05
                    "8a20.webp"
                    pause 0.05
                    "8a21.webp"
                    pause 0.05
                    "8a22.webp"
                    pause 0.05
                    "8a23.webp"
                    pause 0.05
                    "8a24.webp"
                    pause 0.05
                    "8a25.webp"
                    pause 0.05
                    "8a26.webp"
                    pause 0.05
                    "8a27.webp"
                    pause 0.05
                    "8a28.webp"
                    pause 0.05
                    "8a29.webp"
                    pause 0.05
                    "8a30.webp"
                    pause 0.05
                    repeat
                a "\" Mmmm...\""
                p "\" Ohh...\""
                p "\" That's...\""
                a "\" Mmmm...\""
                $ renpy.pause ()
                show 7newalex235
                with dissolve
                a "\" Been studying.\""
                p "\" Where?\""
                a "\" There are videos.\""
                scene alexblow2 animated with fade:
                    "8a1.webp"
                    pause 0.03
                    "8a2.webp"
                    pause 0.03
                    "8a3.webp"
                    pause 0.03
                    "8a4.webp"
                    pause 0.03
                    "8a5.webp"
                    pause 0.03
                    "8a6.webp"
                    pause 0.03
                    "8a7.webp"
                    pause 0.03
                    "8a8.webp"
                    pause 0.03
                    "8a9.webp"
                    pause 0.03
                    "8a10.webp"
                    pause 0.03
                    "8a11.webp"
                    pause 0.03
                    "8a12.webp"
                    pause 0.03
                    "8a13.webp"
                    pause 0.03
                    "8a14.webp"
                    pause 0.03
                    "8a15.webp"
                    pause 0.03
                    "8a16.webp"
                    pause 0.03
                    "8a17.webp"
                    pause 0.03
                    "8a18.webp"
                    pause 0.03
                    "8a19.webp"
                    pause 0.03
                    "8a20.webp"
                    pause 0.03
                    "8a21.webp"
                    pause 0.03
                    "8a22.webp"
                    pause 0.03
                    "8a23.webp"
                    pause 0.03
                    "8a24.webp"
                    pause 0.03
                    "8a25.webp"
                    pause 0.03
                    "8a26.webp"
                    pause 0.03
                    "8a27.webp"
                    pause 0.03
                    "8a28.webp"
                    pause 0.03
                    "8a29.webp"
                    pause 0.03
                    "8a30.webp"
                    pause 0.03
                    repeat
                " She gets back at it."
                " This time more forcefully."
                a "\" Mmmm...\""
                p "\" Ohh...\""
                a "\" Mmmm...\""
                p "\" I'm not gonna last...\""
                a "\" Mmmm...\""
                p "\" I'm about to...\""
                $ renpy.pause ()
                show 7newalex236
                with dissolve
                " She pulls your dick out, as you cum all over your stomach."
                a "\" There you go.\""
                a "\" He he he...\""
                show 7newalex237
                with dissolve
                a "\" You think you'll last with both of us?\""
                a "\" Especially once we get competitive?\""
                p "\" On who gives a better blowjob?\""
                a "\" Well?\""
                p "\" That sounds like one of those good problems.\""
                a "\" He he...\""
                p "\" You're sloppier than her though.\""
                a "\" Sloppier?\""
                p "\" She swallows.\""
                a "\" I see.\""
                hide 7newalex237
                show 7newalex238
                with dissolve
                " She goes back down and starts licking the cum off your stomach."
                a "\" *Slurp* *Slurp* *Slurp*\""
                hide 7newalex238
                show 7newalex239
                with dissolve
                p "\" He he he...\""
                a "\" What?\""
                p "\" It tickles.\""
                hide 7newalex239
                show 7newalex240
                with dissolve
                a "\" Really?\""
                a "\" You're going to complain about that while I'm eating your cum?\""
                p "\" Well, it does.\""
                a "\" *Sigh*\""
                hide 7newalex240
                show 7newalex238
                with dissolve
                " She finishes cleaning you up."
                hide 7newalex240
                show 7newalex229
                with dissolve
                " Then gives you another kiss."
                a "\" Good night, puppy.\""
                p "\" Good night.\""
                hide 7newalex229
                show 7newalex241
                with dissolve
                a "\" See you tomorrow.\""
                $ renpy.end_replay()
                " If you're going to ask her for help, this is the time."
                " Do you tell her about Emma?"
                call screen screen42

label ep7rob:
                scene 7newalex253
                with dissolve
                $ ep7robbery = True
                " You decide against it, and just go to sleep."
                show blackscreen
                with dissolve
                "..."
                "... ..."
                "... ... ..."
                hide blackscreen
                show 7newalex254
                with dissolve
                " Next morning goes as usual."
                hide 7newalex254
                show 7newalex256
                with dissolve
                " Alex checks on Boris again."
                " And he claims he's feeling better."
                hide 7newalex256
                show 7newalex91
                with dissolve
                " But the Emma issue still isn't resolved."
                hide 7newalex91
                show 7newalex92
                with dissolve
                p "\" Well...\""
                p "\" Poker game it is.\""
                p "\" James! I need to talk to you.\""
                hide 7newalex92
                show 7newalex269
                with dissolve
                ja "\" Boss?\""
                p "\" Can you handle a gun?\""
                ja "\" As well as anyone.\""
                p "\" And are you comfortable with that?\""
                hide 7newalex269
                show 7newalex270
                with dissolve
                ja "\" Boss...\""
                ja "\" Nevermind what old man Mark says.\""
                ja "\" I'm comfortable with anything that pays.\""
                p "\" Good.\""
                p "\" You're about to earn your keep around here.\""
                jump ep8

label ep7alex:
                scene 7newalex241
                with dissolve
                $ ep7helpfromalex = True
                p "\" Alex!\""
                show 7newalex242
                with dissolve
                a "\" Yes?\""
                p "\" I need to talk to you.\""
                a "\" Well?\""
                p "\" Sit down.\""
                a "\" That bad?\""
                p "\" Just sit down.\""
                hide 7newalex242
                show 7newalex243
                with dissolve
                a "\" What is it?\""
                p "\" Well, where do I start.\""
                hide 7newalex243
                show 7newalex244
                with dissolve
                " You tell her the story about Emma, and what she's having you do."
                hide 7newalex244
                show 7newalex245
                with dissolve
                " And you watch as her face turns to horror."
                a "\" [player_name]...\""
                a "\" This is...\""
                a "\" This is bad on so many levels.\""
                hide 7newalex245
                show 7newalex246
                with dissolve
                " She starts pacing up and down the room."
                a "\" Fuck.\""
                p "\" Like I said.\""
                p "\" I have a way to do it.\""
                p "\" That poker game.\""
                hide 7newalex246
                show 7newalex247
                with dissolve
                a "\" Are you kidding me?\""
                a "\" They already have you in a corner.\""
                a "\" You propose to give them more ammunition?\""
                hide 7newalex247
                show 7newalex248
                with dissolve
                a "\" No, we need to find another way.\""
                a "\" Let me think.\""
                p "\" You do believe me though?\""
                hide 7newalex248
                show 7newalex247
                with dissolve
                a "\" Of course I believe you, puppy.\""
                a "\" That's not the issue.\""
                a "\" The issue is how do we resolve this.\""
                hide 7newalex247
                show 7newalex249
                with dissolve
                a "\" Hmmm...\""
                p "\" What?\""
                hide 7newalex249
                show 7newalex250
                with dissolve
                a "\" First thing is we need to get that money.\""
                a "\" Then find some kind of leverage on that bitch cop.\""
                p "\" The poker game...\""
                a "\" Stop mentioning the game.\""
                a "\" That's not going to happen.\""
                hide 7newalex250
                show 7newalex251
                with dissolve
                a "\" Don't worry.\""
                a "\" Get to sleep.\""
                a "\" I'll find a way to take care of this.\""
                p "\" How?\""
                a "\" I'll think of something.\""
                a "\" Now go to sleep.\""
                a "\" No use staying up.\""
                hide 7newalex251
                show 7newalex252
                with dissolve
                a "\" And one more thing.\""
                a "\" Don't mention this to Dad.\""
                a "\" Not! One! Word!\""
                p "\" I understand.\""
                a "\" Good.\""
                hide 7newalex252
                show 7newalex254
                with dissolve
                " Next morning goes as usual."
                hide 7newalex254
                show 7newalex255
                with dissolve
                a "\" I have an idea.\""
                p "\" What?\""
                a "\" Come with me.\""
                hide 7newalex255
                show 7newalex256
                with dissolve
                a "\" Morning, Dad.\""
                b "\" Sweetheart.\""
                b "\" Going to school?\""
                a "\" Yeah.\""
                hide 7newalex256
                show 7newalex257
                with dissolve
                a "\" Remember, Mom left me some jewels?\""
                b "\" Of course.\""
                a "\" Where are they?\""
                b "\" In a safe deposit box.\""
                b "\" Why?\""
                a "\" I was thinking I might want to wear some.\""
                a "\" They are mine, right?\""
                b "\" Yes.\""
                a "\" Well, if you give me the key I could drop by the bank today.\""
                b "\" In the nightstand.\""
                a "\" Thanks.\""
                hide 7newalex257
                show 7newalex258
                with dissolve
                a "\" You need anything before I leave.\""
                b "\" I'm fine, darling.\""
                a "\" I'll call you this afternoon.\""
                b "\" Alright.\""
                hide 7newalex258
                show back1
                with dissolve
                show 7newalex259
                with dissolve
                a "\" We're dropping by the bank today.\""
                i "\" Why?\""
                a "\" I have some business.\""
                p "\" That's not necessary.\""
                hide 7newalex259
                show 7newalex260
                with dissolve
                a "\" We're not arguing about this.\""
                a "\" It's the best way.\""
                a "\" It will cover the immidiate need, and give us time to work on a different angle to solve the underlying issue.\""
                hide 7newalex260
                show 7newalex261
                with dissolve
                " You stop at the bank."
                hide 7newalex261
                show 7newalex262
                with dissolve
                " After a few minutes conversation with one of the tellers, Alex heads to a back room."
                hide 7newalex262
                show 7newalex264
                with dissolve
                " And comes back out with a small bag that she hands to you."
                a "\" This should cover it.\""
                p "\" Alex.\""
                hide 7newalex264
                show 7newalex265
                with dissolve
                a "\" Don't worry about it.\""
                a "\" If it's between you and some jewels...\""
                a "\" Let's go.\""
                hide 7newalex265
                show 7newalex91
                with dissolve
                " You drop off the girls and go the the office."
                " You feel a little uneasy about what happened."
                hide 7newalex91
                show 7newalex268
                with dissolve
                " But at least now you have the means to get to Marcello."
                jump ep8
