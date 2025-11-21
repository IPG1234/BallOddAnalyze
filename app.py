from Base import create_app
# import UI.Windows as BW

app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
    # BW.CreateTK()