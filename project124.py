from flask import Flask,jsonify,request

app = Flask(__name__)

data = [
    {
        'id':1,
        'Contact':'99876444456',
        'Name':'Raju',
        'done':False
    },
    
    {
        'id':2,
        'Contact':'9876543222',
        'Name':'Rahul',
        'done':False
    }
]

@app.route('/add-data', methods=['POST'])
def add_contact():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'Please provide the data'
        },400)
    
    contact = {
        'id':data[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',''),
        'done':False        
    }   

    data.append(contact)
    
    return jsonify({
        'status':'success',
        'message':'contact added successfully'
    })

@app.route('/get-data')

def get_contact():
    return jsonify({
        'data':data
    })

if(__name__ == '__main__'):
    app.run(debug=True)