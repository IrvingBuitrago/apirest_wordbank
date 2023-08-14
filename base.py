from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)

datos = [
    {"anio": 1980, "vacunados": 0},
    {"anio": 1981, "vacunados": 0},
    {"anio": 1982, "vacunados": 9},
    {"anio": 1983, "vacunados": 27},
    {"anio": 1984, "vacunados": 44},
    {"anio": 1985, "vacunados": 49},
    {"anio": 1986, "vacunados": 51},
    {"anio": 1987, "vacunados": 67},
    {"anio": 1988, "vacunados": 77},
    {"anio": 1989, "vacunados": 83},
    {"anio": 1990, "vacunados": 85},
    {"anio": 1991, "vacunados": 83},
    {"anio": 1992, "vacunados": 81},
    {"anio": 1993, "vacunados": 78},
    {"anio": 1994, "vacunados": 75},
    {"anio": 1995, "vacunados": 72},
    {"anio": 1996, "vacunados": 76},
    {"anio": 1997, "vacunados": 79},
    {"anio": 1998, "vacunados": 80},
    {"anio": 1999, "vacunados": 80},
    {"anio": 2000, "vacunados": 78},
    {"anio": 2001, "vacunados": 81},
    {"anio": 2002, "vacunados": 82},
    {"anio": 2003, "vacunados": 87},
    {"anio": 2004, "vacunados": 92},
    {"anio": 2005, "vacunados": 92},
    {"anio": 2006, "vacunados": 92},
    {"anio": 2007, "vacunados": 92},
    {"anio": 2008, "vacunados": 90},
    {"anio": 2009, "vacunados": 89},
    {"anio": 2010, "vacunados": 87},
    {"anio": 2011, "vacunados": 86},
    {"anio": 2012, "vacunados": 84},
    {"anio": 2013, "vacunados": 83},
    {"anio": 2014, "vacunados": 81},
    {"anio": 2015, "vacunados": 80},
    {"anio": 2016, "vacunados": 80},
    {"anio": 2017, "vacunados": 78},
    {"anio": 2018, "vacunados": 77},
    {"anio": 2019, "vacunados": 75},
    {"anio": 2020, "vacunados": 72},
    {"anio": 2021, "vacunados": 57},
]

@app.route('/', methods=['GET'])
def index():
    return redirect('/vacunados')

@app.route('/vacunados', methods=['GET'])
def vacunados():
    return jsonify(datos)

@app.route('/vacunados/<int:anio>', methods=['GET'])
def vacunados_anio(anio):
    vacunados_anio = next((item for item in datos if item["anio"] == anio), None)
    if vacunados_anio:
        return jsonify(vacunados_anio)
    else:
        return jsonify({"error": f"No se encontraron datos para el anio {anio}"})

if __name__ == '__main__':
    app.run(debug=True)

