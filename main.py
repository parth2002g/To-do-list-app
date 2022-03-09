import creator
from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/item/new', methods = ['POST'])
def add_item():
   #Get item from the POST body
   get_data = request.get_json()
   item = get_data['item']
   
   #Add item to the list
   response_data = creator.add_to_list(item)

   #Return error if item not added
   if response_data is None:
      response = Response("{'error': 'Item not added - '}"  + item, status=400 , mimetype='application/json')
      return response
   
   #Return response
   response = Response(json.dumps(response_data), mimetype='application/json')
   
   return response

@app.route('/items/all')
def get_all_items():
   # Get items from the creator
   response_data = creator.get_all_items()
   #Return response
   response = Response(json.dumps(response_data), mimetype='application/json')
   return response

@app.route('/item/status', methods=['GET'])
def get_item():
   #Get parameter from the URL
   item_name = request.args.get('name')
   
   # Get items from the creator
   status = creator.get_item(item_name)
   
   #Return 404 if item not found
   if status is None:
      response = Response("{'error': 'Item Not Found - '}"  + item_name, status=404 , mimetype='application/json')
      return response

   #Return status
   response_data = {
      'status': status
   }

   response = Response(json.dumps(response_data), status=200, mimetype='application/json')
   return response

@app.route('/item/update', methods = ['PUT'])
def update_status():
   #Get item from the POST body
   get_data = request.get_json()
   item = get_data['item']
   status = get_data['status']
   
   #Update item in the list
   response_data = creator.update_status(item, status)
   if response_data is None:
      response = Response("{'error': 'Error updating item - '" + item + ", " + status   +  "}", status=400 , mimetype='application/json')
      return response
   
   #Return response
   response = Response(json.dumps(response_data), mimetype='application/json')
   
   return response

@app.route('/item/remove', methods = ['DELETE'])
def delete_item():
   #Get item from the POST body
   get_data = request.get_json()
   item = get_data['item']
   
   #Delete item from the list
   response_data = creator.delete_item(item)
   if response_data is None:
      response = Response("{'error': 'Error deleting item - '" + item +  "}", status=400 , mimetype='application/json')
      return response
   
   #Return response
   response = Response(json.dumps(response_data), mimetype='application/json')
   
   return response

app.run(debug = True)