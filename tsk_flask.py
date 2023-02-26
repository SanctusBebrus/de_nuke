from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'POST':
        file = request.files['file']
        with open('static/image.png', 'wb') as image:
            image.write(file.read())

    return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                 <link rel="stylesheet"
                                 href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                 integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                 crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='style.css')}"/>
                                <title>Загрузка фото</title>
                              </head>
                              <body>
                                <h1 class="text-mod">Выберите фоточку</h1>
                                <h2 class="text-mod">получите красоточку</h2>
                                <div class="block2">
                                    <form method="post" enctype="multipart/form-data">
                                       <div class="form-group">
                                            <label for="photo">Выбрать фоточку</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        </br>
                                        <img src="{url_for("static", filename="image.png")}" alt="" class="imag">
                                        </br>
                                        <button type="submit" class="btn btn-primary">Получить красоточку</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
