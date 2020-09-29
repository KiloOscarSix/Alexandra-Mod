label ep13:
                scene 12newalex231
                with dissolve
                default sistersknow = False
                " You start to doze off."
                show blackscreen
                with dissolve
                "..."
                "... ..."
                " You hear Alex saying..."
                a "\" How long does it take you to get ice cream?\""
                hide blackscreen
                show 13newalex1
                with dissolve
                p "\" What?\""
                a "\" How long does it take you to get ice cream?\""
                a "\" She's been gone for twenty minutes now.\""
                hide 13newalex1
                show 13newalex2
                with dissolve
                " The image of the guy downstairs flashes before your eyes."
                p "\" Shit!\""
                p "\" Call her.\""
                a "\" What?\""
                p "\" Call Isabella.\""
                p "\" Now!\""
                hide 13newalex2
                show 13newalex166
                with dissolve
                a "\" Ok.\""
                a "\"... ...\""
                a "\" Not answering.\""
                p "\" Shit!\""
                hide 13newalex167
                with dissolve
                a "\" Where are you going?\" She asks, as you put your clothes on."
                p "\" To go get her.\""
                p "\" Lock the door.\""
                p "\" Lock the door and don't let anyone but me in.\""
                a "\" What's happening?\""
                p "\" Just do what I tell you.\""
                a "\" You're scaring me.\""
                p "\" Good.\""
                hide 13newalex167
                show 13newalex3
                with dissolve
                " You leave Alex and do a frantic search of the hotel grounds."
                p "\" Shit!\""
                p "\" Shit!\""
                p "\" The restaurant, maybe?\""
                hide 13newalex3
                show 13newalex4
                with dissolve
                " You rush over to the restaurant in which you had dinner."
                p "\" Fuck me!\""
                p "\" I should listen to my instincts.\""
                hide 13newalex4
                show 13newalex5
                with dissolve
                " You go over to the barman."
                p "\" Hey!\""
                p "\" Have you seen a girl about this tall?\""
                p "\" Dark hair...\""
                i "\" [player_name]?\""
                hide 13newalex5
                show 13newalex7
                with dissolve
                p "\" There you are!\""
                i "\" What?\""
                p "\" What are you doing here?\""
                p "\" You said you were going out for ice cream.\""
                i "\" The hotel dining room was closed so I came here.\""
                if izzyin == True:
                    hide 13newalex7
                    show 13newalex9
                    with dissolve
                    i "\" What?\""
                    p "\" You scared the shit out of us.\""
                    i "\" Why?\""
                    i "\" I don't get it.\""
                    p "\" Alex even called you.\""
                    i "\" Must not have heard it.\""
                    hide 13newalex8
                    show 13newalex264
                    with dissolve
                    i "\" Yeah.\""
                    i "\" Missed call.\""
                    p "\" Come on.\""
                    p "\" Let's go.\""
                    hide 13newalex264
                    show 13newalex7
                    with dissolve
                    i "\" Let me just get my ice cream.\""
                    p "\" Forget it.\""
                    p "\" Let's just go.\""
                    p "\" We're going to give Alex an ulcer if we don't get back.\""
                    p "\" More importantly. We're going to give me one.\""
                    i "\" That's... Ok...\""
                    hide 13newalex7
                    show 13newalex10
                    with dissolve
                    " You go back to the hotel with a very confused Isabella."
                    i "\" Seriously. What's wrong?\""
                    p "\" It's not that something's wrong.\""
                    p "\" I mean... You know who Alex's dad is, right?\""
                    p "\" You know who I am.\""
                    hide 13newalex10
                    show 13newalex11
                    with dissolve
                    i "\" Please...\""
                    p "\" Don't mock it.\""
                    p "\" You had us worried sick.\""
                    hide 13newalex11
                    show 13newalex12
                    with dissolve
                    i "\" Us?\""
                    p "\" Yeah.\""
                    i "\" *Sigh*\""
                    i "\" Sweet. But I think you're worried about nothing.\""
                    jump ep13cont1

                else:
                    hide 13newalex7
                    show 13newalex8
                    with dissolve
                    i "\" And don't raise your voice at me.\""
                    p "\" Don't raise my voice?\""
                    p "\" You scared the shit out of us.\""
                    i "\" Why?\""
                    p "\" Why do you think. Because we didn't know what happened.\""
                    p "\" Alex even called you.\""
                    i "\" Must not have heard it.\""
                    hide 13newalex8
                    show 13newalex264
                    with dissolve
                    i "\" Yeah.\""
                    i "\" Missed call.\""
                    p "\" Come on.\""
                    p "\" Let's go.\""
                    hide 13newalex264
                    show 13newalex8
                    with dissolve
                    i "\" But I didn't get my ice cream yet.\""
                    p "\" Forget the ice cream.\""
                    p "\" Let's just go.\""
                    i "\" Fine!\""
                    hide 13newalex8
                    show 13newalex10
                    with dissolve
                    " You go back to the hotel with a very unhappy Isabella."
                    i "\" I get that you're fucking Alex. But that doesn't mean you run my life.\""
                    p "\" I'm not in the mood to get in a whole thing with you.\""
                    i "\" Humph...\""
                    hide 13newalex10
                    show 13newalex11
                    with dissolve
                    i "\" A whole thing?\""
                    p "\" You know what I mean.\""
                    jump ep13cont1

label ep13cont1:
                scene 13newalex13
                with dissolve
                " You get back to the hotel."
                " As far as you can tell Alex was getting dressed."
                a "\" There you are.\""
                p "\" Found her.\""
                a "\" Where was she?\""
                p "\" At the restaurant where we ate.\""
                p "\" Dining room is closed at the hotel.\""
                show 13newalex14
                with dissolve
                a "\" Why didn't you call me?\""
                a "\" I got all worked up with the way you stormed out.\""
                p "\" You're right.\""
                p "\" I should have.\""
                hide 13newalex14
                show 13newalex15
                with dissolve
                i "\" What is it with you two?\""
                i "\" I was gone for less than an hour.\""
                hide 13newalex15
                show 13newalex16
                with dissolve
                a "\" And you! Why don't you answer your phone?\""
                i "\" Didn't hear it.\""
                a "\" What do you mean you didn't hear it?\""
                hide 13newalex16
                show 13newalex265
                with dissolve
                i "\" I'm not talking to you while you're shouting.\""
                i "\" Gonna go get undressed.\""
                " She storms off to the bathroom."
                hide 13newalex265
                show 13newalex19
                with dissolve
                " Alex gets back on the bed."
                a "\" Restaurant?\""
                p "\" Yeah.\""
                a "\" The way you stormed out...\""
                a "\" Scared the shit out of me.\""
                p "\" I know.\""
                p "\" I was just thinking...\""
                p "\" Doesn't matter.\""
                hide 13newalex19
                show 13newalex20
                with dissolve
                a "\" You got me thinking...\""
                a "\" You know. That it was those men again.\""
                a "\" Maybe... Izzy...\""
                p "\" That's what I was thinking too.\""
                hide 13newalex20
                show 13newalex21
                with dissolve
                a "\" That's fucked up.\""
                a "\" We shouldn't think like that.\""
                a "\" Can't get paranoid.\""
                a "\" We're here to relax, remember.\""
                p "\" Yeah.\""
                hide 13newalex21
                show 13newalex22
                with dissolve
                " Soon Izzy came back ready for bed."
                if izzyin == True:
                    hide 13newalex22
                    show 13newalex24
                    with dissolve
                    " You get back in bed."
                    i "\" I didn't even get my ice cream.\""
                    a "\" I don't care.\""
                    p "\" I'll get you some tomorrow.\""
                    i "\" Cotton candy too?\""
                    p "\" He he...\""
                    p "\" Whatever you want.\""
                    p "\" Just answer the phone from now on.\""
                    i "\" Ok.\""
                    jump ep13cont2

                else:
                    hide 13newalex22
                    show 13newalex23
                    with dissolve
                    " You get back in bed."
                    i "\" Goodnight.\""
                    a "\" Goodnight.\""
                    jump ep13cont2

label ep13cont2:
                scene blackscreen
                with dissolve
                "..."
                "... ..."
                "... ... ..."
                show 13newalex25
                with dissolve
                " When you open your eyes, Alex is still sleeping."
                a "\" *Snore*\""
                hide 13newalex25
                show 13newalex26
                with dissolve
                " And with Izzy, they were a chorus."
                i "\" *Snore*\""
                hide 13newalex26
                show 13newalex27
                with dissolve
                p "\" Alex.\""
                a "\" Mmm...\""
                p "\" Alex!\""
                a "\" What?\" She says, not opening her eyes."
                p "\" It's morning.\""
                hide 13newalex27
                show 13newalex28
                with dissolve
                " She turns her back."
                a "\" *Sigh*\""
                a "\" Five more minutes.\""
                p "\" Sleep as long as you like. I was just...\""
                a "\" Ten more minutes.\""
                hide 13newalex28
                show 13newalex29
                with dissolve
                " You get up and take a shower."
                if izzyin == True:
                    hide 13newalex29
                    show 13newalex30
                    with dissolve
                    i "\" Hey.\""
                    p "\" Morning.\""
                    i "\" Room for one more?\""
                    p "\" Always.\""
                    hide 13newalex30
                    show 13newalex32
                    with dissolve
                    " She drops her pajamas and gets in the shower with you."
                    i "\" Still upset with me?\""
                    p "\" I wasn't upset.\""
                    p "\" Just worried.\""
                    i "\" Why? What could've happened?\""
                    i "\" We're not exactly in the bad part of town.\""
                    i "\" Very touristy around here.\""
                    p "\" It's not that.\""
                    p "\" It's just that I thought I saw this guy...\""
                    i "\" What guy?\""
                    p "\" Maybe it wasn't even him.\""
                    hide 13newalex32
                    show 13newalex33
                    with dissolve
                    " She gives you a kiss."
                    hide 13newalex33
                    show 13newalex34
                    with dissolve
                    i "\" Don't worry about me.\""
                    i "\" I can handle myself.\""
                    p "\" Is that right?\""
                    i "\" Yeah.\""
                    i "\" Now better wake up Alex.\""
                    i "\" She'll want to be on the beach soon.\""
                    hide 13newalex34
                    show 13newalex35
                    with dissolve
                    " As you leave she says..."
                    i "\" And remember. Cotton candy too.\""
                    p "\" He he...\""
                    p "\" I didn't forget.\""
                    jump ep13cont3

                else:
                    hide 13newalex29
                    show 13newalex30
                    with dissolve
                    i "\" Are you going to be much longer.\""
                    p "\" You're up.\""
                    i "\" Yeah.\""
                    p "\" Just finished.\""
                    hide 13newalex30
                    show 13newalex31
                    with dissolve
                    " You leave, and she takes your place."
                    i "\" Do you mind?\""
                    i "\" Some space?\""
                    p "\" Of course.\""
                    jump ep13cont3

label ep13cont3:
                scene 13newalex36
                with dissolve
                " You get back to Alex."
                p "\" Hey!\""
                a "\" Mmm...\""
                p "\" Time to wake up.\""
                show 13newalex266
                with dissolve
                " She turns around still sleepy."
                p "\" Want another 10 minutes?\""
                a "\" No, no.\""
                a "\" I need to get up.\""
                a "\" We're not here to stay in the hotel.\""
                hide 13newalex266
                show 13newalex37
                with dissolve
                a "\" You? You ok?\""
                a "\" Sorry if I snapped at you last night.\""
                p "\" Fine.\""
                p "\" Sorry I scared you.\""
                a "\" Izzy?\""
                p "\" In the shower.\""
                a "\" I'd better get in there too.\""
                hide 13newalex37
                show 13newalex38
                with dissolve
                " She joins Izzy in the bathroom."
                hide 13newalex38
                show 13newalex39
                with dissolve
                " You spend the morning on the beach."
                " A bit boring for you, but the girls were pleased."
                hide 13newalex39
                show 13newalex40
                with dissolve
                a "\" Thoughtful.\""
                p "\" What?\""
                a "\" You. You look thoughtful.\""
                a "\" Bored?\""
                p "\" A bit.\""
                hide 13newalex40
                show 13newalex41
                with dissolve
                a "\" He he...\""
                a "\" I have the cure for that.\""
                a "\" Come with me.\""
                hide 13newalex41
                show 12newalex137
                with dissolve
                " She runs into the water."
                a "\" COME!\" She screams back at you."
                hide 13newalex267
                show 13newalex42
                with dissolve
                " You follow her in."
                hide 13newalex42
                show 13newalex43
                with dissolve
                a "\" Closer.\""
                a "\" I won't bite.\""
                a "\" Well, not too hard.\""
                hide 13newalex43
                show 13newalex44
                with dissolve
                " As soon as you do, she clings to you."
                a "\" [player_nik]...\""
                hide 13newalex44
                show 13newalex45
                with dissolve
                " You kiss her neck."
                a "\" He he he...\""
                hide 13newalex45
                show 13newalex46
                with dissolve
                a "\" Let me try something.\""
                hide 13newalex46
                show 13newalex48
                with dissolve
                " You can feel her hand fumbling for your shorts."
                hide 13newalex48
                show 13newalex49
                with dissolve
                a "\" Damn.\""
                a "\" You know what? These might be too tight.\""
                p "\" Told you,\""
                hide 13newalex49
                show 13newalex47
                with dissolve
                a "\" Ok.\""
                a "\" Ok, I got this.\""
                a "\" There we go.\"She says, as you feel her warmth engulf your penis."
                hide 13newalex47
                show 13newalex55
                with dissolve
                " You pull her towards you, going deeper."
                a "\" Ouch.\""
                p "\" Ok?\""
                hide 13newalex55
                show 13newalex50
                with dissolve
                a "\" He he...\""
                a "\" Yeah.\""
                a "\" Just... The water...\""
                a "\" Don't stop.\""
                scene alexseasex animated with fade:
                    "21a1.webp"
                    pause 0.01
                    "21a2.webp"
                    pause 0.01
                    "21a3.webp"
                    pause 0.01
                    "21a4.webp"
                    pause 0.01
                    "21a5.webp"
                    pause 0.01
                    "21a6.webp"
                    pause 0.01
                    "21a7.webp"
                    pause 0.01
                    "21a8.webp"
                    pause 0.01
                    "21a9.webp"
                    pause 0.01
                    "21a10.webp"
                    pause 0.01
                    "21a11.webp"
                    pause 0.02
                    "21a12.webp"
                    pause 0.02
                    "21a13.webp"
                    pause 0.02
                    "21a14.webp"
                    pause 0.02
                    "21a15.webp"
                    pause 0.02
                    "21a16.webp"
                    pause 0.02
                    "21a17.webp"
                    pause 0.02
                    "21a18.webp"
                    pause 0.02
                    "21a19.webp"
                    pause 0.02
                    "21a20.webp"
                    pause 0.02
                    "21a21.webp"
                    pause 0.03
                    "21a22.webp"
                    pause 0.03
                    "21a23.webp"
                    pause 0.03
                    "21a24.webp"
                    pause 0.03
                    "21a25.webp"
                    pause 0.03
                    "21a26.webp"
                    pause 0.03
                    "21a27.webp"
                    pause 0.03
                    "21a28.webp"
                    pause 0.03
                    "21a29.webp"
                    pause 0.03
                    "21a30.webp"
                    pause 0.03
                    "21a31.webp"
                    pause 0.04
                    "21a30.webp"
                    pause 0.03
                    "21a29.webp"
                    pause 0.03
                    "21a28.webp"
                    pause 0.03
                    "21a27.webp"
                    pause 0.03
                    "21a26.webp"
                    pause 0.03
                    "21a25.webp"
                    pause 0.03
                    "21a24.webp"
                    pause 0.03
                    "21a23.webp"
                    pause 0.03
                    "21a22.webp"
                    pause 0.03
                    "21a21.webp"
                    pause 0.03
                    "21a20.webp"
                    pause 0.02
                    "21a19.webp"
                    pause 0.02
                    "21a18.webp"
                    pause 0.02
                    "21a17.webp"
                    pause 0.02
                    "21a16.webp"
                    pause 0.02
                    "21a15.webp"
                    pause 0.02
                    "21a14.webp"
                    pause 0.02
                    "21a13.webp"
                    pause 0.02
                    "21a12.webp"
                    pause 0.02
                    "21a11.webp"
                    pause 0.02
                    "21a10.webp"
                    pause 0.01
                    "21a9.webp"
                    pause 0.01
                    "21a8.webp"
                    pause 0.01
                    "21a7.webp"
                    pause 0.01
                    "21a6.webp"
                    pause 0.01
                    "21a5.webp"
                    pause 0.01
                    "21a4.webp"
                    pause 0.01
                    "21a3.webp"
                    pause 0.01
                    "21a2.webp"
                    pause 0.01
                    repeat
                a "\" Ohhh...\""
                " It's a bit difficult pulling her towards you and pushing her away without a perch."
                a "\" Ahhh...\""
                a "\" Hurts.\""
                p "\" Stop?\""
                a "\" No.\""
                $ renpy.pause ()
                show 13newalex56
                with dissolve
                a "\" Ahh...\""
                a "\" Yes...\""
                a "\" Just like that...\""
                scene alexseasex animated with fade:
                    "21a1.webp"
                    pause 0.01
                    "21a2.webp"
                    pause 0.01
                    "21a3.webp"
                    pause 0.01
                    "21a4.webp"
                    pause 0.01
                    "21a5.webp"
                    pause 0.01
                    "21a6.webp"
                    pause 0.01
                    "21a7.webp"
                    pause 0.01
                    "21a8.webp"
                    pause 0.01
                    "21a9.webp"
                    pause 0.01
                    "21a10.webp"
                    pause 0.01
                    "21a11.webp"
                    pause 0.02
                    "21a12.webp"
                    pause 0.02
                    "21a13.webp"
                    pause 0.02
                    "21a14.webp"
                    pause 0.02
                    "21a15.webp"
                    pause 0.02
                    "21a16.webp"
                    pause 0.02
                    "21a17.webp"
                    pause 0.02
                    "21a18.webp"
                    pause 0.02
                    "21a19.webp"
                    pause 0.02
                    "21a20.webp"
                    pause 0.02
                    "21a21.webp"
                    pause 0.03
                    "21a22.webp"
                    pause 0.03
                    "21a23.webp"
                    pause 0.03
                    "21a24.webp"
                    pause 0.03
                    "21a25.webp"
                    pause 0.03
                    "21a26.webp"
                    pause 0.03
                    "21a27.webp"
                    pause 0.03
                    "21a28.webp"
                    pause 0.03
                    "21a29.webp"
                    pause 0.03
                    "21a30.webp"
                    pause 0.03
                    "21a31.webp"
                    pause 0.04
                    "21a30.webp"
                    pause 0.03
                    "21a29.webp"
                    pause 0.03
                    "21a28.webp"
                    pause 0.03
                    "21a27.webp"
                    pause 0.03
                    "21a26.webp"
                    pause 0.03
                    "21a25.webp"
                    pause 0.03
                    "21a24.webp"
                    pause 0.03
                    "21a23.webp"
                    pause 0.03
                    "21a22.webp"
                    pause 0.03
                    "21a21.webp"
                    pause 0.03
                    "21a20.webp"
                    pause 0.02
                    "21a19.webp"
                    pause 0.02
                    "21a18.webp"
                    pause 0.02
                    "21a17.webp"
                    pause 0.02
                    "21a16.webp"
                    pause 0.02
                    "21a15.webp"
                    pause 0.02
                    "21a14.webp"
                    pause 0.02
                    "21a13.webp"
                    pause 0.02
                    "21a12.webp"
                    pause 0.02
                    "21a11.webp"
                    pause 0.02
                    "21a10.webp"
                    pause 0.01
                    "21a9.webp"
                    pause 0.01
                    "21a8.webp"
                    pause 0.01
                    "21a7.webp"
                    pause 0.01
                    "21a6.webp"
                    pause 0.01
                    "21a5.webp"
                    pause 0.01
                    "21a4.webp"
                    pause 0.01
                    "21a3.webp"
                    pause 0.01
                    "21a2.webp"
                    pause 0.01
                    repeat
                a "\" Yes...\""
                a "\" Yes... [player_nik]...\""
                a "\" Ahh...\""
                $ renpy.pause ()
                show 13newalex57
                with dissolve
                " She tightens up and you can feel her nails digging into you a bit as you cum."
                p "\" Ahhgh...\""
                a "\" *Pant* *Pant* *Pant*\""
                p "\" *Pant* *Pant* *Pant*\""
                show 13newalex58
                with dissolve
                a "\" He he...\""
                hide 13newalex58
                show 13newalex60
                with dissolve
                a "\" Ouch...\""
                p "\" What?\""
                a "\" Is your dick bigger than last time?\""
                p "\" He he...\""
                p "\" Who knows, but I wouldn't think so.\""
                a "\" Hurts more, though.\""
                p "\" Salt water.\""
                hide 13newalex60
                show 13newalex59
                with dissolve
                a "\" Hmmm...\""
                a "\" Mental note. No salt water sex from now on.\""
                a "\" Ouch...\""
                p "\" You ok?\""
                a "\" Yeah.\""
                hide 13newalex59
                show 13newalex61
                with dissolve
                " You kiss."
                hide 13newalex61
                show 13newalex59
                with dissolve
                a "\" Love ya, pupster.\""
                p "\" Love you too.\""
                hide 13newalex59
                show 13newalex51
                with dissolve
                " When you get back on the beach, Izzy isn't on the blanket anymore."
                hide 13newalex51
                show 13newalex52
                with dissolve
                a "\" Damn it!\""
                a "\" She's gone again.\""
                p "\" Call her.\""
                hide 13newalex52
                show 13newalex53
                with dissolve
                a "\" No!\""
                a "\" She should know better after last night.\""
                a "\" Starting to think she's just doing this for attention.\""
                a "\" Shell turn up with a bucket of ice cream.\""
                p "\" Hmmm...\""
                a "\" I know the girl.\""
                hide 13newalex53
                show 13newalex54
                with dissolve
                " You both lay down on the blanket, and wait for Izzy to turn up."
                " 10 minutes pass..."
                " Then twenty..."
                " Then an hour..."
                p "\" Call her.\""
                hide 13newalex54
                show 13newalex62
                with dissolve
                a "\" What if she doesn't answer again?\""
                p "\" Just do it.\""
                a "\" Ok.\""
                hide 13newalex62
                show 13newalex64
                with dissolve
                " *Ring* *Ring* *Ring*"
                a "\" Damn it!\""
                p "\" Nothing?\""
                a "\" No.\""
                hide 13newalex64
                show 13newalex63
                with dissolve
                a "\" Is she trying to pull a prank?\""
                a "\" After last night I'll kill her, I swear.\""
                p "\" Get dressed.\""
                a "\" Why?\""
                p "\" Stop questioning me!\""
                p "\" Not on this shit.\""
                a "\" *Sigh*\""
                hide 13newalex63
                show 13newalex65
                with dissolve
                " She does as you tell her."
                a "\" Some vacation this is turning out to be.\""
                a "\" Izzy disappearing every five minutes.\""
                a "\" You freaking out about it every time.\""
                p "\" Does her phone have one of those find me things?\""
                a "\" Find me?\""
                p "\" One of those apps that finds it when it gets stolen?\""
                hide 13newalex65
                show 13newalex66
                with dissolve
                a "\" Yeah.\""
                p "\" And?\""
                p "\" Can you use it?\""
                a "\" Give me a second.\""
                hide 13newalex66
                show 13newalex67
                with dissolve
                a "\" Aha...\""
                a "\" There!\""
                a "\" Two miles away?\""
                a "\" The hell?\""
                hide 13newalex67
                show 13newalex68
                with dissolve
                a "\" What is she doing that far?\""
                p "\" That's it!\""
                hide 13newalex68
                show 13newalex69
                with dissolve
                " You grab Alex's arm and start heading back to the hotel."
                a "\" Hey!\""
                p "\" That mother fucker!\""
                a "\" Ouch!\""
                a "\" Watch it.\""
                a "\" You're goon handing me.\""
                p "\" Should've put my hands on him that night.\""
                p "\" Serves me right.\""
                hide 13newalex69
                show 13newalex70
                with dissolve
                a "\" Pupster?\""
                p "\" Let's go.\""
                a "\" Where?\""
                p "\" Back to the hotel.\""
                a "\" Aren't we going to Izzy.\""
                p "\" I am. You're not.\""
                hide 13newalex70
                show 13newalex72
                with dissolve
                " You march her back to the hotel."
                a "\" I think we just passed our room.\""
                p "\" Not leaving you there.\""
                p "\" Your name is registered to it.\""
                hide 13newalex72
                show 13newalex73
                with dissolve
                a "\" You're really goon handing me.\""
                a "\" My arm is starting to hurt.\""
                p "\" Don't have time to negotiate with you, Alex.\""
                p "\" Come!\""
                a "\" Where?\""
                p "\" To find some other room to keep you in while I go look for Izzy.\""
                hide 13newalex73
                show 13newalex74
                with dissolve
                " You start knocking on door after door."
                hide 13newalex74
                show 13newalex75
                with dissolve
                " Eventually, someone answers."
                m10 "\" Yes?\""
                hide 13newalex75
                show 13newalex76
                with dissolve
                " You barge in through the open door and grab him by the throat."
                m10 "\" Woah...\""
                a "\" Careful.\""
                a "\" Don't hurt him.\""
                hide 13newalex76
                show 13newalex77
                with dissolve
                m10 "\" Whoa are you?\""
                m10 "\" Nevermind.\""
                m10 "\" Look, just take what you want.\""
                p "\" Hush.\""
                m10 "\" Listen. My wallet is...\""
                hide 13newalex77
                show 13newalex78
                with dissolve
                " You cover his mouth."
                p "\" Hush, I said.\""
                p "\" Is anyone else here?\""
                " He shakes his head."
                w1 "\" Gerald?\""
                p "\" Hmmm...\""
                w1 "\" Gerald, who is it?\""
                hide 13newalex78
                show 13newalex79
                with dissolve
                p "\" Who's that?\""
                m10 "\" My wife.\""
                m10 "\" Don't... Don't hurt her.\""
                hide 13newalex79
                show 13newalex80
                with dissolve
                w1 "\" Oh, my God!\""
                p "\" Come here.\""
                a "\" You're scaring them.\""
                p "\" Good.\""
                w1 "\" Just take what you want.\""
                p "\" I want you to come here.\""
                hide 13newalex80
                show 13newalex81
                with dissolve
                " She hesitates."
                p "\" Come here!\""
                p "\" Come here or I snap his neck.\""
                a "\" No he won't.\""
                p "\" Come here!\""
                hide 13newalex81
                show 13newalex82
                with dissolve
                " She obeys and you put them on the couch."
                w1 "\" We don't have much.\""
                w1 "\" But just take it.\""
                w1 "\" I have some earrings too.\""
                p "\" Hush...\""
                w1 "\" Don't... Don't hurt us.\""
                hide 13newalex82
                show 13newalex84
                with dissolve
                a "\" No one is going to hurt you ma'am.\""
                p "\" Well, that depends.\""
                hide 13newalex84
                show 13newalex82
                with dissolve
                p "\" I don't want your money.\""
                a "\" No one is going to rob you.\""
                p "\" See this girl?\""
                " They nod."
                p "\" I want you to stay on this couch, until I come back.\""
                p "\" And the girl will stay with you.\""
                m10 "\" What?\""
                p "\" Exactly what I said.\""
                p "\" Do I have to tie you up?\""
                " They shake their heads."
                hide 13newalex82
                show 13newalex85
                with dissolve
                m10 "\" Why can't you just take the money and go?\""
                p "\" Shut up!\""
                p "\" Now if you do what I tell you, I'll come back and take the girl.\""
                p "\" And neither of you ever have to see me again.\""
                p "\" You don't? I strangle you old man, and shove your rotting corpse up your wife's ass.\""
                hide 13newalex85
                show 13newalex84
                with dissolve
                a "\" Pupster!!!\""
                p "\" Hush.\""
                a "\" He won't do any of that.\""
                hide 13newalex84
                show 13newalex85
                with dissolve
                p "\" Do you two understand me?\""
                " They nod."
                p "\" Good! I'll be right back.\""
                hide 13newalex85
                show 13newalex83
                with dissolve
                a "\" You have to scare them like that?\""
                p "\" Yes.\""
                p "\" Wait for me.\""
                p "\" I'll be right back.\""
                hide 13newalex83
                show 13newalex86
                with dissolve
                " You check Izzy's location again before you leave."
                " Looks like a building."
                hide 13newalex86
                show 13newalex87
                with dissolve
                " On your way out, you check your room just to make sure no one is there."
                " It's empty."
                hide 13newalex87
                show 13newalex88
                with dissolve
                " You rush over to where Izzy's phone seems to be."
                hide 13newalex88
                show 13newalex89
                with dissolve
                " The phone takes you to what looks like a bad area of the city."
                " Definitely not a place you'd go for ice cream and cotton candy."
                hide 13newalex89
                show 13newalex90
                with dissolve
                " You manage to narrow down the building the phone seems to be in."
                " And you try to sneak inside."
                hide 13newalex90
                show 13newalex91
                with dissolve
                " Seems like an abandoned warehouse."
                " You go deeper."
                hide 13newalex91
                show 13newalex92
                with dissolve
                " You finally hear some voices down a stairway."
                m11 "\" It's going to be ok.\""
                i "\" Fuck you!\""
                hide 13newalex92
                show 13newalex93
                with dissolve
                " You follow the stairs."
                m11 "\" Don't be truculent.\""
                m11 "\" We don't want to hurt you. So don't make us.\""
                i "\" Think I'm scared?\""
                hide 13newalex93
                show 13newalex94
                with dissolve
                " You get closer."
                m11 "\" No.\""
                m11 "\" In fact, I know you're not.\""
                m11 "\" You're special, Izzy.\""
                m11 "\" I know you're special.\""
                hide 13newalex94
                show 13newalex95
                with dissolve
                i "\" Don't you fucking call me that.\""
                m11 "\" What? Izzy?\""
                i "\" Only those close to me call me that.\""
                m11 "\" I understand.\""
                m11 "\" You don't like me now.\""
                m11 "\" But fear not. You'll like me better in the future.\""
                hide 13newalex95
                show 13newalex96
                with dissolve
                " Izzy notices you standing behind the guy."
                i "\" Future?\""
                i "\" What makes you think you have one?\""
                p "\" Hey, now.\" you whisper."
                hide 13newalex96
                show 13newalex97
                with dissolve
                m11 "\" What the...\""
                hide 13newalex97
                show 13newalex98
                with dissolve
                " A large knife appears in his hand, like a magic trick."
                hide 13newalex98
                show 13newalex99
                with dissolve
                " But before either you or he can act, Izzy jumps on his back."
                m11 "\" AAAAAAAA!!!\""
                " Sinking her teeth deep into his neck."
                m11 "\" AGGGGGG!!!\""
                hide 13newalex99
                show 13newalex101
                with dissolve
                " He falls writhing to the floor."
                m11 "\" AGGGHHHHH!!!\""
                m11 "\" Fuck!!\""
                hide 13newalex101
                show 13newalex102
                with dissolve
                " Isabella grabs the knife."
                hide 13newalex102
                show 13newalex103
                with dissolve
                i "\" You piece of shit!\" She screams, her teeth still bloody from the bite."
                m11 "\" No... No...\""
                m11 "\" I never meant you any harm.\""
                i "\" Never meant me any harm?\""
                i "\" Just Alex, right.\""
                m11 "\" No... I...\""
                hide 13newalex103
                show 13newalex104
                with dissolve
                " But before he can finish, Izzy drives the knife in his neck."
                i "\" Not meant me harm, eh!\""
                m11 "\" *Gurgle*\""
                i "\" Piece of shit!\""
                m11 "\" *Gurgle*\""
                p "\" He's dying Izzy.\""
                hide 13newalex104
                show 13newalex105
                with dissolve
                " She turns on you."
                " Anger in her eyes."
                p "\" Easy.\""
                p "\" Easy, now.\""
                p "\" It's me.\""
                hide 13newalex105
                show 13newalex106
                with dissolve
                i "\" It's you.\""
                p "\" Yeah.\""
                p "\" Easy, now.\""
                hide 13newalex106
                show 13newalex107
                with dissolve
                i "\" Ughh...\""
                " She starts spitting on the floor."
                i "\" Ptooey!\""
                p "\" Isabella.\""
                i "\" I'm going to throw up.\""
                hide 13newalex107
                show 13newalex108
                with dissolve
                " You look over at the man, and see that he's dead."
                p "\" Shit.\""
                hide 13newalex108
                show 13newalex109
                with dissolve
                p "\" Izzy. Are there any more?\""
                i "\" Ptooey.\""
                i "\" What?\""
                p "\" Are there any more?\""
                hide 13newalex109
                show 13newalex110
                with dissolve
                " She stands up."
                i "\" More?\""
                p "\" Did you see someone else, or just him?\""
                i "\" Just him.\""
                i "\" He kept saying 'we', though.\""
                p "\" Ok.\""
                p "\" How did he get you here?\""
                i "\" I'm not sure.\""
                i "\" I was going for cotton candy and...\""
                i "\" I don't remember anything after that.\""
                i "\" Just woke up here.\""
                p "\" He didn't tie you up?\""
                hide 13newalex110
                show 13newalex111
                with dissolve
                i "\" No.\""
                i "\" It was like he wanted to be my friend.\""
                p "\" Your friend?\""
                i "\" Yeah.\""
                p "\" Strange.\""
                p "\" Ok.\""
                p "\" We have to get out of here pretty quick. There's probably others.\""
                hide 13newalex111
                show 13newalex117
                with dissolve
                i "\" He's dead?\""
                p "\" Knife through throat usually does the trick.\""
                hide 13newalex117
                show 13newalex112
                with dissolve
                " She turns her back."
                i "\" Gonna be sick.\""
                p "\" Don't be sick.\""
                p "\" Not now.\""
                p "\" You can do that later.\""
                p "\" Now, I have to ask you.\""
                p "\" Does anyone have your fingerprints on file?\""
                hide 13newalex112
                show 13newalex111
                with dissolve
                i "\" What?\""
                p "\" Have you ever been arrested?\""
                i "\" No.\""
                p "\" No job application, where they ask for fingerprints?\""
                i "\" No.\""
                p "\" Are you sure?\""
                i "\" Yes.\""
                p "\" Good, that will make things easier.\""
                p "\" There's the spit and the bitemarks.\""
                p "\" But we can just send you to the dentist, and the DNA will be degraded.\""
                p "\" Don't have anything to compare it to anyway.\""
                i "\" What?\""
                p "\" Izzy, this is murder.\""
                hide 13newalex111
                show 13newalex112
                with dissolve
                i "\" *Barf*\""
                p "\" Ok.\""
                hide 13newalex112
                show 13newalex113
                with dissolve
                " She latches on to you."
                i "\" My God!\""
                i "\" What's going to happen?\""
                p "\" Nothing.\""
                p "\" Nothing if we're careful.\""
                hide 13newalex113
                show 13newalex114
                with dissolve
                i "\" Alex?\""
                p "\" I have her stashed away.\""
                p "\" Don't worry.\""
                p "\" We'll go to her soon.\""
                i "\" Are you sure?\""
                p "\" Why? Did he say something?\""
                i "\" No. He never really mentioned her, but...\""
                i "\" I mean...\""
                p "\" She's safe.\""
                p "\" Call her just to make sure.\""
                p "\" She's probably worried sick.\""
                i "\" Ok.\""
                p "\" But be careful what you say on the phone.\""
                i "\" Ok.\""
                p "\" And the knife.\""
                p "\" Give it to me.\""
                hide 13newalex114
                show 13newalex115
                with dissolve
                " She hands it over without complaint."
                i "\" What are we going to do with him?\""
                p "\" Go through his pockets, and see if I find anything.\""
                i "\" I mean...\""
                p "\" We'll just leave him here.\""
                i "\" Unburied?\""
                p "\" Don't worry.\""
                p "\" You just call Alex.\""
                hide 13newalex115
                show 13newalex116
                with dissolve
                " You go over to the body."
                hide 13newalex116
                show 13newalex119
                with dissolve
                i "\" Hey!\""
                i "\" Hey, it's me.\""
                hide 13newalex119
                show 13newalex118
                with dissolve
                p "\" Careful what you say.\""
                hide 13newalex118
                show 13newalex119
                with dissolve
                i "\" I need to be careful about what I say.\""
                i "\" Yeah...\""
                i "\" I was detoured by a guy. Someone I didn't know.\""
                hide 13newalex119
                show 13newalex120
                with dissolve
                " Going through his pockets, you find another knife, a wallet, a cell phone, and a USB stick."
                p "\" Perfect.\""
                hide 13newalex120
                show 13newalex140
                with dissolve
                " You focus on the stick."
                p "\" Must get that.\""
                hide 13newalex140
                show 13newalex119
                with dissolve
                i "\" Yeah...\""
                i "\" We're both fine.\""
                i "\" No, it's not your fault.\""
                hide 13newalex119
                show 13newalex118
                with dissolve
                " Going through his wallet, you manage to find an ID and some cash."
                p "\" John Johnson. Really?\""
                p "\" This is obviously bullshit.\""
                p "\" But the rest should prove more useful.\""
                hide 13newalex118
                show 13newalex119
                with dissolve
                i "\" We're on our way.\""
                i "\" Just hang tight.\""
                i "\" Love you too.\""
                p "\" Ready?\""
                hide 13newalex119
                show 13newalex121
                with dissolve
                " She hangs up."
                i "\" We're just going to leave?\""
                p "\" Yeah.\""
                p "\" Doubt law enforcement can trace this back to you.\""
                p "\" Didn't know the guy, and you don't have anything on file.\""
                p "\" Besides. I think 'we' will take care of this for us.\""
                hide 13newalex121
                show 13newalex122
                with dissolve
                i "\" She relaxes a bit.\""
                i "\" Thank you. For coming, you know...\""
                p "\" Yeah. Now we need to go.\""
                hide 13newalex122
                show 13newalex123
                with dissolve
                " You take one last look at the body."
                p "\" Motherfucker!\""
                hide 13newalex123
                show 13newalex124
                with dissolve
                i "\" Can I ask you...\""
                p "\" What?\""
                i "\" Don't tell her...\""
                i "\" You know...\""
                i "\" What I did.\""
                p "\" All on me.\""
                hide 13newalex124
                show 13newalex125
                with dissolve
                i "\" T-thank you.\""
                i "\" I don't want her to think that I...\""
                p "\" I get it.\""
                p "\" But to be honest, I should give you a job. Put you on the payroll.\""
                p "\" You're ruthless.\""
                p "\" Now let's fucking go!\""
                hide 13newalex125
                show 13newalex126
                with dissolve
                " You rush back to the hotel, at a brisk pace."
                hide 13newalex126
                show 13newalex127
                with dissolve
                " When you get there Alex is fretting."
                p "\" How are things here?\""
                a "\" Fine.\""
                p "\" They behaved themselves?\""
                a "\" Managed to calm them down.\""
                a "\" Told them we're hiding from my psycho ex.\""
                hide 13newalex127
                show 13newalex128
                with dissolve
                a "\" Now Gerald is very comforting.\""
                a "\" That or hitting on me.\""
                p "\" That piece of...\""
                a "\" We barged into his room!\""
                a "\" Be nice.\""
                a "\" Izzy?\""
                p "\" Right here.\""
                hide 13newalex128
                show 13newalex129
                with dissolve
                " The girls hug."
                a "\" Babe!\""
                a "\" Babe, are you ok?\""
                i "\" Yeah.\""
                i "\" Sorry. Didn't want to scare you.\""
                hide 13newalex129
                show 13newalex130
                with dissolve
                " Alex kisses Izzy's forehead."
                a "\" It's my fault, baby.\""
                i "\" No, it's not.\""
                a "\" Yes.\""
                a "\" It's because of who I am.\""
                hide 13newalex130
                show 13newalex131
                with dissolve
                " You go back to the elderly couple."
                p "\" We all good?\""
                ger "\" Why didn't you tell us the girl was hiding from her old ex.\""
                ger "\" Would've been happy to help.\""
                ger "\" I remember a girl in college.\""
                ger "\" What was her name? Maria, that's right.\""
                ger "\" She had a crazy ex...\""
                hide 13newalex131
                show 13newalex132
                with dissolve
                w1 "\" Stop it!\""
                w1 "\" Remember what he said to us?\""
                w1 "\" Now a pretty girl gives you a smile and a pat on the cheek, and you're best friends?\""
                hide 13newalex132
                show 13newalex133
                with dissolve
                ger "\" My wife doesn't understand.\""
                ger "\" Probably because she never really inspired such passion.\""
                w1 "\" WHAT???\""
                p "\" We'll just be going.\""
                hide 13newalex133
                show 13newalex134
                with dissolve
                p "\" Ready?\""
                a "\" We're going?\""
                p "\" Yeah.\""
                a "\" Back to our room?\""
                p "\" Just to get the luggage.\""
                p "\" We're not sleeping there again.\""
                hide 13newalex134
                show 13newalex135
                with dissolve
                a "\" Are we going home, then?\""
                p "\" Of course.\""
                p "\" But I need to get my boys over here first, though.\""
                p "\" We're leaving here with a guard.\""
                hide 13newalex135
                show 13newalex136
                with dissolve
                " You grab the girls and march them back to your room."
                a "\" Here we go again.\""
                a "\" We're coming. You don't have to bruise our arms.\""
                p "\" Hush.\""
                a "\" *Sigh*\""
                hide 13newalex136
                show 13newalex137
                with dissolve
                a "\" Who took her?\""
                p "\" Not sure yet. But I'll find out.\""
                a "\" Was it the same guys that came that night?\""
                p "\" Like I said. Not sure yet.\""
                hide 13newalex137
                show 13newalex138
                with dissolve
                p "\" Alright.\""
                p "\" Pack everything. And I mean everything.\""
                p "\" I'll check how much cash we have.\""
                a "\" Ok.\""
                hide 13newalex138
                show 13newalex139
                with dissolve
                " The girls divide duties, and soon you're all packed."
                hide 13newalex139
                show 13newalex141
                with dissolve
                a "\" Why don't we just go to the airport?\""
                p "\" Because there are likely others out there.\""
                a "\" We have you.\""
                p "\" And that may not be enough.\""
                a "\" So, where are we going then?\""
                p "\" Check on the internet where the hookers hang out around here.\""
                a "\" What?\""
                p "\" There must be some kind of motel near by for their clients.\""
                p "\" Some place that takes cash, and doesn't ask for ID.\""
                a "\" Ahh... I get it.\""
                hide 13newalex141
                show 13newalex142
                with dissolve
                i "\" Sorry about all this.\""
                i "\" If I didn't go for cotton candy...\""
                a "\" Don't be silly.\""
                hide 13newalex142
                show 13newalex144
                with dissolve
                a "\" One second.\""
                a "\" Found one.\""
                p "\" Ok.\""
                p "\" Let's get moving.\""
                hide 13newalex144
                show 13newalex143
                with dissolve
                " You grab the girls again, and head out."
                " This time Alex isn't complaining."
                hide 13newalex143
                show 13newalex145
                with dissolve
                " Must be getting used to it."
                hide 13newalex145
                show 13newalex146
                with dissolve
                a "\" Should we call my dad?\""
                p "\" Not yet.\""
                p "\" Not until I know more.\""
                hide 13newalex146
                show 13newalex147
                with dissolve
                " You finally get to the motel."
                hide 13newalex147
                show 13newalex148
                with dissolve
                a "\" Ok.\""
                a "\" So, this is crossing getting hepatitis of my bucket list.\""
                a "\" This place is...\""
                p "\" Off the map.\""
                hide 13newalex148
                show 13newalex149
                with dissolve
                " You go inside."
                hide 13newalex149
                show 13newalex150
                with dissolve
                p "\" Hey.\""
                m12 "\" Yes?\""
                p "\" Need a room.\""
                m12 "\" Sure.\""
                m12 "\" Will that be for one hour, or two?\""
                m12 "\" Couple of days.\""
                hide 13newalex150
                show 13newalex151
                with dissolve
                " He takes a look at the girls."
                hide 13newalex151
                show 13newalex152
                with dissolve
                m12 "\" Couple of days?\""
                m12 "\" The hell are you up to, man?\""
                p "\" Just give me the fucking key.\""
                m12 "\" Ok, ok...\""
                hide 13newalex152
                show 13newalex153
                with dissolve
                " As you go to the room, the guy stops Alex."
                m12 "\" Hey.\""
                m12 "\" You two are a lot cleaner than most of the girls that come here.\""
                a "\" What?\""
                m12 "\" Prettier too.\""
                a "\" Excuse me?\""
                m12 "\" When you're finished with the guy, you might want to come over.\""
                m12 "\" I can arrange for discounts in the future.\""
                hide 13newalex153
                show 13newalex154
                with dissolve
                " He barely finishes speaking and Izzy is trying to claw his eyes out."
                m12 "\" The fuck?\""
                m12 "\" What's wrong with you?\""
                i "\" You motherless...\""
                hide 13newalex154
                show 13newalex155
                with dissolve
                " Alex pulls her back."
                a "\" Easy, now.\""
                m12 "\" Crazy bitch!\""
                a "\" Let's go.\""
                a "\" Let's just go.\""
                hide 13newalex155
                show 13newalex156
                with dissolve
                " You get to the room."
                hide 13newalex156
                show 13newalex157
                with dissolve
                a "\" Wow.\""
                a "\" Much worse than I imagined.\""
                p "\" It's perfect.\""
                hide 13newalex157
                show 13newalex158
                with dissolve
                a "\" Really?\""
                p "\" Yes.\""
                p "\" Make yourselves comfortable.\""
                p "\" We'll be here til tomorrow at least.\""
                hide 13newalex158
                show 13newalex159
                with dissolve
                i "\" We could clean it up a bit.\""
                p "\" If you want.\""
                p "\" Just don't leave the room.\""
                p "\" NEVER leave the room.\""
                hide 13newalex159
                show 13newalex160
                with dissolve
                a "\" So, what happened?\""
                p "\" I'll let Izzy tell you.\""
                a "\" Who were they?\""
                p "\" I'm not sure yet.\""
                p "\" Can you give me your laptop, please?\""
                a "\" Sure.\""
                hide 13newalex160
                show 13newalex161
                with dissolve
                i "\" Do we have a bathroom?\""
                a "\" There has to be.\""
                i "\" That we'll definitely need to clean.\""
                i "\" We'll be using it.\""
                a "\" I have some wipes.\""
                p "\" Laptop?\""
                hide 13newalex161
                show 13newalex162
                with dissolve
                a "\" Sure.\""
                " She hands it over."
                hide 13newalex162
                show 13newalex163
                with dissolve
                " You pull out the USB stick."
                hide 13newalex163
                show 13newalex164
                with dissolve
                p "\" Ok.\""
                p "\" Let's see what's on this.\""
                hide 13newalex164
                show 13newalex165
                with dissolve
                " The girls go in the bathroom."
                a "\" Oh, my God.\""
                a "\" Smells like shit.\""
                a "\" Literally.\""
                i "\" Maybe we can just hold it in.\""
                hide 13newalex165
                show 13newalex168
                with dissolve
                " You plug in the stick."
                p "\" The fuck?\""
                p "\" Izzy?\""
                hide 13newalex168
                show 13newalex169
                with dissolve
                p "\" In front of their school.\""
                hide 13newalex169
                show 13newalex170
                with dissolve
                p "\" Inside the school?\""
                " Nothing but pics of Izzy."
                hide 13newalex170
                show 13newalex171
                with dissolve
                " The only pic you found of Alex was in front of your building ,and Izzy was in it too."
                p "\" The fuck?\""
                p "\" They're after her?\""
                hide 13newalex171
                show 13newalex172
                with dissolve
                a "\" Hey!\""
                hide 13newalex172
                show 13newalex164
                with dissolve
                " You quickly close the laptop and put the stick back in your pocket."
                hide 13newalex164
                show 13newalex172
                with dissolve
                p "\" Yeah?\""
                a "\" We can kinda clean the toilet.\""
                a "\" But the shower?\""
                a "\" Seriously. You'll get sick if you use that.\""
                p "\" Whatever.\""
                hide 13newalex172
                show 13newalex173
                with dissolve
                a "\" Can you get off the bed for a second?\""
                a "\" Let me see what I can do with it.\""
                p "\" Sure.\""
                hide 13newalex173
                show 13newalex174
                with dissolve
                " She takes clothes out of the luggage and throws them all over the bed."
                hide 13newalex174
                show 13newalex175
                with dissolve
                a "\" Well, it's not great.\""
                a "\" But at least we don't have to touch it.\""
                i "\" It's just a dirty bed, Alex.\""
                a "\" I know.\""
                hide 13newalex175
                show 13newalex176
                with dissolve
                a "\" Were they going to hurt her?\""
                a "\" Izzy, I mean?\""
                p "\" I don't know.\""
                a "\" It's all because of me, right?\""
                a "\" Because of my dad?\""
                p "\" Maybe.\""
                hide 13newalex176
                show 13newalex177
                with dissolve
                " She hugs you."
                a "\" *Sniff*\""
                p "\" Hey. Easy.\""
                a "\" *Sniff*\""
                a "\" I'm not good for people.\""
                a "\" *Sniff*\""
                hide 13newalex177
                show 13newalex178
                with dissolve
                " You gently kiss her."
                p "\" It's ok,\""
                a "\" *Sniff*\""
                p "\" Not your fault. Trust me.\""
                a "\" Just...\""
                a "\" Just give me a second...\""
                a "\" *Sniff*\""
                hide 13newalex178
                show 13newalex179
                with dissolve
                " It takes her a couple of minutes to compose herself."
                a "\" You know, I'll understand.\""
                p "\" Understand what?\""
                a "\" If you have second thoughts.\""
                a "\" About the whole dream thing. About me.\""
                a "\" You already got stabbed once.\""
                p "\" That was my fault.\""
                a "\" Still.\""
                p "\" I'll always be here, ok?\""
                hide 13newalex179
                show 13newalex180
                with dissolve
                a "\" Thanks.\""
                p "\" And sorry about manhandling you today.\""
                p "\" Well, maybe I'm not sorry.\""
                p "\" But I didn't have patience for...\""
                a "\" I get it.\""
                a "\" You don't want to always explain.\""
                a "\" I'll listen to you more from now on.\""
                hide 13newalex180
                show 13newalex181
                with dissolve
                " Izzy comes out of the bathroom."
                i "\" I did the best I could.\""
                a "\" I'm sure.\""
                hide 13newalex181
                show 13newalex182
                with dissolve
                " The girls get on the bed."
                hide 13newalex182
                show 13newalex183
                with dissolve
                i "\" When can we get out of here.\""
                p "\" Tomorrow.\""
                p "\" I'll call my guys right now, and tomorrow we're heading home.\""
                hide 13newalex183
                show 13newalex184
                with dissolve
                a "\" Dad?\""
                p "\" Don't want to panic him.\""
                p "\" When I have you home and safe, you can tell him everything.\""
                p "\" Now, both of you try to catch some sleep.\""
                p "\" You must be exhausted.\""
                a "\" And you?\""
                p "\" I'll be fine.\""
                a "\" You shouldn't stay up all night.\""
                p "\" Alex?\""
                p "\" What did you say about listening to me more?\""
                a "\" Got it.\""
                hide 13newalex184
                show 13newalex185
                with dissolve
                " The girls get on the bed and try to get some sleep."
                hide 13newalex185
                show 13newalex186
                with dissolve
                " Meanwhile, you call your boys and tell them to come over here."
                hide 13newalex186
                show 13newalex187
                with dissolve
                a "\" When are they coming over?\""
                p "\" Tomorrow.\""
                p "\" Now get some sleep.\""
                hide 13newalex187
                show 13newalex188
                with dissolve
                a "\" And my dad?\""
                p "\" No.\""
                a "\" Why?\""
                p "\" *Sigh*\""
                p "\" Who knew we were coming over here?\""
                p "\" Now, maybe they got your name from the reservation, and maybe no.\""
                hide 13newalex188
                show 13newalex189
                with dissolve
                a "\" You're not saying...\""
                p "\" All I'm saying is that I have my suspicions.\""
                p "\" Your dad too.\""
                p "\" The smaller the circle right now, the better.\""
                hide 13newalex189
                show 13newalex190
                with dissolve
                " She lies back down."
                a "\" And your boys?\""
                a "\" Do you trust them?\""
                p "\" No.\""
                a "\" Ok.\""
                hide 13newalex190
                show 13newalex191
                with dissolve
                " Night eventually comes, and the girls fall asleep."
                hide 13newalex191
                show 13newalex192
                with dissolve
                " You didn't sleep, though."
                " Thoughts of why was Izzy on the USB stick and not Alex kept going through your head."
                hide 13newalex192
                show 13newalex194
                with dissolve
                " And so the night passes."
                " And next morning."
                " Wasn't till near noon that you hear a knock on the door."
                " *Knock* *Knock*"
                hide 13newalex194
                show 13newalex193
                with dissolve
                " Izzy immediately opens her eyes."
                i "\" Who's that?\""
                i "\" Your men?\""
                p "\" I hope so.\""
                p "\" Stay here. I'll go see.\""
                hide 13newalex193
                show 13newalex195
                with dissolve
                " You go outside."
                hu "\" Boss?\""
                ja "\" What happened?\""
                p "\" Nothing.\""
                p "\" You have a car?\""
                ja "\" Of course.\""
                p "\" Let's go, then.\""
                p "\" We'll get the tickets at the airport.\""
                hide 13newalex195
                show 13newalex196
                with dissolve
                " You go back inside."
                i "\" Who is it?\""
                a "\" If it wasn't his boys, he wouldn't just walk in here.\""
                p "\" You're right.\""
                p "\" Grab your things.\""
                p "\" Let's go.\""
                hide 13newalex196
                show back1
                with dissolve
                show 13newalex197
                with dissolve
                " You pack the girls in the car, and are headed for the airport."
                hide 13newalex197
                show 13newalex198
                with dissolve
                ja "\" Cutting your vacation short, boss?\""
                p "\" Yeah.\""
                ja "\" If you don't mind me asking...\""
                ja "\" What kinda dingy motel did we pick you up at?\""
                ja "\" I mean. Surely you can afford...\""
                p "\" I mind you asking!\""
                ja "\" Sorry.\""
                hide 13newalex198
                show 13newalex199
                with dissolve
                " Looking at the girls, Izzy seemed almost untroubled by the events."
                " Almost serene."
                hide 13newalex199
                show 13newalex200
                with dissolve
                " Alex on the other hand was still nervous."
                " Fidgeting left and right."
                hide 13newalex200
                show 13newalex201
                with dissolve
                " Making nonsense conversation with James and Hugo."
                " Maybe the proximity to the violence unnerved her."
                " Or maybe the possibility that Izzy would be in the mix."
                hide 13newalex201
                show 13newalex202
                with dissolve
                " On the way back home, the girls sat hand in hand the whole trip."
                hide 13newalex202
                show 13newalex203
                with dissolve
                " With Alex looking lovingly at Izzy."
                hide 13newalex203
                show 13newalex204
                with dissolve
                " And you alone with your thoughts."
                hide 13newalex204
                show 13newalex205
                with dissolve
                " But eventually you get back home."
                i "\" I should go see momma.\""
                p "\" Not just yet.\""
                p "\" We stop by the villa first.\""
                hide 13newalex205
                show 13newalex206
                with dissolve
                ja "\" Where to?\""
                p "\" Big boss's place.\""
                ja "\" Got it.\""
                hide 13newalex206
                show 13newalex207
                with dissolve
                " They drive you over."
                hide 13newalex207
                show 13newalex208
                with dissolve
                ja "\" Pick you up back here tomorrow?\""
                p "\" No.\""
                p "\" See you back at the agency.\""
                ja "\" If you say so.\""
                hide 13newalex208
                show 13newalex209
                with dissolve
                a "\" Dad?\""
                a "\" Dad, we're back!\""
                a "\" Where is he?\""
                a "\" Daaaaaddddd!\""
                hide 13newalex209
                show 13newalex267
                with dissolve
                " She decides to call him."
                a "\" Hey!\""
                a "\" Where am I? Home.\""
                a "\" No. Decided to cut our trip a little short.\""
                a "\" Where are you?\""
                a "\" I know you're out. Where?\""
                a "\" *Sigh*\""
                a "\" So, when will you be back?\""
                a "\" Ok... Ok...\""
                a "\" Love you too.\""
                hide 13newalex267
                show 13newalex211
                with dissolve
                a "\" Says he's out.\""
                a "\" Business.\""
                a "\" Won't be back tonight.\""
                p "\" That's fine.\""
                p "\" You have plenty of guards here.\""
                a "\" What do we tell him?\""
                p "\" Nothing.\""
                p "\" Nothing for now.\""
                p "\" We came back early cause we got bored.\""
                a "\" Ok.\""
                hide 13newalex211
                show 13newalex210
                with dissolve
                i "\" I really need to go se momma.\""
                a "\" Yes, of course.\""
                a "\" [player_name] will take you.\""
                p "\" Sure.\""
                p "\" And I'll spend the night over there too.\""
                if izzyin == True:
                    hide 13newalex210
                    show 13newalex212
                    with dissolve
                    i "\" You don't have to.\""
                    p "\" Alex has plenty of guards here.\""
                    p "\" You don't.\""
                    hide 13newalex212
                    show 13newalex215
                    with dissolve
                    a "\" He's right.\""
                    a "\" And we need to start listening to him more.\""
                    i "\" I'm not the one who's always a contrarian.\""
                    i "\" But yeah.\""
                    hide 13newalex215
                    show 13newalex214
                    with dissolve
                    a "\" Come back here tomorrow?\""
                    p "\" First thing.\""
                    p "\" Both of us.\""
                    a "\" Thanks.\""
                    hide 13newalex214
                    show 13newalex217
                    with dissolve
                    a "\" It's gonna be ok.\""
                    a "\" We'll figure this out.\""
                    i "\" I know.\""
                    hide 13newalex217
                    show 13newalex218
                    with dissolve
                    " She gives you a kiss as you leave."
                    a "\" Tomorrow.\""
                    p "\" Tomorrow.\""
                    hide 13newalex218
                    show 13newalex219
                    with dissolve
                    a "\" Take care of her.\""
                    p "\" Both of you.\""
                    a "\" Thanks.\""
                    hide 13newalex219
                    show back1
                    with dissolve
                    show 13newalex216
                    with dissolve
                    " On your way over, Izzy is very quiet."
                    p "\" You ok?\""
                    i "\" Yeah.\""
                    i "\"... ...\""
                    i "\" Do you honestly think I'm in danger?\""
                    p "\" Yeah.\""
                    i "\" Fuck.\""
                    hide 13newalex216
                    show 13newalex221
                    with dissolve
                    " You get to her place."
                    i "\" I only hope momma hasn't turned the place upside down."
                    hide 13newalex221
                    show 13newalex222
                    with dissolve
                    ag "\" I knew you'd come.\""
                    p "\" Whoa.\""
                    i "\" MOM!!!\""
                    ag "\" I knew you couldn't stay away forever.\""
                    hide 13newalex222
                    show 13newalex223
                    with dissolve
                    i "\" MOM!!!\""
                    i "\" What the hell???\""
                    hide 13newalex223
                    show 13newalex224
                    with dissolve
                    ag "\" Hush, dear. I'm speaking to your father.\""
                    ag "\" Finally had enough of her?\" she says addressing you."
                    ag "\" She never loved you like I did.\""
                    hide 13newalex224
                    show 13newalex225
                    with dissolve
                    " Isabella physically grabs her and pulls her away."
                    ag "\" Stop it, girl.\""
                    ag "\" Me and your father have to talk.\""
                    i "\" Daddy's not here!\""
                    i "\" Come!\""
                    hide 13newalex225
                    show 13newalex226
                    with dissolve
                    p "\" Wow.\""
                    p "\" What was... Yeah...\""
                    hide 13newalex226
                    show 13newalex227
                    with dissolve
                    " She comes back clutching her head."
                    i "\" That was... Mortifying.\""
                    i "\" Sorry.\""
                    p "\" It's fine.\""
                    hide 13newalex227
                    show 13newalex228
                    with dissolve
                    i "\" Guess you're used to my crazy mom by now.\""
                    p "\" A bit.\""
                    i "\" Still embarrassing, though.\""
                    p "\" Not in front of me.\""
                    hide 13newalex228
                    show 13newalex229
                    with dissolve
                    p "\" But I want to know.\""
                    p "\" How come you're not affected.\""
                    p "\" I mean, you almost got killed.\""
                    i "\" I don't think so.\""
                    hide 13newalex229
                    show 13newalex230
                    with dissolve
                    i "\" I knew you'd come.\""
                    p "\" You knew.\""
                    p "\" How?\""
                    i "\" I don't know.\""
                    i "\" I just knew.\""
                    hide 13newalex230
                    show 13newalex231
                    with dissolve
                    i "\" You love me, right?\""
                    p "\" Of course.\""
                    i "\" See?\""
                    i "\" So, I knew you'd come.\""
                    hide 13newalex231
                    show 13newalex232
                    with dissolve
                    " You give her a kiss on the forehead."
                    p "\" About the guy...\""
                    p "\" You'll tell me if you have nightmares about it.\""
                    hide 13newalex232
                    show 13newalex233
                    with dissolve
                    " She kisses you back on the chin."
                    i "\" He was going to hurt Alex.\""
                    i "\" And maybe you too.\""
                    i "\" I won't have any nightmares.\""
                    p "\" Brave girl.\""
                    i "\" Or sociopath.\""
                    p "\" No. No, you're not that.\""
                    i "\" Let me just go take a shower.\""
                    p "\" Sure.\""
                    hide 13newalex234
                    show 13newalex235
                    with dissolve
                    " While she's gone, you look through the stick again."
                    p "\" Nope...\""
                    p "\" Just pictures of her.\""
                    i "\" Hey!\""
                    hide 13newalex235
                    show 13newalex236
                    with dissolve
                    p "\" Yes?\""
                    hide 13newalex236
                    show 13newalex237
                    with dissolve
                    " You slam the laptop shut."
                    hide 13newalex237
                    show 13newalex236
                    with dissolve
                    i "\" I put momma to bed.\""
                    hide 13newalex236
                    show 13newalex238
                    with dissolve
                    " She comes to sit down next to you."
                    i "\" What happens now?\""
                    p "\" Now, things go on as usual.\""
                    p "\" Except I'll have guards for you and Alex.\""
                    hide 13newalex238
                    show 13newalex239
                    with dissolve
                    i "\" And you're going to find them?\""
                    p "\" Oh, yes.\""
                    p "\" I have a phone. A stick. I'll find them.\""
                    i "\" Good.\""
                    hide 13newalex239
                    show 13newalex240
                    with dissolve
                    i "\" Now are you coming to bed?\""
                    p "\" After not sleeping last night?\""
                    p "\" Oh yes.\""
                    hide 13newalex240
                    show 13newalex244
                    with dissolve
                    " You go to the bedroom."
                    i "\" Let me just get these things off.\""
                    i "\" Better call Alex too.\""
                    hide 13newalex244
                    show 13newalex246
                    with dissolve
                    i "\" Hey.\""
                    i "\" Yeah.\""
                    i "\" Just getting ready for bed.\""
                    i "\" I don't think so. He'll just have to sleep naked.\""
                    i "\" No, I'll let him sleep.\""
                    i "\" Yeah.\""
                    i "\" Sure. I'll put him on.\""
                    hide 13newalex246
                    show 13newalex247
                    with dissolve
                    a "\" Hey!\""
                    p "\" Yes?\""
                    a "\" You get some sleep now, you hear me?\""
                    a "\" You can sex Izzy up in the morning if you have to.\""
                    a "\" But you didn't get to sleep last night.\""
                    p "\" Well, I wasn't planning to, but now that you mention it.\""
                    a "\" In the morning.\""
                    a "\" Get some sleep.\""
                    p "\" You too.\""
                    a "\" Goodnight.\""
                    p "\" Goodnight.\""
                    hide 13newalex247
                    show 13newalex245
                    with dissolve
                    i "\" You coming to bed?\""
                    p "\" Yeah.\""
                    i "\" I don't have any pajamas for you, but don't get your hopes up.\""
                    i "\" Under strict instructions to make sure you sleep.\""
                    hide 13newalex245
                    show 13newalex248
                    with dissolve
                    " You get into bed with her."
                    p "\" Always trying to be the boss.\""
                    i "\" it's in her nature.\""
                    i "\" And she's right.\""
                    hide 13newalex248
                    show 13newalex249
                    with dissolve
                    i "\" Love you, puppy.\""
                    p "\" Love you too.\""
                    hide 13newalex249
                    show 13newalex250
                    with dissolve
                    " Not sleeping the night before has you exhausted and you're quickly sleeping."
                    hide 13newalex268
                    show blackscreen
                    with dissolve
                    "..."
                    "... ..."
                    "... ... ..."
                    hide blackscreen
                    show 13newalex251
                    with dissolve
                    " You open your eyes a few hours later."
                    i "\" I just coughed.\""
                    i "\" Did I wake you?\""
                    p "\" No.\""
                    p "\" Thirsty.\""
                    i "\" Want me to get you something.\""
                    p "\" I'll go get it.\""
                    i "\" The kitchen. Fridge.\""
                    p "\" Figured.\""
                    p "\" I'll be right back.\""
                    hide 13newalex251
                    show 13newalex253
                    with dissolve
                    " You walk naked to the fridge."
                    p "\" Some orange juice.\""
                    p "\" That would be best.\""
                    p "\" Milk, maybe?\""
                    ag "\" Boris!\""
                    p "\" What?\""
                    hide 13newalex253
                    show 13newalex254
                    with dissolve
                    " In a flash, Agatha is there."
                    " Naked and with her arms around you."
                    p "\" Lady!\""
                    ag "\" My sweet, Boris.\""
                    p "\" Mrs. Agatha, you need to go back to your bedroom.\""
                    hide 13newalex254
                    show 13newalex255
                    with dissolve
                    ag "\" The kid's asleep, my love.\""
                    ag "\" She won't hear us.\""
                    ag "\" I missed you so much.\""
                    ag "\" Your eyes, your lips, your dick...\""
                    p "\" Get off me!\" You say, pushing her back."
                    hide 13newalex255
                    show 13newalex256
                    with dissolve
                    ag "\" Why?\""
                    ag "\" Don't you love me anymore?\""
                    ag "\" Mrs. Agatha! You need to go to bed.\""
                    hide 13newalex256
                    show 13newalex257
                    with dissolve
                    ag "\" What has she done to you?\""
                    ag "\" That piss haired bitch!\""
                    p "\" GO TO BED!\""
                    ag "\" FINE!\""
                    hide 13newalex257
                    show 13newalex258
                    with dissolve
                    " She pulls away on her own this time."
                    ag "\" Just remember.\""
                    ag "\" Isabella is MY daughter. Not yours.\""
                    ag "\" I don't care you squirted her inside me.\""
                    ag "\" She's mine, you understand?\""
                    p "\" Fine.\""
                    p "\" Now, go.\""
                    " She scurries away."
                    hide 13newalex258
                    show 13newalex259
                    with dissolve
                    p "\" Shit!\""
                    p "\" Crazy woman.\""
                    p "\" She did call me Boris, though....\""
                    p "\" And said I squirted Izzy inside her.\""
                    p "\" Does that mean...\""
                    menu:
                        " Izzy and Alex are half sisters {color=#0f0}\[SistersKnow\]":
                            $ sistersknow = True
                            p "\" Holy shit!\""
                            p "\" And they're...\""
                            p "\" Fuck!\""
                            p "\" How do I deal with this?\""
                            p "\" Shit.\""
                            hide 13newalex259
                            show 13newalex260
                            with dissolve
                            " You drink your orange juice and get back to bed."
                            " Izzy is asleep again."
                            p "\" *Sigh*\""
                            hide 13newalex260
                            show 13newalex261
                            with dissolve
                            p "\" Could I ever tell you?\""
                            p "\" Poor thing.\""
                            p "\" No.\""
                            p "\" I have to keep my mouth shut for now.\""
                            jump ep14
                            scene end
                            with dissolve
                            $ renpy.pause ()
                            $ MainMenu(confirm=False)()


                        " It's just the ramblings of an old woman":
                            p "\" Nah...\""
                            p "\" Just some crazy old woman.\""
                            hide 13newalex259
                            show 13newalex260
                            with dissolve
                            " You drink your orange juice and get back to bed."
                            " Izzy is asleep again."
                            hide 13newalex260
                            show 13newalex261
                            with dissolve
                            p "\" Poor thing.\""
                            p "\" Your crazy mother must drive you up the walls.\""
                            jump ep14
                            scene end
                            with dissolve
                            $ renpy.pause ()
                            $ MainMenu(confirm=False)()



                else:
                    hide 13newalex210
                    show 13newalex213
                    with dissolve
                    i "\" Spend the night?\""
                    i "\" Why?\""
                    p "\" Alex has plenty of guards here.\""
                    p "\" You don't.\""
                    hide 13newalex213
                    show 13newalex215
                    with dissolve
                    a "\" He's right.\""
                    a "\" And be nicer to him.\""
                    i "\" I wasn't...\""
                    i "\" Yeah.\""
                    hide 13newalex215
                    show 13newalex214
                    with dissolve
                    a "\" Come back here tomorrow?\""
                    p "\" First thing.\""
                    p "\" Both of us.\""
                    a "\" Thanks.\""
                    hide 13newalex214
                    show 13newalex217
                    with dissolve
                    a "\" It's gonna be ok.\""
                    a "\" We'll figure this out.\""
                    i "\" I know.\""
                    hide 13newalex217
                    show 13newalex218
                    with dissolve
                    " She gives you a kiss as you leave."
                    a "\" Tomorrow.\""
                    p "\" Tomorrow.\""
                    hide 13newalex218
                    show 13newalex219
                    with dissolve
                    a "\" Take care of her.\""
                    p "\" Both of you.\""
                    a "\" Thanks.\""
                    hide 13newalex219
                    show back1
                    with dissolve
                    show 13newalex216
                    with dissolve
                    " On your way over, Izzy is very quiet."
                    p "\" You ok?\""
                    i "\" Yeah.\""
                    i "\"... ...\""
                    i "\" Do you honestly think I'm in danger?\""
                    p "\" Yeah.\""
                    i "\" Fuck.\""
                    hide 13newalex216
                    show 13newalex221
                    with dissolve
                    " You get to her place."
                    i "\" I only hope momma hasn't turned the place upside down."
                    hide 13newalex221
                    show 13newalex222
                    with dissolve
                    ag "\" I knew you'd come.\""
                    p "\" Whoa.\""
                    i "\" MOM!!!\""
                    ag "\" I knew you couldn't stay away forever.\""
                    hide 13newalex222
                    show 13newalex223
                    with dissolve
                    i "\" MOM!!!\""
                    i "\" What the hell???\""
                    hide 13newalex223
                    show 13newalex224
                    with dissolve
                    ag "\" Hush, dear. I'm speaking to your father.\""
                    ag "\" Finally had enough of her?\" She says, addressing you."
                    ag "\" She never loved you like I did.\""
                    hide 13newalex224
                    show 13newalex225
                    with dissolve
                    " Isabella physically grabs her and pulls her away."
                    ag "\" Stop it, girl.\""
                    ag "\" Me and your father have to talk.\""
                    i "\" Daddy's not here!\""
                    i "\" Come!\""
                    hide 13newalex225
                    show 13newalex226
                    with dissolve
                    p "\" Wow.\""
                    p "\" What was... Yeah...\""
                    hide 13newalex226
                    show 13newalex227
                    with dissolve
                    " She comes back clutching her head."
                    i "\" That was... Mortifying.\""
                    i "\" Sorry.\""
                    p "\" It's fine.\""
                    hide 13newalex227
                    show 13newalex234
                    with dissolve
                    i "\" I apologize, really.\""
                    p "\" You don't have to.\""
                    i "\" Thanks.\""
                    i "\" I'll just unpack and take a shower then, if you don't mind.\""
                    p "\" Sure.\""
                    hide 13newalex234
                    show 13newalex235
                    with dissolve
                    " While she's gone, you look through the stick again."
                    p "\" Nope...\""
                    p "\" Just pictures of her.\""
                    i "\" Hey!\""
                    hide 13newalex235
                    show 13newalex236
                    with dissolve
                    p "\" Yes?\""
                    hide 13newalex236
                    show 13newalex237
                    with dissolve
                    " You slam the laptop shut."
                    hide 13newalex237
                    show 13newalex236
                    with dissolve
                    i "\" Hungry?\""
                    i "\" Thirsty?\""
                    p "\" No.\""
                    p "\" No, I'm good.\""
                    i "\" Let me just get you some sheets or something.\""
                    hide 13newalex236
                    show 13newalex262
                    with dissolve
                    " She makes your bed on the couch."
                    hide 13newalex262
                    show 13newalex236
                    with dissolve
                    i "\" Well, if you do get hungry or thirsty, there's stuff in the fridge.\""
                    p "\" Thanks.\""
                    i "\" Goodnight.\""
                    p "\" Goodnight.\""
                    hide 13newalex236
                    show 13newalex268
                    with dissolve
                    " You get undressed and get ready for bed."
                    " Not sleeping the night before has you exhausted and you're quickly sleeping."
                    hide 13newalex268
                    show blackscreen
                    with dissolve
                    "..."
                    "... ..."
                    "... ... ..."
                    hide blackscreen
                    show 13newalex252
                    with dissolve
                    " When you open your eyes again, is late at night."
                    p "\" Damn.\""
                    p "\" Thirsty.\""
                    p "\" The fridge, she said.\""
                    hide 13newalex252
                    show 13newalex253
                    with dissolve
                    " You walk naked to the fridge."
                    p "\" Some orange juice.\""
                    p "\" That would be best.\""
                    p "\" Milk, maybe?\""
                    ag "\" Boris!\""
                    p "\" What?\""
                    hide 13newalex253
                    show 13newalex254
                    with dissolve
                    " In a flash, Agatha is there."
                    " Naked and with her arms around you."
                    p "\" Lady!\""
                    ag "\" My sweet, Boris.\""
                    p "\" Mrs. Agatha, you need to go back to your bedroom.\""
                    hide 13newalex254
                    show 13newalex255
                    with dissolve
                    ag "\" The kid's asleep, my love.\""
                    ag "\" She won't hear us.\""
                    ag "\" I missed you so much.\""
                    ag "\" Your eyes, your lips, your dick...\""
                    p "\" Get off me!\" You say, pushing her back."
                    hide 13newalex255
                    show 13newalex256
                    with dissolve
                    ag "\" Why?\""
                    ag "\" Don't you love me anymore?\""
                    ag "\" Mrs. Agatha! You need to go to bed.\""
                    hide 13newalex256
                    show 13newalex257
                    with dissolve
                    ag "\" What has she done to you?\""
                    ag "\" That piss haired bitch!\""
                    p "\" GO TO BED!\""
                    ag "\" FINE!\""
                    hide 13newalex257
                    show 13newalex258
                    with dissolve
                    " She pulls away on her own this time."
                    ag "\" Just remember.\""
                    ag "\" Isabella is MY daughter. Not yours.\""
                    ag "\" I don't care you squirted her inside me.\""
                    ag "\" She's mine, you understand?\""
                    p "\" Fine.\""
                    p "\" Now, go.\""
                    " She scurries away."
                    hide 13newalex258
                    show 13newalex259
                    with dissolve
                    p "\" Shit!\""
                    p "\" Crazy woman.\""
                    p "\" She did call me Boris, though...\""
                    p "\" And said I squirted Izzy inside her.\""
                    p "\" Does that mean...\""
                    menu:
                        " Izzy and Alex are half sisters":
                            $ sistersknow = True
                            p "\" Holy shit!\""
                            p "\" And they're...\""
                            p "\" Fuck!\""
                            p "\" How do I deal with this?\""
                            hide 13newalex259
                            show 13newalex269
                            with dissolve
                            p "\" Could I ever tell them?\""
                            p "\" Poor things.\""
                            p "\" No.\""
                            p "\" I have to keep my mouth shut for now.\""
                            jump ep14
                            scene end
                            with dissolve
                            $ renpy.pause ()
                            $ MainMenu(confirm=False)()

                        " It's just the ramblings of an old woman":
                            p "\" Nah...\""
                            p "\" Just some crazy old woman.\""
                            hide 13newalex259
                            show 13newalex269
                            with dissolve
                            p "\" Imagine living with this old nutty woman.\""
                            p "\" Poor Isabella.\""
                            jump ep14
                            scene end
                            with dissolve
                            $ renpy.pause ()
                            $ MainMenu(confirm=False)()
