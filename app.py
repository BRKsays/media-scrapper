from flask import Flask, request, render_template
import yt_dlp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        media_type = request.form['media_type']
        format = request.form['format']
        resolution = request.form['resolution']

        if media_type == 'audio':
            ydl_opts = {
                'format': f'bestaudio[ext={format}]/best[ext={format}]',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': format,
                }],
            }
        else:
            ydl_opts = {
                'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
            }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return 'Download complete!'

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
app.debug = True
