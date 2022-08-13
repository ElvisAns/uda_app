from factory import create_app
from routes import urls

#SOC: Seperation Of Concerns

app = create_app('config')
app.register_blueprint(urls)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

