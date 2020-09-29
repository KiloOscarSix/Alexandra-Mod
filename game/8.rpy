label ep8:
                default adigoodend3 = False
                default jamieride2goodending = False
                default boyspts = 0
                if ep7robbery == True:
                    jump ep8rob1
                else:
                    jump ep8norob1

label ep8rob1:
                scene 7newalex91
                with dissolve
                ja "\" What are we doing?\""
                p "\" Robbing a poker game.\""
                show 8newalex2
                with dissolve
                hu "\" Poker game?\""
                p "\" Yeah.\""
                p "\" Supposed to be a lot of cash inside a certain room.\""
                hu "\" Sounds good.\""
                ja "\" Yeah.\""
                p "\" Alright. I'll start setting things up.\""
                hide 8newalex2
                show 7newalex93
                with dissolve
                p "\" Hmmm...\""
                p "\" We should stake out the place a bit.\""
                p "\" Probably need some wheels.\""
                p "\" Wouldn't do to take a car that can come back to us.\""
                p "\" Should call Jamie about that.\""
                hide 7newalex93
                show 8newalex1
                with dissolve
                p "\" Hello?\""
                jam "\" Yes?\""
                jam "\" Who is this?\""
                p "\"[player_name].\""
                if jamieride1goodending == True:
                    jam "\" Hey!\""
                    jam "\" Long time no see.\""
                    p "\" Sadly, I called you because I need something.\""
                    jam "\" Well, come by.\""
                    p "\" Thanks.\""
                    hide 8newalex1
                    show back1
                    with dissolve
                    show 8newalex3
                    with dissolve
                    " You take the boys and head over."
                    hide 8newalex3
                    show 8newalex4
                    jam "\" There you are!\""
                    jam "\" I was starting to think you were hiding from me.\""
                    p "\" Never.\""
                    hide 8newalex4
                    show 8newalex5
                    with dissolve
                    " She comes over and gives you a short hug."
                    jam "\" You won't believe what came in.\""
                    p "\" You mean a car?\""
                    jam "\" Of course.\""
                    p "\" I'd love to take a ride with you, but...\""
                    hide 8newalex5
                    show 8newalex9
                    with dissolve
                    jam "\" Right.\""
                    jam "\" You came for another car.\""
                    p "\" Something that can't be traced back to anyone, hopefully.\""
                    hide 8newalex6
                    show 8newalex7
                    with dissolve
                    jam "\" Hmmm...\""
                    jam "\" Yeah. I can do that.\""
                    hide 8newalex7
                    show 8newalex8
                    with dissolve
                    jam "\" There's this.\""
                    p "\" A van?\""
                    jam "\" Problem?\""
                    p "\" No.\""
                    p "\" It's perfect, actually.\""
                    hide 8newalex8
                    show 8newalex10
                    with dissolve
                    jam "\" It's yours then.\""
                    p "\" How much?\""
                    jam "\" For you? I can make a good price.\""
                    jam "\" But can you come over here for a second?\""
                    p "\" Sure.\""
                    hide 8newalex10
                    show 8newalex11
                    with dissolve
                    " You both go over to one side."
                    jam "\" I get that you're busy now.\""
                    jam "\" But you want to drop by this weekend?\""
                    p "\" For the car you mentioned?\""
                    jam "\" What else?\""
                    call screen screen43

                else:
                    jam "\" Who?\""
                    p "\" [player_name].\""
                    p "\" Dima introduced us.\""
                    p "\" I brought you a car some time ago?\""
                    jam "\" Oh.\""
                    jam "\" Well, what do you want?\""
                    p "\" I imagine you're not only taking cars, but selling them?\""
                    jam "\" You need something?\""
                    p "\" Yeah.\""
                    jam "\" Well, come by.\""
                    p "\" Thanks.\""
                    hide 8newalex1
                    show back1
                    with dissolve
                    show 8newalex3
                    with dissolve
                    " You take the boys and head over."
                    hide 8newalex3
                    show 8newalex12
                    with dissolve
                    jam "\" Hey!\""
                    p "\" Hey!\""
                    hide 8newalex12
                    show 8newalex6
                    with dissolve
                    jam "\" What do you need?\""
                    p "\" Something that can't be traced back to anyone, hopefully.\""
                    hide 8newalex6
                    show 8newalex7
                    with dissolve
                    jam "\" Hmmm...\""
                    jam "\" Yeah. I can do that.\""
                    hide 8newalex7
                    show 8newalex8
                    with dissolve
                    jam "\" There's this.\""
                    p "\" A van?\""
                    jam "\" Problem?\""
                    p "\" No.\""
                    p "\" It's perfect, actually.\""
                    hide 8newalex8
                    show 8newalex6
                    with dissolve
                    jam "\" It will cost.\""
                    p "\" I'm sure.\""
                    jump ep8robcont1

label ep8yesjamie:
                scene 8newalex11
                with dissolve
                $ jamieride2goodending = True
                p "\" Sure.\""
                jam "\" Great.\""
                jam "\" I'll call you on Saturday?\""
                p "\" Deal.\""
                jump ep8robcont1

label epnojamie:
                scene 8newalex11
                with dissolve
                p "\" I'd love to, but...\""
                p "\" I'm not sure your driving style is what I'd call fun.\""
                p "\" Last time, I squeezed my knuckles so hard I lost feeling in my fingers.\""
                jam "\" Hmmm...\""
                jam "\" Never took you for a pussy.\""
                jam "\" Oh, well...\""
                jump ep8robcont1

label ep8robcont1:
                scene back1
                with dissolve
                show 8newalex13
                with dissolve
                " You pay for the car, and head out."
                ja "\" Where are we going?\""
                p "\" I'll tell you.\""
                hide 8newalex13
                show 7newalex97
                with dissolve
                " You take them to the laundry shop."
                hide 7newalex97
                show 8newalex13
                with dissolve
                ja "\" What's this?\""
                p "\" What does it look like.\""
                p "\" From what I understand, there's a poker game in there every other day.\""
                p "\" Lots of money.\""
                hide 8newalex13
                show 8newalex14
                with dissolve
                hu "\" And is there one tonight?\""
                p "\" I don't know.\""
                p "\" But you two will stand here and watch.\""
                p "\" If you see people going in without laundry bags and not coming out...\""
                hu "\" Got it.\""
                hide 8newalex14
                show 8newalex15
                with dissolve
                ja "\" And if to goes down tonight?\""
                p "\" No time like the present.\""
                p "\" About guns.\""
                ja "\" I can get guns.\""
                p "\" Good.\""
                p "\" I'll catch up on you later.\""
                hide 8newalex15
                show 7newalex91
                with dissolve
                " You leave them and head back to the agancy."
                p "\" Better call Marcello.\""
                show 8newalex1
                with dissolve
                p "\" Hello.\""
                vinc "\" Yes?\""
                p "\" It's [player_name]. Can you put your boss on?\""
                vinc "\" You can talk to me.\""
                p "\" Just tell him I'll have his money tonight.\""
                vinc "\" We'll have someone drop by tomorrow.\""
                p "\" Alright.\""
                jump ep8cont1

label ep8norob1:
                scene 7newalex91
                with dissolve
                p "\" Better call Marcello.\""
                show 8newalex1
                with dissolve
                p "\" Hello.\""
                vinc "\" Yes?\""
                p "\" It's [player_name]. Can you put your boss on?\""
                vinc "\" You can talk to me.\""
                p "\" Just tell him I have his money.\""
                vinc "\" We'll have someone drop by tomorrow.\""
                p "\" Alright.\""
                jump ep8cont1

label ep8cont1:
                scene 8newalex16
                with dissolve
                " Yuri comes and sits down next to you."
                yuri "\" So, when are we getting it?\""
                p "\" Soon.\""
                p "\" I'm working on it.\""
                p "\" You need help with anything?\""
                yuri "\" Me? No.\""
                p "\" Then I'm going home to take a nap.\""
                yuri "\" Sleep tight Chief.\""
                show 8newalex17
                with dissolve
                " You decide to go home for the afternoon."
                if adigoodend2 == True:
                    hide 8newalex17
                    show 8newalex18
                    with dissolve
                    " Walking up the stairs you pass by Adriana's door."
                    p "\" Hmmm...\""
                    p "\" I told her to wait for me by the door.\""
                    p "\" Do I really need this in my life?\""
                    call screen screen44

                else:
                    jump ep8homeend

label ep8noadi:
                scene 8newalex18
                with dissolve
                p "\" Fuck this shit.\""
                p "\" I have enough problems to deal with.\""
                jump ep8homeend

label ep8yesadi:
                scene 8newalex18
                with dissolve
                $ adigoodend3 = True
                p "\" Why not.\""
                p "\" It will take my mind of things.\""
                " *Knock* *Knock* *Knock*"
                " You hear scurrying inside."
                adi "\" Who is it?\""
                p "\" Who do you think?\""
                p "\" Open this door before I start huffing and puffing.\""
                " You hear her opening the door."
                show 8newalex19
                with dissolve
                " And enter."
                adi "\" Welcome...\""
                p "\" Hmmm...\""
                p "\" Is this where you've been waiting for me?\""
                adi "\" Yes. Every day.\""
                p "\" So, I definitely didn't hear you scrurrying just now.\""
                p "\" If you were here at the door, you wouldn't need to do that.\""
                adi "\"...\""
                p "\" *Sigh* Such a bad girl.\""
                hide 8newalex19
                show 8newalex20
                with dissolve
                " As you walk forward, she gently grabs your legs."
                hide 8newalex20
                show 8newalex21
                with dissolve
                " And starts rubbing her face against your crotch."
                adi "\" I'm so happy to see you.\""
                adi "\" I've waited so long.\""
                hide 8newalex21
                show 8newalex22
                with dissolve
                adi "\" Are you happy to see me?\""
                p "\" Ugh!\""
                p "\" No.\""
                hide 8newalex22
                show 8newalex23
                with dissolve
                " You go into the room, and she follows you on all fours."
                p "\" At least you know your place.\""
                adi "\" Yes, sir.\""
                hide 8newalex23
                show 8newalex24
                with dissolve
                p "\" Aghh...\""
                p "\" I've had a hell of a day.\""
                p "\" Confortable couch.\""
                hide 8newalex24
                show 8newalex25
                with dissolve
                adi "\" I have a way to make you feel better.\""
                p "\" Let me guess. Orally?\""
                adi "\" Well?\""
                p "\" Unrepentant slut.\""
                p "\" Hmmm...\""
                p "\" Rub my feet, and we'll see.\""
                hide 8newalex25
                show 8newalex26
                with dissolve
                " She takes off your shoes and starts rubbing your feet."
                p "\" Ahh...\""
                adi "\" You like it?\""
                p "\" Shut up, and don't stop.\""
                adi "\" Yes, sir.\""
                hide 8newalex26
                show 8newalex27
                with dissolve
                " She seems completely focused on her task."
                adi "\" Want to hear about how my day went?\""
                p "\" Why would I want to do that?\""
                adi "\" I don't know.\""
                hide 8newalex27
                show 8newalex28
                with dissolve
                " She takes your foot and starts rubbing it against her chest."
                p "\" Fine. Tell me.\""
                adi "\" We're making a new website.\""
                adi "\" Mr. Smith said it should bring in more people.\""
                p "\" Mr. Smith?\""
                adi "\" My boss.\""
                adi "\" You'll be able to see if a book is available.\""
                p "\" Right. Because with the internet, Amazon, audiobooks and everything else, people will come to you for their copy of Tropic of Cancer.\""
                hide 8newalex28
                show 8newalex29
                with dissolve
                " She kisses your foot."
                adi "\" Mr. Smith says...\""
                p "\" I don't really care what he says.\""
                p "\" That's enough.\""
                hide 8newalex29
                show 8newalex30
                with dissolve
                adi "\" Did you like it?\""
                p "\" Well enough.\""
                adi "\" Will you let me please you now?\""
                hide 8newalex30
                show 8newalex31
                with dissolve
                " You sit forward."
                p "\" Please me?\""
                p "\" And have you been good?\""
                adi "\" Yes.\""
                p "\" Now you lie to me too?\""
                hide 8newalex31
                show 8newalex33
                with dissolve
                p "\" Tell me.\""
                p "\" Did you wait for me by the door like I told you?\""
                adi "\" Yes.\""
                p "\" Look at me.\""
                hide 8newalex33
                show 8newalex32
                with dissolve
                p "\" Don't lie now.\""
                adi "\" I sometimes came in here and sat on the couch.\""
                p "\" I see.\""
                p "\" And why did you lie?\""
                adi "\" I don't know.\""
                p "\" You don't know. *Hummph!*\""
                p "\" Turn around.\""
                hide 8newalex32
                show 8newalex34
                with dissolve
                adi "\" Like this?\""
                p "\" Bend forward!\""
                hide 8newalex34
                show 8newalex35
                with dissolve
                p "\" Good.\""
                hide 8newalex35
                show 8newalex36
                with dissolve
                p "\" What am I to do with you?\""
                p "\" Huh?\""
                adi "\" I don't know.\""
                hide 8newalex36
                show 8newalex37
                with dissolve
                " You raise the bottom of her nightie and grab ahold of her ass."
                " It feels firm and muscular under your touch."
                p "\" Lying little girl.\""
                hide 8newalex37
                show 8newalex38
                with dissolve
                adi "\" I'm sorry.\""
                p "\" Sorry for what?\""
                adi "\" For lying.\""
                p "\" And what else?\""
                adi "\" For being disobedient.\""
                p "\" Not yet you're not.\""
                hide 8newalex38
                show 8newalex39
                with dissolve
                " You pull your hand back."
                hide 8newalex39
                show 8newalex40
                with dissolve
                " And bring it back down. Perhaps harder than you thought you would."
                hide 8newalex40
                show 8newalex41
                with dissolve
                adi "\" Aghhh...\""
                hide 8newalex41
                show 8newalex39
                with dissolve
                hide 8newalex39
                show 8newalex40
                with dissolve
                "And again."
                show 8newalex39
                with dissolve
                hide 8newalex39
                show 8newalex40
                with dissolve
                "And again."
                show 8newalex39
                with dissolve
                hide 8newalex39
                show 8newalex40
                with dissolve
                "And again."
                hide 8newalex40
                show 8newalex42
                with dissolve
                " Til her ass turns bright red."
                hide 8newalex42
                show 8newalex43
                with dissolve
                adi "\" Thank you.\""
                adi "\" Thank you for the instruction, sir.\""
                p "\" You're welcome.\""
                p "\" And I have to say. Despite being a little liar, at least you know how to take instruction.\""
                hide 8newalex43
                show 8newalex44
                with dissolve
                adi "\" Thank you.\""
                p "\" Come here.\""
                hide 8newalex44
                show 8newalex45
                with dissolve
                " She stands up, and you give her a hug."
                adi "\" Thank you for being so patient.\""
                p "\" I can be patient if you put in the effort.\""
                p "\" If not...\""
                hide 8newalex45
                show 8newalex46
                with dissolve
                adi "\" May I...\""
                adi "\" May I please you now?\""
                p "\" You think you've earned it?\""
                adi "\" No. But...\""
                p "\" But?\""
                adi "\" But I thought you might let me...\""
                p "\" *Sigh*\""
                hide 8newalex46
                show 8newalex45
                with dissolve
                p "\" Very well.\""
                p "\" You promise to be good from now on?\""
                adi "\" Yes, sir.\""
                p "\" *Sigh*\""
                p "\" You may take down my pants then.\""
                hide 8newalex45
                show 8newalex47
                with dissolve
                " She gets on her knees and pulls down your pants."
                adi "\" Ohh...\""
                adi "\" Is it all for me?\""
                " You had to stifle a laugh."
                p "\" If you promise to be good.\""
                adi "\" Oh, I will.\" She says. But you can hear a trace of her own amusement in her voice."
                hide 8newalex47
                show 8newalex48
                with dissolve
                " She starts flicking her tongue around the tip of your dick."
                p "\" Good, girl.\""
                hide 8newalex48
                scene adiblow animated with fade:
                    "9a1.webp"
                    pause 0.05
                    "9a2.webp"
                    pause 0.05
                    "9a3.webp"
                    pause 0.05
                    "9a4.webp"
                    pause 0.05
                    "9a5.webp"
                    pause 0.05
                    "9a6.webp"
                    pause 0.05
                    "9a7.webp"
                    pause 0.05
                    "9a8.webp"
                    pause 0.05
                    "9a9.webp"
                    pause 0.05
                    "9a10.webp"
                    pause 0.05
                    "9a11.webp"
                    pause 0.05
                    "9a12.webp"
                    pause 0.05
                    "9a13.webp"
                    pause 0.05
                    "9a14.webp"
                    pause 0.05
                    "9a15.webp"
                    pause 0.05
                    "9a16.webp"
                    pause 0.05
                    "9a17.webp"
                    pause 0.05
                    "9a18.webp"
                    pause 0.05
                    "9a19.webp"
                    pause 0.05
                    "9a20.webp"
                    pause 0.05
                    "9a21.webp"
                    pause 0.05
                    "9a22.webp"
                    pause 0.05
                    "9a23.webp"
                    pause 0.05
                    "9a24.webp"
                    pause 0.05
                    "9a25.webp"
                    pause 0.05
                    "9a26.webp"
                    pause 0.05
                    "9a27.webp"
                    pause 0.05
                    "9a28.webp"
                    pause 0.05
                    "9a29.webp"
                    pause 0.05
                    "9a30.webp"
                    pause 0.05
                    repeat
                adi "\" Mmmmm...\""
                p "\" Good, girl.\""
                $ renpy.pause ()
                show 8newalex49
                with dissolve
                adi "\" See, sir?\""
                adi "\" I can be good.\""
                p "\" Did I tell you to stop?\""
                hide 8newalex49
                scene adiblow animated with fade:
                    "9a1.webp"
                    pause 0.05
                    "9a2.webp"
                    pause 0.05
                    "9a3.webp"
                    pause 0.05
                    "9a4.webp"
                    pause 0.05
                    "9a5.webp"
                    pause 0.05
                    "9a6.webp"
                    pause 0.05
                    "9a7.webp"
                    pause 0.05
                    "9a8.webp"
                    pause 0.05
                    "9a9.webp"
                    pause 0.05
                    "9a10.webp"
                    pause 0.05
                    "9a11.webp"
                    pause 0.05
                    "9a12.webp"
                    pause 0.05
                    "9a13.webp"
                    pause 0.05
                    "9a14.webp"
                    pause 0.05
                    "9a15.webp"
                    pause 0.05
                    "9a16.webp"
                    pause 0.05
                    "9a17.webp"
                    pause 0.05
                    "9a18.webp"
                    pause 0.05
                    "9a19.webp"
                    pause 0.05
                    "9a20.webp"
                    pause 0.05
                    "9a21.webp"
                    pause 0.05
                    "9a22.webp"
                    pause 0.05
                    "9a23.webp"
                    pause 0.05
                    "9a24.webp"
                    pause 0.05
                    "9a25.webp"
                    pause 0.05
                    "9a26.webp"
                    pause 0.05
                    "9a27.webp"
                    pause 0.05
                    "9a28.webp"
                    pause 0.05
                    "9a29.webp"
                    pause 0.05
                    "9a30.webp"
                    pause 0.05
                    repeat
                adi "\" Mmmmm...\""
                p "\" That's it...\""
                p "\" Good girl.\""
                p "\" Faster, now.\""
                $ renpy.pause ()
                scene adiblow animated with fade:
                    "9a1.webp"
                    pause 0.03
                    "9a2.webp"
                    pause 0.03
                    "9a3.webp"
                    pause 0.03
                    "9a4.webp"
                    pause 0.03
                    "9a5.webp"
                    pause 0.03
                    "9a6.webp"
                    pause 0.03
                    "9a7.webp"
                    pause 0.03
                    "9a8.webp"
                    pause 0.03
                    "9a9.webp"
                    pause 0.03
                    "9a10.webp"
                    pause 0.03
                    "9a11.webp"
                    pause 0.03
                    "9a12.webp"
                    pause 0.03
                    "9a13.webp"
                    pause 0.03
                    "9a14.webp"
                    pause 0.03
                    "9a15.webp"
                    pause 0.03
                    "9a16.webp"
                    pause 0.03
                    "9a17.webp"
                    pause 0.03
                    "9a18.webp"
                    pause 0.03
                    "9a19.webp"
                    pause 0.03
                    "9a20.webp"
                    pause 0.03
                    "9a21.webp"
                    pause 0.03
                    "9a22.webp"
                    pause 0.03
                    "9a23.webp"
                    pause 0.03
                    "9a24.webp"
                    pause 0.03
                    "9a25.webp"
                    pause 0.03
                    "9a26.webp"
                    pause 0.03
                    "9a27.webp"
                    pause 0.03
                    "9a28.webp"
                    pause 0.03
                    "9a29.webp"
                    pause 0.03
                    "9a30.webp"
                    pause 0.03
                    repeat
                " She increases the pace, making incresingly slurping noises as she does."
                adi "\" *Slurp* *Slurp* *Slurp*\""
                p "\" Yes.\""
                p "\" I'm gonna...\""
                p "\" Yes.\""
                $ renpy.pause ()
                show 8newalex50
                with dissolve
                " You pull out your dick and cum all over her face."
                p "\" Ahhh...\""
                show 8newalex51
                with dissolve
                " She smiles up at you with a mouth full of cum."
                p "\" Good girl.\""
                hide 8newalex51
                show 8newalex52
                with dissolve
                " You pull your pants back up and sit down on the couch."
                p "\" I'm going to take a nap now.\""
                adi "\" Aha.\""
                p "\" You stay right there.\""
                p "\" Don't wash your face. You understand me?\""
                adi "\" I wouldn't.\""
                p "\" Good.\""
                hide 8newalex52
                show 8newalex53
                with dissolve
                " You lie down on the couch to close your eyes for a bit."
                p "\" *Sigh*\""
                hide 8newalex53
                show 8newalex54
                with dissolve
                " You turn around to see her obediently kneeling there."
                " Your cum slowly dripping down her face."
                hide 8newalex54
                show 8newalex55
                with dissolve
                p "\" Alright.\""
                hide 8newalex55
                show 8newalex56
                with dissolve
                adi "\" Sir?\""
                p "\" Alright, you can go wash your face.\""
                p "\" And then crawl in here with me.\""
                adi "\" Thank you.\" She whispers."
                hide 8newalex56
                show 8newalex57
                with dissolve
                " She runs to the bathroom to wash her face, and comes right back with a smile."
                hide 8newalex57
                show 8newalex58
                with dissolve
                " Crawling into your arms she seems utterly content."
                " But after a few minutes you feel compelled to say..."
                p "\" You're really into this aren't you.\""
                " You notice that her voice goes a couple of octaves lower when she answers."
                " The girly tone of her submissive persona has vanished."
                adi "\" Only way I can really get off.\""
                p "\" Why?\""
                adi "\" I don't really feel like talking about it.\""
                p "\" If you say so.\""
                p "\" But I'm going to get you every time with not waiting for me by the door.\""
                adi "\" That's the point.\""
                adi "\" There can be no sweet without sour.\""
                adi "\" And no confort without punishment.\""
                hide 8newalex58
                show blackscreen
                with dissolve
                " You close your eyes and take a nap."
                "..."
                "... ..."
                hide blackscreen
                show 8newalex58
                with dissolve
                " You open your eyes a few hours later to find she hasn't moved an inch."
                " As if she didn't want to disturb you."
                p "\" I have to go.\""
                hide 8newalex58
                show 8newalex59
                with dissolve
                " She clings to you as you stand up, not wanting to let you go."
                adi "\" Please don't go sir.\""
                " Her voice is back to the childish tone from earlier."
                p "\" I'll come back if you're good.\""
                adi "\" Promise?\""
                p "\" Promise.\""
                hide 8newalex59
                show 8newalex60
                with dissolve
                " You put her down by the door as you leave."
                p "\" You wait for me right here.\""
                adi "\" Right here.\""
                p "\" Good girl.\""
                $ renpy.end_replay()
                jump ep8cont2

label ep8homeend:
                scene 8newalex61
                with dissolve
                " You get to your place, and take a nap til it's time to go pick up the girls."
                jump ep8cont2

label ep8cont2:
                scene back1
                with dissolve
                show 8newalex63
                with dissolve
                " You go to the school and pick up Alexandra and Izzy."
                p "\" How are you girls?\""
                a "\" Well enough.\""
                i "\" Fine.\""
                if ep7helpfromalex == True:
                    hide 8newalex63
                    show 8newalex62
                    with dissolve
                    a "\" What about you?\""
                    a "\" Is that thing taken care of?\""
                    a "\" With the bag?\""
                    i "\" What?\""
                    p "\" He'll send someone over.\""
                    p "\" I'll keep you updated.\""
                    jump ep8cont3

                else:
                    jump ep8cont3

label ep8cont3:
                if izzyin == True:
                    jump ep8izzyin1
                else:
                    jump ep8noizzy1

label ep8izzyin1:
                scene back1
                with dissolve
                show 8newalex64
                with dissolve
                a "\" So, you two had your big date.\""
                a "\" Didn't bring me anything, I noticed.\""
                a "\" Not even a doggie bag.\""
                p "\" That's because we never thought of you.\""
                p "\" Alex who?\""
                hide 8newalex64
                show 8newalex65
                with dissolve
                a "\" Ass!\""
                a "\" Trying to make me feel bad?\""
                p "\" A little.\""
                hide 8newalex65
                show 8newalex66
                with dissolve
                i "\" You'll have your time together today.\""
                i "\" Can you drop me off at my place?\""
                p "\" Why?\""
                i "\" I wanna spend the evening with Momma.\""
                hide 8newalex66
                show 8newalex68
                with dissolve
                a "\" Everything ok?\""
                i "\" Yes.\""
                i "\" She's better than most days.\""
                i "\" Almost all there.\""
                i "\' I wanna spend some time with her while she's like this.\""
                i "\" Know what I mean?\""
                a "\" Of course.\""
                hide 8newalex68
                show 8newalex69
                with dissolve
                i "\" You two be good now.\""
                i "\" Don't get into any mischief.\""
                hide 8newalex69
                show 8newalex68
                with dissolve
                a "\" You know me better than that.\""
                i "\" I do.\""
                i "\" It was a bit of a jab, actually.\""
                a "\" Well, someone has to be the adult in this relationship.\""
                i "\" I know.\""
                hide 8newalex68
                show 8newalex69
                with dissolve
                i "\" Can you drop me off?\""
                p "\" Of course.\""
                jump ep8cont4

label ep8noizzy1:
                scene back1
                with dissolve
                show 8newalex64
                with dissolve
                a "\" So, what should we get up to tonight.\""
                a "\" Snooker match though, I have to see that with Dad.\""
                hide 8newalex64
                show 8newalex66
                with dissolve
                i "\" You'll have your time together today.\""
                i "\" Can you drop me off at my place?\""
                p "\" Why?\""
                i "\" I wanna spend the evening with Momma.\""
                hide 8newalex66
                show 8newalex68
                with dissolve
                a "\" Everything ok?\""
                i "\" Yes.\""
                i "\" She's better than most days.\""
                i "\" Almost all there.\""
                i "\' I wanna spend some time with her while she's like this.\""
                i "\" Know what I mean?\""
                a "\" Of course.\""
                hide 8newalex68
                show 8newalex70
                with dissolve
                i "\" Besides. It's not like you're going to miss me.\" She whispers."
                a "\" What?\""
                i "\" Nothing.\""
                hide 8newalex70
                show 8newalex69
                with dissolve
                i "\" Can you drop me off?\""
                p "\" Of course.\""
                jump ep8cont4

label ep8cont4:
                scene 8newalex71
                with dissolve
                " You drop Izzy off at her place, with Alex giving her a hug before you go."
                show 8newalex75
                with dissolve
                " As you leave you notice a familiar car in front of her apartment."
                p "\" Hmmm...\""
                a "\" What?\""
                p "\" I think I saw that car before.\""
                p "\" Can't remember where.\""
                a "\" You know how many cars like that must be in the city?\""
                a "\" It's probably your imagination.\""
                a "\" Let's just go.\""
                hide 8newalex75
                show back1
                with dissolve
                show 8newalex72
                with dissolve
                if ep7helpfromalex == True:
                    a "\" I've been thinking about how to deal with your police problem.\""
                    p "\" Yes?\""
                    a "\" I've learned a few things from my Dad over the years.\""
                    a "\" The direct approach, I think would be wrong.\""
                    a "\" We need to find out more about her. Her secrets.\""
                    p "\" Blackmail?\""
                    hide 8newalex72
                    show 8newalex73
                    with dissolve
                    a "\" God, no!\""
                    a "\" Like I said. No direct approach.\""
                    a "\" But we could get her distracted.\""
                    a "\" Brutality complaints. Bribery accusations.\""
                    p "\" What if she's clean?\""
                    a "\" No one is completely clean.\""
                    a "\" But it doesn't matter anyway.\""
                    a "\" As long as we can smear her.\""
                    a "\" Get her reassigned.\""
                    a "\" Drag her through the courts.\""
                    a "\" Investigations. Create activity.\""
                    p "\" That's pretty underhanded.\""
                    hide 8newalex73
                    show 8newalex72
                    with dissolve
                    a "\" I care about those I love, Puppy.\""
                    a "\" The rest of the world can go fuck itself.\""
                    p "\" Glad I'm on the other side of the equation.\""
                    a "\" I'll talk to my Uncle.\""
                    jump ep8cont5

                else:
                    a "\" So, ready for a evening of watching snooker?\""
                    p "\" I might actually have to leave tonight.\""
                    hide 8newalex72
                    show 8newalex73
                    with dissolve
                    a "\" Leave?\""
                    p "\" I might have some work to do.\""
                    hide 8newalex73
                    show 8newalex72
                    with dissolve
                    a "\" Just like my Dad.\""
                    p "\" Sorry.\""
                    a "\" Don't be.\""
                    a "\" If I don't understand, who will?\""
                    jump ep8cont5

label ep8cont5:
                scene 8newalex74
                with dissolve
                " You drive Alex home."
                a "\" I never asked you.\""
                a "\" What's your preferred TV watching food?\""
                a "\" Popcorn? Chips?\""
                show 8newalex76
                with dissolve
                " You step forward and kiss her."
                hide 8newalex76
                show 8newalex77
                with dissolve
                a "\" Hmmm...\""
                a "\" Tongue?\""
                a "\" That's your favorite?\""
                p "\" I wouldn't say that. But it will do for now.\""
                hide 8newalex77
                show 8newalex78
                with dissolve
                " She steps forward now and shoves her tongue into your mouth."
                b "\" Ahem!\""
                hide 8newalex78
                show 8newalex79
                with dissolve
                b "\" Am I interrupting?\""
                hide 8newalex79
                show 8newalex80
                with dissolve
                a "\" Dad?\""
                a "\" What the hell are you doing out of bed?\""
                a "\" And you're dressed too.\""
                hide 8newalex80
                show 8newalex81
                with dissolve
                a "\" Get back in the bedroom.\""
                b "\" I have work to do.\""
                a "\" Work?\""
                a "\" What kind of work?\""
                a "\" You're sick.\""
                b "\" I'm well enough.\""
                hide 8newalex81
                show 8newalex82
                with dissolve
                a "\" Whatever it is, you can send Puppy.\""
                a "\" You can trust him.\""
                a "\" Now, get back in there!\""
                b "\" Enough, Alex!\""
                hide 8newalex82
                show 8newalex83
                with dissolve
                b "\" Ready to go?\" He asks you."
                p "\" Sure boss.\""
                b "\" Good.\""
                hide 8newalex83
                show 8newalex84
                with dissolve
                a "\" Sure, don't mind me.\""
                a "\" I'll just be here ready to take care of you when you get the sniffles or get stabbed.\""
                b "\" Stabbed?\""
                a "\" I was just speaking hypothetically.\""
                hide 8newalex84
                show 8newalex85
                with dissolve
                " As you walk away, she says..."
                a "\" Be careful, ok?\""
                a "\" Both of you.\""
                p "\" Of course.\""
                hide 8newalex85
                show back1
                with dissolve
                show 8newalex86
                with dissolve
                b "\" She frets, that girl.\""
                p "\" Where are we going?\""
                hide 8newalex86
                show 8newalex87
                with dissolve
                b "\" *Cough* *Cough* *Cough*\""
                hide 8newalex87
                show 8newalex86
                with dissolve
                b "\" Damn it!\""
                p "\" You ok?\""
                b "\" I'm fine. Fine.\""
                b "\" We're going to Dima's.\""
                b "\" Managed to fuck it all up.\""
                p "\" What?\""
                b "\" He was supposed to meet with someone.\""
                b "\" Well, he did do that.\""
                b "\" Words were exchanged, and he managed to slap the kid around.\""
                p "\" Is that really a problem?\""
                hide 8newalex86
                show 8newalex88
                with dissolve
                b "\" You don't know the kid's Mother.\""
                p "\" His mother?\""
                hide 8newalex88
                show 8newalex86
                with dissolve
                b "\" Yeah.\""
                b "\" If the Devil had a cunt, it would be her.\""
                hide 8newalex86
                show 8newalex89
                with dissolve
                " When you arive at Dima's office you find him pacing around the room."
                b "\" Dimitri!\""
                hide 8newalex89
                show 8newalex90
                with dissolve
                di "\" Boss, I know what you're going to say.\""
                b "\" Do you?\""
                di "\" It wasn't my fault.\""
                b "\" Then who's fault is it?\""
                b "\" You know who his Mother is, right?\""
                hide 8newalex90
                show 8newalex91
                with dissolve
                di "\" *Gulp*\""
                di "\" I do.\""
                hide 8newalex91
                show 8newalex92
                with dissolve
                b "\" Then?\""
                b "\" If I had any sense at all, I'd feed you to her.\""
                hide 8newalex92
                show 8newalex91
                with dissolve
                di "\" Boss...\""
                hide 8newalex91
                show 8newalex92
                with dissolve
                b "\" Shut up!\""
                b "\" Now, me and [player_name] will go see if we can't clean this up and still let you keep your head.\""
                hide 8newalex92
                show 8newalex93
                with dissolve
                di "\" I'm sorry, boss.\""
                b "\" Shut up!\""
                hide 8newalex93
                show 8newalex94
                with dissolve
                " As you leave, you think you hear Dima mutter under his breath."
                di "\" Of course he's taking his Daughter's pet.\""
                hide 8newalex94
                show back1
                with dissolve
                show 8newalex86
                with dissolve
                " Back in the car Boris says..."
                b "\" We have to go meet with this bitch.\""
                b "\" But we're picking up Micha first.\""
                b "\" Just in case we walk in there and see plastic under our feet.\""
                p "\" That bad?\""
                b "\" Trust me. We men get a bad rep when it comes to being bloodthirsty.\""
                p "\" Sure.\""
                p "\" Can I ask more about this woman?\""
                b "\" She owns a few clubs around town.\""
                b "\" Dima was supposed to meet with her Son and see if they can't buy their alcohol from us.\""
                p "\" And words were exchanged.\""
                b "\" Exactly.\""
                p "\" But buying alcohol?\""
                p "\" There's no prohibition that I know of.\""
                b "\" It is if you don't want to pay $14 per gallon in taxes.\""
                p "\" I see.\""
                hide 8newalex86
                show 8newalex96
                with dissolve
                " You stop and pick up Micha."
                mi "\" Boss?\""
                mi "\" [player_name]?\""
                b "\" You heard what Dima did?\""
                mi "\" Yeah.\""
                mi "\" That little shit deserved to be slapped around for as long as he's been breathing.\""
                b "\" That's no excuse.\""
                b "\" Just be ready.\""
                hide 8newalex96
                show 8newalex97
                with dissolve
                mi "\" I'm always ready boss.\""
                hide 8newalex97
                show 8newalex98
                with dissolve
                b "\" That's what I like about you.\""
                hide 8newalex98
                show 8newalex99
                with dissolve
                " You drive according to Boris's directions til you arrive at an expensive looking house."
                b "\" Here we go.\""
                b "\" Just be ready. Both of you.\""
                p "\" No worries chief.\""
                hide 8newalex99
                show 8newalex100
                with dissolve
                " After knocking, a man comes to the door."
                b "\" We're here to see Mrs. Tanya.\""
                m4 "\" Is she expecting you?\""
                b "\" I bet she is.\""
                b "\" New get the fuck out of the way.\""
                m4 "\" Hmmm...\""
                b "\" Do you recognize me?\""
                m4 "\" This way.\""
                hide 8newalex100
                show 8newalex101
                with dissolve
                " He takes you to a small open air enclosure at the back on the house."
                p "\" Jesus.\""
                hide 8newalex101
                show 8newalex102
                with dissolve
                b "\" Tanya.\""
                b "\" We need to talk.\""
                hide 8newalex102
                show 8newalex103
                with dissolve
                ta "\" Boris.\""
                ta "\" Happy to see you.\""
                ta "\" I can only assume you have that little shit tied up in the back of your car.\""
                b "\" No.\""
                hide 8newalex103
                show 8newalex104
                with dissolve
                " She stands up, and the two men follow."
                ta "\" You don't?\""
                b "\" No.\""
                ta "\" Then I don't see what we have to talk about.\""
                hide 8newalex104
                show 8newalex105
                with dissolve
                " She comes forward."
                ta "\" Are you going to offer me someone else's head in exchange?\""
                hide 8newalex105
                show 8newalex111
                with dissolve
                " She looks at you."
                ta "\" Or maybe offer me this one as a toy?\""
                ta "\" You could do worse for an apology.\""
                b "\" This one is my Daughter's boyfriend.\" He almost growls."
                ta "\" Even better.\""
                hide 8newalex111
                show 8newalex105
                with dissolve
                ta "\" So, what will it be.\""
                b "\" Neither.\""
                b "\" I'm here for us to reach a reasonable understanding.\""
                hide 8newalex105
                show 8newalex106
                with dissolve
                m5 "\" Reasonable?\""
                m5 "\" Mrs. Tanya's son was smacked around.\""
                m5 "\" That can only be paid in blood.\""
                hide 8newalex106
                show 8newalex105
                with dissolve
                b "\" Who is this idiot?\""
                hide 8newalex105
                show 8newalex107
                with dissolve
                ta "\" Hush, dear.\""
                ta "\" The men are talking now, yes?\""
                ta "\" Why don't you two boys head inside?\""
                hide 8newalex107
                show 8newalex108
                with dissolve
                " Reluctantly the two men go inside the house."
                hide 8newalex108
                show 8newalex109
                with dissolve
                ta "\" Mmmm...\""
                ta "\" Look at them.\""
                ta "\" How did I get so lucky.\""
                b "\" Are we done with your pets?\""
                b "\" Can we talk now?\""
                hide 8newalex109
                show 8newalex110
                with dissolve
                ta "\" Again. Talk about what?\""
                ta "\" My little chocolate bear may not be bright, but he is right about this.\""
                ta "\" There's only one way this could end.\""
                b "\" You know I can't give up a man over a slap.\""
                hide 8newalex110
                show 8newalex112
                with dissolve
                b "\" Now, I'm open to some other kind of arrangement.\""
                b "\" Something financial, maybe.\""
                hide 8newalex112
                show 8newalex113
                with dissolve
                ta "\" Do I look like a fucking charity case?\""
                b "\" A piece of Dimitry's business?\""
                hide 8newalex113
                show 8newalex114
                with dissolve
                ta "\" If that means a piece of the business between his legs, chopped off and on a silver platter...\""
                ta "\" I might be willing to accept.\""
                hide 8newalex114
                show 8newalex115
                b "\" You're being absurd.\""
                hide 8newalex115
                show 8newalex116
                with dissolve
                ta "\" You've heard what I have to say.\""
                ta "\" Deliver to me what I want, or get ready for the consequences.\""
                b "\" You don't mean that.\""
                ta "\" Are you still here?\""
                b "\" That's your final word?\""
                ta "\" Still here?\""
                hide 8newalex116
                show 8newalex117
                with dissolve
                " As you leave, she looks at you and says..."
                ta "\" I might spare this one.\""
                ta "\" He'd make a pretty little toy.\""
                hide 8newalex117
                show 8newalex119
                with dissolve
                mi "\" That could've went better.\""
                hide 8newalex119
                show 8newalex118
                with dissolve
                b "\" Thank you for your cutting analysis.\""
                b "\" This will likely end bad.\""
                b "\" Drop you off at your place?\""
                hide 8newalex118
                show 8newalex119
                with dissolve
                mi "\" Sure.\""
                hide 8newalex119
                show 8newalex120
                with dissolve
                " You drop off Micha, and drive Boris home."
                if ep7robbery == True:
                    jump ep8robcont2
                else:
                    b "\" Alright.\""
                    b "\" I'm heading back to bed.\""
                    b "\" Keep your eyes extra open from now on.\""
                    p "\" Got it.\""
                    jump ep8cont6

label ep8robcont2:
                scene 8newalex120
                with dissolve
                b "\" Alright.\""
                b "\" I'm heading back to bed.\""
                b "\" Keep your eyes extra open from now on.\""
                p "\" Got it.\""
                p "\" But I have to go take care of something tonight.\""
                b "\" What?\""
                p "\" Things at the agency.\""
                p "\" Nothing important.\""
                b "\" Fine.\""
                b "\" But hurry up.\""
                p "\" I will.\""
                show 8newalex121
                with dissolve
                " You go back to the laundry, and your boys are still there."
                hide 8newalex121
                show back
                with dissolve
                show 8newalex122
                with dissolve
                " You get inside the van."
                p "\" Anything new?\""
                ja "\" Definitely more going on than laundry in there.\""
                p "\" You think the game is tonight?\""
                ja "\" Yeah. But I can't be sure.\""
                ja "\" You want us to stake it out tomorrow? See the difference?\""
                p "\" No time.\""
                p "\" There's a bit of a rush on this.\""
                p "\" Let's wait for it to get dark.\""
                " A couple of hours later, the sun goes down."
                hide 8newalex122
                show 8newalex123
                with dissolve
                ja "\" Ready when you are.\""
                p "\" The hell is that?\""
                ja "\" Thought it would be better to cover our faces.\""
                hide 8newalex123
                show 8newalex124
                with dissolve
                hu "\" We got you one too.\""
                p "\" Give it to me.\""
                hide 8newalex124
                show 8newalex123
                with dissolve
                p "\" Guns?\""
                hide 8newalex123
                show 8newalex127
                with dissolve
                ja "\" Got that covered.\""
                p "\" Good.\""
                hide 8newalex127
                show 8newalex125
                with dissolve
                p "\" Alright.\""
                p "\" No use in delaying.\""
                p "\" Let's go.\""
                hide 8newalex125
                show 8newalex128
                with dissolve
                " You all get out of the car, and bust inside the laundry shop."
                hide 8newalex128
                show 8newalex129
                with dissolve
                m6 "\" Good thing we're in a laundry.\""
                m6 "\" Because I'm really about to take you to the cleaners, kid.\""
                kid3 "\" Keep talking, old man.\""
                hu "\" Evening, gents.\""
                hide 8newalex129
                show 8newalex130
                with dissolve
                hu "\" Now, you all just stay calm, and you might just get out of here.\""
                kid3 "\" The fuck are you people?\""
                hu "\" I think we're the winners.\""
                p "\" Get the cash.\""
                hide 8newalex130
                show 8newalex131
                with dissolve
                kid3 "\" You look like the boss.\""
                kid3 "\" Who are you.\""
                kid3 "\" Homo Hood and his fairy men?\""
                p "\" Shut up!\""
                hide 8newalex131
                show 8newalex132
                with dissolve
                kid4 "\" Shut up Al!\""
                hide 8newalex132
                show 8newalex131
                with dissolve
                p "\" Yeah.\""
                p "\" Shut up, Al!\""
                p "\" It's past your bedtime anyway.\""
                hide 8newalex131
                show 8newalex133
                with dissolve
                p "\" You!\""
                p "\" Hand it over.\""
                " The man refuses to look at you."
                m7 "\" Hand over what?\""
                hide 8newalex133
                show 8newalex134
                with dissolve
                ja "\" Don't get cute now.\""
                ja "\" Be a good boy and hand it over.\""
                ja "\" They pay you enough to get shot?\""
                hide 8newalex134
                show 8newalex135
                with dissolve
                kid3 "\" You know who my Father is, dumbass?\""
                kid3 "\" Huh?\""
                kid3 "\" Any idea who I am?\""
                p "\" Shut up.\""
                hide 8newalex135
                show 8newalex136
                with dissolve
                kid4 "\" Al!\""
                kid4 "\" Shut up, man!\""
                hide 8newalex136
                show 8newalex137
                with dissolve
                m7 "\" Here!\""
                " He throws a bag in front of you."
                hide 8newalex137
                show 8newalex138
                with dissolve
                kid3 "\" I'll find you, jackass.\""
                kid3 "\" Me and my Dad will find you.\""
                kid4 "\" Damn it.\""
                kid3 "\" I'll cut your balls off.\""
                kid3 "\" And fuck your bitch til she moans.\""
                p "\" What did you say?\""
                hide 8newalex138
                show 8newalex139
                with dissolve
                kid3 "\" I'll fuck your slut til she moans.\""
                hide 8newalex139
                show 8newalex140
                with dissolve
                " Bang!"
                kid3 "\" Agh...\""
                kid3 "\" Till she moans...\""
                hide 8newalex140
                show 8newalex141
                with dissolve
                hide 8newalex141
                show 8newalex142
                with dissolve
                " *BANG!*"
                hide 8newalex142
                show 8newalex141
                with dissolve
                hide 8newalex141
                show 8newalex142
                with dissolve
                " *BANG!*"
                hide 8newalex142
                show 8newalex141
                with dissolve
                hide 8newalex141
                show 8newalex142
                with dissolve
                " *BANG!*"
                hide 8newalex142
                show 8newalex143
                with dissolve
                hide 8newalex143
                show 8newalex144
                with dissolve
                " *BANG!*"
                hide 8newalex144
                show 8newalex143
                with dissolve
                hide 8newalex143
                show 8newalex144
                with dissolve
                " *BANG!*"
                hide 8newalex144
                show 8newalex143
                with dissolve
                hide 8newalex143
                show 8newalex144
                with dissolve
                " *BANG!*"
                hide 8newalex144
                show 8newalex143
                with dissolve
                hide 8newalex143
                show 8newalex144
                with dissolve
                " *BANG!*"
                hide 8newalex144
                show 8newalex145
                with dissolve
                kid4 "\" Jesus, man...\""
                hide 8newalex145
                show 8newalex146
                with dissolve
                " He slumps down to the floor."
                p "\" Little fucking cunt!\""
                hide 8newalex146
                show 8newalex147
                with dissolve
                ja "\" Let's go man, Jesus.\""
                ja "\" We got what we wanted.\""
                ja "\" Let's go.\""
                p "\" Little shit.\""
                hide 8newalex147
                show back1
                with dissolve
                show 8newalex148
                with dissolve
                " You rush back to the car."
                ja "\" Christ man!\""
                ja "\" What was that?\""
                p "\" Shut up!\""
                ja "\" Fuck!\""
                ja "\" You think he's dead?\""
                p "\" I don't care.\""
                p "\" Just drive.\""
                hide 8newalex148
                show 8newalex149
                with dissolve
                " You head back to your place."
                ja "\" At least we have the money.\""
                hide 8newalex149
                show 8newalex150
                with dissolve
                hu "\" He he...\""
                hu "\" I think I heard his neck snap.\""
                hide 8newalex150
                show 8newalex151
                with dissolve
                ja "\" That ain't funny man.\""
                ja "\" All he did was talk some shit.\""
                hide 8newalex151
                show 8newalex150
                with dissolve
                hu "\" He he...\""
                hu "\" Loved it boss.\""
                hide 8newalex150
                show 8newalex151
                with dissolve
                ja "\" Fucking psycho.\""
                hide 8newalex151
                show 8newalex152
                with dissolve
                hu "\" So, how do we split the cash?\""
                " You only need a small part for Marcello."
                " Do you let them split the rest?"
                call screen screen45

label ep8small:
                scene 8newalex152
                with dissolve
                $ boyspts = 1
                p "\" I just need a small part of it.\""
                p "\" Just put aside 500k for me and you two split the rest.\""
                p "\" Make sure you bring it to me tomorrow at the agency.\""
                show 8newalex154
                with dissolve
                ja "\" Really?\""
                p "\" I need what I need.\""
                p "\" Now, don't make me change my mind.\""
                hide 8newalex154
                show 8newalex153
                with dissolve
                hu "\" Thanks boss.\""
                hide 8newalex153
                show 8newalex156
                with dissolve
                p "\" I gotta go.\""
                p "\" You two handle this.\""
                ja "\" Sure boss.\""
                hu "\" See you tomorrow.\""
                p "\" Leave the keys under the mat when you leave.\""
                ja "\" Got it.\""
                hide 8newalex156
                show 8newalex157
                with dissolve
                " You head back to the villa."
                p "\" Alex?\""
                jump ep8cont6

label ep8split:
                scene 8newalex152
                with dissolve
                p "\" We split it evenly.\""
                p "\" Make sure you bring my share to me tomorrow at the agency.\""
                show 8newalex155
                with dissolve
                ja "\" Fair.\""
                ja "\" We'll do that.\""
                hide 8newalex155
                show 8newalex153
                with dissolve
                hu "\" Thanks boss.\""
                hide 8newalex153
                show 8newalex156
                with dissolve
                p "\" I gotta go.\""
                p "\" You two handle this.\""
                ja "\" Sure boss.\""
                hu "\" See you tomorrow.\""
                p "\" Leave the keys under the mat when you leave.\""
                ja "\" Got it.\""
                hide 8newalex156
                show 8newalex157
                with dissolve
                " You head back to the villa."
                p "\" Alex?\""
                jump ep8cont6

label ep8cont6:
                scene 8newalex158
                with dissolve
                " You find Alexandra almost nodding off in front of the TV."
                p "\" Alex?\""
                a "\" Huh?\""
                show 8newalex159
                with dissolve
                a "\" Hey.\""
                p "\" Sorry, but I had to go.\""
                a "\" I know.\""
                a "\" It's just something I have to get used to.\""
                a "\" We all have our part.\""
                hide 8newalex159
                show 8newalex160
                with dissolve
                a "\" Now come over here for a cuddle.\""
                p "\" Your Dad?\""
                a "\" Don't worry about it.\""
                a "\" Just come here.\""
                hide 8newalex160
                show 8newalex161
                with dissolve
                " You get under the covers with her."
                hide 8newalex161
                show 8newalex162
                with dissolve
                a "\" Is it too warm for you?\""
                a "\" We can put aside the blanket...\""
                p "\" It's fine.\""
                hide 8newalex162
                show 8newalex163
                with dissolve
                p "\" Snooker.\""
                a "\" Yeah.\""
                p "\" Can you even see with the candles?\""
                a "\" It's not about the games.\""
                a "\" It's about the ritual with my Dad.\""
                a "\" Want me to move them?\""
                p "\" I don't care.\""
                hide 8newalex163
                show 8newalex164
                with dissolve
                " You kiss her neck."
                a "\" Don't.\""
                p "\" *Sigh*\""
                a "\" I meant, don't stop.\""
                p "\" Bitch.\""
                a "\" He he...\""
                hide 8newalex164
                show 8newalex165
                with dissolve
                p "\" Mr. Boris is going to come to watch it with you, yes?\""
                a "\" It's our thing.\""
                p "\" Maybe I should leave.\""
                a "\" No.\""
                a "\" You're part of it now.\""
                a "\" He needs to accept that.\""
                p "\" It's my neck on the line.\""
                a "\" No, it's not.\""
                hide 8newalex165
                show 8newalex166
                with dissolve
                " Boris walks in."
                b "\" Huh!\""
                b "\" [player_name] likes snooker too?\""
                a "\" No.\""
                a "\" He just likes to be with me.\""
                hide 8newalex166
                show 8newalex167
                with dissolve
                b "\" I thought this was our time.\""
                a "\" It is.\""
                a "\" OUR time.\""
                a "\" Have a seat.\""
                hide 8newalex167
                show 8newalex168
                with dissolve
                " He sits down and watches the match. meanwhile you watch Alex, and Alex is nodding off."
                hide 8newalex168
                show 8newalex169
                with dissolve
                " It isn't long before she's sleeping restfully."
                hide 8newalex169
                show 8newalex170
                with dissolve
                b "\" You'd better take her to her room.\""
                b "\" She'll sleep more soundly on a bed.\""
                p "\" Sure.\""
                b "\" But then you come right back here.\""
                b "\" Hear me?\""
                p "\" Yes.\""
                hide 8newalex170
                show 8newalex171
                with dissolve
                " You slightly nuzzle your nose against the back of her neck."
                b "\" *Groan*\""
                p "\" Alex?\""
                p "\" Alex, I'm taking you to your room.\""
                a "\" Mmmmm...\""
                a "\" Carry me?\""
                b "\" *Sigh*\""
                p "\" Sure.\""
                hide 8newalex171
                show 8newalex172
                with dissolve
                " You pick her up."
                b "\" Right back here, you understand?\""
                p "\" Got it boss.\""
                hide 8newalex172
                show 8newalex173
                with dissolve
                " You carry her upstairs, and she just slumps on the bed."
                p "\" He he...\""
                a "\" What?\""
                p "\" I've never seen a more graceless pose.\""
                p "\" It's like you're a dead frog.\""
                hide 8newalex173
                show 8newalex174
                with dissolve
                a "\" Ass.\""
                a "\" You should be telling me that I'm pretty regardless.\""
                p "\" Really?\""
                a "\" No, actually.\""
                a "\" I prefer the truth.\""
                p "\" Well, I'd better go.\""
                hide 8newalex174
                show 8newalex175
                with dissolve
                a "\" Wait!\""
                a "\" Come over here for a minute.\""
                p "\" Yes?\""
                hide 8newalex175
                show 8newalex176
                with dissolve
                " You get on top of her."
                " She opens her legs willingly enough, but you doubt it will go further."
                a "\" He he...\""
                a "\" I didn't mean that.\""
                p "\" Then what did you mean?\""
                a "\" I want to tell you something.\""
                hide 8newalex176
                show 8newalex177
                with dissolve
                a "\" You're going back down to Dad, right?\""
                p "\" Yes.\""
                a "\" Well, after the match is over, make sure you come here and not to your room.\""
                hide 8newalex177
                show 8newalex179
                with dissolve
                a "\" We'll just be sleeping, now.\""
                a "\" But make sure Dad sees you coming here.\""
                p "\" Causing drama?\""
                a "\" More like conditioning.\""
                a "\" He's gotten used to you being around the house.\""
                a "\" Sleeping over here.\""
                a "\" Now he needs to get used to you sleeping in my room.\""
                a "\" And eventually...\""
                p "\" Plowing his Daughter?\""
                a "\" Making sweet love to his Daughter, ASS.\""
                p "\" Like the frog and the warm water?\""
                a "\" That's not true. It's an urban myth, but yes.\""
                p "\" Do you manipulate everyone.\""
                a "\" I like to think of it as making things run smoothly.\""
                hide 8newalex179
                show 8newalex178
                with dissolve
                " She kisses you."
                hide 8newalex178
                show 8newalex177
                with dissolve
                a "\" Now go bond, or whatever.\""
                p "\" He he...\""
                p "\" Alright.\""
                hide 8newalex177
                show 8newalex180
                with dissolve
                " You head back downstairs."
                hide 8newalex180
                show 8newalex181
                with dissolve
                b "\" She has a leash on you doesn't she?\""
                p "\" Alex?\""
                p "\" Kinda.\""
                b "\" *Sigh*\""
                b "\" Yeah. Someday someone will take her mouth the wrong way and smack her teeth out.\""
                p "\" I'll rip his head off.\""
                b "\" I kinda believe you.\""
                b "\" But let me ask you something else.\""
                b "\" This thing with Tanya is likely to get very bad.\""
                b "\" Steps will need to be taken.\""
                hide 8newalex181
                show 8newalex182
                with dissolve
                b "\" Are you ready to rip the head off someone who isn't threatening my Daughter?\""
                b "\" Are you ready to pull the trigger on someone who you don't know?\""
                p "\" Like an old blonde woman?\""
                b "\" Theoretically.\""
                b "\" Could you do it?\""
                b "\" Not in a fit of anger. Not in self defense?\""
                b "\" Could you take a life in cold blood?\""
                call screen screen46

label ep8noboris:
                scene 8newalex182
                with dissolve
                p "\" I don't know.\""
                p "\" I've never done it before.\""
                p "\" Not in cold blood.\""
                show 8newalex183
                with dissolve
                b "\" Well, you'll need to make peace with the idea.\""
                b "\" It will likely come to that some day.\""
                b "\" It always does eventually.\""
                jump ep8cont7

label ep8yesboris:
                scene 8newalex182
                with dissolve
                $ borispts = borispts + 1
                " You nod your head."
                show 8newalex183
                with dissolve
                b "\" Good.\""
                b "\" It will likely come to that some day.\""
                b "\" It always does eventually.\""
                jump ep8cont7

label ep8cont7:
                scene 8newalex184
                with dissolve
                " You watched the match with Boris."
                " Trying to make sense of snooker's byzantine rules."
                show 8newalex185
                with dissolve
                " But eventually it ended."
                " And you both head to sleep."
                hide 8newalex185
                show 8newalex186
                with dissolve
                b "\" Buddy!\""
                b "\" You're room isn't over there.\""
                p "\" Actually...\""
                p "\" I'm going to Alexandra's room.\""
                hide 8newalex186
                show 8newalex187
                with dissolve
                b "\" Excuse me?\""
                p "\" She insisted.\""
                b "\" She insisted?\""
                p "\" Made it clear, that we'll just be sleeping.\""
                p "\" But yes, she insisted.\""
                hide 8newalex187
                show 8newalex188
                with dissolve
                " He walks away without another word, but you can hear him muttering under his breath."
                hide 8newalex188
                show 8newalex189
                with dissolve
                " You find Alex sleeping in her room."
                hide 8newalex189
                show 8newalex190
                with dissolve
                " But she wakes up as soon as you enter."
                a "\" Still in one piece I see.\""
                p "\" Still in one piece.\""
                a "\" Told you.\""
                p "\" Going to take a shower.\""
                a "\" Of course.\""
                hide 8newalex190
                show 8newalex191
                with dissolve
                " You undress and get in the shower."
                hide 8newalex191
                show 8newalex192
                with dissolve
                a "\" Hey.\""
                a "\" I forgot to ask you.\""
                a "\" Do you need... Release?\""
                p "\" Release?\""
                p "\" Wow.\""
                p "\" When you put it like that...\""
                a "\" Sorry, I'm not Izzy. I'm more...\""
                p "\" I know.\""
                p "\" I'm good love.\""
                hide 8newalex192
                show 8newalex193
                with dissolve
                " She kisses you."
                hide 8newalex193
                show 8newalex194
                with dissolve
                a "\" Love you, puppy.\""
                p "\" He he...\""
                p "\" I knew that before you did.\""
                a "\" I take it back.\""
                p "\" Far too late.\""
                a "\" Well hurry up.\""
                hide 8newalex194
                show 8newalex191
                with dissolve
                " You finish your shower and head outside."
                hide 8newalex191
                show 8newalex195
                with dissolve
                p "\" Shit!\""
                hide 8newalex195
                show 8newalex196
                with dissolve
                a "\" What?\""
                p "\" My pyjamas are upstairs.\""
                p "\" Have to go get them.\""
                hide 8newalex196
                show 8newalex197
                with dissolve
                a "\" Don't be silly.\""
                a "\" Just sleep naked.\""
                a "\" We'll get an extra blanket.\""
                hide 8newalex197
                show 8newalex198
                with dissolve
                a "\" What?\""
                p "\" Are you trying to provoke me?\""
                hide 8newalex198
                show 8newalex199
                with dissolve
                a "\" Maybe?\""
                a "\" A little?\""
                hide 8newalex199
                show 8newalex200
                with dissolve
                " She stands up and takes off her bottoms."
                p "\" Alex?\""
                a "\" Yes?\""
                hide 8newalex200
                show 8newalex201
                with dissolve
                " Then the rest of her pyjamas."
                p "\" Why?\""
                a "\" Because I think we'd both prefer skin on skin.\""
                hide 8newalex201
                show 8newalex202
                with dissolve
                " Your eyes are drawn to her pussy."
                p "\" But I'm not allowed to do anything.\""
                hide 8newalex202
                show 8newalex203
                with dissolve
                a "\" I may call you puppy, but I know you're not an animal.\""
                p "\" Don't be so sure.\""
                a "\" Not with me, anyway.\""
                hide 8newalex203
                show 8newalex204
                with dissolve
                a "\" Now hurry up and get in here.\""
                a "\" I'm feeling chilly already, and with Dad spreading his germs...\""
                hide 8newalex204
                show 8newalex205
                with dissolve
                " You take the blanket and get in the bed with her."
                a "\" *Sigh*\""
                a "\" This is nice.\""
                a "\" This is what we're doing from now on.\""
                p "\" What about when Izzy is here.\""
                a "\" She'll go to your old room, and sneak back here after Dad's asleep.\""
                a "\" Let me turn off the lights.\""
                hide 8newalex205
                show 8newalex206
                with dissolve
                p "\" What if Mr. Boris comes in.\""
                a "\" He won't.\""
                a "\" Too afraid he'll find you with your dick down my throat.\""
                p "\" Now you are trying to drive me crazy.\""
                a "\" He he...\""
                hide 8newalex206
                show 8newalex207
                with dissolve
                a "\" Goodnight.\""
                p "\" Goodnight.\""
                hide 8newalex207
                show blackscreen
                with dissolve
                "..."
                "... ..."
                "... ... ..."
                hide blackscreen
                label galleryScene7:
                show 8newalex210
                with dissolve
                " You wake up with your face again nuzzled against her neck."
                a "\" Are you awake?\""
                p "\" Yeah.\""
                a "\" Noticed your breathing changed.\""
                hide 8newalex210
                show 8newalex211
                with dissolve
                p "\" Where's the blanket.\""
                a "\" We must've lost it in the night.\""
                a "\" Your dick is lodged between my buttcheeks, you know.\""
                p "\" I'd say I'm sorry, but I'm not.\""
                hide 8newalex211
                show 8newalex212
                with dissolve
                a "\" Did I say you should be?\""
                hide 8newalex212
                show 8newalex213
                with dissolve
                "  She turns around to face you."
                a "\" Ready to meet the day?\""
                a "\" See if Dad will kill us both?\""
                p "\" I might need a little encouragement.\""
                hide 8newalex213
                show 8newalex214
                with dissolve
                a "\" I see.\""
                p "\" Going out there in a big bad world.\""
                a "\" Something to look forward to?\""
                hide 8newalex214
                show 8newalex215
                with dissolve
                a "\" Like this?\""
                p "\" Eh...\""
                hide 8newalex215
                show 8newalex216
                with dissolve
                a "\" A little more?\""
                p "\" Eh...\""
                hide 8newalex216
                show 8newalex217
                with dissolve
                a "\" He he...\""
                a "\" Come on.\""
                a "\" We have to get up, and I have to call Izzy.\""
                hide 8newalex217
                show 8newalex218
                with dissolve
                " She takes her phone."
                hide 8newalex218
                show 8newalex219
                with dissolve
                a "\" Morning sweetie!\""
                a "\" Yeah.\""
                a "\" Well, we're just getting ready.\""
                a "\" We're picking you up, right?\""
                if izzyin == True:
                    hide 8newalex219
                    show 8newalex220
                    with dissolve
                    a "\" Yeah, he's right here.\""
                    a "\" What do you mean?\""
                    a "\" Kiss and a squeeze?\""
                    a "\" *Sigh*\""
                    hide 8newalex220
                    show 8newalex221
                    with dissolve
                    " She comes over, squeezes your dick and gives you a kiss on the ear."
                    a "\" From Izzy.\""
                    p "\" I figured.\""
                    hide 8newalex221
                    show 8newalex222
                    with dissolve
                    a "\" Done.\""
                    a "\" Yes, I did it.\""
                    a "\" Ask him if you don't believe me.\""
                    a "\" Ok.\""
                    a "\" See you soon.\""
                    jump ep8cont8

                else:
                    hide 8newalex219
                    show 8newalex222
                    with dissolve
                    a "\" Ok.\""
                    a "\" See you soon.\""
                    jump ep8cont8

label ep8cont8:
                scene 8newalex223
                with dissolve
                a "\" Come on, puppy.\""
                p "\" *Groan*\""
                a "\" I know.\""
                a "\" But you have to get up.\""
                show 8newalex224
                with dissolve
                " You enter the shower first, and she waits outside."
                p "\" We could both get in here.\""
                a "\" Too small.\""
                hide 8newalex224
                show 8newalex225
                with dissolve
                a "\" Why?\""
                a "\" You want to wash together?\""
                p "\" Well...\""
                a "\" *Sigh*\""
                a "\" You and Izzy both.\""
                a "\" I'll get a tub.\""
                hide 8newalex225
                $ renpy.end_replay()
                show 8newalex226
                with dissolve
                " You get dressed and head downstairs."
                hide 8newalex226
                show 8newalex227
                with dissolve
                " And find Boris already in the kitchen."
                b "\" Kids?\""
                p "\" Boss.\""
                hide 8newalex227
                show 8newalex228
                with dissolve
                b "\" I'm sure you had a good night's sleep.\""
                hide 8newalex228
                show 8newalex229
                with dissolve
                a "\" Is that your round about way to ask if we had sex?\""
                a "\" We didn't, Dad.\""
                a "\" Puppy isn't like that.\""
                hide 8newalex229
                show 8newalex230
                with dissolve
                b "\" Alex!\""
                hide 8newalex230
                show 8newalex229
                with dissolve
                a "\" You want a play by play when we do?\""
                a "\" Maybe video evidence?\""
                hide 8newalex230
                show 8newalex229
                with dissolve
                b "\" *Sigh*\""
                hide 8newalex229
                show 8newalex230
                with dissolve
                a "\" Don't ask questions you don't want answers to.\""
                a "\" That's what you told me when I turned 16 and asked you what you really do for a living.\""
                a "\" Well?\""
                b "\"...\""
                p "\" Am I driving you today boss?\" You say to ease the tension."
                hide 8newalex230
                show 8newalex228
                with dissolve
                b "\" Yes.\""
                b "\" Feeling better, and I have to go take care of something.\""
                hide 8newalex228
                show back1
                with dissolve
                show 8newalex231
                with dissolve
                " You have a quick breakfast, and go pick up Izzy."
                a "\" How's your Mom?\""
                i "\" Good.\""
                i "\" Very good actually.\""
                i "\" Better than she's been in a long time.\""
                hide 8newalex231
                show 8newalex232
                with dissolve
                b "\" I'm happy to hear that.\""
                b "\" Your Mother is quite a woman.\""
                hide 8newalex232
                show 8newalex233
                with dissolve
                i "\" Thank you.\""
                i "\" I'm sure she thinks the world of you too.\""
                hide 8newalex233
                show 8newalex232
                with dissolve
                b "\" Doesn't really remember me?\""
                hide 8newalex232
                show 8newalex233
                with dissolve
                i "\" I don't think so.\""
                i "\" She doesn't really mention you.\""
                i "\"...\""
                i "\" I'm sorry.\""
                hide 8newalex233
                show 8newalex232
                with dissolve
                b "\" Time and illness gets us all in the end, girl."
                hide 8newalex232
                show 8newalex234
                with dissolve
                " You drop the girls off at school, and you leave Boris at an address he gave you."
                b "\" Pick me back up in four hours.\""
                p "\" Got it.\""
                b "\" And remember about Tanya.\""
                b "\" We need to get ready.\""
                p "\" I understand.\""
                if ep7robbery == True:
                    hide 8newalex234
                    show 8newalex235
                    with dissolve
                    " When you get to work, Yuri is already there."
                    yuri "\" Boss?\""
                    hide 8newalex235
                    show 8newalex208
                    with dissolve
                    " He brings up a bag."
                    yuri "\" Your men brought this in.\""
                    p "\" Good.\""
                    hide 8newalex208
                    show 8newalex235
                    with dissolve
                    yuri "\" Someone's here to see you too.\""
                    p "\" Marcello's man?\""
                    yuri "\" I doubt it.\""
                    if alicehug1 == True:
                        jump ep8alice
                    else:
                        jump ep8noalice

                else:
                    hide 8newalex234
                    show 8newalex235
                    with dissolve
                    " When you get to work, Yuri is already there."
                    yuri "\" Boss?\""
                    p "\" Everything ready for Marcello?\""
                    yuri "\" I hope so.\""
                    hide 8newalex235
                    show 7newalex93
                    with dissolve
                    " You take a seat, and wait for Marcello's man."
                    jump ep9cont2

label ep8noalice:
                scene 8newalex236
                with dissolve
                lenny "\" Hey man.\""
                p "\" Lenny.\""
                p "\" What are you doing here?\""
                lenny "\" I need to talk to you.\""
                p "\" Sure.\""
                lenny "\" Alone?\""
                p "\" There's a smoking area on the roof, I think.\""
                lenny "\" Ok.\""
                show 8newalex237
                with dissolve
                " You make your way upstairs."
                lenny "\" This is nice.\""
                p "\" What can I do for you, Lenny?\""
                hide 8newalex237
                show 8newalex238
                with dissolve
                lenny "\" What did you do man?\""
                p "\" What?\""
                lenny "\" At the poker game?\""
                p "\" What?\""
                lenny "\" Well, the word is that one of the players was the jagoff son of some DA.\""
                lenny "\" And that someone crushed his skull.\""
                hide 8newalex238
                show 8newalex239
                with dissolve
                p "\" Fuck me.\""
                lenny "\" What did you do man?\""
                p "\" Just fuck me.\""
                jump ep9robnoalice

label ep8alice:
                scene 8newalex240
                with dissolve
                ali "\" Hey.\""
                p "\" Alice?\""
                p "\" What are you doing here?\""
                ali "\" I need to talk to you.\""
                p "\" Sure.\""
                ali "\" Alone?\""
                p "\" There's a smoking area on the roof, I think.\""
                ali "\" Ok.\""
                show 8newalex241
                with dissolve
                " You make your way upstairs."
                ali "\" This is nice.\""
                p "\" What is it, Alice?\""
                hide 8newalex241
                show 8newalex242
                with dissolve
                ali "\" What did you do man?\""
                p "\" What?\""
                ali "\" At the poker game?\""
                p "\" What?\""
                ali "\" Well, the word is that one of the players was the jackoff son of some DA.\""
                ali "\" And that someone crushed his skull.\""
                hide 8newalex242
                show 8newalex243
                with dissolve
                p "\" Fuck me.\""
                ali "\" What did you do man?\""
                p "\" Just fuck me.\""
                jump ep9robalice
