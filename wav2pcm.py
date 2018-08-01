import os

def wav_to_pcm(wav_file):
    #假设wav_file = "音频文件.wav"
    #wav_file.spilr(".")得到["音频文件","wav"]拿出第一个结果"音频文件"与".pcm"拼接，得到结果"音频文件.pcm"
    pcm_file = "%s.pcm"%(wav_file.split(".")[0])

    #就是此前在cmd窗口中输入命令，这里面就是让Python帮我们在cmd中执行命令
    os.system("D:/ffmpeg/bin/ffmpeg -y  -i %s  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 %s" %(wav_file,pcm_file))

    return pcm_file

def play_mp3(file_name):
    os.system("D:/ffmpeg/bin/ffplay  %s"%(file_name))