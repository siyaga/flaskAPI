from flask import Flask, jsonify,request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData, functionName):
    if(functionName == "add" or functionName == "subtract" or functionName == "multiply"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200
    elif ( functionName == "division"):
        if"x" not in postedData or "y" not in postedData:
            return 301
        elif int ( postedData["y"]) ==0:
            return 302
        else:
            return 200
class Add(Resource):
    def post(self):
        # if I am here, then the resouce Add was requested using the method POST

        #Stap 1: Get posted data:
        postedData = request.get_json()

        #Stap 1b: verify validaty of posted data
        status_code = checkPostedData(postedData, "add")
        if(status_code != 200):
            retJson= {
                "Message": "An error happend",
                "Status Code": status_code
            }
            return jsonify(retJson)
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        # Step 2: Add the posted data
        ret = x + y
        retMap = {
            'Message' :ret,
            'Status code': 200
        }
        return jsonify(retMap)

class Subtract(Resource):
     def post(self):
        # if I am here, then the resouce Substract was requested using the method POST

        #Stap 1: Get posted data:
        postedData = request.get_json()

        #Stap 1b: verify validaty of posted data
        status_code = checkPostedData(postedData, "subtract")
        if(status_code != 200):
            retJson= {
                "Message": "An error happend",
                "Status Code": status_code
            }
            return jsonify(retJson)
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        # Step 2: Substract the posted data
        ret = x - y
        retMap = {
            'Message' :ret,
            'Status code': 200
        }
        return jsonify(retMap)


class Multiply(Resource):       
      def post(self):
        # if I am here, then the resouce Multiply was requested using the method POST

        #Stap 1: Get posted data:
        postedData = request.get_json()

        #Stap 1b: verify validaty of posted data
        status_code = checkPostedData(postedData, "multiply")
        if(status_code != 200):
            retJson= {
                "Message": "An error happend",
                "Status Code": status_code
            }
            return jsonify(retJson)
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        # Step 2: Multiply the posted data
        ret = x * y
        retMap = {
            'Message' :ret,
            'Status code': 200
        }
        return jsonify(retMap)

class Divide(Resource):       
      def post(self):
        # if I am here, then the resouce Divide was requested using the method POST

        #Stap 1: Get posted data:
        postedData = request.get_json()

        #Stap 1b: verify validaty of posted data
        status_code = checkPostedData(postedData, "division")
        if(status_code != 200):
            retJson= {
                "Message": "An error happend",
                "Status Code": status_code
            }
            return jsonify(retJson)
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        # Step 2: Divide the posted data
        ret = (x*1.0) / y
        retMap = {
            'Message' :ret,
            'Status code': 200
        }
        return jsonify(retMap)        


api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/division")

# 127.0.0.1:5000/
@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/hithere')
def hi_there_everyone():
    return "I just hit /hithere"

@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():
    # get x,y from the posted data
    dataDict = request.get_json()
    x = dataDict["x"]
    y = dataDict["y"]

    z = x + y
    retJSON = {
        "z":z
    }

    return jsonify(retJSON), 200

    # add z =x+y

    # Prepare a JSON, "Z":Z

    # return jsonify(map_prepared)

@app.route('/bye')
def bye():
    # Prepare a response for the request that came to /bye
    c = 2*534
    s = str(c)

    # c = 1/0
    retJson = {
        'Name' :'Elfarouk',
        'Age' : '22',
        "phones" : [
            {
                "phoneName" : "Iphone8",
                "phoneNumber" : "11111"
            },
            {
                "phoneName" : "Iphone8",
                "phoneNumber" : "11121"
            }
        ]
    }
    return jsonify(retJson)  ,404


if __name__ == '__main__':
    app.run(debug=True)
