
from speech_to_text.utils.exceptions import GenericCustomException





if __name__ == '__main__':
    file = open('../assets/male.wav')
    print get_test_from_speech(file)
