from flask import Flask, render_template, request, redirect
import psycopg2
import psycopg2.extras

app = Flask(__name__)

DB_HOST = "137.184.120.127"
DB_NAME = "sigcon"
DB_USER = "modulo4"
DB_PASS = "modulo4"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

@app.route('/')
def index():
    cur.execute("SELECT * FROM recaudacion")
    datos = cur.fetchall()
    return render_template('index.html', datos=datos)

@app.route('/agregar', methods=['POST'])
def agregar():
    id_recaudacion = request.form['id_recaudacion']
    id_cuenta = request.form['id_cuenta']
    int_mant_recibo = request.form['int_mant_recibo']
    n_operacion = request.form['n_operacion']
    fecha_operacion = request.form['fecha_operacion']
    moneda= request.form['moneda']
    importe= request.form['importe']
    id_recaudacion_estado = request.form['id_recaudacion_estado']
    id_cuenta_predio= request.form['id_cuenta_predio']
    observacion = request.form['observacion']
    
    cur.execute("INSERT INTO casa (id_recaudacion, id_cuenta, int_mant_recibo, n_operacion, fecha_operacion, moneda, importe, id_recaudacion_estado, id_cuenta_predio, observacion) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (id_recaudacion, id_cuenta, int_mant_recibo, n_operacion, fecha_operacion, moneda, importe, id_recaudacion_estado, id_cuenta_predio, observacion))
    conn.commit()
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)