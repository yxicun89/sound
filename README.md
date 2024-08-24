## 環境構築

まずは学習済みモデルのファイルをダウンロードします。

```
curl https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm -o data/model/deepspeech-0.9.3-models.pbmm
```

あるいは、シンプルに上のurlをブラウザで開いてダウンロードし、data/modelの下に配置してもOKです。

### Dockerを使う場合の環境構築

```
docker-compose build --no-cache
```
データが残っていてエラーが起きることがあるため、--no-cacheというオプションをつけています

### Dockerを使わない場合の環境構築

#### 下記のpythonライブラリをダウンロード
* flask
* librosa
* DeepSpeech

#### コマンドラインで下記を実行
```
python app.py
```

## アプリの使い方

ブラウザで http://localhost:5000/ を開くとファイル選択のUIが出るので、`data/audio/sample.wav`をアップしてください。

おおよそ、英語の音声書き起こしが出来ていることがわかると思います。