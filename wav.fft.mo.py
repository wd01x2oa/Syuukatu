import numpy as np
import  matplotlib as plt
from pydub import AudioSegment

#モノラルに変換
sounds = AudioSegment.from_wav("data_piano3.wav")
sound = sounds.set_channels(1)
sound.export("aiueo_LPFed.mp3", format="wav")

# モノラルに変換したので、sounds.channelsは1
sig =  np.array(sounds.get_array_of_samplies())[:: sounds.channels()]
dt = 1.0/sounds.frame_trate #サンプリング時間

#時間アレイを作る
tms = 0.0 # サンプル開始時間を0にセット
tme = sounds.duration_seconds # サンプル終了時刻
tm = np.linspace(tms, tme, len(sig), endpoint=False) #時間nunpy配列を作成

# #DFT
N = len(sig)
x = np.fft.fft(sig)
f = np.fft.fftfreq(N, dt) #xのindexに対応する周波数のnumpy配列を取得

# ローパスフィルター
f_cutoff_LPF = 5.0e2 #カットオフ周波数

X_LPFed = x.copy()
X_LPFed[(f > f_cutoff_LPF) | (f < -f_cutoff_LPF)] = 0.0
sig_LPFed =  np.real(np.fft.ifft(X_LPFed))

#音声データの書き出し
sounds_LPFed = AudioSegment(sig_LPFed.astype('int16').tobytes(),
                            sample_width = sounds.sample_width,
                            frame_reta =sounds.frame_rate, channels =1)
sounds_LPFed.export("aiueo_LPFed2.mp3", fprmat = "mp3") 

# ハイパスフィルター
f_cutoff_LPF = 10.0e2 #カットオフ周波数

X_HPfed = x.copy()
X_HPfed[((f > 0) & (f < f_cutoff_LPF)) | ((f < 0) & (f > -f_cutoff_HPF))] = 0.0 #カットオフ周波数より小さい周波数成分を0に

sig_HPFed = np.real(np.fft.ifft(X_HPfed))



# 音声データの書き出し
sounds_HPFed = AudioSegment(sig_HPFed.astype("int16").tobytes(), 
                            sample_width=sounds.sample_width, 
                            frame_rate=sounds.frame_rate, channels=1)
sounds_HPFed.export("aiueo_HPFed.mp3", format="mp3")

# データをプロット (なくても良い)
fig, (ax01, ax02) = plt.subplots(nrows=2, figsize=(6, 8))
plt.subplots_adjust(wspace=0.0, hspace=0.6)

ax01.set_xlim(tms, tme)
ax01.set_xlabel('time (s)')
ax01.set_ylabel('x')
ax01.plot(tm, sig, color='black') # 入力信号
ax01.plot(tm, sig_LPFed, color='blue') # LPF後の波形
ax01.plot(tm, sig_HPFed, color='orange') # LPF後の波形

ax02.set_xlim(0, 2000)
ax02.set_xlabel('frequency (Hz)')

ax02.set_ylabel('|X|/N')
ax02.plot(f[0:N//2], np.abs(x[0:N//2])/N, color='black') # 振幅スペクトル
ax02.plot(f[0:N//2], np.abs(X_LPFed[0:N//2])/N, color='blue') # 振幅スペクトル
ax02.plot(f[0:N//2], np.abs(X_HPfed[0:N//2])/N, color='orange') # 振幅スペクトル

plt.show()


