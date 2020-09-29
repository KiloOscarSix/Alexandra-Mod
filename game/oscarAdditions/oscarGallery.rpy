init python:
    galleryCharacter = ""
    galleryPageNumber = 1

    def galleryDecreasePageNumber():
        global galleryPageNumber
        galleryPageNumber -= 1
        return

    def galleryIncreasePageNumber():
        global galleryPageNumber
        galleryPageNumber += 1
        return

    sceneGalleryMenuDict = {
    "galleryMenu": [
    ["Alexandra", "/images/1/123.webp"],
    ["Isabella", "/images/1/150.webp"],
    ["Adriana", "/images/1/54.webp"],
    ["Danny", "/images/2/174.webp"],
    ["Jenny", "/images/3/297.webp"],
    ["Alice", "/images/2/74.webp"],
    ["Jamie", "/images/1/75.webp"],
    ["Other", "/images/6/199.webp"],
    ],
    "Alexandra": {
    1: [
    ["ep3bigcont6", {}, "/images/3/244.webp"],
    ["ep4izzyalexblow", {}, "/images/4/118.webp"],
    ["galleryScene2", {}, "/images/5/88.webp"],
    ["ep6cont3", {"izzyin":True}, "/images/6/73.webp"],
    ["galleryScene6", {}, "/images/7/236.webp"],
    ["galleryScene7", {}, "/images/8/213.webp"],
    ["ep9cont11", {}, "/images/9/315.webp"],
    ["ep12cont8", {"izzyin":True}, "/images/12/205.webp"],
    ],
    2: [
    ["galleryScene9", {}, "/images/18/al-20-202-Beauty.webp"]
    ]
    },
    "Isabella": {
    1: [
    ["day5izzyshower", {}, "/images/5/135.webp"],
    ["galleryScene3", {}, "/images/6/17.webp"],
    ["galleryScene4", {}, "/images/7/22.webp"],
    ["galleryScene5", {}, "/images/7/212.webp"],
    ["ep12cont8", {}, "/images/12/223.webp"],
    ["ep14izzy", {}, "/images/14/al-16-9-Beauty.webp"],
    ],
    },
    "Adriana": {
    1: [
    ["ep5adi2", {}, "/images/5/232.webp"],
    ["ep8yesadi", {}, "/images/8/23.webp"],
    ["galleryScene8", {}, "/images/17/al-19-67-Beauty.webp"]
    ],
    },
    "Danny": {
    1: [
    ["dannyhandjob", {}, "/images/2/185.webp"],
    ["galleryScene1", {}, "/images/4/227.webp"],
    ],
    },
    "Jenny": {
    1: [
    ["ep15jenny", {}, "/images/15/al-17-153-Beauty.webp"],
    ],
    },
    "Alice": {
    1: [
    ["ep11alice1", {}, "/images/11/209.webp"],
    ["ep11alice2", {}, "/images/11/277.webp"],
    ],
    },
    "Jamie": {
    1: [
    ["ep10jamieyes", {}, "/images/10/93.webp"],
    ],
    },
    "Other": {
    1: [
    ["ep14nar", {}, "/images/14/al-16-154-Beauty.webp"],
    ],
    },
    }

label galleryNameChange:
    default persistent.player_name = ""
    while persistent.player_name == "":
        $ persistent.player_name = renpy.input("What is your name?", default="Dan")
    return

screen sceneGalleryMenu():
    tag menu
    modal True
    add "#23272a"

    text "Oscar's Scene Gallery":
        style "galleryHeader"
        xcenter 0.5
        ycenter 165

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
                idle "/oscarAdditions/images/button.png"
                hover Transform(im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2)))
            text "Back":
                style "galleryBody"
                xcenter 0.5
                ycenter 0.5

        imagebutton:
            action OpenURL("https://www.patreon.com/oscarsix/overview")
            idle Transform("/oscarAdditions/images/become_a_patron_button.png", zoom=0.7465437788)
            hover Transform(im.MatrixColor("/oscarAdditions/images/become_a_patron_button.png", im.matrix.brightness(0.2)), zoom=0.7465437788)
            xanchor 1.0

    vpgrid:
        cols 4
        xspacing 50
        yspacing 37
        pos (117, 360)

        for i in sceneGalleryMenuDict["galleryMenu"]:
            vbox:
                imagebutton:
                    action ShowMenu("sceneCharacterMenu"), Hide("sceneGalleryMenu"), SetVariable("galleryCharacter", i[0])
                    idle Transform(i[1], zoom=0.2)
                    hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                text i[0]:
                    style "galleryBody"
                    xcenter 0.5

screen sceneCharacterMenu():
    tag menu
    modal True
    add "#23272a"

    text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
        style "galleryHeader"
        xcenter 0.5
        ycenter 165

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                if galleryPageNumber == 1:
                    action Show("sceneGalleryMenu"), Hide("sceneCharacterMenu")
                else:
                    action Function(galleryDecreasePageNumber)
                idle "/oscarAdditions/images/button.png"
                hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
            text "Back":
                style "galleryBody"
                xcenter 0.5
                ycenter 0.5

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            if galleryPageNumber != len(sceneGalleryMenuDict[galleryCharacter]):
                imagebutton:
                    action Function(galleryIncreasePageNumber)
                    idle "/oscarAdditions/images/button.png"
                    hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
                text "Next":
                    style "galleryBody"
                    xcenter 0.5
                    ycenter 0.5

    vpgrid:
        cols 4
        xspacing 50
        yspacing 100
        pos (117, 360)

        for i in sceneGalleryMenuDict[galleryCharacter][galleryPageNumber]:
            $ scopeDict = {"player_name":persistent.player_name}
            $ scopeDict.update(i[1])
            imagebutton:
                action Replay(i[0], scope=scopeDict, locked=False)
                idle Transform(i[2], zoom=0.2)
                hover Transform(im.MatrixColor(i[2], im.matrix.brightness(0.2)), zoom=0.2)
