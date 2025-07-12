from pydub import AudioSegment

# 変換する音声ファイルのパス
input_file = "data_piano3.wav"

# 音声ファイルを読み込みます
audio = AudioSegment.from_wav(input_file)

# モノラルからステレオに変換します モノラル変換は1,ステレオ変換は2
stereo_audio = audio.set_channels(1)

# 変換後の音声ファイルを保存します
output_file = "data_piano4.wav"
stereo_audio.export(output_file, format="wav")