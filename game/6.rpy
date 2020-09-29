label ep6:
                scene 5newalex251
                with dissolve
                default izzyclairekiss = False
                default alexep7hug = False
                default alexep7pussy = False
                default narysastart = False
                " Boris takes you to his office."
                show 5newalex252
                with dissolve
                b "\" Hmm...\""
                p "\" Boss?\""
                b "\" I'm thinking.\""
                b "\" Why don't you go get me a beer?\""
                p "\" Sure.\""
                hide 5newalex252
                show 5newalex253
                with dissolve
                " You head to the kitchen."
                a "\" [player_name]?\""
                p "\" Boss wants a beer.\""
                hide 5newalex253
                show 5newalex254
                with dissolve
                " She caresses your chin."
                a "\" You two are getting close.\""
                p "\" I wouldn't say that.\""
                a "\" Yes you are.\""
                a "\" You just don't like to admit it.\""
                a "\" *Sigh* Mutual man-crush...\""
                p "\" You're going way overboard.\""
                p "\" I think he's just stuck with me.\""
                a "\" You'll see.\""
                a "\" Now get him his beer.\""
                hide 5newalex254
                show 5newalex255
                with dissolve
                " You bring Boris back the beer."
                b "\" Ahh...\""
                b "\" That hit the spot.\""
                hide 5newalex255
                show 5newalex256
                with dissolve
                b "\" I'm thinking...\""
                b "\" Georgie...\""
                b "\" Did he strike you as being too familiar?\""
                p "\" Too familiar?\""
                b "\" He called me a pimp.\""
                b "\" Like he's too comfortable around me.\""
                b "\" Like he's forgot who I am, and what our relationship is.\""
                call screen screen33

label ep6georgieyes:
                scene 5newalex256
                with dissolve
                $ borispts = borispts + 1
                p "\" Maybe.\""
                p "\" Maybe he's starting to see you as a friend, rather than a business partner.\""
                show 6newalex2
                with dissolve
                b "\" Yeah...\""
                b "\" Getting very familiar.\""
                b "\" I'll have to sleep on this.\""
                jump ep6cont1

label ep6georgieno:
                scene 5newalex256
                with dissolve
                p "\" No.\""
                p "\" He's just being friendly.\""
                show 6newalex3
                with dissolve
                b "\" Maybe.\""
                b "\" But you should never let anyone take liberties with you.\""
                b "\" They should always remember their place.\""
                b "\" I'll have to sleep on this.\""
                jump ep6cont1

label ep6cont1:
                scene 5newalex252
                with dissolve
                b "\" But that's for tomorrow, not tonight.\""
                b "\" Tonight. Why don't we give Alexandra a break?\""
                b "\" Let's go out to eat.\""
                p "\" You're the boss.\""
                b "\" Let's go find Alex.\""
                show 6newalex4
                with dissolve
                " You go to the kitchen."
                a "\" Dad?\""
                b "\" Put the spoon down.\""
                b "\" I'm taking you all out.\""
                a "\" Out?\""
                b "\" To eat somewhere,\""
                hide 6newalex4
                show 6newalex5
                with dissolve
                a "\" Hmm...\""
                a "\" Let me see...\""
                a "\" Slave away for a few hours for two ungrateful jackasses?\""
                a "\" Or... Go out. Hmmm....\""
                a "\" This is difficult.\""
                hide 6newalex5
                show 6newalex6
                with dissolve
                a "\" But I think I'll go for option 'b'.\""
                b "\" No need for that, girl.\""
                a "\" Where are you taking us?\""
                b "\" I know a few places.\""
                hide 6newalex6
                show 6newalex7
                with dissolve
                a "\" Let's go get Izzy.\""
                a "\" Maybe find you a change of clothes, and a shower?\""
                hide 6newalex7
                show 6newalex8
                with dissolve
                " You go to Alex's room."
                a "\" Hmmm...\""
                a "\" Not in here.\""
                a "\" Must be in the bathroom.\""
                hide 6newalex8
                show 6newalex9
                with dissolve
                a "\" Izzy?\""
                i "\" Huh?\""
                a "\" What are you up to?\""
                i "\" What does it look like?\""
                i "\" Shaving my legs.\""
                hide 6newalex9
                show 6newalex10
                with dissolve
                i "\" What's up?\""
                a "\" Dad wants to take us out.\""
                a "\" To dinner, I mean.\""
                a "\" When can you be ready?\""
                i "\" A few minutes.\""
                hide 6newalex10
                show 6newalex11
                with dissolve
                a "\" Also. Do you mind if [player_name] takes a shower while you shave?\""
                a "\" I'll go get him some fresh clothes.\""
                if izzyin == True:
                    i "\" Do I mind?\""
                    a "\" Do you?\""
                    i "\" Is that a trick question?\""
                    a "\" It's polite for me to ask.\""
                    hide 6newalex11
                    show 6newalex12
                    with dissolve
                    a "\" You wash up.\""
                    a "\" I'll go find you something.\""
                    p "\" From your Dad's closet?\""
                    a "\" Would you like to try some clothes from mine?\""
                    p "\" No need to go that far.\""
                    a "\" Dad's closet it is then.\""
                    hide 6newalex12
                    label galleryScene3:
                    show 5newalex126
                    with dissolve
                    " You start showering."
                    hide 5newalex126
                    show 6newalex13
                    with dissolve
                    " Meanwhile Izzy keeps shaving."
                    p "\" Do you do that every day?\""
                    i "\" I try to.\""
                    i "\" I don't always get the chance.\""
                    p "\" What about the wax stuff?\""
                    i "\" Takes a long time. I don't always have that kind of time.\""
                    hide 6newalex13
                    show 6newalex15
                    with dissolve
                    " You get out of the shower."
                    p "\" I'm done.\""
                    hide 6newalex15
                    show 6newalex16
                    with dissolve
                    i "\" I'm almost done too.\""
                    i "\" Just one more thing.\""
                    hide 6newalex16
                    show 6newalex17
                    with dissolve
                    " She throws away the towel, and starts trimming her pubic hair."
                    p "\" Izzy?\""
                    i "\" I have to trim this too.\""
                    i "\" Will only take a minute.\""
                    hide 6newalex17
                    show 6newalex18
                    with dissolve
                    p "\" *Gulp*\""
                    hide 6newalex18
                    show 6newalex19
                    with dissolve
                    i "\" Hey!\""
                    p "\" What?\""
                    i "\" We don't have time.\""
                    i "\" Alex and Mr. Boris are waiting for us.\""
                    p "\" I know.\""
                    " Do you want to give Claire a kiss?"
                    call screen screen34

                else:
                    i "\" I don't mind.\""
                    i "\" He might, though.\""
                    a "\" Please.\""
                    hide 6newalex11
                    show 6newalex12
                    with dissolve
                    a "\" You wash up.\""
                    a "\" I'll go find you something.\""
                    p "\" From your Dad's closet?\""
                    a "\" Would you like to try some of the clothes from mine?\""
                    p "\" No need to go that far.\""
                    a "\" Dad's closet it is, then.\""
                    hide 6newalex12
                    show 5newalex126
                    with dissolve
                    " You start showering."
                    hide 5newalex126
                    show 6newalex13
                    with dissolve
                    " Meanwhile Izzy keeps shaving, and ignoring you completely."
                    p "\" Do you do that every day?\""
                    i "\" I try to.\""
                    i "\" I don't always get the chance.\""
                    hide 6newalex13
                    show 6newalex26
                    with dissolve
                    " She finishes up, and says..."
                    i "\" Done.\""
                    i "\" We'll wait for you outside.\""
                    hide 6newalex26
                    show 5newalex126
                    with dissolve
                    " You finish up as well, and head outside."
                    hide 5newalex126
                    show 6newalex27
                    with dissolve
                    a "\" We're all ready.\""
                    p "\" I see.\""
                    a "\" I laid out some clothes for you on that chair.\""
                    p "\" Thanks.\""
                    hide 6newalex27
                    show 6newalex38
                    with dissolve
                    " You get dressed."
                    p "\" Your Dad has a thing for sweaters, eh?\""
                    a "\" I guess so.\""
                    hide 6newalex38
                    show 6newalex27
                    with dissolve
                    a "\" We should get going.\""
                    a "\" He's probably waiting for us.\""
                    hide 6newalex27
                    show back
                    with dissolve
                    show 6newalex39
                    with dissolve
                    " You all head down and get in the car."
                    b "\" Found a place.\""
                    " He gives you an address."
                    hide 6newalex39
                    show back1
                    with dissolve
                    show 6newalex40
                    with dissolve
                    a "\" Best be good food Dad.\""
                    a "\" Not just... Edible.\""
                    b "\" *Sigh*\""
                    a "\" He he...\""
                    i "\" Thank you for treating us to dinner, Mr. Boris.\""
                    hide 6newalex40
                    show 6newalex41
                    with dissolve
                    b "\" I'm very impressed by your maturity Isabella.\""
                    i "\" Sir?\""
                    b "\" I mean, you and Alex broke up. Yes?\""
                    b "\" You're taking it so well.\""
                    b "\" I was afraid we might not see you again.\""
                    hide 6newalex41
                    show 6newalex42
                    with dissolve
                    i "\" Well, that's how life is.\""
                    i "\" Isn't that so, Mr. Boris?\""
                    b "\" Very stoic in your views.\""
                    jump ep6cont2

label ep7claireno:
                     scene 6newalex22
                     with dissolve
                     p "\" You just looked huggable.\""
                     i "\" He he...\""
                     i "\" Alright.\""
                     show 6newalex25
                     with dissolve
                     " She untangles herself from you."
                     i "\" But now we really should get going.\""
                     p "\" Alright.\""
                     hide 6newalex25
                     show 6newalex28
                     with dissolve
                     a "\" You were in there a long time.\""
                     i "\" Just had to do some maintenance.\""
                     a "\" Well, hurry up.\""
                     a "\" Dad's waiting.\""
                     hide 6newalex28
                     $ renpy.end_replay()
                     show 6newalex37
                     with dissolve
                     " The girls get dressed."
                     hide 6newalex37
                     show 6newalex38
                     with dissolve
                     " And Alex finds something for you too."
                     p "\" Your Dad has a thing for sweaters, eh?\""
                     a "\" I guess so.\""
                     hide 6newalex38
                     show 6newalex27
                     with dissolve
                     a "\" We should get going.\""
                     a "\" He's probably waiting for us.\""
                     hide 6newalex27
                     show back
                     with dissolve
                     show 6newalex39
                     with dissolve
                     " You all head down and get in the car."
                     b "\" Found a place.\""
                     " He gives you an address."
                     hide 6newalex39
                     show back1
                     with dissolve
                     show 6newalex40
                     with dissolve
                     a "\" Best be good food, Dad.\""
                     a "\" Not just... Edible.\""
                     b "\" *Sigh*\""
                     a "\" He he...\""
                     i "\" Thank you for treating us to dinner, Mr. Boris.\""
                     hide 6newalex40
                     show 6newalex41
                     with dissolve
                     b "\" I'm very impressed by your maturity Isabella.\""
                     i "\" Sir?\""
                     b "\" I mean, you and Alex broke up. Yes?\""
                     b "\" You're taking it so well.\""
                     b "\" I was afraid we might not see you again.\""
                     hide 6newalex41
                     show 6newalex42
                     with dissolve
                     i "\" Well, that's how life is.\""
                     i "\" Isn't that so, Mr. Boris?\""
                     b "\" Very stoic in your views.\""
                     jump ep6cont2

label ep7claireyes:
                $ izzyclairekiss = True
                scene 6newalex19
                p "\" There's just someone else I want to greet properly.\""
                show 6newalex20
                with dissolve
                " You kneel and kiss her pussy."
                i "\" Hey!\""
                p "\" Hello Claire.\""
                p "\" How are you sweetie?\""
                p "\" Getting a new doo?\""
                hide 6newalex20
                show 6newalex21
                with dissolve
                i "\" Ha ha ha...\""
                i "\" Stop being stupid.\""
                hide 6newalex21
                show 6newalex22
                with dissolve
                " You come back up."
                p "\" What?\""
                p "\" She deserves a greeting too.\""
                i "\" Sure, but a kiss?\""
                i "\" What about me?\""
                i "\" Don't I get one?\""
                hide 6newalex22
                show 6newalex23
                with dissolve
                " You kiss her, and she answers back sweetly."
                hide 6newalex23
                show 6newalex24
                with dissolve
                i "\" How are you what you are, and yet be so sweet and silly at the same time?\""
                p "\" I can ask the same of you.\""
                i "\" I guess.\""
                hide 6newalex24
                show 6newalex25
                with dissolve
                " She untangles herself from you."
                i "\" But now we really should get going.\""
                p "\" Alright.\""
                hide 6newalex25
                show 6newalex28
                with dissolve
                a "\" You were in there a long time.\""
                i "\" Just had to do some maintenance.\""
                hide 6newalex28
                show 6newalex29
                with dissolve
                " She sits down on the bed."
                a "\" Got your clubbing outfit.\""
                a "\" Hope that's ok.\""
                i "\" I don't care.\""
                hide 6newalex29
                $ renpy.end_replay()
                show 6newalex30
                with dissolve
                a "\" So, you two are getting along aright?\""
                a "\" I don't know.\""
                a "\" I just feel like I'm missing something.\""
                a "\" There's something you're not saying.\""
                hide 6newalex30
                show 6newalex31
                with dissolve
                i "\" There really isn't.\""
                i "\" He and Claire cuddled a bit.\""
                a "\" Ha ha...\""
                a "\" Really?\""
                i "\" Apparently, they're quite fond of one another.\""
                hide 6newalex31
                show 6newalex32
                with dissolve
                a "\" He he he...\""
                a "\" Really puppy?\""
                p "\" What can I say?\""
                p "\" She's been very good to me.\""
                hide 6newalex32
                show 6newalex33
                with dissolve
                " She comes over and gives you a kiss."
                hide 6newalex33
                show 6newalex35
                with dissolve
                " Then goes to Izzy, and does the same."
                hide 6newalex35
                show 6newalex36
                with dissolve
                a "\" Isn't this nice.\""
                a "\" When we just all get along?\""
                a "\" Now hurry up, Dad's waiting.\""
                hide 6newalex36
                show 6newalex37
                with dissolve
                " The girls get dressed."
                hide 6newalex37
                show 6newalex38
                with dissolve
                " And Alex finds something for you too."
                p "\" Your Dad has a thing for sweaters, eh?\""
                a "\" I guess so.\""
                hide 6newalex38
                show 6newalex27
                with dissolve
                a "\" We should get going.\""
                a "\" He's probably waiting for us.\""
                hide 6newalex27
                show back
                with dissolve
                show 6newalex39
                with dissolve
                " You all head down and get in the car."
                b "\" Found a place.\""
                " He gives you an address."
                hide 6newalex39
                show back1
                with dissolve
                show 6newalex40
                with dissolve
                a "\" Best be good food, Dad.\""
                a "\" Not just... Edible.\""
                b "\" *Sigh*\""
                a "\" He he...\""
                i "\" Thank you for treating us to dinner, Mr. Boris.\""
                hide 6newalex40
                show 6newalex41
                with dissolve
                b "\" I'm very impressed by your maturity Isabella.\""
                i "\" Sir?\""
                b "\" I mean, you and Alex broke up. Yes?\""
                b "\" You're taking it so well.\""
                b "\" I was afraid we might not see you again.\""
                hide 6newalex41
                show 6newalex43
                with dissolve
                i "\" I'm not that petty, Mr. Boris.\""
                i "\" Besides, we have too many things in common.\""
                b "\" Things in common?\""
                hide 6newalex43
                show 6newalex44
                with dissolve
                i "\" We're both very fond of Alex.\""
                i "\" And like I said to her earlier. He and Claire seem to be besties.\""
                b "\" Claire?\""
                b "\" Have I met her?\""
                hide 6newalex44
                show 6newalex45
                with dissolve
                " Alex's cheeks inflate, trying not to laugh."
                b "\" Is she nice?\""
                hide 6newalex45
                show 6newalex46
                with dissolve
                a "\" Ha ha ha...\""
                a "\" Dad, please?\""
                b "\" What?\""
                b "\" You're saying I wouldn't like her?\""
                a "\" Ha ha ha...\""
                hide 6newalex46
                show 6newalex44
                with dissolve
                i "\" Think most men would.\""
                a "\" Ha ha...\""
                a "\" You too. Stop it.\""
                hide 6newalex44
                show 6newalex41
                with dissolve
                b "\" Well, if you ever want to bring her over.\""
                a "\" Snigger...\""
                b "\" I'm sure we'd get along.\""
                a "\" *Snigger* Ok, Dad.\'"
                hide 6newalex41
                jump ep6cont2

label ep6cont2:
                scene 6newalex47
                with dissolve
                " You get to the restaurant."
                i "\" It's very nice.\""
                a "\" We'll see about the food.\""
                hide 6newalex47
                show 6newalex48
                with dissolve
                " And then order."
                hide 6newalex48
                show 6newalex50
                with dissolve
                i "\" Thank you, Mr. Boris.\""
                hide 6newalex50
                show 6newalex51
                with dissolve
                b "\" Please...\""
                b "\" And stop calling me Mr. Boris.\" "
                b "\" You know you're like a Daughter to me.\""
                hide 6newalex51
                show 6newalex50
                with dissolve
                i "\" Thank you.\""
                i "\" I will... Boris.\""
                hide 6newalex50
                show 6newalex51
                with dissolve
                i "\" Now, how is school?\""
                hide 6newalex51
                show 6newalex48
                with dissolve
                " You all chat about this and that while you eat."
                hide 6newalex48
                show 6newalex49
                with dissolve
                a "\" What did you get?\""
                a "\" Is it good?\""
                p "\" It's ok.\""
                hide 6newalex49
                show 6newalex52
                with dissolve
                " She comes to you."
                a "\" I want a taste.\""
                hide 6newalex52
                show 6newalex53
                with dissolve
                " She climbs into your lap, and starts eating from your plate."
                a "\" Let's see.\""
                a "\" What do we have here?\""
                hide 6newalex53
                show 6newalex56
                with dissolve
                " Boris looks with disapproval."
                " But in the end, just sighs."
                hide 6newalex56
                show 6newalex54
                with dissolve
                a "\" Hmmmm...\""
                a "\" Not bad.\""
                a "\" Not bad at all.\""
                a "\" But I can make better.\""
                hide 6newalex54
                show 6newalex56
                with dissolve
                b "\" Don't be a braggart.\""
                hide 6newalex56
                show 6newalex55
                with dissolve
                a "\" Well, I can.\""
                a "\" Is it bragging if it's true?\""
                b "\" Yes.\""
                a "\" Ok.\""
                hide 6newalex55
                show 6newalex48
                with dissolve
                " She gets back to her seat, and you all finish your meals."
                hide 6newalex48
                show 6newalex57
                with dissolve
                a "\" Ugh...\""
                a "\" Feel so full.\""
                a "\" I think I might be sick.\""
                hide 6newalex57
                show 6newalex58
                with dissolve
                i "\" You ate too much.\""
                i "\" You ate half of [player_name]'s portion too.\""
                hide 6newalex58
                show 6newalex57
                with dissolve
                a "\" Ugh...\""
                hide 6newalex58
                show back1
                with dissolve
                show 6newalex59
                with dissolve
                " On the way back, Alexandra is still feeling sick."
                i "\" Don't worry.\""
                i "\" Well do a few laps in the pool, and you'll feel better. You'll see.\""
                a "\" Greed got the better of me.\""
                hide 6newalex59
                show 6newalex61
                with dissolve
                " When you get to the villa, Boris asks..."
                b "\" You want a digestive, dear?\""
                a "\" Nah...\""
                a "\" I'll just do a couple of laps like Izzy says.\""
                b "\" Alright.\""
                hide 6newalex61
                show 6newalex60
                with dissolve
                i "\" Bathing suits?\""
                i "\" Should I get some?\""
                a "\" I think I have some there.\""
                hide 6newalex60
                show 6newalex62
                with dissolve
                a "\" You're coming too.\""
                a "\" Right, [player_name]?\""
                p "\" Of course.\""
                hide 6newalex62
                show 6newalex63
                with dissolve
                " You all head to the pool area."
                " When you hear Alex gasp."
                " Do you go to her?"
                call screen screen35

label ep7hugalex:
                scene 6newalex64
                with dissolve
                $ alexep7hug = True
                p "\" You ok?\""
                a "\" Yeah.\""
                a "\" It's just that here... Those men...\""
                a "\" I had forgotten until now.\""
                show 6newalex65
                with dissolve
                a "\" It's fine.\""
                a "\" Soon it will be just a memory.\""
                a "\" Then, not even that.\""
                jump ep6cont3

label ep7nohugalex:
                scene 6newalex63
                with dissolve
                " She recovers in just a second, and she's back to normal."
                jump ep6cont3

label ep6cont3:
                scene 6newalex66
                with dissolve
                " You head inside the pool house, and turn the lights on."
                i "\" You ok?\""
                a "\" What?\""
                i "\" Outside...\""
                a "\" It was nothing.\""
                a "\" Just a chill wind.\""
                i "\" If you say so.\""
                i "\" I'll go find some swimsuits.\""
                show 6newalex67
                with dissolve
                " Izzy goes off, while you and Alex head to the bedroom."
                p "\" About what Isabella said.\""
                p "\" You sure you're ok?\""
                a "\" Yeah.\""
                a "\" It's nothing.\""
                hide 6newalex67
                show 6newalex68
                with dissolve
                a "\" Now, how about you help me change?\""
                p "\" Help you change?\""
                a "\" Yeah.\""
                p "\" Like a queen.\""
                hide 6newalex68
                show 6newalex69
                with dissolve
                a "\" It's fine if you don't want to.\""
                a "\" I was just thinking...\""
                a "\" You know...\""
                a "\" Give my gangster boyfriend a chance to squeeze a tit.\""
                a "\" You know... Maybe grab me by the pussy.\""
                a "\" But if he doesn't want to...\""
                hide 6newalex69
                show 6newalex70
                with dissolve
                p "\" Hey, hey...\""
                p "\" You should've been more specific.\""
                a "\" Too late now.\""
                a "\" We've committed to this.\""
                p "\" I haven't.\""
                hide 6newalex70
                show 6newalex71
                with dissolve
                " You pull her sweater over her head, and cup her breasts."
                a "\" So, now he does it.\""
                a "\" Needs a special invitation.\""
                hide 6newalex71
                show 6newalex72
                with dissolve
                " You push her on the bed."
                a "\" Ooooh...\""
                a "\" Asserting himself.\""
                a "\" I like that.\""
                hide 6newalex72
                show 6newalex73
                with dissolve
                " You get on top of her."
                p "\" Hey there.\""
                a "\" Hey.\""
                hide 6newalex73
                show 6newalex74
                with dissolve
                a "\" Am I being cruel to you?\""
                a "\" Denying you?\""
                p "\" I don't know if I'd call it cruel.\""
                p "\" Maybe if I wasn't sure about my dreams.\""
                hide 6newalex74
                show 6newalex75
                with dissolve
                " She turns on her side."
                a "\" Right.\""
                a "\" Your dreams again.\""
                p "\" And yours.\""
                p "\" How did you know to call me the night I got hurt?\""
                a "\"...\""
                p "\" Well?\""
                a "\" Coincidence.\""
                p "\" If that's what you want to tell yourself.\""
                a "\" I see.\""
                hide 6newalex75
                show 6newalex76
                with dissolve
                a "\" You know...\""
                a "\" About me denying you...\""
                p "\" Not wanting to fuck me, you mean?\""
                hide 6newalex76
                show 6newalex79
                with dissolve
                a "\" Being intimate, is how I'd word it.\""
                a "\" It's not that I don't want to.\""
                a "\" It's...\""
                p "\" I know. You said it.\""
                hide 6newalex79
                show 6newalex76
                with dissolve
                a "\" But I'm my Father's Daughter.\""
                a "\" Grew up with him.\""
                p "\" What do you mean?\""
                a "\" I know he wasn't an angel.\""
                hide 6newalex76
                show 6newalex77
                with dissolve
                a "\" He... You know...\""
                a "\" There were others...\""
                p "\" And?\""
                a "\" And so are all the others in his circle.\""
                a "\" I know.\""
                p "\" What are you trying to say?\""
                a "\" I'm saying there will be others.\""
                a "\" With you...\""
                p "\" Izzy?\""
                a "\" I'm not talking about Izzy.\""
                a "\" But I know what goes on with guys like you.\""
                hide 6newalex77
                show 6newalex78
                with dissolve
                " She gives you a kiss, and whispers..."
                a "\" I know what I signed up for.\""
                a "\" Just like my Dad is what he is.\""
                a "\" Just... Just don't ever let me find out about it.\""
                p "\" Alex...\""
                a "\" I mean it.\""
                a "\" I don't want to know.\""
                hide 6newalex78
                show 6newalex80
                with dissolve
                " She gets up and takes off the rest of her clothes."
                a "\" Now, where's Izzy with that suit.\""
                i "\" Here.\""
                hide 6newalex80
                show 6newalex81
                with dissolve
                a "\" Found them?\""
                i "\" Of course.\""
                i "\" Found something for [player_name] too.\""
                i "\" But what are you doing?\""
                a "\" What?\""
                hide 6newalex81
                show 6newalex82
                with dissolve
                i "\" Showing off your bony ass?\""
                a "\" My ass isn't bony?\""
                i "\" He he he...\""
                i "\" Come here.\""
                hide 6newalex82
                show 6newalex83
                with dissolve
                i "\" You know I like you slender.\""
                a "\" You said bony as second ago.\""
                i "\" You know what I mean.\""
                a "\" He he he...\""
                if izzyin == True:
                    i "\" I love you, babe.\""
                    i "\" But you're skinny.\""
                    hide 6newalex83
                    show 6newalex84
                    with dissolve
                    " She turns around and lifts her dress."
                    i "\" You need a little more meat to have an ass.\""
                    hide 6newalex84
                    show 6newalex85
                    with dissolve
                    " Getting a closer look, you have to agree."
                    hide 6newalex85
                    show 6newalex86
                    with dissolve
                    a "\" Do you have to outshine me?\""
                    i "\" He he...\""
                    i "\" In this case, I do.\""
                    a "\" Grrr...\""
                    i "\" He he he...\""
                    i "\" I'll go to the bathroom and change too, ok?\""
                    a "\" Sure.\""
                    hide 6newalex86
                    show 6newalex87
                    with dissolve
                    " Izzy goes to the bathroom."
                    a "\" Sigh...\""
                    p "\" Are you really upset?\""
                    hide 6newalex87
                    show 6newalex88
                    with dissolve
                    a "\" Ha ha ha...\""
                    a "\" Don't be silly.\""
                    hide 6newalex88
                    show 6newalex89
                    with dissolve
                    " You change and head out."
                    $ renpy.end_replay()
                    jump ep6cont4

                else:
                    i "\" I'll go to the bathroom and change too, ok?\""
                    a "\" Sure.\""
                    hide 6newalex83
                    show 6newalex87
                    with dissolve
                    " Izzy goes to the bathroom."
                    a "\" She's still so shy around you.\""
                    a "\" I don't get it.\""
                    a "\" I hope you two can close that gap.\""
                    hide 6newalex87
                    show 6newalex89
                    with dissolve
                    " You change and head out."
                    jump ep6cont4

label ep6cont4:
                scene 6newalex90
                with dissolve
                a "\" Oooh...\""
                a "\" A little chilly.\""
                p "\" Still feeling sick?\""
                a "\" I wasn't sick. Just overate.\""
                p "\" Does that mean you'll grow fat?\""
                p "\" You'll turn me into a chubby chaser?\""
                a "\" Fuck you.\""
                p "\" He he...\""
                show 6newalex91
                with dissolve
                " She gets up on the diving board."
                a "\" Now, watch this.\""
                hide 6newalex91
                show 6newalex92
                with dissolve
                " And dives into the water."
                hide 6newalex92
                show 6newalex93
                with dissolve
                a "\" Ahhh...\""
                a "\" Cold!\""
                a "\" Jump in!\""
                p "\" You just said it was cold.\""
                a "\" I meant refreshing.\""
                hide 6newalex93
                show 6newalex94
                with dissolve
                a "\" Come on.\""
                a "\" I've already seen your dick, so I won't be fooled by shrinkage.\""
                p "\" You have mouth on you.\""
                a "\" Come and shut it for me.\""
                hide 6newalex94
                show 6newalex95
                with dissolve
                " You dive in after her."
                hide 6newalex95
                show 6newalex96
                with dissolve
                " And you land near her crotch."
                " Do you want to grab it?"
                call screen screen36

label ep7alexpussyno:
                scene 6newalex99
                with dissolve
                " You come up."
                a "\" Hey, there.\""
                p "\" Hello, yourself.\""
                p "\" How are ya?\""
                show 6newalex100
                with dissolve
                a "\" Bloated.\""
                p "\" Your sexy talk sometimes leaves a lot to be desired, you know that?\""
                a "\" He he he...\""
                jump ep6cont5

label ep7alexpussy:
                scene 6newalex97
                with dissolve
                $ alexep7pussy = True
                " You reach out and cup her vagina."
                show 6newalex98
                with dissolve
                a "\" Ooooh...\""
                a "\" What the???\""
                hide 6newalex98
                show 6newalex99
                with dissolve
                " You come up."
                a "\" Hey there.\""
                a "\" What was that?\""
                p "\" What do you mean?\""
                a "\" I think I just got attacked.\""
                p "\" Must've been a pussy shark.\""
                hide 6newalex99
                show 6newalex100
                with dissolve
                a "\" Pussy shark?\""
                p "\" Little known species.\""
                p "\" Lives in pools.\""
                a "\" Hmmm...\""
                jump ep6cont5

label ep6cont5:
                scene 6newalex101
                with dissolve
                i "\" Hey.\""
                i "\" How's the water?\""
                a "\" Cold. Jump in.\""
                i "\" I don't think so.\""
                show 6newalex102
                with dissolve
                " She gently lowers herself into the pool."
                hide 6newalex102
                show 6newalex103
                with dissolve
                i "\" Ugh, this is cold.\""
                hide 6newalex103
                show 6newalex104
                with dissolve
                a "\" Puppy...\""
                a "\" She's asking for you to warm her up.\""
                p "\" I think she's just saying that the water is cold\""
                a "\" You should warm her anyway.\""
                if izzyin == True:
                    jump ep6izzypoolizzyin
                else:
                    jump ep6izzypoolnoizzyin

label ep6izzypoolnoizzyin:
                scene 6newalex105
                with dissolve
                i "\" I was just making a remark.\""
                i "\" I'm fine.\""
                show 6newalex106
                with dissolve
                a "\" Go to her.\""
                p "\" She said she's fine.\""
                a "\" Go anyway.\""
                hide 6newalex106
                show 6newalex107
                with dissolve
                " You swim to Izzy."
                i "\" I said I'm fine.\""
                p "\" I heard you.\""
                i "\" *Sigh*\""
                hide 6newalex107
                show 6newalex113
                with dissolve
                " She swims away from you, and goes to Alex."
                i "\" But we're here to do some laps, right?\""
                i "\" Keep slender.\""
                a "\" After what you said about my ass, I'm not so sure anymore.\""
                i "\" He he...\""
                hide 6newalex113
                show 6newalex114
                with dissolve
                " The girls start to swim up and down the pool."
                hide 6newalex114
                show 6newalex115
                with dissolve
                " Meanwhile, you sit on the edge of the pool and watch."
                hide 6newalex115
                show 6newalex116
                with dissolve
                " After a few laps..."
                i "\" Whoa...\""
                i "\" Refreshing.\""
                i "\" But I think that's enough.\""
                a "\" I'll swim a while longer.\""
                a "\" Make my ass bonier.\""
                i "\" Come on.\""
                a "\" He he...\""
                hide 6newalex116
                show 6newalex117
                with dissolve
                " While Alex keeps swimming, Izzy comes and sits next to you."
                hide 6newalex117
                show 6newalex118
                with dissolve
                " After a few minutes, she says..."
                i "\" You and I are not going to get along, are we?\""
                p "\" I don't know.\""
                hide 6newalex118
                show 6newalex119
                with dissolve
                i "\" I just want to say...\""
                i "\" It won't be my fault.\""
                p "\" You think so?\""
                hide 6newalex119
                show 6newalex120
                with dissolve
                i "\" I was willing to accept you, and learn to love you.\""
                i "\" It was you who kept pushing me away.\""
                p "\" Learn to love?\""
                i "\" What?\""
                p "\" I don't think that's how it works.\""
                i "\" Are we not in control of our emotions?\""
                p "\" When I dream. I don't dream of you.\""
                hide 6newalex120
                show 6newalex121
                with dissolve
                i "\" I see.\""
                i "\" So, that's that.\""
                " Do you want to try to get closer to her?"
                call screen screen37

label ep7izzynotry:
                scene 6newalex121
                with dissolve
                p "\" I guess it is.\""
                show 6newalex124
                with dissolve
                a "\" Hey.\""
                a "\" I think I'm done.\""
                a "\" Dad's about to go to bed.\""
                a "\" I'll go kiss him goodnight.\""
                a "\" He likes me to do that when I'm home.\""
                i "\" We'll be right behind you.\""
                hide 6newalex124
                show 6newalex125
                with dissolve
                " Alexandra leaves."
                hide 6newalex125
                show 6newalex126
                with dissolve
                i "\" I guess we should get changed.\""
                p "\" Right.\""
                hide 6newalex126
                show 6newalex131
                with dissolve
                " You head back in the pool house, and change."
                hide 6newalex131
                show 6newalex135
                with dissolve
                " Then you follow Alex in the main house."
                " Izzy doesn't say a word to you during all this time."
                hide 6newalex135
                show 6newalex136
                with dissolve
                a "\" Hey.\""
                hide 6newalex136
                show 6newalex137
                with dissolve
                i "\" You kissed your Dad goodnight?\""
                a "\" Yeah.\""
                hide 6newalex137
                show 6newalex138
                with dissolve
                a "\" Have to go to sleep.\""
                a "\" I'd invite you to stay puppy...\""
                p "\" Your Dad's house.\""
                p "\" I get it.\""
                a "\" Good night.\""
                p "\" Good night.\""
                jump ep6cont6

label ep7izzytry:
                $ izzyin = True
                scene 6newalex121
                with dissolve
                p "\" Sigh...\""
                p "\" I never meant to...\""
                i "\" What?\""
                p "\" Make you feel rejected in some way.\""
                p "\" I'd like to... If you're willing...\""
                p "\" Maybe start over?\""
                show 6newalex119
                with dissolve
                i "\" Start over?\""
                p "\" If you want.\""
                i "\" I'm willing to try.\""
                p "\" Alright.\""
                show 6newalex124
                with dissolve
                a "\" Hey.\""
                a "\" I think I'm done.\""
                a "\" Dad's about to go to bed.\""
                a "\" I'll go kiss him goodnight.\""
                a "\" He likes me to do that when I'm home.\""
                i "\" We'll sit a while longer.\""
                a "\" Alright.\""
                hide 6newalex124
                show 6newalex125
                with dissolve
                " Alexandra leaves."
                hide 6newalex125
                show 6newalex128
                with dissolve
                i "\" So, how do we start over?\""
                p "\" I don't know.\""
                i "\" Maybe...\""
                i "\" When we're free. Both of us.\""
                i "\" Sometime this week.\""
                i "\" Maybe we could go out?\""
                i "\" Just us?\""
                i "\" See where we go from there?\""
                p "\" Alright.\""
                p "\" Let's try.\""
                i "\" I guess we should get changed.\""
                p "\" Right.\""
                hide 6newalex126
                show 6newalex131
                with dissolve
                " You head back in the pool house, and change."
                hide 6newalex131
                show 6newalex135
                with dissolve
                " Then you follow Alex in the main house."
                " Izzy doesn't say a word to you during all this time."
                hide 6newalex135
                show 6newalex136
                with dissolve
                a "\" Hey.\""
                hide 6newalex136
                show 6newalex137
                with dissolve
                i "\" You kissed your Dad goodnight?\""
                a "\" Yeah.\""
                hide 6newalex137
                show 6newalex138
                with dissolve
                a "\" Have to go to sleep.\""
                a "\" I'd invite you to stay puppy...\""
                p "\" Your Dad's house.\""
                p "\" I get it.\""
                a "\" Good night.\""
                p "\" Good night.\""
                jump ep6cont6

label ep6izzypoolizzyin:
                scene 6newalex108
                with dissolve
                i "\" I was just making a remark, actually.\""
                i "\" But he doesn't need your permission to come cuddle me.\""
                show 6newalex109
                with dissolve
                " You go to her and take her in your arms."
                i "\" Mmmm... Nice.\""
                i "\" Actually, it is warming me up.\""
                p "\" In what way?\""
                hide 6newalex109
                show 6newalex110
                with dissolve
                i "\" Puppy...\""
                i "\" I mean... If you want...\""
                hide 6newalex110
                show 6newalex111
                with dissolve
                a "\" Hey!\""
                a "\" I'm glad that you're getting so close.\""
                a "\" But not here.\""
                a "\" Dad could catch you.\""
                hide 6newalex111
                show 6newalex112
                with dissolve
                i "\" What about this morning?\""
                a "\" That was in my bathroom.\""
                a "\" Dad's not gonna come in there.\""
                a "\" But he might come to check on us.\""
                hide 6newalex112
                show 6newalex111
                with dissolve
                i "\" Sorry puppy.\""
                p "\" He he...\""
                hide 6newalex111
                show 6newalex114
                with dissolve
                " The girls start to swim up and down the pool."
                hide 6newalex114
                show 6newalex115
                with dissolve
                " Meanwhile, you sit on the edge of the pool and watch."
                hide 6newalex115
                show 6newalex116
                with dissolve
                " After a few laps..."
                i "\" Whoa...\""
                i "\" Refreshing.\""
                i "\" But I think that's enough.\""
                a "\" I'll swim a while longer.\""
                a "\" Make my ass bonier.\""
                i "\" Come on.\""
                a "\" He he...\""
                hide 6newalex116
                show 6newalex117
                with dissolve
                " While Alex keeps swimming, Izzy comes and sits next to you."
                hide 6newalex117
                show 6newalex122
                with dissolve
                i "\" Pupster?\""
                p "\" Huh?\""
                i "\" Can I tell you something?\""
                hide 6newalex122
                show 6newalex123
                with dissolve
                " She leans on you."
                i "\" It's starting...\""
                p "\" What?\""
                i "\" It's starting to be...\""
                i "\" That I can't have thoughts without you.\""
                p "\" What?\""
                i "\" Sorry. I'm not good at expressing myself.\""
                i "\" It's like... When I plan ahead. When I look at my life ahead...\""
                i "\" I always see you in it.\""
                i "\" Does that make sense?\""
                p "\" I think I understand.\""
                hide 6newalex123
                show 6newalex124
                with dissolve
                a "\" Hey.\""
                a "\" I think I'm done.\""
                a "\" Dad's about to go to bed.\""
                a "\" I'll go kiss him goodnight.\""
                a "\" He likes me to do that when I'm home.\""
                i "\" We'll sit a while longer.\""
                a "\" Alright.\""
                hide 6newalex124
                show 6newalex125
                with dissolve
                " Alexandra leaves."
                hide 6newalex125
                show 6newalex127
                with dissolve
                i "\" We should get going too.\""
                p "\" Yeah.\""
                hide 6newalex127
                show 6newalex128
                with dissolve
                " She turns to you."
                i "\" I was thinking.\""
                i "\" Maybe we could do something. Just the two of us.\""
                p "\" What?\""
                hide 6newalex128
                show 6newalex129
                with dissolve
                i "\" I don't know...\""
                i "\" A date, maybe?\""
                p "\" A date?\""
                i "\" Yeah.\""
                p "\" What kind?\""
                i "\" I don't know.\""
                hide 6newalex129
                show 6newalex130
                with dissolve
                i "\" And maybe...\""
                i "\" At the end of it...\""
                i "\" YOU could make ME shudder for a change.\""
                p "\" I'm in.\""
                i "\" He he he...\""
                i "\" Now we should get going.\""
                hide 6newalex130
                show 6newalex131
                with dissolve
                " You head back in the pool house, to change."
                hide 6newalex131
                show 6newalex132
                with dissolve
                p "\" What kind of dates do you usually go on?\""
                i "\" Haven't been on one since high school.\""
                i "\" And that was at the back of the school, where all the smokers hung out.\""
                p "\" I'll try to do better than that.\""
                hide 6newalex132
                show 6newalex133
                " You both change."
                hide 6newalex133
                show 6newalex134
                with dissolve
                i "\" I'm not high maintenance.\""
                i "\" Anything will do.\""
                p "\" I'll think of something.\""
                hide 6newalex134
                show 6newalex135
                with dissolve
                " Then you follow Alex in the main house."
                hide 6newalex135
                show 6newalex136
                with dissolve
                a "\" Hey.\""
                hide 6newalex136
                show 6newalex137
                with dissolve
                i "\" You kissed your Dad goodnight?\""
                a "\" Yeah.\""
                i "\" Well, me and puppy have a date?\""
                i "\" Just the two of us.\""
                a "\" Just the two of you?\""
                i "\" I want something that's just ours.\""
                a "\" Makes sense.\""
                hide 6newalex137
                show 6newalex138
                with dissolve
                a "\" Have to go to sleep.\""
                a "\" I'd invite you to stay puppy...\""
                p "\" Your Dad's house.\""
                p "\" I get it.\""
                a "\" Good night.\""
                p "\" Good night.\""
                jump ep6cont6

label ep6cont6:
                scene 5newalex118
                with dissolve
                " You head to your room, where you find the pajamas from the day before, and go to sleep."
                show blackscreen
                with dissolve
                "..."
                "... ..."
                "... ... ..."
                hide blackscreen
                show 6newalex139
                with dissolve
                " The next day, the girls are ready for you and Boris to take them to school."
                p "\" My boy's are probably here already.\""
                p "\" But you don't want to go with them.\""
                a "\" No.\""
                p "\" I'll send them to the agency.\""
                a "\" Thank you.\""
                hide 6newalex139
                show 5newalex178
                with dissolve
                " You head outside."
                ja "\" Where do we go?\""
                p "\" You go to the agency.\""
                ja "\" Got it.\""
                p "\" And you know what? Don't come here anymore.\""
                p "\" I'll just meet you there.\""
                ja "\" If you say so.\""
                hide 5newalex178
                show 6newalex140
                with dissolve
                " That's when you notice there's a girl in the back seat."
                hide 6newalex140
                show 6newalex141
                with dissolve
                p "\" Who's that?\""
                ja "\" Just my Sister.\""
                ja "\" She won't be a bother, I promise.\""
                ja "\" I just have to take her to her doctor.\""
                ol "\" Cherubael?\""
                hide 6newalex141
                show 6newalex142
                with dissolve
                " She gets out of the car."
                ol "\" Cherubael.\""
                p "\" What?\""
                ol "\" Are you still running?\""
                hide 6newalex142
                show 6newalex143
                with dissolve
                " James gets out of the car, and puts his arm in front of her."
                hide 6newalex143
                show 6newalex144
                with dissolve
                ja "\" Don't mind her.\""
                ja "\" She's off her meds, literally.\""
                p "\" I see.\""
                hide 6newalex144
                show 6newalex145
                with dissolve
                ol "\" You can spend your lifetime running from the Goddess.\""
                ol "\" But she loves you.\""
                ol "\" She adores you, and all of your kind.\""
                ol "\" And when you shed your mortal coil, you will be hers.\""
                ol "\" A consort of spirit and shadow. Claimed by your true love at last.\""
                p "\" What?\""
                hide 6newalex145
                show 6newalex144
                with dissolve
                ja "\" Like I said.\""
                p "\" Right.\""
                hide 6newalex144
                show 6newalex141
                with dissolve
                " She gets pushed back in the car, and he gets back at the wheel."
                ja "\" So, go to the agency?\""
                p "\" That's your routine from now on.\""
                p "\" Unless I tell you otherwise.\""
                ja "\" Got it.\""
                hide 6newalex141
                show back1
                with dissolve
                show 6newalex39
                with dissolve
                " After they leave, you and Boris take the girls to school."
                hide 6newalex39
                show 6newalex147
                with dissolve
                a "\" So, you're gonna have another Mufasa day, Dad?\""
                b "\" Alexandra...\""
                hide 6newalex147
                show 6newalex148
                a "\" I think it's sweet.\""
                a "\" My boy's.\""
                hide 6newalex148
                show 6newalex149
                with dissolve
                b "\" When did you get so controlling?\""
                b "\" Trying to run other people's lives.\""
                a "\" Got it from you.\""
                b "\" Please.\""
                a "\" Where else do you think?\""
                hide 6newalex149
                show 6newalex150
                with dissolve
                " You drop them off, and are alone with Boris."
                p "\" Where to?\""
                b "\" Back to the health club.\""
                p "\" Will do.\""
                hide 6newalex150
                show 6newalex151
                with dissolve
                " You go to the club."
                p "\" What are we going to do?\""
                b "\" We're gonna see what he says again.\""
                b "\" And if he gets lippy with me.\""
                p "\" You want me to...\""
                b "\" Do nothing but listen.\""
                b "\" When I want you to do something, I'll tell you.\""
                hide 6newalex151
                show 6newalex152
                with dissolve
                " When you get to the sauna, you see George with a young girl."
                gi "\" Come on baby.\""
                gi "\" Do the right thing.\""
                girl3 "\" Sir...\""
                hide 6newalex152
                show 6newalex153
                with dissolve
                gi "\" Be good now.\""
                girl3 "\" Please...\""
                gi "\" You don't want to be a towel girl for the rest of your life.\""
                girl3 "\" Let me go.\""
                hide 6newalex153
                show 6newalex154
                with dissolve
                b "\" Let the girl go Georgie.\""
                gi "\" *Sigh*\""
                gi "\" What are you doing here?\""
                hide 6newalex154
                show 6newalex155
                with dissolve
                " With George distracted the girl gets free, and rushes by you as she exits."
                girl3 "\" Excuse me.\""
                hide 6newalex155
                show 6newalex156
                with dissolve
                gi "\" What do you want?\""
                hide 6newalex156
                show 6newalex157
                with dissolve
                b "\" Just checking in.\""
                gi "\" You did that yesterday.\""
                b "\" And I'm doing it again today.\""
                b "\" Problem?\""
                gi "\" I didn't say it was a problem.\""
                gi "\" Did you get my escort?\""
                hide 6newalex157
                show 6newalex158
                with dissolve
                b "\" We will.\""
                b "\" Now, what about the people we need to lean on.\""
                hide 6newalex158
                show 6newalex159
                with dissolve
                gi "\" I said, I'll tell you on Friday.\""
                b "\" No need to take that tone.\""
                gi "\" Well, it seems that you're hard of hearing.\""
                hide 6newalex159
                show 6newalex160
                with dissolve
                " Boris gets up."
                b "\" Let's go.\""
                gi "\" Where are you going?\""
                hide 6newalex160
                show 6newalex154
                with dissolve
                b "\" To get you your escort.\""
                gi "\" Good.\""
                hide 6newalex154
                show back1
                with dissolve
                show 6newalex150
                with dissolve
                " You get back to the car."
                b "\" Did you hear that?\""
                b "\" His tone?\""
                p "\"...\""
                b "\" He needs to be taught a lesson.\""
                p "\" Isn't he an elected official?\""
                b "\" What did I tell you about the law?\""
                p "\" That the worst part of stepping outside of it, is you lose it's protection?\""
                b "\" Exactly.\""
                b "\" Take me to Bogdan's house?\""
                p "\" Bogdan?\""
                b "\" I think you met him playing poker at my house.\""
                p "\" Right. The one who wants to live forever.\""
                b "\" What?\""
                p "\" Nothing. Just something Alex said.\""
                p "\" I don't know where he lives.\""
                b "\" I'll tell you where to go.\""
                hide 6newalex150
                show 6newalex161
                with dissolve
                " When you get there, you find him in the pool."
                bog "\" Get in here boy.\""
                boy "\" Hmmm...\""
                bog "\" Don't be shy.\""
                boy "\"...\""
                b "\" Get out here, you old goat.\""
                hide 6newalex161
                show 6newalex162
                with dissolve
                bog "\" Boris?\""
                bog "\" What are you doing here?\""
                b "\" Came to see you.\""
                hide 6newalex162
                show 6newalex163
                with dissolve
                bog "\" You can go.\""
                bog "\" We'll resume this later.\""
                boy "\" Alright.\""
                boy "\" Later, uncle Bogdi.\""
                bog "\" There's a good boy.\""
                hide 6newalex163
                show 6newalex164
                with dissolve
                bog "\" Now, what can I do for you?\""
                b "\" Uncle Bogdi?\""
                bog "\" Nephew. Twice removed.\""
                hide 6newalex164
                show 6newalex165
                with dissolve
                b "\" I should hope at least twice.\""
                b "\" You're getting worse with age, you know that?\""
                b "\" Now put some clothes on.\""
                b "\" We need to talk.\""
                hide 6newalex165
                show 6newalex166
                with dissolve
                b "\" We'll wait for you in the living room.\""
                b "\" Jesus Christ.\""
                hide 6newalex166
                show 6newalex167
                with dissolve
                " He gets dressed, and you all meet in the living room."
                hide 6newalex167
                show 6newalex168
                with dissolve
                bog "\" Now, what can I do for you?\""
                hide 6newalex168
                show 6newalex169
                with dissolve
                " Boris sits down."
                b "\" Remember Georgie?\""
                bog "\" Georgie?\""
                b "\" Our friend with the council?\""
                bog "\" That Georgie! Right.\""
                b "\" He needs to be taught a lesson.\""
                hide 6newalex169
                show 6newalex170
                with dissolve
                bog "\" What kind?\""
                b "\" Not the worst kind.\""
                b "\" Just help him remember who he's dealing with.\""
                bog "\" I understand.\""
                hide 6newalex170
                show 6newalex171
                with dissolve
                b "\" [player_name] here will help you out.\""
                bog "\" Alright.\""
                b "\" We've got him to expect an escort from us.\""
                b "\" Maybe use that angle.\""
                hide 6newalex171
                show 6newalex170
                with dissolve
                bog "\" Doesn't your boy here have a whole bunch of those?\""
                hide 6newalex170
                show 6newalex173
                with dissolve
                b "\" That's right.\""
                b "\" And he's more than willing to help out.\""
                hide 6newalex173
                show 6newalex172
                with dissolve
                bog "\" The dream team, eh?\""
                hide 6newalex172
                show 6newalex174
                with dissolve
                bog "\" Let's go.\""
                bog "\" We're burning sunlight and I want to be back here by 10.\""
                p "\" Why?\""
                bog "\" My telenovella starts then.\""
                hide 6newalex174
                show 6newalex175
                with dissolve
                b "\" Go with him.\""
                b "\" Do as he says.\""
                b "\" I'll have Dima drive me the rest of the day.\""
                hide 6newalex175
                show back1
                with dissolve
                show 6newalex176
                with dissolve
                " You go with Bogdan."
                p "\" What are we doing?\""
                hide 6newalex176
                show 6newalex177
                with dissolve
                bog "\" First we'll go see these girls of yours.\""
                bog "\" See which one we can use.\""
                p "\" Alright.\""
                hide 6newalex177
                show 6newalex178
                with dissolve
                " You go to the agency."
                hide 6newalex178
                show 6newalex179
                with dissolve
                cl "\" You're here today?\""
                p "\" For now?\""
                cl "\" Need anything?\""
                p "\" Not really.\""
                p "\" How are the boys settling in?\""
                cl "\" Fine.\""
                cl "\" Yuri has been keeping them out of our hair."
                p "\" Good.\""
                hide 6newalex179
                show 6newalex182
                with dissolve
                bog "\" She doesn't like you much, does she?\""
                p "\" What?\""
                p "\" She likes me fine.\""
                bog "\" Really?\""
                hide 6newalex182
                show 6newalex181
                with dissolve
                bog "\" Darling, what's your name?\""
                cl "\" Clara.\""
                bog "\" Well, Clara. Do you like [player_name] here?\""
                bog "\" I mean as a boss. Coworker.\""
                cl "\" He is the boss.\""
                hide 6newalex181
                show 6newalex182
                with dissolve
                bog "\" That's the biggest non answer I ever heard.\""
                bog "\" He he...\""
                p "\" What's your point.\""
                hide 6newalex182
                show 6newalex180
                with dissolve
                bog "\" My point is that we need someone we can trust.\""
                bog "\" Is there anyone here that you can say that about?\""
                p "\" I don't know.\""
                bog "\" No one you trust even a little.\""
                p "\" Narysa, maybe.\""
                bog "\" Could you go get her?\""
                hide 6newalex180
                show 6newalex183
                with dissolve
                " You go get Narysa."
                nar "\" What's this about?\""
                nar "\" What can I do for you?\""
                hide 6newalex183
                show 6newalex180
                with dissolve
                bog "\" Pretty girl.\""
                bog "\" I think she'll do just fine.\""
                bog "\" But can we talk to her somewhere more private?\""
                bog "\" Your place, maybe.\""
                hide 6newalex180
                show 6newalex183
                with dissolve
                p "\" Can you come with us please?\""
                p "\" We have a proposition for you.\""
                nar "\" I suppose.\""
                hide 6newalex183
                show 6newalex184
                with dissolve
                " You take them to your place."
                nar "\" Yes?\""
                bog "\" We wanted to talk with you in private.\""
                bog "\" [player_name] here, says he trusts you.\""
                bog "\" My dear, I'll be blunt with you.\""
                bog "\" We're in need of an escort.\""
                hide 6newalex184
                show 6newalex1
                with dissolve
                nar "\" I see.\""
                nar "\" But I'm afraid I don't do that anymore.\""
                bog "\" Ahhh...\""
                bog "\" Anymore.\""
                nar "\" Yes.\""
                hide 6newalex1
                show 6newalex188
                with dissolve
                bog "\" But what if we told you that you wouldn't have to have sex with anyone.\""
                hide 6newalex188
                show 6newalex189
                with dissolve
                nar "\" I'd say that you have a strange idea of what an escort is.\""
                hide 6newalex189
                show 6newalex188
                with dissolve
                bog "\" I'll put my cards on the table.\""
                bog "\" There's this man that needs to be taught a lesson.\""
                nar "\" Taught a lesson?\""
                bog "\" But we need to get him alone. In a private place.\""
                hide 6newalex188
                show 6newalex185
                with dissolve
                nar "\" What kind of lesson?\""
                nar "\" Are you going to hurt him?\""
                bog "\" Mostly his pride.\""
                hide 6newalex185
                show 6newalex188
                with dissolve
                bog "\" Don't worry.\""
                bog "\" And we'll see that you're well rewarded.\""
                hide 6newalex188
                show 6newalex185
                with dissolve
                nar "\" And what would I have to do?\""
                bog "\" Just pose as an escort and go with him to his room.\""
                nar "\" And then?\""
                bog "\" Then, nothing.\""
                bog "\" I'll take it from there.\""
                nar "\" I won't have to fuck him?\""
                bog "\" No.\""
                hide 6newalex185
                show 6newalex187
                with dissolve
                nar "\" I'll do it.\""
                p "\" Are you sure?\""
                nar "\" But I want a piece of the agency.\""
                bog "\" A percentage?\""
                hide 6newalex187
                show 6newalex186
                with dissolve
                bog "\" Well.\""
                bog "\" That's your call, [player_name].\""
                hide 6newalex186
                show 6newalex187
                with dissolve
                nar "\" I won't stay young forever.\""
                nar "\" And I have little in the way of job security.\""
                p "\" Hmmm...\""
                p "\" How big a piece.\""
                nar "\" I'm not stupid. Two percent.\""
                p "\" I could do that.\""
                hide 6newalex187
                show 6newalex190
                with dissolve
                bog "\" It's settled, then.\""
                bog "\" You help the girl get ready and wait for me to call.\""
                p "\" Where are you going?\""
                bog "\" To find a good hotel.\""
                bog "\" I'll call when I'm ready.\""
                hide 6newalex190
                show 6newalex1
                with dissolve
                " He leaves, and you and Narysa are alone."
                nar "\" I'll need a change of clothes.\""
                nar "\" I have plenty at my place.\""
                p "\" Alright.\""
                hide 6newalex1
                show back1
                with dissolve
                show 6newalex191
                with dissolve
                " You drive to Narysa's place."
                p "\" Are you sure you want to do this?\""
                nar "\" No, but I will.\""
                nar "\" Can't let this pass me by.\""
                nar "\" As a chance, I mean.\""
                p "\" You can't?\""
                hide 6newalex191
                show 6newalex192
                with dissolve
                nar "\" I won't be pretty forever.\""
                nar "\" And my resume consists of convincing girls to experiment with the world's oldest profession.\""
                p "\" I see.\""
                nar "\" Yeah.\""
                hide 6newalex192
                show 6newalex193
                with dissolve
                " You arrive at her place."
                nar "\" Make yourself comfortable.\""
                nar "\" I'll just be a minute.\""
                p "\" Take your time.\""
                hide 6newalex193
                show 6newalex194
                with dissolve
                " She leaves you alone while she goes and changes."
                p "\" Hmm...\""
                p "\" She said being an escort paid for apartment.\""
                " You can't help but compare it to yours."
                p "\" Guess lovin' pays better than fightin'.\""
                hide 6newalex194
                show 6newalex195
                with dissolve
                " She comes back a few minutes later."
                p "\" Jeans and a shirt?\""
                nar "\" What were you expecting?\""
                p "\" I don't know.\""
                p "\" Something that barely clings to you?\""
                hide 6newalex195
                show 6newalex196
                with dissolve
                nar "\" I used to be an escort, darling. Not a hooker.\""
                nar "\" Trust me, I know what I'm doing.\""
                nar "\" Men with money, don't want a hooker.\""
                nar "\" They want the college girl that they saw on the street one day.\""
                nar "\" In a way. They like to think that you're making an exception to your usually strict sexual morality.\""
                nar "\" An exception for them.\""
                p "\" Aha.\""
                " Do you want to give her one last chance to back out?"
                call screen screen38

label ep7narysano:
                scene 6newalex196
                with dissolve
                " You sit there waiting for Bogdan to call."
                show 6newalex197
                with dissolve
                nar "\" So do we just sit here and wait?\""
                p "\" Pretty much.\""
                nar "\" Alright.\""
                hide 6newalex197
                show 6newalex196
                with dissolve
                " The minutes pass slowly as you wait for the call."
                hide 6newalex196
                show 6newalex203
                with dissolve
                " But eventually it does."
                bog "\" Ready?\""
                p "\" Yes.\""
                p "\" You?\""
                bog "\" Come to the Hotel Ambassador.\""
                p "\" Alright.\""
                hide 6newalex203
                show 6newalex205
                with dissolve
                nar "\" That was him?\""
                p "\" Yeah.\""
                p "\" We're going to the Hotel Ambassador.\""
                nar "\" I know it.\""
                nar "\" Nice place.\""
                jump ep6cont7

label ep7narysayes:
                $ narysastart = True
                scene 6newalex196
                with dissolve
                p "\" Narysa.\""
                nar "\" Yes?\""
                show 6newalex197
                with dissolve
                p "\" There's still time for you to back out.\""
                p "\" It's not like this guy's the president or anything.\""
                p "\" We can get at him some other way.\""
                hide 6newalex197
                show 6newalex198
                with dissolve
                nar "\" Trying to not give me my two percent?\""
                p "\" You're doing me an injustice.\""
                hide 6newalex198
                show 6newalex199
                with dissolve
                nar "\" I know.\""
                nar "\" And I'm resolved about this.\""
                p "\" Alright.\""
                hide 6newalex199
                show 6newalex200
                with dissolve
                nar "\" Tell me.\""
                nar "\" How did such a sweet guy like you end up being a thug for gangsters.\""
                p "\" How did you end up an escort?\""
                p "\" And then an escort recruiter.\""
                nar "\" Touche.\""
                hide 6newalex200
                show 6newalex201
                with dissolve
                " She comes and leans against you while you wait."
                hide 6newalex201
                show 6newalex202
                with dissolve
                nar "\" About the escort thing.\""
                nar "\" It's not so terrible.\""
                nar "\" Better people have done worse.\""
                nar "\" And lived through worse.\""
                p "\" I guess it's the same with being a thug.\""
                hide 6newalex202
                show 6newalex204
                with dissolve
                " She nods off against your chest as you wait."
                " Her warm breath heating up the front of your sweater."
                hide 6newalex204
                show 6newalex203
                with dissolve
                " And eventually the call comes."
                bog "\" Ready?\""
                p "\" Yes.\""
                p "\" You?\""
                bog "\" Come to the Hotel Ambassador.\""
                p "\" Alright.\""
                hide 6newalex203
                show 6newalex202
                with dissolve
                nar "\" That was him?\""
                p "\" Yeah.\""
                p "\" We're going to the Hotel Ambassador.\""
                nar "\" I know it.\""
                nar "\" Nice place.\""
                jump ep6cont7

label ep6cont7:
                scene 6newalex206
                with dissolve
                " You make your way to the hotel."
                show 6newalex207
                with dissolve
                mi "\" Can I help you?\""
                p "\" What?\""
                mi "\" What a lovely couple you two are.\""
                p "\" Micha? What are we doing here?\""
                hide 6newalex207
                show 6newalex208
                with dissolve
                mi "\" We've taken over the hotel.\""
                p "\" Really?\""
                mi "\" Just for today.\""
                mi "\" Rented it all.\""
                p "\" That's a lot of cash to spend.\""
                mi "\" Maybe.\""
                mi "\" But we don't want any mistakes.\""
                mi "\" The old man is waiting for you upstairs.\""
                " And he gives you a room key.\""
                hide 6newalex208
                show 6newalex209
                with dissolve
                nar "\" Better than I remember.\""
                nar "\" Must've did some renovations since I was last here.\""
                p "\" Let's go.\""
                hide 6newalex209
                show 6newalex210
                with dissolve
                " You go upstairs."
                hide 6newalex210
                show 6newalex211
                with dissolve
                bog "\" There you are.\""
                bog "\" Wanted you to get a look at the room.\""
                hide 6newalex211
                show 6newalex212
                with dissolve
                nar "\" Just to be clear on what I have to do...\""
                bog "\" Pretty simple.\""
                hide 6newalex212
                show 6newalex211
                with dissolve
                bog "\" You and my friend here will go and pick this guy up.\""
                bog "\" You'll be the escort that [player_name] brings to him.\""
                bog "\" You get him back here, and make him comfortable.\""
                hide 6newalex211
                show 6newalex212
                with dissolve
                nar "\" How comfortable.\""
                bog "\" Just take his clothes off.\""
                bog "\" Nothing else.\""
                hide 6newalex212
                show 6newalex211
                with dissolve
                bog "\" And that's all you have to do.\""
                bog "\" We'll take it from there.\""
                hide 6newalex211
                show 6newalex212
                with dissolve
                nar "\" Alright then.\""
                nar "\" Ready when you are.\""
                p "\" Let's go.\""
                hide 6newalex212
                show back1
                with dissolve
                show 6newalex213
                with dissolve
                " You drive to the health club."
                hide 6newalex213
                show 6newalex214
                with dissolve
                nar "\" Health nut, this guy?\""
                p "\" Not exactly.\""
                p "\" He'll be in the sauna.\""
                hide 6newalex214
                show 6newalex215
                with dissolve
                " You go to the sauna."
                gi "\" Boris' boy.\""
                gi "\" What are you doing back here?\""
                p "\" Keeping our promise.\""
                hide 6newalex215
                show 6newalex216
                with dissolve
                nar "\" Hello.\""
                gi "\" Ohhh...\""
                nar "\" You must be the stud I've been hearing about.\""
                hide 6newalex216
                show 6newalex217
                with dissolve
                gi "\" Stud, eh?\""
                gi "\" What's your name?\""
                nar "\" Electra.\""
                gi "\" Come closer, Electra.\""
                hide 6newalex217
                show 6newalex218
                with dissolve
                " He tries to kiss her, but she shies away."
                gi "\" That's not very friendly of you, Electra.\""
                nar "\" Not here.\""
                gi "\" Why not?\""
                gi "\" The boy there, can watch if you want.\""
                nar "\" No.\""
                hide 6newalex218
                show 6newalex219
                with dissolve
                " She grabs him by the balls."
                nar "\" But if you come to my place of refuge...\""
                hide 6newalex219
                show 6newalex220
                with dissolve
                gi "\" What's wrong with here?\""
                nar "\" Not that kind of girl.\""
                nar "\" I don't do this for a living.\""
                gi "\" What do you do for a living?\""
                nar "\" Nothing. I'm just a student.\""
                gi "\" A little old for that, no?\""
                nar "\" Made some bad choices. Now I have to catch up.\""
                gi "\" I see.\""
                nar "\" And I only take a few clients.\""
                nar "\" Just to help out.\""
                hide 6newalex220
                show 6newalex221
                with dissolve
                gi "\" Alright.\""
                gi "\" Where is this place.\""
                nar "\" Hotel Ambassador.\""
                gi "\" Not your place?\""
                nar "\" I live with my parents.\""
                gi "\" Ahhh...\""
                gi "\" Alright.\""
                p "\" We'll wait for you in the car.\""
                gi "\" I'll just be a minute.\""
                hide 6newalex221
                show back
                with dissolve
                show 6newalex222
                with dissolve
                " You head to the car and wait for George."
                p "\" Living with your parents 'Electra'?\""
                nar "\" It adds to the girl next door vibe.\""
                p "\" You ok?\""
                nar "\" Yeah.\""
                nar "\" I'd like to tell you that hes the worst I've ever seen but that wouldn't be true.\""
                hide 6newalex222
                show 6newalex223
                with dissolve
                nar "\" I'm not an innocent [player_name].\""
                nar "\" I've seen and done worse than him.\""
                hide 6newalex223
                show 6newalex265
                with dissolve
                " After a few minutes, George joins you."
                gi "\" What are you doing in front, Electra?\""
                gi "\" Get back here.\""
                hide 6newalex265
                show 6newalex222
                with dissolve
                nar "\" Excuse me.\""
                hide 6newalex222
                show 6newalex224
                with dissolve
                " She gets in the back seat, and he gropes her all the way to the hotel."
                hide 6newalex224
                show 6newalex225
                with dissolve
                nar "\" Let me just get my room key.\""
                nar "\" Will only be a minute.\""
                gi "\" The boy won't be coming up will he?\""
                gi "\" Or do you like him to watch.\""
                nar "\" It will just be the two of us.\""
                gi "\" Good.\""
                hide 6newalex225
                show 6newalex226
                with dissolve
                nar "\" May I have my key, please?\""
                nar "\" The Electra suite.\""
                mi "\" Of course, Miss.\""
                hide 6newalex226
                show 6newalex227
                with dissolve
                " They go upstairs."
                hide 6newalex227
                show 6newalex228
                with dissolve
                mi "\" Putting silk on a pig, eh?\""
                p "\" What?\""
                mi "\" Her and him?\""
                p "\" Pretty much.\""
                hide 6newalex228
                show 6newalex229
                with dissolve
                p "\" What do we do now?\""
                mi "\" We wait.\""
                mi "\" We wait for Bogdan to call.\""
                p "\" And when he does?\""
                mi "\" When he does, we barge in and take care of business.\""
                " The minutes seem like hours as you wait."
                hide 6newalex229
                show 6newalex230
                with dissolve
                mi "\" There it is.\""
                mi "\" That's Bogdan.\""
                mi "\" Let's go.\""
                hide 6newalex230
                show 6newalex231
                with dissolve
                " You rush upstairs, and burst through the door."
                nar "\" I said, no.\""
                gi "\" What's the difference.\""
                nar "\" I said, get a condom.\""
                gi "\" Are you saying that I'm sick?\""
                gi "\" Now you're starting to upset me.\""
                hide 6newalex231
                show 6newalex232
                with dissolve
                " He raises his head as you burst through the door."
                gi "\" The fuck you doing?\""
                hide 6newalex232
                show 6newalex233
                with dissolve
                mi "\" He he he...\""
                mi "\" I'll let you guess.\""
                hide 6newalex233
                show 6newalex234
                with dissolve
                " And with that Micha's on him."
                " Kicking and punching as Narysa scurries away."
                gi "\" Agha... Agh...\""
                mi "\" There you go.\""
                mi "\" He he he...\""
                mi "\" There you go.\""
                hide 6newalex234
                show 6newalex235
                with dissolve
                " Narysa hides behind you."
                p "\" You ok?\""
                nar "\" I guess.\""
                p "\" He didn't...\""
                nar "\" No.\""
                hide 6newalex235
                show 6newalex236
                with dissolve
                " Micha keeps gleefully hitting George."
                mi "\" He he he...\""
                mi "\" Have some leather instead of silk.\""
                gi "\" Agh... Agh... Agh...\""
                mi "\" He he he...\""
                hide 6newalex236
                show 6newalex237
                with dissolve
                nar "\" Your friend...\""
                nar "\" He ain't right.\""
                p "\" No, no he's not.\""
                hide 6newalex237
                show 6newalex238
                with dissolve
                bog "\" That's enough, Micha.\""
                bog "\" Don't want to kill him.\""
                bog "\" At least not yet.\""
                hide 6newalex238
                show 6newalex239
                with dissolve
                gi "\" *Cough* *Cough* *Cough*\""
                gi "\" You cunts!\""
                gi "\" Do you know who I am?\""
                bog "\" We know exactly who you are.\""
                gi "\" I'll have you all in prison by the end of the day.\""
                hide 6newalex239
                show 6newalex240
                with dissolve
                bog "\" For what?\""
                bog "\" For saving this girl from being raped?\""
                bog "\" Fortunately for her, these two young men heard her screams for help and burst in your room.\""
                bog "\" Where they found you trying to force yourself on her.\""
                hide 6newalex240
                show 6newalex241
                with dissolve
                bog "\" And me also.\""
                bog "\" A kindly old man.\""
                hide 6newalex241
                show 6newalex240
                with dissolve
                gi "\" Who's going to believe that shit?\""
                bog "\" Who knows...\""
                bog "\" It is four against one.\""
                bog "\" Not that it really matters.\""
                bog "\" If we go to prison, your dealings with Boris will ensure that you're coming with us.\""
                hide 6newalex240
                show 6newalex241
                with dissolve
                bog "\" Who do you think will fare better in there?\""
                bog "\" Us? Or you?\""
                gi "\"...\""
                bog "\" Exactly.\""
                bog "\" Now you and I will have a talk.\""
                bog "\" Well, I will talk and you will listen.\""
                bog "\" Just let me see off our young friends.\""
                hide 6newalex241
                show 6newalex242
                with dissolve
                bog "\" Are you ok my dear?\""
                hide 6newalex242
                show 6newalex237
                with dissolve
                nar "\" Yeah.\""
                bog "\" Good.\""
                hide 6newalex237
                show 6newalex242
                with dissolve
                bog "\" Get dressed, darling.\""
                hide 6newalex242
                show 6newalex243
                with dissolve
                " She clambers for her clothes."
                hide 6newalex243
                show 6newalex244
                with dissolve
                bog "\" Take her home, and make sure she's ok.\""
                bog "\" Me and Micha will handle it from here.\""
                hide 6newalex244
                show back1
                with dissolve
                show 6newalex222
                with dissolve
                " You get back to the car, and she seems that shes about to cry."
                p "\" You ok?\""
                nar "\" Yes.\""
                p "\" Are you sure?\""
                hide 6newalex222
                show 6newalex245
                with dissolve
                nar "\" I SAID I'M FUCKING FINE!\" she screams."
                p "\" Easy.\""
                hide 6newalex245
                show 6newalex222
                with dissolve
                nar "\" Sorry.\""
                nar "\" Could you just take me home, please?\""
                p "\" Yeah.\""
                hide 6newalex222
                show 6newalex246
                with dissolve
                " You drive her home."
                hide 6newalex246
                show 6newalex247
                with dissolve
                nar "\" Just be sure you get me what we agreed on, ok?\""
                p "\" Your two percent?\""
                nar "\" That's right.\""
                " Do you want to try and hug her before you leave?\""
                call screen screen39

label ep7narysahugno:
                scene 6newalex247
                with dissolve
                p "\" I'll be going now.\""
                nar "\" You do that.\""
                jump ep6cont8

label ep7narysahugyes:
                $ narysastart = True
                scene 6newalex248
                with dissolve
                " You try to hug her."
                nar "\" What are you doing?\""
                p "\" It's ok.\""
                p "\" Just...just calm down.\""
                show 6newalex249
                with dissolve
                " Once she realizes what you were doing, she hugs you back."
                nar "\" Thanks.\""
                hide 6newalex249
                show 6newalex250
                nar "\" Maybe I did get a little triggered.\""
                nar "\" Thought I had left all that behind, you know.\""
                p "\" Sorry.\""
                nar "\" Don't be.\""
                nar "\" But you should get going now.\""
                p "\" Right.\""
                jump ep6cont8

label ep6cont8:
                scene 6newalex251
                with dissolve
                " It's well into the night by the time you get back to the villa."
                show 6newalex252
                with dissolve
                " The guards let you through without complaint."
                " Seems Boris has told them you're one of the household now."
                hide 6newalex252
                show 6newalex253
                with dissolve
                " And you find him still awake in the kitchen."
                b "\" How did it go?\""
                p "\" I don't know.\""
                p "\" Never done anything like that before.\""
                hide 6newalex253
                show 6newalex254
                with dissolve
                b "\" Well, Bogdan praised you.\""
                b "\" Doesn't do that often.\""
                p "\" Thanks.\""
                b "\" Don't get too cocky.\""
                b "\" He mosly said he liked your ass.\""
                p "\" Ugh...\""
                b "\" He he he...\""
                b "\" Well, you did good.\""
                b "\" Go to sleep.\""
                p "\" See you tomorrow.\""
                b "\" Tomorrow.\""
                hide 6newalex254
                show 6newalex255
                with dissolve
                " You head up to your room, and there's Alexandra sleeping in your bed."
                p "\" Ohh...\""
                hide 6newalex255
                show 6newalex256
                with dissolve
                " You come a little bit closer."
                p "\" Alex?\""
                a "\" Ah?\""
                a "\" There you are.\""
                hide 6newalex256
                show 6newalex257
                with dissolve
                " She wakes and turns on the lights."
                p "\" What are you doing here?\""
                a "\" Well, Dad came to pick us up instead of you.\""
                a "\" Said you wouldn't be back till late.\""
                p "\" That's true.\""
                hide 6newalex257
                show 6newalex258
                with dissolve
                a "\" Wanted to see if you were ok?\""
                a "\" Well, are you?\""
                p "\" As you see me.\""
                a "\" Good.\""
                hide 6newalex258
                show 6newalex259
                with dissolve
                " You lean down to kiss her, and she responds eagerly."
                hide 6newalex259
                show 6newalex260
                with dissolve
                a "\" Well, get changed.\""
                a "\" Time for bed.\""
                a "\" Pjamas are on the chair.\""
                hide 6newalex260
                show 6newalex261
                with dissolve
                " You start to change your clothes."
                p "\" Are you just going to sit there watching me?\""
                a "\" Yup.\""
                p "\" Why?\""
                a "\" Because I want to.\""
                hide 6newalex261
                show 6newalex262
                with dissolve
                a "\" Hey, I'm allowed to look at you.\""
                hide 6newalex262
                show 6newalex263
                with dissolve
                " You put on the pijamas."
                p "\" Well, good night.\""
                a "\".....\""
                p "\" You're not leaving.\""
                a "\" I'm not.\""
                p "\" Staying here for the night?\""
                a "\" Yeah.\""
                p "\" What about your Dad?\""
                a "\" What is he going to do? Kill me?\""
                p "\" What about Izzy?\""
                a "\" She's sound asleep already.\""
                a "\" Whatever Dad had you doing tonight, I don't want you to sleep alone.\""
                p "\" I see.\""
                a "\" But it will just be sleeping.\""
                p "\" Never doubted it.\""
                a "\" Now, come on.\""
                hide 6newalex263
                show 6newalex264
                with dissolve
                " You turn off the lights and she curls in your arms."
                a "\" Was it bad?\""
                p "\" What?\""
                a "\" What you were doing.\""
                p "\" It depends on how you look at it.\""
                a "\" Sigh...\""
                a "\" Good night.\""
                p "\" Good night.\""
                jump ep7



                
