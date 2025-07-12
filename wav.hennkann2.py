import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment

# 変換する音声ファイルのパス
input_file = "data_piano6.wav"

# 音声ファイルを読み込みます
audio = AudioSegment.from_wav(input_file)

# モノラルからステレオに変換します
stereo_audio = audio.set_channels(2)

# 変換後の音声ファイルを保存します
output_file = "data_piano7.wav"
stereo_audio.export(output_file, format="wav")

# 変換後の音声ファイルを再度読み込みます
audio = AudioSegment.from_wav(output_file)

# モノラル変換をしたので、channels = 1
sig = np.array(audio.get_array_of_samples())[::audio.channels]

# ステレオ音声の場合はこの操作は必須
# sig = np.array(audio.get_array_of_samples())[::audio.channels]

dt = 1.0 / audio.frame_rate  # サンプリング時間
tms = 0.0  # サンプル開始時間を0にセット
tme = audio.duration_seconds  # サンプル終了時刻
tm = np.linspace(tms, tme, len(sig), endpoint=False)  # 時間ndarryを作成
N = len(sig)
X = np.fft.fft(sig)
f = np.fft.fftfreq(N, dt)  # Xのindexに対応する周波数のndarrayを取得

# データをプロット
fig, (ax01, ax02) = plt.subplots(nrows=2, figsize=(6, 8))
plt.subplots_adjust(wspace=0.0, hspace=0.6)
ax01.set_xlim(tms, tme)
ax01.set_xlabel('time (s)')
ax01.set_ylabel('x')
ax01.plot(tm, sig, label='Mono')
ax01.legend(["Mono"])
ax02.set_xlim(0, 2000)  # 振幅スペクトルを0 ~ 2000 Hzまで表示
ax02.set_xlabel('frequency (Hz)')
ax02.set_ylabel('|x|/N')
ax02.plot(f[0:N//2], np.abs(X[0:N//2]/N))

# 図情報を追加できます。
# タイトル
plt.suptitle("Piano sound sample")
# 軸のラベル
ax01.set_xlabel("Time [s]")
ax01.set_ylabel("Audio intensity")
# レジェンド
ax01.legend(["Mono"])
plt.show()
