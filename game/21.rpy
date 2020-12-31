label ep21:
                scene 20newalex237
                with dissolve
                p "\" I fail to see how this is good.\""
                p "\" What if he opens...\""
                a "\" He won't!\""
                show 21newalex1
                with dissolve
                a "\" Are you ok, bubu?\""
                a "\" You seem out of sorts.\""
                i "\" Well, a man just walked in on me naked.\""
                a "\" He he...\""
                a "\" Besides that?\""
                with dissolve
                if izzyin == True:
                    i "\" Isn't that enough?\""
                    i "\" He might tell on us.\""
                    jump ep21cont1
                    
                else:
                    i "\" Just that.\""
                    i "\" He might get the wrong idea.\""
                    jump ep21cont1
                    
label ep21cont1:
                scene 21newalex2
                with dissolve
                " Alex looks at you."
                a "\" Well, if it comes to that.\""
                p "\" I'll take care of it?\""
                a "\" Exactly.\""
                show 21newalex3
                with dissolve
                " You and the girls get dressed."
                p "\" No bikini's?\""
                p "\" Aren't you a little dressed up?\""
                hide 21newalex3
                show 21newalex214
                with dissolve
                a "\" If we're staying here, we are.\""
                a "\" But I'll want you to drive us to the hospital.\""
                i "\" Hospital?\""
                i "\" Why?\""
                hide 21newalex214
                show 21newalex3
                with dissolve
                a "\" You'll see, sweetie.\""
                p "\" What about Bogdan and Vadim?\""
                hide 21newalex3
                show 21newalex215
                with dissolve
                a "\" They'll stay here.\""
                a "\" Don't worry.\""
                hide 21newalex215
                show 21newalex4
                with dissolve
                " You leave Alex's bedroom and find Bogdan in a robe, wandering the halls."
                hide 21newalex4
                show 21newalex5
                with dissolve
                a "\" Morning!\" Alex exclaims, cheerfully."
                hide 21newalex5
                show 21newalex4
                with dissolve
                bog "\" Morning, darlings.\""
                hide 21newalex4
                show 21newalex6
                with dissolve
                bog "\" What's for breakfast?\""
                bog "\" I'm starving.\""
                " He seems to have settled down."
                " Doesn't seem to want to leave, or at least is resigned to staying at the villa."
                " And is even wearing one of what must be Boris's robes around."
                hide 21newalex6
                show 21newalex8
                with dissolve
                " Vadim walks in, still in his bathing suit."
                hide 21newalex8
                show 21newalex7
                with dissolve
                " With Alex giving him a baleful look."
                if vadimrespect == True:
                    hide 21newalex7
                    show 21newalex8
                    with dissolve
                    " But he doesn't seem to mind, and just keeps walking along."
                    hide 21newalex8
                    show 21newalex9
                    with dissolve
                    " Giving you a small wink, as he passes by."
                    jump ep21cont2
                    
                else:
                    hide 21newalex7
                    show 21newalex8
                    with dissolve
                    " But he doesn't seem to mind, and just keeps walking along."
                    jump ep21cont2
                
label ep21cont2:
                scene 21newalex10
                with dissolve
                a "\" I'll have to ask you to cook for yourself this morning, uncle.\""
                a "\" Me and Izzy have to go away for a bit this morning.\""
                bog "\" He he...\""
                bog "\" I like it when you call me uncle.\""
                bog "\" Wait! You're leaving?\""
                a "\" Just for a bit.\""
                show 21newalex11
                with dissolve
                a "\" We have some documents to sign at school.\""
                a "\" [player_name] will drive us.\""
                a "\" We'll be right back.\""
                p "\" Right.\""
                bog "\" Documents? What documents?\""
                hide 21newalex11
                show 21newalex12
                with dissolve
                i "\" Ahhh...\""
                " She's at a loss for words."
                hide 21newalex12
                show 21newalex10
                with dissolve
                a "\" I don't know.\""
                a "\" Just some bullshit.\""
                a "\" We'll be right back, though.\""
                a "\" And I can't wait to have another little party.\""
                bog "\" Normally, I'd say I'm too old to party.\""
                p "\" I wouldn't say that.\""
                hide 21newalex10
                show 21newalex216
                with dissolve
                bog "\" He he...\""
                hide 21newalex216
                show 21newalex10
                with dissolve
                bog "\" But you caught me in a good mood.\""
                hide 21newalex10
                show 21newalex31
                with dissolve
                a "\" Let's go, babe.\""
                hide 21newalex31
                show 21newalex32
                with dissolve
                i "\" Yeah.\""
                hide 21newalex32
                show back1
                with dissolve
                show 21newalex33
                with dissolve
                " You bundle the girls in the car and go head over to the hospital."
                a "\" You think he slept ok?\""
                p "\" Why wouldn't he?\""
                a "\" You know how he is.\""
                hide 21newalex33
                show 21newalex34
                with dissolve
                i "\" This is starting to get annoying.\""
                a "\" My dad is in the hospital, Izzy.\""
                i "\" Mr. Boris?\""
                a "\" Yeah.\""
                hide 21newalex34
                show 21newalex217
                with dissolve
                i "\" What happened?\""
                p "\" He got sick.\""
                a "\" Now he's had an operation.\""
                i "\" And all the secrecy...\""
                hide 21newalex217
                show 21newalex35
                with dissolve
                a "\" You know who my dad is, right.\""
                a "\" We have to keep this under our hats.\""
                hide 21newalex35
                show 21newalex34
                with dissolve
                i "\" Yeah.\""
                hide 21newalex34
                show 21newalex70
                with dissolve
                i "\" Is he ok?\""
                p "\" Yeah.\""
                a "\" He's had his operation.\""
                i "\" And he's all good now, yes.\""
                hide 21newalex70
                show 21newalex35
                with dissolve
                a "\" Not exactly.\""
                a "\" But he's better.\""
                hide 21newalex35
                show 21newalex36
                with dissolve
                " You get to the hospital."
                hide 21newalex36
                show 21newalex37
                with dissolve
                a "\" Heh.\""
                a "\" I should actually pay Yuri a visit too.\""
                a "\" It's my fault he's in here.\""
                p "\" I'll do it.\""
                p "\" I think it more my fault than yours.\""
                a "\" He he...\""
                a "\" Poor Yuri.\""
                p "\" Let's go see Boris first.\""
                hide 21newalex37
                show 21newalex38
                with dissolve
                " You go to Boris's room."
                i "\" Oh My God!\""
                a "\" What?\""
                i "\" Sorry.\""
                i "\" I didn't mean that.\""
                i "\" It's just... Strange...\""
                hide 21newalex38
                show 21newalex39
                with dissolve
                i "\" Strange to see him like this.\""
                i "\" He always seemed...\""
                i "\" Like the mountains, you know?\""
                a "\" Eternal?\""
                i "\" Immovable.\""
                hide 21newalex39
                show 21newalex40
                with dissolve
                a "\" I know.\""
                a "\" Dad?\""
                a "\" Dad, are you awake?\""
                hide 21newalex40
                show 21newalex73
                with dissolve
                b "\" Mmmm...\""
                a "\" Dad?!\""
                hide 21newalex73
                show 21newalex41
                with dissolve
                b "\" Whoa!!!\""
                " He wakes up panting, and tries to stand up."
                hide 21newalex41
                show 21newalex42
                with dissolve
                a "\" No, no, it's just me.\""
                b "\" *Pant* *Pant* *Pant*\""
                a "\" Lie back down, daddy.\""
                a "\" It's just us.\""
                hide 21newalex42
                show 21newalex43
                with dissolve
                i "\" Mr. Boris?\""
                b "\" Gafsdgshbwrnh...\""
                i "\" Mr. Boris?\""
                i "\" What's wrong?\""
                hide 21newalex43
                show 21newalex42
                with dissolve
                a "\" He can't speak.\""
                i "\" What?\""
                a "\" It's just...\""
                hide 21newalex42
                show 21newalex44
                with dissolve
                a "\" It's ok, daddy.\""
                a "\" It's ok.\""
                a "\" I'm here.\""
                i "\" We're here, sir.\""
                b "\" Gafsdgshbwrnh...Bad...Agsgdgherh.....\""
                b "\"...Dream...\""
                hide 21newalex44
                show 21newalex45
                with dissolve
                a "\" Did you...\""
                a "\" I think I understood that.\""
                p "\" I heard it too.\""
                i "\" Yes.\""
                hide 21newalex45
                show 21newalex48
                with dissolve
                a "\" Like 'bad dream', right?\""
                p "\" Something like that.\""
                hide 21newalex48
                show 21newalex46
                with dissolve
                b "\"...Adasfgsagfa...Monster...Asdagrhgrh...\""
                b "\" Gbdfbdfhr...Red...Vshdthrhr...\""
                hide 21newalex46
                show 21newalex45
                with dissolve
                a "\" Don't strain yourself.\""
                a "\" Rest.\""
                a "\" He he...\""
                a "\" It's coming back to you.\""
                hide 21newalex45
                show 21newalex48
                with dissolve
                a "\" What do you know?\""
                a "\" Both my men have nightmares.\""
                hide 21newalex48
                show 21newalex47
                with dissolve
                " Boris looks at you."
                " You shrug."
                hide 21newalex47
                show 21newalex49
                with dissolve
                i "\" Calm down, sir.\""
                i "\" Everything is ok.\""
                i "\" Can we get you anything?\""
                i "\" Thirsty?\""
                i "\" Hungry?\""
                hide 21newalex49
                show 21newalex45
                with dissolve
                a "\" Hungry, daddy?\""
                b "\" Uadgsbr...\""
                a "\" Right, sorry.\""
                a "\" You can't really speak yet.\""
                a "\" I'm sure the nurses will bring you food when you need it.\""
                hide 21newalex45
                show 21newalex50
                with dissolve
                " The girls sit down and start chatting with Boris."
                " It is a one way conversation, though."
                hide 21newalex50
                show 21newalex51
                with dissolve
                dk "\" Miss?\""
                a "\" Hey, doc.\""
                dk "\" Visiting hours are not here yet.\""
                p "\" We showed ourselves in.\""
                hide 21newalex51
                show 21newalex52
                with dissolve
                a "\" He spoke.\""
                a "\" Earlier, I mean.\""
                a "\" I understood a few words.\""
                hide 21newalex52
                show 21newalex51
                with dissolve
                dk "\" That's good to hear.\""
                dk "\" He's healing.\""
                hide 21newalex51
                show 21newalex52
                with dissolve
                a "\" I have a few questions.\""
                dk "\" I'm sure you do.\""
                hide 21newalex52
                show 21newalex53
                with dissolve
                p "\" This medical stuff is all Greek to me.\""
                p "\" I'll go check on Yuri.\""
                a "\" Give him a kiss from me.\""
                p "\" Heh.\""
                p "\" I'll just tell him you said that.\""
                hide 21newalex53
                show 21newalex54
                with dissolve
                " You go to Yuri's room, and find him pacing."
                p "\" Hey.\""
                hide 21newalex54
                show 21newalex55
                with dissolve
                yuri "\" Oh, it's you.\""
                p "\" Expecting someone else?\""
                yuri "\" *Sigh*\""
                yuri "\" Vanya.\""
                p "\" That's what you call him?\""
                hide 21newalex55
                show 21newalex56
                with dissolve
                yuri "\" Heh.\""
                yuri "\" I'm in this hospital so often, it's starting to feel like home.\""
                yuri "\" I think one of the nurses likes me.\""
                p "\" Yeah.\""
                p "\" Sorry you had to land in here again.\""
                hide 21newalex56
                show 21newalex57
                with dissolve
                yuri "\" I didn't land in here.\""
                yuri "\" You punched me.\""
                p "\" Yeah well...\""
                p "\" You understand why I did that, right.\""
                yuri "\" Because of uncle Boris.\""
                yuri "\" Alex told me yesterday.\""
                yuri "\" Fucked up.\""
                p "\" Yes.\""
                yuri "\" How is he?\""
                p "\" Better, I think.\""
                yuri "\" I'll try to visit him tonight. After everyone is gone.\""
                hide 21newalex57
                show 21newalex58
                with dissolve
                van "\" Heh.\""
                " Alex's uncle walks in."
                van "\" Here you are.\""
                van "\" What did you do this time?\""
                van "\" Walked into a glass door or something?\""
                hide 21newalex58
                show 21newalex59
                with dissolve
                yuri "\" What are you doing here?\""
                yuri "\" Leave me alone.\""
                hide 21newalex59
                show 21newalex60
                with dissolve
                van "\" No, let me guess.\""
                van "\" Got syphilis from a whore.\""
                yuri "\" They don't put you in the hospital for that.\""
                van "\" You'd know.\""
                hide 21newalex60
                show 21newalex61
                with dissolve
                " The two start going at each other like hammer and tongs."
                p "\" Yeah...\""
                p "\" I think I'll leave the two of you to it.\""
                p "\" Nice to see you, Yuri.\""
                hide 21newalex61
                show 21newalex55
                with dissolve
                yuri "\" Wait!\""
                yuri "\" My girls?\""
                p "\" What?\""
                van "\" Heh.\""
                yuri "\" At the agency?\""
                p "\" I'm sure everything is fine.\""
                p "\" I'll stop by there later.\""
                hide 21newalex55
                show 21newalex62
                with dissolve
                " You leave Yuri and get back to Boris."
                " Where Alex is once again interrogating the doctor."
                a "\" When can we get him out of here?\""
                dk "\" He's still recovering.\""
                a "\" But he can do that at home, can't he?\""
                dk "\" I suppose.\""
                dk "\" If he has proper care.\""
                a "\" We'll get a nurse.\""
                hide 21newalex62
                show 21newalex63
                with dissolve
                i "\" And it would be nice for him to be with his family, no?\""
                i "\" Hospitals are so... Sterile.\""
                dk "\" That's by design, miss.\""
                hide 21newalex63
                show 21newalex64
                with dissolve
                p "\" So we can get him out?\""
                dk "\" I suppose.\""
                dk "\" In a few days.\""
                dk "\" But he has to return for the rest of his treatment.\""
                p "\" Of course.\""
                hide 21newalex64
                show 21newalex62
                with dissolve
                a "\" We'll make all the arrangements he needs.\""
                p "\" Time to go.\""
                a "\" Yeah.\""
                hide 21newalex62
                show 21newalex65
                with dissolve
                a "\" Love you, daddy.\""
                a "\" We'll take you home soon, ok.\""
                b "\" Ghdnbtenbtn...\""
                hide 21newalex65
                show back1
                with dissolve
                show 21newalex67
                with dissolve
                " You drive back to the villa."
                a "\" He looked great, didn't he?\""
                p "\" He looked fine.\""
                a "\" More than fine.\""
                a "\" He actually spoke.\""
                hide 21newalex67
                show 21newalex69
                with dissolve
                i "\" I heard it.\""
                i "\" Something about red stuff.\""
                hide 21newalex69
                show 21newalex70
                with dissolve
                i "\" But why didn't you tell me before, about your dad?\""
                a "\" Because we need to keep this under our hat.\""
                i "\" So?\""
                i "\" I can keep a secret.\""
                hide 21newalex70
                show 21newalex68
                with dissolve
                a "\" I didn't really want you that involved.\""
                a "\" And I probably shouldn't have taken you with us to see him now.\""
                a "\" But you've been so dejected lately.\""
                a "\" It's not that I don't trust you, babe.\""
                hide 21newalex68
                show 21newalex67
                with dissolve
                a "\" You hear it too, right.\""
                a "\" What he said?\""
                p "\" I heard something.\""
                hide 21newalex67
                show 21newalex71
                with dissolve
                a "\" We're going to get him home soon.\""
                a "\" Get a nurse or something.\""
                p "\" Are you sure that's a good idea?\""
                a "\" No.\""
                a "\" But I want him home.\""
                hide 21newalex71
                show 21newalex72
                with dissolve
                " You get back to the villa."
                hide 21newalex72
                show 21newalex74
                with dissolve
                " And are accosted by Dima."
                di "\" Listen.\""
                di "\" How long am I going to be here for?\""
                di "\" Did you talk to the boss?\""
                p "\" Didn't get the chance.\""
                hide 21newalex74
                show 21newalex75
                with dissolve
                a "\" What's the matter?\""
                di "\" I'm not some two-bit thug.\""
                di "\" I'm growing old out here, Alex.\""
                a "\" That's exactly why you're here.\""
                a "\" My dad trusts you to keep me safe while he's gone.\""
                hide 21newalex75
                show 21newalex76
                with dissolve
                di "\" If I'm doing that, what's he good for?\" He asks, looking at you."
                p "\" Careful.\""
                di "\" You don't scare me.\""
                hide 21newalex76
                show 21newalex77
                with dissolve
                a "\" Just an extra layer.\""
                a "\" Shows how much he trusts you two.\""
                p "\" Heh.\""
                a "\" Now, be a good boy and stay out here.\""
                hide 21newalex77
                show 21newalex78
                with dissolve
                " Outback you find Bogdan and Vadim at he pool."
                hide 21newalex78
                show 21newalex79
                with dissolve
                a "\" He he...\""
                a "\" I see you're way ahead of me.\""
                a "\" Did you manage to get something to eat?\""
                bog "\" Of course, darling.\""
                bog "\" Finished signing your whatever at school?\""
                bog "\" If not, tell uncle Bogdan.\""
                bog "\" Anybody gives you any trouble, I'll have a talk with them.\""
                a "\" He he...\""
                a "\" No need.\""
                a "\" Let's just have fun.\""
                hide 21newalex79
                show 21newalex80
                with dissolve
                vad "\" Have fun, eh?\""
                vad "\" Well, I've never been a pool person.\""
                hide 21newalex80
                show 21newalex79
                with dissolve
                a "\" That's not what you said last night.\""
                hide 21newalex79
                show 21newalex80
                with dissolve
                vad "\" Last night.\""
                vad "\" Lost of things happened last night that we shouldn't mention, no?\""
                a "\" That's up to you.\""
                hide 21newalex80
                show 21newalex81
                with dissolve
                " Alex changes and jumps in the pool."
                hide 21newalex81
                show 21newalex133
                with dissolve
                " Followed closely by Izzy."
                " And they both try to be as cheerful and appear as care free as possible."
                hide 21newalex82
                show 21newalex83
                with dissolve
                vad "\" Pretty girls.\""
                p "\" And?\""
                vad "\" Notice that I said girls, not girl.\""
                p "\" I did.\""
                p "\" And?\""
                if vadimrespect == True:
                    hide 21newalex83
                    show 21newalex84
                    with dissolve
                    vad "\" I'm not judgin, buddy.\""
                    vad "\" He he...\""
                    vad "\" Nice deal if you can pull it off.\""
                    p "\" I don't know what you mean.\""
                    vad "\" Sure, sure...\""
                    hide 21newalex84
                    show 21newalex86
                    with dissolve
                    vad "\" He he...\""
                    vad "\" I would have done it if I thought it could be done.\""
                    p "\" Careful.\""
                    hide 21newalex86
                    show 21newalex87
                    with dissolve
                    vad "\" Careful about what?\""
                    vad "\" I thought you had no idea what I was talking about.\""
                    hide 21newalex87
                    show 21newalex86
                    with dissolve
                    vad "\" I get it.\""
                    vad "\" I'd stay quiet about it too.\""
                    vad "\" Definitely a death penalty offence, if I'm any judge.\""
                    p "\" You're not.\""
                    jump ep21cont3
                    
                else:
                    hide 21newalex83
                    show 21newalex85
                    with dissolve
                    vad "\" And?\" He whispers."
                    vad "\" I wonder what Boris will have to say about that.\""
                    p "\" About what?\""
                    vad "\" You know.\""
                    p "\" How can I know when you won't say?\""
                    hide 21newalex85
                    show 21newalex86
                    with dissolve
                    vad "\" Heh.\""
                    vad "\" We'll see what he says when he gets back.\""
                    p "\" We will.\""
                    jump ep21cont3 
                            
label ep21cont3:
                scene 21newalex88
                with dissolve
                a "\" You two fighting?\""
                vad "\" No.\""
                vad "\" Nothing to fight about, do we.\""
                show 21newalex89
                with dissolve
                a "\" I shouldn't think so.\""
                a "\" Now get in the pool, both of you.\""
                a "\" The spoiled princess wants you to play together.\""
                hide 21newalex89
                show 21newalex80
                with dissolve
                vad "\" Is that what you are?\""
                vad "\" The spoiled princess?\""
                hide 21newalex80
                show 21newalex89
                with dissolve
                a "\" What else?\""
                hide 21newalex89
                show 21newalex13
                with dissolve
                " You spend some time at the pool, with Alex trying to make a few phone calls."
                p "\" Who are you trying to reach?\""
                p "\" It's the third time you're calling.\""
                hide 21newalex13
                show 21newalex14
                with dissolve
                a "\" My dear Uncle Anton.\""
                p "\" Oh.\""
                a "\" I have to say, I'm worried.\""
                a "\" He's not answering.\""
                a "\" Talk to you?\""
                p "\" Sure.\""
                hide 21newalex14
                show 21newalex15
                with dissolve
                " You retreat to the kitchen."
                p "\" He's not answering?\""
                a "\" No.\""
                a "\" Fat fuck!\""
                p "\" Alex?\""
                hide 21newalex15
                show 21newalex16
                with dissolve
                a "\" You know where he lives?\""
                p "\" Yeah.\""
                a "\" Get over there and see why.\""
                a "\" Why he's not answering.\""
                a "\" Then grab him by the ears and drag his fat ass over here.\""
                p "\" Are you sure?\""
                a "\" Being polite is one thing.\""
                a "\" Being timid is another.\""
                a "\" And I won't be timid.\""
                p "\" I'll have to swing by the agency too.\""
                p "\" Have to meet James.\""
                hide 21newalex16
                show 21newalex17
                with dissolve
                a "\" You do that.\""
                a "\" But then go to Anton's.\""
                p "\" And grab him by the ears.\""
                a "\" Exactly.\""
                hide 21newalex17
                show back1
                with dissolve
                show 21newalex18
                with dissolve
                " You get in the car and head over to the agency."
                hide 21newalex18
                show 21newalex19
                with dissolve
                cl "\" *Humph*\""
                cl "\" Back in the hospital.\""
                cl "\" And he won't let me go see him.\""
                hide 21newalex19
                show 21newalex21
                with dissolve
                nar "\" He just said it's not a good time.\""
                cl "\" Not a good time?\""
                cl "\" Why?\""
                cl "\" When is it a good time, then?\""
                hide 21newalex21
                show 21newalex20
                with dissolve
                cl "\" You'd know.\" She says, when she sees you." 
                cl "\" What happened to Yuri?\""
                p "\" Yuri?\""
                cl "\" Why is he in the hospital again?\""
                hide 21newalex20
                show 21newalex22
                with dissolve
                nar "\" Yeah.\""
                nar "\" Why is he in the hospital again?\""
                nar "\" Did someone punch him?\""
                hide 21newalex22
                show 21newalex20
                with dissolve
                cl "\" What?\""
                cl "\" Someone punched him?\""
                cl "\" Who?\""
                p "\" No.\""
                p "\" I don't think so.\""
                hide 21newalex20
                show 21newalex23
                with dissolve
                cl "\" Well, I'm gonna go see him.\""
                cl "\" No matter what he says.\""
                p "\" Yeah.\""
                p "\" Yeah, you do that.\""
                hide 21newalex23
                show 21newalex24
                with dissolve
                nar "\" Make sure to bring him some crackers.\""
                nar "\" And that none of the orderlies punch him.\""
                hide 21newalex24
                show 21newalex23
                with dissolve
                cl "\" I'm going.\""
                hide 21newalex23
                show 21newalex25
                with dissolve
                " Clara leaves, leaving you alone with Naryssa."
                p "\" Did anyone punch him?\""
                nar "\" He he...\""
                p "\" It's not that funny.\""
                p "\" She hates me enough already.\""
                nar "\" I wouldn't say she hates you.\""
                nar "\" More like she despises you.\""
                p "\" Heh.\""
                p "\" That makes it much better, then.\""
                p "\" Is James around?\""
                hide 21newalex25
                show 21newalex26
                with dissolve
                nar "\" Yeah.\""
                nar "\" Up on the roof.\""
                nar "\" Don't know what's wrong with him, but he's pissed as hell.\""
                nar "\" Hardly said two words to me.\""
                p "\" I imagine.\""
                hide 21newalex26
                show 21newalex27
                with dissolve
                " You go up to the roof and find James."
                ja "\" You know who did it?\""
                p "\" No, not yet.\""
                ja "\" Fuck!\""
                p "\" But I have people looking into it.\""
                ja "\" And we have no idea who or why.\""
                p "\" We have an idea.\""
                p "\" Someone was watching the school from across the street.\""
                p "\" Hugo offered to wait for him on the roof one morning.\""
                ja "\" And that's when...\""
                p "\" Yeah.\""
                hide 21newalex27
                show 21newalex218
                with dissolve
                ja "\" Fuck me!\""
                ja "\" His poor mom.\""
                p "\" Yeah.\""
                hide 21newalex218
                show 21newalex27
                with dissolve
                ja "\" What's the plan?\""
                ja "\" To get at them, that is.\""
                p "\" We don't know who 'them' is yet.\""
                p "\" But like I said, I have people looking into it.\""
                p "\" And I have something for you to do on that front.\""
                ja "\" What?\""
                p "\" The girls won't be back in school for a while.\""
                p "\" So, our watcher will probably try to get a look at Isabella some other way.\""
                hide 21newalex27
                show 21newalex28
                with dissolve
                ja "\" Isabella?\""
                ja "\" Not...\""
                p "\" Don't think so.\""
                p "\" Call it a hunch.\""
                hide 21newalex28
                show 21newalex27
                with dissolve
                p "\" The villa is covered by Dima.\""
                p "\" But he might look for her at her mom's house.\""
                ja "\" Where?\""
                p "\" Izzy's mother's house.\""
                p "\" I want you on that.\""
                hide 21newalex27
                show 21newalex219
                with dissolve
                ja "\" Wait around hoping someone shows up?\""
                p "\" Basically.\""
                p "\" If someone is staking out the place.\""
                p "\" If that happens, call me.\""
                ja "\" I'll call you.\""
                ja "\" I'll call you after I skull fuck them.\""
                p "\" You do you.\""
                p "\" Just make sure they're breathing when I get there.\""
                p "\" We need answers.\""
                hide 21newalex219
                show 21newalex27
                with dissolve
                ja "\" Where is this place.\""
                p "\" I'll show you.\""
                p "\" I have to take care of something else after.\""
                hide 21newalex27
                show back1
                with dissolve
                show 21newalex29
                with dissolve
                " You show James where Izzy's mom lives on your way to Anton's."
                p "\" Call me.\""
                ja "\" Yeah.\""
                hide 21newalex29
                show 21newalex90
                with dissolve
                " When you get there, the place looks empty."
                hide 21newalex90
                show 21newalex91
                with dissolve
                " But someone answers the door when you knock."
                m16 "\" Yes?\""
                p "\" Where's Anton?\""
                m16 "\" Who the fuck are you?\""
                p "\" I'm Boris's man.\""
                p "\" Now where the fuck is Anton?\""
                p "\" And who the fuck are you, actually?\""
                hide 21newalex91
                show 21newalex92
                with dissolve
                m16 "\" He's not here.\""
                m16 "\" Now, fuck off.\""
                p "\" He's not here is, he?\""
                p "\" Let me just check.\""
                hide 21newalex92
                show 21newalex93
                with dissolve
                m16 "\" I told you to fuck off.\""
                p "\" Aha.\""
                hide 21newalex93
                show 21newalex94
                with dissolve
                " You slap him aside, and he crumbles immediately."
                p "\" Let me see if I can find him.\""
                hide 21newalex94
                show 21newalex95
                with dissolve
                m16 "\" Ughh...\""
                hide 21newalex95
                show 21newalex96
                with dissolve
                " You search high and low, but there's no one there."
                p "\" Fuck me.\""
                p "\" Where is he?\""
                hide 21newalex96
                show 21newalex97
                with dissolve
                m16 "\" I told you.\""
                m16 "\" He's not here.\""
                m16 "\" Won't answer his phone either.\""
                p "\" Fuck me!\""
                p "\" And you are?\""
                p "\" Don't make me smack you again.\""
                m16 "\" I'm his fucking son.\""
                p "\" Heh.\""
                p "\" If he shows up, tell him to call Alexandra.\""
                p "\" Don't make me come back here again.\""
                hide 21newalex97
                show 21newalex98
                with dissolve
                m16 "\" Now, get the fuck out!\""
                hide 21newalex98
                show 21newalex99
                with dissolve
                " You get back to the villa to find Alex and Vadim much better disposed towards each other."
                a "\" You?\""
                a "\" Dive?\""
                a "\" You'd fall like a rock.\""
                a "\" And not an elegant rock.\""
                a "\" A clumsy rock. The kind of rock that other rocks change addresses to avoid.\""
                vad "\" Watch this, girlie.\""
                hide 21newalex99
                show 21newalex100
                with dissolve
                " He jumps in the pool."
                hide 21newalex100
                show 21newalex101
                with dissolve
                a "\" Back?\""
                p "\" Yeah.\""
                a "\" Alone, I see.\""
                p "\" Inside.\""
                hide 21newalex101
                show 21newalex102
                with dissolve
                " She follows you inside the house."
                a "\" Where is he?\""
                p "\" Don't know.\""
                p "\" I went to his place, and ran into his son.\""
                a "\" Which one?\""
                p "\" Didn't think to ask.\""
                p "\" Short, bald, ugly dude.\""
                hide 21newalex102
                show 21newalex103
                with dissolve
                a "\" Leonid.\""
                p "\" If you say so.\""
                p "\" He's not home, and they're looking for him too it seems.\""
                p "\" Won't answer his phone.\""
                hide 21newalex103
                show 21newalex104
                with dissolve
                a "\" Not just me, then.\""
                p "\" Won't answer for anyone it seems.\""
                a "\" Maybe he can't.\""
                p "\" Maybe.\""
                hide 21newalex104
                show 21newalex105
                with dissolve
                a "\" And you trust him?\""
                p "\" Who?\""
                a "\" Leo.\""
                p "\" I don't think he was lying.\""
                p "\" But what the fuck do I know?\""
                hide 21newalex105
                show 21newalex106
                with dissolve
                a "\" We should keep looking.\""
                p "\" Where?\""
                a "\" I'm not sure yet.\""
                a "\" I'll try to get in touch with some of Dad's other men.\""
                hide 21newalex106
                show 21newalex107
                with dissolve
                a "\" They all have to fall in line.\""
                a "\" I'll be damned if I'll be a victim.\""
                a "\" Or if I let all my dad built fall to nothing.\""
                p "\" Anton might actually be missing.\""
                hide 21newalex107
                show 21newalex108
                with dissolve
                a "\" We're going to have to find out.\""
                p "\" Yeah.\""
                hide 21newalex108
                show 21newalex113
                with dissolve
                " You get back outside."
                a "\" One more thing.\""
                a "\" We're going to have to do something about a nurse.\""
                if ep15danny == True:
                    p "\" There is a nurse I know.\""
                    a "\" Who?\""
                    p "\" You might not like her.\""
                    p "\" I... Know her pretty well.\""
                    a "\" You think I give a fuck about that at a time like this?\""
                    a "\" Just call her.\""
                    hide 21newalex113
                    show 21newalex131
                    with dissolve
                    " You call Danny."
                    danny "\" Yeah?\""
                    p "\" Hey, it's me.\""
                    p "\" I need to see you.\""
                    danny "\" Let me guess.\""
                    danny "\" You need something?\""
                    p "\" Can you come see me at the villa?\""
                    danny "\" Villa?\""
                    danny "\" Right. Where you took me before.\""
                    danny "\" Ahh...\""
                    danny "\" I guess.\""
                    p "\" Great.\""
                    p "\" I'll be waiting.\""
                    hide 21newalex131
                    show 21newalex132
                    with dissolve
                    a "\" Well?\""
                    p "\" She's on her way.\""
                    hide 21newalex132
                    show 21newalex133
                    with dissolve
                    i "\" Hey.\""
                    i "\" Who's hungry?\""
                    bog "\" Famished.\""
                    a "\" I could eat.\""
                    hide 21newalex133
                    show 21newalex134
                    with dissolve
                    i "\" You?\""
                    p "\" I'm ok.\""
                    hide 21newalex134
                    show 21newalex136
                    with dissolve
                    " You follow her in as she starts cooking."
                    i "\" Sure I can't tempt you?\""
                    p "\" You can. But I gotta see someone.\""
                    i "\" *Ugh*\""
                    p "\" What?\""
                    hide 21newalex136
                    show 21newalex137
                    with dissolve
                    i "\" It's Mr. Boris.\""
                    i "\" I don't know...\""
                    i "\" Seeing him like that...\""
                    p "\" I get it.\""
                    hide 21newalex137
                    show 21newalex138
                    with dissolve
                    i "\" You think I'd be used to it.\""
                    i "\" People being sick.\""
                    i "\" With momma and everything.\""
                    i "\" But somehow...\""
                    hide 21newalex138
                    show 21newalex139
                    with dissolve
                    i "\" It kinda hurt me more.\""
                    if sistersknow == True:
                        p "\" They say you first grow up when you see your parents are mortal.\""
                        i "\" He's not my dad.\""
                        p "\" Oh...\""
                        p "\" Right...\""
                        jump ep21danny
                        
                    else:
                        p "\" He was always like a rock to you.\""
                        i "\" Something like that.\""
                        jump ep21danny
                    
                else:
                    p "\" I guess I could call the doc.\""
                    a "\" Alright.\""
                    hide 21newalex113
                    show 21newalex131
                    with dissolve
                    " You call the doctor."
                    doc "\" Yes?\""
                    p "\" Hey, doc.\""
                    p "\" It's [player_name].\""
                    doc "\" What happened now?\""
                    p "\" Nothing.\""
                    p "\" I just need to talk to you.\""
                    p "\" Are you at your office?\""
                    doc "\" Yes.\""
                    doc "\" I'll be here for most of the day.\""
                    p "\" I'll be there soon.\""
                    hide 21newalex131
                    show 21newalex132
                    with dissolve
                    p "\" I'll go see him.\""
                    a "\" Ok.\" she nods."
                    hide 21newalex132
                    show 21newalex133
                    with dissolve
                    i "\" Hey.\""
                    i "\" Who's hungry?\""
                    bog "\" Famished.\""
                    a "\" I could eat.\""
                    hide 21newalex133
                    show 21newalex134
                    with dissolve
                    i "\" You?\""
                    p "\" I have to go take care of something.\""
                    p "\" I'll handle my food arrangements.\""
                    hide 21newalex134
                    show 21newalex136
                    with dissolve
                    " You follow her in as she starts cooking."
                    i "\" Sure I can't tempt you?\""
                    p "\" You can. But I gotta go see someone.\""
                    i "\" *Ugh*\""
                    p "\" What?\""
                    hide 21newalex136
                    show 21newalex137
                    with dissolve
                    i "\" It's Mr. Boris.\""
                    i "\" I don't know...\""
                    i "\" Seeing him like that...\""
                    p "\" I get it.\""
                    hide 21newalex137
                    show 21newalex138
                    with dissolve
                    i "\" You think I'd be used to it.\""
                    i "\" People being sick.\""
                    i "\" With momma and everything.\""
                    i "\" But somehow...\""
                    hide 21newalex138
                    show 21newalex139
                    with dissolve
                    i "\" It kinda hurt me more.\""
                    if sistersknow == True:
                        p "\" They say you first grow up when you see your parents are mortal.\""
                        i "\" He's not my dad.\""
                        p "\" Oh...\""
                        p "\" Right...\""
                        jump ep21doc
                        
                    else:
                        p "\" He was always like a rock to you.\""
                        i "\" Something like that.\""
                        jump ep21doc
                
label ep21doc:
                scene 21newalex140
                with dissolve
                i "\" She should have trusted me.\""
                i "\" Alex, I mean.\""
                p "\" I don't think it's because she didn't trust you.\""
                i "\" Feels like it.\""
                p "\' Well, I have to go.\""
                i "\" Ok.\""
                show 21newalex109
                with dissolve
                " You get to the doctor's office."
                doc "\" Yes?\""
                p "\" It's about Mr. Boris.\""
                doc "\" Heard he's doing good.\""
                p "\" They might release him.\""
                doc "\" Really?\""
                p "\" But we'd need a nurse.\""
                p "\" To stay with him and everything.\""
                doc "\" I see.\""
                hide 21newalex109
                show 21newalex110
                with dissolve
                " He walks around a bit."
                doc "\" Yes, yes...\""
                doc "\" Home care.\""
                p "\" Can you help?\""
                hide 21newalex110
                show 21newalex111
                with dissolve
                doc "\" Well, you'd need to pay her.\""
                p "\" Of course.\""
                p "\" And they need to be trustworthy.\""
                doc "\" Of course.\""
                doc "\" I'll find someone.\""
                hide 21newalex111
                show 21newalex112
                with dissolve
                doc "\" Anything else?\""
                p "\" That's it for now.\""
                p "\" Call me about the nurse?\""
                doc "\" As soon as I find her.\""
                jump ep21cont4
                
label ep21danny:
                scene 21newalex114
                with dissolve
                " Soon, you get a call from Dima about a woman at the door."
                " And it's Danny."
                show 21newalex115
                with dissolve
                danny "\" Hey!\""
                danny "\" This guy won't let me in.\""
                p "\" Yeah.\""
                hide 21newalex115
                show 21newalex129
                with dissolve
                di "\" Who are you?\""
                p "\" It's fine.\""
                p "\" She's a friend.\""
                di "\" A friend of whom's?\""
                p "\" Everyone.\""
                hide 21newalex129
                show 21newalex130
                with dissolve
                danny "\" I'm everyone's friend.\""
                di "\" Well, I don't know her.\""
                p "\" It's fine.\""
                p "\" Come in.\""
                hide 21newalex130
                show 21newalex116
                with dissolve
                " You take her to the kitchen."
                danny "\" So?\""
                danny "\" What is it this time?\""
                danny "\" Thorn stuck in your paw?\""
                p "\" I appreciate the comparison, but it's about my boss.\""
                hide 21newalex116
                show 21newalex117
                with dissolve
                danny "\" Oh, my!\""
                danny "\" Is he ok?\""
                p "\" Yes, yes...\""
                p "\" Looks like that.\""
                p "\" They'll be releasing him, maybe.\""
                hide 21newalex117
                show 21newalex118
                with dissolve
                danny "\" That's too soon!\" She exclaims."
                p "\" Hush...\""
                p "\" Keep your voice down.\""
                p "\" Not everyone here knows about the boss.\""
                p "\" And not everyone needs to know.\""
                p "\" They'll let him go.\""
                p "\" If we get a nurse.\""
                hide 21newalex118
                show 21newalex119
                with dissolve
                " Alex walks in."
                a "\" Is she here?\""
                a "\" Good.\""
                a "\" When can you start?\""
                hide 21newalex119
                show 21newalex120
                with dissolve
                danny "\" Excuse me?\""
                a "\" [player_name] didn't explain?\""
                a "\" We need a nurse.\""
                a "\" But don't go spreading that about.\""
                danny "\" I got that much.\""
                hide 21newalex120
                show 21newalex121
                with dissolve
                a "\" You're good at it, right?\""
                a "\" Nursing, that is.\""
                hide 21newalex121
                show 21newalex122
                with dissolve
                danny "\" I'm not a nurse anymore.\""
                danny "\" I used to be one.\""
                hide 21newalex122
                show 21newalex121
                with dissolve
                a "\" But you can still do it, right.\""
                a "\" It's not like you lost your touch.\""
                hide 21newalex121
                show 21newalex123
                with dissolve
                a "\" I'm gonna go back to Bogdan.\""
                a "\" Give her anything she wants.\""
                a "\" Just get her here.\""
                hide 21newalex123
                show 21newalex124
                with dissolve
                danny "\" Let me get this straight.\""
                danny "\" You need a nurse, and you thought of me?\""
                p "\" Only one I know.\""
                hide 21newalex124
                show 21newalex125
                with dissolve
                danny "\" I'm not a nurse anymore.\""
                p "\" So?\""
                danny "\" You couldn't pay me enough.\""
                p "\" Try her?\""
                hide 21newalex125
                show 21newalex126
                with dissolve
                danny "\" Her?\""
                p "\" Alex.\""
                p "\" She'll pay you enough to buy your own gym.\""
                p "\" A chain of them, if you want.\""
                p "\" Call it 'Danny's Dumbbells'.\""
                danny "\" I don't think marketing is your calling in life.\""
                hide 21newalex126
                show 21newalex127
                with dissolve
                danny "\" Heh...\""
                p "\" You heard her.\""
                p "\" Anything you want.\""
                danny "\" For now, I'll  just take a ride home.\""
                danny "\" Then, I'll think about it.\""
                p "\" Alright.\""
                hide 21newalex127
                show 21newalex128
                with dissolve
                " You walk outside."
                p "\" I have to go.\""
                hide 21newalex128
                show 21newalex132
                with dissolve
                a "\" Go?\""
                p "\" Driving that girl back home.\""
                a "\" Aha.\""
                a "\" Anything she wants.\""
                bog "\" What are you two talking about?\""
                a "\" Nothing.\""
                a "\" Just a nurse for Izzy's mom.\""
                bog "\" Oh.\""
                bog "\" Poor woman.\""
                hide 21newalex132
                show back1
                with dissolve
                show 21newalex141
                with dissolve
                " You start driving her to her place."
                danny "\" Boss's daughter.\""
                p "\" Yeah.\""
                danny "\" Pretty stuck up, isn't she.\""
                p "\" She's worried about her dad.\""
                hide 21newalex141
                show 21newalex142
                with dissolve
                danny "\" You're right.\""
                danny "\" My bad.\""
                hide 21newalex142
                show 21newalex143
                with dissolve
                danny "\" I should be more understanding.\""
                danny "\" Must be scared out of her wits.\""
                danny "\" Poor thing.\""
                p "\" Good news about the boss, though.\""
                danny "\" Yes.\""
                hide 21newalex143
                show 21newalex142
                with dissolve
                danny "\" Surprised they're willing to release him.\""
                p "\" Under care.\""
                hide 21newalex142
                show 21newalex144
                with dissolve
                " You get her to her place."
                p "\" So, will you come?\""
                p "\" I really need you.\""
                hide 21newalex144
                show 21newalex146
                with dissolve
                danny "\" How come you only come to me when you need me?\""
                p "\" I'm a dickhead, I know.\""
                danny "\" Heh.\""
                danny "\" At least you admit it.\""
                hide 21newalex146
                show 21newalex147
                with dissolve
                danny "\" Would I be in danger?\""
                p "\" Danger?\""
                danny "\" You know what I mean.\""
                p "\" Only of Boris trying to look up your skirt.\""
                hide 21newalex147
                show 21newalex145
                with dissolve
                danny "\" Heh.\""
                danny "\" He wouldn't be the first to try it.\""
                danny "\" Guess I will be wearing pants, then.\""
                p "\" Then how would I look up your skirt?\""
                hide 21newalex145
                show 21newalex148
                with dissolve
                danny "\" Guess you'll have to learn to live without.\""
                p "\" Cruel woman.\""
                danny "\" You don't know the half of it.\""
                hide 21newalex148
                show 21newalex149
                with dissolve
                p "\" You'll come then.\""
                p "\" Yes?\""
                danny "\" I expect to be paid very well.\""
                p "\" Don't worry.\""
                p "\" Close your eyes and picture it. 'Danny's Dumbbells'.\""
                hide 21newalex149
                show 21newalex150
                with dissolve
                danny "\" Still not as enticing as you might think.\""
                p "\" Ahh...\""
                p "\" 'Danny's Decline Benches'?\""
                danny "\" He he...\""
                p "\" You'll come, yes?\""
                danny "\" Yes.\""
                hide 21newalex150
                show 21newalex151
                with dissolve
                " You give her a kiss."
                p "\" Thanks.\""
                hide 21newalex151
                show 21newalex152
                with dissolve
                danny "\" I'm gonna have something to eat.\""
                danny "\" Want some?\""
                p "\" Would that mean I owe you two dinners now?\""
                danny "\" At least.\""
                p "\" Yeah.\""
                hide 21newalex152
                show 21newalex153
                with dissolve
                " You sit down and eat with her."
                " But it's rabbit food."
                hide 21newalex153
                show 21newalex154
                with dissolve
                danny "\" You don't like it?\""
                p "\" Ahh...\""
                p "\" I like it just fine.\""
                p "\" But I think my food would like it more.\""
                hide 21newalex154
                show 21newalex155
                with dissolve
                danny "\" Your food?\""
                danny "\" Carnivore to the end?\""
                p "\" I like to think it was loved and had a name.\""
                hide 21newalex155
                show 21newalex156
                with dissolve
                danny "\" Still counts as dinner, though.\""
                p "\" I won't argue.\""
                hide 21newalex156
                show 21newalex157
                with dissolve
                " You finish up and take your leave."
                p "\" Thanks, again.\""
                danny "\" You're welcome.\""
                jump ep21cont4
                
label ep21cont4:
                scene 21newalex158
                with dissolve
                " You get back to the villa."
                show 21newalex159
                with dissolve
                i "\" No way!\""
                bog "\" Yes, way.\""
                i "\" No way, you can hold your breath longer than me.\""
                bog "\" Try me, girl.\""
                hide 21newalex159
                show 21newalex160
                with dissolve
                p "\" They're having fun.\""
                a "\" Yeah.\""
                a "\" They've taken quite a liking to one another.\""
                a "\" Everything settled?\""
                p "\" Yes.\""
                p "\" Where's Vadim?\""
                a "\" I don't know.\""
                a "\" Why don't you go look for him?\""
                p "\" Sure.\""
                hide 21newalex160
                show 21newalex161
                with dissolve
                " You find him in Boris's office."
                " Sitting at his desk."
                hide 21newalex161
                show 21newalex162
                with dissolve
                p "\" What are you doing here?\""
                vad "\" What?\""
                vad "\" Is there some area I'm not allowed in?\""
                vad "\" Like Bluebeard?\""
                p "\" What?\""
                hide 21newalex162
                show 21newalex163
                with dissolve
                vad "\" Just watching the world from this angle.\""
                vad "\" Heh.\""
                vad "\" Looks good from here.\""
                p "\" Get out of the chair.\""
                hide 21newalex163
                show 21newalex164
                with dissolve
                vad "\" You must think I'm stupid.\""
                vad "\" Something is up.\""
                vad "\" I don't know what exactly, but something is up.\""
                vad "\" You're keeping us prisoners here.\""
                p "\" I'll tell you one last time.\""
                p "\" Get out of that chair.\""
                hide 21newalex164
                show 21newalex165
                with dissolve
                " He stands up."
                vad "\" *Sigh*\""
                vad "\" Dima at the door, you messing about...\""
                vad "\" Something is up.\""
                hide 21newalex165
                show 21newalex166
                with dissolve
                " But despite his obvious suspicions, for the rest of the evening he was all charm."
                hide 21newalex166
                show 21newalex167
                with dissolve
                " Giving you a knowing glare as you head to bed."
                hide 21newalex167
                show 21newalex168
                with dissolve
                i "\" I think I should head to [player_name]'s room tonight.\""
                i "\" Sleep over there.\""
                a "\" What?\""
                a "\" Why?\""
                hide 21newalex168
                show 21newalex169
                with dissolve
                i "\" That Vadim guy.\""
                a "\" Please...\""
                i "\" It's not just this morning.\""
                i "\" The way he looks at us.\""
                hide 21newalex169
                show 21newalex170
                with dissolve
                a "\" I told you not to worry.\""
                a "\" I got him handled.\""
                hide 21newalex170
                show 21newalex171
                with dissolve
                i "\" Are you so sure about that?\""
                a "\" Yes.\""
                if izzyin == True:
                    hide 21newalex171
                    show 21newalex173
                    with dissolve
                    i "\" Puppy?\""
                    p "\" I'll rip his throat out if he's the reason you're leaving.\""
                    i "\" He he...\""
                    i "\" No need to go that far.\""
                    hide 21newalex172
                    show 21newalex174
                    with dissolve
                    a "\" Seriously?\""
                    a "\" You were going to leave me alone, because some guy is giving you bad looks?\""
                    hide 21newalex174
                    show 21newalex171
                    with dissolve
                    i "\" Not just some guy.\""
                    i "\" He walked in on us.\""
                    i "\" Who knows what he's figured out.\""
                    i "\" And I wouldn't be leaving you alone.\""
                    i "\" You're with your puppy.\""
                    i "\" But I don't want anyone's throat ripped out.\""
                    hide 21newalex171
                    show 21newalex176
                    with dissolve
                    " You all go to bed."
                    a "\" He he...\""
                    a "\" Dad will be home soon.\""
                    p "\" You'll have to send them away.\""
                    p "\" Vadim and Bogdan.\""
                    p "\" Once he's here, that is.\""
                    hide 21newalex176
                    show 21newalex177
                    with dissolve
                    a "\" Once he's here and safe, I will.\""
                    a "\" Who gives a fuck then.\""
                    p "\" And Anton.\""
                    a "\" We'll find him.\""
                    a "\" Oh yes.\""
                    hide 21newalex177
                    show 21newalex178
                    with dissolve
                    " She gives you a kiss on the neck."
                    a "\" We'll take care of everything.\""
                    p "\" Everything.\""
                    hide 21newalex178
                    show blackscreen
                    with dissolve
                    " You fall asleep."
                    "..."
                    "... ..."
                    "... ... ..."
                    hide blackscreen
                    show 21newalex179
                    with dissolve
                    " When you open your eyes, you see Boris's room at the hospital."
                    " But something is wrong."
                    hide 21newalex179
                    show 21newalex180
                    with dissolve
                    " A mist rises from the floor."
                    t "\" He he he...\""
                    hide 21newalex180
                    show 21newalex181
                    with dissolve
                    " There it is..."
                    " It's there!"
                    " It's there with him!"
                    hide 21newalex181
                    show 21newalex182
                    with dissolve
                    t "\" He he...\""
                    t "\" Morsel.\""
                    hide 21newalex182
                    show 21newalex183
                    with dissolve
                    t "\" Is it you?\""
                    t "\" Is it you what's been keeping Cherubael?\""
                    t "\" He he...\""
                    hide 21newalex183
                    show 21newalex184
                    with dissolve
                    p "\" *Gasp!!!!*\""
                    p "\" *Pant* *Pant* *Pant*\""
                    hide 21newalex184
                    show 21newalex185
                    with dissolve
                    a "\" What's wrong?!\""
                    a "\" Puppy?\""
                    p "\" I know!\""
                    p "\" I know what he was talking about!\""
                    p "\" Red thing.\""
                    p "\" I need to go over there!\""
                    a "\" What? Where?\""
                    p "\" I need to go!\""
                    hide 21newalex185
                    show 21newalex187
                    with dissolve
                    " You start putting your clothes on."
                    a "\" Where?\""
                    a "\" Where do you need to go?\""
                    p "\" The hospital.\""
                    a "\" What?\""
                    p "\" Sorry.\""
                    p "\" Can't explain.\""
                    p "\" You saw it too, right Izzy?\""
                    p "\" In your dream?\""
                    i "\" Dream?\""
                    i "\" I just dreamt about some red mist.\""
                    p "\" Fuck!\""
                    jump ep21cont5
                    
                else:
                    hide 21newalex171
                    show 21newalex172
                    with dissolve
                    i "\" I still don't like it.\""
                    i "\" I'll be going upstairs.\""
                    p "\" If you want.\""
                    hide 21newalex172
                    show 21newalex174
                    with dissolve
                    a "\" Seriously?\""
                    a "\" You're going to leave me alone, because some guy is giving you bad looks?\""
                    hide 21newalex174
                    show 21newalex171
                    with dissolve
                    i "\" Not just some guy.\""
                    i "\" He walked in on us.\""
                    i "\" Who knows what he's thinking.\""
                    i "\" And I'm not leaving you alone.\""
                    i "\" You're with your puppy.\""
                    hide 21newalex171
                    show 21newalex175
                    with dissolve
                    " Izzy leaves, and you go to bed with Alex."
                    a "\" He he...\""
                    a "\" Dad will be home soon.\""
                    p "\" You'll have to send them away.\""
                    p "\" Vadim and Bogdan.\""
                    p "\" Once he's here, that is.\""
                    hide 21newalex175
                    show 21newalex177
                    with dissolve
                    a "\" Once he's here and safe, I will.\""
                    a "\" Who gives a fuck then.\""
                    p "\" And Anton.\""
                    a "\" We'll find him.\""
                    a "\" Oh yes.\""
                    hide 21newalex177
                    show 21newalex178
                    with dissolve
                    " She gives you a kiss on the neck."
                    a "\" We'll take care of everything.\""
                    p "\" Everything.\""
                    hide 21newalex178
                    show blackscreen
                    with dissolve
                    " You fall asleep."
                    "..."
                    "... ..."
                    "... ... ..."
                    hide blackscreen
                    show 21newalex179
                    with dissolve
                    " When you open your eyes, you see Boris's room at the hospital."
                    " But something is wrong."
                    hide 21newalex179
                    show 21newalex180
                    with dissolve
                    " A mist rises from the floor."
                    t "\" He he he...\""
                    hide 21newalex180
                    show 21newalex181
                    with dissolve
                    " There it is..."
                    " It's there!"
                    " It's there with him!"
                    hide 21newalex181
                    show 21newalex182
                    with dissolve
                    t "\" He he...\""
                    t "\" Morsel.\""
                    hide 21newalex182
                    show 21newalex183
                    with dissolve
                    t "\" Is it you?\""
                    t "\" Is it you what's been keeping Cherubael?\""
                    t "\" He he...\""
                    hide 21newalex183
                    show 21newalex184
                    with dissolve
                    p "\" *Gasp!!!!*\""
                    p "\" *Pant* *Pant* *Pant*\""
                    hide 21newalex184
                    show 21newalex186
                    with dissolve
                    a "\" What's wrong?!\""
                    a "\" Puppy?\""
                    p "\" I know!\""
                    p "\" I know what he was talking about!\""
                    p "\" Red thing.\""
                    p "\" I need to go over there!\""
                    a "\" What? Where?\""
                    p "\" I need to go!\""
                    hide 21newalex186
                    show 21newalex188
                    with dissolve
                    " You start putting your clothes on."
                    a "\" Where?\""
                    a "\" Where do you need to go?\""
                    p "\" The hospital.\""
                    a "\" What?\""
                    p "\" Sorry.\""
                    p "\" Can't explain.\""
                    jump ep21cont5
                    
label ep21cont5:
                scene back2
                with dissolve
                show 21newalex189
                with dissolve
                " You jump in the car and race over to the hospital."
                hide 21newalex189
                show 21newalex190
                with dissolve
                " When you get there the place is mostly empty."
                hide 21newalex190
                show 21newalex191
                with dissolve
                " You find Boris's door."
                " Taking a deep breath, you walk in."
                hide 21newalex191
                show 21newalex192
                with dissolve
                p "\" STEP AWAY FROM HIM!!!\""
                hide 21newalex192
                show 21newalex193
                with dissolve
                m17 "\" What?\""
                m17 "\" Who are you?\""
                m17 "\" What are you doing here?\""
                hide 21newalex193
                show 21newalex194
                with dissolve
                t "\" He he he...\""
                t "\" You came running.\""
                p "\" THING!\""
                hide 21newalex194
                show 21newalex195
                with dissolve
                " Before you know it, he's on the floor."
                m17 "\" Aaaaaaa!...\""
                hide 21newalex195
                show 21newalex196
                with dissolve
                dk "\" What the?!...\""
                dk "\" What are you doing?!\""
                dk "\" Security!!!\""
                hide 21newalex196
                show 21newalex197
                with dissolve
                t "\" He he he...\""
                t "\" I know, now.\""
                t "\" I know.\""
                hide 21newalex197
                show 21newalex195
                with dissolve
                " When you blink, the thing was gone."
                " And all that was there, was a scared young man."
                m17 "\" Please...\""
                hide 21newalex195
                show 21newalex199
                with dissolve
                " Police rush in."
                hide 21newalex199
                show 21newalex195
                with dissolve
                " You keep looking to see that thing, but it's not there."
                hide 21newalex195
                show 21newalex200
                with dissolve
                " And before you know it you're in handcuffs, in the hospital lobby."
                p "\" Shit!\""
                p "\" Listen, there's obviously a mistake.\""
                hide 21newalex200
                show 21newalex201
                with dissolve
                cop2 "\" Your mistake was attacking hospital staff.\""
                cop2 "\" The wagon is coming down to pick you up.\""
                p "\" Fuck!\""
                em "\" Well, well...\""
                hide 21newalex201
                show 21newalex202
                with dissolve
                p "\" Double fuck!\""
                em "\" Is there a good reason you pulled me out of bed at this hour?\""
                p "\" What are you doing here?\""
                em "\" You think you're not flagged?\""
                hide 21newalex202
                show 21newalex203
                with dissolve
                em "\" If you jaywalk, a little birdie tells me about it.\""
                em "\" Come on.\""
                em "\" Let's go.\""
                hide 21newalex203
                show 21newalex204
                with dissolve
                cop2 "\" Ma'am?\""
                cop2 "\" He's assaulted someone.\""
                hide 21newalex204
                show 21newalex205
                with dissolve
                em "\" I know.\""
                em "\" He's coming with me anyway.\""
                hide 21newalex205
                show 21newalex204
                with dissolve
                cop2 "\" But...\""
                hide 21newalex204
                show 21newalex205
                with dissolve
                em "\" Yes?\""
                cop2 "\" Nothing.\""
                hide 21newalex205
                show 21newalex206
                with dissolve
                em "\" Let's go, boyo.\""
                hide 21newalex206
                show back2
                with dissolve
                show 21newalex207
                with dissolve
                " Emma takes you and puts you in the back of her car."
                p "\" I can explain.\""
                hide 21newalex207
                show 21newalex208
                with dissolve
                em "\" Explain why you punched some goober?\""
                em "\" I can't wait to hear it.\""
                em "\" But first you'll tell me what you were doing there in the first place.\""
                p "\"...\""
                hide 21newalex208
                show 21newalex209
                with dissolve
                em "\" What?\""
                em "\" Not feeling chatty anymore.\""
                em "\" Then maybe a night in a cell would help you out.\""
                hide 21newalex209
                show 21newalex210
                with dissolve
                p "\" You think a night in a cell would break me?\""
                em "\" No.\""
                em "\" But I'm petty that way.\""
                hide 21newalex210
                show 21newalex211
                with dissolve
                " She takes you to the central station and puts you in a cell."
                hide 21newalex211
                show 21newalex212
                with dissolve
                em "\" Want to tell me what you were doing at the hospital?\""
                p "\"...\""
                em "\" No?\""
                p "\" Don't I get my phone call?\""
                hide 21newalex212
                show 21newalex213
                with dissolve
                em "\" Of course you will.\""
                em "\" In the morning.\""
                em "\" Well, I'm headed off to bed.\""
                em "\" Goodnight. Don't let the bed bugs bite.\""
                em "\" Seriously. This place has bed bugs.\""
                hide 21newalex213
                show 21newalex211
                with dissolve
                p "\" *Sigh*\""
                jump ep21end
                
label ep21end:
                scene end
                with dissolve
                $ renpy.pause ()
                $ MainMenu(confirm=False)()                     
