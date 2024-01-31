import os

#Path of the images for the game and hero
IMAGE_PATH = {
    "golf": os.path.join(os.getcwd(), "resources/images/gold.png"),
    "background": os.path.join(os.getcwd(), "resources/images/background.png"),
    "apple": os.path.join(os.getcwd(), "resources/images/apple.png"),
    "hero": [os.path.join(os.getcwd(), "resources/images/%d.png" % i) for i in range(1, 11)] #this list comprehension takes the number of the images of the hero
}

#Path of the audios for the game
AUDIO_PATH = {
    "coin_sound": os.path.join(os.getcwd(), "resources/audios/get.wav"),
    "music": os.path.join(os.getcwd(), "resources/audios/bgm.mp3")
}

#Path of the font for the game
FONT_PATH = os.path.join(os.getcwd(), "resources/font/font.TTF")

HIGHEST_SCORE_RECORD_FILEPATH = "highest_score.rec"

screen_size = (800, 600)

background_color = (0, 160, 233)

FPS = 30