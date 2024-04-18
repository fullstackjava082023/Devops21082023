import gtts
def text_to_mp3():
    # make a request to google to get synthesis
    t1 = gtts.gTTS("Hello it is Arja i am writing you")
    # save the audio file
    t1.save("welcome.mp3")

def main():
    text_to_mp3()


if __name__ == '__main__':
    main()