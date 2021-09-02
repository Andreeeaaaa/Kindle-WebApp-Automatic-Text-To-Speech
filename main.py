def main():
    print('\n\nKindle Reader - developed by Andreeeaaaa.\n\nHOW TO USE THE PROGRAM:\nOnce you start the program, you have 30 seconds to put your kindle reader web application full screen (press f11). Please make sure that the reader is in light mode for better results.\n\n')
    start = input('Input "Start" to start the process, "Language" to change the language (italian = default).\n')

    if start.upper() == 'START':
        import gui, read, speak
        import time, os
        os.environ['TESSDATA_PREFIX'] = os.getcwd() + '/etc/tessdata'

        print('30 seconds to start')
        time.sleep(30)

        while True:
            gui.take_screenshot()
            print('Screenshot taken')

            text = read.img_to_text()
            print('text aquired')

            speak.text_to_mp3(text)
            print('to mp3')

            speak.mp3_to_wav()
            print('to wav')

            try: speak_obj.wait_done() 
            except: pass

            speak_obj = speak.speak()
            print('Reading out loud')

            gui.change_page()
            print('Changed page')
    
    if start.upper() == 'LANGUAGE':
        lang = input('Do you want:\n1. Italian     2. English\nInput 1 or 2\n')
        
        if lang == '1':
            import json
            import settings
            with open(settings.WORKSPACE_DIR + '/language.json', 'w') as lang_file:
                json.dump({'language': 'ita'}, lang_file)
    
            print('Language changed to italian, restarting.')
            main()
        
        if lang == '2':
            import json
            import settings
            with open(settings.WORKSPACE_DIR + '/language.json', 'w') as lang_file:
                json.dump({'language': 'eng'}, lang_file)

            print('Language changed to english, restarting.')
            main()
        
        else:
            print('Invalid input. Restarting')
            main()
    
    else:
        print('Invalid input, closing the program')
        exit()

if __name__ == '__main__':
    main()
