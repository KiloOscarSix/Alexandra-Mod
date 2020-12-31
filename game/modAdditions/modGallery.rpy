init python:
    galleryItems = []

    class GalleryItem:
        def __init__(self, char, pageNum, label, thumbnail, scope=None):
            self.char = char
            self.pageNum = pageNum
            self.label = label
            if scope is None:
                scope = {}
            self.scope = scope
            self.thumbnail = "/images/{}".format(thumbnail)
            galleryItems.append(self)

    def galleryDecreasePageNumber():
        global galleryPageNumber
        galleryPageNumber -= 1

    def galleryIncreasePageNumber():
        global galleryPageNumber
        galleryPageNumber += 1

    def updateScope(newScope):
        rv = scopeDict.copy()
        rv.update(newScope)
        return rv

define galleryMenu = [
["Alexandra", "/images/1/123.webp"],
["Isabella", "/images/1/150.webp"],
["Adriana", "/images/1/54.webp"],
["Danny", "/images/2/174.webp"],
["Jenny", "/images/3/297.webp"],
["Alice", "/images/2/74.webp"],
["Jamie", "/images/1/75.webp"],
["Other", "/images/6/199.webp"],
]

define alexandra = GalleryItem("Alexandra", 1, "ep3bigcont6", "3/244.webp")
define alexandra = GalleryItem("Alexandra", 1, "ep4izzyalexblow", "4/118.webp")
define alexandra = GalleryItem("Alexandra", 1, "galleryScene2", "5/88.webp")
define alexandra = GalleryItem("Alexandra", 1, "ep6cont3", "6/73.webp", {"izzyin":True})
define alexandra = GalleryItem("Alexandra", 1, "galleryScene6", "7/236.webp")
define alexandra = GalleryItem("Alexandra", 1, "galleryScene7", "8/213.webp")
define alexandra = GalleryItem("Alexandra", 1, "ep9cont11", "9/315.webp")
define alexandra = GalleryItem("Alexandra", 1, "ep12cont8", "12/205.webp", {"izzyin":True})
define alexandra = GalleryItem("Alexandra", 2, "galleryScene9", "18/al-20-202-Beauty.webp")
define alexandra = GalleryItem("Alexandra", 2, "ep19cont4", "19/al-21-216-Beauty.webp")

define isabella = GalleryItem("Isabella", 1, "day5izzyshower", "5/135.webp")
define isabella = GalleryItem("Isabella", 1, "galleryScene3", "6/17.webp")
define isabella = GalleryItem("Isabella", 1, "galleryScene4", "7/22.webp")
define isabella = GalleryItem("Isabella", 1, "galleryScene5", "7/212.webp")
define isabella = GalleryItem("Isabella", 1, "ep12cont8", "7/236.webp")
define isabella = GalleryItem("Isabella", 1, "ep14izzy", "14/al-16-9-Beauty.webp")

define adriana = GalleryItem("Adriana", 1, "ep5adi2", "5/232.webp")
define adriana = GalleryItem("Adriana", 1, "ep8yesadi", "8/23.webp")
define adriana = GalleryItem("Adriana", 1, "galleryScene8", "17/al-19-61-Beauty.webp")

define galleryDanny = GalleryItem("Danny", 1, "dannyhandjob", "2/185.webp")
define galleryDanny = GalleryItem("Danny", 1, "galleryScene1", "4/227.webp")

define Jenny = GalleryItem("Jenny", 1, "ep15jenny", "15/al-17-153-Beauty.webp")

define alice = GalleryItem("Alice", 1, "ep11alice1", "11/209.webp")
define alice = GalleryItem("Alice", 1, "ep11alice2", "11/277.webp")

define jamie = GalleryItem("Jamie", 1, "ep10jamieyes", "10/93.webp")

define other = GalleryItem("Other", 1, "ep14nar", "14/al-16-154-Beauty.webp")
define other = GalleryItem("Other", 1, "ep20tanyayes", "20/al-22-136-Beauty.webp")


default galleryPageNumber = 1
default scopeDict = {}

label galleryNameChange:
    default persistent.player_name = ""
    if persistent.player_name == "":
        $ persistent.player_name = renpy.input("What is your name?", default="Dan")

    $ scopeDict = {"player_name":persistent.player_name}
    return

screen sceneGalleryMenu():
    tag menu
    modal True
    add "#23272a"

    text "Oscar's Scene Gallery":
        style "modTextHeader"
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
                idle "/modAdditions/images/button.png"
                hover Transform(im.MatrixColor("/modAdditions/images/button.png", im.matrix.brightness(0.2)))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        imagebutton:
            action OpenURL("https://www.patreon.com/oscarsix/overview")
            idle Transform("/modAdditions/images/become_a_patron_button.png", zoom=0.7465437788)
            hover Transform(im.MatrixColor("/modAdditions/images/become_a_patron_button.png", im.matrix.brightness(0.2)), zoom=0.7465437788)
            xanchor 1.0

    vpgrid:
        cols 4
        xspacing 50
        yspacing 37
        pos (117, 360)

        for i in galleryMenu:
            vbox:
                imagebutton:
                    action [Show("sceneCharacterMenu", galleryCharacter=i[0]), Hide("sceneGalleryMenu")]
                    idle Transform(i[1], zoom=0.2)
                    hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                text i[0]:
                    style "modTextBody"
                    xcenter 0.5

screen sceneCharacterMenu(galleryCharacter="Alexandra"):
    tag menu
    modal True
    add "#23272a"

    text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
        style "modTextHeader"
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
                idle "/modAdditions/images/button.png"
                hover im.MatrixColor("/modAdditions/images/button.png", im.matrix.brightness(0.2))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            if galleryPageNumber != max([galleryItem.pageNum for galleryItem in galleryItems if galleryItem.char == galleryCharacter]):
                imagebutton:
                    action Function(galleryIncreasePageNumber)
                    idle "/modAdditions/images/button.png"
                    hover im.MatrixColor("/modAdditions/images/button.png", im.matrix.brightness(0.2))
                text "Next":
                    style "modTextBody"
                    xcenter 0.5
                    ycenter 0.5

    vpgrid:
        cols 4
        xspacing 50
        yspacing 100
        pos (117, 360)

        for galleryItem in galleryItems:
            if galleryItem.char == galleryCharacter and galleryItem.pageNum == galleryPageNumber:
                imagebutton:
                    action Replay(galleryItem.label, scope=updateScope(galleryItem.scope), locked=False)
                    idle Transform(galleryItem.thumbnail, zoom=0.2)
                    hover Transform(im.MatrixColor(galleryItem.thumbnail, im.matrix.brightness(0.2)), zoom=0.2)

label beforeGalleryScene9:
    menu:
        mod "Path?"
        "Good":
            $ wheretoafterslayerbath = "good"
        "Neutral":
            $ wheretoafterslayerbath = "neutral"
        "Evil":
            $ wheretoafterslayerbath = "Evil"
    jump galleryScene9
