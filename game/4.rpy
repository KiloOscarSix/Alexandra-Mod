label ep4:
                default izzyin = False
                default izzycaress = False
                default izzyaccept3 = False
                default jennycomp1 = False
                default jennydinner = False
                default dannyaskdate1 = False
                scene 3newalex304
                with dissolve
                p "\" What will it cost me?\""
                jen "\" I'm not sure yet. But they don't come cheap.\""
                show 4newalex1
                with dissolve
                jen "\" Listen, I'll ask around.\""
                jen "\" Maybe I can come up with something.\""
                p "\" I'd appreciate that. Happy to pay too.\""
                jen "\" Oh, you'll pay. And maybe someday you can do me a favor in return.\""
                p "\" Done.\""
                hide 4newalex1
                show back1
                with dissolve
                show 4newalex2
                with dissolve
                " You leave Jenny and head back to work."
                " Until you hear sirens behind your car."
                hide 4newalex2
                show 4newalex3
                with dissolve
                " You pull over."
                p "\" Damn it!\""
                p "\" What the hell did I do?\""
                hide 4newalex3
                show back
                show 4newalex4
                with dissolve
                " An officer leaves the cop car, and enters your passenger seat."
                phil "\" You're not hard to track down.\""
                phil "\" Should be more careful about that.\""
                p "\" It's you.\""
                phil "\" This time.\""
                phil "\" I found your boys. The ones you're looking for.\""
                p "\" The ones that came to the agency?\""
                phil "\" Yes.\""
                phil "\" Meet me tonight. I'll show them to you.\""
                p "\" Where?\""
                phil "\" Where we usually meet.\""
                phil "\" See you then.\""
                hide 4newalex4
                show 4newalex2
                with dissolve
                p "\" How the fuck did he find me while I was driving?\""
                p "\" Damn!\""
                " You head back to the office."
                hide 4newalex2
                show 4newalex5
                with dissolve
                yuri "\" I see.\""
                cl "\" That's when I moved here.\""
                " These two seem closer and closer."
                p "\" Ahem!\""
                hide 4newalex5
                show 4newalex6
                with dissolve
                yuri "\" Hey chief.\""
                yuri "\" Wasn't expecting you so soon.\""
                p "\" What's there to do around here?\""
                yuri "\" You can do whatever you want I guess.\""
                hide 4newalex6
                show 4newalex7
                with dissolve
                " Not having much to do, you spend your workday with Narysa until it's time to go pick up Alexandra."
                hide 4newalex7
                show back1
                with dissolve
                show 4newalex8
                with dissolve
                a "\" Hey Puppy?\""
                a "\" Got a table for tonight?\""
                p "\" Table?\""
                a "\" For our dinner? Remember?\""
                p "\" About that...\""
                hide 4newalex8
                show 4newalex9
                with dissolve
                a "\" He's gonna come up with an excuse now, just watch.\""
                i "\" Maybe he's not in the mood.\""
                hide 4newalex9
                show 4newalex10
                with dissolve
                a "\" Alright, let us hear it.\""
                a "\" What's the problem.\""
                p "\" I have to work tonight.\""
                hide 4newalex10
                show 4newalex11
                with dissolve
                a "\" Work?\""
                a "\" Well, that's disappointing?\""
                p "\" Just have to take care of a few things.\""
                a "\" Hmmm...\""
                hide 4newalex11
                show 4newalex12
                with dissolve
                " You take the girls to Izzy's."
                a "\" So, you'll be out there working. While we'll be in here having sex.\""
                a "\" Fine, if that's what you want.\""
                i "\" That's mean of you Alex.\""
                hide 4newalex12
                show 4newalex13
                with dissolve
                " Alex grabs Isabella's breasts."
                a "\" The two of us here... Alone...\""
                a "\" Fingering ourselves just out of boredom.\""
                i "\" He he...\""
                a "\" But hey! Puppy has to go to work.\""
                a "\" It's nice to see he has his priorities straight.\""
                hide 4newalex13
                show 4newalex14
                with dissolve
                a "\" Isn't that so Puppy?\""
                a "\" You'd rather spend your evenings with a bunch of fat mobsters, than with us.\""
                p "\" You're being cruel right now.\""
                a "\" Hey, if that's what you want to do, that's what you want to do.\""
                a "\" We'll just be here monkey-fucking.\""
                hide 4newalex14
                show 4newalex15
                with dissolve
                " Izzy manages to disentangle herself from Alexandra's embrace."
                i "\" Don't listen to her.\""
                i "\" She's just teasing.\""
                i "\" We'll probably just have dinner and watch a movie.\""
                hide 4newalex15
                show 4newalex16
                with dissolve
                a "\" Right. Eating pussy and a porn.\""
                a "\" That's what I said.\""
                p "\" You're just twisting the knife now.\""
                a "\" If you say so.\""
                if izzyaccept == True or izzyaccept1 == True or izzyaccept2 == True:
                    hide 4newalex16
                    show 4newalex18
                    with dissolve
                    i "\" You're coming here when you're done, right?\""
                    p "\" It might be quite late. I don't want to wake you.\""
                    i "\" Don't be ridiculous.\""
                    hide 4newalex18
                    show 4newalex17
                    with dissolve
                    i "\" I have a spare set of keys in my room.\""
                    i "\" I'll go get them.\""
                    " She scurries off."
                    hide 4newalex17
                    show 4newalex19
                    with dissolve
                    a "\" She's giving you her keys?\""
                    a "\" Hmmm...\""
                    p "\" What?\""
                    a "\" I don't even have that.\""
                    p "\" Jealous?\""
                    a "\" If I'm honest...\""
                    hide 4newalex19
                    show 4newalex20
                    with dissolve
                    a "\" Now what's this thing that you have to do?\""
                    p "\" There were these guys that visited the agency before.\""
                    p "\" That cop friend of Dima's found them.\""
                    p "\" I need to pay them a visit.\""
                    hide 4newalex20
                    show 4newalex21
                    with dissolve
                    a "\" Just you?\""
                    a "\" Maybe you should bring Dima along.\""
                    p "\" I can't order him around.\""
                    p "\" Besides. I can't go to him every time something needs done.\""
                    hide 4newalex21
                    show 4newalex19
                    with dissolve
                    a "\" You will be careful though?\""
                    p "\" What do you mean?\""
                    hide 4newalex19
                    show 4newalex22
                    with dissolve
                    a "\" I know you like to walk around like you're invincible, but it's not true.\""
                    a "\" Maybe you should get a couple of muscle-heads to hang around with you.\""
                    p "\" I'm fine.\""
                    hide 4newalex22
                    show 4newalex23
                    with dissolve
                    " She gives you a kiss."
                    hide 4newalex23
                    show 4newalex24
                    with dissolve
                    a "\" Just don't be stupid, ok?\""
                    p "\" Ok.\""
                    a "\" I mean it this time. It's not a joke.\""
                    p "\" I understand.\""
                    hide 4newalex24
                    show 4newalex25
                    with dissolve
                    i "\" Found them!\""
                    hide 4newalex25
                    show 4newalex26
                    with dissolve
                    " She takes them, and places them in your hand."
                    hide 4newalex26
                    show 4newalex27
                    with dissolve
                    " You get the feeling this means a lot to her."
                    i "\" Just don't wake up Momma.\""
                    p "\" Of course.\""
                    i "\" We'll be in my bedroom.\""
                    hide 4newalex27
                    show 4newalex28
                    with dissolve
                    a "\" Right.\""
                    a "\" Exhausted from all the fucking.\""
                    i "\" Stop it.\""
                    hide 4newalex28
                    show 4newalex29
                    with dissolve
                    p "\" See you girls later.\""
                    i "\" Later.\""
                    a "\" Remember what I said.\""
                    p "\" The fucking part? Or the other one?\""
                    a "\" Don't be stupid.\""
                    p "\" Alright.\""
                    jump ep4cont1

                else:
                    hide 4newalex16
                    show 4newalex29
                    with dissolve
                    a "\" You're coming back here after?\""
                    i "\" What if he wakes up Momma?\""
                    a "\" Good point.\""
                    a "\" See you tomorrow?\""
                    p "\" Yeah.\""
                    hide 4newalex29
                    show 4newalex17
                    with dissolve
                    i "\" I'm going to go take a shower.\""
                    p "\" Bye.\""
                    i "\" Bye.\""
                    hide 4newalex17
                    show 4newalex20
                    with dissolve
                    a "\" Now what's this thing that you have to do?\""
                    p "\" There were these guys that visited the agency before.\""
                    p "\" That cop friend of Dima's found them.\""
                    p "\" I need to pay them a visit.\""
                    hide 4newalex20
                    show 4newalex21
                    with dissolve
                    a "\" Just you?\""
                    a "\" Maybe you should bring Dima along.\""
                    p "\" I can't order him around.\""
                    p "\" Besides. I can't go to him every time something needs done.\""
                    hide 4newalex21
                    show 4newalex19
                    with dissolve
                    a "\" You will be careful though?\""
                    p "\" What do you mean?\""
                    hide 4newalex19
                    show 4newalex22
                    with dissolve
                    a "\" I know you like to walk around like you're invincible, but it's not true.\""
                    a "\" Maybe you should get a couple of muscle-heads to hang around with you.\""
                    p "\" I'm fine.\""
                    hide 4newalex22
                    show 4newalex23
                    with dissolve
                    " She gives you a kiss."
                    hide 4newalex23
                    show 4newalex24
                    with dissolve
                    a "\" Just don't be stupid, ok?\""
                    p "\" Ok.\""
                    a "\" I mean it this time. It's not a joke.\""
                    p "\" I understand.\""
                    hide 4newalex24
                    show 4newalex23
                    with dissolve
                    " She kisses you again."
                    a "\" Bye.\""
                    p "\" Bye.\""
                    jump ep4cont1

label ep4cont1:
                scene 4newalex32
                with dissolve
                " You head  over to meet the cop."
                phil "\" You're late.\""
                p "\" Five minutes.\""
                phil "\" Don't do that again.\""
                phil "\" Let's go.\""
                show back1
                with dissolve
                show 4newalex33
                with dissolve
                " You both head to the car, and he gives you the address of a bar."
                phil "\" Go there.\""
                phil "\" These guys are not a big crew, but they're not locals.\""
                phil "\" So there's only so much I can tell you about them.\""
                p "\" Don't worry about it.\""
                hide 4newalex33
                show 4newalex34
                with dissolve
                phil "\" Be careful what you do!\""
                phil "\" I'm only willing to look the other way just so much.\""
                p "\" Understood.\""
                hide 4newalex34
                show 4newalex31
                with dissolve
                " Eventually you arrive at the bar."
                hide 4newalex31
                show 4newalex35
                with dissolve
                phil "\" You see the guy at the bar?\""
                phil "\" The bald one?\""
                hide 4newalex35
                show 4newalex31
                with dissolve
                p "\" The guy with the lumberjack shirt?\""
                phil "\" Yeah.\""
                hide 4newalex31
                show 4newalex35
                with dissolve
                phil "\" He's the chief of that crew.\""
                p "\" How many of them are there?\""
                phil "\" Four.\""
                p "\" And where are the rest?\""
                phil "\" I don't know. Holed up somewhere.\""
                phil "\" Just follow this little mouse. He'll take you to the rest.\""
                p "\" Ok.\""
                hide 4newalex35
                show 4newalex36
                with dissolve
                " You take another good look at the guy."
                phil "\" There best be more of you when you confront them.\""
                p "\" I'll just follow him for now.\""
                phil "\" We'll be in touch.\""
                hide 4newalex36
                show 4newalex37
                with dissolve
                " You head back to the car, to wait for the guy to come out."
                hide 4newalex37
                show 4newalex38
                with dissolve
                p "\" Christ, this might take forever.\""
                p "\" Even without the fucking, sleeping in a warm bed next to the girls sounds good right now.\""
                p "\" What if the guy's a drunk, and he doesn't leave 'til morning?\""
                p "\" Fuck my life.\""
                hide 4newalex38
                show 4newalex37
                with dissolve
                " The hours pass while you wait for the guy."
                hide 4newalex37
                show 4newalex39
                with dissolve
                " Until he finally does."
                p "\" Thank fuck!\""
                p "\" Better see where he goes.\""
                hide 4newalex39
                show 4newalex40
                with dissolve
                " You get out of the car, and start following on foot."
                hide 4newalex40
                show 4newalex41
                with dissolve
                " Until he disappears."
                p "\" The fuck?\""
                p "\" Where did he go?\""
                p "\" Down that alley?\""
                hide 4newalex41
                show 4newalex42
                with dissolve
                p "\" Where the fuck is he?\""
                hide 4newalex42
                show 4newalex43
                with dissolve
                guy "\" There you are!\""
                guy "\" Think I can't spot you stupid?\""
                hide 4newalex43
                show 4newalex44
                with dissolve
                " He charges into you."
                p "\" Ugh!\""
                hide 4newalex44
                show 4newalex45
                with dissolve
                " He takes you by surprise, but soon you manage to put up a defense."
                hide 4newalex45
                show 4newalex46
                with dissolve
                guy "\" Ohhhh... More skillful than I thought.\""
                guy "\" Won't help you, though.\""
                " You hear the sound of metal on leather."
                hide 4newalex46
                show 4newalex47
                with dissolve
                " You look towards the source of the sound, and see a dagger in the guy's hand."
                p "\" Shit!\""
                " You bring your left hand down to defend yourself."
                hide 4newalex47
                show 4newalex48
                with dissolve
                " And the knife passes through your palm like it's a magic trick."
                p "\" Grrrr....\""
                guy "\" Hehe....\""
                " Lances of pain flash up your arm."
                " You never knew there was such agony in the world..."
                hide 4newalex48
                show 4newalex49
                with dissolve
                guy "\" Don't fight it.\""
                guy "\" Don't fight it. Just let it happen.\""
                " You feel yourself growing weaker."
                hide 4newalex49
                show 4newalex50
                with dissolve
                " And then stronger."
                " Fish hooks tug on your cheeks till your face approaches something like a grin."
                guy "\" What the fuck...\""
                hide 4newalex50
                show blackscreen
                with dissolve
                " And then the world goes dark..."
                "... ..."
                "... ... ..."
                voic "\" *Pant* *Pant* *Pant*\""
                hide blackscreen
                show 4newalex51
                with dissolve
                " When you regain your sight, you see him lying there."
                p "\" The fuck?\""
                hide 4newalex51
                show 4newalex52
                with dissolve
                p "\" What the hell?\""
                p "\" What the fuck just happened...\""
                " You feel pain lancing through your ribs."
                p "\" Fucker must've broken my ribs.\""
                hide 4newalex52
                show 4newalex53
                with dissolve
                " You lift your shirt to take a look."
                p "\" Well...\""
                p "\" That's not good.\""
                p "\" No! Definitely not good.\""
                hide 4newalex53
                show 4newalex54
                with dissolve
                p "\" Grrrr...\""
                p "\" Fuck!\""
                p "\" I need to get out of here...\""
                hide 4newalex54
                show 4newalex55
                with dissolve
                " You manage to make your way back to the car."
                p "\" *Groan*\""
                p "\" What the fuck do I do?\""
                p "\" About myself?... About the body?...\""
                hide 4newalex55
                show 4newalex55a
                with dissolve
                " Your vision starts to darken once again."
                p "\" Must be the blood loss.\""
                " *Ring* *Ring*"
                " Alexandra is calling."
                p "\" Great... This is just great...\""
                hide 4newalex55a
                show 4newalex56
                with dissolve
                p "\" Hello?\""
                a "\" Hey! Where are you?\""
                p "\" What?\""
                a "\" I had a nightmare about you. Where are you?\""
                p "\" Actually...\""
                p "\" Bleeding my life away in my car.\""
                a "\" What?\""
                p "\" It went bad.\""
                a "\" Where are you???\" She says, shrilly."
                " You give her the address."
                a "\" Don't move! I'm on my way!\""
                " *Click*\""
                hide 4newalex56
                show 4newalex55a
                with dissolve
                p "\" Fuck...\""
                hide 4newalex55a
                show 4newalex55b
                with dissolve
                " Your vision gets darker, and darker..."
                p "\" I... I'm...\""
                hide 4newalex55b
                show blackscreen
                with dissolve
                "..."
                "... ..."
                " *Wheels screeching*"
                hide blackscreen
                show 4newalex57
                with dissolve
                a "\" Stop the car!\""
                a "\" There he is!\""
                hide 4newalex57
                show blackscreen
                with dissolve
                a "\" Fuck!\""
                i "\" Yeah...\""
                a "\" Hey stupid. Grab his arm.\""
                yuri "\" Alright.\""
                "..."
                yuri "\" Fuck... He's heavy...\""
                a "\" Stop bitching!\""
                hide blackscreen
                show 4newalex58
                with dissolve
                " When you next open your eyes, you see a bed before you."
                a "\" Where the fuck did you get this van?\""
                yuri "\" It's mine.\""
                a "\" You got a rape van. That's great.\""
                i "\" It actually is a rape van.\""
                a "\" If we get stopped, I swear...\""
                hide 4newalex58
                show blackscreen
                with dissolve
                " And that's the last thing you see."
                "..."
                "... ... ..."
                p "\" Ugh...\""
                hide blackscreen
                show 4newalex59
                with dissolve
                " When you wake up, you recognize Izzy's room."
                " And the knife sitting on the bedside table."
                hide 4newalex59
                show 4newalex60
                with dissolve
                i "\" You're awake!\""
                p "\" Isabella?\""
                i "\" Don't move.\""
                if izzyaccept == True or izzyaccept1 == True or izzyaccept2 == True:
                    hide 4newalex60
                    show 4newalex63
                    with dissolve
                    " She kneels next to you and takes your hand."
                    i "\" What happened?\""
                    p "\" I should ask you that.\""
                    i "\" Well, Alex comes in screaming that you're hurt.\""
                    i "\" So we got Yuri and came to get you.\""
                    hide 4newalex63
                    show 4newalex64
                    with dissolve
                    i "\" Scared the fuck out of us.\""
                    i "\" Does it hurt?\""
                    i "\" Your hand?\""
                    p "\" No.\""
                    i "\" How about the side of your chest?\""
                    p "\" Can't really feel anything right now.\""
                    i "\" Must be the medication.\""
                    call screen screen21
                else:
                    hide 4newalex60
                    show 4newalex61
                    with dissolve
                    i "\" How are you feeling?\""
                    p "\" More or less ok.\""
                    p "\" What happened?\""
                    i "\" Well, Alex comes in screaming that you're hurt.\""
                    i "\" So we got Yuri and came to get you.\""
                    i "\" Scared the fuck out of her.\""
                    i "\" I should go get her.\""
                    jump ep4cont2



label ep4izzycaress:
                $ izzycaress = True
                scene 4newalex67
                with dissolve
                " You cup Izzy's face in your hand."
                p "\" Izzy?\""
                p "\" I feel fine.\""
                show 4newalex68
                with dissolve
                " She takes your hand, and kisses it."
                hide 4newalex68
                show 4newalex65
                with dissolve
                " Then gives you a gentle hug."
                i "\" Don't do that again, ok?\""
                i "\" You looked like a corpse when we found you.\""
                p "\" I'll try.\""
                i "\" I'll go get Alex.\""
                jump ep4cont2

label ep4izzynothing:
                scene 4newalex64
                with dissolve
                i "\" Don't do that again, ok?\""
                i "\" You looked like a corpse when we found you.\""
                p "\" I'll try.\""
                i "\" I'll go get Alex.\""
                jump ep4cont2

label ep4cont2:
                scene 4newalex66
                with dissolve
                " She comes back a minute later with Alexandra."
                a "\" How are you?\""
                p "\" Ok, I guess.\""
                a "\" Are you in pain?\""
                p "\" Not really.\""
                show 4newalex69
                with dissolve
                " She gives you a gentle hug."
                a "\" Scared the fuck out of me.\""
                p "\" Sorry.\""
                hide 4newalex69
                show 4newalex70
                with dissolve
                a "\" What the hell is wrong with you?\""
                a "\" Why were you alone if the guy was dangerous?\""
                a "\" You're a fucking asshole! You know that?\""
                p "\" Didn't mean...\""
                hide 4newalex70
                show 4newalex69
                with dissolve
                " She hugs you again."
                a "\" But you're here now.\""
                a "\" Izzy, go get the doc.\""
                i "\" Alright.\""
                hide 4newalex69
                show 4newalex71
                with dissolve
                " She comes back a couple of minutes later with a corpse-like looking guy."
                doc "\" How is he?\""
                doc "\" Good color.\""
                doc "\" Alex, let me take a look.\""
                doc "\" Move aside.\""
                a "\" Alright.\""
                hide 4newalex71
                show 4newalex72
                with dissolve
                " He pokes you here, he pokes you there..."
                a "\" Well?\""
                doc "\" Hmmm...\""
                a "\" That doesn't sound good.\""
                doc "\" It's very good in fact.\""
                doc "\" Can't say more without a CT scan...\""
                a "\" That's not an option.\""
                doc "\" You said that.\""
                doc "\" But it looks good. Too good.\""
                p "\" Too good?\""
                doc "\" No one should heal this quickly. Not after what happened to you.\""
                doc "\" Any abdominal pain?\""
                p "\" No.\""
                doc "\" Hmm... I could've sworn that chest wound would've given you internal bleeding.\""
                doc "\" Hmmm...\""
                doc "\" Alright.\""
                hide 4newalex72
                show 4newalex73
                with dissolve
                a "\" So?\""
                doc "\" Despite everything I said last night, it looks like he'll be ok.\""
                doc "\" Amazing really.\""
                doc "\" Still, he should go to the hospital.\""
                a "\" Can't do that.\""
                doc "\" Well, change his dressing. And call me immediately if he has any fever or abdominal pain.\""
                a "\" Will do. Thank you.\""
                a "\" And... Sorry for threatening you last night.\""
                doc "\" Hmmm... May I go now?\""
                a "\" Yes.\""
                hide 4newalex73
                show 4newalex74
                with dissolve
                " He leaves, and the girls jump on the bed."
                a "\" Looks like you'll be here for a little while.\""
                i "\" Probably need to put a chair in the shower.\""
                a "\" Izzy, can you leave us alone for a minute? I want to talk to [player_name] about something.\""
                i "\" I'll go check on Momma.\""
                hide 4newalex74
                show 4newalex75
                with dissolve
                a "\" Now tell me what happened.\""
                " You recount what you remember."
                p "\" What about you? What happened while I was out.\""
                a "\" Well, after I talked to you I got Izzy and Yuri, and we came to get you.\""
                a "\" We brought you back here, Yuri took care of the body.\""
                p "\" How?\""
                a "\" I don't know and I don't want to.\""
                p "\" Why didn't you take me to the hospital?\""
                a "\" Because no one can know what happened. You have to tell Dima you have a cold, and can't be really active.\""
                a "\" Yuri will cover for you at the agency.\""
                p "\" What? Why?\""
                hide 4newalex75
                show 4newalex76
                with dissolve
                a "\" Think about it.\""
                a "\" The cop guy knew you were there.\""
                a "\" Just because he was willing to look away from a little violence, doesn't mean he'll look away from this.\""
                a "\" So he can never suspect.\""
                p "\" The guy attacked me.\""
                a "\" Good luck getting him to buy that.\""
                a "\" But even more important is my Dad.\""
                p "\" What?\""
                hide 4newalex76
                show 4newalex77
                with dissolve
                a "\" Let's say you get arrested...\""
                p "\" That's inevitable, isn't it?\""
                a "\" Maybe.\""
                a "\" But you can link him to extorting that agency. And with prostitution.\""
                p "\" Are you saying he'd kill me?\""
                a "\" I don't know. I don't think so.\""
                a "\" But either way, I'm not betting your life on it.\""
                hide 4newalex77
                show 4newalex78
                with dissolve
                a "\" So, you've got a cold. Got it?\""
                p "\" Yeah.\""
                a "\" I trust Yuri. He'll cover for you.\""
                p "\" Alright.\""
                p "\" What about the doctor?\""
                hide 4newalex78
                show 4newalex79
                with dissolve
                a "\" He's alright.\""
                p "\" Who is he?\""
                a "\" My pediatrician.\""
                p "\" You're kidding.\""
                a "\" He's been taking care of me all my life. I trust him.\""
                p "\" Alright.\""
                a "\" Don't worry. I'll take care of you puppy.\""
                hide 4newalex79
                show 4newalex80
                with dissolve
                a "\" Bet you wished you'd stayed with us last night though.\""
                p "\" You don't say.\""
                p "\" How was it?\""
                a "\" Oh, we went spelunking.\""
                p "\" Ha ha...\""
                hide 4newalex80
                show 4newalex82
                with dissolve
                " She nuzzles up against you, and gives you a kiss on the neck."
                a "\" We'll get you some bodyguards.\""
                p "\" I think I'm supposed to do that job.\""
                a "\" Once you get better, we'll talk with the guy from that boxing gym.\""
                a "\" He must know some men with big fists and small brains.\""
                p "\" Like me?\""
                a "\" Like you.\""
                p "\" When you hold me like this...\""
                a "\" Yes?\""
                p "\" Why do I get the vibe of Cathy Bates, in Misery?\""
                hide 4newalex82
                show 4newalex81
                with dissolve
                a "\" Hahaha...\""
                a "\" Oh, fuck you.\""
                hide 4newalex81
                show 4newalex60
                with dissolve
                i "\" Alex?\""
                i "\" Yuri is here.\""
                a "\" Alright. Can you send him in?\""
                i "\" Sure.\""
                hide 4newalex60
                show 4newalex83
                with dissolve
                yuri "\" Hey chief.\""
                yuri "\" Feeling better?\""
                a "\" What the hell?\""
                hide 4newalex83
                show 4newalex84
                with dissolve
                a "\" You came in here with that cigarette?\""
                yuri "\" Come on...\""
                a "\" Get the fuck out before I shove it up your ass!\""
                yuri "\" Alright... Alright...\""
                hide 4newalex84
                show 4newalex85
                with dissolve
                " After throwing him out, she comes back to you."
                p "\" I actually think you're going overboard.\""
                a "\" Nonsense!\""
                a "\" We need to look after your health.\""
                hide 4newalex85
                show 4newalex87
                with dissolve
                " You spend the next few days with the girls doting over you."
                " And you grew comfortable with it."
                " Staying in bed all day."
                hide 4newalex87
                show 4newalex86
                with dissolve
                " Alexandra bringing you your meals."
                " All in all, despite the occasional lances of pain, you rarely felt more content."
                hide 4newalex86
                show 4newalex89
                with dissolve
                a "\" Aren't you going to eat your breakfast?\""
                hide 4newalex89
                show 4newalex88
                with dissolve
                " You take a sneaky glance under the tray."
                a "\" Really?\""
                hide 4newalex88
                show 4newalex89
                with dissolve
                a "\" Don't even think about it.\""
                a "\" You're still healing.\""
                a "\" You'd come apart like an old kitchen rag.\""
                p "\" I'm feeling much better, actually.\""
                a "\" Really?\""
                p "\" Man does not live on bread alone.\""
                a "\" Just finish your meal.\""
                hide 4newalex89
                show 4newalex90
                with dissolve
                " You quickly finish up everything she brought you."
                hide 4newalex90
                show 4newalex91
                with dissolve
                a "\" Hmmm...\""
                p "\" What?\""
                a "\" Maybe you are feeling better.\""
                p "\" I told you.\""
                a "\" This isn't exactly making love under the moonlight though.\""
                p "\" No. But it's deeper in a way.\""
                a "\" I guess sleeping next to us every night and not doing anything about it, is a bit teasing.\""
                p "\" More than a bit.\""
                hide 4newalex91
                show 4newalex93
                with dissolve
                a "\" I'll go get Izzy.\""
                p "\" Izzy?\""
                a "\" She was upset the last time that we didn't include her.\""
                call screen screen22

label ep4stopher:
                scene 4newalex93
                with dissolve
                p "\" Really?\""
                p "\" How about just the two of us.\""
                show 4newalex94
                with dissolve
                a "\" You and I will mess around in Izzy's bed without her?\""
                a "\" You won't give up, will you?\""
                hide 4newalex94
                show 4newalex128
                with dissolve
                " She sits back down next to you."
                a "\" I love her puppy.\""
                a "\" You'll just have to get used to that.\""
                a "\" I won't leave her.\""
                a "\" I won't leave you either. But I'm certainly not leaving her.\""
                a "\" There's no getting around it.\""
                call screen screen23

label ep4saynothing:
                scene 4newalex132
                with dissolve
                " She hugs you again."
                a "\" Sorry.\""
                a "\" Like I said. I'm not disloyal.\""
                a "\" And I'll always love her.\""
                p "\" I see.\""
                jump ep4cont3

label ep4getizzy:
                scene 4newalex128
                with dissolve
                $ izzyaccept3 = True
                p "\" Go get her then.\""
                show 4newalex131
                with dissolve
                a "\" Are you saying that just for me?\""
                p "\" Pretty much.\""
                hide 4newalex131
                show 4newalex130
                with dissolve
                a "\" I don't get it, though.\""
                a "\" What do you have against her?\""
                p "\" Against her? Nothing.\""
                hide 4newalex130
                show 4newalex129
                with dissolve
                a "\" You should start caring about her though.\""
                a "\" When you were bleeding in that car, she helped save your life. Literally.\""
                a "\" I'll go get her.\""
                jump ep4izzyalexblow

label ep4ok:
                scene 4newalex93
                with dissolve
                p "\" Go get her then.\""
                p "\" hurry up.\""
                a "\" He he...\""
                jump ep4izzyalexblow

label ep4izzyalexblow:
                scene 4newalex95
                with dissolve
                " She runs to get Isabella."
                p "\" Yeah...\""
                p "\" I could get used to this life.\""
                show 4newalex96
                with dissolve
                " Alexandra comes back 2 minutes later."
                p "\" Isabella?\""
                a "\" She was taking a shower.\""
                a "\" Said she'll come as soon as she's done.\""
                hide 4newalex96
                show 4newalex97
                with dissolve
                a "\" Some ground rules first.\""
                p "\" Ground rules?\""
                a "\" First of all, you don't move.\""
                a "\" No exertion on your part. You just sit there.\""
                p "\" Got it.\""
                a "\" Second rule. Blowjob, no sex.\""
                a "\" I don't need you to overexert yourself.\""
                a "\" Third rule, if you feel ANY pain...\""
                p "\" I get it.\""
                a "\" I don't want to have to explain to anyone how your stitches snapped.\""
                p "\" You know what, you're right. This isn't exactly making love under the moonlight.\""
                a "\" He he... Shut up.\""
                hide 4newalex97
                show 4newalex98
                with dissolve
                " She locks her lips on yours."
                hide 4newalex98
                show 4newalex99
                with dissolve
                " You slide your hand up her thigh."
                a "\" Hey.\""
                p "\" What?\""
                hide 4newalex99
                show 4newalex100
                with dissolve
                a "\" What did I tell you about moving?\""
                a "\" You have stitches in your hand too if you haven't noticed.\""
                a "\" Sit back, relax.\""
                hide 4newalex100
                show 4newalex101
                with dissolve
                " She starts kissing your chest."
                hide 4newalex101
                show 4newalex102
                with dissolve
                " Then slides her hand under the blanket and takes hold of your dick."
                " You feel yourself instantly getting hard."
                hide 4newalex102
                show 4newalex103
                with dissolve
                a "\" Maybe not so crippled after all.\""
                p "\" Told you.\""
                a "\" Don't start.\""
                hide 4newalex103
                show 4newalex104
                with dissolve
                " She throws away the blanket, and starts running her lips up and down your thigh."
                a "\" Sweet little puppy.\""
                hide 4newalex104
                show 4newalex105
                with dissolve
                " She crawls in-between your legs, and starts rubbing your dick against her face."
                a "\" Ok so far?\""
                p "\" You're just teasing.\""
                a "\" I mean, is there any pain?\""
                p "\" No.\""
                a "\" Good.\""
                hide 4newalex105
                show 4newalex106
                with dissolve
                a "\" Forgot to tell you the fourth rule.\""
                a "\" I'm not exactly an old hand at this so no complaints.\""
                p "\" So you suck at sucking?\""
                hide 4newalex106
                show 4newalex107
                with dissolve
                " She runs her teeth on the head of your dick."
                p "\" Owww...\""
                hide 4newalex107
                show 4newalex108
                with dissolve
                a "\" What did I say? No complaints.\""
                p "\" Understood.\""
                hide 4newalex108
                show 4newalex109
                with dissolve
                " She runs her tongue around your balls."
                p "\" You said you were new at this.\""
                a "\" I am.\""
                hide 4newalex109
                show 4newalex110
                with dissolve
                " She alters her attention between your balls, and the inside of your thighs."
                p "\" That's... that's...\""
                i "\" Hey.\""
                hide 4newalex110
                show 4newalex111
                with dissolve
                i "\" I see you've started.\""
                a "\" Mmmm...\""
                hide 4newalex111
                show 4newalex112
                with dissolve
                i "\" What are you doing?\""
                a "\" Checking his temperature, what does it look like?\""
                hide 4newalex112
                show 4newalex113
                with dissolve
                i "\" Are you sure you're up to this?\" She asks you."
                i "\" You don't feel any pain do you?\""
                p "\" No.\""
                hide 4newalex113
                show 4newalex114
                with dissolve
                i "\" Surprised you can get hard.\""
                p "\" What?\""
                i "\" I've heard it takes weeks to get hard after an operation.\""
                a "\" He didn't have an operation.\""
                i "\" He got cut. It's the same thing.\""
                hide 4newalex114
                show 4newalex115
                with dissolve
                " She takes the head of your dick in her mouth, and flicks her tongue around it."
                p "\" Ohhh...\""
                p "\" That's... That's...\""
                scene izzyalexblow animated with fade:
                    "3a1.webp"
                    pause 0.05
                    "3a2.webp"
                    pause 0.05
                    "3a3.webp"
                    pause 0.05
                    "3a4.webp"
                    pause 0.05
                    "3a5.webp"
                    pause 0.05
                    "3a6.webp"
                    pause 0.05
                    "3a7.webp"
                    pause 0.05
                    "3a8.webp"
                    pause 0.05
                    "3a9.webp"
                    pause 0.05
                    "3a10.webp"
                    pause 0.05
                    "3a11.webp"
                    pause 0.05
                    "3a12.webp"
                    pause 0.05
                    "3a13.webp"
                    pause 0.05
                    "3a14.webp"
                    pause 0.05
                    "3a15.webp"
                    pause 0.05
                    "3a16.webp"
                    pause 0.05
                    "3a17.webp"
                    pause 0.05
                    "3a18.webp"
                    pause 0.05
                    "3a19.webp"
                    pause 0.05
                    "3a20.webp"
                    pause 0.05
                    repeat
                p "\" Ohh..."
                p "\" You never did this before?\""
                i "\" Mmmm...\""
                a "\" *Slurp*\""
                p "\" Fuck...\""
                $ renpy.pause ()
                show 4newalex116
                with dissolve
                " You close your eyes, getting lost in the feeling."
                " Until it suddenly stops."
                show 4newalex117
                with dissolve
                i "\" Are you ok?\""
                p "\" What? Why did you stop?\""
                i "\" You made a face.\""
                a "\" Yeah. What was that?\""
                a "\" Where does it hurt.\""
                p "\" It doesn't. It's just...\""
                p "\" Please don't stop.\""
                i "\" Alright.\""
                hide 4newalex117
                show 4newalex118
                with dissolve
                a "\" Tell us when you're about to... You know...\""
                a "\" And Izzy?\""
                i "\" Huh?\""
                a "\" Not his chest, ok?\""
                a "\" It can't get on his chest.\""
                i "\" Uh huh...\""
                scene izzyalexblow animated with fade:
                    "3a1.webp"
                    pause 0.03
                    "3a2.webp"
                    pause 0.03
                    "3a3.webp"
                    pause 0.03
                    "3a4.webp"
                    pause 0.03
                    "3a5.webp"
                    pause 0.03
                    "3a6.webp"
                    pause 0.03
                    "3a7.webp"
                    pause 0.03
                    "3a8.webp"
                    pause 0.03
                    "3a9.webp"
                    pause 0.03
                    "3a10.webp"
                    pause 0.03
                    "3a11.webp"
                    pause 0.03
                    "3a12.webp"
                    pause 0.03
                    "3a13.webp"
                    pause 0.03
                    "3a14.webp"
                    pause 0.03
                    "3a15.webp"
                    pause 0.03
                    "3a16.webp"
                    pause 0.03
                    "3a17.webp"
                    pause 0.03
                    "3a18.webp"
                    pause 0.03
                    "3a19.webp"
                    pause 0.03
                    "3a20.webp"
                    pause 0.03
                    repeat
                " Izzy resumes with greater forcefulness."
                p "\" Ohh..."
                i "\" Mmmm...\""
                a "\" *Slurp*\""
                p "\" It won't take long like... Like this...\""
                i "\" Mmmm...\""
                p "\" Girls... I'm about to...\""
                p "\" I'm about to...\""
                $ renpy.pause ()
                show 4newalex119
                with dissolve
                " As you cum, Izzy does as she's told and aims away from your chest."
                a "\" Ugh...\""
                a "\" What the?...\""
                hide 4newalex119
                show 4newalex120
                with dissolve
                a "\" It's all over me.\""
                i "\" Just your face.\""
                a "\" I can feel it dripping.\""
                i "\" He he...\""
                hide 4newalex120
                show 4newalex122
                with dissolve
                a "\" It's not funny Izzy.\""
                i "\" It kinda is... He he...\""
                a "\" It feels weird.\""
                i "\" Come here.\""
                a "\" Why?\""
                i "\" Come here.\""
                hide 4newalex122
                show 4newalex123
                with dissolve
                i "\" It's not poison, you know.\""
                a "\" It's just feels... Sticky...\""
                a "\" Sorry puppy. I don't mean that...\""
                i "\" Come closer.\""
                hide 4newalex123
                show 4newalex124
                with dissolve
                " She starts licking the cum off Alexandra's face."
                a "\" Ohhh...\""
                i "\" *Slurp*\""
                p "\" Ok...\""
                a "\" What are you doing?\""
                hide 4newalex124
                show 4newalex125
                with dissolve
                i "\" What?\""
                i "\" Don't tell me you didn't like it.\""
                a "\" You're a freak.\""
                i "\" That's the first time you've complained about that.\""
                a "\" I wasn't complaining.\""
                hide 4newalex125
                show 4newalex126
                with dissolve
                i "\" What about you?\""
                a "\" Any stitches come undone?\""
                p "\' Don't think so.\""
                a "\" Abdominal pain?\""
                p "\" I'm fine. And I think we're just getting started.\""
                a "\" Nah, nah... You just have to be patient.\""
                hide 4newalex126
                show 4newalex127
                with dissolve
                i "\" Alright. Guess I have to shower again.\""
                i "\" You should hurry up and get dressed Alex.\""
                i "\" We'll be late for school.\""
                a "\" Be with you in a minute.\""
                hide 4newalex127
                $ renpy.end_replay()
                show 4newalex131
                with dissolve
                a "\" So, a little release?\""
                p "\" A little. Was looking for more.\""
                a "\" Not while you're recovering.\""
                a "\" Besides, don't be an asshole.\""
                hide 4newalex131
                show 4newalex132
                with dissolve
                a "\" You'll have to get back out there soon.\""
                a "\" People will start to suspect something's not right.\""
                jump ep4cont3

label ep4cont3:
                scene 4newalex78
                with dissolve
                " Your recovery went quite quickly."
                show 4newalex133
                with dissolve
                " Soon you could walk with a little help from Alex."
                " And it was time you got back to work."
                hide 4newalex133
                show 4newalex134
                with dissolve
                i "\" Isn't it too soon?\""
                a "\" For what?\""
                i "\" He's not completely healed yet.\""
                a "\" Puppy's no bitch.\""
                a "\" But we don't have a choice.\""
                a "\" He has to show his face before people start asking questions.\""
                hide 4newalex134
                show back1
                with dissolve
                show 4newalex135
                with dissolve
                " That day you drove the girls to school again."
                " When you hit a pot hole."
                hide 4newalex135
                show 4newalex136
                with dissolve
                a "\" Are you ok?\""
                p "\" Fine.\""
                p "\" I'm not made of glass now Alex.\""
                p "\" Listen, I need to ask you something.\""
                p "\" Did you see that guy again?\""
                hide 4newalex136
                show 4newalex10
                with dissolve
                a "\" What guy?\""
                p "\" The guy that was outside my apartment, remember?\""
                a "\" Oh... Him.\""
                a "\" No, not really.\""
                p "\" I see.\""
                hide 4newalex10
                show 4newalex2
                with dissolve
                p "\" But just because you didn't see him, doesn't mean he wasn't there.\""
                p "\" Just be careful.\""
                hide 4newalex2
                show 4newalex10
                with dissolve
                a "\" Shouldn't I be telling you that?\""
                hide 4newalex10
                show 4newalex137
                with dissolve
                " You drop them off, and head to work."
                yuri "\" Hey. Back already?\""
                p "\" How are things here?\""
                yuri "\" Peachy. Don't worry about it.\""
                p "\" Hmmm...\""
                yuri "\" You just relax. We got it covered.\""
                hide 4newalex137
                show 4newalex138
                with dissolve
                " Later while in the park with Narysa looking for girls, you ask her..."
                p "\" So, you noticed I've been gone.\""
                nar "\" Yup.\""
                p "\" How has Yuri been handling things?\""
                nar "\" What do you mean?\""
                nar "\" The place hasn't caught fire.\""
                p "\" That bad?\""
                nar "\" You really want me to tell you the truth?\""
                nar "\" You're not going to go all King Kong, are you?\""
                p "\" I'm not.\""
                hide 4newalex138
                show 4newalex139
                with dissolve
                nar "\" He's a lot better at this than you are.\""
                p "\" Really?\""
                nar "\" Does it surprise you?\""
                nar "\" No offense, but you're not very personable.\""
                nar "\" He's... He's nice and non threatening.\""
                nar "\" Makes the girls more comfortable.\""
                nar "\" More than you do, at any rate.\""
                p "\" I see.\""
                p "\" And why did you think I'd go all King Kong?\""
                hide 4newalex139
                show 4newalex138
                with dissolve
                nar "\" I don't know...\""
                nar "\" You seem like the type that might.\""
                p "\" Really?\""
                nar "\" Yeah.\""
                nar "\" Kinda the opposite of Yuri.\""
                hide 4newalex138
                show 4newalex5
                with dissolve
                " Seeing Yuri interact with Clara and the rest of the girls, you realize that Narysa might be right."
                " He was certainly non threatening. And had a talent of putting them at ease, when he wanted to."
                hide 4newalex5
                show 4newalex140
                with dissolve
                p "\" I'd better go see Mark, since I'm really not needed here.\""
                p "\" And Alex is probably right about getting some muscle in the long term.\""
                hide 4newalex140
                show 4newalex141
                with dissolve
                " You drive over to the gym."
                Mark "\" Keep your hands up!\""
                Mark "\" You see that? That's paying the stupid tax.\""
                Mark "\" Now, keep your hands up!\""
                p "\" Hey!\""
                hide 4newalex141
                show 4newalex142
                with dissolve
                Mark "\" Oh, it's you.\""
                Mark "\" Haven't seen you in a while.\""
                p "\" Been busy.\""
                p "\" Listen. We're looking for some of the guys from here, that might be looking for some extra cash.\""
                Mark "\" By doing what?\""
                p "\" Just keeping someone safe. Just in case.\""
                Mark "\" Who?\""
                p "\" Me.\""
                hide 4newalex142
                show 4newalex143
                with dissolve
                Mark "\" I see.\""
                Mark "\" I'll make up a list.\""
                Mark "\" There are always guys in need of cash.\""
                hide 4newalex143
                show 4newalex144
                with dissolve
                Mark "\" I'll have it for you in a couple of days.\""
                p "\" That would work.\""
                Mark "\" Ready to get in the ring?\""
                p "\" Not tonight.\""
                p "\" Talk to you later.\""
                if jasminemission1goodending == True:
                    hide 4newalex144
                    show 4newalex145
                    with dissolve
                    jas "\" Hi!\""
                    p "\" Hey.\""
                    jas "\" Can you come over here for a second?\""
                    p "\" I guess.\""
                    hide 4newalex145
                    show 4newalex146
                    with dissolve
                    " You walk with her to a corner of the gym."
                    jas "\" What the hell?\""
                    jas "\" Haven't seen you in more than a week.\""
                    jas "\" Weren't even going to say hello?\""
                    p "\" Last time, you ran away from me.\""
                    hide 4newalex146
                    show 4newalex147
                    with dissolve
                    jas "\" What does that have to do with anything.\""
                    jas "\" I'm allowed to do that.\""
                    jas "\" And you're supposed to run after.\""
                    p "\" I'll make a note of that.\""
                    hide 4newalex147
                    show 4newalex148
                    with dissolve
                    jas "\" I see you have a lot to learn.\""
                    jas "\" Now how have you been.\""
                    p "\" Surviving... Literally.\""
                    jas "\" You haven't been here in a while.\""
                    hide 4newalex148
                    show 4newalex149
                    with dissolve
                    " She gives you a playful punch."
                    p "\" *Groan*\""
                    jas "\" What?\""
                    hide 4newalex149
                    show 4newalex150
                    with dissolve
                    jas "\" What's the matter?\""
                    p "\" Nothing... It's just...\""
                    p "\" I have some stitches.\""
                    jas "\" What? Why?\""
                    p "\" Got hurt.\""
                    hide 4newalex150
                    show 4newalex151
                    with dissolve
                    " She hugs you."
                    jas "\" How? What happened?\""
                    p "\" Nothing. Just the usual.\""
                    jas "\" Your usual must be pretty rough.\""
                    p "\" It is.\""
                    hide 4newalex151
                    show 4newalex152
                    with dissolve
                    jas "\" Is that why you haven't been coming around?\""
                    p "\" Pretty much.\""
                    jas "\" And you will again from now on, yes?\""
                    p "\" As soon as I've healed up.\""
                    hide 4newalex152
                    show 4newalex153
                    with dissolve
                    jas "\" See you soon then?\""
                    p "\" Certainly.\""
                    jas "\" Alright.\""
                    p "\" I have to go now.\""
                    jas "\" Bye.\""
                    jump ep4cont4

                else:
                    jump ep4cont4

label ep4cont4:
                scene 4newalex154
                with dissolve
                " You head back to the agency, where everything seems to be running smoothly."
                " Guess, Narysa was right."
                " *Ring* *Ring*"
                show 4newalex155
                with dissolve
                p "\" Hello?\""
                phil "\" I need you to come meet me.\""
                p "\" Who's this?\""
                phil "\" Who do you think?\""
                phil "\" Unless you want me to stroll over there, and let the whole world know you're talking to a cop.\""
                phil "\" What would that do for your clientèle.\""
                p "\" Where do you want to meet?\""
                phil "\" Usual place.\""
                p "\" I'm on my way.\""
                hide 4newalex155
                show 4newalex156
                with dissolve
                p "\" What is it?\""
                phil "\" Don't take that tone with me.\""
                phil "\" Life is curious, you know that?\""
                phil "\" I was checking up on that crew. Wanted to see what they were up to.\""
                phil "\" And you know what? I couldn't find hide nor hair of them.\""
                p "\" I suppose they got the message.\""
                phil "\" Is that what happened?\""
                phil "\" You had a little chat, and they decided to skip town all together?\""
                hide 4newalex156
                show 4newalex157
                with dissolve
                phil "\" You'd better hope I don't hear different.\""
                phil "\" But that's not why I brought you here.\""
                p "\" Why did you then?\""
                phil "\" To meet someone.\""
                em "\" To meet me.\""
                hide 4newalex157
                show 4newalex158
                with dissolve
                em "\" Hello, [player_name].\""
                em "\" Heard a lot about you.\""
                p "\" And you are?\""
                em "\" You can call me Emma.\""
                hide 4newalex158
                show 4newalex159
                with dissolve
                em "\" This is your boy, eh?\""
                phil "\" I wouldn't call him my boy.\""
                phil "\" But he owes me a favor.\""
                em "\" I see.\""
                hide 4newalex159
                show 4newalex160
                with dissolve
                em "\" Care to come inside?\""
                em "\" I'd like to talk.\""
                p "\" Do I have a choice?\""
                em "\" Of course you do.\""
                em "\" And so do we.\""
                p "\" I see.\""
                p "\" Lead the way.\""
                hide 4newalex160
                show 4newalex161
                with dissolve
                " She takes you to the kitchen."
                em "\" Have a seat.\""
                p "\" Who are you?\""
                em "\" I'm a colleague of Phillip's.\""
                p "\" So, you're a police officer?\""
                em "\" Something like that.\""
                em "\" Have a seat.\""
                hide 4newalex161
                show 4newalex162
                with dissolve
                em "\" See? Isn't this better?\""
                p "\" What do you want?\""
                em "\" I'd like to talk to you about your future.\""
                em "\" How long do you think do you have?\""
                p "\" I'm not sure what you mean?\""
                em "\" How long before some rival, or Boris puts a bullet in you?\""
                p "\" Boris? Don't know anyone named Boris.\""
                em "\" Really? Cause you've been driving his Daughter around for weeks.\""
                hide 4newalex162
                show 4newalex163
                with dissolve
                phil "\" Are you forgetting who you're talking with here?\""
                p "\" I don't know you... 'Emma'...\""
                em "\" It's fine.\""
                hide 4newalex163
                show 4newalex164
                with dissolve
                em "\" Listen. I'll make you a deal.\""
                em "\" I'll look the other way on your own activities, if from time to time you do something for me.\""
                em "\" And so will Phillip, over here.\""
                em "\" Don't worry, we don't want you to inform on your little girlfriend's Dad.\""
                em "\" We want you to enter in the cocaine business.\""
                p "\" What?\""
                em "\" Don't tell me those girls you have working for you are virgins when it comes to that.\""
                em "\" All they do is party with rich men, right?\""
                em "\" Only make sense for them to provide even more entertainment.\""
                em "\" We'll tell you who to buy from.\""
                p "\" And what are you getting out of this?\""
                em "\" Eventually, once you've established a good rapport, you'll meet their supplier.\""
                em "\" And that's the name I want to hear.\""
                p "\" I see.\""
                em "\" I'm glad you do. If you think about it it's good all around.\""
                em "\" You make some more cash. We get our name. Your boss will think higher of you.\""
                em "\" Everybody goes home happy.\""
                p "\" And if I say no?\""
                hide 4newalex164
                show 4newalex165
                with dissolve
                em "\" If you say no, I'll be on you day and night.\""
                em "\" Do you speed? Do you rip tags off mattresses?\""
                em "\" I don't care what it is, I'll put you away.\""
                em "\" Now Boris might let your little girlfriend make you some conjugal visits, but I doubt it.\""
                em "\" More likely, he'll have you killed.\""
                em "\" Don't answer me now. Take a few days.\""
                em "\" We'll be in touch.\""
                em "\" You have to go pick up those girls from school right about now, yes?\""
                p "\"... ...\""
                p "\" You'd better get going.\""
                hide 4newalex165
                show 4newalex166
                with dissolve
                " You walk back out to the garage."
                em "\" Drive me back.\""
                phil "\" Of course.\""
                hide 4newalex166
                show 4newalex167
                with dissolve
                phil "\" And you. I'll see you soon.\""
                hide 4newalex167
                show back1
                with dissolve
                show 4newalex168
                with dissolve
                " You go and pick up Alex and Izzy."
                a "\" So, how was your first day back?\""
                p "\" Eventful.\""
                a "\" Not too eventful I hope.\""
                p "\" No.\""
                a "\" Did you go by that gym?\""
                p "\" Yes. I'll have a list of recruits in a few days.\""
                p "\" I have to go by the gun range and the fitness center tonight.\""
                hide 4newalex168
                show 4newalex170
                with dissolve
                a "\" Want me to come with you?\""
                p "\" You're starting to worry too much.\""
                p "\" I ordered something from someone from the range, and I'd like to see if it's arrived.\""
                a "\" And the fitness?\""
                p "\" I need to move a little. I was bedridden for days.\""
                p "\" Don't worry. I'll be home soon.\""
                hide 4newalex170
                show 4newalex169
                with dissolve
                a "\" You're calling it home now?\""
                p "\" Sorry.\""
                a "\" Don't be.\""
                a "\" You should be calling it that.\""
                a "\" Don't overdo it at the fitness thing.\""
                p "\" I won't.\""
                hide 4newalex169
                show 4newalex172
                with dissolve
                " You drop the girls off at Izzy's, and head to the gun range."
                p "\" Jenny?\""
                hide 4newalex172
                show 4newalex173
                with dissolve
                jen "\" Oh, hey!\""
                jen "\" Where have you been? Haven't seen you in a while.\""
                p "\" I had a little accident.\""
                jen "\" What kind of accident?\""
                p "\" Nothing major.\""
                p "\" Did you manage to get what I asked for?\""
                hide 4newalex173
                show 4newalex174
                with dissolve
                jen "\" It wasn't easy.\""
                p "\" But yes?\""
                jen "\" Yes.\""
                jen "\" I don't have it with me. It's at home.\""
                p "\" Could we go get it?\""
                jen "\" Yeah. Just let me finish up.\""
                hide 4newalex174
                show 4newalex175
                with dissolve
                " You wait patiently 'til she finishes her rounds."
                hide 4newalex175
                show 4newalex176
                with dissolve
                jen "\" So, what happened? Cut yourself shaving?\""
                p "\" It was a little more than that.\""
                p "\" That's why I want Titus's Sister.\""
                jen "\" I see.\""
                jen "\" Well, ok. Let's get going.\""
                hide 4newalex176
                show back1
                with dissolve
                show 4newalex177
                with dissolve
                p "\" So, where did you get it?\""
                jen "\" Can't tell you.\""
                p "\" You're not some kind of secret hitman, are you?\""
                hide 4newalex177
                show 4newalex178
                with dissolve
                jen "\" He he...\""
                jen "\" If I was, you'd be in trouble.\""
                jen "\" Going off alone with me like this...\""
                jen "\" That's reckless.\""
                p "\" I could say the same thing about you.\""
                p "\" Inviting a man to your home.\""
                hide 4newalex178
                show 4newalex177
                with dissolve
                jen "\" If you get stupid, Titus will handle you.\""
                jen "\" There it is. Stop right here.\""
                hide 4newalex177
                show 4newalex179
                with dissolve
                " Before you enter she tells you..."
                jen "\" Now, my Sister Sam lives with me.\""
                jen "\" She doesn't know anything about anything, so mum's the word.\""
                p "\" Got it.\""
                p "\" But if she asks who I am?\""
                jen "\" I don't know. Some guy from the gun range I like. Escorted me home.\""
                p "\" Got it.\""
                hide 4newalex179
                show 4newalex180
                with dissolve
                " You walk into a shoebox apartment, much like your own."
                " And find a girl dancing in her underwear in front of the mirror."
                jen "\" Sam!\""
                sam "\" Huh?\""
                hide 4newalex180
                show 4newalex181
                with dissolve
                sam "\" What the?...\""
                sam "\" Aaaaaaa...\""
                jen "\" Don't worry, he's just...\""
                hide 4newalex181
                show 4newalex182
                with dissolve
                " She runs away into another room."
                sam "\" What the hell Jen?\""
                hide 4newalex182
                show 4newalex183
                with dissolve
                jen "\" Relax, it's just [player_name].\""
                sam "\" Who?\""
                jen "\" A friend of mine from the range.\""
                sam "\" You could've told me he was coming.\""
                jen "\" I could've, but I didn't.\""
                jen "\" Now come out, you're being rude.\""
                sam "\" Could you give me a minute to dress?\""
                hide 4newalex183
                show 4newalex184
                with dissolve
                jen "\" She's right though.\""
                jen "\" I should've told her you were coming.\""
                jen "\" Don't know why she's so shy though.\""
                jen "\" She's very pretty.\""
                call screen screen24

label epj4ennocomp:
                scene 4newalex184
                with dissolve
                p "\" Yes she is.\""
                jump ep4cont5

label ep4jencomp:
                scene 4newalex184
                with dissolve
                $ jennycomp1 = True
                p "\" I guess it runs in the family.\""
                show 4newalex185
                with dissolve
                jen "\" Look at you, trying to be charming.\""
                p "\" Just trying?\""
                p "\" Not succeeding? Not even a little bit?\""
                jen "\" Well, maybe a little bit.\""
                jen "\" But just a little bit.\""
                p "\" I'll take it.\""
                jump ep4cont5

label ep4cont5:
                scene 4newalex186
                with dissolve
                " After a few minutes, Sam comes out."
                sam "\" Hello.\""
                sam "\" Sorry about that. But you surprised me.\""
                p "\" I could tell.\""
                sam "\" If my Sister told me you were coming...\""
                show 4newalex187
                with dissolve
                jen "\" Now where would be the fun in that?\""
                hide 4newalex187
                show 4newalex188
                with dissolve
                sam "\" So, you're a gun range guy too?\""
                p "\" Yes.\""
                sam "\" I figured. Jenny only dates those types.\""
                hide 4newalex188
                show 4newalex187
                with dissolve
                jen "\" I didn't say we were dating.\""
                jen "\" I just said he was a friend.\""
                hide 4newalex187
                show 4newalex189
                with dissolve
                jen "\" We should get down to it.\""
                jen "\" It's in the kitchen.\""
                p "\" Right.\""
                jen "\" This way.\""
                hide 4newalex189
                show 4newalex190
                with dissolve
                " You and Jenny go to the kitchen."
                jen "\" I've got it hidden. One second.\""
                p "\" Sure.\""
                hide 4newalex190
                show 4newalex191
                with dissolve
                " She scrambles for a little while..."
                hide 4newalex191
                show 4newalex192
                with dissolve
                "...And then she pulls it out."
                p "\" Wow!\""
                jen "\" What you wanted, yes?\""
                hide 4newalex192
                show 4newalex193
                with dissolve
                p "\" Perfect.\""
                p "\" Feels so heavy in my hand.\""
                jen "\" It is heavy.\""
                hide 4newalex193
                show 4newalex194
                with dissolve
                jen "\" Might want to practice with it a little.\""
                jen "\" It's hard to handle without practice.\""
                p "\" Are you offering?\""
                jen "\" If you want.\""
                p "\" And what do you want for it?\""
                hide 4newalex194
                show 4newalex195
                with dissolve
                jen "\" Well, the money would be nice.\""
                jen "\" It's not cheap.\""
                p "\" I got that.\""
                p "\" Anything else?\""
                hide 4newalex195
                show 4newalex197
                with dissolve
                jen "\" Like what?\""
                call screen screen25

label ep4idk:
                scene 4newalex197
                with dissolve
                p "\" I don't know.\""
                jen "\" Well, if I think of something, I'll let you know.\""
                show 4newalex196
                with dissolve
                jen "\" For now, just the cash.\""
                p "\" Done.\""
                jen "\" And hide it before you walk out?\""
                jen "\" Don't want Sam to see it.\""
                p "\" I understand.\""
                hide 4newalex196
                " You pay Jenny, and head out."
                jump ep4cont6

label ep4dinner:
                scene 4newalex197
                with dissolve
                $ jennydinner = True
                p "\" Well, I don't know...\""
                show 4newalex200
                with dissolve
                " You take a step closer."
                p "\" Dinner, maybe?\""
                hide 4newalex200
                show 4newalex198
                with dissolve
                jen "\" With you?\""
                p "\" Yes.\""
                hide 4newalex198
                show 4newalex199
                with dissolve
                jen "\" He he...\""
                jen "\" Is that a gift for you, or me?\""
                p "\" Both?\""
                p "\" Your Sister already thinks we're together.\""
                hide 4newalex199
                show 4newalex197
                jen "\" She thinks a lot of things.\""
                p"\" Well?\""
                jen "\" Well, I'll think about it.\""
                jen "\" Can't tell you now.\""
                p "\" Alright.\""
                jen "\" For now, just the cash.\""
                p "\" Done.\""
                jen "\" And hide it before you walk out?\""
                jen "\" Don't want Sam to see it.\""
                p "\" I understand.\""
                hide 4newalex196
                " You pay Jenny, and head out."
                jump ep4cont6

label ep4cont6:
                scene 4newalex201
                with dissolve
                sam "\" It was nice to meet you.\""
                p "\" You too.\""
                show 4newalex202
                with dissolve
                " You head to the car, and hide it under the passenger seat."
                hide 4newalex202
                show back
                with dissolve
                show 4newalex203
                with dissolve
                p "\" That's better.\""
                p "\" I'll be ready next time.\""
                hide 4newalex203
                show 4newalex171
                with dissolve
                " You check around to see if you spot the guy who followed you before."
                p "\" Fuck.\""
                p "\" Maybe I'm paranoid.\""
                p "\" Maybe getting stabbed shook me.\""
                hide 4newalex171
                show 4newalex203
                with dissolve
                p "\" Will lightly hit the gym for an hour, and then head to Izzy's."
                hide 4newalex203
                show 4newalex204
                with dissolve
                " You go to the gym and do some light exercises."
                if dannyaskdate == True:
                    danny "\" Hello!\""
                    hide 4newalex204
                    show 4newalex205
                    with dissolve
                    p "\" Danny.\""
                    danny "\" Haven't been around here lately.\""
                    danny "\" Where have you been?\""
                    p "\" A little injured.\""
                    hide 4newalex205
                    show 4newalex206
                    with dissolve
                    danny "\" Still waiting for my date.\""
                    p "\" Right. Sorry about that.\""
                    hide 4newalex206
                    show 4newalex207
                    with dissolve
                    " She sits down next to you."
                    danny "\" I see your hand's all stitched up.\""
                    danny "\" Let me see.\""
                    p "\" It's just a cut.\""
                    hide 4newalex207
                    show 4newalex208
                    with dissolve
                    danny "\" Did you forget I was a nurse?\""
                    danny "\" Come on, give me your hand.\""
                    danny "\" Let me see.\""
                    hide 4newalex208
                    show 4newalex209
                    with dissolve
                    " She takes your hand in hers."
                    danny "\" What the hell happened here?\""
                    p "\" Cut myself.\""
                    danny "\" How?\""
                    p "\" Cooking.\""
                    hide 4newalex209
                    show 4newalex210
                    with dissolve
                    danny "\" How? Did you skewer yourself?\""
                    p "\" Something like that?\""
                    danny "\" I don't believe that for a second.\""
                    p "\" If I said someone skewered me, would that be more believable?\""
                    danny "\" Much more.\""
                    hide 4newalex210
                    show 4newalex211
                    with dissolve
                    danny "\" Come on, I'll take you home.\""
                    danny "\" I'll take a good look at this.\""
                    p "\" I'm sure it's fine.\""
                    danny "\" I insist.\""
                    hide 4newalex211
                    show 4newalex212
                    with dissolve
                    " She stands up."
                    danny "\" Come on, I'll count it as a date.\""
                    p "\" You're low maintenance.\""
                    hide 4newalex212
                    show 4newalex213
                    with dissolve
                    danny "\" So I've been told.\""
                    hide 4newalex213
                    show 4newalex214
                    with dissolve
                    " You stand up."
                    danny "\" Are you coming or not?\""
                    call screen screen26

                else:
                    jump ep4cont7

label ep4dannyno:
                scene 4newalex214
                with dissolve
                p "\" Danny...\""
                p "\" I appreciate what you're trying to do, but...\""
                danny "\" But what?\""
                p "\" I think we should stop here.\""
                show 4newalex216
                with dissolve
                danny "\" Why?\""
                p "\" I have someone.\""
                danny "\" You...\""
                danny "\" I see.\""
                hide 4newalex216
                show 4newalex217
                with dissolve
                " She abruptly turns around."
                danny "\" Goodbye then.\""
                danny "\" Don't worry, I won't bother you any longer.\""
                " And she storms off."
                jump ep4cont7

label ep4dannyyes:
                scene 4newalex214
                with dissolve
                $ dannyaskdate1 = True
                p "\" You couldn't keep me away.\""
                show 4newalex215
                with dissolve
                danny "\" Something tells me you're expecting more than a checkup.\""
                p "\" Am I wrong?\""
                danny "\" Well... We'll see.\""
                danny "\" Let's first take a look at that hand.\""
                hide 4newalex215
                show 4newalex218
                with dissolve
                " You both change and go to Danny's place."
                hide 4newalex218
                show 4newalex220
                with dissolve
                danny "\" Now, let me see.\""
                danny "\" Give me your hand.\""
                p "\" Here you go.\""
                hide 4newalex220
                show 4newalex221
                with dissolve
                " She takes a look at it."
                hide 4newalex221
                show 4newalex222
                with dissolve
                danny "\" Hmmm...\""
                p "\" What?\""
                danny "\" It pains me to say it, but that's expertly stitched.\""
                danny "\" I don't think I can improve on it.\""
                hide 4newalex222
                show 4newalex223
                with dissolve
                " You go around to her."
                p "\" But you could see that earlier, surely.\""
                label galleryScene1:
                p "\" So why did you bring me here?\""
                hide 4newalex223
                show 4newalex224
                with dissolve
                danny "\" Take a guess.\""
                p "\" Hmmm...\""
                p "\" My guess is that even though you're a romantic, sometimes...\""
                danny "\" Sometimes?\""
                p "\" Sometimes you just want to get fucked.\""
                hide 4newalex224
                show 4newalex225
                with dissolve
                danny "\" Really?\""
                p "\" Really.\""
                danny "\" And you think I'll choose you for that.\""
                p "\" No, I'm sure you give hand-jobs to all the men at the gym.\""
                danny "\" What makes you think I don't?\""
                p "\" Because you are a romantic, like I said.\""
                p "\" Just not always.\""
                hide 4newalex225
                show 4newalex226
                with dissolve
                " She presses herself against you."
                danny "\" Presuming that was true...\""
                danny "\" How would you deal with it.\""
                hide 4newalex226
                show 4newalex227
                with dissolve
                " You push her down, against the counter."
                danny "\" Oh, I see.\""
                hide 4newalex227
                show 4newalex228
                with dissolve
                " You pull her pants down, and yours as well."
                danny "\" Just stick it in?\""
                p "\" I'll stop right now if you want.\""
                danny "\"... ...\""
                p "\" Well?\""
                hide 4newalex228
                show 4newalex229
                with dissolve
                danny "\" I didn't say anything.\""
                hide 4newalex229
                show 4newalex230
                " You shove your dick inside her."
                danny "\" Oh...\""
                p "\" What you were looking for?\""
                hide 4newalex230
                show 4newalex231
                with dissolve
                danny "\" Ohh...\""
                danny "\" Exactly what I was looking for.\""
                scene dannysex1 animated with fade:
                    "4a1.webp"
                    pause 0.05
                    "4a2.webp"
                    pause 0.05
                    "4a3.webp"
                    pause 0.05
                    "4a4.webp"
                    pause 0.05
                    "4a5.webp"
                    pause 0.05
                    "4a6.webp"
                    pause 0.05
                    "4a7.webp"
                    pause 0.05
                    "4a8.webp"
                    pause 0.05
                    "4a9.webp"
                    pause 0.05
                    "4a10.webp"
                    pause 0.05
                    "4a11.webp"
                    pause 0.05
                    "4a12.webp"
                    pause 0.05
                    "4a13.webp"
                    pause 0.05
                    "4a14.webp"
                    pause 0.05
                    "4a15.webp"
                    pause 0.05
                    "4a16.webp"
                    pause 0.05
                    "4a17.webp"
                    pause 0.05
                    "4a18.webp"
                    pause 0.05
                    "4a19.webp"
                    pause 0.05
                    "4a20.webp"
                    pause 0.05
                    "4a21.webp"
                    pause 0.05
                    "4a22.webp"
                    pause 0.05
                    "4a23.webp"
                    pause 0.05
                    "4a24.webp"
                    pause 0.05
                    "4a25.webp"
                    pause 0.05
                    "4a26.webp"
                    pause 0.05
                    "4a27.webp"
                    pause 0.05
                    "4a28.webp"
                    pause 0.05
                    "4a29.webp"
                    pause 0.05
                    "4a30.webp"
                    pause 0.05
                    repeat
                danny "\" Ohh... Yeah...\""
                danny "\" It's been... It's been a while...\""
                p "\" For me too.\""
                danny "\" Don't you dare cum early.\""
                p "\" Yes, Ma'am.\""
                danny "\" Ohhh...\""
                danny "\" Ohhh... Fuck...\""
                danny "\" Just like that...\""
                $ renpy.pause ()
                show 4newalex232
                with dissolve
                danny "\" Mmmm...\""
                danny "\" More...\""
                p "\" Faster?\""
                danny "\" Yeah...\""
                scene dannysex1 animated with fade:
                    "4a1.webp"
                    pause 0.03
                    "4a2.webp"
                    pause 0.03
                    "4a3.webp"
                    pause 0.03
                    "4a4.webp"
                    pause 0.03
                    "4a5.webp"
                    pause 0.03
                    "4a6.webp"
                    pause 0.03
                    "4a7.webp"
                    pause 0.03
                    "4a8.webp"
                    pause 0.03
                    "4a9.webp"
                    pause 0.03
                    "4a10.webp"
                    pause 0.03
                    "4a11.webp"
                    pause 0.03
                    "4a12.webp"
                    pause 0.03
                    "4a13.webp"
                    pause 0.03
                    "4a14.webp"
                    pause 0.03
                    "4a15.webp"
                    pause 0.03
                    "4a16.webp"
                    pause 0.03
                    "4a17.webp"
                    pause 0.03
                    "4a18.webp"
                    pause 0.03
                    "4a19.webp"
                    pause 0.03
                    "4a20.webp"
                    pause 0.03
                    "4a21.webp"
                    pause 0.03
                    "4a22.webp"
                    pause 0.03
                    "4a23.webp"
                    pause 0.03
                    "4a24.webp"
                    pause 0.03
                    "4a25.webp"
                    pause 0.03
                    "4a26.webp"
                    pause 0.03
                    "4a27.webp"
                    pause 0.03
                    "4a28.webp"
                    pause 0.03
                    "4a29.webp"
                    pause 0.03
                    "4a30.webp"
                    pause 0.03
                    repeat
                danny "\" Ohh... Yeah...\""
                danny "\" Fuck me...\""
                danny "\" Fuck me hard...\""
                danny "\" Yeah...\""
                danny "\" Right there...\""
                danny "\" I'm... I'm about...\""
                p "\" Yeah...\""
                $ renpy.pause ()
                show 4newalex233
                with dissolve
                " You collapse over her as you finish."
                p "\" Yeah...\""
                danny "\" Mmmm...\""
                p "\" Fuck...\""
                show 4newalex234
                with dissolve
                danny "\" That was...\""
                p "\" Yeah...\""
                danny "\" You know... You're starting to get a little heavy.\""
                p "\" Sorry.\""
                hide 4newalex234
                show 4newalex235
                with dissolve
                danny "\" Phew...\""
                danny "\" It's amazing how much fun it can be to just...\""
                p "\" Fuck?\""
                danny "\" Yes.\""
                hide 4newalex235
                show 4newalex236
                with dissolve
                danny "\" Don't think that I do this regularly.\""
                p "\" Which part?\""
                danny "\" The bring men to my place part.\""
                p "\" Really?\""
                p "\" So I'm not just your 3 o'clock?\""
                hide 4newalex236
                show 4newalex237
                with dissolve
                danny "\" He he...\""
                danny "\" If my pussy wasn't tingling, you'd be getting slapped right now.\""
                hide 4newalex237
                show 4newalex238
                with dissolve
                p "\" I can't spend the night.\""
                danny "\" I figured.\""
                p "\" It's not that I don't want to.\""
                hide 4newalex238
                show 4newalex239
                with dissolve
                danny "\" I'm grown [player_name].\""
                danny "\" I'm not a kid.\""
                p "\" Good.\""
                danny "\" Still want my date though.\""
                hide 4newalex239
                show 4newalex240
                with dissolve
                " You give her a kiss."
                hide 4newalex240
                show 4newalex241
                with dissolve
                p "\" Will do.\""
                p "\" And flowers.\""
                danny "\" I'm counting on it.\""
                p "\" Bye.\""
                danny "\" Bye.\""
                $ renpy.end_replay()
                jump ep4cont7

label ep4cont7:
                scene 4newalex242
                with dissolve
                if izzythree or izzyaccept or izzyaccept1 or izzyaccept2 or izzyaccept3 == True:
                    $ izzyin = True
                " You go to Izzy's and find the place silent."
                show 4newalex243
                with dissolve
                " Seems the girls are already asleep."
                hide 4newalex243
                show 4newalex244
                with dissolve
                " After getting undressed, you get in bed beside them."
                if izzyin == True:
                    i "\" He's home.\""
                    a "\" Huh?\""
                    hide 4newalex244
                    show 4newalex245
                    with dissolve
                    " You open your eyes."
                    a "\" Hey.\""
                    a "\" Had us a little worried.\""
                    p "\" Nothing to worry about.\""
                    i "\" He should sleep between us.\""
                    hide 4newalex245
                    show 4newalex246
                    with dissolve
                    " She gets up and starts coming over to your left side."
                    i "\" I'll go.\""
                    i "\" You'll just end up elbowing him in the ribs.\""
                    a "\" No I wouldn't.\""
                    i "\" Please.\""
                    hide 4newalex246
                    show 4newalex247
                    with dissolve
                    " The girls embrace you from both sides."
                    hide 4newalex247
                    show 4newalex248
                    with dissolve
                    i "\" I'm not putting any pressure?\""
                    i "\" Nothing hurts?\""
                    p "\" I'm good Izzy.\""
                    hide 4newalex248
                    show 4newalex249
                    with dissolve
                    " She gives you a kiss on the shoulder."
                    hide 4newalex249
                    show 4newalex250
                    with dissolve
                    i "\" Good.\""
                    i "\" If I do, wake me up.\""
                    hide 4newalex250
                    show 4newalex251
                    with dissolve
                    a "\" Yeah, me too.\""
                    p "\" Good night, girls.\""
                    jump ep5



                else:
                    jump ep5
