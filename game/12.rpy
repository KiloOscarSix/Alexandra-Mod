label ep12alicehome:
                scene back1
                with dissolve
                show 6newalex203
                with dissolve
                " You head out to the car."
                " With nothing else to do, you pick up the girls and take them to the villa."
                jump ep12cont1

label ep12alice:
                scene back1
                with dissolve
                show 12newalex1
                with dissolve
                " You go to the car, and soon after alice follows."
                if alicesex == True:
                    p "\" So, I'll wait for your call?\""
                    ali "\" That will work.\""
                    p "\" Where do I drop you off.\""
                    ali "\" Anywhere.\""
                    hide 12newalex1
                    show 12newalex2
                    with dissolve
                    ali "\" But it's that it?\""
                    p "\" What?\""
                    ali "\" That's all you're going to leave me with?\""
                    p "\" Oh.\""
                    hide 12newalex2
                    show 12newalex3
                    with dissolve
                    " You give her a kiss before dropping her off."
                    hide 12newalex3
                    show 6newalex203
                    with dissolve
                    " And with nothing else to do, you pick up the girls and take them to the villa."
                    jump ep12cont1


                else:
                    p "\" So, I'll wait for your call?\""
                    ali "\" That will work.\""
                    p "\" Ok.\""
                    ali "\" Drop me off?\""
                    p "\" Sure.\""
                    hide 11newalex226
                    show 6newalex203
                    with dissolve
                    " You drop Alice off."
                    " And with nothing else to do, you pick up the girls and take them to the villa."
                    jump ep12cont1


label ep12lenny:
                scene back1
                with dissolve
                show 11newalex226
                with dissolve
                " You head out to the car."
                " And soon after, Lenny joins you."
                p "\" So, I'll wait for your call?\""
                lenny "\" That will work.\""
                p "\" Ok.\""
                lenny "\" Drop me off?\""
                p "\" Sure.\""
                hide 11newalex226
                show 6newalex203
                with dissolve
                " You drop Lenny off."
                " And with nothing else to do, you pick up the girls and take them to the villa."
                jump ep12cont1

label ep12alice2:
                scene back1
                with dissolve
                show 6newalex203
                with dissolve
                " With nothing else to do, you pick up the girls and take them to the villa."
                jump ep12cont1

label ep12cont1:
                scene 12newalex4
                with dissolve
                " That evening, you check on them before going to bed."
                a "\" We're gonna need to go shopping tomorrow.\""
                i "\" Why?\""
                a "\" Our plane is the day after.\""
                a "\" We need to get stuff for our trip.\""
                i "\" Clothes?\""
                a "\" Yeah.\""
                i "\" If you don't have enough stuff, no one does.\""
                a "\" Still.\""
                show 12newalex5
                with dissolve
                a "\" Besides. I need to get [player_name] some stuff.\""
                p "\" What?\""
                a "\" Some summer clothes.\""
                a "\" Do you even own vacation clothes?\""
                p "\" Are they different from normal clothes?\""
                hide 12newalex5
                show 12newalex6
                with dissolve
                i "\" They are in Alex's world.\""
                a "\" In every world.\""
                p "\" Hmmm...\""
                p "\" Don't think so.\""
                hide 12newalex6
                show 12newalex5
                with dissolve
                a "\" I do.\""
                a "\" And what do you know about clothes anyway?\""
                p "\" I wear them?\""
                a "\" Exactly.\""
                a "\" You know nothing.\""
                p "\" Whatever.\""
                p "\" I'd best be heading to bed.\""
                hide 12newalex5
                show 12newalex7
                with dissolve
                a "\" See you later, then.\""
                a "\" I'll be there after dad is asleep.\""
                p "\" I don't need you to tuck me in, Alex.\""
                a "\" But...\""
                p "\" I'm fine.\""
                hide 12newalex7
                show 12newalex8
                with dissolve
                a "\" Ok.\""
                a "\" Good night kiss?\""
                hide 12newalex8
                show 12newalex9
                with dissolve
                " You give her a kiss on the forehead."
                a "\" He he...\""
                a "\" I like that.\""
                if izzyin == True:
                    hide 12newalex9
                    show 12newalex10
                    with dissolve
                    i "\" Hey!\""
                    i "\" Don't I get a good night kiss.\""
                    p "\" Of course.\""
                    hide 12newalex10
                    show 12newalex11
                    with dissolve
                    " As you lean in, she grabs you and pulls you on top of her."
                    i "\" Mmm...\""
                    p "\" Oh..\""
                    p "\" Ok.\""
                    hide 12newalex11
                    show 12newalex12
                    with dissolve
                    a "\" Not that I'm not happy about you two getting along. But this isn't the time.\""
                    i "\" Mmm...\""
                    a "\" Don't make me bring out the hose now.\""
                    i "\" Fine.\""
                    hide 12newalex12
                    show 12newalex11
                    with dissolve
                    " She lets you go."
                    i "\" Good night.\""
                    p "\" Good night.\""
                    jump ep12cont2

                else:
                    jump ep12cont2

label ep12cont2:
                scene 12newalex237
                with dissolve
                " You go to your room and go to sleep."
                show blackscreen
                with dissolve
                "..."
                "... ..."
                " You're waken by the sounds of footsteps."
                hide blackscreen
                show 12newalex13
                with dissolve
                p "\" The hell?\""
                a "\" Hey.\""
                p "\" I told you, I was fine.\""
                a "\" Yeah.\""
                a "\" But I don't listen.\""
                hide 12newalex13
                show 12newalex14
                with dissolve
                " She crawls in bed with you."
                p "\" You should listen.\""
                a "\" Be fair.\""
                a "\" I let you order me around, more than I let dad.\""
                p "\" But not in this case.\""
                a "\" No. Not in this case.\""
                a "\" Go to sleep now.\""
                a "\" I'm here.\""
                hide 12newalex14
                show blackscreen
                with dissolve
                " You close your eyes."
                "..."
                "... ..."
                "... ... ..."
                hide blackscreen
                show 12newalex15
                with dissolve
                " When you wake up, Alex is gone."
                hide 12newalex15
                show 12newalex16
                with dissolve
                " But she seems to have left some clothes for you."
                p "\" Damn it, girl.\""
                hide 12newalex16
                show 12newalex17
                with dissolve
                " But you do put them on, and head out."
                hide 12newalex17
                show 12newalex18
                with dissolve
                " In the kitchen, you find no one."
                p "\" Is no one up yet?\""
                p "\" Guess Alex must've gone back to her bedroom.\""
                hide 12newalex18
                show 12newalex19
                with dissolve
                " And sure enough, that's where you find her."
                a "\" *Snore*\""
                p "\" Alex.\""
                p "\" Time to get up.\""
                a "\" *Snore*\""
                p "\" Alex!\""
                hide 12newalex19
                show 12newalex20
                with dissolve
                " She lazily opens one eye."
                a "\" What?\""
                p "\" Time to get up.\""
                a "\" Why?\""
                a "\" Not going to school today. Leaving tomorrow.\""
                p "\" Don't you need to find out your results.\""
                a "\" Yeah.\""
                p "\" So, get up.\""
                hide 12newalex20
                show 12newalex21
                with dissolve
                " She turns her back."
                a "\" I will.\""
                p "\" When?\""
                a "\" Soon.\""
                p "\" Don't we need to go shopping too?\""
                p "\" Alex.\""
                a "\" Yeah.\""
                p "\" Time to get up.\""
                a "\" Don't want to.\""
                p "\" Don't care.\""
                hide 12newalex21
                show 12newalex22
                with dissolve
                a "\" God, you're incessant.\""
                a "\" Leave me be.\""
                p "\" No.\""
                a "\" *Sigh*\""
                hide 12newalex22
                show 12newalex23
                with dissolve
                " You lift her nightshirt."
                a "\" Huh?\""
                a "\" Touching my pussy will just make me sleep deeper.\""
                p "\" Not what I had in mind.\""
                hide 12newalex23
                show 12newalex24
                with dissolve
                " *SMACK!!*"
                hide 12newalex24
                show 12newalex25
                with dissolve
                a "\" AIIIII!!\""
                hide 12newalex25
                show 12newalex26
                with dissolve
                " She jumps up."
                a "\" The hell?\""
                a "\" You don't leave me alone, I'm breaking up with you.\""
                p "\" Ok.\""
                a "\" Ok, what?\""
                p "\" Ok, break up with me.\""
                hide 12newalex26
                show 12newalex27
                with dissolve
                " She lies back down and takes a big yawn."
                a "\" *Yawwnnnn*\""
                a "\" Fine then. We're broken up.\""
                p "\" Ok.\""
                p "\" Now, get up.\""
                a "\" Sigh.\""
                hide 12newalex27
                show 12newalex28
                with dissolve
                " The girls slowly get up, and head to the bathroom."
                i "\" Shit.\""
                i "\" I was sleeping so well.\""
                i "\" But I guess we do have to get up like your boyfriend says.\""
                a "\" Mine? He's not mine.\""
                a "\" I'm done with him.\""
                a "\" You can have him if you want.\""
                p "\" I'll wait for you downstairs.\""
                hide 12newalex28
                show 12newalex29
                with dissolve
                " After a while the girls come downstairs."
                p "\" Why are you so tired.\""
                p "\" I understood yesterday. But why today?\""
                a "\" Fatigue accumulates.\""
                a "\" Where's dad?\""
                p "\" Haven't seen him.\""
                a "\" We should go check.\""
                hide 12newalex29
                show 12newalex30
                a "\" But first.\" She says, tapping her cheek."
                p "\" What?\""
                a "\" Kiss on the cheek?\""
                p "\" I thought we were broken up.\""
                a "\" We are.\""
                a "\" But do this and I might take you back.\""
                hide 12newalex30
                show 12newalex31
                with dissolve
                " You give her a kiss on the cheek."
                a "\" He he...\""
                p "\" Better?\""
                a "\" Nice.\""
                a "\" But not nice enough to take you back.\""
                hide 12newalex31
                show 12newalex32
                with dissolve
                p "\" How about this?\" you ask grabbing her ass."
                a "\" Aright, alright...\""
                a "\" You've won me over.\""
                hide 12newalex32
                show 12newalex33
                with dissolve
                a "\" We're back together again.\""
                p "\" Who said that I'm taking you back?\""
                a "\" So we're still broken up?\""
                p "\" Til you get me something.\""
                a "\" What?\""
                p "\" I don't know.\""
                a "\" Something pretty?\""
                p "\" He he... Ok.\""
                a "\" I will.\""
                a "\" Now, let's go check on dad.\""
                hide 12newalex33
                show 12newalex34
                with dissolve
                b "\" *SNOREEEEE*\""
                p "\" Uh.\""
                p "\" He's louder than you.\""
                a "\" Me?\""
                a "\" I don't snore.\""
                p "\" Hmmm...\""
                p "\" Sometimes you do.\""
                a "\" No, I don't.\""
                hide 12newalex34
                show 12newalex35
                with dissolve
                " She climbs on the bed."
                a "\" Dad!\""
                b "\" *SNOREEE*\""
                a "\" DAD!!!\""
                b "\" Wha?!...\""
                b "\" *Cough* *Cough* *Cough*\""
                hide 12newalex35
                show 12newalex36
                with dissolve
                " Still coughing, he sits up."
                b "\" *Cough* *Cough* *Cough*\""
                a "\" Dad?\""
                a "\" You ok?\""
                " She pats him on the back."
                b "\" *Cough* *Cough* *Cough*\""
                b "\" Yes.\""
                hide 12newalex36
                show 12newalex37
                with dissolve
                b "\" *Cough* *Cough* *Cough*\""
                a "\" Dad?!\""
                b "\" I'm fine.\""
                b "\" Cough, cough, cough!\""
                b "\" Just letting the phlegm settle.\""
                hide 12newalex37
                show 12newalex39
                with dissolve
                " He eventually stands up."
                b "\" Yeah.\""
                b "\" What is it?\""
                p "\" I'm taking the girls to see their results.\""
                p "\" And then do some shopping.\""
                b "\" Right.\""
                b "\" Leaving tomorrow.\""
                p "\" I just wanted to know if you needed me to do anything.\""
                b "\" Not today.\""
                b "\" It can all wait.\""
                hide 12newalex39
                show 12newalex38
                with dissolve
                " A smile spreads across his face."
                b "\" As for me.\""
                b "\" I think I'll just sleep in.\""
                p "\" Alright.\""
                hide 12newalex38
                show 12newalex40
                with dissolve
                " The girls finally get dressed, and you're ready to head out."
                hide 12newalex40
                show back
                with dissolve
                show 12newalex41
                with dissolve
                a "\" You got a lot to do?\""
                a "\" How's your schedule.\""
                p "\" I'll give Naryssa a call. See if I need to drop by.\""
                p "\" But other than that, I'm good.\""
                hide 12newalex41
                show 12newalex42
                with dissolve
                p "\" Drop you off at the school first?\""
                a "\" Yeah.\""
                a "\" But can you wait for us?\""
                a "\" We won't take long.\""
                p "\" Sure.\""
                hide 12newalex42
                show 12newalex43
                with dissolve
                " You drop off the girls, and wait for them to come back."
                hide 12newalex43
                show 12newalex238
                with dissolve
                " *Ring* *Ring*"
                nar "\" Hello?\""
                p "\" Hi. It's me.\""
                p "\" Just wanted to know how everything was.\""
                nar "\" How EVERYTHING is?\""
                p "\" Yeah. What's happening today.\""
                nar "\" Well, the sun is shining, every tree has grown a little taller...\""
                p "\" Narysa!\""
                nar "\" He he...\""
                nar "\" Everything is fine, chief.\""
                nar "\" Stop worrying.\""
                p "\" Well, I'm leaving tomorrow for small vacation a couple of days.\""
                nar "\" Have fun. Everything is good.\""
                p "\" Alright, then. Call me if anything happens.\""
                nar "\" Will do.\""
                nar "\" Have fun.\""
                p "\" Alright.\""
                hide 12newalex238
                show 12newalex44
                with dissolve
                " The girls come back, and Alex gets in next to you slamming the door."
                p "\" Problem?\""
                a "\" Humph.\""
                p "\" Didn't pass?\""
                a "\" Humph!!\""
                hide 12newalex44
                show 12newalex46
                with dissolve
                i "\" She got a 92, and I got a 94.\""
                i "\" She's just harumphing for attention.\""
                hide 12newalex46
                show 12newalex47
                with dissolve
                a "\" You just sit back there, missy.\""
                a "\" In the smarty pants part of the car.\""
                a "\" We'll just sit up here, in the dumb dumb part.\""
                p "\" Dumb dumb?\""
                hide 12newalex47
                show 12newalex45
                with dissolve
                p "\" Speak for yourself, dummy.\""
                p "\" I'm a genius. Just misunderstood.\""
                a "\" Watch it!\""
                p "\" Breaking up with me again?\""
                a "\" Thinking about it.\""
                hide 12newalex45
                show 12newalex46
                with dissolve
                i "\" Are we going shopping, or no?\""
                hide 12newalex46
                show 12newalex76
                with dissolve
                a "\" Yeah.\""
                a "\" Pupster? You need to be somewhere now?\""
                p "\" Apparently not.\""
                a "\" Let's go then.\""
                hide 12newalex76
                show 12newalex48
                with dissolve
                " You drive to a clothing store."
                hide 12newalex48
                show 12newalex49
                with dissolve
                p "\" I can wait for you outside.\""
                a "\" Why?\""
                p "\" 'Cause this is boring.\""
                a "\" We have to get things for you too.\""
                a "\" Besides, you have to do stuff with me.\""
                p "\" Why?\""
                a "\" Because... Well because, ok?!\""
                a "\" We gotta do things together.\""
                hide 12newalex49
                show 12newalex50
                with dissolve
                " The girls start looking around, while you stand there bored."
                hide 12newalex50
                show 12newalex51
                with dissolve
                " After half an hour or so, Alex comes over."
                a "\" Think I got it.\""
                a "\" Let's see what you guys think.\""
                hide 12newalex51
                show 12newalex52
                with dissolve
                " She goes to the changing room and comes out in a bikini."
                a "\" So?\""
                a "\" What do you think?\""
                p "\" Me?\""
                a "\" Yeah.\""
                p "\" Could be skimpier.\""
                a "\" Fuck off.\""
                p "\" He he...\""
                a "\" I like it.\""
                a "\" I'm taking this.\""
                hide 12newalex52
                show 12newalex53
                with dissolve
                " Next she comes out in a dress."
                a "\" This?\""
                p "\" Well...\""
                a "\" Not you this time.\" She cuts you off."
                hide 12newalex53
                show 12newalex54
                with dissolve
                i "\" Evening wear?\""
                a "\" Yeah.\""
                i "\" Like it.\""
                hide 12newalex54
                show 12newalex55
                with dissolve
                " She goes back in and changes again."
                i "\" This?\""
                i "\" What is this?\""
                a "\" For everyday.\""
                a "\" Comfortable. Sweater, in case it rains. Backpack to carry some water.\""
                p "\" Like it.\""
                hide 12newalex55
                show 12newalex57
                with dissolve
                " Then, it was Izzy's turn."
                i "\" Something more classic for a bathing suit, I'm thinking.\""
                a "\" Like it.\""
                hide 12newalex57
                show 12newalex59
                with dissolve
                i "\" And this, for when we go out.\""
                hide 12newalex59
                show 12newalex58
                with dissolve
                a "\" You won't be able to wear a bra with that.\""
                a "\" Maybe no underwear, either.\""
                hide 12newalex58
                show 12newalex59
                with dissolve
                i "\" And?\""
                i "\" Is that a problem?\""
                a "\" Not for me.\""
                hide 12newalex59
                show 12newalex60
                with dissolve
                i "\" And this for every day.\""
                i "\" No backpack, though.\""
                a "\" You can put your stuff in mine.\""
                a "\" And we could get one for puppy too.\""
                hide 12newalex60
                show 12newalex61
                with dissolve
                a "\" Speaking of which.\""
                a "\" I chose something for you too.\""
                p "\" Clothes?\""
                p "\" I don't really like to play dressup.\""
                a "\" Come on. How will I see if it fits you well, if you don't try it?\""
                p "\" I'm sure it'll be fine.\""
                a "\" Please!\""
                p "\" Fine.\""
                hide 12newalex61
                show 12newalex62
                with dissolve
                " You try on the clothes she chose for you."
                p "\" I can't believe I'm saying this, but I kinda like it.\""
                p "\" Comfortable too.\""
                hide 12newalex62
                show 12newalex63
                with dissolve
                a "\" See?\""
                a "\" Momma has taste.\""
                p "\" I probably should get a bathing suit too.\""
                a "\" Got one for you.\""
                p "\" Where?\""
                a "\" Don't worry about it.\""
                a "\" Got you covered.\""
                p "\" Alex!?\""
                a "\" I said, don't worry.\""
                a "\" You'll like it.\""
                hide 12newalex63
                show 12newalex64
                with dissolve
                " Alex pays for everyone and you're ready to head out."
                hide 12newalex64
                show 12newalex65
                with dissolve
                p "\" How much do I owe you?\""
                a "\" For what? For this?\""
                p "\" Yes.\""
                a "\" Don't be silly.\""
                a "\" Like to spoil you sometimes.\""
                p "\" So, you're my sugar momma?\""
                a "\" Yeah.\""
                hide 12newalex65
                show 12newalex66
                with dissolve
                " Back in the car Izzy says."
                i "\" Can you drop me off at my place?\""
                i "\" Need to pack.\""
                a "\" Sure.\""
                hide 12newalex66
                show 12newalex47
                with dissolve
                a "\" Pick you up later.\""
                i "\" Ok.\""
                hide 12newalex47
                show 12newalex76
                with dissolve
                " You drop off Izzy, and Alex says."
                a "\" I wanna go see Yuri too.\""
                a "\" Won't be seeing him for a couple of days.\""
                p "\" Yeah.\""
                p "\" We probably should.\""
                hide 12newalex76
                show 11newalex113
                with dissolve
                " You go to see Yuri before going to your place."
                hide 11newalex113
                show 12newalex67
                with dissolve
                a "\" How long do you intend on keeping this place?\""
                p "\" I don't know.\""
                a "\" You're practically living with us now.\""
                p "\" Yeah.\""
                p "\" I still want my own space, though.\""
                a "\" *Sigh*\""
                a "\" Fine, I guess.\""
                hide 12newalex67
                show 12newalex68
                with dissolve
                " She insists on packing your bag for you."
                hide 12newalex68
                show 12newalex69
                with dissolve
                a "\" What's this?\""
                p "\" What?\""
                a "\" This empty picture frame.\""
                p "\" Came with the apartment.\""
                hide 12newalex69
                show 12newalex70
                with dissolve
                a "\" Why is it still empty?\""
                p "\" Don't have anything to put in there.\""
                a "\" Mom? Dad?\""
                p "\" Don't really have anyone.\""
                hide 12newalex70
                show 12newalex71
                with dissolve
                a "\" Aww...\""
                p "\" Well, I have you I guess.\""
                p "\" But not...\""
                hide 12newalex71
                show 12newalex72
                with dissolve
                " Before you finish, she grabs you and squeezes you tight."
                a "\" I'll give you a picture.\""
                a "\" And you can take it with you when you move in.\""
                p "\" When? No if?\""
                a "\" When!\""
                p "\" Hmmm...\""
                p "\" Can I have a nude picture?\""
                a "\" Don't ruin this, you animal.\""
                p "\" He he...\""
                hide 12newalex72
                show 12newalex73
                with dissolve
                a "\" Love you pupster.\""
                a "\" And you'll always have me, ok.\""
                p "\" Till we break up again, at least.\""
                hide 12newalex73
                show 12newalex74
                with dissolve
                " She gives you a kiss on the cheek."
                a "\" Well, don't wake me up when I don't want you.\""
                a "\" He he...\""
                hide 12newalex74
                show 12newalex75
                with dissolve
                " After you're finished, you go pick up Izzy."
                a "\" Got everything?\""
                i "\" Yeah.\""
                a "\" How's Agatha?\""
                i "\" Good. Better anyway.\""
                i "\" She'll be fine til I come back.\""
                hide 12newalex75
                show 12newalex77
                with dissolve
                " You take the girls back to the villa."
                hide 12newalex77
                show 12newalex79
                with dissolve
                a "\" Hmm...\""
                a "\" Where is Dad?\""
                p "\" Around, I guess.\""
                a "\" Maybe he's not feeling well.\""
                a "\" Saw how he coughed this morning?\""
                p "\" Yeah.\""
                hide 12newalex79
                show 12newalex80
                with dissolve
                " Going to Boris's bedroom, you find him watching TV and surrounded by buckets of fried chicken."
                hide 12newalex80
                show 12newalex81
                with dissolve
                a "\" The hell?\""
                a "\" You didn't get out of bed?\""
                hide 12newalex81
                show 12newalex80
                with dissolve
                b "\" *Burp*\""
                b "\" No.\""
                hide 12newalex80
                show 12newalex81
                with dissolve
                a "\" Here I am worried about you and your cough, and I find you still in bed pigging out.\""
                b "\" *Burp*\""
                b "\" Yeah.\""
                hide 12newalex81
                show 12newalex82
                with dissolve
                b "\" I'll be taking it more easy from now on, baby.\""
                b "\" Got dressed the other day like I went out.\""
                b "\" But your boy pointed out that I shouldn't be getting dressed up, if I wasn't planning on going out.\""
                a "\" Don't blame this on him.\""
                hide 12newalex82
                show 12newalex83
                with dissolve
                a "\" Stinks in here.\""
                a "\" At least open a window.\""
                b "\" Nope.\""
                a "\" Ugh...\""
                a "\" Let's get out of here.\""
                hide 12newalex83
                show 12newalex84
                with dissolve
                " Later on, you Alex and Izzy are in the living room, watching TV."
                a "\" You should've seen it.\""
                a "\" Smelled awful.\""
                a "\" That fried smell, you know.\""
                i "\" I'm sure I've seen worse with mom.\""
                a "\" Yeah, maybe.\""
                a "\" But she has an excuse.\""
                hide 12newalex84
                show 12newalex85
                with dissolve
                i "\" He's just getting old.\""
                i "\" It's not getting better from here.\""
                i "\" It will soon be your turn to take care of him, instead of him taking care of you.\""
                hide 12newalex85
                show 12newalex86
                with dissolve
                a "\" Please.\""
                a "\" Dad isn't rusting, he's good for years.\""
                hide 12newalex86
                show 12newalex87
                with dissolve
                i "\" I'm just saying.\""
                i "\" It's not getting better from here.\""
                i "\" And you'll need to get ready.\""
                i "\" Emotionally, I mean.\""
                hide 12newalex87
                show 12newalex88
                with dissolve
                a "\" Dad will be fine!!!\""
                a "\" And you need to stop talking like this.\""
                hide 12newalex88
                show 12newalex90
                with dissolve
                i "\" See?\""
                i "\" This is what I mean.\""
                i "\" You're not ready at all.\""
                a "\" There's nothing to be ready for.\""
                i "\" Alex.\""
                hide 12newalex90
                show 12newalex88
                with dissolve
                a "\" You're really trying to piss me off?\""
                a "\" No joke, now.\""
                hide 12newalex88
                show 12newalex89
                with dissolve
                p "\" Yup.\""
                p "\" Not uncomfortable at all.\""
                p "\" Yup.\""
                hide 12newalex89
                show 12newalex90
                with dissolve
                i "\" No need for you to get upset.\""
                i "\" I'm just saying...\""
                a "\" Well, stop saying.\""
                i "\" *Sigh*\""
                i "\" I'm going to bed.\""
                i "\" Good night.\""
                hide 12newalex90
                show 12newalex91
                with dissolve
                " Izzy leaves, and you're alone with Alex."
                a "\" Jesus, that girl.\""
                a "\" Dad is going to be fine, right?\""
                p "\" Well, eventually...\""
                a "\" Right?!\""
                p "\" Right... Right.\""
                hide 12newalex91
                show 12newalex92
                with dissolve
                " She gives you a kiss."
                a "\" We'd better get to sleep too.\""
                a "\" We have to wake up early to catch out plane.\""
                a "\" See you later tonight.\""
                p "\" I appreciate you tryin to look after me, but I'm fine.\""
                p "\" I didn't have anymore nightmares.\""
                p "\" Besides, you need your sleep too. Else I'll have to slap your ass again in the morning.\""
                a "\" Don't threaten me with a good time.\""
                p "\" He he...\""
                p "\" Seriously, though.\""
                a "\" Ok.\""
                hide 12newalex92
                show 12newalex235
                with dissolve
                " You head upstairs to get some sleep too."
                hide 12newalex235
                show blackscreen
                with dissolve
                " You close your eyes."
                "..."
                "... ..."
                "... ... ..."
                hide blackscreen
                show 12newalex233
                with dissolve
                " And when you open them again, the desert stretches out in front of you."
                p "\" Damn it.\""
                t "\" Cherubael.\""
                p "\" That's my name.\""
                hide 12newalex233
                show 12newalex234
                with dissolve
                " You see something grabbing your arm."
                t "\" COME BACK HOME!\""
                hide 12newalex234
                show 12newalex236
                with dissolve
                p "\" AHHHH!!!\""
                " You violently stir yourself awake."
                p "\" Damn it!\""
                show 12newalex237
                with dissolve
                p "\" Shit.\""
                p "\" Nightmares again.\""
                p "\" Teaches me for not letting Alex sleep with me.\""
                p "\" Ok...\""
                p "\" It's just a dream.\""
                p "\" Close your eyes.\""
                p "\" Go back to sleep.\""
                p "\" Close your eyes.\""
                hide 12newalex237
                show blackscreen
                with dissolve
                " It took you a while, but you eventually managed to get back to sleep."
                "..."
                "... ..."
                "... ... ..."
                hide blackscreen
                show 12newalex15
                with dissolve
                " When you wake up, you wake up tired."
                p "\" Fucking nightmares.\""
                hide 12newalex15
                show 12newalex93
                with dissolve
                " You put on the clothes Alex got for you, and head to her room."
                hide 12newalex93
                show 12newalex94
                with dissolve
                " You find that the girls are already up and dressed."
                p "\" Oh.\""
                p "\" You're up.\""
                hide 12newalex94
                show 12newalex95
                with dissolve
                a "\" Disappointed?\""
                p "\" Well. A bit.\""
                a "\" He he...\""
                a "\" Ready?\""
                p "\" Yes.\""
                hide 12newalex95
                show 12newalex96
                with dissolve
                i "\" Help me with my luggage too?\""
                p "\" Of course.\""
                hide 12newalex96
                show 12newalex97
                with dissolve
                " Boris says his goodbyes as you leave."
                b "\" You have everything?\""
                a "\" Yeah.\""
                b "\" Money?\""
                a "\" We have money, dad.\""
                b "\" Ok.\""
                hide 12newalex97
                show 12newalex98
                with dissolve
                b "\" Look after yourself, ok?\""
                a "\" What?\""
                a "\" I'm grown girl.\""
                b "\" And take a shower.\""
                b "\" You still smell of fried chicken.\""
                hide 12newalex98
                show 12newalex99
                with dissolve
                b "\" Look after them.\""
                p "\" Of course.\""
                b "\" I told you to bring one of your boys with you.\""
                p "\" I'm not chopped liver.\""
                b "\" If you say so.\""
                b "\" And behave yourself.\""
                p "\" Always.\""
                hide 12newalex99
                show 12newalex100
                with dissolve
                " On the plane, Alex seems worried."
                p "\" Everything ok.\""
                a "\" I guess.\""
                p "\" You guess?\""
                a "\" Izzy.\""
                hide 12newalex100
                show 12newalex101
                with dissolve
                " You look over where Izzy is sitting, while some guy is trying to talk to her."
                m9 "\" So, you're a student?\""
                i "\" Yeah.\""
                p "\" That guy?\" You ask."
                p "\" Seems harmless.\""
                hide 12newalex101
                show 12newalex102
                with dissolve
                a "\" It's not that.\""
                a "\" She just doesn't do well with planes.\""
                p "\" Isn't there a pill for that?\""
                a "\" Doesn't help her.\""
                hide 12newalex102
                show 12newalex103
                with dissolve
                a "\" Look at her.\""
                a "\" Poor thing.\""
                hide 12newalex103
                show 12newalex104
                with dissolve
                a "\" Can I ask you for a favor?\""
                p "\" What?\""
                p "\" Need me to talk to that guy?\""
                hide 12newalex104
                show 12newalex102
                with dissolve
                a "\" Mind if I don't sit next to you on the flight?\""
                a "\" I mean. Do you mind if she and I change places.\""
                p "\" Would that help?\""
                a "\" Sitting next to someone she knows? I think so.\""
                p "\" She and I could switch places.\""
                a "\" No.\""
                a "\" You two need more time alone than her and I do.\""
                a "\" It will bring you closer.\""
                a "\" I'm going over there.\""
                hide 12newalex102
                show 12newalex105
                with dissolve
                a "\" Hey.\""
                i "\" Hey.\""
                a "\" You ok?\""
                i "\" You know. Just a bit sick.\""
                a "\" Switch places with me.\""
                i "\" It's fine.\""
                a "\" I don't like you arguing.\""
                a "\" Just switch places, ok.\""
                i "\" Fine.\""
                hide 12newalex105
                show 12newalex106
                with dissolve
                " Alex takes Izzy's place."
                m8 "\" Your friend ok?\""
                a "\" Ya ne govoryu po angliyski.\""
                m8 "\" What?\""
                a "\" Ich spreche kein Englisch.\""
                m8 "\" Excuse me?\""
                a "\" How many languages do you need me to tell you that I don't speak English.\""
                m8 "\" But you're...\""
                a "\" Je ne parle pas anglais.\""
                m8 "\" Sigh...\""
                hide 12newalex106
                show 12newalex107
                with dissolve
                " Izzy comes next to you."
                i "\" Sorry.\""
                p "\" What about?\""
                i "\" That you don't get to sit with Alex.\""
                if izzyin == True:
                    p "\" Don't be silly.\""
                    p "\" How are you?\""
                    hide 12newalex107
                    show 12newalex108
                    with dissolve
                    i "\" Me and flying, we don't really get along.\""
                    p "\" Why?\""
                    i "\" I don't know.\""
                    i "\" I just feel sick.\""
                    p "\" How sick.\""
                    hide 12newalex108
                    show 12newalex109
                    with dissolve
                    " She makes a face."
                    i "\" This sick.\""
                    p "\" He he...\""
                    p "\" Ok.\""
                    hide 12newalex109
                    show 12newalex108
                    with dissolve
                    i "\" Mind if I hold your hand?\""
                    p "\" Go ahead.\""
                    hide 12newalex108
                    show 12newalex110
                    with dissolve
                    " You offer her your hand, and she squeezes it all the way over."
                    " You're not sure if it helped, but she didn't throw up."
                    jump ep12cont3

                else:
                    p "\" Don't be silly.\""
                    p "\" I'm not a child.\""
                    p "\" You ok?\""
                    i "\" Yeah.\""
                    i "\" I will be.\""
                    hide 12newalex107
                    show 12newalex111
                    with dissolve
                    " But you could see her being uncomfortable and sick all the way over."
                    jump ep12cont3

label ep12cont3:
                scene 12newalex112
                with dissolve
                " You get there, and to the hotel."
                i "\" Pretty big.\""
                a "\" Yeah.\""
                i "\" I was thinking something more coquettish.\""
                a "\" You can't get coquettish on the beach.\""
                a "\" Only the big ones.\""
                show 12newalex113
                with dissolve
                a "\" You like it?\""
                p "\" I guess.\""
                p "\" I don't really care.\""
                p "\" I'm not here for the hotel.\""
                a "\" Let's go check our room out.\""
                hide 12newalex113
                show 12newalex115
                with dissolve
                p "\" Big.\""
                a "\" It has to be.\""
                a "\" Booked for three people.\""
                a "\" Told them you were sleeping on the couch.\""
                p "\" Ouch.\""
                hide 12newalex115
                show 12newalex116
                with dissolve
                a "\" Big bed, though.\""
                a "\" Room for all of us.\""
                p "\" We can make it work.\""
                hide 12newalex116
                show 12newalex117
                with dissolve
                a "\" Is that so?\""
                p "\" I'm adaptable.\""
                a "\" You're huge, though.\""
                p "\" Thank you.\""
                a "\" I meant your whole body.\""
                p "\" I know what you meant.\""
                p "\" It's ok. You can admit it.\""
                a "\" Ass!\""
                hide 12newalex117
                show 12newalex118
                with dissolve
                i "\" Big bathroom too.\""
                hide 12newalex118
                show 12newalex119
                with dissolve
                " Alex throws herself on the bed."
                a "\" Ahh...\""
                a "\" We should check the air conditioning.\""
                a "\" Likely to melt without it.\""
                p "\" We should leave it on even when we're not here.\""
                p "\" Come back to a cool place.\""
                a "\" Can't do that.\""
                a "\" Air conditioning doesn't work, unless the key is in the little holder.\""
                p "\" What?\""
                a "\" Turns off the power to the entire room.\""
                a "\" Trying to save money.\""
                p "\" Can't even charge a phone unless you're here with the key?\""
                a "\" Nope.\""
                p "\" Asshats.\""
                hide 12newalex119
                show 12newalex120
                with dissolve
                a "\" So, how are you feeling?\""
                i "\" Good.\""
                a "\" Not sick anymore?\""
                i "\" The plane thing?\""
                i "\" Passes quickly.\""
                a "\" Beach?\""
                i "\" Sure.\""
                if izzyin == True:
                    hide 12newalex120
                    show 12newalex121
                    with dissolve
                    a "\" You?\""
                    a "\" Too tired for the beach?\""
                    p "\" No.\""
                    p "\" That's what we're here for, right?\""
                    a "\" Let's go then.\""
                    jump ep12cont4

                else:
                    hide 12newalex120
                    show 12newalex122
                    with dissolve
                    a "\" You?\""
                    a "\" Too tired for the beach?\""
                    p "\" No.\""
                    p "\" That's what we're here for, right?\""
                    a "\" Let's go then.\""
                    jump ep12cont4

label ep12cont4:
                scene 12newalex123
                with dissolve
                " You head out to the beach."
                a "\" Ahh...\""
                p "\" Yes?\""
                a "\" Love the ocean.\""
                show 12newalex124
                with dissolve
                p "\" It's a big bowl of water.\""
                p "\" I mean, I get it.\""
                p "\" Don't really see the romanticism in it, though.\""
                hide 12newalex124
                show 12newalex125
                with dissolve
                a "\" A big bowl of water, eh?\""
                p "\" Well, yes.\""
                a "\" And you're just a cluster of atoms.\""
                p "\" Equally correct.\""
                a "\" For someone who talks about his dreams, you sure can be a cynic sometimes.\""
                p "\" What do you mean cynic?\""
                p "\" What am I doubting about it.\""
                hide 12newalex125
                show 12newalex126
                with dissolve
                i "\" I get what she's saying.\""
                i "\" Maybe you guys will get a house on the ocean some day.\""
                a "\" You mean we.\""
                a "\" All three of us.\""
                a "\" Maybe.\""
                hide 12newalex126
                show 12newalex127
                with dissolve
                a "\" Wanna change?\""
                a "\" Seen anywhere we could do that?\""
                i "\" Yeah.\""
                i "\" Over there. It's like a booth.\""
                hide 12newalex127
                show 12newalex128
                with dissolve
                p "\" There's some people over there.\""
                p "\" Probably some kind of booth around.\""
                hide 12newalex128
                show 12newalex129
                with dissolve
                a "\" Ahh...\""
                a "\" I'd rather we just be by ourselves.\""
                i "\" Agreed.\""
                hide 12newalex129
                show 12newalex130
                with dissolve
                " You head to the place that Izzy mentioned."
                a "\" Wait for us?\""
                p "\" Sure.\""
                a "\" We won't be long.\""
                hide 12newalex130
                show 12newalex131
                with dissolve
                " They come out a few minutes later."
                a "\" Done.\""
                a "\" Your turn.\""
                i "\" Alex left you the bathing suit inside.\""
                i "\" He he...\""
                p "\" What?\""
                i "\" Nothing.\""
                a "\" Come on.\""
                a "\" Hurry up.\""
                hide 12newalex131
                show 12newalex132
                with dissolve
                " You go inside and change."
                " But coming out you feel it's about two sizes too small."
                p "\" This...\""
                p "\" This is not good.\""
                hide 12newalex132
                show 12newalex133
                with dissolve
                i "\" Why?\""
                p "\" I don't really feel comfortable.\""
                a "\" It's just us here.\""
                a "\" Don't worry. We'll protect your innocence if some big burly man comes by to try to take it.\""
                i "\" He he...\""
                p "\" Wearing this, it might come to that.\""
                i "\" He he he...\""
                a "\" You like looking at me in skimpy clothes, right?\""
                a "\" So?\""
                a "\" It's just us here pupster.\""
                p "\" *Sigh*\""
                p "\" Fine.\""
                hide 12newalex133
                show 12newalex134
                with dissolve
                " You head back out and spread a blanket."
                hide 12newalex134
                show 12newalex135
                with dissolve
                a "\" Thinking about work?\""
                p "\" No.\""
                a "\" Dad?\""
                p "\" No.\""
                a "\" What are you thinking about then?\""
                p "\" Nothing really.\""
                a "\" Good.\""
                a "\" We're here to forget about all of that.\""
                hide 12newalex135
                show 12newalex136
                with dissolve
                i "\" All of that?\""
                i "\" Like how I got two points more than you in that exam?\""
                a "\" Watch it.\""
                i "\" He he...\""
                hide 12newalex136
                show 12newalex137
                with dissolve
                a "\" Ahh...\""
                a "\" Going for a swim.\""
                hide 12newalex137
                show 12newalex138
                with dissolve
                i "\" She seems happy.\""
                p "\" I hope so.\""
                if izzyin == True:
                    hide 12newalex138
                    show 12newalex139
                    with dissolve
                    i "\" Help me out with something?\""
                    p "\" What?\""
                    i "\" Sunscreen?\""
                    p "\" Sure.\""
                    hide 12newalex139
                    show 12newalex140
                    with dissolve
                    " She gets on her stomach."
                    p "\" Sunscreen?\""
                    i "\" Alex's bag.\""
                    hide 12newalex140
                    show 12newalex141
                    with dissolve
                    p "\" You know...\""
                    p "\" This bathing suit may have a classic style, but...\""
                    i "\" Still missing fabric in certain places?\""
                    p "\" Yeah.\""
                    i "\" I can feel the breeze.\""
                    p "\" He he...\""
                    i "\" It's fine.\""
                    i "\" It's just us here.\""
                    hide 12newalex141
                    show 12newalex142
                    with dissolve
                    " You take the sunscreen and start rubbing it on her."
                    p "\" So, how's school?\""
                    i "\" Pretty good.\""
                    p "\" So, that 94 is out of...\""
                    i "\" 100.\""
                    p "\" Ahh...\""
                    p "\" That's good then.\""
                    p "\" I never went to university.\""
                    hide 12newalex142
                    show 12newalex143
                    with dissolve
                    i "\" Would you like to?\""
                    p "\" Never been a good student.\""
                    i "\" Maybe you never had had a good teacher.\""
                    p "\" I don't think so.\""
                    hide 12newalex143
                    show 12newalex144
                    with dissolve
                    " Your hands reach her top."
                    i "\" Take it off.\""
                    p "\" You sure?\""
                    i "\" It's just us here.\""
                    hide 12newalex144
                    show 12newalex145
                    with dissolve
                    " You take off her top and continue to apply the cream."
                    i "\" It's not half as difficult as you might think.\""
                    p "\" Learning not a strong suit.\""
                    p "\" Alex was kidding about the dumb dumb part of the car.\""
                    p "\" But she was only half wrong.\""
                    hide 12newalex145
                    show 12newalex146
                    with dissolve
                    i "\" I don't think so.\""
                    p "\" All I've ever been good at really, was smashing stuff.\""
                    p "\" But I'm REALLY good at that,\""
                    i "\" He he...\""
                    hide 12newalex146
                    show 12newalex147
                    with dissolve
                    i "\" I don't think you can survive the way you do by just smashing stuff.\""
                    p "\" You'd be surprised.\""
                    i "\" I think you never really gave it a chance.\""
                    p "\" No point.\""
                    hide 12newalex147
                    show 12newalex148
                    with dissolve
                    i "\" I can't force you.\""
                    i "\" But if you change your mind, I can help you.\""
                    i "\" And I don't think you're half as dumb as you pretend to be.\""
                    p "\" It's not an act.\""
                    i "\" Yes it is.\""
                    i "\" I can tell.\""
                    hide 12newalex148
                    show 12newalex149
                    with dissolve
                    " You finish up, and she puts her top back on."
                    i "\" Just think about it, ok?\""
                    p "\" Ok.\""
                    jump ep12cont5

                else:
                    jump ep12cont5

label ep12cont5:
                scene 12newalex150
                with dissolve
                a "\" Hey!\""
                a "\" Are you coming in or no?\""
                show 12newalex149
                with dissolve
                i "\" Go ahead.\""
                i "\" I'll watch our stuff.\""
                p "\" Ok.\""
                hide 12newalex149
                show 12newalex151
                with dissolve
                " You follow Alex into the sea."
                a "\" Izzy?\""
                p "\" Says she'll watch over our stuff.\""
                a "\" Good idea actually.\""
                a "\" Can't lose that key.\""
                hide 12newalex151
                show 12newalex152
                with dissolve
                " She swims away."
                a "\" Catch me.\""
                p "\" Alright.\""
                hide 12newalex152
                show 12newalex153
                with dissolve
                " You take a few strokes, and you don't see her anymore."
                p "\" The hell?\""
                " And you can feel something tugging on one of your toes."
                hide 12newalex153
                show 12newalex154
                with dissolve
                " Diving you find her."
                hide 12newalex154
                show 12newalex155
                with dissolve
                " Smiling she comes into your arms."
                hide 12newalex155
                show 12newalex156
                with dissolve
                " She moves her mouth as if trying to say something."
                hide 12newalex156
                show 12newalex157
                with dissolve
                " But then she just covers yours with a kiss."
                " And holds it til she runs out of air."
                hide 12newalex157
                show 12newalex158
                with dissolve
                " When she does, she lets go and goes back up to the surface."
                hide 12newalex158
                show 12newalex150
                with dissolve
                " You follow her up."
                a "\" He he...\""
                p "\" What were you trying to say?\""
                a "\" What?\""
                p "\" Down there. What were you trying to say.\""
                a "\" I'm not saying it again.\""
                p "\" Say what?\""
                a "\" Guess you'll have to find out.\""
                hide 12newalex150
                show 12newalex152
                with dissolve
                " You swim a bit more before you go back to the beach."
                hide 12newalex152
                show 12newalex159
                with dissolve
                " When you do, you find Izzy nodding off."
                a "\" Watching over our things?\""
                a "\" The way she's nodding off, someone could've stolen her too.\""
                a "\" Sweetie?\""
                hide 12newalex159
                show 12newalex160
                with dissolve
                " She takes her in her arms."
                a "\" Hey there.\""
                i "\" Hey.\""
                i "\" I was just having the strangest dream.\""
                a "\" What was it about?\""
                i "\" It's going to sound weird.\""
                hide 12newalex160
                show 12newalex161
                with dissolve
                i "\" You were in it.\" She says looking at you."
                p "\" Is that so?\""
                i "\" Yeah.\""
                i "\" I was in this like... Desert.\""
                p "\" Desert?\""
                i "\" Yeah. Kinda scary.\""
                i "\" But we held each other by the hand.\""
                p "\" Us?\""
                i "\" Yes.\""
                i "\" The desert was scary, but we knew that we could walk each other out.\""
                i "\" With the certainty of dreams, you know. We just knew.\""
                p "\" What else?\""
                i "\" I don't really remember.\""
                p "\" Nothing.\""
                " She shakes her head."
                hide 12newalex161
                show 12newalex162
                with dissolve
                " Then stands up."
                i "\" I wanna go for a swim.\""
                hide 12newalex162
                show 12newalex163
                with dissolve
                " You immediately follow her out."
                i "\" What?\""
                p "\" Tell me more about your dream.\""
                hide 12newalex163
                show 12newalex165
                with dissolve
                i "\" I don't remember anymore.\""
                p "\" How was the desert?\""
                p "\" Were there creatures in it?\""
                i "\" No. Not that I can remember.\""
                p "\" What color was it?\""
                p "\" Like purple?\""
                hide 12newalex165
                show 12newalex164
                with dissolve
                i "\" Hmmm...\""
                i "\" Maybe.\""
                i "\" Kinda.\""
                hide 12newalex164
                show 12newalex165
                with dissolve
                i "\" Come on.\""
                i "\" Dreams are dreams.\""
                i "\" Let's just go for a swim.\""
                hide 12newalex165
                show 12newalex166
                with dissolve
                " You swim with her."
                " But your mind goes back to the desert in your dreams."
                if izzyin == True:
                    hide 12newalex166
                    show 12newalex167
                    with dissolve
                    " After a while... She says..."
                    i "\" I'm going back in.\""
                    p "\" Yeah.\""
                    p "\" Me too.\""
                    jump ep12cont6

                else:
                    hide 12newalex166
                    show 12newalex165
                    with dissolve
                    " After a while... She says..."
                    i "\" I'm going back in.\""
                    p "\" Yeah.\""
                    p "\" Me too.\""
                    jump ep12cont6

label ep12cont6:
                scene 12newalex168
                with dissolve
                " You spend the rest of the day, just lazing around on the beach."
                show 12newalex169
                with dissolve
                " Then head back to the hotel to change before dinner."
                hide 12newalex169
                show 12newalex170
                with dissolve
                " But in the corner of your eye, you spot someone."
                p "\" Who's that?\""
                a "\" Who?\""
                p "\" That guy.\""
                a "\" The hell should I know?\""
                p "\" I've seen him before.\""
                a "\" So?\""
                p "\" I don't remember where, though.\""
                hide 12newalex170
                show 12newalex171
                with dissolve
                a "\" Seeing monsters in every shadow?\""
                p "\" Remember what we talked about?\""
                a "\" Yes.\""
                a "\" But that doesn't mean that everyone is a suspect.\""
                a "\" Besides. He's wearing sunglasses at night.\""
                a "\" Probably just a drunk douchebag.\""
                p "\" Hmmm...\""
                a "\" Relax.\""
                a "\" We're here to relax, remember.\""
                hide 12newalex171
                show 12newalex172
                with dissolve
                " You go upstairs."
                a "\" Ugh...\""
                a "\" My feet hurt.\""
                p "\" From what?\""
                a "\" Sand in my shoes.\""
                p "\" *Sigh*\""
                hide 12newalex172
                show 12newalex173
                with dissolve
                a "\" Little rub, after we come back?\""
                p "\" And tug?\""
                a "\" I mean for my feet.\""
                p "\" We'll see how you behave.\""
                hide 12newalex173
                show 12newalex174
                with dissolve
                a "\" So, only as a reward.\""
                a "\" I can't just expect it.\""
                p "\" Nope.\""
                a "\" You're not a very nice boyfriend.\""
                a "\" Guess you can just jackoff then.\""
                p "\" I've had lots of practice.\""
                a "\" He he...\""
                a "\" Fuck you.\""
                hide 12newalex174
                show 12newalex175
                with dissolve
                " The girls begin changing their clothes."
                a "\" Commando then?\""
                i "\" You're complaining?\""
                hide 12newalex175
                show 12newalex176
                with dissolve
                a "\" Will be difficult to keep my hands to myself.\""
                a "\" You know.\""
                a "\" Knowing that there's nothing under there. That I can just reach out my hand and...\""
                i "\" You'll just have to try it.\""
                i "\" See if I stop you.\""
                a "\" Little tease.\""
                hide 12newalex176
                show 12newalex177
                with dissolve
                " Alex turns to you."
                a "\" Ok.\""
                a "\" I got you a suit too.\""
                p "\" Nope.\""
                hide 12newalex177
                show 12newalex178
                with dissolve
                a "\" What?\""
                p "\" After the bathing suit?\""
                p "\" I think I'll make my own arrangements.\""
                a "\" Puppy?\""
                p "\" No puppy.\""
                p "\" I got this.\""
                hide 12newalex178
                show 12newalex179
                with dissolve
                " You get a suit from your luggage."
                p "\" Good enough?\""
                hide 12newalex179
                show 12newalex180
                with dissolve
                a "\" I have to say I'm disappointed.\""
                p "\" Really?\""
                a "\" No assless chaps.\""
                a "\" But it will do.\""
                p "\" You're too kind.\""
                hide 12newalex180
                show 12newalex181
                with dissolve
                " You go out and find a restaurant."
                i "\" Looks nice.\""
                a "\" It's ok.\""
                hide 12newalex181
                show 12newalex182
                with dissolve
                a "\" Damn, I'm hungry.\""
                i "\" Me too actually.\""
                a "\" Figures.\""
                a "\" We haven't eaten all day.\""
                hide 12newalex182
                show 12newalex183
                with dissolve
                a "\" You? Hungry?\""
                p "\" I can eat.\""
                a "\" I can eat.\" She says, imitating you."
                a "\" Afraid to use more words? Just in case they run out?\""
                p "\" Fuck off.\""
                hide 12newalex183
                show 12newalex184
                with dissolve
                " Your food is brought to the table."
                i "\" Mmm...\""
                a "\" Looks delicious.\""
                hide 12newalex184
                show 12newalex185
                with dissolve
                " Alex starts devouring her plate."
                hide 12newalex185
                show 12newalex186
                with dissolve
                a "\" What?\""
                p "\" Nothing.\""
                p "\" You're just so enthusiastic about that spaghetti.\""
                a "\" It's here.\""
                a "\" Why not enjoy it.\""
                hide 12newalex186
                show 12newalex187
                with dissolve
                i "\" He's right, though.\""
                i "\" You're almost vaping that plate.\""
                hide 12newalex187
                show 12newalex188
                with dissolve
                a "\" I'm gonna grow fat.\""
                a "\" You know like those people that they have to break the wall down to get them out of their house?\""
                a "\" That's going t be me.\""
                a "\" Pupster will have to go to the gym to be able to carry me.\""
                hide 12newalex188
                show 12newalex186
                with dissolve
                a "\" Don't skip leg day, now.\""
                p "\" He he...\""
                hide 12newalex186
                show 12newalex188
                with dissolve
                a "\" And you, Izzy.\""
                a "\" You'll just keep shoveling food in my mouth.\""
                a "\" That will be your job.\""
                i "\" Hehe...\""
                i "\" Yes, ma'am.\""
                if alexpreg == True:
                    hide 12newalex188
                    show 12newalex190
                    with dissolve
                    " She finishes her plate with a blissful look on her face."
                    a "\" Mmm...\""
                    a "\" Needed that.\""
                    hide 12newalex190
                    show 12newalex189
                    with dissolve
                    a "\" Can I be honest?\""
                    a "\" I could use another plate.\""
                    p "\" Get one.\""
                    p "\" But I'll be getting a trolley.\""
                    p "\" Not carrying you on my back when you get to 300.\""
                    a "\" Ass.\""
                    hide 12newalex189
                    show 12newalex191
                    with dissolve
                    " She does get another plate."
                    hide 12newalex191
                    show 12newalex192
                    with dissolve
                    " And finishes it with the same voracity."
                    a "\" *Burp*\""
                    hide 12newalex192
                    show 12newalex193
                    with dissolve
                    i "\" He he...\""
                    i  "\" Let's go.\""
                    hide 12newalex194
                    show 12newalex195
                    with dissolve
                    a "\" Back to the hotel?\""
                    p "\" Sure.\""
                    a "\" Ugh...\""
                    a "\" I did eat a lot.\""
                    a "\" May have to waddle back.\""
                    jump ep12cont7

                else:
                    hide 12newalex188
                    show 12newalex190
                    with dissolve
                    " She finishes her plate with a blissful look on her face."
                    a "\" Mmm...\""
                    a "\" Needed that.\""
                    hide 12newalex190
                    show 12newalex192
                    with dissolve
                    a "\" *Burp*\""
                    hide 12newalex192
                    show 12newalex193
                    with dissolve
                    i "\" He he...\""
                    i  "\" Let's go.\""
                    hide 12newalex193
                    show 12newalex194
                    with dissolve
                    a "\" Back to the hotel?\""
                    p "\" Sure.\""
                    a "\" Ugh...\""
                    a "\" I did eat a lot.\""
                    a "\" May have to waddle back.\""
                    jump ep12cont7

label ep12cont7:
                scene 12newalex195
                with dissolve
                " You get back to the hotel."
                show 12newalex196
                with dissolve
                " Alex takes her shoes off, and throws herself on the bed."
                a "\" Ugh...\""
                a "\" Belly hurts.\""
                hide 12newalex196
                show 12newalex197
                with dissolve
                a "\" Sorry pupster.\""
                p "\" Why?\""
                a "\" You ain't getting no sexy time tonight.\""
                p "\" Is that so.\""
                hide 12newalex197
                show 12newalex198
                with dissolve
                a "\" Well...\""
                a "\" You can have these two fingers.\""
                a "\" Too bloated to do anything else.\""
                p "\" Two fingers?\""
                a "\" Make lemonade.\""
                hide 12newalex198
                show 12newalex199
                with dissolve
                " You push her legs apart, and step between them."
                a "\" Brute.\""
                p "\" But what if I want more?\""
                hide 12newalex199
                show 12newalex200
                with dissolve
                a "\" Oh...\""
                a "\" He's gonna ravish me now.\""
                p "\" He he...\""
                p "\" Ravish?\""
                a "\" Yeah.\""
                a "\" Izzy! Help!\""
                a "\" This brute is about to mount me.\""
                if izzyin == True:
                    hide 12newalex200
                    show 12newalex201
                    with dissolve
                    i "\" I can see that.\""
                    a "\" So?\""
                    a "\" Are you just going to stand there and watch?\""
                    i "\" Only for the first five minutes.\""
                    i "\" Or until he tags me in.\""
                    a "\" You too?\""
                    hide 12newalex201
                    show 12newalex203
                    with dissolve
                    a "\" BRUTES!\""
                    a "\" Both of you.\""
                    jump ep12cont8

                else:
                    hide 12newalex200
                    show 12newalex202
                    with dissolve
                    i "\" I think I should leave the two of you alone.\""
                    a "\" What?\""
                    i "\" Don't you want your intimacy?\""
                    hide 12newalex202
                    show 12newalex203
                    with dissolve
                    a "\" And that includes you.\""
                    i "\" Does it?\""
                    a "\" Izzy, if you don't even give this a chance, I swear...\""
                    hide 12newalex203
                    show 12newalex202
                    with dissolve
                    i "\" Sorry.\""
                    i "\" Ok.\""
                    jump ep12cont8

label ep12cont8:
                scene 12newalex204
                with dissolve
                " You rip her dress off."
                a "\" Ouch.\""
                a "\" Now you have to buy me a new one.\""
                p "\" If you earn a new one.\""
                show 12newalex205
                with dissolve
                " Then you get on top of her."
                a "\" *Sigh*\""
                a "\" Just my luck.\""
                a "\" Had to have an animal for a boyfriend.\""
                p "\" Animal, am I?\""
                hide 12newalex205
                show 12newalex207
                with dissolve
                " You rub your erect dick against her pussy."
                hide 12newalex207
                show 12newalex206
                with dissolve
                a "\" Ahmm...\""
                p "\" Yes?\""
                a "\" Are we going further?\""
                p "\" I don't know.\""
                p "\" Are we?\""
                hide 12newalex206
                show 12newalex208
                with dissolve
                a "\" Well.\""
                a "\" I don't think I have to draw you a map.\""
                p "\" No.\""
                hide 12newalex208
                show 12newalex206
                with dissolve
                a "\" Then?\""
                p "\" Am I an animal?\""
                a "\" *Sigh*\""
                a "\" You know I'm just teasing.\""
                p "\" I know.\""
                p "\" But tell me you want me.\""
                hide 12newalex206
                show 12newalex209
                with dissolve
                a "\" I want you.\""
                p "\" Tell me you need me.\""
                a "\" I need you.\""
                p "\" And who am I?\""
                a "\" Puppy.\""
                p "\" No.\""
                a "\" [player_name].\""
                p "\" No.\""
                a "\" Baby?\""
                p "\" No.\""
                a "\" What then?\""
                default player_nik = "Love"
                show screen name_input( "What do you want her to call you?", player_nik )
                a "\" What then?\""
                # $ player_nik = renpy.input("What do you want her to call you?", screen = 'input' )
                # if player_nik == "":
                #     $ player_nik="Love"
                a "\" [player_nik].\""
                a "\" Puppy.\""
                hide 12newalex209
                show 12newalex210
                with dissolve
                " You enter her."
                a "\" Ahhh...\""
                hide 12newalex210
                show 12newalex211
                with dissolve
                a "\" Baby...\""
                a "\" Yes.\""
                scene alexvac animated with fade:
                    "18a1.webp"
                    pause 0.01
                    "18a2.webp"
                    pause 0.01
                    "18a3.webp"
                    pause 0.01
                    "18a4.webp"
                    pause 0.01
                    "18a5.webp"
                    pause 0.01
                    "18a6.webp"
                    pause 0.01
                    "18a7.webp"
                    pause 0.01
                    "18a8.webp"
                    pause 0.01
                    "18a9.webp"
                    pause 0.01
                    "18a10.webp"
                    pause 0.01
                    "18a11.webp"
                    pause 0.02
                    "18a12.webp"
                    pause 0.02
                    "18a13.webp"
                    pause 0.02
                    "18a14.webp"
                    pause 0.02
                    "18a15.webp"
                    pause 0.02
                    "18a16.webp"
                    pause 0.02
                    "18a17.webp"
                    pause 0.02
                    "18a18.webp"
                    pause 0.02
                    "18a19.webp"
                    pause 0.02
                    "18a20.webp"
                    pause 0.02
                    "18a21.webp"
                    pause 0.03
                    "18a22.webp"
                    pause 0.03
                    "18a23.webp"
                    pause 0.03
                    "18a24.webp"
                    pause 0.03
                    "18a25.webp"
                    pause 0.03
                    "18a26.webp"
                    pause 0.03
                    "18a27.webp"
                    pause 0.03
                    "18a28.webp"
                    pause 0.03
                    "18a29.webp"
                    pause 0.03
                    "18a30.webp"
                    pause 0.03
                    "18a31.webp"
                    pause 0.04
                    "18a32.webp"
                    pause 0.04
                    "18a33.webp"
                    pause 0.04
                    "18a34.webp"
                    pause 0.04
                    "18a35.webp"
                    pause 0.04
                    "18a36.webp"
                    pause 0.04
                    "18a37.webp"
                    pause 0.04
                    "18a38.webp"
                    pause 0.04
                    "18a39.webp"
                    pause 0.04
                    "18a40.webp"
                    pause 0.04
                    "18a39.webp"
                    pause 0.04
                    "18a38.webp"
                    pause 0.04
                    "18a37.webp"
                    pause 0.04
                    "18a36.webp"
                    pause 0.04
                    "18a35.webp"
                    pause 0.04
                    "18a34.webp"
                    pause 0.04
                    "18a33.webp"
                    pause 0.04
                    "18a32.webp"
                    pause 0.04
                    "18a31.webp"
                    pause 0.04
                    "18a30.webp"
                    pause 0.03
                    "18a29.webp"
                    pause 0.03
                    "18a28.webp"
                    pause 0.03
                    "18a27.webp"
                    pause 0.03
                    "18a26.webp"
                    pause 0.03
                    "18a25.webp"
                    pause 0.03
                    "18a24.webp"
                    pause 0.03
                    "18a23.webp"
                    pause 0.03
                    "18a22.webp"
                    pause 0.03
                    "18a21.webp"
                    pause 0.03
                    "18a20.webp"
                    pause 0.02
                    "18a19.webp"
                    pause 0.02
                    "18a18.webp"
                    pause 0.02
                    "18a17.webp"
                    pause 0.02
                    "18a16.webp"
                    pause 0.02
                    "18a15.webp"
                    pause 0.02
                    "18a14.webp"
                    pause 0.02
                    "18a13.webp"
                    pause 0.02
                    "18a12.webp"
                    pause 0.02
                    "18a11.webp"
                    pause 0.02
                    "18a10.webp"
                    pause 0.01
                    "18a9.webp"
                    pause 0.01
                    "18a8.webp"
                    pause 0.01
                    "18a7.webp"
                    pause 0.01
                    "18a6.webp"
                    pause 0.01
                    "18a5.webp"
                    pause 0.01
                    "18a4.webp"
                    pause 0.01
                    "18a3.webp"
                    pause 0.01
                    "18a2.webp"
                    pause 0.01
                    repeat
                a "\" Ahh...\""
                a "\" Yes...\""
                a "\" Yes... Baby...\""
                $ renpy.pause ()
                show 12newalex211
                with dissolve
                a "\" So good...\""
                a "\" So good to me....\""
                show 12newalex212
                with dissolve
                " You suddenly feel a tongue on your balls."
                p "\" Ohhh!\""
                scene alexvac2 animated with fade:
                    "19a1.webp"
                    pause 0.01
                    "19a2.webp"
                    pause 0.01
                    "19a3.webp"
                    pause 0.01
                    "19a4.webp"
                    pause 0.01
                    "19a5.webp"
                    pause 0.01
                    "19a6.webp"
                    pause 0.01
                    "19a7.webp"
                    pause 0.01
                    "19a8.webp"
                    pause 0.01
                    "19a9.webp"
                    pause 0.01
                    "19a10.webp"
                    pause 0.01
                    "19a11.webp"
                    pause 0.02
                    "19a12.webp"
                    pause 0.02
                    "19a13.webp"
                    pause 0.02
                    "19a14.webp"
                    pause 0.02
                    "19a15.webp"
                    pause 0.02
                    "19a16.webp"
                    pause 0.02
                    "19a17.webp"
                    pause 0.02
                    "19a18.webp"
                    pause 0.02
                    "19a19.webp"
                    pause 0.02
                    "19a20.webp"
                    pause 0.02
                    "19a21.webp"
                    pause 0.03
                    "19a22.webp"
                    pause 0.03
                    "19a23.webp"
                    pause 0.03
                    "19a24.webp"
                    pause 0.03
                    "19a25.webp"
                    pause 0.03
                    "19a26.webp"
                    pause 0.03
                    "19a27.webp"
                    pause 0.03
                    "19a28.webp"
                    pause 0.03
                    "19a29.webp"
                    pause 0.03
                    "19a30.webp"
                    pause 0.03
                    "19a31.webp"
                    pause 0.04
                    "19a32.webp"
                    pause 0.04
                    "19a33.webp"
                    pause 0.04
                    "19a34.webp"
                    pause 0.04
                    "19a35.webp"
                    pause 0.04
                    "19a36.webp"
                    pause 0.04
                    "19a37.webp"
                    pause 0.04
                    "19a38.webp"
                    pause 0.04
                    "19a39.webp"
                    pause 0.04
                    "19a40.webp"
                    pause 0.04
                    "19a39.webp"
                    pause 0.04
                    "19a38.webp"
                    pause 0.04
                    "19a37.webp"
                    pause 0.04
                    "19a36.webp"
                    pause 0.04
                    "19a35.webp"
                    pause 0.04
                    "19a34.webp"
                    pause 0.04
                    "19a33.webp"
                    pause 0.04
                    "19a32.webp"
                    pause 0.04
                    "19a31.webp"
                    pause 0.04
                    "19a30.webp"
                    pause 0.03
                    "19a29.webp"
                    pause 0.03
                    "19a28.webp"
                    pause 0.03
                    "19a27.webp"
                    pause 0.03
                    "19a26.webp"
                    pause 0.03
                    "19a25.webp"
                    pause 0.03
                    "19a24.webp"
                    pause 0.03
                    "19a23.webp"
                    pause 0.03
                    "19a22.webp"
                    pause 0.03
                    "19a21.webp"
                    pause 0.03
                    "19a20.webp"
                    pause 0.02
                    "19a19.webp"
                    pause 0.02
                    "19a18.webp"
                    pause 0.02
                    "19a17.webp"
                    pause 0.02
                    "19a16.webp"
                    pause 0.02
                    "19a15.webp"
                    pause 0.02
                    "19a14.webp"
                    pause 0.02
                    "19a13.webp"
                    pause 0.02
                    "19a12.webp"
                    pause 0.02
                    "19a11.webp"
                    pause 0.02
                    "19a10.webp"
                    pause 0.01
                    "19a9.webp"
                    pause 0.01
                    "19a8.webp"
                    pause 0.01
                    "19a7.webp"
                    pause 0.01
                    "19a6.webp"
                    pause 0.01
                    "19a5.webp"
                    pause 0.01
                    "19a4.webp"
                    pause 0.01
                    "19a3.webp"
                    pause 0.01
                    "19a2.webp"
                    pause 0.01
                    repeat
                a "\" Ahh...\""
                a "\" Yes...\""
                i "\" *Slurp*\""
                a "\" Yess...\""
                a "\" Give it to me...\""
                a "\" Yes...\""
                a "\" YEEESSSS!!!\""
                $ renpy.pause ()
                show 12newalex213
                with dissolve
                " Her convulsions as she cums make you cum too."
                p "\" Shit...\""
                a "\" Ahhh...\""
                p "\" Ahh...\""
                show 12newalex214
                with dissolve
                " Impossibly, you managed to pull out and cum on her belly."
                p "\" Damn it girls.\""
                a "\" Kiss me.\""
                hide 12newalex214
                show 12newalex215
                with dissolve
                " You do as she says."
                " And perhaps it was the endorphins, perhaps just your imagination, but her mouth tasted sweeter than ever."
                hide 12newalex215
                show 12newalex216
                with dissolve
                a "\" Uhhh...\""
                a "\" Need to go wash up.\""
                a "\" Be right back.\""
                if izzyin == True:
                    hide 12newalex216
                    show 12newalex217
                    with dissolve
                    " Izzy lies down too."
                    p "\" That was...\""
                    i "\" He he...\""
                    i "\" Thought you'd like it.\""
                    hide 12newalex217
                    show 12newalex219
                    with dissolve
                    i "\" Are you happy with us?\""
                    p "\" What?\""
                    i "\" Me and Alex.\""
                    p "\" Wouldn't any man be?\""
                    i "\" Sometimes with you, I can't tell.\""
                    p "\" I'm happy.\""
                    hide 12newalex219
                    show 12newalex220
                    with dissolve
                    i "\" A little unfair though.\""
                    p "\" What?\""
                    hide 12newalex220
                    show 12newalex221
                    with dissolve
                    " She grabs your dick."
                    p "\" Ohhh...\""
                    hide 12newalex221
                    show 12newalex220
                    with dissolve
                    i "\" Oh, indeed.\""
                    hide 12newalex220
                    show 12newalex222
                    with dissolve
                    i "\" He he he...\""
                    hide 12newalex222
                    show 12newalex220
                    with dissolve
                    i "\" The downside about dating two girls is that you'd better have the cardio.\""
                    p "\" I think I can manage it.\""
                    i "\" Do you?\""
                    hide 12newalex220
                    show 12newalex223
                    with dissolve
                    "She climbs in your lap, slips your dick inside her."
                    p "\" Ok.\""
                    hide 12newalex223
                    show 12newalex224
                    with dissolve
                    i "\" It's not complaining.\""
                    i "\" Growing.\""
                    i "\" I can feel it.\""
                    hide 12newalex224
                    show 12newalex225
                    with dissolve
                    a "\" Hey!\""
                    a "\" Can't leave the two of you alone for one minute.\""
                    i "\" Why would you want to?\""
                    scene alexvac3 animated with fade:
                        "20a1.webp"
                        pause 0.01
                        "20a2.webp"
                        pause 0.01
                        "20a3.webp"
                        pause 0.01
                        "20a4.webp"
                        pause 0.01
                        "20a5.webp"
                        pause 0.01
                        "20a6.webp"
                        pause 0.01
                        "20a7.webp"
                        pause 0.01
                        "20a8.webp"
                        pause 0.01
                        "20a9.webp"
                        pause 0.01
                        "20a10.webp"
                        pause 0.01
                        "20a11.webp"
                        pause 0.02
                        "20a12.webp"
                        pause 0.02
                        "20a13.webp"
                        pause 0.02
                        "20a14.webp"
                        pause 0.02
                        "20a15.webp"
                        pause 0.02
                        "20a16.webp"
                        pause 0.02
                        "20a17.webp"
                        pause 0.02
                        "20a18.webp"
                        pause 0.02
                        "20a19.webp"
                        pause 0.02
                        "20a20.webp"
                        pause 0.02
                        "20a21.webp"
                        pause 0.03
                        "20a22.webp"
                        pause 0.03
                        "20a23.webp"
                        pause 0.03
                        "20a24.webp"
                        pause 0.03
                        "20a25.webp"
                        pause 0.03
                        "20a26.webp"
                        pause 0.03
                        "20a27.webp"
                        pause 0.03
                        "20a28.webp"
                        pause 0.03
                        "20a29.webp"
                        pause 0.03
                        "20a30.webp"
                        pause 0.03
                        "20a31.webp"
                        pause 0.04
                        "20a32.webp"
                        pause 0.04
                        "20a33.webp"
                        pause 0.04
                        "20a34.webp"
                        pause 0.04
                        "20a35.webp"
                        pause 0.04
                        "20a36.webp"
                        pause 0.04
                        "20a37.webp"
                        pause 0.04
                        "20a38.webp"
                        pause 0.04
                        "20a39.webp"
                        pause 0.04
                        "20a40.webp"
                        pause 0.04
                        "20a39.webp"
                        pause 0.04
                        "20a38.webp"
                        pause 0.04
                        "20a37.webp"
                        pause 0.04
                        "20a36.webp"
                        pause 0.04
                        "20a35.webp"
                        pause 0.04
                        "20a34.webp"
                        pause 0.04
                        "20a33.webp"
                        pause 0.04
                        "20a32.webp"
                        pause 0.04
                        "20a31.webp"
                        pause 0.04
                        "20a30.webp"
                        pause 0.03
                        "20a29.webp"
                        pause 0.03
                        "20a28.webp"
                        pause 0.03
                        "20a27.webp"
                        pause 0.03
                        "20a26.webp"
                        pause 0.03
                        "20a25.webp"
                        pause 0.03
                        "20a24.webp"
                        pause 0.03
                        "20a23.webp"
                        pause 0.03
                        "20a22.webp"
                        pause 0.03
                        "20a21.webp"
                        pause 0.03
                        "20a20.webp"
                        pause 0.02
                        "20a19.webp"
                        pause 0.02
                        "20a18.webp"
                        pause 0.02
                        "20a17.webp"
                        pause 0.02
                        "20a16.webp"
                        pause 0.02
                        "20a15.webp"
                        pause 0.02
                        "20a14.webp"
                        pause 0.02
                        "20a13.webp"
                        pause 0.02
                        "20a12.webp"
                        pause 0.02
                        "20a11.webp"
                        pause 0.02
                        "20a10.webp"
                        pause 0.01
                        "20a9.webp"
                        pause 0.01
                        "20a8.webp"
                        pause 0.01
                        "20a7.webp"
                        pause 0.01
                        "20a6.webp"
                        pause 0.01
                        "20a5.webp"
                        pause 0.01
                        "20a4.webp"
                        pause 0.01
                        "20a3.webp"
                        pause 0.01
                        "20a2.webp"
                        pause 0.01
                        repeat
                    i "\" [player_nik]...\""
                    a "\" Fuck her....\""
                    a "\" Fuck her, puppy.\""
                    i "\" Ahh...\""
                    i "\" Ahhh...\""
                    a "\" Just like that.\""
                    a "\" Give it to her.\""
                    i "\" Ahhh...\""
                    i "\" AAAAHHHHHH...\""
                    $ renpy.pause ()
                    show 12newalex226
                    with dissolve
                    i "\" Yeah!!\""
                    i "\" YES!!!\""
                    show 12newalex227
                    with dissolve
                    " You fall back on the bed as you cum and Alex lies down beside you caressing your balls."
                    p "\" He hee...\""
                    p "\" Round two.\""
                    a "\" He he...\""
                    a "\" Don't even pretend that you don't like it.\""
                    hide 12newalex227
                    show 12newalex229
                    with dissolve
                    i "\" Going to go wash too.\""
                    i "\" Be right back.\""
                    hide 12newalex229
                    show 12newalex228
                    with dissolve
                    a "\" Love you.\""
                    p "\" Love you too.\""
                    hide 12newalex228
                    show 12newalex230
                    with dissolve
                    " Izzy comes out of the bathroom dressed."
                    a "\" Hey!\""
                    a "\" Where are you going?\""
                    hide 12newalex230
                    show 12newalex231
                    with dissolve
                    i "\" Going downstairs to get a soda or something.\""
                    i "\" Want something?\""
                    hide 12newalex231
                    show 12newalex232
                    with dissolve
                    a "\" I don't know.\""
                    a "\" Could use some ice cream.\""
                    p "\" If you wanted something creamy...\""
                    a "\" Watch it.\""
                    hide 12newalex232
                    show 12newalex231
                    with dissolve
                    i "\" Ice cream.\""
                    i "\" Got it.\""
                    i "\" I'll be right back.\""
                    $ renpy.end_replay()
                    jump ep13
                    scene end
                    with dissolve
                    $ renpy.pause ()
                    $ MainMenu(confirm=False)()

                else:
                    hide 12newalex216
                    show 12newalex218
                    with dissolve
                    " Izzy lies down too."
                    p "\" That was...\""
                    i "\" You're welcome.\""
                    p "\" He he...\""
                    p "\" What got into you.\""
                    i "\" Just doing what Alex wants of me.\""
                    p "\" Oh...\""
                    hide 12newalex218
                    show 12newalex229
                    with dissolve
                    i "\" Going to go wash my mouth.\""
                    hide 12newalex229
                    show 12newalex227
                    with dissolve
                    " In the mean time, Alex comes back and sits down next to you, caressing your balls."
                    p "\" He hee...\""
                    p "\" Round two.\""
                    a "\" I really am to bloated for that.\""
                    a "\" Just thought you'd like it.\""
                    p "\" You're not wrong.\""
                    hide 12newalex227
                    show 12newalex228
                    with dissolve
                    a "\" Love you.\""
                    p "\" Love you too.\""
                    hide 12newalex228
                    show 12newalex230
                    with dissolve
                    " Izzy comes out of the bathroom dressed."
                    a "\" Hey!\""
                    a "\" Where are you going?\""
                    hide 12newalex230
                    show 12newalex231
                    with dissolve
                    i "\" Going downstairs to get a soda or something.\""
                    i "\" Want something?\""
                    hide 12newalex231
                    show 12newalex232
                    with dissolve
                    a "\" I don't know.\""
                    a "\" Could use some ice cream.\""
                    p "\" If you wanted something creamy...\""
                    a "\" Watch it.\""
                    hide 12newalex232
                    show 12newalex231
                    with dissolve
                    i "\" Ice cream.\""
                    i "\" Got it.\""
                    i "\" I'll be right back.\""
                    jump ep13
                    scene end
                    with dissolve
                    $ renpy.pause ()
                    $ MainMenu(confirm=False)()
