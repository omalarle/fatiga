from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Obtener las respuestas del formulario
    q1 = int(request.form.get('q1', 0))
    q2 = request.form.get('q2', 'no')
    q3 = request.form.get('q3', 'no')
    q4 = request.form.get('q4', 'no')
    q5 = request.form.get('q5', 'no')
    reaction_time = int(request.form.get('reaction_time', 10000))  # Tiempo en ms

    # Lógica básica para determinar si está apto
    score = 0

    if q1 >= 7:  # Si ha dormido 7 horas o más
        score += 20
    if q2 == 'no':  # Si no se ha sentido somnoliento
        score += 20
    if q3 == 'no':  # Si no ha tomado cafeína recientemente
        score += 10
    if q4 == 'no':  # Si no está estresado
        score += 20
    if q5 == 'no':  # Si no tiene problemas de concentración
        score += 10
    if reaction_time <= 500:  # Si su tiempo de reacción es 500 ms o menos
        score += 20
    elif reaction_time <= 1000:  # Si su tiempo de reacción es entre 500 y 1000 ms
        score += 10

    apto = score >= 70  # Define si el usuario está apto

    return render_template('result.html', apto=apto)

if __name__ == "__main__":
    app.run(debug=True)
