import pickle
import time

while(True):
    with open('deepSpeech/shared.pkl', 'rb') as f:
        print(pickle.load(f))
    time.sleep(1)
