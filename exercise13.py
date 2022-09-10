from flask import Flask, request
import json




app = Flask(__name__)
@app.route('/sum')
def sum():
    is_prime = "false"
    args = request.args
    number = int(args.get("number"))

    all_prime_numbers = [2,3]
    for i in range(2,number+1):
        has_mod = 0
        for j in all_prime_numbers: 
            if (i % j == 0):
                has_mod = 1
        if (has_mod != 1):
            all_prime_numbers.append(i)
            has_mod = 0

    if  (number in all_prime_numbers):
       is_prime = True 
    else:
       is_prime = False

    response = {
        "number" : number,
        "is_prime" : is_prime
    }

    json_data = json.dumps(response, default=lambda o: o.__dict__, indent=4)

    # return response
    return json_data

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
