from flask import Flask, jsonify, render_template
from pomodoro_timer import PomodoroTimer

app = Flask(__name__)

# Crear instancia global del temporizador de 20 minutos (1200 seg)
pomodoro = PomodoroTimer(20 * 60)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start_timer():
    pomodoro.start()
    return jsonify({'status': 'started', 'time_left': pomodoro.time_left})

@app.route('/pause')
def pause_timer():
    pomodoro.pause()
    return jsonify({'status': 'paused', 'time_left': pomodoro.time_left})

@app.route('/reset')
def reset_timer():
    pomodoro.reset()
    return jsonify({'status': 'reset', 'time_left': pomodoro.time_left})

@app.route('/status')
def status():
    return jsonify({'running': pomodoro.running, 'time_left': pomodoro.time_left})

if __name__ == '__main__':
    app.run(debug=True)
