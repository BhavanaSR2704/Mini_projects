from flask import Flask, render_template, request, jsonify
from student import (students, linear_search, binary_search,
                     bubble_sort, quick_sort, merge_sort)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data    = request.get_json()
    query   = data.get('query', '').strip().lower()
    method  = data.get('method', 'linear')

    if method == 'binary':
        sorted_students = quick_sort(students[:], key='name')
        results = binary_search(sorted_students, query)
    else:
        results = linear_search(students, query)

    return jsonify({'results': results, 'count': len(results)})

@app.route('/sort', methods=['POST'])
def sort():
    data      = request.get_json()
    algorithm = data.get('algorithm', 'bubble')
    key       = data.get('key', 'name')
    reverse   = data.get('reverse', False)

    if algorithm == 'bubble':
        result = bubble_sort(students[:], key=key, reverse=reverse)
    elif algorithm == 'quick':
        result = quick_sort(students[:], key=key, reverse=reverse)
    else:
        result = merge_sort(students[:], key=key, reverse=reverse)

    return jsonify({'results': result, 'count': len(result), 'algorithm': algorithm})

if __name__ == '__main__':
    app.run(debug=True)