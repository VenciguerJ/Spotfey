from app import app

@app.route("/")
def main():
    return "<h1>hello world</h1>"