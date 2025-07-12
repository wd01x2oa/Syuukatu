import numpy as np
import matplotlib.pyplot as  plt
from pydub import AudioSegment
from scipy import fftpack
from scipy.io import wavfile

fs, data = wavfile.read("data_piano5.wav") #相対PASSを指定

#変換する音声ファイルのパス
input_file = "data_piano5.wav" #変数 input_file 相対PASSを指定

#音声ファイルを読み込み
audio = AudioSegment.from_wav(input_file) #

# モノラルからステレオに変換し,モノラル変換は1, ステレオ変換は2
stereo_audio = audio.set_channels(1) #変数 stereo_file 音声ファイルを読み込み モノラル変換は1

#変換後の音声ファイルを保存
output_file = "data_piano6.wav"
stereo_audio.export(output_file, format = "wav")

# 基本情報の表示
print(f'channel: {output_file.channels}')
print(f'frame rate: {output_file.frame_rate}')
print(f'duration: {output_file.duration_seconds} s')
print(f'sample width: {output_file.sample_width}')


# テストデータの生成
N = 1000
ts = 0.0
te = 1.0
t = np.linspace(ts, te, N) #配列の始点と終点を指定
x = 1.0*np.sin(2.0*np.pi*100.0*t) + 0.5*np.cos(2.0*np.pi*10.0*t) + 0.05*np.random.rand(N)

# DET
X = np.fft.fft(x)
dt = t[1] - t[0] #時間刻み
f = np.fft.fftfreq(N, dt) # Xのindexに対応する周波数のndarryを取得

# データをプロット
fig, (ax01, ax02) = plt.subplots(nrows = 2, figsaize = (6, 8))

plt.subplots_sdjust(wspace = 0.0, hspace = 0.6)

ax01.set_xlabel('time (s)')
ax01.set_ylabel('X')
ax01.plot(t,x) #入力信号

# ax02.set_xlim(0, f.max)
ax02.set_xlabel('frequency (HZ)')
ax02.set_ylabel('|x|/|N|')
ax02.plot(f, np.ads(x)/N) #増幅スペクトル

# data.shapeで形を調べる
# 第1次元は行の数,第2次元は列の数
print("The shape of the audio array is", output_file .shape)

#モノラル再生に変換したのでoutput_file[:, 0]
#第0番目の列を選択
audio(output_file[:, 0], rate=output_file)

# plotがutput_fileの列を一つずつ書く
plt.plot(output_file)

time = np.arange(data.shape[0]) / fs
plt.plot(time, output_file)

# 図情報を追加はできます。
# タイトル
plt.title("Piano sound sample.1")
plt.xlabel("Time [s1]")
plt.ylabel("Audio intensity1")

plt.title("Piano sound sample.2")
plt.xlabel("Time [s2]")
plt.ylabel("Audio intensity2")

# レジェンド
plt.legend(["Left channel", "Right channel"])

plt.show()















