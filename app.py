from init import app, api
from Models.Log import LogDetails, logs_schema
from Controllers.LogController import Apii
@app.route('/api/data', methods=['GET'])
def get():
    data = LogDetails.query.all()
    return logs_schema.jsonify(data)

api.add_resource(Apii, '/api')

if __name__=="__main__":
    app.run(debug=True)