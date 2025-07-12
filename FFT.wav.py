import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Audio
from scipy.io import wavfile

fs, data = wavfile.read("data_piano2.wav") #相対PASSを指定

# テストデータの生成
N = 1000
ts = 0.0
te = 1.0
t = np.linspace(ts, te, N)
x = 1.0*np.sin(2.0*np.pi*100.0*t) + 0.5*np.cos(2.0*np.pi*10.0*t) + 0.05*np.random.randn(N)

# DFT
X = np.fft.fft(x)
dt = t[1] - t[0] # 時間刻み
f = np.fft.fftfreq(N, dt) # Xのindexに対応する周波数のndarrayを取得

# データをプロット
fig, (ax01, ax02) = plt.subplots(nrows=2, figsize=(6, 8))
plt.subplots_adjust(wspace=0.0, hspace=0.6)

ax01.set_xlabel('time (s)')
ax01.set_ylabel('x')
ax01.plot(t, x) # 入力信号

# ax02.set_xlim(0, f.max())
ax02.set_xlabel('frequency (Hz)')
ax02.set_ylabel('|X|/N')
ax02.plot(f, np.abs(X)/N) # 振幅スペクトル

# `data.shape`でアレーの形を調べられます。
# 行列みたいに第一次元は行の数、第２次元は列の数です。
print("The shape of the audio array is", data.shape)
# モノラル再生しかいできないので、`data[:, 0]`を書いて、
# 第０目の列を選びます
Audio(data[:, 0], rate=fs)

# `plot`が`data`の列をひとつずつ書きます
plt.plot(data)

time = np.arange(data.shape[0]) / fs
plt.plot(time, data)


# 図情報を追加はできます。
# タイトル
plt.title("Piano sound sample")
# 軸のラベル
plt.xlabel("Time [s]")
plt.ylabel("Audio intensity")
# レジェンド
plt.legend(["Left channel", "Right channel"])

plt.show()




