from . import app

@app.route('/login')
def login():
    return 'hello login!'

@app.route('/logout')
def logout():
    return 'hello logout!'