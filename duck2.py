class Instagram:
    def open(self):
        print("Opening Instagram")

class WhatsApp:
    def open(self):
        print("Opening WhatsApp")

def start_app(app):
    app.open()

start_app(Instagram())
start_app(WhatsApp())