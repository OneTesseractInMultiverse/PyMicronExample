from micron import (
    app
)
from flask import (
    jsonify,
    request,
    url_for
)


# --------------------------------------------------------------------------
# GET: /
# --------------------------------------------------------------------------
@app.route('/', methods=['GET'])
def get_root():
    return jsonify(
        {
            "ApiPlatform": "PyMicron is up and running! Good job!",
            "IP Address": request.remote_addr,
            "User Agent": request.headers.get('User-Agent')
        }
    ), 200




