import pyaudio
import wave
from aip import AipSpeech
from xpinyin import Pinyin
import paho.mqtt.client as mqtt
import requests
#from weather import *
#from nature import *
from music import *
 
 
MQTTHOST = "47.101.154.50"
MQTTPORT = 1883
mqttClient = mqtt.Client()


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 8000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "录音.wav"


APP_ID = '15834169'
API_KEY = 'sG4lDgskMHePrG3GjoDGLR4t'
SECRET_KEY = 'fk8FILysQEqRAt66dQX9SIThGzVrIm7e'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

STATE = 0
TIME_START = 0
TIME_END = 0

num = 0
    

def onMqttConnect():
    mqttClient.connect(MQTTHOST, MQTTPORT, 60)
    mqttClient.loop_start()
 
def onPublish(topic, payload, qos):
    mqttClient.publish(topic, payload, qos)

def readFile(fileName):
    with open(fileName, 'rb') as fp:
        return fp.read()
    
def writeFile(fileName,result):
    with open(fileName, 'wb') as fp:
        fp.write(result)
    
def getBaiduText():
	
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    stream.start_stream()
    print("* 开始录音......")

    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    
    print("* 正在识别......")
    result = client.asr(readFile('录音.wav'), 'wav', 16000, {
    'dev_pid': 1536,
})
    if result["err_no"] == 0:
        for t in result["result"]:
            return t
    else:
        print("没有识别到语音\n")
        return ""


def getBaiduVoice(text):
    result  = client.synthesis(text, 'zh', 6, {'vol': 5, 'per':4,'spd':5})
    if not isinstance(result, dict):
        writeFile("录音.wav",result)
    playVoice("录音.wav")


#def getVoiceResult():
    #return baiduVoice()

def getPinYin(result):
    pin = Pinyin()
    return pin.get_pinyin(result)


def wakeUp(result,pinyin):
  #  if getPinYin("狗") in pinyin:
    if getPinYin("你好") in pinyin:
        print("你好")
        getBaiduVoice("你好")
       
   # elif getPinYin("天气") in pinyin:
        #getBaiduVoice(getWeatherInfo(getCity(result)))
    #elif getPinYin("听") in pinyin:
       # downMusic(getMusicName(result))
    #elif getPinYin("首") in pinyin:
        #downMusic(getMusicName(result))
    
  #  else:
   #     print("我在")
    #    playVoice("im.mp3")
    

def main():
    onMqttConnect()
    count=1
    while count==1:
        count=count+1
        result = getBaiduText()
        pinyin = getPinYin(result)
        print("等待唤醒")
        print(result)
        wakeUp(result,pinyin)
            

            
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        #os.system("del back.mp3")
        os.system("del 录音.wav")
        os.system("rmdir /s/q __pycache__")
       

