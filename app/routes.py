from app import app

@app.route('/v1/health')
def index():
    return ''