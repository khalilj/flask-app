from app import app

@app.route('/v1/health')
def health():
    return ''

@app.route('/v1/test')
def test():
    return 'this is Salt security'
