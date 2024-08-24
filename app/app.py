import os
import numpy as np
import librosa
from deepspeech import Model
from flask import Flask, request

app = Flask(__name__)

def get_text_from_soundfile(model, fpath):
    sample_rate = model.sampleRate()
    audio_arr, _ = librosa.load(fpath, sample_rate)
    # librosaがfloat型でのアウトプットだが、deepspeechがint16の入力しかサポートしていないため
    # データ型を変換
    int16_audio_arr = (
        audio_arr * np.iinfo(np.int16).max
    ).astype(np.int16)
    return model.stt(int16_audio_arr)


@app.route('/', methods=["GET", "POST"])
def main():
    # 音声ファイルをアップするためのhtml
    html = """
    <form method="post" enctype="multipart/form-data">
        <p>
            音声ファイルを選択してください（wavファイル形式のみ動作確認済み）
        </p>
        <p>
            <input type="file" name="file" id="file">
        </p>
        <p>
            <input type="submit" value="Upload" name="submit">
        </p>
    </form>
    """

    # 音声ファイルがアップされた場合は、その解析結果も最初に出す
    if request.method == 'POST':
        save_file_path = "model_input.wav"
        f = request.files['file']
        f.save(save_file_path)
        text_from_voice = get_text_from_soundfile(ds_model, save_file_path)
        html = "<p>解析結果：{}</p>".format(text_from_voice) + html

    return html

if __name__ == "__main__":
    ds_model = Model("python/sound_sample_app/data/model/deepspeech-0.9.3-models(1).pbmm")
    os.environ["FLASK_ENV"] = "development"
    app.run(debug=True)