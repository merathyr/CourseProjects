# M. Romain - Assig6b
# Input:      N/A
# Processing: N/A
# Output:     Display Animation - "A Beautiful Day"

import pygame, time
from pygame.locals import *

# Step 1:  Setup game/animation.
pygame.init()
windowWidth = 800
windowHeight = 700
window = pygame.display.set_mode([windowWidth, windowHeight])
pygame.display.set_caption("A Beautiful Day")
# Fonts
myFont1 = pygame.font.SysFont("Baskerville Old Face", 60)
myFont2 = pygame.font.SysFont("Niagara Solid", 50)
myFont3 = pygame.font.SysFont("Sylfaen", 23)
myFont4 = pygame.font.SysFont("Sylfaen", 15)
myFont5 = pygame.font.SysFont("High Tower Text", 28)
myFont6 = pygame.font.SysFont("High Tower Text", 60)
sansFont = pygame.font.SysFont("Comic Sans MS", 15)
sansFont2 = pygame.font.SysFont("Comic Sans Ms", 25)
# Colours
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
pink = (255, 0, 190)
orange = (255, 160, 0)
# Images
sansImg = pygame.image.load("Sans.jpg")  # Normal eyes
sans2Img = pygame.image.load("Sans 2.jpg")  # Eyes closed
sans3Img = pygame.image.load("Sans 3.jpg")  # Black eyes
sans4Img = pygame.image.load("Sans Blue.JPG")  # Blue eye
sans5Img = pygame.image.load("Sans 5.png")  # Shrugging
textbubbleImg = pygame.image.load("Text Bubble.JPG")
bones1Img = pygame.image.load("Row Bones.png")
bones2Img = pygame.image.load("Row Bones 2.png")  # Flipped 90 degrees counter clockwise
bones3Img = pygame.image.load("Row Bones 3.png")  # Upside down
bones4Img = pygame.image.load("Row Bones 4.png")  # Flipped 90 degrees clockwise
doubbonesImg = pygame.image.load("Double row bones.JPEG")
# Music & Sound Effects
musicFile1 = ("Birds Chirping.wav")
musicFile2 = ("Megalovania.wav")
# Positions
heartX = 0
loadingX = 0
loading2X = 0
sansX = 0
sans2X = 0
pixelHeartX = 0
pixelHeartY = 0
bones1X = 0
bones1Y = 0
bones2X = 0
bones2Y = 0
bones3Y = 0
bones4X = 0
doubbonesX = 0
# Scene & Pause
scene = 0
pause = 5

# Step 2:  Set up game loop and poll for events.
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        break

# Step 3:  Update game and objects
    if scene == 0 and heartX <= 950:  # Title Page
        words = myFont1.render("A Beautiful Day", 3, white)
        words10 = myFont5.render("Loading...", 3, black)
        heartX = heartX + 3
        loadingX = loadingX + 3
        heart1 = (5 + heartX, 500, 20, 20)  # Starts from the bottom
        heart2 = (-15 + heartX, 480, 60, 20)
        heart3 = (-35 + heartX, 460, 100, 20)
        heart4 = (-55 + heartX, 440, 140, 20)
        heart5 = (-75 + heartX, 420, 180, 20)
        heart6 = (-95 + heartX, 400, 220, 20)
        heart7 = (-115 + heartX, 380, 260, 20)
        heart8 = (-115 + heartX, 360, 260, 20)
        heart9 = (-115 + heartX, 340, 260, 20)
        heart10 = (-95 + heartX, 320, 100, 20)
        heart11 = (25 + heartX, 320, 100, 20)
        heart12 = (-75 + heartX, 300, 60, 20)
        heart13 = (45 + heartX, 300, 60, 20)
        loadingBar1 = (-10, 530, 820, 40)  # Hollow loading bar
        loadingBar2 = (-1200 + loadingX, 533, 1100, 35)
        pause = 0.01
    elif scene == 1:  # Sans Dialogue 1
        sans2ImgScaled = pygame.transform.scale(sans2Img, (200, 220))
        orangeRec1 = (75, 640, 120, 45)
        orangeRec2 = (250, 640, 120, 45)
        orangeRec3 = (425, 640, 120, 45)
        orangeRec4 = (600, 640, 120, 45)
        textbubbleImgScaled = pygame.transform.scale(textbubbleImg, (240, 100))
        sansWords1 = sansFont.render("It's a beautiful day outside.", 2, black)
        words10 = myFont2.render("FIGHT", 2, orange)
        words3 = myFont2.render("ACT", 2, orange)
        words4 = myFont2.render("ITEM", 2, orange)
        words5 = myFont2.render("MERCY", 2, orange)
        words6 = myFont3.render("YOU", 2, white)
        words7 = myFont3.render("LV 19", 2, white)
        words8 = myFont4.render("HP", 2, white)
        hpBar = (330, 610, 127, 20)
        words9 = myFont3.render("92 / 92", 2, white)
        pygame.mixer.music.load(musicFile1)
        pygame.mixer.music.play(0)
        pause = 2.5
    elif scene == 2:  # Sans Dialogue 2
        sansWords2 = sansFont.render("Birds are singing,", 2, black)
        sansWords3 = sansFont.render("flowers are blooming...", 2, black)
        pause = 3
    elif scene == 3:  # Sans Dialogue 3
        sansWords4 = sansFont.render("On days like these,", 2, black)
        sansWords5 = sansFont.render("kids like you...", 2, black)
        pause = 3
    elif scene == 4:  # Blank screen & Birds chirping stops
        pygame.mixer.music.stop()
        pause = 0.2
    elif scene == 5:  # Sans Dialogue 4
        sans3ImgScaled = pygame.transform.scale(sans3Img, (130, 170))
        sansWords6 = sansFont2.render("SHOULD DIE", 2, black)
        pause = 2.5
    elif scene == 6 and pixelHeartY >= -113:  # Moves pixel heart down by itself
        sans4ImgScaled = pygame.transform.scale(sans4Img, (130, 177))
        whiteRec = (270, 330, 250, 270)
        pixelHeartY = pixelHeartY - 5
        pixelHeart1 = (395, 480 - pixelHeartY, 2, 2)  # Starts from the bottom
        pixelHeart2 = (393, 478 - pixelHeartY, 6, 2)
        pixelHeart3 = (391, 476 - pixelHeartY, 10, 2)
        pixelHeart4 = (389, 474 - pixelHeartY, 14, 2)
        pixelHeart5 = (387, 472 - pixelHeartY, 18, 2)
        pixelHeart6 = (385, 470 - pixelHeartY, 22, 2)
        pixelHeart7 = (383, 468 - pixelHeartY, 26, 2)
        pixelHeart8 = (381, 466 - pixelHeartY, 30, 2)
        pixelHeart9 = (381, 464 - pixelHeartY, 30, 2)
        pixelHeart10 = (383, 462 - pixelHeartY, 12, 2)
        pixelHeart11 = (397, 462 - pixelHeartY, 12, 2)
        pixelHeart12 = (385, 460 - pixelHeartY, 8, 2)
        pixelHeart13 = (399, 460 - pixelHeartY, 8, 2)
        pause = 0.03
    elif scene == 7 and pixelHeartY <= 0 and bones1Y <= 85:  # Heart & bones move up from bottom
        bones1ImgScaled = pygame.transform.scale(bones1Img, (250, 180))
        pixelHeartY = pixelHeartY + 5
        bones1Y = bones1Y + 5
        pixelHeart1 = (395, 480 - pixelHeartY, 2, 2)  # Starts from the bottom
        pixelHeart2 = (393, 478 - pixelHeartY, 6, 2)
        pixelHeart3 = (391, 476 - pixelHeartY, 10, 2)
        pixelHeart4 = (389, 474 - pixelHeartY, 14, 2)
        pixelHeart5 = (387, 472 - pixelHeartY, 18, 2)
        pixelHeart6 = (385, 470 - pixelHeartY, 22, 2)
        pixelHeart7 = (383, 468 - pixelHeartY, 26, 2)
        pixelHeart8 = (381, 466 - pixelHeartY, 30, 2)
        pixelHeart9 = (381, 464 - pixelHeartY, 30, 2)
        pixelHeart10 = (383, 462 - pixelHeartY, 12, 2)
        pixelHeart11 = (397, 462 - pixelHeartY, 12, 2)
        pixelHeart12 = (385, 460 - pixelHeartY, 8, 2)
        pixelHeart13 = (399, 460 - pixelHeartY, 8, 2)
        blackRec1 = (230, 600, 350, 200)
        pause = 0.03
    elif scene == 8 and pixelHeartX <= 103 and bones1Y >= -500:  # Move heart to right and move bones down at same time
        pixelHeartX = pixelHeartX + 3
        bones1Y = bones1Y + 5
        pixelHeart1 = (395 + pixelHeartX, 500, 2, 2)  # Starts from the bottom
        pixelHeart2 = (393 + pixelHeartX, 498, 6, 2)
        pixelHeart3 = (391 + pixelHeartX, 496, 10, 2)
        pixelHeart4 = (389 + pixelHeartX, 494, 14, 2)
        pixelHeart5 = (387 + pixelHeartX, 492, 18, 2)
        pixelHeart6 = (385 + pixelHeartX, 490, 22, 2)
        pixelHeart7 = (383 + pixelHeartX, 488, 26, 2)
        pixelHeart8 = (381 + pixelHeartX, 486, 30, 2)
        pixelHeart9 = (381 + pixelHeartX, 484, 30, 2)
        pixelHeart10 = (383 + pixelHeartX, 482, 12, 2)
        pixelHeart11 = (397 + pixelHeartX, 482, 12, 2)
        pixelHeart12 = (385 + pixelHeartX, 480, 8, 2)
        pixelHeart13 = (399 + pixelHeartX, 480, 8, 2)
        pause = 0.03
    elif scene == 9 and pixelHeartX >= -50 and bones2X >= -100:  # Heart and bones move out from right side
        bones2ImgScaled = pygame.transform.scale(bones2Img, (180, 270))
        pixelHeartX = pixelHeartX - 5
        bones2X = bones2X - 5
        pixelHeart1 = (378 + pixelHeartX, 500, 2, 2)  # Starts from the bottom
        pixelHeart2 = (376 + pixelHeartX, 498, 6, 2)
        pixelHeart3 = (374 + pixelHeartX, 496, 10, 2)
        pixelHeart4 = (372 + pixelHeartX, 494, 14, 2)
        pixelHeart5 = (370 + pixelHeartX, 492, 18, 2)
        pixelHeart6 = (368 + pixelHeartX, 490, 22, 2)
        pixelHeart7 = (366 + pixelHeartX, 488, 26, 2)
        pixelHeart8 = (364 + pixelHeartX, 486, 30, 2)
        pixelHeart9 = (364 + pixelHeartX, 484, 30, 2)
        pixelHeart10 = (366 + pixelHeartX, 482, 12, 2)
        pixelHeart11 = (380 + pixelHeartX, 482, 12, 2)
        pixelHeart12 = (368 + pixelHeartX, 480, 8, 2)
        pixelHeart13 = (382 + pixelHeartX, 480, 8, 2)
        blackRec2 = (519, 300, 200, 400)
        pause = 0.03
    elif scene == 10 and bones2X <= 80:  # Move bones to the right
        bones2X = bones2X + 5
        blackRec2 = (519, 300, 300, 400)
        pygame.mixer.music.load(musicFile2)
        pygame.mixer.music.play(0)
        pause = 0.03
    elif scene == 11:  # Text appears in the white square
        sans1ImgScaled = pygame.transform.scale(sansImg, (130, 170))
        whiteRec2 = (80, 400, 640, 200)
        text = myFont5.render("* You Feel Like You're Going To Have A Bad Time", 2, white)
        pause = 3.5
    elif scene == 12:  # Sans Dialogue 5
        sansWords7 = sansFont.render("Can you survive", 2, black)
        sansWords8 = sansFont.render("THIS?", 2, red)
        pause = 3
    elif scene == 13 and doubbonesX >= -2000:  # Everything but the pixel heart moves to the left
        doubbonesX = doubbonesX - 5
        sansX = sansX - 5
        doubbonesImgScaled = pygame.transform.scale(doubbonesImg, (1100, 200))
        sans5ImgScaled = pygame.transform.scale(sans5Img, (190, 190))
        whiteRec3 = (-10, 380, 820, 200)
        blackRec3 = (0, 182, 120, 190)
        blackRec4 = (680, 182, 150, 190)
        pause = 0.01
    elif scene == 14 and pixelHeartX <= 95:  # Pixel heart moves diagonally down
        pixelHeartX = pixelHeartX + 3
        pixelHeartY = pixelHeartY + 3
        pixelHeart1 = (378 + pixelHeartX, 500 + pixelHeartY, 2, 2)  # Starts from the bottom
        pixelHeart2 = (376 + pixelHeartX, 498 + pixelHeartY, 6, 2)
        pixelHeart3 = (374 + pixelHeartX, 496 + pixelHeartY, 10, 2)
        pixelHeart4 = (372 + pixelHeartX, 494 + pixelHeartY, 14, 2)
        pixelHeart5 = (370 + pixelHeartX, 492 + pixelHeartY, 18, 2)
        pixelHeart6 = (368 + pixelHeartX, 490 + pixelHeartY, 22, 2)
        pixelHeart7 = (366 + pixelHeartX, 488 + pixelHeartY, 26, 2)
        pixelHeart8 = (364 + pixelHeartX, 486 + pixelHeartY, 30, 2)
        pixelHeart9 = (364 + pixelHeartX, 484 + pixelHeartY, 30, 2)
        pixelHeart10 = (366 + pixelHeartX, 482 + pixelHeartY, 12, 2)
        pixelHeart11 = (380 + pixelHeartX, 482 + pixelHeartY, 12, 2)
        pixelHeart12 = (368 + pixelHeartX, 480 + pixelHeartY, 8, 2)
        pixelHeart13 = (382 + pixelHeartX, 480 + pixelHeartY, 8, 2)
        pause = 0.03
    elif scene == 15 and bones1X >= -2100:  # Everything but pixel heart moves to the left
        sans2X = sans2X - 5
        bones1X = bones1X - 5
        bones3ImgScaled = pygame.transform.scale(bones3Img, (250, 180))
        pixelHeart1 = (473, 570, 2, 2)  # Starts from the bottom
        pixelHeart2 = (471, 568, 6, 2)
        pixelHeart3 = (469, 566, 10, 2)
        pixelHeart4 = (467, 564, 14, 2)
        pixelHeart5 = (465, 562, 18, 2)
        pixelHeart6 = (463, 560, 22, 2)
        pixelHeart7 = (461, 558, 26, 2)
        pixelHeart8 = (459, 556, 30, 2)
        pixelHeart9 = (459, 554, 30, 2)
        pixelHeart10 = (461, 552, 12, 2)
        pixelHeart11 = (475, 552, 12, 2)
        pixelHeart12 = (463, 550, 8, 2)
        pixelHeart13 = (477, 550, 8, 2)
        blackRec5 = (-10, 259, 820, 120)
        pause = 0.01
    elif scene == 16 and bones3Y >= -130:  # The player dies
        bones1Y = bones1Y + 3
        bones2X = bones2X - 3
        bones3Y = bones3Y - 3
        bones4X = bones4X + 3
        bones4ImgScaled = pygame.transform.scale(bones4Img, (180, 270))
        pixelHeart1 = (395, 500, 2, 2)  # Starts from the bottom
        pixelHeart2 = (393, 498, 6, 2)  # Sub 10
        pixelHeart3 = (391, 496, 10, 2)
        pixelHeart4 = (389, 494, 14, 2)
        pixelHeart5 = (387, 492, 18, 2)
        pixelHeart6 = (385, 490, 22, 2)
        pixelHeart7 = (383, 488, 26, 2)
        pixelHeart8 = (381, 486, 30, 2)
        pixelHeart9 = (381, 484, 30, 2)
        pixelHeart10 = (383, 482, 12, 2)
        pixelHeart11 = (397, 482, 12, 2)
        pixelHeart12 = (385, 480, 8, 2)
        pixelHeart13 = (399, 480, 8, 2)
        blackRec6 = (73, 320, 200, 400)
        blackRec7 = (270, 130, 300, 200)
        pause = 0.02
    elif scene == 17 and loading2X >= 0 and loading2X <= 950:  # End Page
        loading2X = loading2X + 3
        pygame.mixer.music.stop()
        words11 = myFont6.render("GAME OVER", 3, white)
        words12 = myFont6.render("The End", 3, blue)
        words13 = myFont5.render("Loading New Game...", 3, black)
        loadingBar3 = (-1200 + loading2X, 533, 1100, 35)
        pause = 0.01
    else:
        break

# Step 4:  Draw on surface/window
    window.fill(black)
    if scene == 0:
        window.blit(words, ([200, 170]))
        pygame.draw.rect(window, red, heart1, 0)
        pygame.draw.rect(window, red, heart2, 0)
        pygame.draw.rect(window, red, heart3, 0)
        pygame.draw.rect(window, red, heart4, 0)
        pygame.draw.rect(window, red, heart5, 0)
        pygame.draw.rect(window, red, heart6, 0)
        pygame.draw.rect(window, red, heart7, 0)
        pygame.draw.rect(window, red, heart8, 0)
        pygame.draw.rect(window, red, heart9, 0)
        pygame.draw.rect(window, red, heart10, 0)
        pygame.draw.rect(window, red, heart11, 0)
        pygame.draw.rect(window, red, heart12, 0)
        pygame.draw.rect(window, red, heart13, 0)
        pygame.draw.rect(window, white, loadingBar1, 2)
        pygame.draw.rect(window, red, loadingBar2, 0)
        window.blit(words10, ([350, 538]))
        if heartX >= 950:
            scene = 1
    elif scene == 1:
        window.blit(sans2ImgScaled, (285, 110))
        pygame.draw.rect(window, orange, orangeRec1, 2)
        pygame.draw.rect(window, orange, orangeRec2, 2)
        pygame.draw.rect(window, orange, orangeRec3, 2)
        pygame.draw.rect(window, orange, orangeRec4, 2)
        window.blit(textbubbleImgScaled, (445, 175))
        window.blit(sansWords1, ([480, 195]))
        window.blit(words10, ([100, 638]))
        window.blit(words3, ([287, 638]))
        window.blit(words4, ([457, 638]))
        window.blit(words5, ([625, 638]))
        window.blit(words6, ([75, 610]))
        window.blit(words7, ([150, 610]))
        window.blit(words8, ([300, 612]))
        pygame.draw.rect(window, yellow, hpBar, 0)
        window.blit(words9, ([480, 610]))
        scene = 2
    elif scene == 2:
        window.blit(sans2ImgScaled, (285, 110))
        pygame.draw.rect(window, orange, orangeRec1, 2)
        pygame.draw.rect(window, orange, orangeRec2, 2)
        pygame.draw.rect(window, orange, orangeRec3, 2)
        pygame.draw.rect(window, orange, orangeRec4, 2)
        window.blit(textbubbleImgScaled, (445, 175))
        window.blit(sansWords2, ([480, 195]))
        window.blit(sansWords3, ([480, 220]))
        window.blit(words10, ([100, 638]))
        window.blit(words3, ([287, 638]))
        window.blit(words4, ([457, 638]))
        window.blit(words5, ([625, 638]))
        window.blit(words6, ([75, 610]))
        window.blit(words7, ([150, 610]))
        window.blit(words8, ([300, 612]))
        pygame.draw.rect(window, yellow, hpBar, 0)
        window.blit(words9, ([480, 610]))
        scene = 3
    elif scene == 3:
        window.blit(sans2ImgScaled, (285, 110))
        pygame.draw.rect(window, orange, orangeRec1, 2)
        pygame.draw.rect(window, orange, orangeRec2, 2)
        pygame.draw.rect(window, orange, orangeRec3, 2)
        pygame.draw.rect(window, orange, orangeRec4, 2)
        window.blit(textbubbleImgScaled, (445, 175))
        window.blit(sansWords4, ([480, 195]))
        window.blit(sansWords5, ([480, 220]))
        window.blit(words10, ([100, 638]))
        window.blit(words3, ([287, 638]))
        window.blit(words4, ([457, 638]))
        window.blit(words5, ([625, 638]))
        window.blit(words6, ([75, 610]))
        window.blit(words7, ([150, 610]))
        window.blit(words8, ([300, 612]))
        pygame.draw.rect(window, yellow, hpBar, 0)
        window.blit(words9, ([480, 610]))
        scene = 4
    elif scene == 4:
        scene = 5
    elif scene == 5:
        window.blit(sans3ImgScaled, (314, 150))
        pygame.draw.rect(window, orange, orangeRec1, 2)
        pygame.draw.rect(window, orange, orangeRec2, 2)
        pygame.draw.rect(window, orange, orangeRec3, 2)
        pygame.draw.rect(window, orange, orangeRec4, 2)
        window.blit(textbubbleImgScaled, (445, 175))
        window.blit(sansWords6, ([500, 205]))
        window.blit(words10, ([100, 638]))
        window.blit(words3, ([287, 638]))
        window.blit(words4, ([457, 638]))
        window.blit(words5, ([625, 638]))
        window.blit(words6, ([75, 610]))
        window.blit(words7, ([150, 610]))
        window.blit(words8, ([300, 612]))
        pygame.draw.rect(window, yellow, hpBar, 0)
        window.blit(words9, ([480, 610]))
        scene = 6
    elif scene == 6:
        window.blit(sans4ImgScaled, (314, 147))
        pygame.draw.rect(window, orange, orangeRec1, 2)
        pygame.draw.rect(window, orange, orangeRec2, 2)
        pygame.draw.rect(window, orange, orangeRec3, 2)
        pygame.draw.rect(window, orange, orangeRec4, 2)
        pygame.draw.rect(window, white, whiteRec, 4)
        pygame.draw.rect(window, red, pixelHeart1, 0)
        pygame.draw.rect(window, red, pixelHeart2, 0)
        pygame.draw.rect(window, red, pixelHeart3, 0)
        pygame.draw.rect(window, red, pixelHeart4, 0)
        pygame.draw.rect(window, red, pixelHeart5, 0)
        pygame.draw.rect(window, red, pixelHeart6, 0)
        pygame.draw.rect(window, red, pixelHeart7, 0)
        pygame.draw.rect(window, red, pixelHeart8, 0)
        pygame.draw.rect(window, red, pixelHeart9, 0)
        pygame.draw.rect(window, red, pixelHeart10, 0)
        pygame.draw.rect(window, red, pixelHeart11, 0)
        pygame.draw.rect(window, red, pixelHeart12, 0)
        pygame.draw.rect(window, red, pixelHeart13, 0)
        window.blit(words10, ([100, 638]))
        window.blit(words3, ([287, 638]))
        window.blit(words4, ([457, 638]))
        window.blit(words5, ([625, 638]))
        window.blit(words6, ([75, 610]))
        window.blit(words7, ([150, 610]))
        window.blit(words8, ([300, 612]))
        pygame.draw.rect(window, yellow, hpBar, 0)
        window.blit(words9, ([480, 610]))
        if pixelHeartY <= -113:
            scene = 7
    elif scene == 7:
        window.blit(sans4ImgScaled, (314, 147))
        window.blit(bones1ImgScaled, (270, 600 - bones1Y))
        pygame.draw.rect(window, black, blackRec1, 0)
        pygame.draw.rect(window, orange, orangeRec1, 2)
        pygame.draw.rect(window, orange, orangeRec2, 2)
        pygame.draw.rect(window, orange, orangeRec3, 2)
        pygame.draw.rect(window, orange, orangeRec4, 2)
        pygame.draw.rect(window, white, whiteRec, 4)
        pygame.draw.rect(window, red, pixelHeart1, 0)
        pygame.draw.rect(window, red, pixelHeart2, 0)
        pygame.draw.rect(window, red, pixelHeart3, 0)
        pygame.draw.rect(window, red, pixelHeart4, 0)
        pygame.draw.rect(window, red, pixelHeart5, 0)
        pygame.draw.rect(window, red, pixelHeart6, 0)
        pygame.draw.rect(window, red, pixelHeart7, 0)
        pygame.draw.rect(window, red, pixelHeart8, 0)
        pygame.draw.rect(window, red, pixelHeart9, 0)
        pygame.draw.rect(window, red, pixelHeart10, 0)
        pygame.draw.rect(window, red, pixelHeart11, 0)
        pygame.draw.rect(window, red, pixelHeart12, 0)
        pygame.draw.rect(window, red, pixelHeart13, 0)
        window.blit(words10, ([100, 638]))
        window.blit(words3, ([287, 638]))
        window.blit(words4, ([457, 638]))
        window.blit(words5, ([625, 638]))
        window.blit(words6, ([75, 610]))
        window.blit(words7, ([150, 610]))
        window.blit(words8, ([300, 612]))
        pygame.draw.rect(window, yellow, hpBar, 0)
        window.blit(words9, ([480, 610]))
        if bones1Y > 85:
            scene = 8
    elif scene == 8:
        window.blit(sans4ImgScaled, (314, 147))
        window.blit(bones1ImgScaled, (270, 400 + bones1Y))
        pygame.draw.rect(window, black, blackRec1, 0)
        pygame.draw.rect(window, orange, orangeRec1, 2)
        pygame.draw.rect(window, orange, orangeRec2, 2)
        pygame.draw.rect(window, orange, orangeRec3, 2)
        pygame.draw.rect(window, orange, orangeRec4, 2)
        pygame.draw.rect(window, white, whiteRec, 4)
        pygame.draw.rect(window, red, pixelHeart1, 0)
        pygame.draw.rect(window, red, pixelHeart2, 0)
        pygame.draw.rect(window, red, pixelHeart3, 0)
        pygame.draw.rect(window, red, pixelHeart4, 0)
        pygame.draw.rect(window, red, pixelHeart5, 0)
        pygame.draw.rect(window, red, pixelHeart6, 0)
        pygame.draw.rect(window, red, pixelHeart7, 0)
        pygame.draw.rect(window, red, pixelHeart8, 0)
        pygame.draw.rect(window, red, pixelHeart9, 0)
        pygame.draw.rect(window, red, pixelHeart10, 0)
        pygame.draw.rect(window, red, pixelHeart11, 0)
        pygame.draw.rect(window, red, pixelHeart12, 0)
        pygame.draw.rect(window, red, pixelHeart13, 0)
        window.blit(words10, ([100, 638]))
        window.blit(words3, ([287, 638]))
        window.blit(words4, ([457, 638]))
        window.blit(words5, ([625, 638]))
        window.blit(words6, ([75, 610]))
        window.blit(words7, ([150, 610]))
        window.blit(words8, ([300, 612]))
        pygame.draw.rect(window, yellow, hpBar, 0)
        window.blit(words9, ([480, 610]))
        if pixelHeartX >= 103:
            scene = 9
    elif scene == 9:
        window.blit(sans4ImgScaled, (314, 147))
        window.blit(bones2ImgScaled, (540 + bones2X, 330))
        pygame.draw.rect(window, black, blackRec2, 0)
        pygame.draw.rect(window, orange, orangeRec1, 2)
        pygame.draw.rect(window, orange, orangeRec2, 2)
        pygame.draw.rect(window, orange, orangeRec3, 2)
        pygame.draw.rect(window, orange, orangeRec4, 2)
        pygame.draw.rect(window, white, whiteRec, 4)
        pygame.draw.rect(window, red, pixelHeart1, 0)
        pygame.draw.rect(window, red, pixelHeart2, 0)
        pygame.draw.rect(window, red, pixelHeart3, 0)
        pygame.draw.rect(window, red, pixelHeart4, 0)
        pygame.draw.rect(window, red, pixelHeart5, 0)
        pygame.draw.rect(window, red, pixelHeart6, 0)
        pygame.draw.rect(window, red, pixelHeart7, 0)
        pygame.draw.rect(window, red, pixelHeart8, 0)
        pygame.draw.rect(window, red, pixelHeart9, 0)
        pygame.draw.rect(window, red, pixelHeart10, 0)
        pygame.draw.rect(window, red, pixelHeart11, 0)
        pygame.draw.rect(window, red, pixelHeart12, 0)
        pygame.draw.rect(window, red, pixelHeart13, 0)
        window.blit(words10, ([100, 638]))
        window.blit(words3, ([287, 638]))
        window.blit(words4, ([457, 638]))
        window.blit(words5, ([625, 638]))
        window.blit(words6, ([75, 610]))
        window.blit(words7, ([150, 610]))
        window.blit(words8, ([300, 612]))
        pygame.draw.rect(window, yellow, hpBar, 0)
        window.blit(words9, ([480, 610]))
        if bones2X < -100:
            scene = 10
    elif scene == 10:
        window.blit(sans4ImgScaled, (314, 147))
        window.blit(bones2ImgScaled, (500 + bones2X, 330))
        pygame.draw.rect(window, black, blackRec2, 0)
        pygame.draw.rect(window, orange, orangeRec1, 2)
        pygame.draw.rect(window, orange, orangeRec2, 2)
        pygame.draw.rect(window, orange, orangeRec3, 2)
        pygame.draw.rect(window, orange, orangeRec4, 2)
        pygame.draw.rect(window, white, whiteRec, 4)
        pygame.draw.rect(window, red, pixelHeart1, 0)
        pygame.draw.rect(window, red, pixelHeart2, 0)
        pygame.draw.rect(window, red, pixelHeart3, 0)
        pygame.draw.rect(window, red, pixelHeart4, 0)
        pygame.draw.rect(window, red, pixelHeart5, 0)
        pygame.draw.rect(window, red, pixelHeart6, 0)
        pygame.draw.rect(window, red, pixelHeart7, 0)
        pygame.draw.rect(window, red, pixelHeart8, 0)
        pygame.draw.rect(window, red, pixelHeart9, 0)
        pygame.draw.rect(window, red, pixelHeart10, 0)
        pygame.draw.rect(window, red, pixelHeart11, 0)
        pygame.draw.rect(window, red, pixelHeart12, 0)
        pygame.draw.rect(window, red, pixelHeart13, 0)
        window.blit(words10, ([100, 638]))
        window.blit(words3, ([287, 638]))
        window.blit(words4, ([457, 638]))
        window.blit(words5, ([625, 638]))
        window.blit(words6, ([75, 610]))
        window.blit(words7, ([150, 610]))
        window.blit(words8, ([300, 612]))
        pygame.draw.rect(window, yellow, hpBar, 0)
        window.blit(words9, ([480, 610]))
        if bones2X >= 80:
            scene = 11
    elif scene == 11:
        window.blit(sans1ImgScaled, (313, 219))
        pygame.draw.rect(window, white, whiteRec2, 4)
        pygame.draw.rect(window, orange, orangeRec1, 2)
        pygame.draw.rect(window, orange, orangeRec2, 2)
        pygame.draw.rect(window, orange, orangeRec3, 2)
        pygame.draw.rect(window, orange, orangeRec4, 2)
        window.blit(text, ([90, 450]))
        window.blit(words10, ([100, 638]))
        window.blit(words3, ([287, 638]))
        window.blit(words4, ([457, 638]))
        window.blit(words5, ([625, 638]))
        window.blit(words6, ([75, 610]))
        window.blit(words7, ([150, 610]))
        window.blit(words8, ([300, 612]))
        pygame.draw.rect(window, yellow, hpBar, 0)
        window.blit(words9, ([480, 610]))
        scene = 12
    elif scene == 12:
        window.blit(sans1ImgScaled, (315, 152))
        pygame.draw.rect(window, orange, orangeRec1, 2)
        pygame.draw.rect(window, orange, orangeRec2, 2)
        pygame.draw.rect(window, orange, orangeRec3, 2)
        pygame.draw.rect(window, orange, orangeRec4, 2)
        window.blit(textbubbleImgScaled, (445, 175))
        window.blit(sansWords7, ([480, 195]))
        window.blit(sansWords8, ([590, 195]))
        window.blit(words10, ([100, 638]))
        window.blit(words3, ([287, 638]))
        window.blit(words4, ([457, 638]))
        window.blit(words5, ([625, 638]))
        window.blit(words6, ([75, 610]))
        window.blit(words7, ([150, 610]))
        window.blit(words8, ([300, 612]))
        pygame.draw.rect(window, yellow, hpBar, 0)
        window.blit(words9, ([480, 610]))
        scene = 13
    elif scene == 13:
        window.blit(sans1ImgScaled, (315 + sansX, 192))
        window.blit(sans5ImgScaled, (715 + sansX, 183))
        window.blit(sans3ImgScaled, (1115 + sansX, 195))
        window.blit(sans2ImgScaled, (1515 + sansX, 152))
        window.blit(sans4ImgScaled, (1915 + sansX, 192))
        pygame.draw.rect(window, black, blackRec3, 0)
        pygame.draw.rect(window, black, blackRec4, 0)
        window.blit(doubbonesImgScaled, (850 + doubbonesX, 382))
        pygame.draw.rect(window, orange, orangeRec1, 2)
        pygame.draw.rect(window, orange, orangeRec2, 2)
        pygame.draw.rect(window, orange, orangeRec3, 2)
        pygame.draw.rect(window, orange, orangeRec4, 2)
        pygame.draw.rect(window, white, whiteRec3, 4)
        pygame.draw.rect(window, red, pixelHeart1, 0)
        pygame.draw.rect(window, red, pixelHeart2, 0)
        pygame.draw.rect(window, red, pixelHeart3, 0)
        pygame.draw.rect(window, red, pixelHeart4, 0)
        pygame.draw.rect(window, red, pixelHeart5, 0)
        pygame.draw.rect(window, red, pixelHeart6, 0)
        pygame.draw.rect(window, red, pixelHeart7, 0)
        pygame.draw.rect(window, red, pixelHeart8, 0)
        pygame.draw.rect(window, red, pixelHeart9, 0)
        pygame.draw.rect(window, red, pixelHeart10, 0)
        pygame.draw.rect(window, red, pixelHeart11, 0)
        pygame.draw.rect(window, red, pixelHeart12, 0)
        pygame.draw.rect(window, red, pixelHeart13, 0)
        window.blit(words10, ([100, 638]))
        window.blit(words3, ([287, 638]))
        window.blit(words4, ([457, 638]))
        window.blit(words5, ([625, 638]))
        window.blit(words6, ([75, 610]))
        window.blit(words7, ([150, 610]))
        window.blit(words8, ([300, 612]))
        pygame.draw.rect(window, yellow, hpBar, 0)
        window.blit(words9, ([480, 610]))
        if doubbonesX < -2000:
            scene = 14
    elif scene == 14:
        pygame.draw.rect(window, black, blackRec3, 0)
        pygame.draw.rect(window, black, blackRec4, 0)
        pygame.draw.rect(window, orange, orangeRec1, 2)
        pygame.draw.rect(window, orange, orangeRec2, 2)
        pygame.draw.rect(window, orange, orangeRec3, 2)
        pygame.draw.rect(window, orange, orangeRec4, 2)
        pygame.draw.rect(window, white, whiteRec3, 4)
        pygame.draw.rect(window, red, pixelHeart1, 0)
        pygame.draw.rect(window, red, pixelHeart2, 0)
        pygame.draw.rect(window, red, pixelHeart3, 0)
        pygame.draw.rect(window, red, pixelHeart4, 0)
        pygame.draw.rect(window, red, pixelHeart5, 0)
        pygame.draw.rect(window, red, pixelHeart6, 0)
        pygame.draw.rect(window, red, pixelHeart7, 0)
        pygame.draw.rect(window, red, pixelHeart8, 0)
        pygame.draw.rect(window, red, pixelHeart9, 0)
        pygame.draw.rect(window, red, pixelHeart10, 0)
        pygame.draw.rect(window, red, pixelHeart11, 0)
        pygame.draw.rect(window, red, pixelHeart12, 0)
        pygame.draw.rect(window, red, pixelHeart13, 0)
        window.blit(words10, ([100, 638]))
        window.blit(words3, ([287, 638]))
        window.blit(words4, ([457, 638]))
        window.blit(words5, ([625, 638]))
        window.blit(words6, ([75, 610]))
        window.blit(words7, ([150, 610]))
        window.blit(words8, ([300, 612]))
        pygame.draw.rect(window, yellow, hpBar, 0)
        window.blit(words9, ([480, 610]))
        if pixelHeartX >= 95:
            scene = 15
    elif scene == 15:
        window.blit(bones3ImgScaled, (700 + bones1X, 330))
        window.blit(bones3ImgScaled, (1200 + bones1X, 330))
        window.blit(bones3ImgScaled, (1800 + bones1X, 330))
        pygame.draw.rect(window, black, blackRec5, 0)
        window.blit(sans1ImgScaled, (315 + sans2X, 192))
        window.blit(sans5ImgScaled, (715 + sans2X, 183))
        window.blit(sans3ImgScaled, (1115 + sans2X, 195))
        window.blit(sans2ImgScaled, (1515 + sans2X, 152))
        window.blit(sans4ImgScaled, (1915 + sans2X, 192))
        pygame.draw.rect(window, black, blackRec3, 0)
        pygame.draw.rect(window, black, blackRec4, 0)
        pygame.draw.rect(window, orange, orangeRec1, 2)
        pygame.draw.rect(window, orange, orangeRec2, 2)
        pygame.draw.rect(window, orange, orangeRec3, 2)
        pygame.draw.rect(window, orange, orangeRec4, 2)
        pygame.draw.rect(window, white, whiteRec3, 4)
        pygame.draw.rect(window, red, pixelHeart1, 0)
        pygame.draw.rect(window, red, pixelHeart2, 0)
        pygame.draw.rect(window, red, pixelHeart3, 0)
        pygame.draw.rect(window, red, pixelHeart4, 0)
        pygame.draw.rect(window, red, pixelHeart5, 0)
        pygame.draw.rect(window, red, pixelHeart6, 0)
        pygame.draw.rect(window, red, pixelHeart7, 0)
        pygame.draw.rect(window, red, pixelHeart8, 0)
        pygame.draw.rect(window, red, pixelHeart9, 0)
        pygame.draw.rect(window, red, pixelHeart10, 0)
        pygame.draw.rect(window, red, pixelHeart11, 0)
        pygame.draw.rect(window, red, pixelHeart12, 0)
        pygame.draw.rect(window, red, pixelHeart13, 0)
        window.blit(words10, ([100, 638]))
        window.blit(words3, ([287, 638]))
        window.blit(words4, ([457, 638]))
        window.blit(words5, ([625, 638]))
        window.blit(words6, ([75, 610]))
        window.blit(words7, ([150, 610]))
        window.blit(words8, ([300, 612]))
        pygame.draw.rect(window, yellow, hpBar, 0)
        window.blit(words9, ([480, 610]))
        if bones1X < -2100:
            scene = 16
    elif scene == 16:
        window.blit(bones1ImgScaled, (270, 865 - bones1Y))  # Bottom
        window.blit(bones2ImgScaled, (450 + bones2X, 330))  # Right
        window.blit(bones3ImgScaled, (270, 150 - bones3Y))  # Top
        window.blit(bones4ImgScaled, (90 + bones4X, 330))  # Left
        pygame.draw.rect(window, black, blackRec1, 0)
        pygame.draw.rect(window, black, blackRec2, 0)
        pygame.draw.rect(window, black, blackRec7, 0)
        pygame.draw.rect(window, black, blackRec6, 0)
        window.blit(sans4ImgScaled, (314, 147))
        pygame.draw.rect(window, orange, orangeRec1, 2)
        pygame.draw.rect(window, orange, orangeRec2, 2)
        pygame.draw.rect(window, orange, orangeRec3, 2)
        pygame.draw.rect(window, orange, orangeRec4, 2)
        pygame.draw.rect(window, white, whiteRec, 4)
        pygame.draw.rect(window, red, pixelHeart1, 0)
        pygame.draw.rect(window, red, pixelHeart2, 0)
        pygame.draw.rect(window, red, pixelHeart3, 0)
        pygame.draw.rect(window, red, pixelHeart4, 0)
        pygame.draw.rect(window, red, pixelHeart5, 0)
        pygame.draw.rect(window, red, pixelHeart6, 0)
        pygame.draw.rect(window, red, pixelHeart7, 0)
        pygame.draw.rect(window, red, pixelHeart8, 0)
        pygame.draw.rect(window, red, pixelHeart9, 0)
        pygame.draw.rect(window, red, pixelHeart10, 0)
        pygame.draw.rect(window, red, pixelHeart11, 0)
        pygame.draw.rect(window, red, pixelHeart12, 0)
        pygame.draw.rect(window, red, pixelHeart13, 0)
        window.blit(words10, ([100, 638]))
        window.blit(words3, ([287, 638]))
        window.blit(words4, ([457, 638]))
        window.blit(words5, ([625, 638]))
        window.blit(words6, ([75, 610]))
        window.blit(words7, ([150, 610]))
        window.blit(words8, ([300, 612]))
        pygame.draw.rect(window, yellow, hpBar, 0)
        window.blit(words9, ([480, 610]))
        if bones3Y <= -130:
            scene = 17
    elif scene == 17:
        window.blit(words11, ([200, 170]))
        window.blit(words12, ([265, 290]))
        pygame.draw.rect(window, white, loadingBar1, 2)
        pygame.draw.rect(window, blue, loadingBar3, 0)
        window.blit(words13, ([295, 538]))
        if loading2X >= 900:
            scene = 18

# Step 5:  Show/display surface
    pygame.display.flip()
    time.sleep(pause)
pygame.display.quit()
quit()