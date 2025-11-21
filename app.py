from Base import create_app
from UI.Windows import CreateTK

app = create_app()
TK=CreateTK()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)