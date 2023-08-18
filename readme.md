# `Flask with React` Template

### Creating from 0:

1. `npx create-react-app frontend`

1. `mkdir backend`

1. `cd frontend`

1. `npm run eject` ... `y` to accept

1. Ctrl+P `path.js`

    In path.js `module.exports = {...}` -> Go To Line 57 and add:

    `appBuild: resolveApp('../backend/static/react'),`

1. Ctrl+P `webpack.config.js`
   add the `filename` property
    ```
    Object.assign(
        {},
        {
            ...
            filename: "../../templates/index.html"
        },
        ...
    )
    ```
1. Test the jinja in `public/index.html`. Example:

    ```
        <script>
            window.token = '{{ flask_token }}'
        </script>
    ```

1. Ctrl+P `App.js` add

    `{ window.token }`

1. Ctrl+P `package.json` add before `"scripts"` (in line 60 more or less), add:

    `"homepage": "static/react",`

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
