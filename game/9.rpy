label ep9robalice:
                scene 9newalex2
                with dissolve
                " You sit yourself down on the couch."
                p "\" Seriously.\""
                p "\" Fuck me!\""
                p "\" I don't need this shit right now.\""
                show 9newalex3
                with dissolve
                ali "\" Or ever, would be my guess.\""
                p "\" Yeah.\""
                p "\" This is bad.\""
                ali "\" Well, it isn't good.\""
                p "\" Yeah.\""
                if ep7alice == True:
                    hide 9newalex3
                    show 9newalex5
                    with dissolve
                    " She takes a seat next to you."
                    ali "\" I hear he was a jackass, though.\""
                    p "\" Who?\""
                    ali "\" The son.\""
                    p "\" He was.\""
                    hide 9newalex5
                    show 9newalex6
                    with dissolve
                    ali "\" I'm sure.\""
                    ali "\" You'd never hurt someone just like that.\""
                    ali "\" He must've been horrid.\""
                    p "\" Hmmmm.....\""
                    ali "\" It's going to be ok.\""
                    hide 9newalex6
                    show 9newalex7
                    with dissolve
                    " She gives you a kiss."
                    hide 9newalex7
                    show 9newalex8
                    with dissolve
                    p "\" Maybe.\""
                    ali "\" I'm sure it will.\""
                    ali "\" Me and Lenny will help you.\""
                    p "\" That's sweet.\""
                    p "\" But I don't want you dragged into this.\""
                    ali "\" You're always there for us, remember?\""
                    ali "\" We'll figure it out.\""
                    ali "\" I'm sure we can dig up a lot of bad shit about the kid.\""
                    ali "\" Put his father on the defensive.\""
                    hide 9newalex8
                    show 9newalex7
                    with dissolve
                    " She gives you another kiss."
                    ali "\" It will be ok.\""
                    ali "\" I know it.\""
                    p "\" Thanks.\""
                    hide 9newalex7
                    show 9newalex4
                    with dissolve
                    ali "\" I'd better go now.\""
                    ali "\" Me and Lenny will get right on it.\""
                    p "\" I appreciate it.\""
                    p "\" Really.\""
                    ali "\" Of course.\""
                    jump ep9cont1
                else:
                    hide 9newalex3
                    show 9newalex4
                    with dissolve
                    ali "\" I'd better go now.\""
                    ali "\" Me and Lenny will get right on this.\""
                    ali "\" Maybe we can dig up something about the son.\""
                    ali "\" Something you could use.\""
                    p "\" I appreciate it.\""
                    p "\" Really.\""
                    ali "\" Of course.\""
                    jump ep9cont1

label ep9robnoalice:
                scene 9newalex2
                with dissolve
                " You sit yourself down on the couch."
                p "\" Seriously.\""
                p "\" Fuck me!\""
                p "\" I don't need this shit right now.\""
                show 9newalex9
                with dissolve
                lenny "\" Asshole, though.\""
                p "\" What?\""
                lenny "\" The son.\""
                lenny "\" I heard he needed killing every day he took a breath.\""
                p "\" Hmmm....\""
                hide 9newalex9
                show 9newalex10
                with dissolve
                lenny "\" I'd better go now.\""
                lenny "\" Me and Alice will get right on this.\""
                lenny "\" Maybe we can dig up something about the son.\""
                lenny "\" Something you could use.\""
                p "\" I appreciate it.\""
                p "\" Really.\""
                lenny "\" Of course.\""
                jump ep9cont1

label ep9cont1:
                scene 7newalex93
                with dissolve
                " You head back downstairs and start to wait for Marcello's man."
                jump ep9cont2

label ep9cont2:
                default ep9sideboris = False
                default ep9phillie = False
                default ep9borislie = False
                default ep9savetanya = False
                scene 9newalex11
                with dissolve
                " It took a while for him to show up."
                " But eventually he did."
                show 9newalex12
                with dissolve
                vinc "\" Do you have it?\""
                p "\" How about hello first.\""
                vinc "\" Do you have it?\""
                hide 9newalex12
                show 9newalex13
                with dissolve
                " You throw him the bag."
                vinc "\" Good.\""
                vinc "\" What we owe you is in a car.\""
                p "\" A car.\""
                vinc "\" Parked in a downtown parking lot.\""
                vinc "\" I'll give you the keys and where you can find it.\""
                p "\" I'm supposed to take this on faith?\""
                vinc "\" Do you want your money back?\""
                vinc "\" I'll give it to you.\""
                p "\" Fine.\""
                p "\" Just give me the keys.\""
                hide 9newalex13
                show 9newalex14
                with dissolve
                " He tells you where to find the car, and leaves."
                yuri "\" Not very friendly, is he?\""
                p "\" No.\""
                yuri "\" This is how it should be, though.\""
                yuri "\" Money and... you know... never in the same place.\""
                p "\" I imagine.\""
                yuri "\" What? Do you think he's cheating you?\""
                p "\" Doubt it.\""
                hide 9newalex14
                show 9newalex15
                with dissolve
                yuri "\" So? Do we go get it?\""
                p "\" We?\""
                yuri "\" I mean. I'm your main guy, right?\""
                p "\" My main guy... haha.\""
                yuri "\" Laugh all you want.\""
                yuri "\" But who's going to handle the day to day on this?\""
                p "\" Hmmm...\""
                p "\" Sure you want to be involved?\""
                yuri "\" You know who my family is, yes?\""
                p "\" Let's go.\""
                hide 9newalex15
                show back1
                with dissolve
                show 9newalex16
                with dissolve
                yuri "\" How much do you think you'll make?\""
                yuri "\" Per month, I mean?\""
                yuri "\" Where will you price it?\""
                p "\" I honestly have no clue.\""
                yuri "\" I can take care of that for you... if you want.\""
                p "\" And for a piece of the profits, of course.\""
                yuri "\" You think that's unreasonable?\""
                p "\" How much?\""
                yuri "\" Ten percent.\""
                p "\" Done.\""
                yuri "\" Should've asked for twenty.\""
                p "\" Hehe... probably.\""
                hide 9newalex16
                show 9newalex17
                with dissolve
                " You arrive at the parking lot."
                yuri "\" I'll go check.\""
                hide 9newalex17
                show 9newalex18
                with dissolve
                p "\" Find anything?\""
                yuri "\" Hmmm...\""
                p "\" Well?\""
                yuri "\" Yeah.\""
                yuri "\" It's here under the seat.\""
                hide 9newalex18
                show 9newalex16
                with dissolve
                " You take the package and get back in your own car."
                p "\" You'll take care of this?\""
                yuri "\" Yeah.\""
                yuri "\" Consider it done.\""
                p "\" Find out how much we can sell in a week.\""
                p "\" I'll know how big our next order should be.\""
                yuri "\" Anything for my twenty percent.\""
                p "\" You mean ten.\""
                yuri "\" Fifteen.\""
                p "\" Alright. But we're not negotiating again.\""
                p "\" I'll drop you off at the agency.\""
                p "\" Have to go pick up Boris.\""
                yuri "\" Yeah. It's getting pretty late.\""
                hide 9newalex16
                show 9newalex19
                with dissolve
                " After dropping off Yuri at the agency, you make your way back to where you left Boris."
                hide 9newalex19
                show 9newalex20
                with dissolve
                b "\" All good?\""
                p "\" As far as I know.\""
                b "\" No one came to bother you today?\""
                p "\" Bother me?\""
                b "\" Tanya's men maybe?\""
                b "\" She seemed to take a liking to you.\""
                p "\" No.\""
                b "\" Good.\""
                b "\" Let's go pick up the girls.\""
                p "\" Mmm...\""
                p "\" Is it my imagination...\""
                p "\" Or did you change your clothes, boss?\""
                b "\" What? No!\""
                p "\" I thought...\""
                b "\" I didn't.\""
                p "\" Ok.\""
                hide 9newalex20
                show 9newalex21
                with dissolve
                " You go to school and pick up Alex and Izzy."
                a "\" Hey.\""
                p "\" Hey.\""
                a "\" You boys went shopping?\""
                p "\" No.\""
                hide 9newalex21
                show 9newalex22
                with dissolve
                a "\" Hmmm...\""
                a "\" I'm pretty sure your jacket was black this morning, Dad.\""
                hide 9newalex22
                show 9newalex23
                with dissolve
                b "\" You're misremembering!\""
                hide 9newalex23
                show 9newalex24
                with dissolve
                a "\" I...\""
                hide 9newalex24
                show 9newalex25
                with dissolve
                a "\" Ohh...\""
                a "\" Right.\""
                a "\" It was blue.\""
                a "\" I remember now.\""
                hide 9newalex25
                show 9newalex26
                with dissolve
                " You get to the villa."
                " And with Boris heading to his office, and Izzy to do some studying, you're left alone with Alex."
                p "\" What was that?\""
                hide 9newalex26
                show 9newalex27
                with dissolve
                a "\" Huh?\""
                p "\" He changed his clothes.\""
                p "\" I noticed too.\""
                p "\" I'm not crazy.\""
                a "\" Oceania has always been at war with Eastasia.\""
                p "\" What?\""
                a "\" I told you. There are some things I don't want to know.\""
                a "\" Not about you. Not about Dad.\""
                a "\" Not about your... escapades.\""
                p "\" So you think...\""
                a "\" I'm not asking him. And I won't be asking you.\""
                hide 9newalex27
                show 9newalex28
                with dissolve
                a "\" Hey!\""
                a "\" There are many men that would be ecstatic about having a willfully oblivious wife.\""
                a "\" Especially when it comes to some things.\""
                p "\" Wife?\""
                a "\" Shut up!\""
                a "\" Now, come on. Let's get something to eat.\""
                hide 9newalex28
                show 9newalex29
                with dissolve
                " Later, you're back in the living room watching Snooker."
                " With Alex cradled in your arms again."
                hide 9newalex29
                show 9newalex30
                with dissolve
                b "\" So this is how it's going to be?\""
                a "\" Huh?\""
                b "\" This is a thing the three of us do now?\""
                hide 9newalex30
                show 9newalex31
                with dissolve
                a "\" Yeah.\""
                a "\" We should do things like a family. Don't you think?\""
                hide 9newalex31
                show 9newalex30
                with dissolve
                b "\" Groan.\""
                hide 9newalex30
                show 9newalex32
                with dissolve
                i "\" Hi.\""
                i "\" Mind if I join you?\""
                hide 9newalex32
                show 9newalex33
                with dissolve
                b "\" Of course not, darling.\""
                b "\" Have a seat.\""
                b "\" Done with the studying?\""
                hide 9newalex33
                show 9newalex34
                with dissolve
                i "\" Yes.\""
                i "\" I just needed to freshen up some things in my memory.\""
                b "\" Hear that Alex?\""
                a "\" Snore.\""
                b "\" Sigh.\""
                hide 9newalex34
                show 9newalex35
                with dissolve
                " You all started watching the TV."
                " With Boris looking annoyed, and Alex drifting in and out of sleep."
                hide 9newalex35
                show 9newalex36
                with dissolve
                a "\" Babe?\" She says, addressing Izzy."
                a "\" I think I'm done.\""
                a "\" Want to go to sleep.\""
                hide 9newalex36
                show 9newalex37
                with dissolve
                i "\" Sure.\""
                hide 9newalex37
                show 9newalex38
                with dissolve
                " They go upstairs."
                a "\" Ugh...\""
                i "\" What?\""
                a "\" My butt hurts.\""
                i "\" What?\""
                a "\" Puppy has a heavy arm.\""
                a "\" When he rests it on my ass, it sometimes goes numb.\""
                b "\" Groan...\""
                hide 9newalex38
                show 9newalex39
                with dissolve
                " With the girls gone, you and Boris stay till the end of the match."
                " All the while, from time to time, he would inexplicably snigger."
                hide 9newalex39
                show 9newalex40
                with dissolve
                " He kept sniggering even as you left."
                p "\" Boss?\""
                b "\" Back to your attic room, yes?\""
                b "\" Snigger...\""
                p "\" I guess.\""
                b "\" I mean, Isabella is sleeping in Alex's bedroom, right.\""
                p "\" I assume.\""
                b "\" Snigger...\""
                b "\" Sleep tight.\""
                if izzyin == True:
                    hide 9newalex40
                    show 9newalex41
                    with dissolve
                    " But when you get to your attic bedroom, you find Alex and Izzy there."
                    p "\" Girls?\""
                    a "\" Shush.\""
                    a "\" She's sleeping.\""
                    a "\" Move quietly.\""
                    hide 9newalex41
                    show 9newalex42
                    with dissolve
                    " You quietly change and get on the bed beside them."
                    p "\" What are you doing here.\""
                    a "\" Trying to sleep.\""
                    p "\" Your dad?\""
                    a "\" We'll be gone before morning.\""
                    a "\" Now get to sleep.\""
                    hide 9newalex42
                    show blackscreen
                    with dissolve
                    "...."
                    "......"
                    "........."
                    hide blacksreen
                    show 9newalex44
                    with dissolve
                    " In the morning, you woke up alone."
                    " You change your clothes and head downstairs."
                    jump ep9cont3

                else:
                    hide 9newalex40
                    show 9newalex43
                    with dissolve
                    " You get to your attic bedroom, and go to sleep."
                    p "\" Hmmm...\""
                    p "\" I'm thinking of this room as my bedroom when I have my own place.\""
                    p "\" Strange.\""
                    hide 9newalex43
                    show blackscreen
                    with dissolve
                    "..."
                    "......"
                    "........."
                    hide blackscreen
                    show 9newalex44
                    with dissolve
                    " You wake up in the morning and head downstairs."
                    jump ep9cont3

label ep9cont3:
                scene 9newalex45
                with dissolve
                a "\" Hmm...\""
                a "\" I don't know.\""
                a "\" Maybe next year, I'm thinking.\""
                p "\" Morning, girls.\""
                show 9newalex46
                with dissolve
                a "\" Hey, Pupster.\""
                p "\" What are you two on about.\""
                a "\" Vacation is coming up.\""
                a "\" We were talking about where we should go.\""
                i "\" What's wrong with Europe?\""
                i "\" I have some money saved up.\""
                hide 9newalex46
                show 9newalex47
                with dissolve
                a "\" It's not an issue of money.\""
                a "\" [player_name] can't be gone from work for that long.\""
                if izzyin == True:
                    i "\" Why not?\""
                    a "\" It's too early for him.\""
                    a "\" I know these things.\""
                    jump ep9cont4
                else:
                    i "\" The two of us could go.\""
                    a "\" I hope you're joking.\""
                    a "\" Look. We'll talk about it some other time.\""
                    jump ep9cont4

label ep9cont4:
                scene 9newalex48
                with dissolve
                " You have breakfast in silence, and go wrangle up Boris."
                show 9newalex49
                with dissolve
                " You all get dressed and ready to head out."
                hide 9newalex49
                show 9newalex50
                with dissolve
                mi "\" Boss!\""
                mi "\" You need to get back inside.\""
                hide 9newalex50
                show 9newalex51
                with dissolve
                b "\" What?\""
                hide 9newalex51
                show 9newalex50
                with dissolve
                mi "\" We've been hit in a couple of places.\""
                b "\" Hit?\""
                hide 9newalex50
                show 9newalex52
                with dissolve
                mi "\" Looks like Tanya's men.\""
                hide 9newalex52
                show 9newalex51
                with dissolve
                b "\" Fucking bitch!\""
                b "\" Bad?\""
                hide 9newalex51
                show 9newalex52
                with dissolve
                mi "\" Not bad.\""
                mi "\" Not yet.\""
                hide 9newalex52
                show 9newalex53
                with dissolve
                b "\" Alex! You and Izzy get back in the house.\""
                a "\" What? No.\""
                a "\" I can hear this.\""
                b "\" Get back in the house and don't come out till I tell you.\""
                a "\" I'm not scared, Dad.\""
                b "\" ALEX!\""
                " Do you side with Boris?"
                call screen screen47

label ep9boris:
                scene 9newalex56
                with dissolve
                $ ep9sideboris = True
                $ alexpoints = alexpoints + 2
                p "\" Alex. Your dad is right.\""
                a "\" Told you, I'm not scared.\""
                p "\" It's not about being scared.\""
                a "\" Then why?\""
                p "\" Because I'm telling you to.\" You say putting a bit of bass in your voice."
                p "\" Now go!\""
                " Perhaps hearing the tone of your voice, she obeys without another word."
                show 9newalex57
                with dissolve
                b "\" She listens to you.\""
                p "\" Sometimes.\""
                b "\" Good.\""
                jump ep9cont5

label ep9noboris:
                scene 9newalex54
                with dissolve
                b "\" Do as I tell you!\""
                a "\" When do I ever do that?\""
                b "\" Damn you, girl!\""
                a "\" Fine!\""
                a "\" But I'm only doing this not to undermine you in front of your men.\" She whispers and finally walks away."
                show 9newalex54
                show 9newalex55
                with dissolve
                b "\" You could've said something, you know.\""
                jump ep9cont5

label ep9cont5:
                scene 9newalex58
                with dissolve
                b "\" Now, tell me everything.\""
                mi "\" They hit us in a couple of places.\""
                mi "\" No fatalities.\""
                mi "\" So far, anyway.\""
                show 9newalex59
                with dissolve
                b "\" Alright.\""
                b "\" I'll go with Micha to start dealing with this.\""
                p "\" I should be coming with you.\""
                b "\" I want you here to look after my daughter.\""
                b "\" Don't worry. We'll check on your little agency.\""
                b "\" Priorities, remember.\""
                p "\" Got it.\""
                hide 9newalex59
                show 9newalex60
                with dissolve
                " You head back inside and find the girls."
                a "\" I've been through this before.\""
                a "\" It's going to be fine.\""
                if ep9sideboris == True:
                    " Then Alex notices you come in."
                    a "\" I'm not a child, you know.\""
                    a "\" I don't need to be sent to my room.\""
                    p "\" I know.\""
                    a "\" Then what the hell was that?\""
                    hide 9newalex60
                    show 9newalex61
                    with dissolve
                    " You get very close to her."
                    p "\" Listen.\""
                    p "\" I'm willing to defer to you on most things.\""
                    p "\" Can't say I'm not.\""
                    p "\" I've been your playful little puppy.\""
                    p "\" But on other things...\""
                    p "\" When I tell you to do something.\""
                    p "\" You're doing it!\""
                    p "\" Understood?!\""
                    hide 9newalex61
                    show 9newalex62
                    with dissolve
                    " Despite herself, a smile begins to stretch over her face."
                    a "\" Understood.\""
                    jump ep9cont6

                else:
                    jump ep9cont6

label ep9cont6:
                scene 9newalex64
                with dissolve
                i "\" I'm worried about Momma.\""
                a "\" I'm sure she's fine.\""
                i "\" Still. I'd like her to be here.\""
                i "\" You know...\""
                show 9newalex65
                with dissolve
                i "\" I'll go get her.\""
                a "\" No, you're not.\""
                a "\" Sit down.\""
                a "\" You heard what [player_name] said.\""
                i "\" Even if she's fine, I don't want her to be alone for that long.\""
                i "\" Who knows how long this will last.\""
                hide 9newalex65
                show 9newalex66
                with dissolve
                a "\" Pupster?\""
                p "\" I'll go get her.\""
                p "\" You two stay here.\""
                hide 9newalex66
                show 9newalex67
                with dissolve
                " She kisses your nose."
                a "\" Thanks.\""
                p "\" You stay right here.\""
                a "\" Right here.\""
                hide 9newalex67
                show 9newalex68
                with dissolve
                a "\" Careful, eh?\""
                p "\" You don't have to tell me.\""
                hide 9newalex68
                show 9newalex70
                with dissolve
                i "\" Thank you.\""
                p "\" You don't have to.\""
                hide 9newalex70
                show 9newalex71
                with dissolve
                a "\" Be careful?\""
                p "\" Heard you the first time.\""
                p "\" Don't worry.\""
                hide 9newalex71
                show 9newalex69
                with dissolve
                " You make a call to the agency before you go."
                " Just to make sure everything is ok."
                " Yuri assures you it's all good, and he hasn't heard anything."
                hide 9newalex69
                show 9newalex72
                with dissolve
                " You get to Izzy's place, and open the door."
                hide 9newalex72
                show 9newalex73
                with dissolve
                ag "\" What are you doing here, whoremonger?\""
                p "\" Mrs. Agatha.\""
                p "\" We need to go.\""
                p "\" I'm here to take you to your daughter.\""
                hide 9newalex73
                show 9newalex74
                with dissolve
                ag "\" Nonsense.\""
                ag "\" I know why you're here, whoremonger.\""
                p "\" Mrs. Agatha...\""
                hide 9newalex74
                show 9newalex75
                with dissolve
                " She opens her bathrobe."
                ag "\" Here!\""
                p "\" Groan!\""
                ag "\" Take what you want.\""
                ag "\" You think I haven't been fucked before, whoremonger?\""
                hide 9newalex75
                show 9newalex76
                with dissolve
                p "\" Like I said.\""
                p "\" I'm here to take you to Izzy.\""
                ag "\" You mean to your piss-haired whore.\""
                p "\" I don't have time for this shit.\""
                hide 9newalex76
                show 9newalex77
                with dissolve
                " You pick her up and carry her away."
                ag "\" Agh...\""
                hide 9newalex77
                show back1
                with dissolve
                show 9newalex78
                with dissolve
                " In the car, she starts yapping again."
                ag "\" It's not natural.\""
                ag "\" They think I don't know what they're doing.\""
                ag "\" Same seed.\""
                p "\" Whatever you say, Agatha.\""
                ag "\" He doesn't know, hehe...\""
                ag "\" But it's the same.\""
                hide 9newalex78
                show 9newalex79
                with dissolve
                ag "\" Do you understand me?\""
                ag "\" Same seed!\""
                p "\" Please be quiet.\""
                hide 9newalex79
                show 9newalex80
                with dissolve
                " You finally get her to the house."
                a "\" Will you stop pacing?\""
                a "\" They're both fine, I promise.\""
                hide 9newalex80
                show 9newalex81
                with dissolve
                a "\" There they are.\""
                a "\" See?\""
                a "\" I told you.\""
                hide 9newalex81
                show 9newalex82
                with dissolve
                i "\" Thank God!\""
                i "\" Momma!\""
                hide 9newalex82
                show 9newalex83
                with dissolve
                ag "\" Why has the whoremonger brought me here?\""
                ag "\" I know this house.\""
                ag "\" I swore I wouldn't step foot in here again.\""
                i "\" Yeah, Momma. Whatever.\""
                i "\" Let's go find a room to put you in.\""
                hide 9newalex83
                show 9newalex84
                with dissolve
                " Once they leave, Alex throws her arms around you."
                a "\" Thanks.\""
                p "\" You don't have to.\""
                hide 9newalex84
                show 9newalex85
                with dissolve
                a "\" I know.\""
                hide 9newalex85
                show 9newalex86
                with dissolve
                " She gives you a kiss."
                a "\" Love ya.\""
                hide 9newalex86
                show 9newalex87
                with dissolve
                p "\" I'm going to go outside and stand guard.\""
                p "\" You stay inside the house and don't leave.\""
                a "\" Got it.\""
                p "\" Not unless I come and get you.\""
                a "\" Ok.\""
                p "\" Not for any reason.\""
                a "\" Ok, Pupster.\""
                p "\" Alright, then.\""
                hide 9newalex87
                show 9newalex88
                with dissolve
                " You leave Alex and take a post outside with the other men."
                " Waiting for either Boris or Tanya's men to come."
                hide 9newalex88
                show 9newalex89
                with dissolve
                " Later that day, Boris finally shows up."
                p "\" Boss?\""
                b "\" [player_name].\""
                p "\" All good?\""
                b "\" Yes and no.\""
                b "\" We'll talk inside.\""
                hide 9newalex89
                show 9newalex90
                with dissolve
                " In his office, he collapses in his chair."
                b "\" Groan...\""
                p "\" That bad?\""
                b "\" Yes and no.\""
                hide 9newalex90
                show 9newalex91
                with dissolve
                b "\" She's not trying to destroy us.\""
                b "\" She could never do that.\""
                b "\" She's too small.\""
                b "\" We'd win in the end.\""
                hide 9newalex91
                show 9newalex92
                with dissolve
                b "\" But the fucking bitch is looking for a tribute.\""
                p "\" Tribute?\""
                hide 9newalex92
                show 9newalex91
                with dissolve
                b "\" She can be an annoyance to us.\""
                b "\" Sting us here and there while we have bigger fish to fry.\""
                p "\" So we give her concessions to make her go away?\""
                b "\" That's what she's planning on. Well, hoping for at least.\""
                p "\" Are you going to pay?\""
                b "\" I don't know.\""
                b "\" It might be worth it.\""
                b "\" She's gone underground. Don't know where she is.\""
                hide 9newalex91
                show 9newalex93
                with dissolve
                b "\" So, we have to do it too.\""
                b "\" I've arranged for a hotel.\""
                b "\" Public place. We'll fill the lobby with our men.\""
                p "\" I think I know it.\""
                p "\" The place where we took care of that guy.\""
                b "\" Yeah.\""
                hide 9newalex93
                show 9newalex91
                with dissolve
                b "\" How is Alex?\""
                p "\" Pretty good, considering.\""
                p "\" Not freaking out at all.\""
                b "\" She's been through this before.\'"
                b "\" When she was 6, I had to stash her in a hotel outside of town for 2 months.\""
                p "\" Damn.\""
                b "\" Well, let's go get them.\""
                hide 9newalex91
                show 9newalex94
                with dissolve
                " You find Alex in the living room."
                hide 9newalex94
                show 9newalex95
                with dissolve
                a "\" Dad?\""
                b "\" You're not going to like this, sweetie.\""
                a "\" We have to hide?\""
                hide 9newalex95
                show 9newalex96
                with dissolve
                b "\" Yes. While I take care of this.\""
                b "\" I'm sorry.\""
                hide 9newalex96
                show 9newalex97
                with dissolve
                a "\" Pupster will be guarding us, right?\""
                b "\" Him and others.\""
                a "\" Ok.\""
                b "\" Sorry.\""
                a "\" It's fine.\""
                a "\" I'll go get the girls.\""
                b "\" Girls?\""
                a "\" Izzy and her mom.\""
                b "\" Oh...\""
                hide 9newalex97
                show 9newalex98
                with dissolve
                " Alex mobilizes the girls and you're soon ready to leave."
                hide 9newalex98
                show 9newalex103
                with dissolve
                b "\" Agatha!\""
                b "\" Good to see you again.\""
                hide 9newalex103
                show 9newalex104
                with dissolve
                ag "\"...\""
                hide 9newalex104
                show 9newalex103
                with dissolve
                b "\" Don't you remember me?\""
                hide 9newalex103
                show 9newalex104
                with dissolve
                " For once, she seems at a loss for words."
                ag "\"...\""
                i "\" I'm sorry, sir.\""
                hide 9newalex104
                show 9newalex103
                with dissolve
                b "\" It's fine, darling.\""
                b "\" Let's go.\""
                hide 9newalex103
                show back1
                with dissolve
                show 9newalex99
                with dissolve
                " You get them all in the car and head to the hotel."
                hide 9newalex99
                show 9newalex105
                with dissolve
                " And despite repeated proddings from both Izzy and Boris, Agatha refuses to say a word."
                hide 9newalex105
                show 9newalex100
                with dissolve
                a "\" We're going to a hotel?\""
                p "\" Yeah.\""
                a "\" We can get comfortable in a hotel.\""
                a "\" I remember I was in a motel one time.\""
                hide 9newalex100
                show 9newalex101
                with dissolve
                " You get to the hotel, and head up to the room."
                a "\" Nice big bed.\""
                a "\" Good.\""
                a "\" Had me worried for a second.\""
                hide 9newalex101
                show 9newalex106
                with dissolve
                b "\" The bed is not the issue.\""
                hide 9newalex106
                show 9newalex102
                with dissolve
                a "\" Of course it's an issue.\""
                a "\" Finally have some space.\""
                a "\" My back aches from sleeping in Puppy's cot back home.\""
                a "\" Not to mention all the sneaking.\""
                hide 9newalex102
                show 9newalex108
                with dissolve
                b "\" You've been what?\""
                hide 9newalex108
                show 9newalex107
                with dissolve
                a "\" Yes.\""
                a "\" You really think this is the time to lecture me?\""
                a "\" Really?\""
                hide 9newalex107
                show 9newalex108
                with dissolve
                b "\" We have two rooms.\""
                b "\" He can sleep in the other one.\""
                hide 9newalex108
                show 9newalex109
                with dissolve
                a "\" What about Izzy and her mom?\""
                a "\" Or are you suggesting Puppy bunk with Agatha.\""
                hide 9newalex109
                show 9newalex108
                with dissolve
                b "\" Groan...\""
                b "\" Just keep her safe, ok?\""
                p "\" Done.\""
                hide 9newalex108
                show 9newalex110
                with dissolve
                " Boris leaves, and you're left alone with the girls."
                i "\" Momma, let's go to the other room.\""
                i "\" I'll help you settle in.\""
                ag "\" Is he gone?\""
                i "\" Who?\""
                ag "\" Him.\""
                i "\" Whatever, let's just go.\""
                if izzyin == True:
                    hide 9newalex110
                    show 9newalex117
                    with dissolve
                    i "\" I'll have to go take care of Momma.\""
                    a "\" Need help?\""
                    i "\" It will be a little difficult.\""
                    i "\" New environment and all.\""
                    i "\" But there's nothing you can really help me with.\""
                    a "\" If you say so.\""
                    a "\" I'm so sorry about this, babe.\""
                    i "\" It's fine.\""
                    a "\" This is what you get for being close to me, I guess.\""
                    i "\" Like I said. Don't worry.\""
                    i "\" Love you.\""
                    a "\" Love you too.\""
                    hide 9newalex117
                    show 9newalex118
                    with dissolve
                    i "\" And, Pupster..\""
                    p "\" Love you too.\""
                    i "\" I have to take care of Momma.\""
                    i "\" But if you need something and Alex turns frigid.\""
                    a "\" Oh, fuck you!\""
                    i "\" You know you do, sometimes.\""
                    i "\" Just wait till Momma goes to sleep.\""
                    p "\" Thanks, but I'm fine.\""
                    i "\" Thanks for taking care of us.\""
                    p "\" Of course.\""
                    jump ep9cont7

                else:
                    hide 9newalex110
                    show 9newalex117
                    with dissolve
                    i "\" I'll have to go take care of Momma.\""
                    a "\" Need help?\""
                    i "\" It will be a little difficult.\""
                    i "\" New environment and all.\""
                    i "\" But there's nothing you can really help me with.\""
                    a "\" If you say so.\""
                    a "\" I'm so sorry about this, babe.\""
                    i "\" It's fine.\""
                    a "\" This is what you get for being close to me I guess.\""
                    i "\" Like I said. Don't worry.\""
                    i "\" Love you.\""
                    a "\" Love you too.\""
                    hide 9newalex117
                    show 9newalex116
                    with dissolve
                    " She looks at you timidly."
                    " And grudgingly, she says."
                    i "\" Thanks for helping us.\""
                    p "\" No worries.\""
                    jump ep9cont7

label ep9cont7:
                scene 9newalex111
                with dissolve
                " Izzy goes with Agatha, and you're left with Alex."
                show 9newalex112
                with dissolve
                a "\" You know what the worst thing about these situations is?\""
                p "\" Huh?\""
                a "\" The boredom.\""
                hide 9newalex112
                show 9newalex113
                with dissolve
                " She kisses your shoulder."
                hide 9newalex113
                show 9newalex114
                with dissolve
                a "\" Just want you to know.\""
                a "\" I don't take you for granted.\""
                p "\" You kinda do.\""
                a "\" Well, maybe a little.\""
                a "\" But you take me for granted too.\""
                p "\" No I don't.\""
                hide 9newalex114
                show 9newalex115
                with dissolve
                a "\" Really?\""
                a "\" Do you have any fear that I might send you packing?\""
                a "\" Do you restrain your behavior out of fear of my reaction?\""
                p "\" Not really.\""
                a "\" Well, that's taking someone for granted.\""
                p "\" No. I don't think so.\""
                hide 9newalex115
                show 9newalex113
                with dissolve
                " She kisses you again."
                a "\" Maybe not.\""
                a "\" Maybe you're right.\""
                hide 9newalex113
                show 9newalex120
                with dissolve
                " And then throws herself down on the bed."
                a "\" One thing I know for sure.\""
                a "\" We'll get bored stiff in here.\""
                hide 9newalex120
                show 9newalex122
                with dissolve
                " She lays around on the bed while you get on the couch and face the door."
                hide 9newalex122
                show 9newalex123
                with dissolve
                a "\" Pupster.\""
                p "\" Huh?\""
                a "\" I'm bored.\""
                p "\" You're grown too.\""
                a "\" Can we get some room service?\""
                p "\" No.\""
                a "\" Ya vol mein kommandant.\""
                a "\" Look at Puppy asserting himself.\""
                hide 9newalex123
                show 9newalex124
                with dissolve
                " She comes over and leans on you."
                a "\" I'm not frigid, am I?\""
                p "\" I don't know.\""
                a "\" I am colder than most women, I know.\""
                a "\" I'm not into that sweet slop shit.\""
                a "\" But I'm not...\""
                a "\" I mean, you don't feel that...\""
                p "\" No.\""
                hide 9newalex124
                show 9newalex125
                with dissolve
                p "\" But you can't say I'm not patient.\""
                p "\" With your beach stuff.\""
                a "\" I can't say you haven't.\""
                a "\" I rented a house, you know.\""
                p "\" Is it nice?\""
                a "\" Looks nice in the pictures.\""
                hide 9newalex125
                show 9newalex126
                with dissolve
                a "\" But hey!\""
                a "\" You can't really complain.\""
                a "\" I mean, I've taken more dick from you than anyone else.\""
                p "\" From what I understand, your previous number was zero. So, I can't really say that's an achievement.\""
                a "\" 100 percent increase.\""
                a "\" Now that's growth.\""
                p "\" Hehe.\""
                hide 9newalex126
                show 9newalex127
                with dissolve
                a "\" I find it difficult too, you know.\""
                a "\" I'm not sure how to deal with you.\""
                a "\" I mean, with Izzy...\""
                a "\" I've known her since forever.\""
                a "\"  I don't have to...\""
                a "\" I don't have to explain myself.\""
                hide 9newalex127
                show 9newalex128
                with dissolve
                a "\" Am I making sense?\""
                p "\" I think so.\""
                a "\" I don't want to... be weird, you know?\""
                p "\" Like you're being weird right now?\""
                hide 9newalex128
                show 9newalex129
                with dissolve
                " She gives you a chaste kiss."
                a "\" Now?\""
                p "\" Not weird.\""
                hide 9newalex129
                show 9newalex130
                with dissolve
                " Then she shoves her tongue in your mouth."
                p "\" Getting warmer...\""
                hide 9newalex130
                show 9newalex131
                with dissolve
                " She takes her shirt off."
                hide 9newalex131
                show 9newalex132
                with dissolve
                " And then climbs back on top of you."
                hide 9newalex132
                show 9newalex133
                with dissolve
                a "\" Weird?\""
                p "\" Not at all.\""
                hide 9newalex133
                show 9newalex134
                with dissolve
                " She whispers in your ear."
                a "\" My panties are soaked right now.\""
                p "\" That's the boredom talking?\""
                hide 9newalex134
                show 9newalex135
                with dissolve
                a "\" Hehehe.\""
                a "\" Maybe.\""
                hide 9newalex135
                show 9newalex136
                with dissolve
                a "\" Mmmm...\""
                a "\" So different.\""
                p "\" What?\""
                a "\" Your body is so different.\""
                a "\" Like a big slab of meat.\""
                p "\" Ok. Now it's weird.\""
                a "\" Hehe...\""
                hide 9newalex136
                show 9newalex137
                with dissolve
                a "\" Kind of like it, though.\""
                a "\" I could just fall asleep here.\""
                p "\" What about your back?\""
                a "\" It will be fine.\""
                a "\" I'm not an old woman.\""
                hide 9newalex137
                show 9newalex136
                with dissolve
                a "\" So warm too.\""
                a "\" Why is your skin so much warmer than mine?\""
                p "\" Better circulation?\""
                a "\" Maybe.\""
                hide 9newalex136
                show 9newalex138
                with dissolve
                " That's when Boris decides to walk in."
                b "\" Alexandra?\""
                hide 9newalex138
                show 9newalex139
                with dissolve
                " Nonchalantly, and with seemingly no worry in the world, she turns to look at him."
                a "\" Dad?\""
                a "\" Before you say anything, I'm not under your roof.\""
                b "\" Sigh...\""
                b "\" Your cousin is in the hospital.\""
                hide 9newalex139
                show 9newalex140
                with dissolve
                " She jumps up."
                a "\" What?\""
                a "\" Yuri?\""
                b "\" Put a shirt on, girl.\""
                a "\" Never mind my shirt.\""
                a "\" What about Yuri?\""
                b "\" He's going to be alright.\""
                b "\" But he's been severely beaten.\""
                a "\" I need to go see him.\""
                b "\" That's why I came.\""
                hide 9newalex140
                show 9newalex141
                with dissolve
                " She goes and finds Izzy."
                i "\" What's wrong?\""
                hide 9newalex141
                show 9newalex142
                with dissolve
                a "\" Are you and your mom going to be ok alone for a while?\""
                i "\" Yeah.\""
                i "\" Why, what happened?\""
                a "\" Yuri's in the hospital.\""
                i "\" What?\""
                a "\" We need to go see him.\""
                a "\" Are you going to be ok?\""
                i "\" Yeah. Sure.\""
                i "\" Don't you need me to come with you?\""
                a "\" No.\""
                a "\" I might need you later, though.\""
                i "\" I'll be here.\""
                hide 9newalex142
                show 9newalex143
                with dissolve
                a "\" [player_name], are you coming?\""
                p "\" Of course.\""
                hide 9newalex143
                show back1
                with dissolve
                show 9newalex144
                with dissolve
                " Once in the car, she asks..."
                a "\" What happened.\""
                hide 9newalex144
                show 9newalex145
                with dissolve
                b "\" Tanya's men were waiting outside the agency.\""
                b "\" Apparently they were hoping for [player_name].\""
                b "\" When he never showed, they settled on Yuri.\""
                hide 9newalex145
                show 9newalex146
                with dissolve
                a "\" So, they were targeting my Puppy?\""
                a "\" And when they couldn't get him, they took my cousin.\""
                hide 9newalex146
                show 9newalex145
                with dissolve
                b "\" They just beat him.\""
                b "\" I think they had more serious things in mind for [player_name].\""
                hide 9newalex145
                show 9newalex146
                with dissolve
                a "\" Breathe...\""
                a "\" Breathe, Alex. Breathe...\""
                hide 9newalex146
                show 9newalex147
                with dissolve
                " You get to the hospital, and find the room guarded by one of Boris' men."
                hide 9newalex147
                show 9newalex148
                with dissolve
                " And inside, an unconscious Yuri together with Narysa."
                hide 9newalex148
                show 9newalex149
                with dissolve
                p "\" Narysa?\""
                p "\" What are you doing here?\""
                nar "\" I brought him in.\""
                p "\" You were there?\""
                hide 9newalex149
                show 9newalex150
                with dissolve
                a "\" You poor boy.\""
                a "\" Yuri wouldn't hurt a fly.\""
                a "\" How could she do this to him?\""
                hide 9newalex150
                show 9newalex151
                with dissolve
                a "\" That BITCH!\""
                b "\" Language.\""
                hide 9newalex151
                show 9newalex152
                with dissolve
                nar "\" Yeah.\""
                nar "\" Me and him were the last to leave.\""
                nar "\" They were looking for you, you know.\""
                p "\" I heard.\""
                hide 9newalex152
                show 9newalex155
                with dissolve
                nar "\" Is this going to be big trouble?\""
                p "\" Nothing we can't handle.\""
                hide 9newalex155
                show 9newalex153
                with dissolve
                b "\" Yeah.\""
                b "\" This will definitely be handled.\""
                hide 9newalex153
                show 9newalex154
                with dissolve
                a "\" It's going to be ok, Yuri.\" You can hear her whisper."
                a "\" We're going to take good care of you.\""
                hide 9newalex154
                show 9newalex157
                with dissolve
                " She continues to caress his face while whispering reassurance."
                " But you can't help but notice that there isn't a tear in her eye."
                " Just a cold rage."
                if narysastart == True:
                    hide 9newalex157
                    show 9newalex158
                    with dissolve
                    " You can feel Narysa's hand caressing your leg."
                    nar "\" I'm glad it wasn't you.\""
                    p "\" What?\""
                    hide 9newalex158
                    show 9newalex159
                    with dissolve
                    nar "\" Yuri's a sweet guy, and I feel like shit for saying this.\""
                    nar "\" But I'm glad it wasn't you.\""
                    jump ep9cont8

                else:
                    jump ep9cont8

label ep9cont8:
                scene 9newalex160
                with dissolve
                a "\" Me and Izzy can do shifts.\""
                a "\" Someone should always be with him.\""
                b "\" You need to get back to the hotel.\""
                a "\" You really think I'm doing that, Dad?\""
                a "\" Just have someone that can drive us back and forth.\""
                b "\" I'm not sure the hospital will allow it.\""
                show 9newalex161
                with dissolve
                a "\" Then MAKE them allow it.\""
                a "\" I'm not leaving my cousin alone.\""
                hide 9newalex161
                show 9newalex162
                with dissolve
                a "\" [player_name], can I talk to you?\""
                p "\" Sure.\""
                a "\" Let's go to the hospital garden.\""
                hide 9newalex162
                show 9newalex153
                with dissolve
                b "\" Careful.\""
                a "\" Puppy's with me.\""
                hide 9newalex153
                show 9newalex163
                with dissolve
                " You follow her down the stairs."
                hide 9newalex163
                show 9newalex164
                with dissolve
                " And out to the garden."
                p "\" Alex?\""
                hide 9newalex164
                show 9newalex165
                with dissolve
                " She sits down on the bench."
                a "\" Fuck me.\""
                p "\" What's wrong?\""
                a "\" I'm not good for people.\""
                hide 9newalex165
                show 9newalex166
                with dissolve
                p "\" What do you mean?\""
                a "\" Everyone that I love gets fucked.\""
                a "\" Izzy is in hiding, you've been stabbed...\""
                a "\" And now my cousin too.\""
                p "\" You can't take that on yourself.\""
                hide 9newalex166
                show 9newalex168
                with dissolve
                a "\" I'm not sure.\""
                a "\" It's not like I'm doing it.\""
                a "\" But facts are facts...\""
                hide 9newalex168
                show 9newalex169
                with dissolve
                " You put your arm around her."
                p "\" Hey.\""
                p "\" Where's the lioness, huh?\""
                p "\" You need to be that cold bitch now, ok.\""
                a "\" Not be a burden, I get it.\""
                p "\" I didn't say that.\""
                a "\" You didn't have to.\""
                hide 9newalex169
                show 9newalex170
                with dissolve
                a "\" Don't worry about me.\""
                a "\" I may bend, but never break.\""
                a "\" That's not what I'm talking about.\""
                p "\" What, then.\""
                hide 9newalex170
                show 9newalex167
                with dissolve
                " She turns her head away."
                a "\" I'm going to do something vile.\""
                a "\" But I feel I owe it to you.\""
                p "\" Huh?\""
                a "\" I'll give you my cold bitch analysis.\""
                a "\"...\""
                a "\" Dad will go after that Tanya bitch hard after this.\""
                p "\" Probably.\""
                a "\" Spare her if you can.\""
                p "\" What?\""
                p "\" Is that what you want?\""
                a "\" I want her vitals on a bed of lettuce.\""
                a "\" But the smart move is to spare her if you can.\""
                hide 9newalex167
                show 9newalex168
                with dissolve
                a "\" If you can spare her. And with Dad after her blood...\""
                a "\" You'll be the only thing standing between her and doom.\""
                a "\" You'll be able to use that.\""
                a "\" Use her contacts, her money... her everything.\""
                p "\" I'm not sure I could spare her even if I want to.\""
                a "\" Maybe, maybe not.\""
                a "\" But that's the smart move.\""
                a "\" Use her for whatever she has today, and once she has nothing else to give, well...\""
                p "\" Is that what you want?\""
                a "\" I told you no.\""
                a "\" But that's the smart move, if you can pull it off.\""
                hide 9newalex168
                show 9newalex167
                with dissolve
                a "\" Damn, I feel like shit.\""
                p "\"...\""
                a "\" Let's get back inside.\""
                hide 9newalex167
                show 9newalex171
                with dissolve
                " She kisses your neck before you leave."
                hide 9newalex171
                show 9newalex172
                with dissolve
                " Back inside, she returns to doting on her cousin."
                hide 9newalex172
                show 9newalex183
                with dissolve
                " Hour after hour passes, as Boris' men keep searching the city for Tanya."
                hide 9newalex183
                show 9newalex153
                with dissolve
                p "\" Any news?\""
                b "\" Not yet.\""
                b "\" Don't worry.\""
                b "\" We'll find the bitch.\""
                " Ring... ring... ring..."
                hide 9newalex153
                show 9newalex173
                with dissolve
                p "\" Yeah?\""
                phil "\" Meet me in the garage.\""
                p "\" Who is this?\""
                phil "\" Don't be coy, numbnuts.\""
                phil "\" Meet me in the garage.\""
                hide 9newalex173
                show 9newalex174
                with dissolve
                p "\" I'll be right back.\""
                a "\" Poor Yuri.\""
                hide 9newalex174
                show 9newalex175
                with dissolve
                " You go down to the hospital garage."
                phil "\" Over here.\""
                hide 9newalex175
                show 9newalex176
                with dissolve
                p "\" Cop?\""
                phil "\" Scum?\""
                phil "\" I have some info that you want.\""
                phil "\" The location of a cunty blonde.\""
                p "\" Really.\""
                hide 9newalex176
                show 9newalex177
                with dissolve
                " He lights up a cigarette."
                phil "\" Really.\""
                p "\" And what do you want?\""
                p "\" Money?\""
                phil "\" Please...\""
                hide 9newalex177
                show 9newalex178
                with dissolve
                phil "\" One hand washes another, remember?\""
                p "\" You still haven't answered.\""
                phil "\" What does Emma have you doing?\""
                p "\" You know.\""
                phil "\" Why don't you tell me anyway.\""
                " Do you lie?"
                call screen screen48

label ep9false:
                scene 9newalex178
                with dissolve
                $ ep9phillie = True
                p "\" Buying cocaine.\""
                phil "\" I know that.\""
                p "\" Then why are you asking?\""
                phil "\" From whom?\""
                p "\" Some black guy upstate.\""
                p "\" Calls himself Humongous.\""
                show 9newalex180
                with dissolve
                phil "\" You're fucking with me.\""
                p "\" I swear.\""
                p "\" Calls himself Lord of something or other. I don't remember.\""
                phil "\" Never heard of him.\""
                p "\" Me neither.\""
                jump ep9cont9

label ep9truth:
                scene 9newalex178
                with dissolve
                p "\" Buying cocaine.\""
                phil "\" I know that.\""
                p "\" Then why are you asking?\""
                phil "\" From whom?\""
                p "\" Some guy named Marcello.\""
                hide 9newalex178
                show 9newalex180
                with dissolve
                phil "\" Marcello, huh?\""
                phil "\" Heard of him.\""
                phil "\" Good, this is good.\""
                jump ep9cont9

label ep9cont9:
                scene 9newalex179
                with dissolve
                " He hands you a piece of paper."
                phil "\" You can find the bitch here.\""
                phil "\" She's holed up with a couple of her boy toys.\""
                phil "\" Not much security.\""
                p "\" Really?\""
                show 9newalex182
                with dissolve
                phil "\" She's relying on secrecy.\""
                phil "\" A lot of guys would attract a lot of attention.\""
                phil "\" Besides, your boss can bring more. A lot more.\""
                phil "\" Her hope is to not be noticed.\""
                p "\" Thanks.\""
                phil "\" Talk to you next week.\""
                p "\" Why?\""
                phil "\" To tell me what else Emma has you doing.\""
                phil "\" This is a permanent thing from now on.\""
                phil "\" You'll tell me everything she's up to.\""
                hide 9newalex182
                show 9newalex183
                with dissolve
                " You head back upstairs."
                hide 9newalex183
                show 9newalex184
                with dissolve
                p "\" Still here?\""
                nar "\" Just waiting on Clara.\""
                nar "\" Should be here any minute.\""
                p "\" Clara.\""
                nar "\" She and Yuri are... close.\""
                p "\" If you say so.\""
                hide 9newalex184
                show 9newalex185
                with dissolve
                p "\" Boss?\""
                b "\" Huh?\""
                p "\" I think I got her.\""
                hide 9newalex185
                show 9newalex186
                with dissolve
                b "\" Who?\""
                p "\" Who we're looking for.\""
                b "\" Are you sure?\""
                p "\" I can't be sure.\""
                p "\" But I think so.\""
                hide 9newalex186
                show 9newalex188
                with dissolve
                " You could notice Alexandra was listening."
                hide 9newalex188
                show 9newalex187
                with dissolve
                b "\" Hmmm...\""
                b "\" Alright.\""
                b "\" You and me.\""
                b "\" Alex?\""
                hide 9newalex187
                show 9newalex189
                with dissolve
                a "\" What?\""
                b "\" Are you going to be ok for a few hours?\""
                a "\" Of course.\""
                b "\" Are you sure?\""
                hide 9newalex189
                show 9newalex191
                with dissolve
                a "\" Dad?\""
                a "\" I got this covered.\""
                a "\" You do what you have to do.\""
                hide 9newalex191
                show 9newalex192
                with dissolve
                a "\" I'll take care of Yuri, ok?\""
                b "\" Alright.\""
                hide 9newalex192
                show 9newalex186
                with dissolve
                b "\" Let's go.\""
                hide 9newalex186
                show 9newalex193
                with dissolve
                a "\" Good luck.\" She whispers as you leave."
                hide 9newalex193
                show 9newalex194
                with dissolve
                " On your way out, you run into Clara."
                hide 9newalex194
                show 9newalex195
                with dissolve
                cl "\" Yuri?\""
                p "\" That way.\""
                cl "\" Thanks.\""
                hide 9newalex195
                show 9newalex196
                with dissolve
                p "\"...\""
                b "\"...\""
                hide 9newalex196
                show 9newalex197
                with dissolve
                b "\" Must be more popular than I thought with those girls.\""
                p "\" Maybe he has that magic stick.\""
                b "\" Snigger.\""
                b "\" Shut up, and don't try to make me laugh.\""
                hide 9newalex197
                show back2
                with dissolve
                show 9newalex198
                with dissolve
                " You get in the car and go to the address."
                b "\" Now, tell me.\""
                b "\" How did you find out?\""
                " Do you tell the truth?"
                call screen screen49

label ep9borisfalse:
                scene back2
                with dissolve
                show 9newalex198
                with dissolve
                $ ep9borislie = True
                p "\" I have my ways.\""
                b "\" Keeping it close to the vest, eh?\""
                b "\" That's fine.\""
                b "\" As long as you're sure it's not a trap?\""
                p "\" That's why we're checking it out, right?\""
                jump ep9cont10

label ep9boristruth:
                scene back2
                with dissolve
                show 9newalex198
                with dissolve
                p "\" Dima's cop.\""
                b "\" Huh? What did he want?\""
                p "\" Just some info back.\""
                b "\" About me?\""
                p "\" Of course not.\""
                b "\" Huh.\""
                p "\" Just hope it's not a trap.\""
                b "\" We'll scope it out first, but I doubt it.\""
                b "\" From what I hear, he owes that bitch more than even us.\""
                b "\" This is one way to cancel your debts, I guess.\""
                jump ep9cont10

label ep9cont10:
                scene back2
                with dissolve
                show 9newalex199
                with dissolve
                " You finally get to the house."
                b "\" Do you see anything?\""
                hide 9newalex199
                show 9newalex200
                with dissolve
                p "\" Hmmm...\""
                p "\" Not really.\""
                hide 9newalex200
                show 9newalex202
                with dissolve
                p "\" Wait.\""
                p "\" Bedroom, second floor.\""
                hide 9newalex202
                show 9newalex201
                with dissolve
                b "\" My eyes aren't that good anymore.\""
                hide 9newalex201
                show 9newalex202
                with dissolve
                p "\" I think it's her.\""
                p "\" Yeah...\""
                p "\" I recognize the golden chains.\""
                hide 9newalex202
                show 9newalex199
                with dissolve
                b "\" There's also a car parked on the street.\""
                hide 9newalex199
                show 9newalex203
                with dissolve
                b "\" See it?\""
                b "\" There's someone inside.\""
                b "\" Must be her protection.\""
                p "\" Only that?\""
                hide 9newalex203
                show 9newalex199
                with dissolve
                b "\" Doesn't want to attract attention.\""
                b "\" Yeah.\""
                b "\" This is it.\""
                b "\" Let's go.\""
                p "\" What?\""
                p "\" Aren't we calling in more guys?\""
                p "\" For certain, you should not be part of this.\""
                hide 9newalex199
                show 9newalex201
                with dissolve
                b "\" Bitch put my nephew in the hospital.\""
                b "\" Went after my baby's man.\""
                b "\" Break her heart...\""
                b "\" Fucking cunt.\""
                b "\" Am I going alone, or are you coming.\""
                p "\" Sigh...\""
                p "\" There's a gun under the seat.\""
                b "\" I can't shoot for shit.\""
                hide 9newalex201
                show 9newalex204
                with dissolve
                " He searches through the glove compartment and comes up with a screwdriver."
                b "\" But I can use this.\""
                b "\" I can use this just fine.\""
                hide 9newalex204
                show 9newalex206
                with dissolve
                " Looking at the car, he says..."
                b "\" You wait here.\""
                b "\" I'll go set up on the other side.\""
                b "\" I got this.\""
                hide 9newalex206
                show 9newalex205
                with dissolve
                " Boris crosses the street and starts to slowly approach the car."
                hide 9newalex205
                show 9newalex206
                with dissolve
                " When he gets close, quick as a snake, he jumps into the driver's seat."
                hide 9newalex206
                show 9newalex207
                with dissolve
                " And emerges a few seconds later with a bloody face."
                p "\" You ok, boss?\""
                hide 9newalex207
                show 9newalex208
                with dissolve
                b "\" It's not mine.\""
                b "\" Let's go.\""
                hide 9newalex208
                show 9newalex209
                with dissolve
                " You scale the fence and approach the house."
                hide 9newalex209
                show 9newalex210
                with dissolve
                b "\" Here I come, twat!\""
                hide 9newalex210
                show 9newalex211
                with dissolve
                " Boris enters the house as if he owns it."
                " You can hear footsteps from the kitchen."
                " Sounds like bare feet."
                " He seems to hear you too."
                m8 "\" You followed me downstairs?\""
                m8 "\" Just going to get some beers.\""
                hide 9newalex211
                show 9newalex212
                with dissolve
                " He comes from behind the wall..."
                m8 "\" You're a real...\""
                hide 9newalex212
                show 9newalex213
                with dissolve
                m8 "\"...Cougar...\""
                hide 9newalex213
                show 9newalex214
                with dissolve
                m8 "\" Mhhh...\""
                " He gives a muffled moan as Boris stabs him."
                hide 9newalex214
                show 9newalex215
                with dissolve
                " And collapses on the floor."
                " Still breathing, but not able to speak due to the pain."
                hide 9newalex215
                show 9newalex216
                with dissolve
                " Without a word, Boris goes up the stairs."
                hide 9newalex216
                show 9newalex217
                with dissolve
                " You hear the sound of the shower coming from the bathroom."
                " And Boris is going straight for it."
                hide 9newalex217
                show 9newalex218
                with dissolve
                m5 "\" In a minute!\""
                hide 9newalex218
                show 9newalex219
                with dissolve
                m5 "\" I... I.. I...\""
                hide 9newalex219
                show 9newalex220
                with dissolve
                m5 "\" Listen...\""
                m5 "\" I'm just... I don't even...\""
                hide 9newalex220
                show 9newalex221
                with dissolve
                " After a very brief struggle, Boris, machine-like, continues on his way."
                hide 9newalex221
                show 9newalex222
                with dissolve
                ta "\" Hurry up!\""
                ta "\" Mommy wants some meat.\""
                hide 9newalex222
                show 9newalex223
                with dissolve
                ta "\" You boys sure like to keep a girl waiting.\""
                b "\" Hello!\""
                hide 9newalex223
                show 9newalex224
                with dissolve
                ta "\"...\""
                b "\" Yes?\""
                ta "\"...\""
                hide 9newalex224
                show 9newalex225
                with dissolve
                ta "\" AIIIIII!!!\""
                " Screaming, she bolts for the balcony."
                hide 9newalex225
                show 9newalex226
                with dissolve
                ta "\" NONONONONONONO...\""
                " But doesn't get very far until you catch her."
                hide 9newalex226
                show 9newalex227
                with dissolve
                " You pull her from the balcony and throw her on the bed."
                ta "\" No... no... no...!\""
                hide 9newalex227
                show 9newalex228
                with dissolve
                " And Boris gets on top of her."
                ta "\" No...\""
                ta "\" I'm sorry...\""
                ta "\" I...\""
                ta "\" I can...\""
                hide 9newalex228
                show 9newalex229
                with dissolve
                ta "\" I'll suck your dicks!\""
                ta "\" Both of you!\""
                p "\" Hehe.\" You can't help but chuckle."
                hide 9newalex229
                show 9newalex230
                with dissolve
                " He takes the screwdriver and puts it up her nose."
                b "\" I'll give you some penetration, cunt.\""
                " Do you say something?"
                call screen screen50

label ep9tanyano:
                scene 9newalex231
                with dissolve
                " Boris keeps pushing the screwdriver till her eyes roll over and she gives a snort."
                show 9newalex232
                with dissolve
                " By the time he gets off her, her body is limp."
                hide 9newalex232
                show 9newalex233
                with dissolve
                b "\" That's done.\""
                b "\" Come on. We need to take our clothes off while I call someone to clean this up.\""
                hide 9newalex233
                show 9newalex234
                with dissolve
                b "\" It's me.\""
                b "\" I'll text you an address.\""
                b "\" Come here with a few of your boys right away.\""
                b "\" Alright.\""
                hide 9newalex234
                show 9newalex233
                with dissolve
                b "\" What are you waiting for? Take your clothes off.\""
                hide 9newalex233
                show 9newalex235
                with dissolve
                " He starts to undress and throws his clothes in the bathtub with one of the men's bodies."
                hide 9newalex235
                show 9newalex236
                with dissolve
                b "\" Hurry up.\""
                hide 9newalex236
                show 9newalex237
                with dissolve
                " You follow suit."
                b "\" Let's go downstairs to get a beer.\""
                hide 9newalex237
                show 9newalex238
                with dissolve
                " On your way down, you pass the body of the first man."
                " You notice he's not breathing anymore."
                hide 9newalex238
                show 9newalex239
                with dissolve
                " You grab a couple of beers and sit on the couch."
                p "\" You should not have been here, boss.\""
                p "\" I could've handled this.\""
                hide 9newalex239
                show 9newalex240
                with dissolve
                b "\" I wanted to be here.\""
                b "\" And it's my call.\""
                hide 9newalex240
                show 9newalex243
                with dissolve
                b "\" I feel good about tonight.\""
                b "\" Yes.\""
                b "\" This was a good night.\""
                hide 9newalex243
                show 9newalex244
                with dissolve
                " In about thirty minutes, the men Boris sent for showed up."
                hide 9newalex244
                show 9newalex245
                with dissolve
                ant "\" Boss?\""
                b "\" Anton.\""
                hide 9newalex245
                show 9newalex246
                with dissolve
                ant "\" Beers in hand, half naked, and with the stench of sex in the air.\""
                ant "\" You got something you want to tell me, friend?\""
                hide 9newalex246
                show 9newalex247
                with dissolve
                b "\" Fuck off, and take care of this shit.\""
                b "\" And get us some clothes too.\""
                hide 9newalex247
                show 9newalex246
                with dissolve
                ant "\" I have some jeans and t-shirts in the car.\""
                ant "\" Now get out of here, and let me take care of this.\""
                jump ep9cont11

label ep9tanyayes:
                scene 9newalex230
                with dissolve
                $ ep9savetanya = True
                $ borispts = borispts + 4
                p "\" Boss!\""
                p "\" Boss, wait a minute.\""
                show 9newalex248
                with dissolve
                b "\" What?\""
                p "\" You could use her.\""
                p "\" You have her now.\""
                p "\" She's not getting away.\""
                p "\" If you want to take her head, you can do it just as easy an hour, a day, or week from now.\""
                p "\" Why not see if you can make use of her first?\""
                hide 9newalex248
                show 9newalex249
                with dissolve
                ta "\" Yes... yes...\""
                ta "\" I can help you.\""
                hide 9newalex249
                show 9newalex248
                with dissolve
                b "\" She would've killed you.\""
                p "\" And failed.\""
                b "\" What about my nephew?\""
                p "\" You can deliver her to him if he wants.\""
                hide 9newalex248
                show 9newalex250
                with dissolve
                " With visible effort, he manages to pull away from her."
                b "\" You belong to me now, you understand?\""
                ta "\" Yes... yes...\""
                b "\" I'll let you live as long as you can be useful.\""
                b "\" When you're not... or when this man here, or my nephew wants your head...\""
                ta "\" I'll be useful, you'll see!\""
                hide 9newalex250
                show 9newalex251
                with dissolve
                b "\" I hope so.\""
                b "\" You're living on borrowed time from now on.\""
                hide 9newalex251
                show 9newalex252
                with dissolve
                ta "\" Pant... pant.. pant...\""
                ta "\" Yes...\""
                hide 9newalex252
                show 9newalex253
                with dissolve
                b "\" Stay here till we come get you.\""
                b "\" Try to run, and I'm shoving this up your ass.\""
                hide 9newalex253
                show 9newalex233
                b "\" Come on. We need to take our clothes off while I call someone to clean this up.\""
                hide 9newalex233
                show 9newalex234
                with dissolve
                b "\" It's me.\""
                b "\" I'll text you an address.\""
                b "\" Come here with a few of your boys right away.\""
                b "\" Alright.\""
                hide 9newalex234
                show 9newalex233
                with dissolve
                b "\" What are you waiting for? Take your clothes off.\""
                hide 9newalex233
                show 9newalex255
                with dissolve
                ta "\" Thank you.\" She whispers."
                hide 9newalex255
                show 9newalex256
                with dissolve
                " You leave her on the bed, almost crying with relief."
                hide 9newalex256
                show 9newalex235
                with dissolve
                " He starts to undress and throws his clothes in the bathtub with one of the men's bodies."
                hide 9newalex235
                show 9newalex236
                with dissolve
                b "\" Hurry up.\""
                hide 9newalex236
                show 9newalex237
                with dissolve
                " You follow suit."
                b "\" Go get the bitch.\""
                b "\" Let's go downstairs to get a beer.\""
                hide 9newalex237
                show 9newalex238
                with dissolve
                " On your way down, you pass the body of the first man."
                " You notice he's not breathing anymore."
                hide 9newalex238
                show 9newalex256
                with dissolve
                ta "\" Poor boy...\""
                ta "\" He never hurt a soul.\""
                hide 9newalex256
                show 9newalex257
                with dissolve
                b "\" Go get my boy a beer, woman.\""
                ta "\" Right away.\""
                hide 9newalex257
                show 9newalex258
                with dissolve
                " She brings you the beer, and just sits on the couch not saying anything."
                hide 9newalex258
                show 9newalex242
                with dissolve
                " From time to time, she glances at the body of the boy on the floor."
                hide 9newalex242
                show 9newalex239
                with dissolve
                p "\" You should not have been here, boss.\""
                p "\" I could've handled this.\""
                hide 9newalex239
                show 9newalex240
                with dissolve
                b "\" I wanted to be here.\""
                b "\" And it's my call.\""
                hide 9newalex240
                show 9newalex241
                with dissolve
                b "\" Why did you ask me to stop?\""
                p "\" I said why.\""
                hide 9newalex241
                show 9newalex243
                with dissolve
                b "\" Cold rage.\""
                b "\" That's good if you can keep it.\""
                b "\" Have the malice of anger, but with a clear head.\""
                b "\" Hold on to that. It will make you formidable.\""
                hide 9newalex243
                show 9newalex244
                with dissolve
                " In about thirty minutes, the men Boris sent for showed up."
                hide 9newalex244
                show 9newalex259
                with dissolve
                ant "\" Boss?\""
                b "\" Anton.\""
                hide 9newalex259
                show 9newalex246
                with dissolve
                ant "\" Beers in hand, half naked, and with the stench of sex in the air.\""
                ant "\" You got something you want to tell me, friend?\""
                hide 9newalex246
                show 9newalex247
                with dissolve
                b "\" Fuck off, and take care of this shit.\""
                b "\" And get us some clothes too.\""
                hide 9newalex247
                show 9newalex259
                with dissolve
                ant "\" I have some jeans and t-shirts in the car.\""
                ant "\" Now get out of here, and let me take care of this.\""
                hide 9newalex259
                show 9newalex260
                with dissolve
                ant "\" Mrs. Tanya?\""
                ant "\" You'll have to come with me.\""
                ta "\" I understand.\""
                jump ep9cont11

label ep9cont11:
                scene back2
                with dissolve
                show 9newalex261
                with dissolve
                " After changing, you and Boris head back to the hospital."
                hide 9newalex261
                show 9newalex262
                with dissolve
                " When you arrive, Alex is gone, and Izzy is there."
                hide 9newalex262
                show 9newalex263
                with dissolve
                b "\" What are you doing here, sweetheart?\""
                i "\" My shift.\""
                b "\" Alex is serious about this?\""
                b "\" Don't worry about it.\""
                b "\" I'll stay.\""
                hide 9newalex263
                show 9newalex264
                with dissolve
                i "\" Least I can do.\""
                i "\" You've always treated us like family.\""
                hide 9newalex264
                show 9newalex263
                with dissolve
                i "\" I have to ask.\""
                i "\" How long do you think this will last?\""
                b "\" It's over.\""
                i "\" Really?\""
                b "\" You can go home tomorrow.\""
                hide 9newalex263
                show 9newalex265
                with dissolve
                b "\" Better get to the hotel.\" He says to you."
                b "\" Go get some sleep.\""
                p "\" The hotel?\""
                p "\" Not home?\""
                b "\" Kiss Alex for me.\""
                b "\" And tell her it's over.\""
                p "\" Alright.\""
                hide 9newalex265
                show 9newalex266
                with dissolve
                " You get back to the hotel."
                p "\" Alex?\""
                hide 9newalex266
                show 9newalex267
                with dissolve
                a "\" [player_name]?\""
                a "\" I was just about to take a bath.\""
                p "\" It's over.\""
                hide 9newalex267
                show 9newalex268
                with dissolve
                a "\" Your clothes are different.\""
                p "\" I thought you were never going to ask about that.\""
                a "\" I doubt it's because your old clothes are on some girl's floor.\""
                hide 9newalex268
                show 9newalex269
                with dissolve
                a "\" Was it horrible?\""
                a "\" Do you want to talk about it?\""
                hide 9newalex269
                show 9newalex270
                with dissolve
                p "\" I'm fine.\""
                p "\" I've seen worse.\""
                p "\" Besides. I don't want to make you an accessory.\""
                hide 9newalex270
                show 9newalex269
                with dissolve
                a "\" I'm already an accessory.\""
                a "\" And you can tell me.\""
                hide 9newalex269
                show 9newalex270
                with dissolve
                p "\" I don't.\""
                p "\" Just to tell you that it's over.\""
                hide 9newalex270
                show 9newalex271
                with dissolve
                a "\" Up to you.\""
                a "\" Come on.\""
                a "\" Let me take care of you.\""
                hide 9newalex271
                show 9newalex272
                with dissolve
                " She takes you by the arm and pulls you to the bathroom."
                hide 9newalex272
                show 9newalex273
                with dissolve
                p "\" Big bathroom.\""
                hide 9newalex273
                show 9newalex274
                with dissolve
                a "\" I was just pouring a bath.\""
                a "\" How do you like it?\""
                a "\" Warmer? Colder?\""
                p "\" Warmer.\""
                hide 9newalex274
                show 9newalex278
                with dissolve
                " She adjusts the knobs and tests the water with her legs."
                a "\" Seems good.\""
                hide 9newalex278
                show 9newalex275
                with dissolve
                a "\" Now, let's get you out of those clothes.\""
                hide 9newalex275
                show 9newalex276
                with dissolve
                " She gently helps you undress, and throws your clothes aside."
                hide 9newalex276
                show 9newalex277
                with dissolve
                " Then kisses your back."
                a "\" In you go.\""
                hide 9newalex277
                show 9newalex279
                with dissolve
                a "\" Come on.\""
                a "\" Let me wash you.\""
                hide 9newalex279
                show 9newalex280
                with dissolve
                " You get in the tub, and she wraps her legs around your shoulders."
                " Then starts washing you."
                hide 9newalex280
                show 9newalex281
                with dissolve
                a "\" Are you sure you don't want to unburden yourself?\""
                p "\" Yeah.\""
                hide 9newalex281
                show 9newalex282
                with dissolve
                a "\" Were you in danger?\""
                p "\" Me?\""
                p "\" Not really.\""
                hide 9newalex282
                show 9newalex283
                with dissolve
                " She kisses you again."
                a "\" You wouldn't lie to me about that, would you?\""
                p "\" No.\""
                hide 9newalex283
                show 9newalex284
                with dissolve
                a "\" Hungry?\""
                p "\" No.\""
                a "\" Then let's get you out of this water, and give you a massage.\""
                hide 9newalex284
                show 9newalex285
                with dissolve
                a "\" Come on.\""
                hide 9newalex285
                show 9newalex286
                with dissolve
                " She towels you down."
                p "\" Massage, huh?\""
                a "\" I actually took a class.\""
                hide 9newalex286
                show 9newalex287
                with dissolve
                a "\" You seem like you have a cloud above you.\""
                hide 9newalex287
                show 9newalex288
                with dissolve
                " She kisses your beard."
                p "\" Hehe.\""
                hide 9newalex288
                show 9newalex289
                a "\" Finally. A smile.\""
                p "\" Depends on where you kiss me.\""
                a "\" We'll get to that.\""
                hide 9newalex289
                show 9newalex290
                with dissolve
                " She takes you back to the room."
                hide 9newalex290
                show 9newalex291
                with dissolve
                " Then throws the cover off the bed."
                hide 9newalex291
                show 9newalex292
                with dissolve
                a "\" Come here.\""
                a "\" On the bed.\""
                a "\" Face down.\""
                hide 9newalex292
                show 9newalex293
                with dissolve
                " You get on the bed."
                a "\" Relax.\""
                a "\" You're resting on your hands.\""
                hide 9newalex293
                show 9newalex294
                with dissolve
                a "\" Rest on your belly.\""
                hide 9newalex294
                show 9newalex295
                with dissolve
                " And she pushes you down."
                hide 9newalex295
                show 9newalex296
                with dissolve
                a "\" I don't have any oil, but we'll make due.\""
                hide 9newalex296
                show 9newalex297
                with dissolve
                " She lies down on top of you, and you can feel her nipples harden at the touch of your skin."
                hide 9newalex297
                show 9newalex298
                with dissolve
                a "\" We're in a unique moment in time.\" She whispers."
                a "\" This moment will never occur again.\""
                a "\" We'll never again be here, at this time.\""
                hide 9newalex298
                show 9newalex299
                with dissolve
                " She starts caressing your ribs."
                hide 9newalex299
                show 9newalex300
                with dissolve
                a "\" There's a yesterday and there will be a tomorrow.\" She says kissing your ear."
                a "\" But between, there's an eternity.\""
                a "\" Of just us.\""
                a "\" In this room.\""
                hide 9newalex300
                show 9newalex301
                with dissolve
                " She starts massaging your back."
                " Slowly... gently...."
                " Till you're almost asleep."
                hide 9newalex301
                show 9newalex302
                with dissolve
                " Then she pushes her elbow into you."
                hide 9newalex302
                show 9newalex303
                with dissolve
                p "\" Ouch.\""
                hide 9newalex303
                show 9newalex304
                with dissolve
                a "\" Don't be a pussy.\""
                a "\" I need to get in there.\""
                a "\" It will feel great at the end. Trust me.\""
                hide 9newalex304
                show 9newalex302
                with dissolve
                " She continues to abuse your body to her satisfaction."
                hide 9newalex302
                show 9newalex305
                with dissolve
                " When she's done, she tells you to turn around."
                a "\" Better?\""
                p "\" Actually, yes.\""
                hide 9newalex305
                show 9newalex306
                with dissolve
                a "\" Close your eyes.\" She says caressing you again."
                hide 9newalex306
                show 9newalex307
                with dissolve
                " She presses herself against you."
                " Her ass wiggling in your hands."
                hide 9newalex307
                show 9newalex308
                with dissolve
                a "\" Do you want me?\""
                p "\" Want you?\""
                a "\" Yes?\""
                p "\" What about the beach? The thing.\""
                a "\" We're still doing that. Don't worry.\""
                a "\" But you need this more than I need the beach.\""
                hide 9newalex308
                show 9newalex309
                with dissolve
                a "\" I'll take care of you, Puppy.\""
                a "\" Like you take care of me.\""
                hide 9newalex309
                show 9newalex313
                with dissolve
                " She gets up and takes her shorts off."
                hide 9newalex313
                show 9newalex314
                with dissolve
                " Then climbs on top of you."
                a "\" Ok... ok...\""
                a "\" Let's figure this out.\""
                a "\" Can you sit up a bit?\""
                hide 9newalex314
                show 9newalex315
                with dissolve
                a "\" Yeah.\""
                a "\" Better.\""
                hide 9newalex315
                show 9newalex316
                with dissolve
                " You feel her pussy resting on your dick."
                " And you can feel her getting wetter as she rubs against it."
                hide 9newalex316
                show 9newalex317
                with dissolve
                a "\" This is a bit of terra incognita for me, ok?\""
                a "\" So, grade me on a curve.\""
                p "\" Hehe.\""
                scene alexsex1 animated with fade:
                    "10a1.webp"
                    pause 0.05
                    "10a2.webp"
                    pause 0.05
                    "10a3.webp"
                    pause 0.05
                    "10a4.webp"
                    pause 0.05
                    "10a5.webp"
                    pause 0.05
                    "10a6.webp"
                    pause 0.05
                    "10a7.webp"
                    pause 0.05
                    "10a8.webp"
                    pause 0.05
                    "10a9.webp"
                    pause 0.05
                    "10a10.webp"
                    pause 0.05
                    "10a11.webp"
                    pause 0.05
                    "10a12.webp"
                    pause 0.05
                    "10a13.webp"
                    pause 0.05
                    "10a14.webp"
                    pause 0.05
                    "10a15.webp"
                    pause 0.05
                    "10a16.webp"
                    pause 0.05
                    "10a17.webp"
                    pause 0.05
                    "10a18.webp"
                    pause 0.05
                    "10a19.webp"
                    pause 0.05
                    "10a20.webp"
                    pause 0.05
                    "10a21.webp"
                    pause 0.05
                    "10a22.webp"
                    pause 0.05
                    "10a23.webp"
                    pause 0.05
                    "10a24.webp"
                    pause 0.05
                    "10a25.webp"
                    pause 0.05
                    "10a26.webp"
                    pause 0.05
                    "10a27.webp"
                    pause 0.05
                    "10a28.webp"
                    pause 0.05
                    "10a29.webp"
                    pause 0.05
                    "10a30.webp"
                    pause 0.05
                    repeat
                a "\" Ok...\""
                " She starts grinding on your dick somewhat inexpertly."
                " But her ever wetter pussy and the feel of her juices dripping down your shaft does the job anyway."
                $ renpy.pause ()
                show 9newalex318
                with dissolve
                " She continues to kiss when she stops."
                hide 9newalex318
                show 9newalex319
                with dissolve
                a "\" Love ya, Pupster.\""
                p "\" Love you too.\""
                a "\" I know.\""
                hide 9newalex319
                show 9newalex320
                with dissolve
                " She grabs a hold of your dick."
                hide 9newalex320
                show 9newalex321
                with dissolve
                a "\" Ok...\""
                a "\" There... we...\""
                hide 9newalex321
                show 9newalex322
                with dissolve
                a "\" Go...\""
                a "\" Ouch!\""
                scene alexsex1 animated with fade:
                    "11a1.webp"
                    pause 0.05
                    "11a2.webp"
                    pause 0.05
                    "11a3.webp"
                    pause 0.05
                    "11a4.webp"
                    pause 0.05
                    "11a5.webp"
                    pause 0.05
                    "11a6.webp"
                    pause 0.05
                    "11a7.webp"
                    pause 0.05
                    "11a8.webp"
                    pause 0.05
                    "11a9.webp"
                    pause 0.05
                    "11a10.webp"
                    pause 0.05
                    "11a11.webp"
                    pause 0.05
                    "11a12.webp"
                    pause 0.05
                    "11a13.webp"
                    pause 0.05
                    "11a14.webp"
                    pause 0.05
                    "11a15.webp"
                    pause 0.05
                    "11a16.webp"
                    pause 0.05
                    "11a17.webp"
                    pause 0.05
                    "11a18.webp"
                    pause 0.05
                    "11a19.webp"
                    pause 0.05
                    "11a20.webp"
                    pause 0.05
                    "11a21.webp"
                    pause 0.05
                    "11a22.webp"
                    pause 0.05
                    "11a23.webp"
                    pause 0.05
                    "11a24.webp"
                    pause 0.05
                    "11a25.webp"
                    pause 0.05
                    "11a26.webp"
                    pause 0.05
                    "11a27.webp"
                    pause 0.05
                    "11a28.webp"
                    pause 0.05
                    "11a29.webp"
                    pause 0.05
                    "11a30.webp"
                    pause 0.05
                    repeat
                a "\" Ok...\""
                a "\" Yeah...\""
                a "\" Oh... that's...\""
                a "\" Ouch...\""
                $ renpy.pause ()
                show 9newalex323
                with dissolve
                p "\" Are you ok?\""
                a "\" Yeah.\""
                a "\" Just so different...\""
                " But you could see winces of pain on her face."
                scene alexsex1 animated with fade:
                    "11a1.webp"
                    pause 0.05
                    "11a2.webp"
                    pause 0.05
                    "11a3.webp"
                    pause 0.05
                    "11a4.webp"
                    pause 0.05
                    "11a5.webp"
                    pause 0.05
                    "11a6.webp"
                    pause 0.05
                    "11a7.webp"
                    pause 0.05
                    "11a8.webp"
                    pause 0.05
                    "11a9.webp"
                    pause 0.05
                    "11a10.webp"
                    pause 0.05
                    "11a11.webp"
                    pause 0.05
                    "11a12.webp"
                    pause 0.05
                    "11a13.webp"
                    pause 0.05
                    "11a14.webp"
                    pause 0.05
                    "11a15.webp"
                    pause 0.05
                    "11a16.webp"
                    pause 0.05
                    "11a17.webp"
                    pause 0.05
                    "11a18.webp"
                    pause 0.05
                    "11a19.webp"
                    pause 0.05
                    "11a20.webp"
                    pause 0.05
                    "11a21.webp"
                    pause 0.05
                    "11a22.webp"
                    pause 0.05
                    "11a23.webp"
                    pause 0.05
                    "11a24.webp"
                    pause 0.05
                    "11a25.webp"
                    pause 0.05
                    "11a26.webp"
                    pause 0.05
                    "11a27.webp"
                    pause 0.05
                    "11a28.webp"
                    pause 0.05
                    "11a29.webp"
                    pause 0.05
                    "11a30.webp"
                    pause 0.05
                    repeat
                a "\" Oh...\""
                a "\" Ok...\""
                a "\" There...\""
                a "\" That's...\""
                $ renpy.pause ()
                show 9newalex324
                with dissolve
                " But in no time, her winces of pain and little yelps began to be replaced by smiles and soft moans."
                scene alexsex1 animated with fade:
                    "11a1.webp"
                    pause 0.03
                    "11a2.webp"
                    pause 0.03
                    "11a3.webp"
                    pause 0.03
                    "11a4.webp"
                    pause 0.03
                    "11a5.webp"
                    pause 0.03
                    "11a6.webp"
                    pause 0.03
                    "11a7.webp"
                    pause 0.03
                    "11a8.webp"
                    pause 0.03
                    "11a9.webp"
                    pause 0.03
                    "11a10.webp"
                    pause 0.03
                    "11a11.webp"
                    pause 0.03
                    "11a12.webp"
                    pause 0.03
                    "11a13.webp"
                    pause 0.03
                    "11a14.webp"
                    pause 0.03
                    "11a15.webp"
                    pause 0.03
                    "11a16.webp"
                    pause 0.03
                    "11a17.webp"
                    pause 0.03
                    "11a18.webp"
                    pause 0.03
                    "11a19.webp"
                    pause 0.03
                    "11a20.webp"
                    pause 0.03
                    "11a21.webp"
                    pause 0.03
                    "11a22.webp"
                    pause 0.03
                    "11a23.webp"
                    pause 0.03
                    "11a24.webp"
                    pause 0.03
                    "11a25.webp"
                    pause 0.03
                    "11a26.webp"
                    pause 0.03
                    "11a27.webp"
                    pause 0.03
                    "11a28.webp"
                    pause 0.03
                    "11a29.webp"
                    pause 0.03
                    "11a30.webp"
                    pause 0.03
                    repeat
                " She increased her speed with her new found pleasure."
                " And as her pleasure mounted, so did yours."
                " Tilll..."
                $ renpy.pause ()
                show 9newalex326
                with dissolve
                " You grab and hold her close as you cum."
                p "\" Groan...\""
                a "\" What...\""
                a "\" Oh... that...\""
                a "\" Warm...\""
                show 9newalex327
                with dissolve
                " You slump back down and she follows."
                p "\" Did you...\""
                a "\" A little one.\""
                a "\" I'm not used to it, Puppy. It hurts.\""
                p "\" Sorry.\""
                a "\" It got good near the end there.\""
                hide 9newalex327
                show 9newalex328
                with dissolve
                a "\" Don't worry.\""
                a "\" I'll make you eat me till you get lockjaw.\""
                a "\" Tear your hair out as I cum.\""
                p "\" Really.\""
                a "\" Hehe. Maybe not tear your hair.\""
                hide 9newalex328
                show 9newalex329
                with dissolve
                a "\" Let's just remember to stop by the pharmacy when you drive me back to the hospital.\""
                a "\" Get one of those pill things.\""
                p "\" You're not on anything?\""
                a "\" For whom?\""
                a "\" Izzy?\""
                a "\" If she could get me pregnant, it would've happened already, trust me.\""
                a "\" But don't think about that now.\""
                a "\" Just sleep...\""
                a "\" Sleep... Puppy...\""
                a "\" Sleep...\""
                $ renpy.end_replay()
                jump ep10
