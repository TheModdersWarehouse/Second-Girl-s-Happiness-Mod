init python:
    def galleryDecreasePageNumber():
        global galleryPageNumber
        galleryPageNumber -= 1

    def galleryIncreasePageNumber():
        global galleryPageNumber
        galleryPageNumber += 1

define galleryPageNumber = 1

define sceneGalleryMenuDict = {
    "galleryMenu": [
    ["All", ""],
    ],
    "All": {
    1: [
    ["galleryScene1", {}, "/images/bathroommorning5.png"],
    ["fire2girls", {}, "/images/firepitanim1.png"],
    ["sandymorninga", {}, "/images/giannanet13.png"],
    ["katrinagianna", {}, "/images/katseduction16.png"],
    ["galleryScene2", {}, "/images/kendrahula12.png"],
    ["party1", {"pickupemily":True, "katharem":True}, "/images/party12.png"],
    ["cosplayno", {"confidence":99}, "/images/showerscene9.png"],
    ],
    },
    }

label galleryNameChange:
    default persistent.y = ""
    if persistent.y == "":
        $ persistent.y = renpy.input("Answer with your name.", default="Kyle")
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
        spacing 13
        pos (1245, 33) ## ^^ All set for 720p

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
                idle "/oscarAdditions/images/button.png"
                hover Transform(im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2)))
            text "Back":
                style "modTextBody"
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
                idle "/oscarAdditions/images/button.png"
                hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        fixed:
            xmaximum 124
            ymaximum 51
            xanchor 1.0

            if galleryPageNumber != len(sceneGalleryMenuDict[galleryCharacter]):
                imagebutton:
                    action Function(galleryIncreasePageNumber)
                    idle "/oscarAdditions/images/button.png"
                    hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
                text "Next":
                    style "modTextBody"
                    xcenter 0.5
                    ycenter 0.5

    vpgrid:
        cols 4
        xspacing 33
        yspacing 66
        pos (78, 240)

        for i in sceneGalleryMenuDict[galleryCharacter][galleryPageNumber]:
            $ scopeDict = {"y":persistent.y}
            $ scopeDict.update(i[1])
            imagebutton:
                action Replay(i[0], scope=scopeDict, locked=False)
                idle Transform(i[2], zoom=0.2)
                hover Transform(im.MatrixColor(i[2], im.matrix.brightness(0.2)), zoom=0.2)
