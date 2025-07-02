from flask import Flask, jsonify, request
import sys
import typing as t

app = Flask(__name__)
modname = getattr(app, "__module__", t.cast(object, app).__class__.__module__)
mod = sys.modules.get(modname)
print(mod)
print(getattr(mod, '__file__', None))
print(open("/proc/self/cgroup").read())
itemList = {"1":"Item 1", "2":"Item 2", "3":"Item 3"}

@app.get('/')
def home():
    return "Internal server"

@app.get('/shopCart')
def get_item_list():
    itmid = request.args.get("itmid","")
    if itmid and itmid in itemList:
        return itemList[itmid]
    return jsonify(itemList)

@app.put('/shopCart/<int:itmid>')
def add_item_to_cart(itmid):
    try : 
        itmnbr = request.json['itmnbr']
        itemList[str(itmid)] = itmnbr
        return 'Item added', 200
    except:
        return "Invalid request", 400
    
@app.delete('/shopCart/<int:itmid>')
def remove_item_from_cart(itmid):
    global itemList
    if itmid in itemList:
        del itemList[itmid]
        return 'Item deleted', 200
    return 'Item doesn\'t exist', 200
    

if __name__ == '__main__':
    app.run(debug=True)
