import os
from website import create_app

# Setting up your email and password to which people can send their messages. Best to submit them to environment.
USER_MAIL = "YOUR OWN EMAIL ADDRESS"
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
