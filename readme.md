# `Flask with React` Template

### Starting with Frontend

#### In terminal run the following commands:

1. `npx create-react-app frontend`

1. `cd frontend`

1. Ctrl+P `package.json` add in scripts:

    ```
    "scripts": {
        "start": "concurrently \"npm run backend\" \"npm run frontend\"",
        "backend": "python ../backend/main.py",
        "frontend": "react-scripts start",
        "build": "react-scripts build",
        "test": "react-scripts test",
        "eject": "react-scripts eject"
    },
    ```

1. `npm run build`

### Starting with Backend

1. `mkdir backend`

1. create `backend/main.py` with Flask:

    ```
    import flask
    from flask import *

    app = Flask("__main__")

    @app.route("/")
    def index():
        return render_template("index.html", flask_token="Veio do Flask")


    app.run(debug=True)

    ```
