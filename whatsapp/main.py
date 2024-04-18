import pywhatkit

def main():
    # need to login to whatsapp manually with qr code in your browser
    pywhatkit.sendwhatmsg_instantly("+972524797754", "hi from python", 20, )


if __name__ == '__main__':
    main()


