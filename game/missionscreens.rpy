screen screen2mmsshoot1:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/shoot.png"
                hover_background "gui/button/shoota.png"

                action Call("mms2shoot1")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/dontshoota.png"
                hover_background im.MatrixColor("gui/button/dontshoota.png", im.matrix.brightness(0.2))

                action Jump("mms2gundown1")


screen screen2mmsshoot2:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/shoot.png"
                hover_background "gui/button/shoota.png"

                action Call("mms2shoot2")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/dontshoota.png"
                hover_background im.MatrixColor("gui/button/dontshoota.png", im.matrix.brightness(0.2))

                action Jump("mms2gundown2")


screen alicescreen1:
            textbutton(""):
                area(550, 200, 200, 50)
                background "gui/button/helpalice1a.png"
                hover_background im.MatrixColor("gui/button/helpalice1a.png", im.matrix.brightness(0.2))

                action Call("alicem1help")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/dontheplalice1.png"
                hover_background "gui/button/dontheplalice1a.png"

                action Jump("alicem1nohelp")


screen alicescreen2:
            textbutton(""):
                    area(800, 200, 200, 50)
                    background "gui/button/alicekill1.png"
                    hover_background "gui/button/alicekill1a.png"

                    action Call("alicem1kill")



            textbutton(""):
                area(900, 900, 200, 50)
                background "gui/button/alicenokill1a.png"
                hover_background im.MatrixColor("gui/button/alicenokill1a.png", im.matrix.brightness(0.2))

                action Jump("alicem1nokilll")


screen dannyscreen1:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/goovertherea.png"
                hover_background im.MatrixColor("gui/button/goovertherea.png", im.matrix.brightness(0.2))

                action Call("danny1goover")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/dontgo.png"
                hover_background "gui/button/dontgoa.png"

                action Jump("danny1nogoover")


screen dannyscreen2:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/controla.png"
                hover_background im.MatrixColor("gui/button/controla.png", im.matrix.brightness(0.2))

                action Call("danny1control")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/letlose.png"
                hover_background "gui/button/letlosea.png"

                action Jump("danny1nocontrol")


screen mission3screen1:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/killher.png"
                hover_background "gui/button/killhera.png"

                action Call("m3killizzy")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/putdowna.png"
                hover_background im.MatrixColor("gui/button/putdowna.png", im.matrix.brightness(0.2))

                action Jump("m3nokill")


screen mission3screen2:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/accepta.png"
                hover_background im.MatrixColor("gui/button/accepta.png", im.matrix.brightness(0.2))

                action Call("izzylove")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/refuse.png"
                hover_background "gui/button/refusea.png"

                action Jump("izzynolove")


screen Jasminescreen1:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yes.png"
                hover_background "gui/button/yesa.png"

                action Call("jasminestrike")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/noa.png"
                hover_background im.MatrixColor("gui/button/noa.png", im.matrix.brightness(0.2))

                action Jump("jasminenostrike")

 #


screen screen1:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("tellalexdreamtruth")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("notellalexdreamtruth")

screen screen2:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/iguess.png"
                hover_background "gui/button/iguessa.png"

                action Call("jamienoride")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/offerridea.png"
                hover_background im.MatrixColor("gui/button/offerridea.png", im.matrix.brightness(0.2))

                action Jump("jamieride")

screen screen3:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/itdoesnta.png"
                hover_background im.MatrixColor("gui/button/itdoesnta.png", im.matrix.brightness(0.2))

                action Call("notbothered")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/alittle.png"
                hover_background "gui/button/alittlea.png"

                action Jump("bothered")

screen screen4:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yes.png"
                hover_background "gui/button/yesa.png"

                action Call("izzycheekkissyes")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/alittelmorea.png"
                hover_background im.MatrixColor("gui/button/alittelmorea.png", im.matrix.brightness(0.2))

                action Jump("izzyalittlemorekiss")

screen screen5:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("alicehugback")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("alicenohugback")

screen screen6:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("aliceday2stay")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("aliceday2nostay")

screen screen7:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/justafriend.png"
                hover_background "gui/button/justafrienda.png"

                action Call("aliceday2friend")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/friendfornowa.png"
                hover_background im.MatrixColor("gui/button/friendfornowa.png", im.matrix.brightness(0.2))

                action Jump("aliceday2friendfornow")

screen screen8:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/goodnight.png"
                hover_background "gui/button/goodnighta.png"

                action Call("izzygoodnight")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/gnkissa.png"
                hover_background im.MatrixColor("gui/button/gnkissa.png", im.matrix.brightness(0.2))

                action Jump("izzygoodnightkiss")

screen screen9:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/justworkhard.png"
                hover_background "gui/button/justworkharda.png"

                action Call("dannyworkhardgym")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/sexualfrusta.png"
                hover_background im.MatrixColor("gui/button/sexualfrusta.png", im.matrix.brightness(0.2))

                action Jump("dannysexfrustr")

screen screen10:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("dannyhandjob")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("dannynohandjob")

screen screen11:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("dannydateask")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("dannydatenoask")

screen screen12:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yes.png"
                hover_background "gui/button/yesa.png"

                action Call("alexnothanks")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/thanksa.png"
                hover_background im.MatrixColor("gui/button/thanksa.png", im.matrix.brightness(0.2))

                action Jump("alexthanks")

screen screen13:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/ignorejab.png"
                hover_background "gui/button/ignorejaba.png"

                action Call("claraignorejab")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/grabhera.png"
                hover_background im.MatrixColor("gui/button/grabhera.png", im.matrix.brightness(0.2))

                action Jump("claragrabher")

screen screen14:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/forheada.png"
                hover_background im.MatrixColor("gui/button/forheada.png", im.matrix.brightness(0.2))

                action Call("izzyforhead")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/mouth.png"
                hover_background "gui/button/moutha.png"

                action Jump("izzymouth")

screen screen15:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/lethergo.png"
                hover_background "gui/button/lethergoa.png"

                action Call("adiletgo")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/stophera.png"
                hover_background im.MatrixColor("gui/button/stophera.png", im.matrix.brightness(0.2))

                action Jump("adistop")

screen screen16:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yes.png"
                hover_background "gui/button/yesa.png"

                action Call("adiletgo1")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/noa.png"
                hover_background im.MatrixColor("gui/button/noa.png", im.matrix.brightness(0.2))

                action Jump("adiintervene")

screen screen17:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/Revealing.png"
                hover_background "gui/button/Revealinga.png"

                action Call("alexrevealing")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/Conservativea.png"
                hover_background im.MatrixColor("gui/button/Conservativea.png", im.matrix.brightness(0.2))

                action Jump("alexconservative")

screen screen18:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/threeofusa.png"
                hover_background im.MatrixColor("gui/button/threeofusa.png", im.matrix.brightness(0.2))

                action Call("izzythree")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/twoofus.png"
                hover_background "gui/button/twoofus.png"

                action Jump("izzytwo")

screen screen19:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/maybe.png"
                hover_background "gui/button/maybea.png"

                action Call("izzymaybeleave")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/noa.png"
                hover_background im.MatrixColor("gui/button/noa.png", im.matrix.brightness(0.2))

                action Jump("neverleaveizzy")

screen screen20:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("izzylastchanceyes")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("izzylastchanceno")

screen screen21:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/caressa.png"
                hover_background im.MatrixColor("gui/button/caressa.png", im.matrix.brightness(0.2))

                action Call("ep4izzycaress")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/donothing.png"
                hover_background "gui/button/donothinga.png"

                action Jump("ep4izzynothing")

screen screen22:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/oka.png"
                hover_background im.MatrixColor("gui/button/oka.png", im.matrix.brightness(0.2))

                action Call("ep4ok")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/stopher.png"
                hover_background "gui/button/stophera.png"

                action Jump("ep4stopher")

screen screen23:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/getizzya.png"
                hover_background im.MatrixColor("gui/button/getizzya.png", im.matrix.brightness(0.2))

                action Call("ep4getizzy")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/saynothing.png"
                hover_background "gui/button/saynothinga.png"

                action Jump("ep4saynothing")

screen screen24:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yes.png"
                hover_background "gui/button/yesa.png"

                action Call("epj4ennocomp")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/runsfama.png"
                hover_background im.MatrixColor("gui/button/runsfama.png", im.matrix.brightness(0.2))

                action Jump("ep4jencomp")

screen screen25:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/idk.png"
                hover_background "gui/button/idka.png"

                action Call("ep4idk")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/dinnera.png"
                hover_background im.MatrixColor("gui/button/dinnera.png", im.matrix.brightness(0.2))

                action Jump("ep4dinner")

screen screen26:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep4dannyyes")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep4dannyno")

screen screen27:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep5engageboris")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep5noengageboris")

screen screen28:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep5alexpussy")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep5noalexpussy")

screen screen29:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep5izzykiss")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep5noizzykiss")

screen screen30:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep5standuptoboris")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep5nostanduptoboris")

screen screen31:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep5adi1")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep5noadi1")

screen screen32:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep5adi2")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep5noadi2")

screen screen33:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep6georgieyes")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep6georgieno")

screen screen34:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep7claireyes")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep7claireno")

screen screen35:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep7hugalex")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep7nohugalex")

screen screen36:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep7alexpussy")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep7alexpussyno")

screen screen37:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep7izzytry")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep7izzynotry")

screen screen38:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep7narysayes")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep7narysano")

screen screen39:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep7narysahugyes")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep7narysahugno")

screen screen40:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/lethergo.png"
                hover_background "gui/button/lethergoa.png"

                action Call("ep7alexgo")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/holdhera.png"
                hover_background im.MatrixColor("gui/button/holdhera.png", im.matrix.brightness(0.2))

                action Jump("ep7holdher")

screen screen41:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/aplogize.png"
                hover_background "gui/button/aplogize.png"

                action Call("ep7aliceapologize")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/kisshera.png"
                hover_background im.MatrixColor("gui/button/kisshera.png", im.matrix.brightness(0.2))

                action Jump("ep7kissalice")

screen screen42:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep7alex")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep7rob")

screen screen43:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep8yesjamie")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("epnojamie")

screen screen44:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep8yesadi")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep8noadi")

screen screen45:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep8small")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep8split")

screen screen46:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep8yesboris")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep8noboris")

screen screen47:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep9boris")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep9noboris")

screen screen48:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yes.png"
                hover_background "gui/button/yesa.png"

                action Call("ep9false")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/noa.png"
                hover_background im.MatrixColor("gui/button/noa.png", im.matrix.brightness(0.2))

                action Jump("ep9truth")

screen screen49:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep9boristruth")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep9borisfalse")

screen screen50:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep9tanyayes")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep9tanyano")

screen screen51:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep10clarayes")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep10clarano")

screen screen52:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep10jamieyes")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep10jamieno")

screen screen53:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yes.png"
                hover_background "gui/button/yesa.png"

                action Call("ep10nopreg")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep10preg")

screen screen54:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yes.png"
                hover_background "gui/button/yesa.png"

                action Call("ep11narnoass")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/noa.png"
                hover_background im.MatrixColor("gui/button/noa.png", im.matrix.brightness(0.2))

                action Jump("ep11narass")

screen screen55:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep11alice1")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ap11noalice1")

screen screen56:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep11alice2")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ap11noalice2")

screen screen57:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep14loveizzyyes")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep14loveizzyno")

screen screen58:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep14teachlesson")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep14noteachlesson")

screen screen59:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep15phil")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep15nophil")

screen screen60:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep15Jas")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep15noJas")

screen screen61:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep15danny")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep15doc")

screen screen62:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep15jenny")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep15nojenny")

screen screen63:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep14nar1")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep14nonar1")

screen screen64:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep16dreams")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep16nodreams")

screen screen65:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep16yesboss")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep16noboss")

screen screen66:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yes.png"
                hover_background "gui/button/yesa.png"

                action Call("ep16antonsuspicion")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/noa.png"
                hover_background im.MatrixColor("gui/button/noa.png", im.matrix.brightness(0.2))

                action Jump("ep16antonnosuspicion")

screen screen67:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yes.png"
                hover_background "gui/button/yesa.png"

                action Call("ep16dimasetup")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/noa.png"
                hover_background im.MatrixColor("gui/button/noa.png", im.matrix.brightness(0.2))

                action Jump("ep16dimaredempt")

screen screen68:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep18tanyayes")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep18tanyayno")

screen screen69:
            textbutton(""):
                area(1600, 200, 200, 50)
                background "gui/button/yesa.png"
                hover_background im.MatrixColor("gui/button/yesa.png", im.matrix.brightness(0.2))

                action Call("ep18alextruth")



            textbutton(""):
                area(1600, 900, 200, 50)
                background "gui/button/no.png"
                hover_background "gui/button/noa.png"

                action Jump("ep18alexlie")
