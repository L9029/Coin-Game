import os

IMAGE_PATH = {
    "golf": os.path.join(os.getcwd(), "resources/images/gold.png"),
    "background": os.path.join(os.getcwd(), "resources/images/background.png"),
    "apple": os.path.join(os.getcwd(), "resources/images/apple.png"),
    "hero": [os.path.join(os.getcwd(), "resources/images/%d.png" % i) for i in range(1, 11)]
}

AUDIO_PATH = {
    "coin_sound": os.path.join(os.getcwd(), "resources/audios/get.wav"),
    "music": os.path.join(os.getcwd(), "resources/audios/bgm.mp3")
}

FONT_PATH = os.path.join(os.getcwd(), "resources/font/font.TTF")

HIGHEST_SCORE_RECORD_FILEPATH = "highest_score.rec"

screen_size = (800, 600)

background_color = (0, 160, 233)

FPS = 30