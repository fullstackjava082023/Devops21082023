import  PyPDF2
from gtts import gTTS

def main():
    pdfreader = PyPDF2.PdfReader(open("MA Sample Test B2.pdf", "rb"))
    clean_text = "my text"
    for page in pdfreader.pages:
        text = page.extract_text()
        clean_text = text.strip().replace('\n', ' ')
        print(clean_text)
    music_file = gTTS(clean_text)
    # save the audio file
    music_file.save("welcome.mp3")



if __name__ == '__main__':
    main()