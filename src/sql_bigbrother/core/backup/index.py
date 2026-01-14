from flask import Flask, jsonify, request 
from flask_cors import CORS
from resolvers import Resolvers

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['POST'])
async def test():
    req = request.json
    question = req['question']
    schema = req['schema']
    model = req['model']
    is_explain = req['is_explain']
    
    resolver = Resolvers()
    output, execute, columns = resolver.generate_sql(question, schema, model, is_explain)
    return jsonify({
        'output': output,
        'execute': execute,
        'columns': columns
    })

@app.route('/upload', methods=['POST'])
async def upload():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    try:
        schema = file.read().decode('utf-8')
        resolver = Resolvers()
        result = resolver.setup_sql(schema)
        title, recommends = resolver.initialize_chat(schema)

        if result == True:
            return jsonify({
                'title': title,
                'sql_content': schema,
                'recommends': recommends
            })
        else:
            return 'Setup database error', 403
    except Exception as e:
        return str(e), 500

    
if __name__ == '__main__':
    app.run(host='localhost', port=5000)

