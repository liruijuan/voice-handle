import record
import wav2pcm
import sound2word
import tuling
import speakout

record.rec("1k.wav")    # 实现录音，将文件存储在1k.wav
#pcm_file = wav2pcm.wav_to_pcm("1k.wav") #将wav格式的语音转化为pcm格式
words = sound2word.asr_main("1k.wav") # 读取录音文件，通过API实现语音转写
new_words = tuling.Tuling(words)    #实现与图灵机器人会话
speakout.tts_main(new_words)    #将机器人回复的文字转化为语音
wav2pcm.play_mp3("test.mp3")    #播放机器人的语音文件chat_main2.py