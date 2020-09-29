label ep3:
                scene blackscreen
                with dissolve
                default izzythree = False
                default claragoodend1 = False
                default adigoodend1 = False
                default izzyaccept = False
                default izzyaccept1 = False
                default izzyaccept2 = False
                "...."
                "......"
                show back
                with dissolve
                show 3newalex1
                with dissolve
                " The next day, you're driving the girls to school as usual."
                a "\" So, how did you sleep last night?\""
                p "\" Mmmm...\""
                a "\" What? Don't tell me that you were tossing and turning.\""
                p "\" Mmmm...\""
                i "\" What? What are you talking about?\""
                hide 3newalex1
                show 3newalex2
                with dissolve
                a "\" I have a feeling he had trouble sleeping last night.\""
                i "\" Why?\""
                hide 3newalex2
                show 3newalex4
                with dissolve
                a "\" He got a promotion.\""
                a "\" And no other reason.\""
                i "\" Really?\""
                p "\" That's not why, actually.\""
                a "\" No?\""
                p "\" It's this girl...\""
                p "\" Won't leave me alone. Keeps making eyes at me. Sending me pics of herself.\""
                hide 3newalex4
                show 3newalex305
                with dissolve
                a "\" Really?\""
                a "\" Sounds like she's obsessed with you.\""
                p "\" She won't admit it, but yes.\""
                p "\" And here I am, just asking for a little space.\""
                p "\" I mean... Let a man be.\""
                hide 3newalex305
                show 3newalex306
                with dissolve
                a "\" Ha ha ha...\""
                a "\" I should slap you.\""
                i "\" I see.\""
                hide 3newalex306
                show 3newalex2
                with dissolve
                i "\" So, you sent him the pics.\""
                a "\" Trying to complete his collection.\""
                a "\" He doesn't sound very appreciative.\""
                hide 3newalex2
                show 3newalex3
                with dissolve
                i "\" [player_name]...\""
                a "\" He makes me sound like some slut who craves his dick.\""
                i "\" Well, he's only half wrong.\""
                a "\" I should slap you too.\""
                p "\" Hey, I didn't mention you.\""
                hide 3newalex3
                show 3newalex4
                with dissolve
                p "\" But if you see yourself in my description...\""
                p "\" That's on you.\""
                a "\" Hmmm...\""
                a "\" Just drive, puppy.\""
                hide 3newalex4
                show 3newalex307
                i "\" So, no promotion?\""
                a "\" Yes. He got one.\""
                a "\" He's just being a dick.\""
                hide 3newalex307
                show 3newalex4
                with dissolve
                a "\" And one of these days, he's going to take us out to celebrate, won't he?\""
                p "\" Yes, ma'am.\""
                a "\" Good.\""
                hide 3newalex4
                show 3newalex5
                with dissolve
                " You head to the agency after dropping off the girls."
                p "\" How is everything?\""
                show 3newalex5
                show 3newalex6
                with dissolve
                cl "\" Well enough.\""
                cl "\" Why are you here, if I may ask?\""
                cl "\" Aren't you supposed to just collect your cut?\""
                p "\" You misunderstand me. I'm here to help.\""
                hide 3newalex6
                show 3newalex7
                with dissolve
                cl "\"Yes, I'm sure you are.\" She says, sarcastically."
                cl "\" Help with what, exactly?\""
                hide 3newalex7
                show 3newalex8
                with dissolve
                p "\" Ha!\""
                p "\" I guess I don't really know much about your business.\""
                hide 3newalex8
                show 3newalex9
                with dissolve
                cl "\" Really? You don't say.\""
                cl "\" Why would you need to know anything if you can swing a fist, right?\""
                call screen screen13

label claraignorejab:
                scene 3newalex9
                with dissolve
                $ claragoodend1 = True
                p "\" Hmmm...\""
                show 3newalex8
                with dissolve
                p "\" I suppose you're right.\""
                p "\" We did come crashing down.\""
                p "\" I'll leave you to your work, then.\""
                hide 3newalex8
                show 3newalex11
                with dissolve
                cl "\" Good.\""
                jump ep3bigcont1

label claragrabher:
                scene 3newalex10
                with dissolve
                " You grab her face, and squeeze her jaw."
                " Not hard enough to cause pain, but hard enough that she can't get away."
                p "\" Careful...\""
                cl "\" I... I apologize...\""
                show 3newalex8
                with dissolve
                p "\" I'll leave you to your work. For now.\""
                jump ep3bigcont1

label ep3bigcont1:
                scene 3newalex12
                with dissolve
                " Not knowing what to do, you call Alexandra's Uncle."
                p "\" Hello, sir!\""
                p "\" Nothing. It's just that... I don't really know where to go from here.\""
                p "\" I'll wait for you.\""
                show 3newalex13
                with dissolve
                " You take a seat, and just hang around 'til Vanya arrives."
                hide 3newalex13
                show 3newalex14
                with dissolve
                van "\" Can't manage without me, eh?\""
                p "\" Just looking for some guidance.\""
                van "\" I see.\""
                hide 3newalex14
                show 3newalex15
                with dissolve
                van "\" How is my Niece?\""
                p "\" At school.\""
                p "\" I'll go pick her up later.\""
                van "\" Good. She shouldn't neglect that.\""
                van "\" Now let me talk to these people, and see what's to be done.\""
                hide 3newalex15
                show 3newalex16
                with dissolve
                van "\" Hello, darlin!\""
                cl "\" Umm... Hello?\""
                van "\" You're a pretty one.\""
                cl "\" Excuse me?\""
                hide 3newalex16
                show 3newalex13
                with dissolve
                " You head back to your chair, and wait for Vanya."
                hide 3newalex13
                show 3newalex17
                with dissolve
                " After an hour or so, he comes over to you."
                hide 3newalex17
                show 3newalex18
                with dissolve
                van "\" So, here's the deal.\""
                van "\" You don't have to run the place. But it will be in your interest to help out. And to know how things are done around here.\""
                van "\" It also wouldn't hurt you to be on friendly terms with Miss Clara over there.\""
                p "\" I understand.\""
                hide 3newalex18
                show 3newalex19
                with dissolve
                van "\" There are three priorities for you.\""
                van "\" First! You need to get someone you can trust to keep an eye on things when you're not around.\""
                van "\" Second! You'll need a numbers guy. Someone to keep an eye of that aspect of things for you.\""
                van "\" Third, and most important! They've been approached by someone before you.\""
                van "\" Same shakedown as you did.\""
                van "\" She stood tall, and they went away. Or at least that's what she thinks.\""
                p "\" I suppose we shouldn't assume that we wouldn't be the first.\""
                van "\" You gotta be on that! Really be on it.\""
                van "\" If there's another crew that had eyes on this, they won't be happy with you right now.\""
                van "\" With Clara either.\""
                hide 3newalex19
                show 3newalex20
                with dissolve
                van "\" Clara!\""
                van "\" Sweetheart! Can you come over here for a second?\""
                hide 3newalex20
                show 3newalex21
                with dissolve
                cl "\" Yes?\""
                hide 3newalex21
                show 3newalex20
                with dissolve
                van "\" Tell me again about the guys that came before.\""
                hide 3newalex20
                show 3newalex21
                with dissolve
                cl "\" Well, there were three of them.\""
                cl "\" A blonde guy with glasses. And two others.\""
                van "\" And what did they say?\""
                cl "\" Pretty much what this one said.\""
                cl "\" But I told them to go fuck themselves.\""
                hide 3newalex21
                show 3newalex20
                with dissolve
                van "\" Good girl!\""
                hide 3newalex20
                show 3newalex21
                with dissolve
                cl "\" They said they'd come back, but they never did.\""
                hide 3newalex21
                show 3newalex20
                with dissolve
                van "\" Thank you darling.\""
                van "\" That's all.\""
                hide 3newalex20
                show 3newalex22
                with dissolve
                van "\" You gotta get on them.\""
                van "\" She may think they won't come back, but they will.\""
                van "\" If you paid them a visit first, that would be much better.\""
                p "\" How do I find them?\""
                van "\" Talk to that cop that Dima has. He should be able to find out what crews are running around here.\""
                p "\" I have his number.\""
                van "\" Good! Then call him.\""
                p "\" I should be picking up Alexandra from school, anyway.\""
                hide 3newalex22
                show 3newalex23
                with dissolve
                van "\" That's your most important task.\""
                van "\" I'll stay here and watch over things for you.\""
                van "\" Call the guy, then go look after Alex.\""
                p "\" I'll be back soon.\""
                van "\" I'll be here.\""
                hide 3newalex23
                show 3newalex12
                with dissolve
                " You call Dima's cop friend and ask him to meet you."
                hide 3newalex12
                show 3newalex24
                " You head over to the meeting place."
                phil "\" What do you want? What did you do?\""
                p "\" Nothing.\""
                p "\" But some guys tried to shake down a modeling agency recently.\""
                p "\" I need to know who they are.\""
                phil "\" I see.\""
                phil "\" It will cost you.\""
                p "\" How much.\""
                phil "\" Hmmm...\""
                phil "\" I think I'll want a favor.\""
                p "\" What favor.\""
                phil "\" I'll let you know.\""
                phil "\" Anyway. I'll have your answer for you in a couple of days.\""
                phil "\" I'll call you.\""
                p "\" Alright.\""
                phil "\" See you around.\""
                hide 3newalex24
                show back1
                with dissolve
                show 3newalex1
                with dissolve
                " After you leave Phil, you go and pick up the girls."
                a "\" So, how was it?\""
                p "\" How was what?\""
                hide 3newalex1
                show 3newalex25
                with dissolve
                a "\" Your first day at the new job.\""
                p "\" Pretty overwhelming, to be honest.\""
                a "\" You'll figure it out.\""
                hide 3newalex25
                show 3newalex26
                with dissolve
                i "\" I'm sure you'll do great.\""
                p "\" Thank you, Izzy.\""
                p "\" Where are we going?\""
                i "\" My place.\""
                hide 3newalex26
                show 3newalex27
                with dissolve
                " You get the girls home."
                a "\" What's that noise?\""
                i "\" Oh Jesus.\""
                i "\" Momma?\""
                hide 3newalex27
                show 3newalex28
                with dissolve
                ag "\" Where is it?\""
                ag "\" I know it's here!\""
                ag "\" It has to be here!\""
                hide 3newalex28
                show 3newalex29
                with dissolve
                i "\" What are you doing?\""
                ag "\" Leave me alone girl!\""
                ag "\" I need to find it!\""
                i "\" Find what?\""
                ag "\" That's not your business.\""
                i "\" You've made a mess of all my books.\""
                hide 3newalex29
                show 3newalex30
                with dissolve
                a "\" You take her to bed.\""
                a "\" Me and [player_name] will clean up.\""
                hide 3newalex30
                show 3newalex31
                with dissolve
                i "\" Come Momma.\""
                i "\" You should get some rest.\""
                ag "\" Take your hands off me!\""
                i "\" We're not negotiating!\""
                i "\" Come!\""
                hide 3newalex31
                show 3newalex32
                with dissolve
                a "\" Come! Help me get these books back into their place.\""
                p "\" I thought I just got a promotion.\""
                hide 3newalex32
                show 3newalex33
                with dissolve
                a "\" You're too good to clean up with me now?\""
                p "\" Not at all.\""
                p "\" I'm just wondering how many more excuses will you use to get on all fours in front of me.\""
                a "\" You have a really one track mind.\""
                p "\" I was just about to say the same thing about you.\""
                a "\" Shut up, and help me clean.\""
                hide 3newalex33
                show 3newalex34
                with dissolve
                " Whether intentionally or not, instead of crouching she did get on all fours in front of you."
                a "\" Get down here, and help.\""
                " You help Alexandra clean up the books."
                hide 3newalex34
                show 3newalex35
                with dissolve
                " When you finish up, she jumps up and says..."
                a "\" See?\""
                a "\" Didn't take long at all.\""
                hide 3newalex35
                show 3newalex36
                with dissolve
                p "\" I should get back to the agency soon.\""
                a "\" You'll be there all day?\""
                p "\" Nah...\""
                p "\" They have regular hours.\""
                p "\" No reason for me to be there after five.\""
                a "\" Just like a regular Joe.\""
                p "\" More or less.\""
                hide 3newalex36
                show 3newalex37
                with dissolve
                " You press your body against hers."
                p "\" Are you staying here tonight?\""
                a "\" Where else?\""
                p "\" You're welcome to stay with me.\""
                a "\" Don't say that.\" She says."
                " But at the same time, she presses her body back against yours."
                hide 3newalex37
                show 3newalex38
                with dissolve
                a "\" Please!\""
                a "\" Not here. Not now.\""
                p "\" But at some other place? Some other time?\""
                a "\" [player_name]...\""
                a "\" I...\""
                i "\" Finally put her to bed.\""
                hide 3newalex38
                show 3newalex39
                with dissolve
                a "\" Is she ok?\""
                i "\" Like you don't know.\""
                i "\" As ok as she can be these days.\""
                a "\" What was she looking for?\""
                i "\" Who knows.\""
                hide 3newalex39
                show 3newalex40
                with dissolve
                a "\" Are you ok?\""
                i "\" You know me.\""
                i "\" I'm used to it by now.\""
                i "\" But sometimes...\""
                p "\" Have you considered sending her to a place where she could get professional help?\""
                hide 3newalex40
                show 3newalex41
                with dissolve
                i "\" What?\""
                i "\" A hospice?\""
                p "\" Not necessarily.\""
                i "\" You think I'd put my Mother in a hospice?\""
                hide 3newalex41
                show 3newalex42
                with dissolve
                a "\" He didn't mean anything by it, Izzy.\""
                a "\" You know that.\""
                a "\" Just looking out for you.\""
                a "\" Don't go all berserk on him.\""
                hide 3newalex42
                show 3newalex43
                with dissolve
                i "\" Sorry.\""
                i "\" I didn't mean to...\""
                p "\" It's ok.\""
                hide 3newalex43
                show 3newalex44
                with dissolve
                " She comes close to you."
                i "\" I didn't mean to snap.\""
                i "\" I've got...\""
                p "\" A temper?\""
                i "\" Ha ha... Yeah.\""
                i "\" We're good?\""
                " She seems to be expecting a kiss."
                " What do you go for?"
                call screen screen14

label izzymouth:
                scene 3newalex48
                with dissolve
                " You lean in and kiss her."
                " Her mouth opens willingly enough for you. But she doesn't respond beyond that."
                show 3newalex50
                with dissolve
                a "\" That's not very nice, [player_name].\""
                a "\" Not everything is supposed to be sensual.\""
                i "\" It's fine.\""
                a "\" No, it isn't.\""
                hide 3newalex50
                show 3newalex49
                with dissolve
                i "\" It's fine, really.\""
                p "\" I didn't mean to...\""
                i "\" I know.\""
                p "\" I guess I should head back to the agency.\""
                hide 3newalex49
                show 3newalex50
                with dissolve
                a "\" You probably should.\""
                p "\" See you girls later?\""
                a "\" Maybe.\""
                jump ep3bigcont2

label izzyforhead:
                scene 3newalex45
                with dissolve
                $ alexpoints = alexpoints + 1
                " You lean in and gently kiss her forehead."
                i "\" Mmmm...\""
                i "\" Thank you.\""
                show 3newalex46
                with dissolve
                a "\" Ahh...\""
                a "\" Sweet enough to rot your teeth.\""
                i "\" Shut up.\""
                hide 3newalex46
                show 3newalex47
                with dissolve
                " She hugs you."
                i "\" Let me get some puppy love.\""
                hide 3newalex47
                show 3newalex46
                with dissolve
                a "\" Hey! I'm a romantic too.\""
                a "\" But this is too much.\""
                hide 3newalex46
                show 3newalex47
                with dissolve
                i "\" I don't care.\""
                i "\" Don't watch then.\""
                a "\" Ha ha... Bitch.\""
                p "\" I need to get back to the agency.\""
                i "\" Five more seconds.\""
                i "\" Mmmm...\""
                hide 3newalex47
                show 3newalex46
                with dissolve
                a "\" Let go, Izzy.\""
                a "\" You'll see him again soon.\""
                p "\" See you girls later?\""
                a "\" Call me after work.\""
                jump ep3bigcont2

label ep3bigcont2:
                scene 3newalex51
                with dissolve
                " You head back to the office."
                cl "\" I don't think so.\""
                van "\" Darling! Men age like wine.\""
                cl "\" Or vinegar.\""
                p "\" I'm back.\""
                show 3newalex52
                with dissolve
                van "\" How did it go?\""
                van "\" With the cop, I mean.\""
                p "\" He said, he'll have something in a couple of days.\""
                van "\" Good.\""
                van "\" And what about a shop watcher? For when you're not here?\""
                p "\" Still thinking about it.\""
                van "\" Well. We'll hang around here for a couple more hours, then you drive me home.\""
                p "\" And tomorrow?\""
                van "\" Tomorrow we're back at it.\""
                hide 3newalex52
                show 3newalex13
                with dissolve
                " You just hang around 'til five."
                hide 3newalex13
                show 3newalex5
                with dissolve
                " Watching Clara send girls away to clients."
                " Always giving the same speech."
                hide 3newalex5
                show 3newalex308
                with dissolve
                cl "\" You're there to provide company.\""
                cl "\" Smile at him. Laugh at his dumb jokes.\""
                cl "\" Beyond that. It's your choice.\""
                " You'll need to learn where she gets these girls from."
                " But it's getting late for today."
                hide 3newalex308
                show 3newalex22
                with dissolve
                p "\" Ready to go?\""
                van "\" Yeah.\""
                hide 3newalex22
                show back1
                with dissolve
                show 3newalex54
                with dissolve
                van "\" How are things with my Niece?\""
                p "\" Things?\""
                van "\" Am I going to see a little Nephew soon?\""
                van "\" I know my Brother can be an ass. Especially when it comes to her.\""
                van "\" But don't worry.\""
                p "\" I'm not.\""
                van "\" Here's my stop.\""
                hide 3newalex54
                show 3newalex53
                with dissolve
                van "\" You get on that.\""
                p"\" On?\""
                van "\" Nephew.\""
                p "\" Yes sir.\""
                van "\" See you tomorrow.\""
                hide 3newalex53
                show 3newalex55
                with dissolve
                " You get back to your place, and see Adriana the librarian has arrived at the same time."
                p "\" Hi.\""
                adi "\" What?\""
                hide 3newalex55
                show 3newalex56
                with dissolve
                adi "\" Oh, it's you.\""
                adi "\" I'm not supposed to talk to you.\""
                p "\" Why?\""
                adi "\" Because I'm not allowed.\""
                hide 3newalex56
                show 3newalex57
                with dissolve
                " She tries to go by you."
                call screen screen15

label adiletgo:
                scene 3newalex57
                with dissolve
                " You stand aside, and let her go upstairs."
                show 3newalex58
                with dissolve
                p "\" Huh...\""
                p "\" I guess it takes all kinds.\""
                jump ep3bigcont3

label adistop:
                scene 3newalex59
                with dissolve
                p "\" Stop!\""
                show 3newalex60
                with dissolve
                adi "\" Please... I have to go.\""
                p "\" Where?\""
                adi "\" Upstairs.\""
                p "\" You can stay a minute.\""
                hide 3newalex60
                show 3newalex61
                with dissolve
                adi "\" Please! You'll get me in trouble.\""
                p "\" With whom?\""
                vin "\" Adriana?\""
                hide 3newalex61
                show 1newalex52
                with dissolve
                vin "\" Why aren't you upstairs?\""
                adi "\" I'm coming.\""
                hide 1newalex52
                show 3newalex62
                with dissolve
                " She barges past you."
                adi "\" Excuse me.\""
                hide 3newalex62
                show 3newalex63
                with dissolve
                adi "\" I'm sorry.\""
                vin "\" Don't let it happen again.\""
                adi "\" I won't.\""
                vin "\" Good.\""
                vin "\" Now go upstairs.\""
                hide 3newalex63
                with dissolve
                show 1newalex52
                with dissolve
                " After she leaves, the man turns to you."
                vin "\" What are you looking at?\""
                " Do you let it slide?"
                call screen screen16

label adiletgo1:
                scene 1newalex52
                with dissolve
                p "\" Nothing.\""
                vin "\" That's right.\""
                show 3newalex58
                with dissolve
                p "\" Huh...\""
                p "\" I guess it takes all kinds.\""
                jump ep3bigcont3

label adiintervene:
                scene 1newalex52
                with dissolve
                $ adigoodend1 = True
                p "\" That's it!\""
                vin "\" What?\""
                show 3newalex64
                with dissolve
                " You rush up the stairs and grab him by the throat."
                vin "\" What the???\""
                hide 3newalex64
                show 3newalex65
                with dissolve
                " You throw him down the stairs."
                vin "\" Fuck...\""
                vin "\" Damn...\""
                vin "\" Wait!\""
                p "\" I don't think I'll wait.\""
                hide 3newalex65
                show 3newalex66
                with dissolve
                vin "\" Wait... Wait...\""
                vin "\" It's not what you think.\""
                p "\" You can tell me what to think after I break your arms.\""
                vin "\" No! She makes me do it.\""
                p "\" What?\""
                vin "\" It's her idea.\""
                hide 3newalex66
                show 3newalex67
                with dissolve
                " He gets up, and dusts himself off."
                vin "\" It's her, man!\""
                vin "\" She's into this shit.\""
                vin "\" I have to call her every day at work, and ask her how many times she's went to the bathroom.\""
                p "\" What?\""
                vin "\" Seriously!\""
                vin "\" That choker she's started wearing? Custom made.\""
                vin "\" Metal letters on the inside. They spell cumbucket backwards. So that it gets imprinted on her neck.\""
                p "\" Really?\""
                vin "\" She's got suitcases of this stuff.\""
                p "\" And this is all her idea, you say.\""
                hide 3newalex67
                show 3newalex68
                with dissolve
                vin "\" She gets off on it.\""
                p "\" And you don't?\""
                vin "\" Nah, man. I just want the sex.\""
                p "\" Then why put up with it?\""
                vin "\" Because you can't put a price on good pussy, man.\""
                p "\" Ha ha...\""
                vin "\" Can I go now?\""
                p "\" I guess.\""
                vin "\" Thanks.\""
                hide 3newalex68
                show 3newalex58
                with dissolve
                p "\" Huh...\""
                p "\" I guess it takes all kinds.\""
                jump ep3bigcont3

label ep3bigcont3:
                scene 3newalex69
                with dissolve
                " You leave the lovebirds to their own devices, and head upstairs."
                show 3newalex230
                with dissolve
                " After a quick shower, you decide to call Alexandra."
                hide 3newalex230
                show 3newalex70
                with dissolve
                p "\" Hey. What are you up to.\""
                hide 3newalex70
                show 3newalex309
                with dissolve
                a "\" Nothing much.\""
                a "\" Bored actually. Izzy is asleep.\""
                hide 3newalex309
                show 3newalex70
                with dissolve
                p "\" Good chance for you and Agatha to paint the town red.\""
                hide 3newalex70
                show 3newalex309
                with dissolve
                a "\" Ha! I can picture it so vividly, it's disturbing.\""
                hide 3newalex309
                show 3newalex70
                with dissolve
                p "\" I guess that means our outing is canceled.\""
                hide 3newalex70
                show 3newalex309
                with dissolve
                a "\" Why? You and I can go shopping.\""
                a "\" Need a couple of dresses, for when you take us out.\""
                a "\" And you can probably use a suit. Now that you're no longer a grunt.\""
                hide 3newalex309
                show 3newalex70
                with dissolve
                p "\" A grunt, eh?\""
                hide 3newalex70
                show 3newalex309
                with dissolve
                a "\" Where's the lie?\""
                hide 3newalex309
                show 3newalex70
                with dissolve
                p "\" I didn't say there is one.\""
                hide 3newalex70
                show 3newalex309
                with dissolve
                a "\" Come pick me up?\""
                hide 3newalex309
                show 3newalex70
                with dissolve
                p "\" I'll be there shortly.\""
                hide 3newalex70
                show 3newalex71
                with dissolve
                " You drive over, and find Alex waiting for you."
                hide 3newalex71
                show 3newalex72
                with dissolve
                a "\" Hey.\""
                a "\" Kept me waiting a bit.\""
                p "\" Traffic.\""
                a "\" And here I am thinking you found some other woman on your way here.\""
                p "\" With bigger tits.\""
                a "\" Is that all it would take, bigger tits?\""
                p "\" Of course not. They'd have to be MUCH bigger tits.\""
                a "\" Heh...\""
                a "\" Alright, titboy. Let's go.\""
                hide 3newalex72
                show back
                with dissolve
                show 3newalex73
                with dissolve
                a "\" Do you enjoy it? At the agency?\""
                p "\" It's fine.\""
                a "\" Are there a lot of pretty women there?\""
                p "\" I suppose so.\""
                a "\" Anyone in particular?\""
                p "\" There's Clara.\""
                hide 3newalex73
                show 3newalex101
                with dissolve
                a "\" Clara? Who's Clara?\""
                p "\" The woman who runs the place.\""
                p "\" Listen...\""
                p "\" If I didn't know better, I'd think you were jealous.\""
                hide 3newalex101
                show 3newalex102
                with dissolve
                a "\" Not in the slightest.\""
                a "\" Just looking after my investment.\""
                p "\" I'm sure.\""
                hide 3newalex102
                show 3newalex101
                with dissolve
                a "\" And other than all the pretty ladies?\""
                p "\" Nothing much.\""
                p "\" Vanya told me that I need to find someone to look after the place for me.\""
                a "\" Isn't that your job?\""
                p "\" Yes. But for when I'm not there. Be a presence, I guess.\""
                a "\" So, this man... He'd have to be dangerous. Like a tough guy?\""
                p "\" Not really.\""
                a "\" Smart?\""
                p "\" Nope. Just loyal.\""
                hide 3newalex101
                show 3newalex103
                with dissolve
                a "\" Then I have just the man for you.\""
                p "\" Really?\""
                a "\" Mamma's got you.\""
                p "\" You know a weakling idiot who's loyal?\""
                hide 3newalex103
                show 3newalex102
                with dissolve
                a "\" That's unkindly put.\""
                a "\" But I guess it's true.\""
                hide 3newalex102
                show 3newalex74
                with dissolve
                a "\" So, do you accept?\""
                p "\" Your man?\""
                a "\" Yes.\""
                p "\" Do you really expect me to say no?\""
                a "\" More shocking things have happened.\""
                p "\" Like the fall of Rome.\""
                a "\" For one.\""
                p "\" Bring him.\""
                hide 3newalex74
                show 3newalex73
                with dissolve
                a "\" We're here.\""
                hide 3newalex73
                show 3newalex75
                with dissolve
                a "\" First, a suit for you.\""
                p "\" I don't really like suits.\""
                a "\" You don't have to wear one every day.\""
                a "\" Just from time to time.\""
                a "\" Remind people you're not a kid who just wears sneakers.\""
                hide 3newalex75
                show 3newalex76
                with dissolve
                a "\" Now let's see what we have here.\""
                a "\" Dark colors I'm thinking.\""
                p "\" That's not what you put me in last time.\""
                a "\" Last time my choices were very limited.\""
                hide 3newalex76
                show 3newalex77
                with dissolve
                a "\" Here.\""
                a "\" Go try this on.\""
                p "\" Fine.\""
                hide 3newalex77
                show 3newalex78
                with dissolve
                " You go and put on Alexandra's suit."
                a "\" Come out. Let me see.\""
                hide 3newalex78
                show 3newalex79
                with dissolve
                a "\" Well, it's off the rack.\""
                a "\" And you can tell.\""
                p "\" Ringing endorsement.\""
                a "\" But it looks good.\""
                hide 3newalex79
                show 3newalex80
                with dissolve
                a "\" Yeah. It's fine.\""
                a "\" I think I'll get one for my man too.\""
                p "\" Your man.....\""
                a "\" You called him that, not me.\""
                p "\" And who is the blessed individual.\""
                hide 3newalex80
                show 3newalex81
                with dissolve
                a "\" I think I'll keep that to myself for now.\""
                p "\" Really?\""
                a "\" You'll see tomorrow morning.\""
                p "\" Classmate, is it?\""
                hide 3newalex81
                show 3newalex82
                with dissolve
                a "\" Ha ha ha...\""
                a "\" You really want to know, don't you.\""
                hide 3newalex82
                show 3newalex83
                with dissolve
                a "\" Puppy. If I've managed to say no to you so far. Trust me no one else has a chance.\""
                p "\" Say no to me 'so far', you said.\""
                a "\" Reading a lot into that, are you?\""
                p "\" Shouldn't I? What do you think?\""
                hide 3newalex83
                show 3newalex84
                with dissolve
                a "\" What I think is that you look good in that suit.\""
                a "\" I'll get another one for my man.\""
                p "\" That word again.\""
                a "\" He he...\""
                a "\" And a couple of dresses for me and Izzy.\""
                hide 3newalex84
                show 3newalex85
                with dissolve
                a "\" Now, let's see.\""
                a "\" What do we have here?\""
                hide 3newalex85
                show 3newalex86
                with dissolve
                p "\" What kind of dresses are you looking for?\""
                a "\" Something to wear to the club?\""
                p "\" The club?\""
                a "\" You're taking us out, remember? To celebrate.\""
                p "\" When?\""
                a "\" Tomorrow night.\""
                p "\" I see.\""
                a "\" Listen. Since I picked out your suit.\""
                a "\" Why don't you pick something out for me?\""
                p "\" Alright.\""
                hide 3newalex86
                show 3newalex87
                with dissolve
                " You go rummaging through the store."
                " Do you pick out something more revealing?"
                " Or maybe, something a little more conservative."
                call screen screen17

label alexrevealing:
                scene 3newalex87
                with dissolve
                p "\" Found it!\""
                show 3newalex88
                with dissolve
                a "\" Really?\""
                a "\" Let's see what we got.\""
                hide 3newalex88
                show 3newalex89
                with dissolve
                " She goes in to change, while you wait outside."
                hide 3newalex89
                show 3newalex90
                with dissolve
                " When she comes out, she doesn't look to pleased."
                a "\" Really?\""
                a "\" Really, puppy?\""
                a "\" My tits are poking out!\""
                p "\" That's the point, I think.\""
                hide 3newalex90
                show 3newalex91
                with dissolve
                a "\" Sigh...\""
                a "\" If you want to see my tits, the thing to do is ask.\""
                a "\" I've already sent you pics.\""
                a "\" But flaunting my... Assets in public isn't really my thing.\""
                a "\" That's more Izzy's.....\""
                hide 3newalex91
                show 3newalex92
                with dissolve
                a "\" Oooh...\""
                a "\" Izzy would love this!\""
                a "\" I'll get it for her.\""
                a "\" And I'll get something else for myself.\""
                hide 3newalex92
                show 3newalex89
                with dissolve
                " She goes off to change into another dress."
                hide 3newalex89
                show 3newalex93
                with dissolve
                a "\" Now this is more my thing.\""
                a "\" Form fitting, but not revealing...\""
                hide 3newalex93
                show 3newalex95
                with dissolve
                a "\" Yeah!\""
                a "\" I like this.\""
                p "\" So, this is the one?\""
                a "\" Yes.\""
                hide 3newalex93
                show 3newalex99
                with dissolve
                a "\" Come on.\""
                a "\" We should change back, and get going.\""
                p "\" Alright.\""
                hide 3newalex99
                show back
                with dissolve
                show 3newalex73
                with dissolve
                " You drive her back to Izzy's place."
                hide 3newalex73
                show 3newalex102
                with dissolve
                a "\" See you tomorrow.\""
                p "\" Still time to change your mind, and come to my place.\""
                a "\" What about Izzy?\""
                p "\" She can come too.\""
                a "\" She'd have to.\""
                hide 3newalex102
                show 3newalex104
                with dissolve
                " She gives you a kiss."
                a "\" See you.\""
                jump ep3bigcont4

label alexconservative:
                scene 3newalex87
                with dissolve
                $ alexpoints = alexpoints + 1
                p "\" Found it!\""
                show 3newalex88
                with dissolve
                a "\" Really?\""
                a "\" Let's see what we got.\""
                hide 3newalex88
                show 3newalex89
                with dissolve
                " She goes in to change, while you wait outside."
                hide 3newalex89
                show 3newalex93
                with dissolve
                a "\" [player_name]! How did you know?\""
                a "\" This is what I'd have chosen.\""
                p "\" I can read your mind.\""
                hide 3newalex93
                show 3newalex94
                with dissolve
                " She does a little spin."
                a "\" Feels nice too.\""
                a "\" Light... Soft...\""
                hide 3newalex94
                show 3newalex95
                with dissolve
                a "\" Yeah...\""
                a "\" This is it.\""
                a "\" I'm definitely getting it.\""
                hide 3newalex95
                show 3newalex96
                with dissolve
                a "\" We should get Izzy something too.\""
                a "\" She'll want something more... Revealing, though.\""
                p "\" I don't have a problem with that.\""
                hide 3newalex96
                show 3newalex97
                with dissolve
                a "\" So, what do you think people will say when you walk in with two girls on your arms?\""
                p "\" They'll say that it's a regular Tuesday for me.\""
                a "\" Arrogant.\""
                p "\" Just honest.\""
                hide 3newalex97
                show 3newalex98
                with dissolve
                a "\" I bet.\""
                a "\" We should get Izzy one too.\""
                a "\" I'll go find something for her.\""
                hide 3newalex98
                show 3newalex89
                with dissolve
                " She goes off to change into another dress."
                hide 3newalex89
                show 3newalex310
                with dissolve
                a "\" What do you think?\""
                p "\" Well...\""
                a "\" My tits are almost out, I know.\""
                a "\" Not my thing, really.\""
                a "\" But Izzy will love it.\""
                hide 3newalex310
                show 3newalex92
                with dissolve
                p "\" I kinda love it too.\""
                a "\" You would.\""
                a "\" Come on.\""
                a "\" We should change back, and get going.\""
                p "\" Alright.\""
                hide 3newalex92
                show back
                with dissolve
                show 3newalex73
                with dissolve
                " You drive her back to Izzy's place."
                hide 3newalex73
                show 3newalex102
                with dissolve
                a "\" See you tomorrow.\""
                p "\" Still time to change your mind, and come to my place.\""
                a "\" What about Izzy?\""
                p "\" She can come too.\""
                a "\" She'd have to.\""
                hide 3newalex102
                show 3newalex104
                with dissolve
                " She gives you a kiss."
                a "\" See you.\""
                jump ep3bigcont4

label ep3bigcont4:
                scene 3newalex105
                with dissolve
                " With nothing else to do, you go home and get some sleep."
                show back
                with dissolve
                show 3newalex108
                with dissolve
                " The next day, you once again drive the girls to school."
                i "\" You two went shopping yesterday?\""
                a "\" You were sleeping, love.\""
                i "\" You could have woken me.\""
                a "\" When you were looking so sweet? Never.\""
                hide 3newalex108
                show 3newalex107
                with dissolve
                a "\" Muah!\" She gives her a kiss."
                hide 3newalex107
                show 3newalex106
                with dissolve
                i "\" And you're taking us out tonight?\" She asks you."
                p "\" So, I've been told.\""
                i "\" You don't want to?\""
                p "\" It's just an expression.\""
                i "\" Can you please take us to a place with a dance-floor?\""
                p "\" I think I can arrange that.\""
                i "\" I love to dance.\""
                p "\" Understood.\""
                hide 3newalex106
                show 3newalex108
                with dissolve
                a "\" Can I ask you something, love?\""
                a "\" I'll need to skip the first couple of classes today.\""
                i "\" Why?\""
                a "\" Just something me and [player_name] have to do.\""
                a "\" Family stuff.\""
                a "\" Can you copy your notes for me?\""
                i "\" Sure.\""
                i "\" You'll be back...\""
                a "\" In a couple of hours.\""
                " You arrive at the school."
                hide 3newalex108
                show 3newalex109
                with dissolve
                i "\" And I'll see you tonight?\""
                p "\" Bet on it.\""
                hide 3newalex109
                show 3newalex110
                with dissolve
                i "\" And can you dance?\""
                p "\" Not a step.\""
                i "\" Ahh... No problem.\""
                i "\" I'll teach you.\""
                hide 3newalex110
                show 3newalex109
                with dissolve
                i "\" See you.\""
                hide 3newalex109
                show 3newalex111
                with dissolve
                " With Izzy gone, Alexandra moves to the front seat."
                p "\" We have family stuff to take care of?\""
                a "\" We have to go pick up my man, remember?\""
                p "\" Those words again.\""
                hide 3newalex111
                show 3newalex311
                with dissolve
                a "\" Ha ha ha...\""
                a "\" I love to twist the knife.\""
                p "\" Where are we going?\""
                hide 3newalex311
                show 3newalex111
                with dissolve
                a "\" My dad's place.\""
                p "\" Hmmm...\""
                p "\" Is it the stable boy?\""
                hide 3newalex111
                show 3newalex311
                with dissolve
                a "\" We don't have a stable boy.\""
                p "\" Pool boy?\""
                a "\" You'll see.\""
                hide 3newalex311
                show 3newalex112
                with dissolve
                " You arrive at the villa."
                yuri "\" Alex! What's happening?\""
                yuri "\" Your Dad said that I'll be working somewhere else.\""
                yuri "\" That you'll take me there.\""
                a "\" That's right.\""
                a "\" But first, you need to change.\""
                a "\" I got you a suit.\""
                yuri "\" I don't wear suits.\""
                a "\" But you wear suspenders and a wife-beater. Will you listen to me for once.\""
                hide 3newalex112
                show 3newalex113
                with dissolve
                a "\" Now come get dressed.\""
                a "\" And for the last time. Get rid of that fucking cigarette.\""
                hide 3newalex113
                show 3newalex114
                with dissolve
                " They come back five minutes later."
                yuri "\" I look like an idiot.\""
                a "\" And how would that be different from any other day?\""
                a "\" Get in the car.\""
                yuri "\" Fine.\""
                hide 3newalex114
                show 3newalex115
                with dissolve
                p "\" So, your cousin?\""
                a "\" Yup.\""
                a "\" But you can call him 'Stable boy' if you want.\""
                a "\" Hey, he's loyal. And that's what you said he needed.\""
                a "\" Besides it will get him out of the house for one.\""
                a "\" And if one of those girls feels charitable...\""
                p "\" That's harsh.\""
                p "\" But I can't help but thinking...\""
                p "\" He won't just be my eyes on the agency. But your eyes on me as well.\""
                hide 3newalex115
                show 3newalex312
                with dissolve
                a "\" Told you I've been playing you.\""
                p "\" Let's go, Madame de Pompadour.\""
                p "\" Your spy awaits.\""
                hide 3newalex312
                show back
                with dissolve
                show 3newalex116
                with dissolve
                yuri "\" Where are we going? What do I have to do.\""
                a "\" We're going to a modeling agency.\""
                a "\" Cathouse, really.\""
                p "\" Cathouse? Who taught you that word? Edward G. Robinson?\""
                a "\" Shut up.\""
                a "\" And what you'd have to do, is just to keep an eye on things.\""
                hide 3newalex116
                show 3newalex117
                with dissolve
                yuri "\" Seems like a demotion.\""
                a "\" It isn't.\""
                a "\" Do you plan to spend your whole life on Dad's porch?\""
                a "\" This way, you open yourself up to new possibilities.\""
                a "\" And besides. You'll be watching over attractive young girls.\""
                a "\" Once you walk through the door, I'll hear the squelch of the collective pantie soaking from school.\""
                p "\" Ha ha...\""
                p "\" Umm... Sorry...\""
                hide 3newalex117
                show 3newalex118
                with dissolve
                " You drop Alexandra off at school."
                a "\" Trust me on this Cousin?\""
                yuri "\" Alright.\""
                hide 3newalex118
                show 3newalex119
                with dissolve
                a "\" You'll see.\""
                a "\" You'll do so well, outside Dad's house.\""
                a "\" And you'll be knee deep in pussy by the end of the week.\""
                yuri "\" Ha ha ha...\""
                yuri "\" Alright.\""
                hide 3newalex119
                show 3newalex120
                with dissolve
                a "\" Take good care of him?\""
                p "\" You bet.\""
                a "\" See you after school.\""
                hide 3newalex120
                show back
                with dissolve
                show 3newalex121
                with dissolve
                yuri "\" So, what do I really have to do.\""
                p "\" Exactly what Alexandra said.\""
                yuri "\" Keep an eye on things.\""
                p "\" Yes.\""
                yuri "\" Aren't you supposed to be doing that?\""
                p "\" I won't always be there.\""
                p "\" I have to drive Alexandra. Maybe other things.\""
                hide 3newalex121
                show 3newalex122
                with dissolve
                yuri "\" I see.\""
                " You arrive at the agency."
                hide 3newalex122
                show 3newalex123
                with dissolve
                van "\" A little late, aren't we?\""
                p "\" Had to pick someone up.\""
                p "\" You said I need someone I can trust to keep an eye on things.\""
                van "\" Him?\""
                hide 3newalex123
                show 3newalex124
                with dissolve
                yuri "\" Hi Uncle.\""
                van "\" Crawled from under your Mother's skirts, have you?\""
                yuri "\" Enough.\""
                van "\" I guess you can do no harm.\""
                van "\" Now go make yourself useful.\""
                hide 3newalex124
                show 3newalex125
                with dissolve
                van "\" Him?\""
                p "\" You said someone I can trust.\""
                van "\" I suppose.\""
                van "\" He doesn't have many qualities. But at least he won't betray you.\""
                hide 3newalex125
                show 3newalex126
                with dissolve
                yuri "\" Hello.\""
                cl "\" Hi.\""
                cl "\" What can I do for you?\""
                hide 3newalex126
                show 3newalex127
                with dissolve
                van "\" At least he has some taste in women.\""
                van "\" But it should be you talking to her.\""
                van "\" You need to learn the ins and outs of this place, remember?\""
                p "\" I was wondering how they recruit girls.\""
                van "\" Well, go and ask.\""
                hide 3newalex127
                show 3newalex126
                with dissolve
                p "\" Excuse me.\""
                p "\" I need to talk to you for a minute.\""
                hide 3newalex126
                show 3newalex128
                with dissolve
                cl "\" About what?\""
                p "\" I have a few questions.\""
                p "\" Like, how do you find girls to work for you.\""
                hide 3newalex128
                show 3newalex129
                with dissolve
                cl "\" Well, we advertise of course.\""
                cl "\" Also we have recruiters.\""
                cl "\" They go around inviting suitable girls.\""
                p "\" From where.\""
                cl "\" If you really want to know, you should ask Narysa.\""
                cl "\" She's by far my best.\""
                p "\" I probably will.\""
                cl "\" She probably hasn't left yet. She'll be at reception.\""
                p "\" I'll go talk to her.\""
                hide 3newalex129
                show 3newalex130
                with dissolve
                " You go to find Narysa."
                nar "\" Hi.\""
                p "\" Hi, I'm...\""
                nar "\" I know who you are.\""
                nar "\" You don't think your presence has gone unnoticed.\""
                nar "\" I told Clara that sooner or later... She'll draw attention.\""
                hide 3newalex130
                show 3newalex131
                with dissolve
                nar "\" Well, I guess you're the boss now.\""
                nar "\" What can I do for you?\""
                p "\" Clara told me you're the best... Recruiter?\""
                nar "\" You could say that.\""
                p "\" I want to come with you. Watch you work.\""
                hide 3newalex131
                show 3newalex132
                with dissolve
                nar "\" Ha ha ha...\""
                nar "\" And take samples, I suppose.\""
                p "\" I didn't say that.\""
                hide 3newalex132
                show 3newalex133
                with dissolve
                nar "\" Of course.\""
                nar "\" Not that I have a choice.\""
                nar "\" Nor do I care.\""
                nar "\" Are you coming now?\""
                p "\" No better time.\""
                nar "\" Alright.\""
                hide 3newalex133
                show back
                with dissolve
                show 3newalex134
                with dissolve
                p "\" Where are we going? The Mall?\""
                nar "\" The Mall?\""
                nar "\" Are we specializing on chubby chasers now?\""
                nar "\" Nah. The park.\""
                hide 3newalex134
                show 3newalex135
                with dissolve
                nar "\" A lot of girl joggers there.\""
                nar "\" So we have two things going for us from the start.\""
                nar "\" They like to take care of themselves. And they're without their boyfriends while jogging.\""
                nar "\" At least for the most part.\""
                p "\" You get many... Workers with boyfriends?\""
                nar "\" You'd be surprised.\""
                hide 3newalex135
                show 3newalex136
                with dissolve
                " You drive to the park."
                hide 3newalex136
                show 3newalex137
                with dissolve
                p "\" What do we do now?\""
                nar "\" Find a bench.\""
                nar "\" Make ourselves comfortable.\""
                hide 3newalex137
                show 3newalex138
                with dissolve
                p "\" This is your job?\""
                nar "\" This. And approaching the girls, of course.\""
                p "\" I have to ask. What's the success rate.\""
                nar "\" Pretty high. For me at least.\""
                hide 3newalex138
                show 3newalex139
                with dissolve
                p "\" I can't say I understand it.\""
                p "\" Agreeing to selling your body that easily.\""
                nar "\" Pfft... It's not nearly as bad as you think. And the money is amazing.\""
                p "\" That's easy to say when you don't have to do it.\""
                nar "\" Don't have to do it anymore.\""
                hide 3newalex139
                show 3newalex138
                with dissolve
                p "\" So, you...\""
                nar "\" Paid for my apartment.\""
                p "\" If it's that great, why did you quit?\""
                nar "\" I didn't say it was pleasant.\""
                nar "\" Just not as bad as you think.\""
                hide 3newalex138
                show 3newalex140
                with dissolve
                p "\" What about her?\""
                nar "\" Too old.\""
                nar "\" And I don't like her body.\""
                p "\" Alright.\""
                hide 3newalex140
                show 3newalex141
                with dissolve
                p "\" Her?\""
                nar "\" Ha ha...\""
                nar "\" My bet is that she's already in the business. Look at how she's dressed.\""
                p "\" All the better.\""
                nar "\" Oh no.\""
                nar "\" We want a fresh face. Not an old whore.\""
                nar "\" Someone...\""
                hide 3newalex141
                show 3newalex142
                with dissolve
                nar "\" Someone like her.\""
                p "\" Pretty.\""
                hide 3newalex142
                show 3newalex143
                with dissolve
                nar "\" I'll go talk to her.\""
                nar "\" Best if you let me do this.\""
                nar "\" She won't be as open with a man around.\""
                p "\" Alright.\""
                hide 3newalex143
                show 3newalex144
                with dissolve
                " She goes over to the girl, and they talk for a few minutes."
                " Seems to go pretty well from where you're sitting."
                hide 3newalex144
                show 3newalex145
                with dissolve
                p "\" So? How did it go?\""
                nar "\" She'll come by the agency tomorrow.\""
                p "\" Just like that?\""
                nar "\" She's agreed to be a model.\""
                p "\" Oh...\""
                nar "\" In time she'll ease into our other activities.\""
                nar "\" She'll see how much money some of the other girls are making.\""
                p "\" All about money, eh?\""
                nar "\" You think it's about the love for the fat old men that are our clients?\""
                p "\" Good point.\""
                p "\" While we're at it. Do you recruit in clubs?\""
                nar "\" Nah... Too drunk. They don't remember they even talked to you in the morning.\""
                p "\" But do you know any good clubs?\""
                nar "\" Sure.\""
                nar "\" I'll give you an address.\""
                hide 3newalex145
                show 3newalex139
                with dissolve
                " You spend a few more hours, with Narysa recruiting a few more girls."
                " But now it's time to go pick up Alexandra."
                hide 3newalex139
                show 3newalex145
                with dissolve
                p "\" I have to go.\""
                p "\" Need to go pick up someone.\""
                p "\" Are you going to stay much longer?\""
                nar "\" Nah. I'm pretty much done.\""
                nar "\" Drive me back?\""
                p "\" After my pickup.\""
                nar "\" Sure.\""
                hide 3newalex145
                show back
                with dissolve
                show 3newalex146
                with dissolve
                nar "\" So, who are you picking up?\""
                p "\" The big man's Daughter.\""
                nar "\" Ahh...\""
                nar "\" Are you a driver, or a gangster?\""
                p "\" Why not both?\""
                hide 3newalex146
                show 3newalex147
                with dissolve
                " You pick up the girls."
                hide 3newalex147
                show 3newalex148
                with dissolve
                nar "\" Do you drop them off first, or me?\""
                hide 3newalex148
                show 3newalex149
                with dissolve
                a "\" You're going back to the agency?\""
                p "\" Yes.\""
                a "\" We want to come.\""
                p "\" What?\""
                hide 3newalex149
                show 3newalex150
                with dissolve
                i "\" We want to see where you work.\""
                p "\" I'm not sure that's a good idea.\""
                hide 3newalex150
                show 3newalex149
                with dissolve
                a "\" Why?\""
                a "\" It's not like they're fucking on the desks.\""
                hide 3newalex149
                show 3newalex151
                with dissolve
                nar "\" So, you girls know what we do there?\""
                a "\" We're not as naive as we might look.\""
                nar "\" Blondie. You don't strike me as naive at all.\""
                p "\" Fine, I guess.\""
                hide 3newalex151
                show 3newalex149
                with dissolve
                a "\" Great!\""
                hide 3newalex149
                show 3newalex123
                with dissolve
                " You drive back to the agency."
                hide 3newalex123
                show 3newalex152
                with dissolve
                van "\" Darlin. What are you doing here?\""
                a "\" Just visiting.\""
                van "\" This is no place for you.\""
                a "\" Oh, please. I'm not a child.\""
                hide 3newalex152
                show 3newalex153
                with dissolve
                " She takes a seat next to you."
                a "\" Not quite what I imagined.\""
                p "\" What did you imagine?\""
                a "\" I don't know. Women in burlesque outfits hanging in cages from the roof?\""
                p "\" Ha! That's not a bad idea actually.\""
                hide 3newalex153
                show 3newalex154
                with dissolve
                a "\" So, how does it all work?\""
                p "\" Work?\""
                a "\" What's the process?\""
                a "\" Girls just come in, and are then sent out.\""
                p "\" Still getting to grips with it myself.\""
                p "\" The girl I picked you up with. She's a recruiter.\""
                p "\" They also advertise.\""
                hide 3newalex154
                show 3newalex155
                with dissolve
                a "\" Advertise?\""
                p "\" I don't think they get into specifics. Just trying to get people through the door.\""
                a "\" And the clients? Where do they get them from? How do the process payment? Do they have regular rates?\""
                p "\" Like I said. I'm still coming to grips with things.\""
                hide 3newalex155
                show 3newalex156
                with dissolve
                a "\" And who would be the one to ask.\""
                a "\" That Clara woman?\""
                p "\" Yes.\""
                a "\" I'd like to talk to her.\""
                hide 3newalex156
                show 3newalex157
                with dissolve
                a "\" Hi. Mind if I ask you a few questions?\""
                cl "\" Everyone is asking things of me lately.\""
                cl "\" Who the hell are you?\""
                hide 3newalex157
                show 3newalex7
                with dissolve
                p "\" Someone who's questions you should answer.\""
                cl "\" Oh... Alright.\""
                hide 3newalex7
                show 3newalex157
                with dissolve
                " You leave Alexandra to her questions."
                hide 3newalex157
                show 3newalex158
                with dissolve
                " While you go see how Izzy is doing."
                hide 3newalex158
                show 3newalex159
                with dissolve
                p "\" How are you?\""
                i "\" Good.\""
                p "\" How was school?\""
                i "\" Boring.\""
                i "\" Do you really care?\""
                p "\" No.\""
                hide 3newalex159
                show 3newalex160
                with dissolve
                i "\"Alex is in her element.\""
                hide 3newalex160
                show 3newalex161
                with dissolve
                " You look over to see her drill Clara."
                p "\" How so?\""
                hide 3newalex161
                show 3newalex160
                with dissolve
                i "\" She likes to play naive, but she isn't.\""
                i "\" There's a lot more of her Dad in her than she'd like to admit.\""
                hide 3newalex160
                show 3newalex162
                with dissolve
                i "\" Sometimes she almost scares me, you know.\""
                p "\" How?\""
                i "\" Like I said. She's very soft on the outside. But she has steel on the inside.\""
                p "\" Almost sounds like you're worried.\""
                i "\" I'm not.\""
                hide 3newalex162
                show 3newalex163
                with dissolve
                i "\" She loves me.\""
                i "\" And she loves you too.\""
                i "\" So, you should never be worried.\""
                yuri "\" Izzy?\""
                hide 3newalex163
                show 3newalex164
                with dissolve
                i "\" Hey!\""
                i "\" What are you doing here?\""
                yuri "\" I work here now.\""
                yuri "\" You?\""
                i "\" Just visiting.\""
                hide 3newalex164
                show 3newalex165
                with dissolve
                i "\" How do you like it so far.\""
                yuri "\" Amazing.\""
                yuri "\" You won't believe the women that come through here.\""
                i "\" Has Puppy been treating you well?\""
                hide 3newalex165
                show 3newalex166
                with dissolve
                yuri "\" Puppy?\""
                yuri "\" Who's Puppy?\""
                i "\" Ahh... No one....\""
                i "\" Did I say puppy?\""
                i "\" That's silly. Don't know why I said that.\""
                p "\" Yuri!\""
                hide 3newalex166
                show 3newalex167
                with dissolve
                yuri "\" Yeah?\""
                p "\" I'll need to leave early today.\""
                p "\" Can you watch over things for me?\""
                yuri "\" That's what I've been doing.\""
                p "\" Thanks.\""
                hide 3newalex167
                show 3newalex168
                with dissolve
                " After he leaves, Izzy turns to you and says..."
                i "\" Sorry about that.\""
                p "\" Huh?\""
                i "\" Referring to you as 'Puppy'.\""
                i "\" Alex says that you need to be feared, if you're going to be safe.\""
                p "\" I can handle myself.\""
                i "\" Still though.\""
                hide 3newalex168
                show 3newalex169
                with dissolve
                a "\" Ready to go? Or do you have to wait for them to close.\""
                p "\" That's why your Cousin is here.\""
                p "\" Have you finished with Clara?\""
                a "\" I learned a lot.\""
                p "\" Then, I'm ready to go.\""
                hide 3newalex169
                show 3newalex170
                with dissolve
                i "\" Taking us dancing?\""
                p "\" Yes.\""
                i "\" To a good club?\""
                p "\" I think so. Got the address from someone who would know.\""
                i "\" Yay.\""
                hide 3newalex170
                show back
                with dissolve
                show 3newalex171
                with dissolve
                " As you drive over to Izzy's, the girls are all lovey dovey, and can't keep their hands off each other.\""
                hide 3newalex171
                show 3newalex172
                with dissolve
                a "\" By the way. We got you a dress yesterday.\""
                i "\" When you went shopping?\""
                a "\" Hope you like it.\""
                hide 3newalex172
                show 3newalex173
                with dissolve
                " You take a seat, while the girls change."
                hide 3newalex173
                show 3newalex174
                with dissolve
                a "\" Like it?\""
                i "\" Love it.\""
                a "\" You're into the more revealing stuff.\""
                a "\" Got a suit for [player_name] too.\""
                hide 3newalex174
                show 3newalex175
                with dissolve
                i "\" Why?\""
                i "\" I think he looks great without one.\""
                a "\" You too?\""
                i "\" He's not a suit guy. He's a jeans and t-shirt guy.\""
                p "\" Thank you.\""
                hide 3newalex175
                show 3newalex176
                with dissolve
                i "\" Got your back.\""
                p "\" Ha ha...\""
                hide 3newalex176
                show 3newalex177
                with dissolve
                a "\" If you two are done jerking each other off, we should get going.\""
                a "\" And he is wearing a suit. At least for the first night.\""
                p "\" I take it then, that this is the first of many outings.\""
                hide 3newalex177
                show 3newalex176
                with dissolve
                i "\" We should go out weekly.\""
                i "\" Maybe twice a week.\""
                hide 3newalex176
                show 3newalex177
                with dissolve
                a "\" Enough, you two.\""
                a "\" Let's go.\""
                hide 3newalex177
                show 3newalex179
                with dissolve
                " You drive back to your place to change into your suit."
                hide 3newalex179
                show 3newalex180
                with dissolve
                a "'\" Come on. Hurry up.\""
                a "\" I want Izzy to see.\""
                p "\" Alright, alright.\""
                hide 3newalex180
                show 3newalex181
                with dissolve
                " You change into your suit, and come back out."
                " But you decide to leave the jacket behind."
                hide 3newalex181
                show 3newalex182
                with dissolve
                i "\" No jacket?\""
                hide 3newalex182
                show 3newalex184
                with dissolve
                a "\" I got him one.\""
                a "\" But he doesn't seem to want to wear it.\""
                p "\" Too hot.\""
                a "\" Eh... I'll take what I can get.\""
                hide 3newalex184
                show 3newalex182
                with dissolve
                i "\" I like it.\""
                i "\" You know... You're still not a suit guy. But you fill one out pretty well.\""
                hide 3newalex182
                show 3newalex183
                with dissolve
                a "\" Ahem...\""
                a "\" That's what I've been saying.\""
                a "\" Still... No one listens.\""
                hide 3newalex183
                show 3newalex184
                with dissolve
                a "\" Come on, lovebirds. Lets go.\""
                hide 3newalex184
                show 3newalex186
                with dissolve
                " You go to the club that Narysa told you about."
                " It's pretty dark."
                hide 3newalex186
                show 3newalex187
                with dissolve
                " But you do see girls dancing."
                hide 3newalex187
                show 3newalex188
                with dissolve
                " And couples."
                hide 3newalex188
                show 3newalex189
                with dissolve
                a "\" How did you find out about this place?\""
                p "\" Someone at the agency.\""
                a "\" Looks good.\""
                p "\" I'll go get us drinks.\""
                hide 3newalex189
                show 3newalex208
                with dissolve
                " You go to the bartender, and grab a few drinks."
                hide 3newalex208
                show 3newalex198
                with dissolve
                " As you head back to the girls, you notice a guy standing in the corner."
                " He seems to be alone and just watching."
                hide 3newalex198
                show 3newalex190
                with dissolve
                a "\" Hey are you coming?\""
                i "\" We're thirsty.\""
                p "\" Yeah... Yeah...\""
                hide 3newalex190
                show 3newalex198
                with dissolve
                p "\" Hmmm...\""
                hide 3newalex198
                show 3newalex191
                with dissolve
                " You get to the girls."
                a "\" What's the matter?\""
                a "\" You seem distracted.\""
                p "\" Nothing. It's nothing.\""
                hide 3newalex191
                show 3newalex192
                with dissolve
                a "\" So, you really can't dance?\""
                p "\" I'm made entirely out of elbows and knees.\""
                p "\" Tragic sight on the floor.\""
                hide 3newalex192
                show 3newalex193
                with dissolve
                i "\" I could make you look good out there.\""
                p "\" Not even God could do that.\""
                i "\" I could teach you, really.\""
                p "\" I have no doubt as to what you can do.\""
                p "\" I also have no doubt as to what I can't.\""
                hide 3newalex193
                show 3newalex194
                with dissolve
                a "\" She's not lying, you know.\""
                p "\" Ganging up on me?\""
                a "\" Trust me.\""
                hide 3newalex194
                show 3newalex195
                with dissolve
                i "\" Come on!\""
                i "\" It's easy.\""
                p "\" Fine.\""
                hide 3newalex195
                show 3newalex196
                with dissolve
                i "\" Alright, we'll start simple.\""
                i "\" Just follow my lead.\""
                p "\" Alright.\""
                " As you dance with Izzy you can't help the feeling of being watched."
                hide 3newalex196
                show 3newalex198
                with dissolve
                " There's that guy again."
                i "\"[player_name]?\""
                p "\" Huh?\""
                hide 3newalex196
                show 3newalex197
                with dissolve
                i "\" You look distracted again.\""
                p "\" It's nothing.\""
                i "\" Are you sure?\""
                p "\" Yeah.\""
                hide 3newalex197
                show 3newalex199
                with dissolve
                i "\" I've...\""
                i "\" I've become quite fond of you, you know.\""
                p "\" I know.\""
                hide 3newalex199
                show 3newalex200
                with dissolve
                " She buries her head in your chest."
                i "\" You're becoming family to me.\""
                p "\" I'm glad to hear that.\""
                i "\" You and Alex...\""
                i "\" I know she...\""
                p "\" Yes?\""
                hide 3newalex200
                show 3newalex202
                with dissolve
                i "\" What do you think it will be?\""
                i "\" Honestly.\""
                i "\" The three of us?\""
                i "\" Or... Or the two of you.\""
                call screen screen18

label izzytwo:
                scene 3newalex202
                with dissolve
                p "\" Honestly...\""
                p "\" I don't think...\""
                show 3newalex204
                with dissolve
                i "\" Don't say anymore.\""
                i "\" I hope you're wrong.\""
                hide 3newalex204
                show 3newalex196
                with dissolve
                " You dance for a few more minutes."
                " Then Izzy claims to be tired, and wants to go back to the bar."
                hide 3newalex196
                show 3newalex205
                with dissolve
                a "\" Wow, you weren't kidding.\""
                a "\" You are made of elbows.\""
                p "\" Told you.\""
                a "\" But you almost looked like a real couple out there.\""
                i "\" Looks can be deceiving.\""
                jump ep3bigcont5

label izzythree:
                scene 3newalex202
                with dissolve
                $ izzyaccept = True
                p "\" Honestly...\""
                p "\" I can't really picture myself without either of you.\""
                show 3newalex201
                with dissolve
                " Her usually thoughtful face, burst into a radiant smile."
                i "\" Really?\""
                i "\" Me neither.\""
                hide 3newalex201
                show 3newalex203
                with dissolve
                " She then gives you the most tender kiss, you ever had in your life."
                " Not sensual or, lascivious. Just tender."
                hide 3newalex203
                show 3newalex202
                with dissolve
                " As you continue to dance your feet are hitting hers."
                p "\" Sorry.\""
                i "\" It's fine.\""
                i "\" It doesn't hurt.\""
                hide 3newalex202
                show 3newalex196
                with dissolve
                " You continue to dance for a little while."
                " But you soon start to feel sorry for Izzy's feet, and go back to the bar."
                hide 3newalex196
                show 3newalex205
                a "\" Wow, you weren't kidding.\""
                a "\" You are made of elbows.\""
                p "\" Told you.\""
                a "\" But you almost looked like a real couple out there.\""
                i "\" What are you talking about?...\""
                i "\" We are a real couple.\""
                jump ep3bigcont5

label ep3bigcont5:
                scene 3newalex206
                with dissolve
                i "\" How about I take you out for a spin though?\""
                a "\" You make me sound like a car.\""
                i "\" It applies to dancing too.\""
                show 3newalex198
                with dissolve
                " That guy didn't seem to have moved this whole time."
                hide 3newalex198
                show 3newalex209
                with dissolve
                " Alexandra pulls Izzy out of her chair."
                a "\" Alright Pussy.\""
                a "\" Take me out for a spin, then.\""
                a "\" Show me what you've got.\""
                hide 3newalex209
                show 3newalex210
                with dissolve
                " The girls take to the floor themselves."
                hide 3newalex210
                show 3newalex211
                with dissolve
                " And while they we're no more passionate with each other than they were with you."
                hide 3newalex211
                show 3newalex212
                with dissolve
                " Not having two left legs, helps."
                hide 3newalex212
                show 3newalex191
                with dissolve
                " You and the girls keep drinking."
                " With the occasional break to the floor."
                " But all of you are soon, tipsy."
                hide 3newalex191
                show 3newalex198
                with dissolve
                " And that guy still hasn't moved."
                hide 3newalex198
                show 3newalex214
                with dissolve
                a "\" Alright, what is it?\""
                a "\" Why do you look so jumpy?\""
                p "\" Nothing.\""
                a "\" That's what you said before.\""
                a "\" Now, what is it?\""
                hide 3newalex214
                show 3newalex198
                with dissolve
                p "\" It's this guy, over there.\""
                a "\" What about him.\""
                p "\" He's been watching us, ever since we got here.\""
                a "\" I doubt that.\""
                p "\" I'm telling you, he hasn't moved from that spot.\""
                p "\" And who wears sunglasses in a club?\""
                hide 3newalex198
                show 3newalex213
                with dissolve
                a "\" A jackass?\""
                p "\" Whatever.\""
                p "\" I'm telling you he's watching us.\""
                a "\" Probably just sent by my Dad, to make sure you don't give me a dicking on the dance-floor.\""
                p "\" There go my plans for tonight, I guess.\""
                hide 3newalex213
                show 3newalex214
                with dissolve
                a "\" Ha ha ha...\""
                a "\" Stop.\""
                hide 3newalex214
                show 3newalex206
                with dissolve
                i "\" I'm sure he meant, that he was planning to make sweet love to you.\""
                p "\" If that's what the kids are calling it.\""
                hide 3newalex206
                show 3newalex216
                with dissolve
                a "\" Listen, me and Izzy are pretty drunk anyway.\""
                a "\" If it will make you feel better about the guy, we'll leave.\""
                p "\" It would make me feel better actually.\""
                a "\" Let's go then.\""
                hide 3newalex216
                show back
                with dissolve
                show 3newalex217
                with dissolve
                p "\" Where are we going?\""
                p "\" Izzy's? Your Dad's? My place.\""
                a "\" Whatever's closest.\""
                p "\" That would be my place. But you already knew that.\""
                a "\" Is it? We had no idea.\" She says, sarcastically."
                i "\" Not a clue.\""
                p "\" Alright.\""
                hide 3newalex217
                show 3newalex218
                with dissolve
                " You manage to find a parking spot a block away from your building."
                a "\" Whoa...\""
                i "\" What?\""
                a "\" A little wobbly.\""
                i "\" You're drunk.\""
                a "\" So are you.\""
                hide 3newalex218
                show 3newalex219
                with dissolve
                " You notice another parked car a block away."
                p "\" Is that...\""
                p "\" Is that the guy from the club?\""
                hide 3newalex219
                show 3newalex220
                with dissolve
                p "\" Motherfucker!\""
                a "\" What?\""
                hide 3newalex220
                show 3newalex221
                with dissolve
                i "\" What's wrong?\""
                p "\" You girls head upstairs. Here are the keys.\""
                a "\" Don't need them. But where are you going.\""
                p "\" I'll be right behind you. Just go.\""
                a "\" Alright.\""
                hide 3newalex221
                show 3newalex222
                with dissolve
                " The girls leave, and you start heading towards the guy."
                hide 3newalex222
                show 3newalex223
                with dissolve
                " As soon as he sees you heading towards him, he speeds off."
                p "\" Come back here!\""
                hide 3newalex223
                show 3newalex224
                with dissolve
                p "\" You motherless cunt!\""
                p "\" Damn.\""
                p "\" He's gone.\""
                p "\" Better head upstairs.\""
                p "\" Damn.\""
                hide 3newalex224
                show 3newalex225
                with dissolve
                " When you get upstairs, you see the girls' discarded shoes."
                " And hear the shower running."
                hide 3newalex225
                show 3newalex226
                with dissolve
                i "\" Bah... I love going to clubs.\""
                i "\" But the stench you bring home...\""
                a "\" That's your mouth.\""
                i "\" Fuck off!\""
                a "\" I'm serious.\""
                a "\" It happens to all of us.\""
                p "\" Girls?\""
                i "\" We'll be right out.\""
                hide 3newalex226
                show 3newalex227
                with dissolve
                " You wait a minute for the girls to finish."
                hide 3newalex227
                show 3newalex228
                with dissolve
                a "\" All yours.\""
                a "\" We took all your towels, though.\""
                a "\" So you'll have to come out dick first. He he...\""
                hide 3newalex228
                show 3newalex229
                with dissolve
                i "\" She's joking about the towels.\""
                i "\" There's plenty left.\""
                i "\" Also put out a pair of boxers for you.\""
                i "\" No offense, but you must be drenched in ball sweat.\""
                p "\" Umm... Thanks. I guess.\""
                i "\" No problem.\""
                hide 3newalex229
                show 3newalex230
                with dissolve
                " You take your own shower."
                p "\" Man! She was right about the ball sweat.\""
                p "\" How come I didn't feel it?\""
                p "\" Fucking suit!\""
                hide 3newalex230
                show 3newalex231
                with dissolve
                a "\" Hey, are you going to be much longer?\""
                p "\" Why?\""
                a "\" We have a question.\""
                p "\" Are you sure you're not here just trying again to get a peek?\""
                hide 3newalex231
                show 3newalex232
                with dissolve
                " She slides the shower door wide open."
                a "\" Peek?\""
                a "\" If I told you to get naked because I wanted to examine your balls in detail, and maybe give them a gargle, you'd tell me to fuck myself?\""
                p "\" Good point.\""
                a "\" I don't need to peek.\""
                a "\" But we do have a question. He he...\""
                hide 3newalex232
                show 3newalex230
                with dissolve
                " You finish up your shower, and head to the bedroom."
                hide 3newalex230
                show 3newalex234
                with dissolve
                " When you get there, the girls are both in your bed."
                p "\" Ahh....much better.\""
                a "\" Tell us about it.\""
                a "\" Nothings more disgusting than club sweat.\""
                p "\" You had a question though?\""
                hide 3newalex234
                show 3newalex237
                with dissolve
                i "\" Don't ask it.\""
                i "\" You'll embarrass him.\""
                hide 3newalex237
                show 3newalex235
                with dissolve
                a "\" He doesn't get embarrassed. Not with us.\""
                p "\" Your question?\""
                a "\" Right.\""
                a "\" When you guys measure your dicks...\""
                p "\" Excuse me?\""
                hide 3newalex235
                show 3newalex236
                with dissolve
                a "\" When you measure your dicks.\""
                a "\" Do you measure from the top, or from the bottom?\""
                a "\" Cause the way we're thinking. You gain one inch or so, when measuring from the bottom.\""
                p "\" Deceitful.\""
                a "\" Ha!\""
                p "\" I don't think there's a standard.\""
                a "\" How did you do it?\""
                p "\" I didn't.\""
                hide 3newalex236
                show 3newalex235
                with dissolve
                a "\" You didn't?\""
                p "\" No.\""
                a "\" Never?\""
                p "\" Never.\""
                a "\" You never broke out a ruler, and...\""
                p "\" Nope.\""
                a "\" Wow.\""
                hide 3newalex235
                show 3newalex237
                with dissolve
                i "\" He won't admit it.\""
                i "\" I told you, you were embarrassing him.\""
                hide 3newalex237
                show 3newalex238
                with dissolve
                a "\" No, he's not.\""
                a "\" But I am surprised.\""
                a "\" I thought you all did it.\""
                p "\" That's more of a legend, I think.\""
                hide 3newalex238
                show 3newalex313
                with dissolve
                a "\" *Yawn*...\""
                a "\" Sleepy.\""
                hide 3newalex313
                show 3newalex237
                with dissolve
                i "\" Me too.\""
                hide 3newalex237
                show 3newalex238
                with dissolve
                a "\" Let's get to bed then.\""
                hide 3newalex238
                show 3newalex239
                with dissolve
                " The girls crawl in one half of the bed, leaving the other half to you."
                " You get in beside them, and close your eyes."
                hide 3newalex239
                show blackscreen
                with dissolve
                "..."
                "... ..."
                a "\" Puppy?\""
                p "\" Huh?\""
                a "\" [player_name]?\""
                hide blackscreen
                show 3newalex240
                with dissolve
                a "\" Are you sleeping?\""
                p "\" Not anymore.\""
                a "\" I'll never leave her, you know.\""
                p "\" Who?\""
                a "\" Izzy.\""
                hide 3newalex240
                show 3newalex241
                with dissolve
                p "\" I didn't ask you to leave her.\""
                a "\" And you never will. Right?\""
                call screen screen19

label izzymaybeleave:
                scene 3newalex241
                with dissolve
                p "\" I don't know.\""
                p "\" Maybe.\""
                show 3newalex242
                with dissolve
                " You pull her closer."
                a "\" I won't.\""
                p "\" I trust my dreams.\""
                a "\" Trust me too.\""
                a "\" It won't happen.\""
                jump ep3bigcont6

label neverleaveizzy:
                scene 3newalex241
                with dissolve
                p "\" Izzy?\""
                p "\" Can't imagine life without her.\""
                show 3newalex242
                with dissolve
                a "\" Neither can I.\""
                a "\" And I mean it.\""
                a "\" If you love her, she'll love you back.\""
                p "\" I'm sure.\""
                jump ep3bigcont6

label ep3bigcont6:
                scene 3newalex243
                with dissolve
                p "\" Is that why you woke me up?\""
                p "\" To ask me about Izzy?\""
                a "\" Well?\""
                p "\" You need not ask me that in the middle of the night. In my bed. With the excuse of alcohol to cover any action.\""
                a "\" You're reading too much into what I do.\""
                show 3newalex244
                with dissolve
                " You throw her towel away."
                a "\" What are you doing?\""
                p "\" Take a guess.\""
                hide 3newalex244
                show 3newalex245
                with dissolve
                " You slide your hand down to her pussy. Her moistness covering your fingers."
                p "\" You're wet, Alex.\""
                hide 3newalex245
                show 3newalex246
                with dissolve
                a "\" Mmmm...\""
                a "\" That's just because of the...\""
                p "\" Alcohol?\""
                a "\" Yes.\""
                p "\" Of course.\""
                hide 3newalex246
                show 3newalex247
                with dissolve
                " You bend over, 'til your lips almost touch hers."
                " Your mingled breath's entering your nostrils."
                " She eagerly opens her mouth to yours."
                p "\" No.\""
                a "\" What?\""
                p "\" I can't kiss you 'til you ask me to.\""
                a "\" Kiss me, then.\""
                hide 3newalex247
                show 3newalex248
                with dissolve
                a "\" Mmmm...\""
                hide 3newalex248
                show 3newalex249
                with dissolve
                a "\" Ahh...\""
                hide 3newalex249
                show 3newalex250
                with dissolve
                a "\" You didn't tell me you were...\""
                hide 3newalex250
                scene alexfinger animated with fade:
                    "2a1"
                    pause 0.05
                    "2a2"
                    pause 0.05
                    "2a3"
                    pause 0.05
                    "2a4"
                    pause 0.05
                    "2a5"
                    pause 0.05
                    "2a6"
                    pause 0.05
                    "2a7"
                    pause 0.05
                    "2a8"
                    pause 0.05
                    "2a9"
                    pause 0.05
                    "2a10"
                    pause 0.05
                    "2a11"
                    pause 0.05
                    "2a12"
                    pause 0.05
                    "2a13"
                    pause 0.05
                    "2a14"
                    pause 0.05
                    "2a15"
                    pause 0.05
                    "2a16"
                    pause 0.05
                    "2a17"
                    pause 0.05
                    "2a18"
                    pause 0.05
                    "2a19"
                    pause 0.05
                    "2a20"
                    pause 0.05
                    repeat
                a "\" Ahhh...\""
                a "\" Gently... Gently...\""
                $ renpy.pause ()
                show 3newalex251
                with dissolve
                " She grabs your head and kisses you deep."
                " Her mouth becoming voracious."
                " Her teeth, almost biting your lips."
                hide 3newalex251
                scene alexfinger animated with fade:
                    "2a1"
                    pause 0.03
                    "2a2"
                    pause 0.03
                    "2a3"
                    pause 0.03
                    "2a4"
                    pause 0.03
                    "2a5"
                    pause 0.03
                    "2a6"
                    pause 0.03
                    "2a7"
                    pause 0.03
                    "2a8"
                    pause 0.03
                    "2a9"
                    pause 0.03
                    "2a10"
                    pause 0.03
                    "2a11"
                    pause 0.03
                    "2a12"
                    pause 0.03
                    "2a13"
                    pause 0.03
                    "2a14"
                    pause 0.03
                    "2a15"
                    pause 0.03
                    "2a16"
                    pause 0.03
                    "2a17"
                    pause 0.03
                    "2a18"
                    pause 0.03
                    "2a19"
                    pause 0.03
                    "2a20"
                    pause 0.03
                    repeat
                " You increase you speed, her hips moving along with your hand."
                a "\" Ah...ah...ah...ahhh...\""
                $ renpy.pause ()
                show 3newalex252
                with dissolve
                " She grabs onto you. And you can sense an effort to muffle her moans."
                hide 3newalex252
                show 3newalex253
                with dissolve
                " She finally just buries her face in your shoulder."
                hide 3newalex253
                scene alexfinger animated with fade:
                    "2a1"
                    pause 0.02
                    "2a2"
                    pause 0.02
                    "2a3"
                    pause 0.02
                    "2a4"
                    pause 0.02
                    "2a5"
                    pause 0.02
                    "2a6"
                    pause 0.02
                    "2a7"
                    pause 0.02
                    "2a8"
                    pause 0.02
                    "2a9"
                    pause 0.02
                    "2a10"
                    pause 0.02
                    "2a11"
                    pause 0.02
                    "2a12"
                    pause 0.02
                    "2a13"
                    pause 0.02
                    "2a14"
                    pause 0.02
                    "2a15"
                    pause 0.02
                    "2a16"
                    pause 0.02
                    "2a17"
                    pause 0.02
                    "2a18"
                    pause 0.02
                    "2a19"
                    pause 0.02
                    "2a20"
                    pause 0.02
                    repeat
                a "\" Mmm...mmm...m...mmm...\""
                $ renpy.pause ()
                show 3newalex253
                with dissolve
                a "\"MMMMMMMmmmmmmmmm\""
                " She almost bites down on you as she begins shuddering."
                hide 3newalex253
                show 3newalex254
                with dissolve
                " And brings her hand down to stop you, and you insert your second finger."
                a "\" No.\""
                hide 3newalex254
                show 3newalex255
                with dissolve
                a "\" No.\""
                a "\" Give me... Give me a minute to catch my breath.\""
                a "\" Ahhh...\""
                i "\" You could've woke me, you know.\""
                hide 3newalex255
                show 3newalex256
                with dissolve
                a "\" Izzy?\""
                a "\" Izzy, it's not...\""
                i "\" What I think?\""
                i "\" Don't be silly.\""
                hide 3newalex256
                show 3newalex257
                with dissolve
                a "\" Babe, we were just...\""
                i "\" Getting off?\""
                i "\" It's fine.\""
                a "\" It's fine?\""
                hide 3newalex257
                show 3newalex258
                with dissolve
                i "\" Alex, I knew this was going to happen, way before you did.\""
                i "\" Why do you think I...\""
                a "\" What?\""
                i "\" Nothing.\""
                i "\" It's fine.\""
                a "\" It's not. I...\""
                hide 3newalex258
                show 3newalex259
                with dissolve
                " Before Alexandra can finish, Izzy gives you a deep kiss."
                " Do you kiss her back?"
                call screen screen20

label izzylastchanceno:
                scene 3newalex259
                " You allow her to kiss you, but you don't respond."
                jump ep3bigcont7

label izzylastchanceyes:
                scene 3newalex261
                with dissolve
                $ izzyaccept2 = True
                " You grab her by the back of her head, and forcefully respond to her kiss."
                i "\" Mmmm...\""
                jump ep3bigcont7

label ep3bigcont7:
                scene 3newalex260
                with dissolve
                i "\" You see?\""
                i "\" It's all good.\""
                a "\" Izzy...\""
                i "\" It is.\""
                show 3newalex262
                with dissolve
                " She stretches down again to sleep."
                i "\" Just wish you would've woken me.\""
                " And seems to fall back asleep almost immediately."
                hide 3newalex262
                show 3newalex263
                with dissolve
                a "\" Well, who saw that coming?\""
                p "\" Me, actually.\""
                a "\" Hmmm...\""
                hide 3newalex263
                show 3newalex264
                with dissolve
                " She wraps her legs around your hips, and sits in your lap."
                " Her still wet vagina, moistening the front of your boxers."
                p "\" Jesus.\""
                a "\" What?\""
                p "\" Don't breathe on me, I might cum.\""
                hide 3newalex264
                $ renpy.end_replay()
                show 3newalex265
                with dissolve
                a "\" He he...\""
                a "\" But this was a mistake.\""
                p "\" Izzy...\""
                a "\" It's not Izzy.\""
                p "\" Then what?\""
                a "\" In this dream of yours. Was our first time together an animal coupling after a drunken club scene?\""
                p "\" It didn't go into detail.\""
                a "\" Well, is that how you'd imagine it.\""
                p "\" So... Flowers, dinner, petals on the bed?\""
                a "\" Getting warmer.\""
                p "\" I see.\""
                p "\" What are you doing tomorrow night?\""
                hide 3newalex265
                show 3newalex266
                with dissolve
                " She climbs down off you, and you both lie down."
                a "\" I don't know. You tell me?\""
                p "\" Are you free for dinner?\""
                a "\" Are you cooking?\""
                p "\" Ouch.\""
                p "\" But I guess, I am.\""
                hide 3newalex266
                show 3newalex267
                with dissolve
                a "\" Hmmm...\""
                a "\" I suppose we could make the time.\""
                hide 3newalex267
                show 3newalex266
                with dissolve
                p "\" Tomorrow evening?\""
                a "\" Tomorrow.\""
                hide 3newalex266
                show 3newalex268
                with dissolve
                " With that, she turns around to hold Isabella while she sleeps."
                show blackscreen
                with dissolve
                "..."
                "... ..."
                hide blackscreen
                show 3newalex269
                with dissolve
                " A little later you wake up to Alex and whispering."
                if izzyaccept == True or izzyaccept1 == True or izzyaccept2 == True:
                    a "\" Izzy, it's just us now.\""
                    a "\" [player_name]'s asleep.\""
                    i "\" Yeah?\""
                    a "\" Are you ok?\""
                    i "\" Is this why you woke me?\""
                    a "\" Well...\""
                    i "\" It's [player_name].\""
                    i "\" He's our baby.\""
                    a "\" So, you're really ok?\""
                    i "\" No. You should've woke me up.\""
                    i "\" I've got a headache. But I could've still given a helping hand, or mouth, or whatever...\""
                    a "\" Ha ha...\""
                    a "\" You're not serious?\""
                    i "\" Why not.\""
                    a "\" He's invited us to dinner tomorrow night.\""
                    i "\" I'll bring the lube. Now please, can I get some sleep?\""
                    a "\" Are you sure you're ok?\""
                    i "\" Do I need to fuck him now to prove it to you? Or to film you doing it?\""
                    i "\" He loves me too. Not like he loves you, but...\""
                    i "\" He's our baby.\""
                    a "\" Alright.\""
                    jump ep3bigcont8
                else:
                    a "\" Izzy, it's just us now.\""
                    a "\" [player_name]'s asleep.\""
                    i "\" Yeah?\""
                    a "\" Are you ok?\""
                    i "\" No.\""
                    a "\" I'm sorry.\""
                    i "\" He won't love me.\""
                    i "\" And you'll leave me for him.\""
                    a "\" Never. I could never leave you.\""
                    i "\" Yes, you will.\""
                    a "\" No.\""
                    i "\" Promise?\""
                    a "\" I swear.\""
                    i "\" Thank you.\""
                    jump ep3bigcont8

label ep3bigcont8:
                scene 3newalex269
                with dissolve
                " Eventually sleep overcomes you."
                show blackscreen
                with dissolve
                "..."
                "... ..."
                a "\" See?\""
                a "\" I told you it's universal.\""
                hide blackscreen
                show 3newalex271
                with dissolve
                a "\" They all get it.\""
                i "\" Thats... That's thick.\""
                a "\" Curious?\""
                i "\" Kinda.\""
                hide 3newalex271
                show 3newalex272
                with dissolve
                a "\" He's up.\""
                p "\" Morning.\""
                i "\" Don't mind us.\""
                p "\" Where are my boxers?\""
                hide 3newalex272
                show 3newalex273
                with dissolve
                i "\" We need to hurry a bit.\""
                i "\" All the clothes we have here are those from the club.\""
                a "\" We need to go to your place and change.\""
                i "\" Yup.\""
                a "\" We'll need to get some of our clothes here.\""
                i "\" At least a drawer.\""
                if izzyaccept == True or izzyaccept1 == True or izzyaccept2 == True:
                    hide 3newalex273
                    show 3newalex275
                    with dissolve
                    " You stand up."
                    i "\" I don't get it, though.\""
                    i "\" If you took care of him last night...\""
                    a "\" Well...\""
                    i "\" You didn't?\""
                    hide 3newalex275
                    show 3newalex276
                    with dissolve
                    a "\" Puppy wants it to be special.\""
                    a "\" With both of us.\""
                    hide 3newalex276
                    show 3newalex277
                    with dissolve
                    i "\" I'm sure he does.\""
                    i "\" I'm also sure he wants to drain his balls.\""
                    hide 3newalex277
                    show 3newalex278
                    with dissolve
                    a "\" He doesn't care about that.\""
                    i "\" I'm sure he does.\""
                    a "\" No he doesn't.\""
                    a "\" Do you?\""
                    p "\" I've been told that I don't.\""
                    hide 3newalex278
                    show 3newalex280
                    with dissolve
                    a "\" See?\""
                    a "\" Told you.\""
                    hide 3newalex280
                    show 3newalex281
                    with dissolve
                    a "\" *Muah*\""
                    hide 3newalex281
                    show 3newalex282
                    with dissolve
                    " The girls head for the bathroom, and Alex says..."
                    a "\" We need to hurry a bit.\""
                    a "\" We don't want to be late.\""
                    p "\" Alright.\""
                    jump ep3bigcont9

                else:
                    hide 3newalex273
                    show 3newalex274
                    with dissolve
                    " The girls head for the bathroom, and Alex says..."
                    a "\" We need to hurry a bit.\""
                    a "\" We don't want to be late.\""
                    p "\" I'm getting up.\""
                    jump ep3bigcont9

label ep3bigcont9:
                scene 3newalex283
                with dissolve
                " You quickly shower and get dressed."
                p "\" Need to stop by Izzy's first.\""
                show 3newalex284
                with dissolve
                a "\" Well, we could go to school in these.\""
                a "\" But we might get expelled.\""
                i "\" Suspended, more likely.\""
                p "\" Right.\""
                hide 3newalex284
                show 3newalex285
                with dissolve
                " When you get outside, that guy is back."
                p "\" Damn it!\""
                hide 3newalex285
                show 3newalex286
                with dissolve
                a "\" What?\""
                p "\" That guy again.\""
                hide 3newalex286
                show 3newalex287
                with dissolve
                a "\" Do you really need to see suspicious characters everywhere?\""
                p "\" Yes.\""
                a "\" Why?\""
                p "\" I'm padding the job.\""
                hide 3newalex287
                show 3newalex288
                with dissolve
                a "\" I told you.\""
                a "\" He's probably one of my Dad's guys.\""
                p "\" I don't think so.\""
                a "\" I'm sure.\""
                a "\" Now, let's give him something to report.\""
                hide 3newalex288
                show 3newalex289
                with dissolve
                " She nuzzles up to you, and says in a loud voice, so that the whole street can hear her..."
                a "\" Damn it, why didn't you tell me your dick was that big?\""
                a "\" I can barely walk anymore.\""
                p "\" Alex, the whole street can hear you.\""
                a "\" Good. Let Dad get his money's worth.\" She whispers back."
                hide 3newalex289
                show 3newalex290
                with dissolve
                " Then again in a loud voice, while giving the guy the finger..."
                a "\" I'll need to start buying lube by the bucket!\""
                hide 3newalex290
                show 3newalex291
                with dissolve
                p "\" I don't think that guy works for your Father, Alex.\""
                a "\" Sure, he is.\""
                a "\" I love him, but you don't know how overbearing he can be.\""
                hide 3newalex291
                show 3newalex292
                with dissolve
                a "\" Now all I have to do, is walk with a limp.\""
                p "\" Let's go, Alex.\""
                hide 3newalex292
                show 3newalex291
                with dissolve
                "... ..."
                hide 3newalex291
                show 3newalex293
                with dissolve
                " After a quick visit at Izzy's, you get the girls to school."
                " Better start carrying some heavy fire power."
                hide 3newalex293
                show 3newalex294
                with dissolve
                " Then head to the agency."
                cl "\" Ha ha ha...\""
                cl "\" I can't believe it.\""
                yuri "\" Believe.\""
                " These two seem to be getting along."
                p "\" Yuri!\""
                hide 3newalex294
                show 3newalex295
                with dissolve
                yuri "\" Yeah?\""
                p "\" Can you handle everything alone today?\""
                p "\" I have to go do something.\""
                yuri "\" Sure. That's what I'm here for.\""
                p "\" Thanks.\""
                hide 3newalex295
                show 3newalex296
                with dissolve
                " You go to the gun range."
                p "\" Jenny?\""
                hide 3newalex296
                show 3newalex297
                with dissolve
                jen "\" Oh, hi!\""
                jen "\" Haven't seen you in a while.\""
                p "\" Been busy.\""
                jen "\" No doubt.\""
                p "\" Listen. I need your help with something.\""
                hide 3newalex297
                show 3newalex298
                with dissolve
                jen "\" With what?\""
                p "\" I need a gun.\""
                jen "\" You have a gun.\""
                p "\" Something more... Powerful.\""
                hide 3newalex298
                show 3newalex299
                with dissolve
                jen "\" I see...\""
                jen "\" How powerful?\""
                p "\" Something that could kill a car.\""
                jen "\" Hmmm...\""
                hide 3newalex299
                show 3newalex300
                with dissolve
                jen "\" I think that you should meet my husband.\""
                p "\" Your husband?\""
                jen "\" This way.\""
                hide 3newalex300
                show 3newalex301
                with dissolve
                jen "\" There he is.\""
                jen "\" Titus!\""
                hide 3newalex301
                show 3newalex302
                with dissolve
                jen "\" My baby.\""
                p "\" Your husband?\""
                hide 3newalex302
                show 3newalex303
                with dissolve
                jen "\" No man could ever satisfy me, like he does.\""
                p "\" No doubt.\""
                p "\" Does he have a Sister?\""
                hide 3newalex303
                show 3newalex304
                with dissolve
                jen "\" Maybe...\""
                jen "\" But it will cost you.\""
                jump ep4
