import record
import wav2pcm
import sound2wordXF
import tuling
import com_sound2

record.rec("1kXF.wav")  # 实现录音，将文件存储在1k.wav
words = sound2wordXF.wordfromS("1kXF.wav")  # 读取录音文件，通过API实现语音转写
new_words = tuling.Tuling(words)  # 实现与图灵机器人会话
com_sound2.getsound(new_words)  # 将机器人回复的文字转化为语音
wav2pcm.play_mp3("D:/output1.mp3")  # 播放机器人的语音文件


