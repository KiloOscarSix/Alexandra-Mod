label ep2:
                scene blackscreen
                with dissolve
                default izzypoints = 0
                default alexpoints = 0
                default alicemission2goodending = False
                default alicehug1 = False
                default dannyaskdate = False
                "..."
                "... ..."
                a "\" Hmmm...\""
                a "\" Disappointing. I don't see it.\""
                i "\" Maybe he doesn't get them.\""
                show 2newalex01
                with dissolve
                " You wake to find the girls looming over you."
                p "\" What the???\""
                i "\" You startled him.\""
                a "\" No, you did.\""
                hide 2newalex01
                show 2newalex1
                with dissolve
                a "\" So, where is it?\" she asks you."
                p "\" Where's what?\""
                a "\" Your morning erection.\""
                p "\" What?\""
                a "\" Come on. There's 100 bucks on the line.\""
                i "\" Told you only kids get those.\""
                a "\" They all get it.\""
                hide 2newalex1
                show 2newalex2
                with dissolve
                i "\" Either way, you owe me.\""
                a "\" Fine, fine...\""
                i "\" Now stop embarrassing him.\""
                a "\" Ah, come on. He's not embarrassed with us.\""
                hide 2newalex2
                show 2newalex3
                with dissolve
                a "\" He knows he's my boy.\" She says, caressing your hair."
                hide 2newalex3
                show 2newalex7
                with dissolve
                a "\" It doesn't upset you, does it?\""
                a "\" The teasing?\""
                call screen screen3

label bothered:
                scene 2newalex7
                with dissolve
                p "\" Actually, it kind of does.\""
                show 2newalex9
                with dissolve
                a "\" Oh, ok.\""
                a "\" My apologies then.\""
                i "\" See? I told you.\""
                hide 2newalex9
                show 2newalex10
                with dissolve
                a "\" Again. Sorry.\""
                a "\" Can you drive us to school?\""
                p "\" Of course.\""
                jump ep2bigcont1


label notbothered:
                scene 2newalex7
                with dissolve
                $ alexpoints += 1
                p "\" Upset? No.\""
                p "\" More sad really. That you'd stoop to these tactics just to get a look at my penis.\""
                a "\" When all I had to do was ask?\""
                p "\" Not ask, but pay.\""
                show 2newalex11
                with dissolve
                a "\" What are you? A male whore?\""
                p "\" Give me five bucks, and find out.\""
                i "\" Hehehe...\""
                hide 2newalex11
                show 2newalex4
                with dissolve
                a "\" Ok, ok, I get it.\""
                a "\" Can you drive us to school?\""
                p "\" Of course.\""
                jump ep2bigcont1

label ep2bigcont1:
                scene 2newalex5
                with dissolve
                " The girls change and are ready to go."
                i "\" Just one minute.\""
                show 2newalex6
                with dissolve
                i "\" I have to go to school Mom.\""
                i "\" Are you going to be ok, 'til Martha gets here?\""
                hide 2newalex6
                show 2newalex12
                with dissolve
                p "\" Martha?\""
                a "\" Nurse.\""
                p "\" Oh, I see.\""
                hide 2newalex12
                show 2newalex6
                with dissolve
                ag "\" Huh?\""
                ag "\" I'm fine dear.\""
                i "\" Alright. I have to go now.\""
                hide 2newalex6
                show back
                with dissolve
                show 1newalex186
                with dissolve
                " You drive the girls to school."
                hide 1newalex186
                show 2newalex8
                with dissolve
                " Before she leaves, Alexandra asks you..."
                a "\" How is your afternoon?\""
                p "\" What do you need me to do?\""
                a "\" After you pick us back up, I'd like to take you to meet someone.\""
                p "\" I can do that. Who are we meeting?\""
                a "\" My Uncle.\""
                p "\" I didn't know you had an Uncle?\""
                hide 2newalex8
                show 2newalex13
                with dissolve
                a "\" Well, he and Dad are not on the best of terms.\""
                a "\" We don't really talk about it.\""
                hide 2newalex13
                show 2newalex8
                with dissolve
                a "\" We'll need his help.\""
                p "\" Not a problem.\""
                hide 2newalex8
                show 2newalex20
                with dissolve
                a "\" See you then.\""
                hide 2newalex20
                show easycoll3
                with dissolve
                " You manage to do a few collections that day."
                hide easycoll3
                show 2newalex14
                with dissolve
                " But soon it was time to go pick up the girls."
                hide 2newalex14
                show 2newalex15
                with dissolve
                i "\" Are we spending tonight at my place?\""
                i "\" I'll make my famous jambalaya.\""
                a "\" Can't tonight babe.\""
                hide 2newalex15
                show 2newalex16
                with dissolve
                a "\" Me and [player_name] have something to do.\""
                i "\" Hmm... That's disappointing.\""
                i "\" Make me feel better about it.\""
                a "\" Feel better?\""
                i "\" For you not spending time with me.\""
                hide 2newalex16
                show 2newalex17
                with dissolve
                a "\" There you go.\""
                a "\" Better?\""
                i "\" I think I'll need a little more.\""
                a "\" A little more?\""
                i "\" Aha.\""
                hide 2newalex17
                show 2newalex18
                with dissolve
                " The girls passionately kiss."
                a "\" What about now?\""
                i "\" Better.\""
                hide 2newalex18
                show 2newalex19
                with dissolve
                i "\" You can go do your thing.\""
                i "\" Alex?\""
                a "\" Yeah?\""
                i "\" Je t'aime.\""
                a "\" Je t'aime aussi.\""
                a "\" [player_name] is looking at us in the mirror you know.\""
                hide 2newalex19
                show 2newalex21
                with dissolve
                i "\" Do you feel left out?\""
                p "\" Ha! A little, maybe.\""
                i "\" I know how that feels.\""
                hide 2newalex21
                show 2newalex22
                with dissolve
                " She leans forward and gives you a kiss on the cheek."
                i "\" Better?\""
                call screen screen4

label izzycheekkissyes:
                scene back
                with dissolve
                show 2newalex22
                with dissolve
                p "\" Yes, actually.\""
                hide 2newalex22
                show 2newalex25
                with dissolve
                i "\" See you tomorrow?\""
                a "\" Yes.\""
                a "\" We have to go now babe.\""
                i "\" Later.\""
                hide 2newalex25
                show 2newalex8
                with dissolve
                a "\" Let's go see my uncle.\""
                p "\" Address?\""
                a "\" I'll show you the way.\""
                jump ep2bigcont2

label izzyalittlemorekiss:
                scene back
                with dissolve
                show 2newalex22
                with dissolve
                $ izzypoints += 1
                p "\" Actually...\""
                p "\" I still feel a little left out.\""
                hide 2newalex22
                show 2newalex23
                with dissolve
                " She turns your head and kisses you on the lips."
                a "\" Hey!\""
                hide 2newalex23
                show 2newalex24
                with dissolve
                a "\" What the hell?\""
                i "\" What?\""
                hide 2newalex24
                show 2newalex25
                with dissolve
                i "\" Jealous?\""
                a "\" Well...\""
                i "\" Of whom?\""
                a "\" Both.\""
                i "\" Good.\""
                i "\" See you tomorrow.\""
                hide 2newalex25
                show 2newalex26
                with dissolve
                " Izzy heads upstairs."
                p "\" He...he...he....\""
                a "\" What?\""
                p "\" You said both.\""
                a "\" So?\""
                p "\" I could come back there, and take care of at least one half of that jealousy.\""
                hide 2newalex26
                show 2newalex13
                with dissolve
                a "\" Just drive, Casanova.\""
                p "\" If you say so.\""
                p "\" Address?\""
                a "\" I'll show you the way.\""
                jump ep2bigcont2

label ep2bigcont2:
                scene 2newalex27
                with dissolve
                " It took you 20 minutes, until you arrive in front of an apartment building."
                a "\" We're here.\""
                show 2newalex28
                with dissolve
                a "\" Please be nice to my Uncle.\""
                p "\" Will he help us?\""
                a "\" I don't know.\""
                a "\" But I'm his favorite Niece.\""
                a "\" That also helps when I'm his only one.\""
                hide 2newalex28
                show 2newalex29
                with dissolve
                " You go upstairs."
                van "\" Alex!\""
                van "\" How are you my love?\""
                hide 2newalex29
                show 2newalex30
                with dissolve
                van "\" Came to finally see your Uncle?\""
                a "\" I might have come sooner, if I wasn't afraid to run into one of your... Ladies?\""
                van "\" You must allow me some vices darling.\""
                van "\" Especially since I quit smoking.\""
                a "\" But actually, I'm here because I need your help.\""
                hide 2newalex30
                show 2newalex31
                with dissolve
                van "\" My help?\""
                van "\" But why me and not your Father?\""
                van "\" Are you in trouble?\""
                a "\" No.\""
                van "\" What kind of trouble are you in?\""
                hide 2newalex31
                show 2newalex32
                with dissolve
                van "\" You! Pretty boy! Speak up!\""
                a "\" Uncle...\""
                van "\" What kind of trouble is she in?\""
                a "\" Uncle!\""
                hide 2newalex32
                show 2newalex31
                with dissolve
                a "\" I'm not in any kind of trouble.\""
                a "\" I swear.\""
                a "\" I just need your help with something.\""
                van "\" Alright.\""
                van "\" Let's talk in the kitchen.\""
                hide 2newalex31
                show 2newalex33
                with dissolve
                van "\" Alright, let's hear it.\""
                van "\" What do you need?\""
                hide 2newalex33
                show 2newalex34
                with dissolve
                a "\" You've worked with Dad for many years...\""
                van "\" Yes?\""
                a "\" What's the best way to get ahead in his type of business?\""
                van "\" Get ahead?\""
                a "\" Not for me. For my friend here.\""
                a "\" And his name is [player_name], not pretty boy.\""
                hide 2newalex34
                show 2newalex35
                with dissolve
                van "\" Him?\""
                van "\" What?\""
                a "\" He works for Dad. And I'd like for him to get ahead.\""
                van "\" Why?\""
                hide 2newalex35
                show 2newalex36
                with dissolve
                a "\" I'd just like to help him out.\""
                van "\" Why do you care?\""
                van "\" What's he to you?\""
                van "\" Ahhh... You don't mean...\""
                hide 2newalex36
                show 2newalex37
                with dissolve
                van "\" Are you her man?\""
                hide 2newalex37
                show 2newalex38
                with dissolve
                a "\" Uncle!\""
                hide 2newalex38
                show 2newalex37
                with dissolve
                van "\" He...he...he....\""
                van "\" Good man!\""
                van "\" I was despairing of ever getting a little Nephew from this one.\""
                van "\" Started to think it wasn't going to happen.\""
                hide 2newalex37
                show 2newalex38
                with dissolve
                a "\" Uncle!!!\""
                hide 2newalex38
                show 2newalex37
                with dissolve
                van "\" Finally weaned her off the muff, eh?\""
                a "\" Damn it!\""
                van "\" Good boy!\""
                van "\" Always thought it was just a phase.\""
                a "\" Jesus...\""
                van "\" Boris won't be happy though.\""
                hide 2newalex37
                show 2newalex38
                with dissolve
                a "\" Are you going to help us or not?\""
                hide 2newalex38
                show 2newalex39
                with dissolve
                van "\" That was a bit shrill.\""
                van "\" Hormonal?\""
                van "\" Pregnant already?\""
                a "\" Uncle!\""
                hide 2newalex39
                show 2newalex40
                with dissolve
                van "\" Alright, alright...\""
                van "\" Well it's very simple.\""
                van "\" You need to find new revenue streams.\""
                p "\" New revenue streams.\""
                hide 2newalex40
                show 2newalex41
                with dissolve
                van "\" Why do you two think people borrow money from people like Boris.\""
                van "\" Well, it's because they can't go to a bank.\""
                a "\" So?\""
                van "\" And why do people pay taxes to Boris? Because they can't go to the cops.\""
                hide 2newalex41
                show 2newalex42
                with dissolve
                van "\" It's very simple.\""
                van "\" Do you know a doctor that sells feel good pills on the side?\""
                van "\" A bookshop with a Faro table in the back?\""
                van "\" Tell Boris about them.\""
                a "\" Extortion?\""
                hide 2newalex42
                show 2newalex41
                with dissolve
                van "\" Assistance.\""
                van "\" They need us.\""
                van "\" What if something happens? They can't go to the cops can they?\""
                van "\" But they can come to us.\""
                p "\" And if something doesn't happen?\""
                hide 2newalex41
                show 2newalex42
                with dissolve
                van "\" Then you make sure that it does.\""
                p "\" I see.\""
                van "\" Find someone like that, then come back to me.\""
                a "\" So find someone that does something illegal, and...\""
                hide 2newalex42
                show 2newalex41
                with dissolve
                van "\" Exactly.\""
                van "\" But that's [player_name]'s problem.\""
                hide 2newalex41
                show 2newalex43
                with dissolve
                van "\" You? You get to work on that little Nephew of mine.\""
                a "\" Unbelievable.\""
                hide 2newalex43
                show 2newalex44
                with dissolve
                van "\" You find a good target, and come back to me.\""
                van "\" I'll tell you whether you should take it to Boris.\""
                p "\" Understood.\""
                hide 2newalex44
                show back1
                with dissolve
                show 2newalex45
                with dissolve
                " You leave Vanya's place and drive Alex home."
                a "\" Extortion.\""
                p "\" Guess so.\""
                a "\" I'm not sure how I feel about that.\""
                p "\" Think about it this way. They're already doing something illegal.\""
                p "\" It's not like these people are saints.\""
                hide 2newalex45
                show 2newalex300
                with dissolve
                a "\" You're not bothered by this?\""
                p "\" Not really.\""
                hide 2newalex300
                show 2newalex45
                with dissolve
                a "\" I guess I'd better get used to it.\""
                "... ..."
                a "\" And my Uncle... Jesus!\""
                p "\" I know.\""
                a "\" Give him a Nephew...\""
                p "\" I know.\""
                p "\" It's like all the universe conspires that you belong in my bed.\""
                hide 2newalex45
                show 2newalex301
                with dissolve
                a "\" It's a universal conspiracy, eh?\""
                p "\" Seems so.\""
                hide 2newalex301
                show 2newalex46
                with dissolve
                a "\" And are you part of this conspiracy.\""
                p "\" Merely the beneficiary of it.\""
                a "\" Don't count your chickens, loverboy.\""
                a "\" Why don't you take me home?\""
                p "\" My home?\""
                a "\" My Dad's, jackass.\""
                p "\" Yes, ma'am.\""
                hide 2newalex46
                show 2newalex47
                with dissolve
                a "\" See you tomorrow?\""
                p "\" I'll be driving you, so yes.\""
                a "\" Bye.\""
                hide 2newalex47
                show 2newalex48
                with dissolve
                " Before heading home that day, you decide to pay Lenny a visit."
                p "\" Lenny!\""
                hide 2newalex48
                show 2newalex49
                with dissolve
                lenny "\" Hey!\""
                lenny "\" What can I do for you?\""
                p "\" I need you to find something for me.\""
                lenny "\" What?\""
                p "\" A dirty businessman.\""
                hide 2newalex49
                show 2newalex50
                with dissolve
                lenny "\" In this city? Throw a stone.\""
                lenny "\" Anyone in particular?\""
                p "\" I need to find someone my boss can extort.\""
                hide 2newalex50
                show 2newalex49
                with dissolve
                lenny "\" I see. Not a problem.\""
                p "\" Really?\""
                lenny "\" Like I said... In this city....\""
                lenny "\" I'll have something for you tomorrow.\""
                p "\" Alright.\""
                p "\" See you then.\""
                hide 2newalex49
                show p122
                with dissolve
                " You head home and get to sleep."
                show blackscreen
                with dissolve
                "... ..."
                "... ... ..."
                if alicemission1goodending == True:
                    jump day2withalice
                else:
                    jump da2woalice

label da2woalice:
                scene 1newalex146
                with dissolve
                " You wake up to a knocking on your door."
                p "\" Yes?\""
                "*Knock*...*Knock*...*Knock*..."
                p "\" I'm coming.\""
                show 2newalex51
                with dissolve
                p "\" Lenny. Don't tell me you've already found one.\""
                lenny "\" Told you.\""
                lenny "\" And it's a woman.\""
                p "\" Alright. Let's go.\""
                hide 2newalex51
                show back
                with dissolve
                show 2newalex52
                with dissolve
                p "\" Where are we going?\""
                lenny "\" Modeling agency. He he...\""
                p "\" Modeling agency?\""
                lenny "\" And for a little extra...\""
                p "\" You're kidding.\""
                lenny "\" Here we are.\""
                show 2newalex53
                with disolve
                lenny "\" Second floor.\""
                show back
                with dissolve
                show 2newalex54
                with dissolve
                lenny "\" Don't get me wrong. It's a legitimate business.\""
                lenny "\" But if you're a model, and you want to get ahead...\""
                p "\" I see.\""
                p "\" Any proof?\""
                hide 2newalex54
                show 2newalex55
                with dissolve
                lenny "\" Proof?\""
                lenny "\" Like what? Pictures? Video? Of course not.\""
                p "\" But you're certain.\""
                lenny "\" Oh, yes.\""
                p "\" Alright. Thanks.\""
                p "\" Where do I drop you off?\""
                p "\" I have to go drive Alex to school.\""
                lenny "\" Anywhere is fine.\""
                hide 2newalex55
                show 2newalex98
                with dissolve
                " You go to pick up the girls."
                p "\" Good news.\""
                p "\" I found what we were looking for, I think.\""
                a "\" So soon?\""
                p "\" As a friend of mine said. In this city, throw a stone.\""
                a "\" We should go see my Uncle after school.\""
                p "\" I can't today. Have a lot of collections.\""
                a "\" I guess we'll have to ask someone else to drive us?\""
                p "\" I can...\""
                a "\" It's not a problem.\""
                a "\" You focus on what you need to do.\""
                a "\" Tomorrow?\""
                p "\" Yes.\""
                hide 2newalex98
                show veryhardcoll3
                with dissolve
                " You spend the rest of the day doing collections, and thinking about tomorrow's meeting."
                jump ep2bigcont3

label day2withalice:
                scene 1newalex146
                with dissolve
                " You wake up to a knocking on your door."
                p "\" Yes?\""
                " *Knock*...*Knock*...*Knock*..."
                p "\" I'm coming.\""
                show 2newalex56
                with dissolve
                p "\" Alice?\""
                ali "\" Heard from Lenny you needed a crooked business owner.\""
                p "\" Yes.\""
                ali "\" Found one.\""
                p "\" So soon?\""
                hide 2newalex56
                show 2newalex57
                with dissolve
                ali "\" In this city, throw a stone and you'll hit one.\""
                p "\" That's what Lenny said.\""
                p "\" Alright. Let's go.\""
                hide 2newalex57
                show 2newalex53
                with dissolve
                " She takes you in front of a building in the center of town."
                ali "\" Second floor.\""
                hide 2newalex53
                show back
                with dissolve
                show 2newalex58
                with dissolve
                ali "\" Modeling agency.\""
                p "\" Modeling agency?\""
                ali "\" And cathouse.\""
                p "\" As in prostitutes?\""
                ali "\" Yeah.\""
                hide 2newalex58
                show 2newalex60
                with dissolve
                ali "\" Don't get me wrong, they do real modeling.\""
                ali "\" But for a little extra.\""
                p "\" I see.\""
                hide 2newalex60
                show 2newalex59
                with dissolve
                ali "\" We did good, right?\""
                p "\" Yeah.\""
                ali "\" You don't seem very happy.\""
                p "\" Any proof of what they're doing?\""
                ali "\" Pffft... You need that?\""
                p "\" It would help to be sure.\""
                ali "\" That's easy.\""
                hide 2newalex59
                show 2newalex61
                with dissolve
                ali "\" I can verify things for you.\""
                ali "\" Take me to the nearest clothing shop.\""
                hide 2newalex61
                show 2newalex62
                with dissolve
                " You find a shop nearby."
                ali "\" Talk to the shopkeeper. And keep her talking.\""
                ali "\" When I leave, you follow.\""
                p "\" Are you?...\""
                ali "\" A little caper, ha ha...\""
                hide 2newalex62
                show 2newalex63
                with dissolve
                shop "\" Can I help you?\""
                p "\" Ahhh... Yes...\""
                p "\" I'm looking for a piece of clothing...\""
                shop "\" I figured that out.\""
                shop "\" Anything more specific?\""
                p "\" Yeah... I'm looking for a bra?\""
                hide 2newalex63
                show 2newalex64
                with dissolve
                shop "\" Was that a question?\""
                shop "\" Is it for a wife, girlfriend? Or maybe a... Friend?\""
                p "\" Friend?\""
                shop "\" Are you looking for a specialty item?. We don't judge.\""
                p "\" What? I mean... No...\""
                p "\" It's for... A girlfriend.\""
                hide 2newalex64
                show 2newalex65
                with dissolve
                shop "\" And what size is... She?\""
                p "\" I don't know. About...\""
                hide 2newalex65
                show 2newalex66
                with dissolve
                " You see Alice coming out the back, and winking at you."
                p "\" I have to go.\""
                shop "\" Whatever you say.\""
                hide 2newalex66
                show back
                with dissolve
                show 2newalex67
                with dissolve
                ali "\" Ha ha ha...\""
                p "\" Damn it, girl.\""
                p "\" We could've just bought it, whatever it is.\""
                ali "\" I don't pay.\""
                ali "\" And it's a dress.\""
                ali "\" You said you wanted to be sure.\""
                hide 2newalex67
                show 2newalex61
                with dissolve
                p "\" What do you want to do?\""
                ali "\" Apply for a modeling job.\""
                ali "\" See what they say.\""
                p "\" Are you sure?\""
                hide 2newalex61
                show 2newalex68
                with dissolve
                ali "\" Why not?\""
                ali "\" It will be fun.\""
                p "\" You can change at my place.\""
                hide 2newalex68
                show 2newalex69
                with dissolve
                ali "\" Bathroom?\""
                p "\" Behind me.\""
                ali "\" I'll be right back.\""
                hide 2newalex69
                show 2newalex70
                with dissolve
                " You take a seat as you wait for Alice to come out."
                ali "\" [player_name]?\""
                hide 2newalex70
                show 2newalex71
                with dissolve
                p "\" Yes?\""
                ali "\" You won't tell my Brother that I did this, right?\""
                p "\" What? No. Why?\""
                hide 2newalex71
                show 2newalex72
                with dissolve
                ali "\" He takes a dim view of what I do sometimes.\""
                p "\" In what way?\""
                hide 2newalex72
                show 2newalex71
                with dissolve
                ali "\" Well, he sometimes still thinks I'm a kid.\""
                hide 2newalex71
                show 2newalex73
                with dissolve
                ali "\" So, if we can keep this between us?\""
                p "\" Sure.\""
                ali "\" Ok. I'll be right back.\""
                hide 2newalex73
                show 2newalex74
                with dissolve
                " She comes back out a few minutes later."
                ali "\" What do you think?\""
                p "\" Pretty.\""
                ali "\" Model pretty?\""
                hide 2newalex74
                show 2newalex75
                with dissolve
                ali "\" He he he...\""
                ali "\" I should strike a pose.\""
                p "\" I have a question.\""
                hide 2newalex75
                show 2newalex76
                with dissolve
                ali "\" Yes?\""
                p "\" Why are you doing this?\""
                hide 2newalex76
                show 2newalex77
                with dissolve
                ali "\" You helped me and and my Brother.\""
                ali "\" It's the least I can do.\""
                hide 2newalex77
                show 2newalex78
                with dissolve
                " She gives you a quick hug."
                hide 2newalex78
                show 2newalex79
                with dissolve
                ali "\" Wow. That would of been so much better if you weren't stiff as a board.\""
                " Do you hug her back?"
                call screen screen5

label alicehugback:
                scene 2newalex80
                with dissolve
                $ alicehug1 = True
                " You hug her back."
                ali "\" Oh...\""
                ali "\" Mmmm...\""
                ali "\" This is nice.\""
                jump ep2alicecont1

label alicenohugback:
                scene 2newalex79
                with dissolve
                p "\" Not much of a hugger, I'm afraid.\""
                jump ep2alicecont1

label ep2alicecont1:
                scene 2newalex79
                with dissolve
                ali "\" Right. We should get going.\""
                show back
                with dissolve
                show 2newalex81
                with dissolve
                p "\" What are you going to do exactly?\""
                ali "\" I'll tell them I'm a model looking for work.\""
                p "\" And you think they'll just tell you to work as a prostitute?\""
                hide 2newalex81
                show 2newalex82
                with dissolve
                ali "\" I know how to wiggle out the truth. Trust me.\""
                p "\" Alright.\""
                p "\" Well, I'll be back in one hour or so. I have to drive Alexandra.\""
                ali "\" Alexandra?\""
                ali "\" Right. Your boss's Daughter. Guess you have to do that.\""
                ali "\" Come pick me up when you're done.\""
                p "\" Sure.\""
                hide 2newalex82
                show 2newalex98
                with dissolve
                " You go to pick up the girls."
                p "\" Good news.\""
                p "\" I found what we were looking for, I think.\""
                a "\" So soon?\""
                p "\" As a friend of mine said. In this city, throw a stone.\""
                a "\" We should go see my uncle after school.\""
                p "\" I can't today. Still have to make sure that I'm on the right trail.\""
                a "\" I guess we'll have to ask someone else to drive us?\""
                p "\" I can...\""
                a "\" It's not a problem.\""
                a "\" You focus on what you need to do.\""
                a "\" Tomorrow?\""
                p "\" Yes.\""
                hide 2newalex98
                show 2newalex83
                with dissolve
                " You return just in time to see Alice walk out."
                show back
                show 2newalex84
                with dissolve
                ali "\" Just in time.\""
                p "\" What did you find out.\""
                ali "\" Just like I said.\""
                hide 2newalex84
                show 2newalex85
                with dissolve
                ali "\" Did you ever doubt me?\""
                hide 2newalex85
                show 2newalex84
                with dissolve
                ali "\" Well, they said that they'll steer modeling jobs my way.\""
                ali "\" And that sometimes, some right guys will pay us to be his arm candy.\""
                ali "\" And what happens after that...\""
                p "\" Right.\""
                ali "\" It's up to us.\""
                hide 2newalex84
                show 2newalex85
                with dissolve
                ali "\" I did good, right?\""
                p "\" Very good.\""
                ali "\" He he...\""
                hide 2newalex85
                show 2newalex86
                with dissolve
                " You drive Alice back to your place so that she can change."
                ali "\" I'll change in just a minute.\""
                ali "\" To be honest. I'm not a dress girl.\""
                p "\" More comfortable in jeans?\""
                ali "\" Much.\""
                if alicehug1 == True:
                    jump ep2alicecont2
                else :
                    jump ep2alicecontend

label ep2alicecontend:
                scene 2newalex56
                with dissolve
                ali "\" Guess I'll see you around.\""
                p "\" Yeah.\""
                ali "\" Later.\""
                show veryhardcoll3
                with dissolve
                " You spend the rest of the day doing collections, and thinking about tomorrow's meeting."
                jump ep2bigcont3

label ep2alicecont2:
                scene 2newalex86
                with dissolve
                p "\" You do look good in a dress though.\""
                ali "\" Really? That's very sweet.\""
                " Do you invite her to stay a little longer?"
                call screen screen6

label aliceday2nostay:
                scene 2newalex86
                with dissolve
                ali "\" I should go change now.\""
                show 2newalex56
                with dissolve
                ali "\" Guess I'll see you around.\""
                p "\" Yeah.\""
                ali "\" Later.\""
                show veryhardcoll3
                with dissolve
                " You spend the rest of the day doing collections, and thinking about tomorrow's meeting."
                jump ep2bigcont3

label aliceday2stay:
                scene 2newalex86
                with dissolve
                ali "\" I should go change now.\""
                p "\" You could stay a little longer if you want.\""
                ali "\" Are you inviting me?\""
                p "\" Yes. Have you eaten?\""
                ali "\" No. Lets see what you can come up with.\""
                ali "\" I'll go change. I'm really not a dress kinda girl.\""
                show 2newalex87
                with dissolve
                " While Alice is in the bathroom, you look for something to eat."
                " All you can find is some pasta."
                hide 2newalex87
                show 2newalex88
                with dissolve
                " When she comes out she's not in her jeans. She just took off the dress."
                ali "\" What did you find?\""
                p "\" Some pasta.\""
                ali "\" Let's cook it then.\""
                hide 2newalex88
                show 2newalex89
                with dissolve
                " You and Alice manage to cook it without burning down the building."
                hide 2newalex89
                show 2newalex90
                with dissolve
                ali "\" Supermarket pasta, huh?\""
                p "\" I guess.\""
                p "\" Didn't grow up with a silver spoon in my mouth.\""
                ali "\" Me and Lenny either.\""
                hide 2newalex90
                show 2newalex91
                with dissolve
                " After you watch a little TV, until quite late in the evening."
                hide 2newalex91
                show 2newalex92
                with dissolve
                ali "\" Why did you invite me to stay?\""
                p "\" What do you mean?\""
                ali "\" What are you doing?\""
                p "\" Watching TV with a friend.\""
                hide 2newalex92
                show 2newalex93
                with dissolve
                ali "\" Just a friend? Or just a friend, for now.\""
                call screen screen7


label aliceday2friend:
                scene 2newalex93
                with dissolve
                p "\" Just a friend.\""
                ali "\" I see.\""
                show 2newalex96
                with dissolve
                " She jumps up and runs for the bathroom."
                ali "\" I need to go.\""
                hide 2newalex96
                show 2newalex97
                with dissolve
                " She comes back out in a matter of seconds."
                ali "\" I'll see you around, I guess.\""
                p "\" Alice.\""
                ali "\" I have to go. Lenny will be worried.\""
                ali "\" Bye.\""
                jump ep2bigcont3

label aliceday2friendfornow:
                scene 2newalex93
                with dissolve

                p "\" A friend. For now.\""
                ali "\" What else could we be?\""
                p "\" I'm not sure yet.\""
                show 2newalex94
                with dissolve
                " She scrambles in your lap."
                ali "\" Neither am I.\""
                ali "\" Not yet.\""
                hide 2newalex94
                show 2newalex95
                with dissolve
                " She gives you a deep kiss."
                " Her small and agile tongue, darting inside your mouth."
                hide 2newalex95
                show 2newalex96
                with dissolve
                " She jumps up and runs for the bathroom."
                ali "\" I need to go.\""
                hide 2newalex96
                show 2newalex97
                with dissolve
                " She comes back out in a matter of seconds."
                ali "\" I'll see you around, I guess.\""
                p "\" Alice.\""
                ali "\" I have to go. Lenny will be worried.\""
                ali "\" Bye.\""
                jump ep2bigcont3

label ep2bigcont3:
                scene back1
                with dissolve
                show 2newalex98
                with dissolve
                " The next day, as you drive the girls home from school."
                i "\" Missed you yesterday puppy.\""
                p "\" Thank you darling.\""
                hide 2newalex98
                show 2newalex99
                with dissolve
                i "\" Didn't you miss him Alex?\""
                a "\" Izzy...\""
                i "\" Well?\""
                a "\" Fine, I missed him too.\""
                p "\" The universe is conspiring again.\""
                hide 2newalex99
                show 2newalex100
                with dissolve
                a "\" Speaking of conspiracies...\""
                p "\" It's taken care of.\""
                a "\" And we can go see my Uncle?\""
                p "\" Yes.\""
                hide 2newalex100
                show 2newalex101
                with dissolve
                i "\" You're not staying at my place tonight?\""
                hide 2newalex101
                show 2newalex102
                with dissolve
                a "\" Of course, I am.\""
                a "\" Just have to take care of something first.\""
                a "\" We'll be no more than an hour.\""
                hide 2newalex102
                show 2newalex103
                with dissolve
                i "\" You're coming too.\""
                i "\" I've barely seen you the last couple of days.\""
                p "\" Wouldn't miss it.\""
                hide 2newalex103
                show 2newalex104
                with dissolve
                " After you drop off Izzy, Alex asks you."
                a "\" What kind of place is it?\""
                p "\" A brothel.\""
                a "\" Brothel?\""
                p "\" Masquerading as a modeling agency.\""
                a "\" Damn. Fuckers probably taste the merchandise first.\""
                p "\" It's run by a woman actually.\""
                p "\" And no one is forcing them.\""
                a "\" Uncle Vanya will be thrilled.\""
                a "\" Let's go.\""
                hide 2newalex104
                show 2newalex105
                with dissolve
                van "\" Cathouse huh?\""
                van "\" Perfect.\""
                van "\" Let's talk.\""
                hide 2newalex105
                show 2newalex106
                with dissolve
                van "\" What you want to do, is take this to Boris.\""
                van "\" Tell him you stumbled over it, and ask for his advice.\""
                hide 2newalex106
                show 2newalex107
                with dissolve
                a "\" But how are we to be sure that Dad will give it to him to run?\""
                hide 2newalex107
                show 2newalex36
                with dissolve
                van "\" He might not.\""
                van "\" But that's where you come in.\""
                a "\" I understand.\""
                hide 2newalex36
                show 2newalex37
                with dissolve
                van "\" And I assume I'm getting a discount?\""
                hide 2newalex37
                show 2newalex38
                with dissolve
                a "\" Sleazy old man.\""
                hide 2newalex38
                show 2newalex39
                with dissolve
                van "\" You know it darlin.\""
                a "\" We'll need your help to run it.\""
                a "\" We know nothing about this type of thing.\""
                van "\" Anything for you.\""
                hide 2newalex39
                show 2newalex40
                with dissolve
                van "\" Hey! Employee discount.\""
                p "\" Ha ha ha...\""
                a "\" Both of you, now.\""
                hide 2newalex40
                show 2newalex43
                with dissolve
                a "\" Thank you, Uncle.\""
                a "\" Well, talk to you soon.\""
                van "\" Of course, darling.\""
                hide 2newalex43
                show back1
                with dissolve
                show 2newalex109
                with dissolve
                p "\" It really bothers you doesn't it.\""
                p "\" That it's prostitution.\""
                a "\" It doesn't bother you?\""
                p "\" No.\""
                p "\" If it was forced, you would be right. But since it isn't...\""
                p "\" Listen, if you don't want to do it. We won't do it.\""
                hide 2newalex109
                show 2newalex110
                with dissolve
                a "\" You'd give it up?\""
                p "\" If you asked me, sure.\""
                hide 2newalex110
                show 2newalex111
                with dissolve
                " She reaches out and caresses your face."
                hide 2newalex111
                show 2newalex112
                with dissolve
                a "\" Puppy...\""
                hide 2newalex112
                show 2newalex110
                with dissolve
                a "\" Maybe we'll run away together.\""
                p "\" Just say the word.\""
                a "\" The three of us.\""
                p "\" Sure.\""
                hide 2newalex110
                show 2newalex112
                with dissolve
                a "\" You'd take care of me and Izzy?\""
                p "\" Sure.\""
                hide 2newalex112
                show 2newalex109
                with dissolve
                a "\" You know what? I might just do that one day.\""
                hide 2newalex109
                show 2newalex113
                with dissolve
                " You drive to Izzy's place."
                i "\" Hey.\""
                i "\" Come in.\""
                hide 2newalex113
                show 2newalex114
                with dissolve
                " And you find her studying."
                hide 2newalex114
                show 2newalex115
                with dissolve
                a "\" Shit!\""
                i "\" Yeah.\""
                i "\" You forgot, didn't you.\""
                a "\" We have exams the next few days.\""
                hide 2newalex115
                show 2newalex116
                with dissolve
                i "\" We'll have to pull several all nighters.\""
                a "\" Shit!\""
                i "\" Yeah.\""
                hide 2newalex116
                show 2newalex117
                with dissolve
                a "\" We have to study.\""
                p "\" I gathered that.\""
                p "\" I should go do some collections.\""
                a "\" But you're coming back, right?\""
                p "\" Do you doubt it?\""
                hide 2newalex117
                show veryhardcoll1
                with dissolve
                " You go do a few collections."
                hide veryhardcoll1
                show 2newalex118
                with dissolve
                " But when you come back, the girls are still into their books."
                hide 2newalex118
                show 2newalex119
                with dissolve
                " And they continue late into the night, with little time for you."
                hide 2newalex119
                show 2newalex120
                with dissolve
                a "\" You're tired aren't you?\""
                a "\" Sorry we have to study.\""
                a "\" If you want to go home, it's ok.\""
                a "\" We'll be occupying the couch for most of the night.\""
                hide 2newalex120
                show 2newalex121
                with dissolve
                i "\" What?\""
                i "\" He can sleep in my bed.\""
                a "\" Are you sure?\""
                i "\" What are you talking about. 'Are you sure'?\""
                hide 2newalex121
                show 2newalex122
                with dissolve
                i "\" This way.\""
                hide 2newalex122
                show 2newalex123
                with dissolve
                p "\" Nice.\""
                i "\" Not as cozy as yours...\""
                p "\" That's code word for small.\""
                i "\" No it isn't.\""
                hide 2newalex123
                show 2newalex124
                with dissolve
                " She covers you in a blanket as you get into bed."
                i "\" I'll turn off the light for you.\""
                i "\" Good night.\""
                call screen screen8

label izzygoodnight:
                scene 2newalex124
                with dissolve
                p "\" Good night.\""
                show 2newalex127
                with dissolve
                " She turns off the lights as she leaves. And soon you're asleep."
                jump ep2bigcont4

label izzygoodnightkiss:
                scene 2newalex124
                with dissolve
                $ izzypoints += 1
                p "\" How about a good night kiss?\""
                show 2newalex125
                with dissolve
                i "\" Really?\""
                p "\" I find it hard to sleep without it.\""
                p "\" You wouldn't want me to have nightmares, would you.\""
                i "\" We can't have that.\""
                hide 2newalex125
                show 2newalex126
                with dissolve
                " She gently kisses you."
                hide 2newalex126
                show 2newalex125
                with dissolve
                i "\" Better?\""
                p "\" A little.\""
                hide 2newalex125
                show 2newalex126
                with dissolve
                " She kisses you again."
                hide 2newalex126
                show 2newalex125
                with dissolve
                i "\" Now I really have to go.\""
                i "\" Good night.\""
                hide 2newalex125
                show 2newalex127
                with dissolve
                " She turns off the lights as she leaves. And soon you're asleep."
                jump ep2bigcont4

label ep2bigcont4:
                scene blackscreen
                with dissolve
                "..."
                "... ..."
                show 2newalex128
                with dissolve
                " The sound of footsteps wake you up."
                " It's Alexandra."
                hide 2newalex128
                show 2newalex129
                with dissolve
                " She goes out on the balcony."
                hide 2newalex129
                show 2newalex130
                with dissolve
                " You get up and follow her."
                p "\" Alex.\""
                a "\" AIII!!!\""
                hide 2newalex130
                show 2newalex131
                with dissolve
                a "\" Jesus...\""
                a "\" You scared the shit out of me...\""
                p "\" Are you ok?\""
                a "\" Yeah.\""
                hide 2newalex131
                show 2newalex132
                with dissolve
                a "\" You should be sleeping.\""
                p "\" You woke me up.\""
                a "\" Sorry. Just needed a break.\""
                p "\" It's ok.\""
                hide 2newalex132
                show 2newalex133
                with dissolve
                a "\" I don't get you, [player_name].\""
                p "\" What's not to get?\""
                a "\" Why do you do everything I say?\""
                p "\" Why are you helping me with your Dad?\""
                a "\" I have my reasons.\""
                p "\" So do I.\""
                a "\" Yeah. You said. You recognize me.\""
                p "\" Dreamed of you. Several times now.\""
                a "\" What kind of dreams?\""
                hide 2newalex133
                show 2newalex134
                with dissolve
                " You pull her in your lap, as you sit down."
                " She doesn't resist, and comes willingly to you."
                p "\" It wasn't lascivious, if that's what you're asking.\""
                hide 2newalex134
                show 2newalex135
                with dissolve
                a "\" I'm with Izzy.\""
                p "\" I know.\""
                a "\" I've always been with her.\""
                p "\" I realize that.\""
                a "\" And I like to think of myself as loyal.\""
                p "\" I have no doubt.\""
                a "\" And this doesn't discourage you.\""
                p "\" I trust my dreams.\""
                hide 2newalex135
                show 2newalex136
                with dissolve
                a "\" That's actually pretty scary.\""
                p "\" Sorry about that. But it's true.\""
                hide 2newalex136
                show 2newalex137
                with dissolve
                a "\" What if I told you to leave, and never come back?\""
                p "\" You won't.\""
                a "\" But what if I did?\""
                p "\" I'd leave. But you won't.\""
                hide 2newalex137
                show 2newalex139
                with dissolve
                a "\" Ahhh...\""
                a "\" Guess there's no talking you out of it.\""
                p "\" Say it, then.\""
                hide 2newalex139
                show 2newalex137
                with dissolve
                p "\" Tell me to leave.\""
                a "\"... ...\""
                p "\" Exactly.\""
                p "\" I trust my dreams.\""
                a "\" What if I'm just taking advantage of you, have you thought of that?\""
                a "\" What if I'm just exploiting these... Feelings of yours?\""
                p "\" You are.\""
                p "\" But that's ok.\""
                hide 2newalex137
                show 2newalex139
                with dissolve
                a "\" Because he trusts his dreams...\""
                p "\" Exactly.\""
                hide 2newalex139
                show 2newalex142
                with dissolve
                " She leans in and gives you a chaste kiss on the lips."
                hide 2newalex142
                show 2newalex141
                with dissolve
                p "\" See?\""
                a "\" Again. Manipulation.\""
                a "\" Giving you false hopes.\""
                p "\" If you say so.\""
                hide 2newalex141
                show 2newalex139
                with dissolve
                a "\" I'm never going to win with you, am I?\""
                p "\" That would depend on your definition.\""
                a "\" I'm to tired to fight you right now.\""
                a "\" Maybe some other time.\""
                hide 2newalex139
                show 2newalex140
                with dissolve
                a "\" Are you going to see Dad tomorrow?\""
                p "\" I was thinking about Dima.\""
                hide 2newalex140
                show 2newalex138
                with dissolve
                a "\" That's probably better.\""
                a "\" Chain of command, and all that.\""
                a "\" Well, I have to get back to studying.\""
                hide 2newalex138
                show 2newalex142
                with dissolve
                " She leans in, and kisses you again."
                p "\" Manipulating me again?\""
                hide 2newalex142
                show 2newalex143
                with dissolve
                a "\" Yeah.\" She answers, giving you a wink."
                hide 2newalex143
                show 2newalex144
                with dissolve
                " She gets up and says..."
                a "\" You'd better get some sleep.\""
                a "\" You'll need your energy tomorrow.\""
                p "\" Yeah.\""
                hide 2newalex144
                show 2newalex127
                with dissolve
                " With Alex gone, you head back to bed."
                hide 2newalex127
                with dissolve
                show 2newalex145
                " And wake up one more time in the middle of the night, to find the girls sleeping beside you."
                hide 2newalex145
                show blackscreen
                with dissolve
                "... ..."
                "... ... ..."
                hide blackscreen
                show 2newalex146
                with dissolve
                " When you wake up the sun is up."
                hide 2newalex146
                show 2newalex147
                with dissolve
                " You turn to find Alex next to you."
                " The bedsheets had fallen off, and her nightshirt had ridden up."
                p "\" Alex?\""
                hide 2newalex147
                show 2newalex148
                with dissolve
                a "\" Hey... Morning.\""
                p "\" Where's Izzy.\""
                a "\" She always gets up before the crack of dawn.\""
                a "\" Checks in on her Mother.\""
                hide 2newalex148
                show 2newalex149
                with dissolve
                " Your eyes slide down her body, to her lifted nightshirt."
                hide 2newalex149
                show 2newalex150
                with dissolve
                a "\" Easy, there.\""
                p "\" What?\""
                a "\" Just because I gave you one kiss doesn't mean.\""
                hide 2newalex150
                show 2newalex151
                with dissolve
                a "\" Listen.\""
                a "\" I'm not a disloyal person.\""
                p "\" I know.\""
                hide 2newalex151
                show 2newalex152
                with dissolve
                a "\" Izzy wouldn't like this.\""
                p "\" Are you sure about that?\""
                a "\" Yeah.\""
                hide 2newalex152
                show 2newalex153
                with dissolve
                a "\" Why are you coming closer?\""
                a "\" Stop it.\""
                " But despite her words, her mouth opens up in expectation."
                hide 2newalex153
                show 2newalex154
                with dissolve
                " She reservedly responds to your kiss, but will go no further."
                hide 2newalex154
                show 2newalex155
                with dissolve
                a "\" Please stop. I feel bad enough about myself already from last night.\""
                p "\" You can always push me away.\""
                a "\" The fact that I didn't just makes me feel worse.\""
                p "\" Alright. I promise I won't kiss you again.\""
                a "\" Thank you...\""
                p "\" Unless!\""
                a "\" Yes?\""
                p "\" You kiss me first.\""
                a "\" Deal.\""
                hide 2newalex155
                show 2newalex156
                with dissolve
                a "\" We should be getting up.\""
                a "\" You have to meet with Dima today.\""
                p "\" Right.\""
                hide 2newalex156
                show back1
                with dissolve
                show 2newalex98
                with dissolve
                " You drop the girls off, and head to Dima's office."
                hide 2newalex98
                show 2newalex157
                with dissolve
                p "\" Hey, boss!\""
                di "\" Boss?\""
                di "\" Am I still your boss?\""
                di "\" That's very good to hear, given that I haven't heard from you in the past few days.\""
                di "\" What have you been up to?\""
                p "\" Let me explain.\""
                hide 2newalex157
                show mms41
                with dissolve
                " You tell him about the modeling agency."
                di "\" Hmmm...\""
                di "\" This might be something.\""
                di "\" We need to talk to Boris.\""
                hide mms41
                show back1
                with dissolve
                show 2newalex158
                with dissolve
                di "\" This could be a real feather in your hat, you know.\""
                p "\" I hope so.\""
                di "\" Aha... And what else have you been up to?\""
                p "\" What do you mean?\""
                di "\" I had you followed you know. I don't like not knowing what my people are up to.\""
                di "\" Spent the night at Isabella's place, eh?\""
                di "\" If Alexandra finds out that your railing her friend... Well... It won't be good.\""
                p "\" It's not like that.\""
                p "\" Alexandra was there.\""
                hide 2newalex158
                show 2newalex249
                with dissolve
                di "\" She was there?\""
                di "\" You mean... Both of them?\""
                p "\" It's not like that.\""
                di "\" Right...\""
                di "\" How was it? I've always wanted to know.\""
                di "\" She's been a muff diver all her life, you know.\""
                di "\" Must be like a vice in there.\""
                hide 2newalex249
                show 2newalex249a
                with dissolve
                p "\" Careful...\""
                " Something in your voice, makes him hesitate.\""
                di "\"... ...\""
                di "\" Sorry.\""
                hide 2newalex249a
                show 2newalex158
                with dissolve
                p "\" It's not like that.\""
                di "\" Right. Whatever you say.\""
                hide 2newalex158
                show 2newalex159
                with dissolve
                " You get to Boris' house and find Yuri waiting."
                yuri "\" You here to see the boss?\""
                di "\" Yeah.\""
                yuri "\" I'll let him know you're here.\""
                hide 2newalex159
                show 2newalex160
                with dissolve
                " Dima gently pushes him aside."
                di "\" Right... Right...\""
                di "\" You do you that, buddy.\""
                di "\" Let's go, [player_name].\""
                hide 2newalex160
                show 2newalex161
                with dissolve
                b "\" Yes?\""
                b "\" What do you two want?\""
                hide 2newalex161
                show 2newalex162
                with dissolve
                di "\" Wait 'til you hear this boss.\""
                di "\" Seems our friend here has been a busy little bee.\""
                hide 2newalex162
                show 2newalex163
                with dissolve
                " You tell Boris about the modeling agency."
                hide 2newalex163
                show 2newalex164
                with dissolve
                b "\" I see.\""
                b "\" What else can you tell me about this place?\""
                p "\" What else?\""
                b "\" Who's the owner?\""
                p "\" Some woman. I'm not sure.\""
                b "\" Are they connected to anyone?\""
                p "\" Connected? I don't think so.\""
                b "\" Seems to me you haven't done your homework.\""
                b "\" Still. This is worth looking into.\""
                b "\" Hit the library. Hit the Corporate Registrar's Office.\""
                b "\" Come back to me when you have all the info.\""
                hide 2newalex164
                show 2newalex162
                with dissolve
                di "\" Understood, boss.\""
                di "\" We'll be back when we know everything.\""
                hide 2newalex162
                show 2newalex165
                with dissolve
                di "\" You hit the library. See if you can find out anything.\""
                di "\" I'll see about the rest.\""
                p "\" I don't really see what I can find out there.\""
                di "\" Me neither.\""
                di "\" But they usually keep a record of all judicial decisions. See if this firm pops up anywhere.\""
                p "\" Alright.\""
                di "\" I'll come there once I'm done with my stuff.\""
                hide 2newalex165
                show 2newalex166
                with dissolve
                " You head over, and start looking."
                hide 2newalex166
                show 1newalex56
                with dissolve
                p "\" Adriana?\""
                p "\" Hey!\""
                p "\" Can you help me to look for something?\""
                hide 1newalex56
                show 1newalex57
                with dissolve
                adi "\" What?\""
                p "\" I wanted your help with something.\""
                adi "\" I'm sorry.\""
                adi "\" I'm not allowed to talk to you.\""
                p "\" What?\""
                hide 1newalex57
                show 1newalex58
                with dissolve
                adi "\" I'm sorry.\""
                p "\" Not allowed?\""
                adi "\" Sorry.\""
                di "\" Who's that?\""
                hide 1newalex58
                show 2newalex167
                with dissolve
                p "\" Huh? Oh... Just a neighbor.\""
                p "\" Found anything?\""
                di "\" Not a thing.\""
                p "\" Me neither.\""
                hide 2newalex167
                show 2newalex168
                with dissolve
                di "\" That's good, though.\""
                di "\" It means it's probably what it seems to be.\""
                p "\" Should we go back to Boris?\""
                hide 2newalex168
                show 2newalex169
                with dissolve
                di "\" Not yet.\""
                di "\" He's likely to ask us what year the building was built.\""
                di "\" You go back to collections for now.\""
                di "\" I'll keep looking into this, and report back to the boss.\""
                di "\" I'll let you know when it's time to move.\""
                p "\" Alright.\""
                di "\" Isn't it time to pick up Alex, by the way.\""
                p "\" Shit!\""
                di "\" Wouldn't want to be late.\""
                hide 2newalex169
                show back1
                with dissolve
                show 2newalex170
                with dissolve
                " You quickly go to pick up the girls."
                a "\" So, how did it go?\""
                p "\" Waiting for work from upstairs.\""
                a "\" So, we're going through with it?\""
                p "\" Seems so.\""
                p "\" How did it go with your exam?\""
                hide 2newalex170
                show 2newalex171
                with dissolve
                i "\" Ok.\""
                i "\" We have another one tomorrow, though.\""
                i "\" Have to pull another all-nighter.\""
                hide 2newalex171
                show 2newalex172
                with dissolve
                i "\" We don't have time to hang out with you again.\""
                i "\" I mean, you can hang out with us if you want, But...\""
                p "\" That's ok, Izzy. Ha ha...\""
                p "\" I need to go to the gym tonight anyway. Haven't been in a while.\""
                hide 2newalex172
                show 2newalex173
                with dissolve
                " You drop them off at Izzy's, and head to the gym."
                hide 2newalex173
                show gym2
                with dissolve
                " Having not visited in a while, and you have to admit, sexually frustrated, you push yourself very hard."
                if dannymission1goodending == True:
                    jump dannymission2
                else:
                    jump ep2bigcont5

label dannymission2:
                scene 2newalex174
                with dissolve
                danny "\" Hey there!\""
                p "\" Hey!\""
                danny "\" Pushing yourself pretty hard.\""
                p "\" Yeah.\""
                danny "\" You're the last one in the gym tonight.\""
                p "\" I'll walk you to your car, don't worry.\""
                show 2newalex175
                with dissolve
                danny "\" Thanks. You don't have to.\""
                danny "\" But why are you pushing yourself this hard?\""
                danny "\" You might injure yourself.\""
                call screen screen9

label dannyworkhardgym:
                scene 2newalex175
                with dissolve
                p "\" Just trying to work hard.\""
                danny "\" Alright.\""
                danny "\" I guess I'll leave you to it, then.\""
                p "\" Yeah.\""
                show 2newalex176
                with dissolve
                danny "\" Later.\""
                p "\" Later.\""
                jump ep2bigcont5

label dannysexfrustr:
                scene 2newalex175
                with dissolve
                p "\" To be honest.\""
                danny "\" Yes?\""
                p "\" Trying to work out some sexual frustration.\""
                show 2newalex177
                with dissolve
                danny "\" Ha ha ha...\""
                danny "\" You?\""
                p "\" Yeah.\""
                hide 2newalex177
                show 2newalex178
                with dissolve
                danny "\" I find that a little hard to believe.\""
                p "\" Believe it.\""
                hide 2newalex178
                show 2newalex176
                with dissolve
                danny "\" I'll see you later, I guess.\""
                p "\" Later.\""
                danny "\" Ha ha ha... Sexual frustration.\""
                hide 2newalex176
                show 2newalex179
                with dissolve
                " You work yourself until you just can't do it anymore, and head to the locker room."
                hide 2newalex179
                show 2newalex180
                with dissolve
                p "\" Still no word from Dima.\""
                p "\" Damn.\""
                hide 2newalex180
                show 2newalex181
                with dissolve
                danny "\" We're closing up.\""
                p "\" Sorry.\""
                p "\" I'll be out of here in a minute.\""
                hide 2newalex181
                show 2newalex182
                with dissolve
                danny "\" How did it go with your... Frustrations?\""
                p "\" Ha ha...\""
                p "\" Don't know why I said that.\""
                hide 2newalex182
                show 2newalex183
                with dissolve
                danny "\" Would you like a helping hand with that?\""
                p "\" A helping hand?\""
                danny "\" Yes.\""
                call screen screen10

label dannynohandjob:
                scene 2newalex183
                with dissolve
                p "\" Ha ha...\""
                p "\" I'm good.\""
                p "\" Don't know why I said that, really.\""
                danny "\" Suit yourself.\""
                show 2newalex184
                with dissolve
                danny "\" But we are closing.\""
                danny "\" So, you'd better hurry up.\""
                p "\" Right.\""
                jump ep2bigcont5

label dannyhandjob:
                scene 2newalex183
                with dissolve
                p "\" Actually...\""
                p "\" If you're offering...\""
                show 2newalex185
                with dissolve
                "She comes over, and grabs onto your dick."
                danny "\" Let's see now.\""
                danny "\" What do we have here.\""
                hide 2newalex185
                show 2newalex186
                with dissolve
                danny "\" Are you getting hard for me baby?\""
                hide 2newalex186
                show 2newalex187
                with dissolve
                danny "\" There we go.\""
                scene dannyhand animated with fade:
                    "1a1"
                    pause 0.05
                    "1a2"
                    pause 0.05
                    "1a3"
                    pause 0.05
                    "1a4"
                    pause 0.05
                    "1a5"
                    pause 0.05
                    "1a6"
                    pause 0.05
                    "1a7"
                    pause 0.05
                    "1a8"
                    pause 0.05
                    "1a9"
                    pause 0.05
                    "1a10"
                    pause 0.05
                    "1a11"
                    pause 0.05
                    "1a12"
                    pause 0.05
                    "1a13"
                    pause 0.05
                    "1a14"
                    pause 0.05
                    "1a15"
                    pause 0.05
                    "1a16"
                    pause 0.05
                    repeat
                $ renpy.pause ()
                danny "\" You like that?\""
                show 2newalex188
                with dissolve
                danny "\" Are you going to cum for me?\""
                danny "\" Are you going to cum all over my hand?\""
                scene dannyhand2 animated with fade:
                    "1a1"
                    pause 0.03
                    "1a2"
                    pause 0.03
                    "1a3"
                    pause 0.03
                    "1a4"
                    pause 0.03
                    "1a5"
                    pause 0.03
                    "1a6"
                    pause 0.03
                    "1a7"
                    pause 0.03
                    "1a8"
                    pause 0.03
                    "1a9"
                    pause 0.03
                    "1a10"
                    pause 0.03
                    "1a11"
                    pause 0.03
                    "1a12"
                    pause 0.03
                    "1a13"
                    pause 0.03
                    "1a14"
                    pause 0.03
                    "1a15"
                    pause 0.03
                    "1a16"
                    pause 0.03
                    repeat
                $ renpy.pause ()
                danny "\" That's right.\""
                danny "\" Cum for me.\""
                show 2newalex193
                with dissolve
                " She doesn't protest when you grab her firm ass."
                danny "\' Ohh...\""
                scene dannyhand3 animated with fade:
                    "1a1"
                    pause 0.03
                    "1a2"
                    pause 0.03
                    "1a3"
                    pause 0.03
                    "1a4"
                    pause 0.03
                    "1a5"
                    pause 0.03
                    "1a6"
                    pause 0.03
                    "1a7"
                    pause 0.03
                    "1a8"
                    pause 0.03
                    "1a9"
                    pause 0.03
                    "1a10"
                    pause 0.03
                    "1a11"
                    pause 0.03
                    "1a12"
                    pause 0.03
                    "1a13"
                    pause 0.03
                    "1a14"
                    pause 0.03
                    "1a15"
                    pause 0.03
                    "1a16"
                    pause 0.03
                    repeat
                $ renpy.pause ()
                show 2newalex189
                with dissolve
                danny "\" Give it to me!\""
                danny "\" Give me your cum.\""
                scene dannyhand3 animated with fade:
                    "1a1"
                    pause 0.03
                    "1a2"
                    pause 0.03
                    "1a3"
                    pause 0.03
                    "1a4"
                    pause 0.03
                    "1a5"
                    pause 0.03
                    "1a6"
                    pause 0.03
                    "1a7"
                    pause 0.03
                    "1a8"
                    pause 0.03
                    "1a9"
                    pause 0.03
                    "1a10"
                    pause 0.03
                    "1a11"
                    pause 0.03
                    "1a12"
                    pause 0.03
                    "1a13"
                    pause 0.03
                    "1a14"
                    pause 0.03
                    "1a15" 
                    pause 0.03
                    "1a16"
                    pause 0.03
                    repeat
                $ renpy.pause ()
                p "\" Shit...\""
                danny "\" That's right...\""
                danny "\" That's right...\""
                show 2newalex191
                with dissolve
                p "\" Fuck!!!\""
                show 2newalex190
                with dissolve
                " She buries her face in your shoulder."
                danny "\" There you go.\""
                danny "\" There you go, baby.\""
                hide 2newalex190
                show 2newalex192
                with dissolve
                danny "\" Wow! You really were backed up.\""
                danny "\" Better go wash my hands.\""
                hide 2newalex192
                show 2newalex194
                with dissolve
                p "\" Wait.\""
                danny "\" Sorry. But that's about as far as I'm willing to go without even a date.\""
                $ renpy.end_replay()
                " Do you want to ask her out?"
                call screen screen11

label dannydatenoask:
                scene 2newalex194
                with dissolve
                p "\" Thank you.\""
                danny "\" No problem.\""
                show 2newalex184
                with dissolve
                danny "\" But we are closing.\""
                danny "\" So, you'd better hurry up.\""
                p "\" Right.\""
                jump ep2bigcont5

label dannydateask:
                scene 2newalex194
                with dissolve
                $ dannyaskdate = True
                p "\" Would you like to go out sometime?\""
                show 2newalex195
                with dissolve
                danny "\" Hmmm...\""
                danny "\" I'll think about it.\""
                hide 2newalex195
                show 2newalex184
                with dissolve
                danny "\" But we are closing.\""
                danny "\" So, you'd better hurry up.\""
                p "\" Right.\""
                jump ep2bigcont5

label ep2bigcont5:
                scene 2newalex196
                with dissolve
                " You found it difficult to fall asleep that night, regardless of your gym activities."
                show 2newalex145
                with dissolve
                " And your thoughts kept turning to the image and scent of the girls sleeping next to you."
                scene blackscreen
                with dissolve
                "... ..."
                "... ..."
                scene back1
                with dissolve
                show 2newalex98
                with dissolve
                " When you drove the girls to school the next day, Alex and Izzy were pretty upbeat."
                p "\" Last exam?\""
                a "\" For now.\""
                i "\" Can't wait for it to be over.\""
                hide 2newalex98
                show 2newalex197
                with dissolve
                " But when you picked them up, Izzy was slumped over like a dead bumblebee."
                p "\" Are you ok?\""
                i "\" Agh...\""
                hide 2newalex197
                show 2newalex198
                with dissolve
                a "\" She's finally crashed.\""
                i "\" Mmmm...\""
                a "\" Been surviving on caffeine and sugar for the last few days.\""
                p "\" Why does she push herself so hard.\""
                hide 2newalex198
                show 2newalex199
                with dissolve
                i "\" I have nothing to fall back on.\""
                i "\" For me it's good grades, or bust.\""
                a "\" Shhh... It's ok.\""
                i "\" Can we go to Puppy's place?\""
                i "\" I sleep like the dead over there.\""
                a "\" You slept over there?\""
                p "\" Just slept.\""
                hide 2newalex199
                show 2newalex198
                with dissolve
                a "\" Well, you have your destination.\""
                p "\" Yes, ma'am.\""
                hide 2newalex198
                show 2newalex201
                with dissolve
                " By the time you get home, Izzy is fast asleep."
                hide 2newalex201
                show 2newalex202
                with dissolve
                " Still sleeping, you carry her upstairs."
                p "\" I'm taking her to the bedroom.\""
                hide 2newalex202
                show 2newalex203
                with dissolve
                " You put her on the bed, still dead to the world."
                hide 2newalex203
                show 2newalex204
                with dissolve
                a "\" Any news?\""
                p "\" You seem anxious.\""
                a "\" I am, a little.\""
                p "\" I'll check in with Dima today when I go pick up my collections.\""
                a "\" Good.\""
                hide 2newalex204
                show 2newalex205
                with dissolve
                " She sits down on the couch."
                a "\" So, Izzy's been sleeping over here?\""
                p "\" Only once.\""
                p "\" Nothing happened.\""
                hide 2newalex205
                show 2newalex206
                with dissolve
                a "\" Why do I believe you?\""
                p "\" Because you trust me. Because you trust her.\""
                a "\" Damn it. I do.\""
                hide 2newalex206
                show 2newalex207
                with dissolve
                a "\" Alright. You need to take her clothes off.\""
                a "\" She shouldn't sleep in her school uniform.\""
                a "\" I'll see what you have to eat around here.\""
                hide 2newalex207
                show 2newalex208
                with dissolve
                " Izzy is sprawled all over your bed."
                hide 2newalex208
                show 2newalex209
                with dissolve
                " You take off her shoes."
                hide 2newalex209
                show 2newalex210
                with dissolve
                " Then turn her around."
                i "\" Hey.\""
                p "\" I'm trying to make you more comfortable.\""
                p "\" Keep your legs straight.\""
                hide 2newalex210
                show 2newalex211
                with dissolve
                " You take off her skirt."
                hide 2newalex211
                show 2newalex212
                with dissolve
                p "\" Arms up. Let me get your shirt.\""
                i "\" Alright.\""
                hide 2newalex212
                show 2newalex213
                with dissolve
                p "\" There you go.\""
                p "\" Better?\""
                i "\" Yeah.\""
                i "\" Where's the Teddy I gave you.\""
                p "\" Over there.\""
                hide 2newalex213
                show 2newalex214
                with dissolve
                " She grabs it, and hugs it. And is asleep within seconds."
                hide 2newalex214
                show 2newalex215
                with dissolve
                a "\" Sleeping?\""
                p "\" Like the dead.\""
                a "\" Poor thing.\""
                hide 2newalex215
                show 2newalex216
                with dissolve
                a "\" But on a different note, how do you survive?\""
                p "\" What do you mean?\""
                a "\" I barely found anything to eat.\""
                hide 2newalex216
                show 2newalex217
                with dissolve
                a "\" All I could find is some pasta.\""
                p "\" Well?\""
                a "\" This just won't do.\""
                hide 2newalex217
                show 2newalex218
                with dissolve
                a "\" Keep eating like this, and I'll lose you to a heart attack at 40.\""
                p "\" At 40, huh?\""
                p "\" You're starting to trust my dreams too?\""
                a "\" You know what I mean.\""
                p "\" Yeah.\""
                p "\" I'd better go do my collections.\""
                hide 2newalex218
                show 2newalex219
                with dissolve
                a "\" Are you going to be gone long?\""
                p "\" A little while.\""
                a "\" I'll make this by the time you're back.\""
                hide 2newalex219
                show veryhardcoll2
                with dissolve
                " After doing your collections for the day, you go see Dima."
                hide veryhardcoll2
                show 2newalex220
                with dissolve
                di "\" Good news, my friend.\""
                di "\" We're going forward.\""
                p "\" The agency?\""
                hide 2newalex220
                show 2newalex221
                with dissolve
                di "\" Tomorrow.\""
                di "\" Be here early. Let someone else drive Alexandra for a day.\""
                di "\" You'll do good from this you know.\""
                di "\" Looking at a pretty hefty finder's fee.\""
                p "\" I was hoping Boris might let me run it.\""
                hide 2newalex221
                show 2newalex222
                with dissolve
                di "\" Don't get ahead of yourself.\""
                di "\" You're coming up pretty fast already.\""
                di "\" A finder's fee is enough for now.\""
                di "\" And remember. Tomorrow! Early!\""
                p "\" I'll be here.\""
                hide 2newalex222
                show 2newalex223
                with dissolve
                " When you get home, you find a plate of pasta waiting for you."
                hide 2newalex223
                show 2newalex224
                with dissolve
                a "\" I think it's a little cold by now.\" She says, while watching TV."
                a "\" I'll heat it up if you want.\""
                p "\" It's fine.\""
                p "\" It's just... Things are up for tomorrow, but Dima said I'm only getting a finder's fee.\""
                a "\" Let me worry about that. I'll talk to Dad.\""
                a "\" Hope you didn't tell him I was here. I told Dad I'm sleeping at Izzy's again.\""
                p "\" I didn't. What are you watching.\""
                hide 2newalex224
                show 2newalex225
                with dissolve
                p "\" Oh...\""
                a "\" It was in your favorites.\""
                p "\" Hanzo the Razor.\""
                hide 2newalex225
                show 2newalex226
                with dissolve
                p "\" You're really glued to it, eh?\""
                a "\" I don't get it.\""
                p "\" What's not to get?\""
                p "\" He's just an old fashioned cop, who tortures female subjects with pleasure.\""
                hide 2newalex226
                show 2newalex227
                with dissolve
                a "\" With his dick, you mean.\""
                p "\" Same thing.\""
                a "\" I can't even imagine.\""
                p "\" I think you can. And maybe have.\""
                hide 2newalex227
                show 2newalex228
                with dissolve
                a "\" Ha ha ha...\""
                hide 2newalex228
                show 2newalex229
                with dissolve
                a "\" Getting spit roasted on a giant Japanese dick?\""
                a "\" No, I can't say that I have.\""
                p "\" You're being too specific.\""
                hide 2newalex229
                show 2newalex230
                with dissolve
                a "\" Let me guess. You have a suitable alternative ready?\""
                p "\" Ouch.\""
                p "\" That sounded a little cold.\""
                hide 2newalex230
                show 2newalex231
                with dissolve
                a "\" Sorry.\""
                a "\" If I was planning on getting spit roasted, you'd be my first call.\""
                p "\" First?\""
                a "\" And only.\""
                hide 2newalex231
                show 2newalex232
                with dissolve
                i "\" Hey.\""
                a "\" Hey, sleepy head.\""
                i "\" Where's my shirt?\""
                p "\" On the chair.\""
                i "\" No, I mean your shirt. The one you gave to sleep in.\""
                p "\" Right. In the closet somewhere.\""
                hide 2newalex232
                show 2newalex233
                with dissolve
                a "\" I'd better find something too.\""
                a "\" Need to change out of these clothes.\""
                hide 2newalex233
                show 2newalex234
                with dissolve
                " They come back wearing a couple of your shirts."
                hide 2newalex234
                show 2newalex235
                with dissolve
                " And you settle down for an evening of 'Hanzo the Razor'."
                hide 2newalex235
                show 2newalex236
                with dissolve
                i "\" I don't get it.\""
                i "\" What's he doing?\""
                hide 2newalex236
                show 2newalex237
                with dissolve
                a "\" Torturing them with pleasure, I've been told.\""
                hide 2newalex237
                show 2newalex236
                with dissolve
                i "\" And they just tell him everything?\""
                hide 2newalex236
                show 2newalex237
                with dissolve
                a "\" Seems so.\""
                hide 2newalex237
                show 2newalex236
                with dissolve
                i "\" That's stupid.\""
                hide 2newalex236
                show 2newalex235
                with dissolve
                p "\" Philistines! Both of you.\""
                p "\" Can't appreciate art.\""
                hide 2newalex235
                show 2newalex238
                with dissolve
                " That night you slept like a baby, with the girls softly breathing next to you."
                scene blackscreen
                with dissolve
                "..."
                "... ... ..."
                show 2newalex239
                with dissolve
                a "\" Morning!\""
                p "\" Hey.\""
                a "\" Get up! You shouldn't be late.\""
                hide 2newalex239
                show 2newalex240
                with dissolve
                i "\" Morning.\""
                a "\" We'll get ourselves to school today. You take a shower and hurry up.\""
                p "\" I can take you. Not a problem.\""
                a "\" You focus on your thing. We can manage.\""
                hide 2newalex240
                show 2newalex241
                with dissolve
                " You take a quick shower, and get dressed."
                hide 2newalex241
                show 2newalex242
                with dissolve
                a "\" Big day for our puppy today.\""
                a "\" Getting a promotion.\""
                i "\" Really?\""
                i "\" Congrats.\""
                hide 2newalex242
                show 2newalex243
                with dissolve
                a "\" Let's not celebrate just yet.\""
                a "\" He still has his part to do.\""
                a "\" And me, mine.\""
                p "\" Wish me luck.\""
                hide 2newalex243
                show 2newalex244
                with dissolve
                a "\" I think I can do a little better.\""
                hide 2newalex244
                show 2newalex245
                with dissolve
                " She gives you a kiss."
                i "\" Alright.\""
                hide 2newalex245
                show 2newalex246
                with dissolve
                " And Izzy a far more sensual one."
                hide 2newalex246
                show 2newalex247
                with dissolve
                a "\" Good luck.\""
                p "\" Thanks.\""
                a "\" See you when you pick us up.\""
                hide 2newalex247
                show 2newalex248
                with dissolve
                " You head over to Dima's."
                di "\" Ready?\""
                p "\" Yes.\""
                di "\" These guys will be coming with us.\""
                hide 2newalex248
                show back1
                with dissolve
                show 2newalex249
                with dissolve
                di "\" Better let me do the talking.\""
                di "\" This is your first time and all.\""
                p "\" Got it.\""
                hide 2newalex249
                show 2newalex265
                with dissolve
                di "\" You two, wait in the car.\""
                " The men nod."
                hide 2newalex265
                show 2newalex250
                with dissolve
                " You and Dima go upstairs."
                hide 2newalex250
                show 2newalex251
                with dissolve
                di "\" New day, huh?\""
                di "\" I could get used to working here.\""
                p "\" So could I.\""
                di "\" Don't get greedy.\""
                hide 2newalex251
                show 2newalex252
                with dissolve
                nar "\" Can I help you gentlemen?\""
                hide 2newalex252
                show 2newalex253
                with dissolve
                di "\" We would like to speak to the boss.\""
                hide 2newalex253
                show 2newalex252
                with dissolve
                nar "\" What about, if I may ask?\""
                hide 2newalex252
                show 2newalex253
                with dissolve
                di "\" We're potential customers.\""
                hide 2newalex253
                show 2newalex254
                with dissolve
                nar "\" Oh, of course.\""
                nar "\" I'll show you right in.\""
                hide 2newalex254
                show 2newalex255
                with dissolve
                nar "\" Ma'am. Two customers.\""
                cl "\" One minute.\""
                cl "\" Have a seat, gentlemen.\""
                hide 2newalex255
                show 2newalex256
                with dissolve
                p "\" I feel, we're not being taken seriously.\""
                di "\" Let's sit down.\""
                hide 2newalex256
                show 2newalex257
                with dissolve
                " You and Dima sit down, and wait for the woman to finish."
                cl "\" One minute.\""
                hide 2newalex257
                show 2newalex258
                with dissolve
                cl "\" Finally.\""
                cl "\" All done.\""
                cl "\" What can we do for you gentlemen?\""
                di "\" We have a group of investors coming in from out of town.\""
                hide 2newalex258
                show 2newalex259
                with dissolve
                cl "\" I see.\""
                di "\" And of course, we'd like to promote an image of success.\""
                cl "\" Of course.\""
                hide 2newalex259
                show 2newalex260
                with dissolve
                di "\" We were made to understand that your models might be available for such work?\""
                hide 2newalex260
                show 2newalex259
                with dissolve
                cl "\" It can be arranged, of course.\""
                hide 2newalex259
                show 2newalex260
                with dissolve
                di "\" And there lies the problem.\""
                di "\" I have to apologize, but we performed a little deception.\""
                cl "\" Deception?\""
                di "\" We're not actually clients.\""
                di "\" We represent a group of businessmen, that are very concerned about what happens here.\""
                hide 2newalex260
                show 2newalex261
                with dissolve
                cl "\" Excuse me?\""
                di "\" You see. We've heard that this agency might be a front for prostitution.\""
                cl "\" I think you need to leave.\""
                hide 2newalex261
                show 2newalex260
                with dissolve
                di "\" It doesn't matter to us how you make a living, ma'am.\""
                di "\" But we can't say the same thing about everyone in the community.\""
                di "\" We fear that some puritanical people might get wind of this, and decide to do something about it.\""
                hide 2newalex260
                show 2newalex262
                with dissolve
                cl "\" You need to leave.\""
                di "\" Such a disturbance might cause problems all around.\""
                cl "\" You think I don't know what this is?\""
                di "\" But for a menial fee, we can ensure that no such disturbance happens.\""
                cl "\" You need to leave, NOW!\""
                hide 2newalex262
                show 2newalex263
                with dissolve
                di "\" I'm sorry you feel that way.\""
                di "\" This is all optional, of course.\""
                di "\" We can only hope that your luck holds out.\""
                hide 2newalex263
                show 2newalex264
                with dissolve
                cl "\" What do you take me for? You're just a two-bit thug.\""
                cl "\" Get out.\""
                hide 2newalex264
                show 2newalex263
                with dissolve
                di "\" Very well, ma'am.\""
                hide 2newalex263
                show back
                with dissolve
                show 2newalex249
                with dissolve
                p "\" She didn't seem receptive.\""
                di "\" None of them are at first.\""
                hide 2newalex249
                show 2newalex265
                with dissolve
                di "\" You two! We're going to get some lunch.\""
                di "\" You head upstairs, and do what you do best.\""
                hide 2newalex265
                show 2newalex249
                with dissolve
                di "\" Let's go.\""
                hide 2newalex249
                show 2newalex266
                with dissolve
                " You and Dima go to the park."
                di "\" Mmmm... Ramen.\""
                hide 2newalex266
                show 2newalex267
                with dissolve
                di "\" So, you gotta tell me.\""
                di "\" Alexandra...\""
                p "\" I told you. it's not what you think.\""
                di "\" Right... Right...\""
                hide 2newalex267
                show 2newalex268
                with dissolve
                di "\" You're playing with fire buddy.\""
                p "\" You said that.\""
                di "\" So long as you know.\""
                hide 2newalex268
                show 2newalex267
                with dissolve
                " You finish up your ramen."
                hide 2newalex267
                show 2newalex269
                with dissolve
                di "\" The boys should be done by now.\""
                di "\" We ought to get back.\""
                hide 2newalex269
                show 2newalex270
                with dissolve
                " When you get back to the agency, the girls are all gone and the furniture is upside down."
                hide 2newalex270
                show 2newalex271
                with dissolve
                di "\" Huh.\""
                di "\" Hope those two idiots didn't actually hit someone.\""
                hide 2newalex271
                show 2newalex272
                with dissolve
                " In the office, you find Mrs. Clara sprawled on the floor."
                hide 2newalex272
                show 2newalex273
                with dissolve
                di "\" Are you ok?\""
                cl "\" What do you want?\""
                di "\" No one hit you, did they?\""
                cl "\" No.\""
                hide 2newalex273
                show 2newalex274
                with dissolve
                di "\" Someone will come back tomorrow.\""
                di "\" Now it could be the two of us. Or it could be someone else.\""
                cl "\"... ...\""
                di "\" Who do you want to see tomorrow?\""
                cl "\"... ... ...\""
                cl "\" You.\""
                di "\" Good girl.\""
                hide 2newalex274
                show 2newalex275
                with dissolve
                p "\" Are you ok?\""
                cl "\" Please just go.\""
                hide 2newalex275
                show 2newalex276
                with dissolve
                p "\" Lady...\""
                cl "\" PLEASE... JUST... GO...\""
                p "\" Alright.\""
                hide 2newalex276
                show back
                with dissolve
                show 2newalex249
                with dissolve
                " Back in the car, Dima says."
                di "\" That went well.\""
                p "\" She seemed pretty shook up.\""
                di "\" That's always the case. They didn't hit her.\""
                di "\" But for people who think no one can touch them only to find out that someone can, is always debilitating.\""
                p "\" I need to go pick up Alexandra from school.\""
                di "\" I'll come with you.\""
                di "\" We need to go see Boris, anyway.\""
                hide 2newalex249
                show 2newalex277
                with dissolve
                di "\" Hi, girls!\""
                hide 2newalex277
                show 2newalex279
                with dissolve
                i "\" Hi.\""
                hide 2newalex279
                show 2newalex277
                with dissolve
                a "\" Dima.\""
                di "\" Did you girls miss me?\""
                a "\" No one ever misses you, Dima.\""
                di "\" Watch it blondie, you're cutting deep.\""
                hide 2newalex277
                show 2newalex280
                with dissolve
                di "\" Do we drop you off at your place, Isabella?\""
                di "\" Or are you coming with us.\""
                a "\" She's crashing with me.\""
                di "\" Alright.\""
                hide 2newalex280
                show 2newalex281
                with dissolve
                " You drive to the villa."
                " And while Izzy heads upstairs, Alexandra stays back."
                di "\" Me and [player_name] need to go see your Dad.\""
                a "\" I know. I'm coming too.\""
                di "\" It's a business thing.\""
                a "\" I know. I'm coming too.\""
                di "\" If you say so.\""
                hide 2newalex281
                show 2newalex283
                with dissolve
                " You go and report to Boris what happened."
                hide 2newalex283
                show 2newalex164
                with dissolve
                b "\" Things are good then.\""
                b "\" But there's one thing I don't understand.\""
                hide 2newalex164
                show 2newalex284
                with dissolve
                b "\" And that is, what is Alexandra doing here.\""
                hide 2newalex284
                show 2newalex285
                with dissolve
                a "\" I told you I want to be more involved.\""
                a "\" And I'm here to make sure that this agency goes to [player_name].\""
                hide 2newalex285
                show 2newalex284
                with dissolve
                b "\" Excuse me?\""
                hide 2newalex284
                show 2newalex286
                with dissolve
                a "\" He found it.\""
                a "\" He brought it to you.\""
                a "\" You should give it to him.\""
                hide 2newalex286
                show 2newalex164
                with dissolve
                b "\" Excuse me, boys.\""
                b "\" I need to have a talk with my Daughter.\""
                b "\" Wait outside.\""
                di "\" Understood.\""
                hide 2newalex164
                show 2newalex287
                with dissolve
                " You and Dima go outside."
                di "\" It's not like that, huh?\""
                di "\" She's just here to back you up as a... Friend, huh?\""
                di "\" Damn, boy.\""
                di "\" You must've unleashed a fire hydrant between her legs.\""
                p "\" Careful.\""
                hide 2newalex287
                show 2newalex288
                with dissolve
                " He lights up a cigarette."
                di "\" Oh, relax.\""
                di "\" And enough with the crazy eyes. That shit doesn't scare me.\""
                di "\" But you've unleashed the Kraken, huh?\""
                hide 2newalex288
                show 2newalex289
                with dissolve
                di "\" And trust me. I'll want details.\""
                hide 2newalex289
                show 2newalex290
                with dissolve
                " After a few minutes, Alex and Boris come out."
                hide 2newalex290
                show 2newalex291
                with dissolve
                b "\" The agency is yours.\""
                p "\" Thank you.\""
                b "\" Shut up!\""
                hide 2newalex291
                show 2newalex292
                with dissolve
                " Alexandra gives you a wink over his shoulder."
                hide 2newalex292
                show 2newalex293
                with dissolve
                b "\" This is a much bigger responsibility than what you had before.\""
                p "\" I realize...\""
                b "\" Shut up!\""
                b "\" Don't fuck this up.\""
                p "\" Yes, sir...\""
                b "\" Shut up!\""
                hide 2newalex293
                show 2newalex294
                with dissolve
                " Boris heads back inside."
                a "\" You did the right thing Dad.\""
                b "\" Careful girl.\""
                hide 2newalex294
                show 2newalex295
                with dissolve
                a "\" So, we did it.\""
                hide 2newalex295
                show 2newalex289
                with dissolve
                di "\" 'We' did it, huh?\""
                hide 2newalex289
                show 2newalex295
                with dissolve
                call screen screen12

label alexnothanks:
                scene 2newalex295
                with dissolve
                p "\" Yeah.\""
                show 2newalex296
                with dissolve
                a "\" See you tomorrow.\""
                p "\" Of course.\""
                jump ep2bigcont6

label alexthanks:
                scene 2newalex295
                with dissolve
                $ alexpoints += 1
                p "\" Thank you.\""
                show 2newalex297
                with dissolve
                " She comes forward and gives you a deep kiss."
                di "\" Fire hydrant.\""
                hide 2newalex297
                show 2newalex298
                with dissolve
                a "\" See you tomorrow.\""
                p "\" Of course.\""
                jump ep2bigcont6

label ep2bigcont6:
                scene 1newalex257
                with dissolve
                " Later that night, before you go to bed, you receive a message."
                show 2newalex299
                with dissolve
                show 2newalex302
                with dissolve
                $ renpy.pause ()
                show 2newalex303
                with dissolve
                $ renpy.pause ()
                show 2newalex304
                with dissolve
                hide 2newalex304
                show 3newalex105
                with dissolve
                " It was a struggle to fall asleep that night."
                jump ep3
