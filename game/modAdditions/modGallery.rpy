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
["All", "img"],
]

define all = GalleryItem("All", 1, "galleryScene1", "bathroommorning5.png")
define all = GalleryItem("All", 1, "fire2girls", "firepitanim1.png")
define all = GalleryItem("All", 1, "sandymorninga", "giannanet13.png")
define all = GalleryItem("All", 1, "katrinagianna", "katseduction16.png")
define all = GalleryItem("All", 1, "galleryScene2", "kendrahula12.png")
define all = GalleryItem("All", 1, "party1", "party12.png", {"pickupemily":True, "katharem":True})
define all = GalleryItem("All", 1, "cosplayno", "showerscene9.png", {"confidence":99})
define all = GalleryItem("All", 1, "streaming3", "streaminglesson11.png")
define all = GalleryItem("All", 2, "joininwithalii", "boatgirlv1j.png")
define all = GalleryItem("All", 2, "katrinafulldom3", "boatdaykatrina8.png")
define all = GalleryItem("All", 2, "reenactment", "reenact9.png")
define all = GalleryItem("All", 2, "twostreaming1", "2streaming7.png")

default galleryPageNumber = 1
default scopeDict = {}

label galleryNameChange:
    default persistent.y = ""
    if persistent.y == "":
        $ persistent.y = renpy.input("Answer with your name.", default="Kyle")

    $ scopeDict = {"y":persistent.y}
    return

screen sceneGalleryMenu():
    tag menu
    modal True
    add "#23272a"

    text "Oscar's Scene Gallery":
        style "modTextHeader"
        xcenter 0.5
        ycenter 110

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

screen sceneCharacterMenu(galleryCharacter="All"):
    tag menu
    modal True
    add "#23272a"

    text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
        style "modTextHeader"
        xcenter 0.5
        ycenter 110

    vbox:
        spacing 13
        pos (1245, 33)

        fixed:
            xmaximum 124
            ymaximum 51
            xanchor 1.0

            imagebutton:
                if galleryPageNumber == 1:
                    action Hide("sceneCharacterMenu"), ShowMenu("main_menu")
                else:
                    action Function(galleryDecreasePageNumber)
                idle "/modAdditions/images/button.png"
                hover im.MatrixColor("/modAdditions/images/button.png", im.matrix.brightness(0.2))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        fixed:
            xmaximum 124
            ymaximum 51
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
        xspacing 33
        yspacing 66
        pos (78, 240)

        for galleryItem in galleryItems:
            if galleryItem.char == galleryCharacter and galleryItem.pageNum == galleryPageNumber:
                imagebutton:
                    action Replay(galleryItem.label, scope=updateScope(galleryItem.scope), locked=False)
                    idle Transform(galleryItem.thumbnail, zoom=0.2)
                    hover Transform(im.MatrixColor(galleryItem.thumbnail, im.matrix.brightness(0.2)), zoom=0.2)
