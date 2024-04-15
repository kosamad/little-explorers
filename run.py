# Import OS
import os

# Import app variable
from taskmanager import app

# How and where to run the app
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )