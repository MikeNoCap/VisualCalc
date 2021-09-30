import playsound
import random
import os


def full_path(file):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file)




nums = {
    "0": full_path(r"nums/zero.mp3"),
    "1": full_path(r"nums/one.mp3"),
    "2": full_path(r"nums/two.mp3"),
    "3": full_path(r"nums/three.mp3"),
    "4": full_path(r"nums/four.mp3"),
    "5": full_path(r"nums/five.mp3"),
    "6": full_path(r"nums/six.mp3"),
    "7": full_path(r"nums/seven.mp3"),
    "8": full_path(r"nums/eight.mp3"),
    "9": full_path(r"nums/nine.mp3"),
    "10": full_path(r"nums/ten.mp3")
}

def addition_voice(num1, num2):
    playsound.playsound(full_path(r"legge_sammen1.mp3"))
    playsound.playsound(nums[num1])
    playsound.playsound(full_path(r"og.mp3"))
    playsound.playsound(nums[num2])

addition_voice("3", "1")