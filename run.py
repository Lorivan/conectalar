from app import create_app

try:
    from app import app as app
except ImportError:
    app = create_app()

if __name__ == '__main__':
    app.run(debug=True)