label ep24:
                scene 24newalex1
                with dissolve
                " You go to wake her up."
                p "\" Hey.\""
                p "\" Hey, wake up.\""
                a "\" MMMMmmm...\""
                p "\" Wake up.\""
                p "\" You can't sleep in the kitchen.\""
                show 24newalex2
                with dissolve
                a "\" Mmm...\""
                a "\" I was tired.\""
                p "\" I know.\""
                p "\" But you can't sleep here.\""
                hide 24newalex2
                show 24newalex3
                with dissolve
                a "\" Where is dad?\""
                p "\" His room, I imagine.\""
                p "\" I just got back from Izzy's.\""
                a "\" Izzy's?\""
                p "\" Yeah.\""
                p "\" She's sleeping over there tonight.\""
                hide 24newalex3
                show 24newalex4
                with dissolve
                " She slowly gets up and puts her arms around you."
                a "\" Sleeping over there?\""
                a "\" Why?\""
                p "\" Wants to spend more time with her mother.\""
                p "\" She's doing pretty good it seems.\""
                hide 24newalex4
                show 24newalex5
                with dissolve
                a "\" Nice.\""
                a "\" Both our parents are doing better.\""
                p "\" You're not.\""
                hide 24newalex5
                show 24newalex212
                with dissolve
                a "\" What?\""
                p "\" You're tired as all hell.\""
                p "\" It's obvious.\""
                a "\" Not really.\""
                a "\" It's not like I'm doing a triathlon.\""
                p "\" No.\""
                p "\" But you've been very emotional lately.\""
                hide 24newalex212
                show 24newalex213
                with dissolve
                a "\" Is that a dig?\""
                p "\" You know better than that.\""
                p "\" Emotions can exhaust you too.\""
                hide 24newalex213
                show 24newalex5
                with dissolve
                a "\" How would you know?\""
                p "\" I know.\""
                hide 24newalex5
                show 24newalex6
                with dissolve
                " You kiss her hair."
                a "\" He he...\""
                a "\" Careful.\""
                a "\" You're gonna make me think you've gone all gooey.\""
                p "\" I could live with that.\""
                hide 24newalex6
                show 24newalex7
                with dissolve
                a "\" He he...\""
                a "\" You could?\""
                p "\" There's worse things a man can be.\""
                a "\" Maybe.\""
                hide 24newalex7
                show 24newalex214
                with dissolve
                " She kisses you again."
                hide 24newalex214
                show 24newalex7
                with dissolve
                a "\" But I prefer you like this.\""
                a "\" Let's go see dad.\""
                hide 24newalex7
                show 24newalex8
                with dissolve
                " You go to Boris's bedroom, and Alex jumps straight on the bed."
                a "\" Daddy!\""
                b "\" Goran...\""
                a "\" What? Does anything hurt?\""
                " He shakes his head."
                hide 24newalex8
                show 24newalex9
                with dissolve
                a "\" Why the sour puss, then?\""
                a "\" Like you just had bitter coffee.\""
                hide 24newalex9
                show 24newalex10
                with dissolve
                b "\" Sigh...\""
                " He shakes his head again."
                p "\" Alex.\""
                p "\" Maybe your dad would like to rest for a while.\""
                hide 24newalex10
                show 24newalex11
                with dissolve
                " He vigorously nods his head."
                p "\" He's tired too.\""
                hide 24newalex11
                show 24newalex9
                with dissolve
                a "\" Good. You should rest.\""
                p "\" Alone?\""
                p "\" It's hard for him to close his eyes and rest, with you hovering over him every second.\""
                p "\" Asking him if he needs anything.\""
                hide 24newalex9
                show 24newalex12
                with dissolve
                a "\" You're saying I'm bugging my dad?\""
                p "\" I'm saying he could use a breather from the constant attention.\""
                p "\" Isn't that so, sir?\""
                hide 24newalex12
                show 24newalex13
                with dissolve
                " He shakes his head, but looks at you pleadingly."
                a "\" He's shaking his head.\""
                hide 24newalex13
                show 24newalex12
                with dissolve
                p "\" Could you give us five minutes anyway?\""
                hide 24newalex12
                show 24newalex14
                with dissolve
                a "\" Treachery!\" she says mockingly."
                a "\" Everyone turns against me.\""
                p "\" Alex?\""
                hide 24newalex14
                show 24newalex15
                with dissolve
                " She leaves."
                " And you notice the faint glimmer of a smile, as she passes by you."
                hide 24newalex15
                show 24newalex16
                with dissolve
                " As soon as she leaves, Boris lies back down."
                b "\" Sigh...\""
                p "\" You need a little break from her affection, boss?\""
                b "\" He he...\""
                " He nods."
                p "\" Hope you get back to talking soon.\""
                p "\" I'm not good at this running shit stuff.\""
                p "\" Doing my best, though.\""
                hide 24newalex16
                show 24newalex17
                with dissolve
                " He immediately sits up."
                p "\" Boss?\""
                hide 24newalex17
                show 24newalex18
                with dissolve
                b "\" Asdagrhgrh...\""
                p "\" Still can't talk. I know.\""
                b "\" Asdagrhgrh...\""
                p "\" You want me to tell you what's going on?\""
                hide 24newalex18
                show 24newalex17
                with dissolve
                " He nods."
                " Do you inform him?"
                call screen screen73

label ep24tdontellboris:
                scene 24newalex17
                with dissolve
                " You decide it's best to not say too much."
                p "\" Nothing we can't handle for now.\""
                p "\" Me and Alex.\""
                p "\" You just rest, boss.\""
                p "\" It's fine.\""
                p "\" You just rest.\""
                show 24newalex16
                with dissolve
                " He lies back down."
                p "\" Sleep, boss.\""
                jump ep24cont1

label ep24tellboris:
                $ borispts = borispts + 1
                scene 24newalex17
                with dissolve
                p "\" Ok, boss.\""
                show 24newalex19
                with dissolve
                " You tell him about what happened."
                " How Alex had all the capos stay over under your watch."
                " You left out Anton's death."
                hide 24newalex19
                show 24newalex20
                p "\" Now it's just us.\""
                p "\" Well, except for Dima.\""
                b "\" Huh...\""
                hide 24newalex20
                show 24newalex21
                with dissolve
                b "\" Asdagrhgrh...\""
                p "\" No.\""
                p "\" Still can't understand you, boss.\""
                hide 24newalex21
                show 24newalex16
                with dissolve
                " He lies back down."
                p "\" I'll let you rest, then.\""
                p "\" Get some sleep, chief.\""
                jump ep24cont1

label ep24cont1:
                scene 24newalex22
                with dissolve
                " You go to Alex's room."
                p "\" Alexandra?\""
                a "\" Yeah?\""
                p "\" Hope you didn't take it the wrong way.\""
                p "\" Sending you away.\""
                show 24newalex23
                with dissolve
                a "\" Don't be silly.\""
                a "\" You're right. I shouldn't be smothering him.\""
                a "\" Besides. I have so much else to do.\""
                p "\" Running around naked?\""
                hide 24newalex23
                show 24newalex24
                with dissolve
                a "\" Is that something you'd have a problem with?\""
                p "\" Not particularly.\""
                hide 24newalex24
                show 24newalex27
                with dissolve
                a "\" I didn't think so.\""
                a "\" I have to dissapoint you, though.\""
                a "\" I'm just changing.\""
                p "\" Rats!\""
                a "\" He he...\""
                hide 24newalex27
                show 24newalex24
                with dissolve
                p "\" Listen. I have to get in touch with James...\""
                a "\" James?\" she cuts you off."
                p "\" One of my boys.\""
                p "\" The point is, I won't be coming back tonight.\""
                p "\" I'm gonna sleep over at Isabella's.\""
                hide 24newalex24
                show 24newalex25
                with dissolve
                a "\" You two plan to run away together?\""
                p "\" As soon as your back is turned.\""
                p "\" Have our spot at Ipamina beach all planned out.\""
                a "\" Aha.\""
                hide 24newalex25
                show 24newalex27
                with dissolve
                a "\" Well, I'll be doing some gardening.\""
                a "\" So it's your loss, really.\""
                p "\" Sounds like it.\""
                hide 24newalex27
                show 24newalex25
                with dissolve
                p "\" Also. I didn't tell your dad about Ant...\""
                hide 24newalex25
                show 24newalex26
                with dissolve
                a "\" No!\" she cuts you off."
                a "\" We don't mention that name.\""
                p "\" Alex.\""
                a "\" It never happened.\""
                a "\" Nothing ever happened. Trust me on this.\""
                p "\" Alright.\""
                hide 24newalex26
                show 24newalex28
                with dissolve
                " She puts on some clothes."
                a "\" Well, off you go.\""
                a "\" Leave me alone in my bed.\""
                a "\" You and Izzy both.\""
                p "\" I'll come kiss you goodnight this evening.\""
                hide 24newalex28
                show 24newalex215
                with dissolve
                a "\" Do that.\""
                hide 24newalex215
                show 24newalex29
                with dissolve
                " You leave Alex and call James."
                ja "\" Boss?\""
                p "\" You're there, right.\""
                ja "\" There?\""
                p "\" Where I told you to stand guard, where else.\""
                ja "\" Yeah, yeah...\""
                ja "\" I'm just about to leave, though.\""
                p "\" What?\""
                ja "\" I'm getting one of the other boys to cover for me.\""
                ja "\" I'm gonna go see Hugo's mom.\""
                ja "\" Someone...someone should tell her.\""
                p "\" Ah.\""
                p "\" Right. I should be there too.\""
                ja "\" You wanna come?\""
                p "\" Yeah. Come pick me up.\""
                hide 24newalex29
                show 24newalex30
                with dissolve
                " James arrives half an hour later."
                ja "\" Boss?\""
                p "\" You're on your way to her now?\""
                ja "\" Yeah.\""
                p "\" Let's go.\""
                hide 24newalex30
                show back1
                with dissolve
                show 24newalex31
                with dissolve
                " You get in the car."
                ol "\" I see you.\""
                p "\" Ohh...\""
                p "\" Oh, hi. We...we met before.\""
                hide 24newalex31
                show 24newalex32
                with dissolve
                ja "\" That's my sister, boss.\""
                ja "\" Don't mind her.\""
                ja "\" She's...\""
                hide 24newalex32
                show 24newalex33
                with dissolve
                ol "\" What am I?\""
                hide 24newalex33
                show 24newalex34
                with dissolve
                ja "\" I didn't mean nothing, Liv.\""
                hide 24newalex34
                show 24newalex33
                with dissolve
                ol "\" You seem troubled.\" she says looking at you."
                p "\" I am.\""
                ol "\" Is it because of Hugo?\""
                ol "\" There's no need for that.\""
                ol "\" He was a troubled soul.\""
                ol "\" He...\""
                hide 24newalex33
                show 24newalex32
                with dissolve
                ja "\" Liv, I love you. But shut the hell up.\""
                hide 24newalex32
                show 24newalex35
                with dissolve
                " You arrive in front of a house."
                hide 24newalex35
                show 24newalex36
                with dissolve
                ja "\" This is her place.\""
                p "\" Hugo's mom?\""
                ja "\" Miss. Teresa.\""
                ja "\" Shit!\""
                p "\" There's no point in delaying it.\""
                p "\" Let's just go in.\""
                hide 24newalex36
                show 24newalex35
                with dissolve
                " You knock on the door."
                hide 24newalex35
                show 24newalex37
                with dissolve
                " An elder lady lets you in."
                ter "\" Oh, hello.\""
                ter "\" James?\""
                ter "\" What are you doing here, darling?\""
                hide 24newalex37
                show 24newalex38
                with dissolve
                ja "\" Mrs. Teresa. I...\""
                ja "\" I'm sorry to disturb you, ma'am.\""
                hide 24newalex38
                show 24newalex39
                with dissolve
                ter "\" Look at you.\""
                ter "\" You look so nice in your little suit.\""
                ter "\" If you're looking for Hugo, he isn't here though.\""
                hide 24newalex39
                show 24newalex38
                with dissolve
                ja "\" No, ma'am.\""
                ja "\" I'm not looking for him.\""
                hide 24newalex38
                show 24newalex39
                with dissolve
                ter "\" When you see him. Tell him I'm gonna kick his ass.\""
                ter "\" Last time he was here, he stole 100$ from my wallet before he left.\""
                ter "\" I know it was him.\""
                hide 24newalex39
                show 24newalex41
                with dissolve
                ja "\" Ma'am, it's not...\""
                ja "\" It's you I came to see.\""
                ja "\" Why don't you have a seat.\""
                hide 24newalex41
                show 24newalex40
                with dissolve
                ter "\" And who's this?\" she asks looking at you."
                p "\" I'm a friend.\""
                p "\" A friend of Hugo's.\""
                hide 24newalex40
                show 24newalex41
                with dissolve
                ja "\" Ma'am. Please just have a seat.\""
                hide 24newalex41
                show 24newalex42
                with dissolve
                " They sit down."
                ter "\" What is it, dear.\""
                ter "\" You're being very mysterious.\""
                hide 24newalex42
                show 24newalex43
                with dissolve
                ol "\" She won't take it well.\""
                ol "\" One can't blame her. But it's for the best.\""
                p "\" What?\""
                hide 24newalex43
                show 24newalex44
                with dissolve
                ol "\" Hugo was a kind soul.\""
                p "\" Was he?\""
                ol "\" Deep down, yes.\""
                ol "\" But not the best at controlling his emotions.\""
                p "\" I can relate.\""
                hide 24newalex44
                show 24newalex45
                with dissolve
                ol "\" No, Cherubael.\""
                ol "\" Control is anathema to you.\""
                hide 24newalex45
                show 24newalex46
                with dissolve
                " James tells Teresa about Hugo."
                ter "\" No.\""
                ter "\" No, they're wrong.\""
                hide 24newalex46
                show 24newalex47
                with dissolve
                ol "\" Poor thing.\""
                hide 24newalex47
                show 24newalex48
                with dissolve
                ter "\" No!\""
                ter "\" I'm sure that can't be.\""
                ja "\" Mrs. Teresa.\""
                ter "\" You said you're not sure.\""
                ja "\" Well, we're not.\""
                ter "\" That settles it then.\""
                hide 24newalex48
                show 24newalex49
                with dissolve
                ter "\" No!\""
                hide 24newalex49
                show 24newalex50
                with dissolve
                ol "\" She needs me.\""
                hide 24newalex50
                show 24newalex51
                with dissolve
                ter "\" And who are you again?\" Mrs Theresa turns on you with anger in her voice."
                p "\" Ma'am, I'm...\""
                hide 24newalex51
                show 24newalex53
                with dissolve
                " Olivia rushes to her."
                ol "\" He's a friend.\""
                ol "\" He's going to kill the man that killed Hugo.\""
                ter "\" What?\""
                ol "\" I know.\""
                hide 24newalex53
                show 24newalex52
                with dissolve
                ja "\" Stop it, Liv.\""
                hide 24newalex52
                show 24newalex53
                with dissolve
                ol "\" It's going to be ok, ma'am.\""
                hide 24newalex53
                show 24newalex52
                with dissolve
                ja "\" Olivia!\""
                ja "\" Why don't the two of you wait outside for a minute.\""
                hide 24newalex52
                show 24newalex54
                with dissolve
                ol "\" You still seem worried, ma'am.\""
                p "\" Olivia.\""
                p "\" Let's give them a minute.\""
                hide 24newalex54
                show 24newalex55
                with dissolve
                " You take her outside."
                ol "\" I'm trying to tell her.\""
                ol "\" There's no reason to be sad.\""
                p "\" You're special, alright.\""
                hide 24newalex55
                show 24newalex56
                with dissolve
                ol "\" That's what James says.\""
                p "\" He's not wrong.\""
                p "\" But what did you say?\""
                p "\" I'm gonna do what to the guy that killed Hugo?\""
                hide 24newalex56
                show 24newalex59
                with dissolve
                ol "\" I'm sure of it.\""
                ol "\" His blood is on your hands.\""
                ol "\" I saw it.\""
                ol "\" You should trust what I see.\""
                hide 24newalex59
                show 24newalex56
                with dissolve
                p "\" I trust my dreams.\""
                ol "\" Huh?\""
                hide 24newalex56
                show 24newalex57
                with dissolve
                " James comes back out."
                ja "\" Poor woman.\""
                ja "\" Liv, can you stay with her?\""
                hide 24newalex57
                show 24newalex58
                with dissolve
                ol "\" Of course.\""
                hide 24newalex58
                show 24newalex57
                with dissolve
                ja "\" Make her tea, cry with her, whatever she needs.\""
                ja "\" But...\""
                ja "\" But don't do what you do.\""
                hide 24newalex57
                show 24newalex58
                with dissolve
                ol "\" What do I do?\""
                hide 24newalex58
                show 24newalex57
                with dissolve
                ja "\" You know.\""
                ja "\" Talk nonsense.\""
                hide 24newalex57
                show 24newalex58
                with dissolve
                ol "\" I'll be good.\""
                hide 24newalex58
                scene back1
                with dissolve
                show 24newalex60
                with dissolve
                " You leave Olivia with Mrs. Teresa while James drives you back to the villa."
                ja "\" I hope my sister doesn't fill poor Mrs. Teresa's head with nonsense.\""
                p "\" I'm not sure it's as nonsense as you think.\""
                ja "\" What else is it?\""
                hide 24newalex60
                show 24newalex34
                with dissolve
                ja "\" And she's wrong, anyway.\""
                ja "\" I know.\""
                ja "\" You're not gonna kill the guy that killed Hugo.\""
                hide 24newalex34
                show 24newalex32
                with dissolve
                ja "\" I will.\""
                hide 24newalex32
                show 24newalex61
                with dissolve
                " You get back to the villa."
                p "\" For now I still want you in front of that apartment.\""
                ja "\" Sure.\""
                ja "\" I'll call you if something comes up tonight.\""
                p "\" Don't worry. I'll be there too.\""
                hide 24newalex61
                show 24newalex215
                with dissolve
                " You look around for Alex."
                hide 24newalex215
                show 24newalex62
                with dissolve
                " And you find her outside, by the pool."
                p "\" Hey.\""
                hide 24newalex62
                show 24newalex63
                with dissolve
                a "\" Hey.\""
                p "\" What are you doing out here?\""
                a "\" Just some gardening.\""
                a "\" I won't let mom's flowers die.\""
                p "\" That's nice.\""
                p "\" I'm gonna go sleep at Izzy's tonight.\""
                a "\" You said that.\""
                p "\" I also said I'd come kiss you goodnight.\""
                hide 24newalex63
                show 24newalex64
                with dissolve
                " You give her a kiss."
                hide 24newalex64
                show 24newalex65
                with dissolve
                a "\" Be good, now.\""
                a "\" Don't do anything I wouldn't do.\""
                p "\" And what's that?\""
                a "\" Off the top of my head? I can't really think of anything.\""
                hide 24newalex65
                show 24newalex63
                with dissolve
                a "\" Good night, babe.\""
                p "\" Good night.\""
                hide 24newalex63
                show 24newalex66
                with dissolve
                " You pass by Dima as you leave."
                p "\" Back on post, I see.\""
                p "\" Good.\""
                p "\" Still have that bottle, though.\""
                hide 24newalex66
                show 24newalex67
                with dissolve
                di "\" So?\""
                di "\" When does the master plan of your come together?\""
                p "\" Have patience.\""
                p "\" We threw a stone in the water.\""
                p "\" Now we watch to see what ripples it makes.\""
                hide 24newalex67
                show 24newalex68
                with dissolve
                " You head over to Izzy's."
                i "\" Hey.\""
                p "\" Hey.\""
                ag "\" Who is it dear?\""
                hide 24newalex68
                show 24newalex69
                with dissolve
                i "\" It's [player_name], momma.\""
                hide 24newalex69
                show 24newalex70
                with dissolve
                ag "\" [player_name]?\""
                ag "\" Your friend, yes.\""
                " You see Agatha is awake, and conscious of what she's doing."
                " Also dressed in something else besides her bathrobe."
                p "\" Ma'am.\""
                hide 24newalex70
                show 24newalex69
                with dissolve
                i "\" Be nice, mom.\""
                hide 24newalex69
                show 24newalex70
                with dissolve
                ag "\" I'm always nice, dear.\""
                ag "\" Especially to handsome young men.\""
                i "\" Ugh...\""
                hide 24newalex70
                show 24newalex71
                with dissolve
                i "\" Mind giving us some...\""
                p "\" Space? No problem.\""
                p "\" I'll just wait in your bedroom.\""
                hide 24newalex71
                show 24newalex72
                with dissolve
                " As you pass by Agatha, you hear her whisper..."
                ag "\" Wait in her bedroom.\""
                ag "\" And my daughter looks at me like I don't know how to act.\""
                ag "\" Heh.\""
                hide 24newalex72
                show 24newalex73
                with dissolve
                " You retreat to Izzy's bedroom and call Alex."
                a "\" Yeah?\""
                a "\" What's up?\""
                p "\" Nothing in particular.\""
                p "\" I've just been exiled for a bit.\""
                a "\" So, you call me out of boredom?\""
                hide 24newalex73
                show 24newalex74
                with dissolve
                p "\" Something like that.\""
                a "\" Two needy boys. That's what I have.\""
                a "\" You and dad both.\""
                p "\" There is no end to your suffering.\""
                a "\" He he...\""
                a "\" Nope.\""
                hide 24newalex74
                show 24newalex73
                with dissolve
                " You sit a while just chatting with Alex, while waiting for Izzy."
                hide 24newalex73
                show 24newalex75
                with dissolve
                " She arrives a little while later."
                hide 24newalex75
                show 24newalex76
                with dissolve
                i "\" Momma has gone to bed.\""
                if izzyin == True:
                    p "\" How is she?\""
                    hide 24newalex76
                    show 24newalex84
                    with dissolve
                    " She sits down on the bed."
                    i "\" You saw her.\""
                    i "\" She's good.\""
                    i "\" Very good.\""
                    hide 24newalex84
                    show 24newalex85
                    with dissolve
                    i "\" But that's not what I want to talk about right now.\""
                    p "\" No?\""
                    label galleryScene12:
                    p "\" What do you want to talk about, then.\""
                    i "\" Who says I want to talk at all?\""
                    hide 24newalex85
                    show 24newalex86
                    with dissolve
                    p "\" You had something else in mind?\""
                    i "\" A couple of things.\""
                    i "\" It mostly involves Pyle, though.\""
                    p "\" Girl, I swear...\""
                    i "\" He he...\""
                    i "\" Let's just see you out of those clothes.\""
                    hide 24newalex86
                    show 24newalex87
                    with dissolve
                    " You take off your clothes."
                    p "\" Like what you see?\""
                    hide 24newalex87
                    show 24newalex88
                    with dissolve
                    i "\" I do.\""
                    i "\" Doesn't mean it can't be improved upon.\""
                    p "\" Improved? How?\""
                    i "\" Not everything is as erect as it should be.\""
                    hide 24newalex88
                    show 24newalex89
                    with dissolve
                    i "\" But I think I can help with that.\" she says while kissing your chest."
                    hide 24newalex89
                    show 24newalex90
                    with dissolve
                    " Then slowly moving lower."
                    p "\" I see where this is going.\""
                    i "\" How perceptive.\""
                    scene izzyoral2 animated with fade:
                        "38a00_nvidia.webp"
                        pause 0.06
                        "38a01_nvidia.webp"
                        pause 0.06
                        "38a02_nvidia.webp"
                        pause 0.06
                        "38a03_nvidia.webp"
                        pause 0.06
                        "38a04_nvidia.webp"
                        pause 0.06
                        "38a05_nvidia.webp"
                        pause 0.06
                        "38a06_nvidia.webp"
                        pause 0.06
                        "38a07_nvidia.webp"
                        pause 0.07
                        "38a08_nvidia.webp"
                        pause 0.07
                        "38a09_nvidia.webp"
                        pause 0.07
                        "38a10_nvidia.webp"
                        pause 0.07
                        "38a11_nvidia.webp"
                        pause 0.07
                        "38a12_nvidia.webp"
                        pause 0.07
                        "38a13_nvidia.webp"
                        pause 0.07
                        "38a14_nvidia.webp"
                        pause 0.07
                        "38a15_nvidia.webp"
                        pause 0.07
                        "38a16_nvidia.webp"
                        pause 0.07
                        "38a17_nvidia.webp"
                        pause 0.07
                        "38a18_nvidia.webp"
                        pause 0.07
                        "38a19_nvidia.webp"
                        pause 0.07
                        "38a20_nvidia.webp"
                        pause 0.07
                        "38a21_nvidia.webp"
                        pause 0.07
                        "38a22_nvidia.webp"
                        pause 0.07
                        "38a23_nvidia.webp"
                        pause 0.07
                        "38a24_nvidia.webp"
                        pause 0.07
                        "38a25_nvidia.webp"
                        pause 0.07
                        "38a26_nvidia.webp"
                        pause 0.07
                        "38a27_nvidia.webp"
                        pause 0.07
                        "38a28_nvidia.webp"
                        pause 0.07
                        "38a29_nvidia.webp"
                        pause 0.07
                        "38a30_nvidia.webp"
                        pause 0.07
                        "38a31_nvidia.webp"
                        pause 0.07
                        "38a32_nvidia.webp"
                        pause 0.07
                        "38a33_nvidia.webp"
                        pause 0.07
                        "38a34_nvidia.webp"
                        pause 0.07
                        "38a35_nvidia.webp"
                        pause 0.07
                        "38a36_nvidia.webp"
                        pause 0.07
                        "38a37_nvidia.webp"
                        pause 0.07
                        "38a38_nvidia.webp"
                        pause 0.07
                        "38a39_nvidia.webp"
                        pause 0.07
                        repeat
                    i "\" Mmm...\""
                    " She gently wraps her lips around your shaft."
                    i "\" Mmmmm...\""
                    p "\" Yes.\""
                    p "\" Good girl.\""
                    $ renpy.pause ()
                    scene izzyoral2 animated with fade:
                        "38a00_nvidia.webp"
                        pause 0.04
                        "38a01_nvidia.webp"
                        pause 0.04
                        "38a02_nvidia.webp"
                        pause 0.04
                        "38a03_nvidia.webp"
                        pause 0.04
                        "38a04_nvidia.webp"
                        pause 0.04
                        "38a05_nvidia.webp"
                        pause 0.04
                        "38a06_nvidia.webp"
                        pause 0.04
                        "38a07_nvidia.webp"
                        pause 0.04
                        "38a08_nvidia.webp"
                        pause 0.04
                        "38a09_nvidia.webp"
                        pause 0.04
                        "38a10_nvidia.webp"
                        pause 0.04
                        "38a11_nvidia.webp"
                        pause 0.04
                        "38a12_nvidia.webp"
                        pause 0.04
                        "38a13_nvidia.webp"
                        pause 0.04
                        "38a14_nvidia.webp"
                        pause 0.04
                        "38a15_nvidia.webp"
                        pause 0.04
                        "38a16_nvidia.webp"
                        pause 0.04
                        "38a17_nvidia.webp"
                        pause 0.04
                        "38a18_nvidia.webp"
                        pause 0.04
                        "38a19_nvidia.webp"
                        pause 0.04
                        "38a20_nvidia.webp"
                        pause 0.04
                        "38a21_nvidia.webp"
                        pause 0.04
                        "38a22_nvidia.webp"
                        pause 0.04
                        "38a23_nvidia.webp"
                        pause 0.04
                        "38a24_nvidia.webp"
                        pause 0.04
                        "38a25_nvidia.webp"
                        pause 0.04
                        "38a26_nvidia.webp"
                        pause 0.04
                        "38a27_nvidia.webp"
                        pause 0.04
                        "38a28_nvidia.webp"
                        pause 0.04
                        "38a29_nvidia.webp"
                        pause 0.04
                        "38a30_nvidia.webp"
                        pause 0.04
                        "38a31_nvidia.webp"
                        pause 0.04
                        "38a32_nvidia.webp"
                        pause 0.04
                        "38a33_nvidia.webp"
                        pause 0.04
                        "38a34_nvidia.webp"
                        pause 0.04
                        "38a35_nvidia.webp"
                        pause 0.04
                        "38a36_nvidia.webp"
                        pause 0.04
                        "38a37_nvidia.webp"
                        pause 0.04
                        "38a38_nvidia.webp"
                        pause 0.04
                        "38a39_nvidia.webp"
                        pause 0.04
                        repeat
                    i "\" Mmm...\""
                    " She then picks up the pace."
                    p "\" Yes.\""
                    i "\" Mmm...\""
                    p "\" Ok.\""
                    p "\" Ok, that's enough.\""
                    $ renpy.pause ()
                    scene 24newalex91
                    with dissolve
                    " You push her back."
                    i "\" Hey!\""
                    p "\" That's enough.\""
                    show 24newalex92
                    with dissolve
                    i "\" But me and Pyle were just getting acquainted.\""
                    p "\" First of all, stop saying Pyle.\""
                    p "\" if you need to use a soldier's name, it's Rambo, ok.\""
                    i "\" He he...\""
                    hide 24newalex92
                    show 24newalex93
                    with dissolve
                    " You get on top of her."
                    p "\" Second of all, there are other ways for the two of you to get acquainted.\""
                    hide 24newalex93
                    show 24newalex94
                    with dissolve
                    " Your dick rubs against her pussy as you open her legs."
                    hide 24newalex94
                    show 24newalex95
                    with dissolve
                    i "\" Hmmm...\""
                    i "\" Don't confuse me with Claire, now.\""
                    p "\" He likes what he likes.\""
                    i "\" Pyle?\""
                    p "\" Rambo, I said!\""
                    i "\" He he...\""
                    hide 24newalex95
                    show 24newalex96
                    with dissolve
                    " You help her slip out of her clothes."
                    hide 24newalex96
                    show 24newalex97
                    with dissolve
                    " And slide yourself inside her."
                    hide 24newalex97
                    show 24newalex98
                    with dissolve
                    " She wraps her arms and legs around you, and holds you close."
                    scene izzysex animated with fade:
                        "39a00_nvidia.webp"
                        pause 0.04
                        "39a01_nvidia.webp"
                        pause 0.04
                        "39a02_nvidia.webp"
                        pause 0.04
                        "39a03_nvidia.webp"
                        pause 0.04
                        "39a04_nvidia.webp"
                        pause 0.04
                        "39a05_nvidia.webp"
                        pause 0.04
                        "39a06_nvidia.webp"
                        pause 0.04
                        "39a07_nvidia.webp"
                        pause 0.04
                        "39a08_nvidia.webp"
                        pause 0.04
                        "39a09_nvidia.webp"
                        pause 0.04
                        "39a10_nvidia.webp"
                        pause 0.04
                        "39a11_nvidia.webp"
                        pause 0.05
                        "39a12_nvidia.webp"
                        pause 0.05
                        "39a13_nvidia.webp"
                        pause 0.05
                        "39a14_nvidia.webp"
                        pause 0.05
                        "39a15_nvidia.webp"
                        pause 0.05
                        "39a16_nvidia.webp"
                        pause 0.05
                        "39a17_nvidia.webp"
                        pause 0.05
                        "39a18_nvidia.webp"
                        pause 0.05
                        "39a19_nvidia.webp"
                        pause 0.05
                        "39a20_nvidia.webp"
                        pause 0.03
                        "39a21_nvidia.webp"
                        pause 0.03
                        "39a22_nvidia.webp"
                        pause 0.03
                        "39a23_nvidia.webp"
                        pause 0.03
                        "39a24_nvidia.webp"
                        pause 0.03
                        "39a25_nvidia.webp"
                        pause 0.03
                        "39a26_nvidia.webp"
                        pause 0.03
                        "39a27_nvidia.webp"
                        pause 0.03
                        "39a28_nvidia.webp"
                        pause 0.03
                        "39a29_nvidia.webp"
                        pause 0.03
                        "39a30_nvidia.webp"
                        pause 0.04
                        "39a31_nvidia.webp"
                        pause 0.04
                        "39a32_nvidia.webp"
                        pause 0.04
                        "39a33_nvidia.webp"
                        pause 0.04
                        "39a34_nvidia.webp"
                        pause 0.04
                        "39a35_nvidia.webp"
                        pause 0.04
                        "39a36_nvidia.webp"
                        pause 0.04
                        "39a37_nvidia.webp"
                        pause 0.04
                        "39a38_nvidia.webp"
                        pause 0.04
                        "39a39_nvidia.webp"
                        pause 0.04
                        repeat
                    i "\" Ahhh...\""
                    " She opens up gently under your assault."
                    i "\" Yes...\""
                    " Pushing you deeper with every thrust."
                    p "\" Izzy...\""
                    $ renpy.pause ()
                    scene 24newalex99
                    with dissolve
                    i "\" Ahh...\""
                    i "\" More...\""
                    scene izzysex animated with fade:
                        "39a00_nvidia.webp"
                        pause 0.04
                        "39a01_nvidia.webp"
                        pause 0.04
                        "39a02_nvidia.webp"
                        pause 0.04
                        "39a03_nvidia.webp"
                        pause 0.04
                        "39a04_nvidia.webp"
                        pause 0.04
                        "39a05_nvidia.webp"
                        pause 0.04
                        "39a06_nvidia.webp"
                        pause 0.04
                        "39a07_nvidia.webp"
                        pause 0.04
                        "39a08_nvidia.webp"
                        pause 0.04
                        "39a09_nvidia.webp"
                        pause 0.04
                        "39a10_nvidia.webp"
                        pause 0.04
                        "39a11_nvidia.webp"
                        pause 0.05
                        "39a12_nvidia.webp"
                        pause 0.05
                        "39a13_nvidia.webp"
                        pause 0.05
                        "39a14_nvidia.webp"
                        pause 0.05
                        "39a15_nvidia.webp"
                        pause 0.05
                        "39a16_nvidia.webp"
                        pause 0.05
                        "39a17_nvidia.webp"
                        pause 0.05
                        "39a18_nvidia.webp"
                        pause 0.05
                        "39a19_nvidia.webp"
                        pause 0.05
                        "39a20_nvidia.webp"
                        pause 0.03
                        "39a21_nvidia.webp"
                        pause 0.03
                        "39a22_nvidia.webp"
                        pause 0.03
                        "39a23_nvidia.webp"
                        pause 0.03
                        "39a24_nvidia.webp"
                        pause 0.03
                        "39a25_nvidia.webp"
                        pause 0.03
                        "39a26_nvidia.webp"
                        pause 0.03
                        "39a27_nvidia.webp"
                        pause 0.03
                        "39a28_nvidia.webp"
                        pause 0.03
                        "39a29_nvidia.webp"
                        pause 0.03
                        "39a30_nvidia.webp"
                        pause 0.04
                        "39a31_nvidia.webp"
                        pause 0.04
                        "39a32_nvidia.webp"
                        pause 0.04
                        "39a33_nvidia.webp"
                        pause 0.04
                        "39a34_nvidia.webp"
                        pause 0.04
                        "39a35_nvidia.webp"
                        pause 0.04
                        "39a36_nvidia.webp"
                        pause 0.04
                        "39a37_nvidia.webp"
                        pause 0.04
                        "39a38_nvidia.webp"
                        pause 0.04
                        "39a39_nvidia.webp"
                        pause 0.04
                        repeat
                    i "\" Ahhh...\""
                    i "\" Yes...\""
                    i "\" I want it...\""
                    $ renpy.pause ()
                    scene 24newalex100
                    with dissolve
                    i "\" Ai...\""
                    " She closes her eyes and gives a sharp squeak as she cums."
                    p "\" I...\""
                    p "\" I'm cumming too.\""
                    show 24newalex101
                    with dissolve
                    " She grabs your ass and holds you close as you let loose."
                    p "\"Agh...\""
                    hide 24newalex101
                    show 24newalex98
                    with dissolve
                    p "\" Pant...pant...pant...\""
                    p "\" God, girl.\""
                    i "\" Mmm...\""
                    i "\" Glad to see Pyle living up to his potential.\""
                    p "\" Keep it up, Rambo might just decide on a rear attack.\""
                    hide 24newalex98
                    show 24newalex102
                    with dissolve
                    " You get off her. Not wanting to keep your weight on her small frame."
                    i "\" Is that a promise or a threat?\""
                    p "\" Both.\""
                    hide 24newalex102
                    show 24newalex104
                    with dissolve
                    i "\" Love you.\""
                    hide 24newalex104
                    show 24newalex103
                    with dissolve
                    " You give her a kiss."
                    hide 24newalex103
                    show 24newalex104
                    with dissolve
                    i "\" I gotta call Alex.\""
                    p "\" What? Why?\""
                    i "\" I have to tell her.\""
                    p "\" What? That we just...\""
                    i "\" Of course.\""
                    p "\" Why?\""
                    hide 24newalex104
                    show 24newalex105
                    with dissolve
                    " She quickly pulls out her phone and calls Alex."
                    i "\" Hey.\""
                    i "\" No, not sleeping yet.\""
                    i "\" Yeah, he's right here.\""
                    i "\" Actually, we just had a bit of fun.\""
                    hide 24newalex105
                    show 24newalex106
                    with dissolve
                    i "\" No.\""
                    i "\" No, I'm not bragging.\""
                    i "\" I'd want to know.\""
                    i "\" What do you mean?\""
                    i "\" Sigh...\""
                    i "\" Ok. Good night, then.\""
                    i "\" Love you too.\""
                    hide 24newalex106
                    show 24newalex107
                    with dissolve
                    " She closes the phone."
                    i "\" Wouldn't you want to know?\""
                    p "\" What?\""
                    i "\" If me and Alex have sex without you, wouldn't you want to know?\""
                    p "\" Ahh...\""
                    p "\" I wouldn't care.\""
                    hide 24newalex107
                    show 24newalex108
                    with dissolve
                    i "\" That's what she said.\""
                    i "\" Why wouldn't you want to know?\""
                    i "\" If your loved one had sex with someone else...\""
                    p "\" First of all, if it's you and Alex, it's not someone else.\""
                    p "\" Second, it's loved ones. Plural.\""
                    hide 24newalex108
                    show 24newalex110
                    with dissolve
                    i "\" Mwuuuuaaaa!\""
                    hide 24newalex110
                    show 24newalex109
                    with dissolve
                    i "\" Love you.\""
                    p "\" You said that.\""
                    i "\" You didn't say I love you back.\""
                    p "\" Love you too.\""
                    hide 24newalex109
                    show 24newalex111
                    with dissolve
                    " She climbs on top of you, and quickly falls asleep in your arms."
                    " With you following shortly after."
                    hide 24newalex111
                    show blackscreen
                    with dissolve
                    $renpy.end_replay()
                    "..."
                    "....."
                    "......."
                    hide blackscreen
                    show 24newalex112
                    with dissolve
                    " The next morning, you're awakened by the sunlight falling on your face."
                    p "\" Groan...\""
                    hide 24newalex112
                    show 24newalex113
                    with dissolve
                    " Izzy is still sleeping restfully, and you don't want to wake her."
                    hide 24newalex113
                    show 24newalex114
                    with dissolve
                    " So, you quietly get dressed and head out to find some water."
                    hide 24newalex114
                    show 24newalex115
                    with dissolve
                    " As you enter the living room you run straight into Agatha."
                    hide 24newalex115
                    show 24newalex116
                    with dissolve
                    ag "\" Oh!\""
                    ag "\" Oh, you startled me.\""
                    p "\" My apologies.\""
                    p "\" I didn't mean to.\""
                    hide 24newalex116
                    show 24newalex117
                    with dissolve
                    ag "\" [player_name], right?\""
                    p "\" Yes, ma'am.\""
                    ag "\" Where did you come from?\""
                    p "\" I...\""
                    ag "\" Was that Isabella's room.\""
                    p "\" Ahhmmm...yes.\""
                    i "\" Momma!\""
                    hide 24newalex117
                    show 24newalex118
                    with dissolve
                    " Izzy seems to have woken up, and has followed you."
                    hide 24newalex118
                    show 24newalex119
                    with dissolve
                    i "\" Dear?\""
                    hide 24newalex119
                    show 24newalex118
                    with dissolve
                    i "\" Stop interrogating [player_name].\""
                    hide 24newalex118
                    show 24newalex120
                    with dissolve
                    i "\" Sorry.\""
                    p "\" It's ok.\""
                    hide 24newalex120
                    show 24newalex119
                    with dissolve
                    ag "\" What interrogation?\""
                    ag "\" We were just talking.\""
                    hide 24newalex119
                    show 24newalex121
                    with dissolve
                    ag "\" A young man coming out of a young girl's room...\""
                    ag "\" Things have changed.\""
                    i "\" Have they?\""
                    i "\" Were you married when I was born?\""
                    ag "\" Isabella!\""
                    p "\" I...I'd better go.\""
                    hide 24newalex121
                    show 24newalex122
                    with dissolve
                    i "\" Going to Alex's?\""
                    p "\" Yeah.\""
                    p "\" You want me to come pick you up later?\""
                    i "\" Ahh...sure.\""
                    p "\" When?\""
                    i "\" I'll call and let you know.\""
                    p "\" Alright.\""
                    jump ep24cont2

                else:
                    p "\" Ok.\""
                    p "\" I'll crash on your couch then.\""
                    i "\" I can do that.\""
                    p "\" Don't be silly.\""
                    p "\" Goodnight, now.\""
                    hide 24newalex76
                    show 24newalex77
                    with dissolve
                    " You go to the living room."
                    hide 24newalex77
                    show 24newalex79
                    with dissolve
                    " You make the bed and quickly go to sleep."
                    hide 24newalex79
                    show blackscreen
                    with dissolve
                    "..."
                    "....."
                    "......."
                    " You're woken by the sound of footsteps."
                    hide blackscreen
                    show 24newalex80
                    with dissolve
                    " You open your eyes to see Agatha."
                    p "\" Mmm...\""
                    hide 24newalex80
                    show 24newalex81
                    with dissolve
                    ag "\" Oh, sorry.\""
                    ag "\" I didn't mean to wake you, dear.\""
                    p "\" It's ok, ma'am.\""
                    p "\" What...what's the time.\""
                    ag "\" About nineish.\""
                    p "\" Oh. I have to get up anyway.\""
                    hide 24newalex81
                    show 24newalex82
                    with dissolve
                    i "\" Momma?\""
                    ag "\" Dear?\""
                    i "\" What are you doing up?\""
                    i "\" You should've called me if you needed anything.\""
                    hide 24newalex82
                    show 24newalex83
                    with dissolve
                    ag "\" Are you trying to hide me or something?\""
                    i "\" No.\""
                    ag "\" You're acting like I don't know how to behave.\""
                    ag "\" I know how to behave.\""
                    i "\" I didn't...\""
                    p "\" I have to get going anyway.\""
                    hide 24newalex83
                    show 24newalex122
                    with dissolve
                    " You quickly put on some clothes and head out."
                    i "\" Going to Alex's?\""
                    p "\" Yeah.\""
                    p "\" You want me to come pick you up later?\""
                    i "\" Ahh...sure.\""
                    p "\" When?\""
                    i "\" I'll call and let you know.\""
                    p "\" Alright.\""
                    jump ep24cont2

label ep24cont2:
                scene 24newalex155
                with dissolve
                " When you walk out of Izzy's appartment building, you see James parked across the street."
                show back
                with dissolve
                show 24newalex134
                with dissolve
                " You get in his van."
                p "\" Hey.\""
                ja "\" Boss?\""
                p "\" Did you see anything?\""
                hide 24newalex134
                show 24newalex135
                with dissolve
                ja "\" During the night?\""
                p "\" Yes.\""
                ja "\" No.\""
                ja "\" I saw you come last night.\""
                ja "\" And now I'm seeing you leave.\""
                hide 24newalex135
                show 24newalex136
                with dissolve
                ja "\" Are you sure you're not just having me watch your girlfriend?\""
                ja "\" See if she steps wrong.\""
                p "\" That's not even funny.\""
                hide 24newalex136
                show 24newalex137
                with dissolve
                ja "\" I didn't see anything boss.\""
                p "\" Well, if you do.\""
                ja "\" Call you.\""
                ja "\" To be sure.\""
                hide 24newalex137
                show 24newalex215
                with dissolve
                " You go to the villa."
                hide 24newalex215
                show 24newalex124
                with dissolve
                " And find Alex in her bedroom."
                p "\" Alex.\""
                hide 24newalex124
                show 24newalex123
                with dissolve
                a "\" Hey!\""
                a "\" Back from your little vacation?\""
                p "\" I was just at Izzy's.\""
                a "\" She still with her mom?\""
                p "\" Yeah.\""
                p "\" I'll go get her later, though.\""
                a "\" Yeah. She and I need to have a talk about this.\""
                p "\" What kind of talk.\""
                hide 24newalex123
                show 24newalex125
                with dissolve
                a "\" She needs to take a little better care of you.\""
                p "\" She took care of me just fine.\""
                if izzyin == True:
                    a "\" I heard.\""
                    a "\" But that's not what I mean.\""
                a "\" Same old clothes.\""
                a "\" I ordered you something.\""
                p "\" You're not trying to dress me up, are you?\""
                hide 24newalex125
                show 24newalex126
                with dissolve
                " She rubs her nose against your."
                a "\" Please!\""
                a "\" Have a little faith.\""
                a "\" I'm just tired of seeing you in that shirt.\""
                p "\" Sigh...\""
                hide 24newalex126
                show 24newalex127
                with dissolve
                a "\" He he...\""
                a "\" I always win in the end.\""
                a "\" I got it right here.\""
                hide 24newalex127
                show 24newalex124
                with dissolve
                " She rummages through her drawers."
                hide 24newalex124
                show 24newalex128
                with dissolve
                " And comes up with a new pair of jeans and a t-shirt, that you put on."
                p "\" It's...red.\""
                hide 24newalex128
                show 24newalex129
                with dissolve
                a "\" Don't question my fashion sense, he he...\""
                a "\" I like it.\""
                a "\" You don't?\""
                p "\" I have no idea.\""
                hide 24newalex129
                show 24newalex130
                with dissolve
                a "\" Have a little faith, boyo.\""
                a "\" You're looking good.\""
                p "\" If you say so.\""
                p "\" I'm gonna go take a walk around the grounds.\""
                hide 24newalex130
                show 24newalex131
                with dissolve
                " You check to see if everything is ok around the villa."
                hide 24newalex131
                show 24newalex133
                with dissolve
                " When you're stopped by Dima."
                di "\" He he...\""
                di "\" Where did you get that t-shirt from?\""
                p "\" Why?\""
                hide 24newalex133
                show 24newalex139
                with dissolve
                di "\" You chose it?\""
                p "\" Again. Why?\""
                di "\" Alex got it for you, didn't she.\""
                di "\" He he...\""
                di "\" She's dressing you now, is she?\""
                p "\" Watch it.\""
                hide 24newalex139
                show 24newalex138
                with dissolve
                a "\" Does the doorman have fashion tips.\""
                di "\" Doorman?\""
                a "\" I wouldn't listen to him.\""
                a "\" I'm cooking something.\""
                a "\" Come with me?\""
                hide 24newalex138
                show 24newalex139
                with dissolve
                p "\" Later, doorman.\""
                di "\" Ouch.\""
                hide 24newalex139
                show 24newalex140
                with dissolve
                " You go with Alex to the kitchen."
                p "\" What's up?\""
                hide 24newalex140
                show 24newalex141
                with dissolve
                a "\" Nothing.\""
                a "\" Just cooking dad some breakfast.\""
                p "\" Is he on a speacial diet or something?\""
                a "\" No.\""
                a "\" I just want to do it.\""
                hide 24newalex141
                show 24newalex142
                with dissolve
                a "\" Looks good, right.\""
                p "\" It looks good. I'll grant you that.\""
                p "\" On the taste issue, though.\""
                hide 24newalex142
                show 24newalex143
                with dissolve
                a "\" You're gonna complain about my cooking now?\""
                p "\" I don't feel the need to.\""
                p "\" I think it's established that it's execrable.\""
                hide 24newalex143
                show 24newalex142
                with dissolve
                a "\" You only say that because you have no taste.\""
                p "\" Aha.\""
                hide 24newalex142
                show 24newalex143
                with dissolve
                a "\" Help me carry it?\""
                hide 24newalex143
                show 24newalex144
                with dissolve
                " You grab the tray and head to Boris's room."
                a "\" You'll see.\""
                a "\" Dad will like my breakfast.\""
                p "\" He was fed intrevenously, wasn't he.\""
                p "\" In the hospital, I mean.\""
                p "\" Yeah.\""
                p "\" I'm sure he'll love your breakfast.\""
                a "\" When did you get so nasty?\""
                p "\" What do you mean?\""
                p "\" I was always honest.\""
                hide 24newalex144
                show 24newalex145
                with dissolve
                " You find Boris pacing around his room."
                p "\" Boss?\""
                hide 24newalex145
                show 24newalex146
                with dissolve
                " He smiles at you."
                p "\" Doing some exercise?\""
                " He nods."
                p "\" Good.\""
                hide 24newalex146
                show 24newalex147
                with dissolve
                a "\" I made you breakfast, daddy.\""
                hide 24newalex147
                show 24newalex148
                with dissolve
                b "\" Groannnnn!!!\""
                p "\" He he he...\""
                p "\" Not even hospital food compares to this, eh.\""
                hide 24newalex148
                show 24newalex149
                with dissolve
                a "\" A pox on both your houses!\""
                hide 24newalex149
                show 24newalex150
                with dissolve
                a "\" Now, you're gonna eat it.\""
                a "\" AND!!!\""
                a "\" And you're gonna like it.\""
                hide 24newalex150
                show 24newalex151
                with dissolve
                b "\" Sigh...\""
                p "\" Alex. Ease up.\""
                p "\" The poor man has been through enough.\""
                p "\" No need to waffleboard him.\""
                hide 24newalex151
                show 24newalex152
                with dissolve
                a "\" Pay no mind to the meany, dad.\""
                a "\" You'll like it.\""
                a "\" Trust me.\""
                " Ring...ring...ring..."
                " Your phone rings."
                p "\" I'll be right back.\""
                hide 24newalex152
                show 24newalex132
                with dissolve
                " You step outside to take it."
                p "\" Yes?\""
                ja "\" Boss!!\""
                ja "\" Boss, I got him!\""
                p "\" Got who?\""
                ja "\" The guy! The guy that got Hugo!\""
                p "\" What?\""
                p "\" You killed him?\""
                ja "\" He he...not yet.\""
                p "\" Where are you?\""
                ja "\" At the girls appartment.\""
                p "\" Don't do anything.\""
                p "\" I'm on my way.\""
                " You hang up."
                hide 24newalex132
                show 24newalex152
                with dissolve
                " You rush back in."
                p "\" Alex!\""
                hide 24newalex152
                show 24newalex153
                with dissolve
                a "\" What?\""
                p "\" I need to go.\""
                p "\' Be...be careful.\""
                a "\" Careful? With what?\""
                p "\" Nothing. Just...be careful.\""
                hide 24newalex153
                scene back1
                with dissolve
                show 24newalex154
                with dissolve
                " You jump in the car and rush over to Izzy's."
                hide 24newalex154
                show 24newalex155
                with dissolve
                " When you get there, you run to James's van."
                hide 24newalex155
                show 24newalex156
                with dissolve
                " But looking through the window you see the van is empty."
                p "\" Fuck!\""
                hide 24newalex156
                show 24newalex157
                with dissolve
                " You call James."
                ja "\" Boss?\""
                p "\" Where the hell are you?\""
                ja "\" Where are you?\""
                p "\" I'm by your damned van.\""
                p "\" Now, where are you?\""
                ja "\" I'm upstairs. In the girl's appartment.\""
                ja "\" Isabella, I think?\""
                hide 24newalex157
                show 24newalex158
                with dissolve
                p "\" You're in Izzy's appartment?\""
                p "\" What the fuck?!\""
                ja "\" I couldn't stay with this dude in the street.\""
                ja "\" The girl let me in.\""
                p "\" Fuck!\""
                hide 24newalex158
                show 24newalex159
                with dissolve
                " You hang up and rush up the stairs."
                " Knock...knock...knock..."
                i "\" Who is it?\""
                p "\" Me. Open up.\""
                hide 24newalex159
                show 24newalex160
                with dissolve
                " She opens the door."
                p "\" Wha the...\""
                p "\" Your face...\""
                i "\" It's not mine.\""
                if izzyin == True:
                    hide 24newalex160
                    show 24newalex161
                    with dissolve
                    " You cup her face."
                    p "\" Izzy...\""
                    i "\" It's not mine.\""
                    i "\" I'm ok.\""
                    i "\" It's not mine.\""
                    hide 24newalex161
                show 24newalex162
                with dissolve
                i "\" It's from the boy that guy brought in.\""
                i "\" James?\""
                p "\" He's here.\""
                i "\" Yes. I recognised him from when he was at our school.\""
                i "\" He's one of your guys, right.\""
                p "\" I'm sorry.\""
                hide 24newalex162
                show 24newalex163
                with dissolve
                ag "\" Sob...sob...sob...\""
                " You can see Agatha was very distraught."
                p "\" Is she ok?\""
                hide 24newalex163
                show 24newalex164
                with dissolve
                i "\" No.\""
                i "\" What's happening?\""
                p "\" Where is he?\""
                i "\" James? I told them to go to the bedroom.\""
                i "\" I didn't want them here with momma.\""
                p "\" Alright.\""
                p "\" Close the door, and keep it closed.\""
                hide 24newalex164
                show 24newalex165
                with dissolve
                " You go to the bedroom."
                ja "\" You're fucked now, my boy.\""
                m18 "\" Sob...sob...sob...\""
                ja "\" Proper fucked.\""
                m18 "\" I don't know you, man.\""
                hide 24newalex165
                show 24newalex166
                with dissolve
                ja "\" Shut up!\""
                ja "\" I know you.\""
                ja "\" Did you know Hugo?\""
                hide 24newalex166
                show 24newalex167
                with dissolve
                m18 "\" What?\""
                m18 "\" Who?\""
                hide 24newalex167
                show 24newalex166
                with dissolve
                ja "\" Didn't even know his name, eh.\""
                ja "\" Doesn't matter.\""
                ja "\" I'm gonna carve his name into your chest.\""
                p "\" James!\""
                hide 24newalex166
                show 24newalex168
                with dissolve
                ja "\" Boss.\""
                ja "\" You got here.\""
                ja "\" I got him.\""
                ja "\" Little shit!\""
                hide 24newalex168
                show 24newalex169
                with dissolve
                m18 "\" Sob...sob...sob...\""
                " The man was gasping for air as he cried."
                p "\" Him?\""
                p "\" Doesn't look like much.\""
                " Certainly not the type of man you thought could kill Hugo."
                hide 24newalex169
                show 24newalex170
                with dissolve
                ja "\" I know.\""
                ja "\" Looks can be deceptive, though.\""
                ja "\" He he...\""
                ja "\" We'll see what's under that skin after I cut him open.\""
                hide 24newalex170
                show 24newalex171
                with dissolve
                m18 "\" Sob...sob...sob...\""
                p "\" How do you know?\""
                ja "\" Know what?\""
                p "\" That is was him.\""
                hide 24newalex171
                show 24newalex172
                with dissolve
                ja "\" You told me to look out for the girl.\""
                ja "\" Well, she left to take out the trash.\""
                ja "\" That's when I noticed him.\""
                ja "\" Sneaking around like a little snake.\""
                hide 24newalex172
                show 24newalex171
                with dissolve
                m18 "\" Sob...sob...sob...\""
                p "\" What was he doing?\""
                hide 24newalex171
                show 24newalex173
                with dissolve
                ja "\" Ugh...\""
                ja "\" Taking pictures.\""
                p "\" Of Izzy?\""
                hide 24newalex173
                show 24newalex175
                with dissolve
                ja "\" Yeah.\""
                ja "\" Pictures of the girl.\""
                ja "\" That's when I snatched him.\""
                p "\" And you brought him up here?\""
                hide 24newalex175
                show 24newalex173
                with dissolve
                ja "\" Well, I couldn't fuck him up in the middle of the street.\""
                ja "\" I thought I'd give it a shot.\""
                hide 24newalex173
                show 24newalex176
                with dissolve
                m18 "\" Sob...sob...sob...\""
                m18 "\" I didn't mean...\""
                p "\" Shut up!\""
                p "\" Alright, take him with us\""
                hide 24newalex176
                show 24newalex174
                with dissolve
                ja "\" With us?\""
                ja "\" Where?\""
                p "\" Listen. Whatever we're gonna do, we're not going to do it here.\""
                p "\" Now, take him.\""
                hide 24newalex174
                show 24newalex175
                with dissolve
                ja "\" Some place private to fuck him up.\""
                ja "\" I like that.\""
                hide 24newalex175
                show 24newalex177
                with dissolve
                " When you walk back outside, you see Izzy cleaned herself up."
                i "\" What's going on?\""
                i "\" Who is that guy?\""
                p "\" I'm not sure.\""
                p "\" He might be involved with what happened when we went on vacation.\""
                hide 24newalex177
                show 24newalex178
                with dissolve
                i "\" He tried to hurt Alex?\""
                i "\" Like I said. I'm not sure.\""
                hide 24newalex178
                show 24newalex179
                with dissolve
                ja "\" He's a dead man, is what he is.\""
                ja "\" isn't that right, boy?\""
                m18 "\" Sniff...sniff...sniff...\""
                m18 "\" Please...\""
                hide 24newalex179
                show 24newalex180
                with dissolve
                i "\" You tried to hurt Alex?\" Izzy asks in iron tones."
                m18 "\" I don't know any Alex, lady.\""
                m18 "\" Please...\""
                p "\" Izzy!\""
                hide 24newalex180
                show 24newalex181
                with dissolve
                p "\" We don't know anything yet.\""
                p "\" We'll find out, though.\""
                p "\" Trust me.\""
                p "\" In the mean time...\""
                i "\" Say nothing?\""
                p "\" Not a word.\""
                i "\" Don't worry.\""
                hide 24newalex181
                show 24newalex182
                with dissolve
                " You go on ahead from James to see if the coast is clear."
                hide 24newalex182
                show 24newalex183
                with dissolve
                " Then you bundle him in the back of the van."
                ja "\" Yes, boy.\""
                ja "\" I'm gonna cut off a pound of flesh for every tear I saw come from Mrs. Teresa.\""
                ja "\" One for every tear.\""
                hide 24newalex183
                scene back1
                with dissolve
                show 24newalex184
                with dissolve
                p "\" Where to take him?\""
                p "\" Where to take him?\""
                hide 24newalex184
                show 24newalex185
                with dissolve
                ja "\" How about straight to the cemetary?\""
                ja "\" That's where he's ending up, anyway.\""
                hide 24newalex185
                show 24newalex186
                with dissolve
                p "\" Fuck it!\""
                p "\" Let's just take him to my place.\""
                hide 24newalex186
                show 24newalex184
                with dissolve
                p "\" I'm fucked if Emma is still watching.\""
                ja "\" Emma?\""
                p "\" Quiet, back there!\""
                hide 24newalex184
                show 24newalex187
                with dissolve
                " You drive to your old apartment."
                hide 24newalex187
                show 24newalex188
                with dissolve
                d "\" Ok.\""
                d "\" There you go.\""
                d "\" That should fix it.\""
                p "\" Dan?\""
                hide 24newalex188
                show 24newalex189
                with dissolve
                d "\" Oh!\""
                d "\" Hey there, bud.\""
                d "\" I haven't seen you around in a while.\""
                p "\" What are you doing here?\""
                d "\" Yeah.\""
                d "\" Sorry about that. But your sink has been leaking.\""
                d "\" It's messing up the paint in the apartment downstairs.\""
                p "\" Oh.\""
                d "\" Just came to fix it for a minute.\""
                d "\" Didn't mean to intrude.\""
                p "\" You need to leave, ok.\""
                d "\" Come on, bud.\""
                d "\" I wasn't doing...\""
                hide 24newalex189
                show 24newalex190
                with dissolve
                " That's when James comes in with the boy."
                ja "\" This is where you die, kid.\""
                m18 "\" Agghhh...\""
                hide 24newalex190
                show 24newalex191
                with dissolve
                d "\" Aaaaaa...\""
                d "\" I need to get out of here.\""
                hide 24newalex191
                show 24newalex192
                with dissolve
                d "\" Where's my tools.\""
                d "\" Never mind.\""
                d "\" I didn't need them anyway.\""
                d "\" I'll just be going.\""
                p "\" You do that.\""
                hide 24newalex192
                show 24newalex193
                with dissolve
                " James throws the boy to the ground."
                hide 24newalex193
                show 24newalex194
                with dissolve
                ja "\" You're just gonna let him go?\""
                ja "\" The fat guy?\""
                p "\" Yeah.\""
                ja "\" What if he doesn't keep his mouth shut.\""
                p "\" He's my friend. He will.\""
                ja "\" But...\""
                p "\" He goes!\""
                hide 24newalex194
                show 24newalex195
                with dissolve
                m18 "\" Sob...sob...sob...\""
                p "\" I have enough blood on my hands of late.\""
                hide 24newalex195
                show 24newalex196
                with dissolve
                ja "\" That's not a problem.\""
                ja "\" This little shit's blood will be on mine.\""
                hide 24newalex196
                show 24newalex195
                with dissolve
                p "\" Do you really see him killing Hugo?\""
                hide 24newalex195
                show 24newalex197
                with dissolve
                " You take a seat."
                p "\" Boy!\""
                p "\" Look at me, boy!\""
                hide 24newalex197
                show 24newalex198
                with dissolve
                m18 "\" I...\""
                p "\" Look at me!!\""
                hide 24newalex198
                show 24newalex200
                with dissolve
                p "\" What's your name?\""
                m18 "\" Dddd...David.\""
                p "\" What were you doing there David?\""
                p "\" Why were you taking pictures of the girl.\""
                dav "\" The one with the dark hair?\""
                p "\" How many girls have you been taking pictures of?\""
                hide 24newalex200
                show 24newalex198
                with dissolve
                dav "\" There was supposed to be a blonde too.\""
                dav "\" I don't know.\""
                p "\" You don't know?\""
                hide 24newalex198
                show 24newalex199
                with dissolve
                ja "\" Lying little SHIT!!!\""
                hide 24newalex199
                show 24newalex200
                with dissolve
                dav "\" I don't know, man!\""
                dav "\" I was hired to do it.\""
                dav "\" Figured it was an old guy with some weird kinks.\""
                p "\" Old guy?\""
                p "\" What old guy?\""
                hide 24newalex200
                show 24newalex201
                with dissolve
                dav "\" He hired men over the internet.\""
                p "\" How do you know he's an old guy, then.\""
                dav "\" I don't.\""
                dav "\" I just...\""
                dav "\" I was just thinking...\""
                hide 24newalex201
                show 24newalex202
                with dissolve
                ja "\" TALK!!!!\""
                hide 24newalex202
                show 24newalex203
                with dissolve
                dav "\" I don't know, man.\""
                dav "\" Some guy hired me to take pictures of these girls.\""
                dav "\" Follow them around.\""
                dav "\" Told me where to find them.\""
                p "\" How did he get in touch with you?\""
                hide 24newalex203
                show 24newalex204
                with dissolve
                dav "\" On a message board.\""
                p "\" How did he pay you?\""
                p "\" Credit card?\""
                dav "\" Cash app.\""
                p "\" So, you know his name!\""
                hide 24newalex204
                show 24newalex203
                with dissolve
                dav "\" No, man.\""
                dav "\" There are no names.\""
                hide 24newalex203
                show 24newalex205
                with dissolve
                p "\" Fuck!\""
                p "\" I don't know this internet shit.\""
                hide 24newalex205
                show 24newalex206
                with dissolve
                ja "\" You believe him?\""
                p "\" I don't know.\""
                p "\" But I'll believe that before I believe this dude took out Hugo.\""
                p "\" Maybe someone else did it.\""
                p "\" Maybe they got scared after that.\""
                p "\" Hired this little shit to put some distance between them.\""
                p "\" I've been rushing blindly into shit my whole life.\""
                p "\" Trying to do better with that.\""
                hide 24newalex206
                show 24newalex196
                with dissolve
                ja "\" So what?\""
                ja "\" We're not letting him go.\""
                p "\" No.\""
                p "\" I need to go talk to Alex.\""
                p "\" Tie him up.\""
                hide 24newalex196
                show 24newalex207
                with dissolve
                " James gets some rope and ties him up."
                hide 24newalex207
                show 24newalex208
                with dissolve
                ja "\" The boss is leaving.\""
                ja "\" It's just you and me now, boy.\""
                " Do you leave James alone with David?"
                call screen screen74

label ep24leaveJames:
                scene 24newalex209
                with dissolve
                $ boyspts = boyspts + 1
                p "\" Watch him till I get back.\""
                ja "\" Oh, I'll be watching.\""
                show back1
                with dissolve
                show 24newalex210
                with dissolve
                " You get in James's van and head to the villa."
                jump ep24end

label ep24dontleaveJames:
                scene 24newalex208
                with dissolve
                p "\" You're coming with me.\""
                show 24newalex206
                with dissolve
                ja "\" We're leaving him alone?\""
                p "\" He's tied up.\""
                p "\" He won't be going anywhere.\""
                p "\" Come.\""
                hide 24newalex206
                show back1
                with dissolve
                show 24newalex210
                with dissolve
                " You get in James's van and head to the villa."
                hide 24newalex210
                show 24newalex211
                with dissolve
                ja "\" I'd best find that little shit right where I left him.\""
                jump ep24end

label ep24end:

                scene end
                with dissolve
                $ renpy.pause ()
                $ MainMenu(confirm=False)()




