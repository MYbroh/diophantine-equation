from flask import Flask, render_template, request

app = Flask(__name__)

def gcd(p, q):
    if q == 0:
        return p
    else:
        return gcd(q, p % q)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_result', methods=['POST'])
def update_result():
    a = int(request.form['a'])
    b = int(request.form['b'])
    k = int(request.form['k'])

    y = 1
    x = 1
    ab = [a, b]

    result = ab[0]
    for i in range(1, 2):
        result = gcd(result, ab[i])

    if k % result == 0:
        while x:
            if (k - a * x) % b == 0:
                x_result = x
                break
            x += 1

        y1 = (k - a * x_result) // b
        y2 = ((-1) * a * b) // b
        y_result = y1

        if (x_result == 0 or y_result == 0) == True:
            return f"<p>ผลลัพธ์<p><p>พจน์ทั่วไปของ x คือ (n-1)({b}) ; โดย n คือจำนวนเต็ม</p><p>พจน์ทั่วไปของ y คือ (n-1)({y2}) ; โดย n คือจำนวนเต็ม</p>"
        else:
            return f"<p>ผลลัพธ์<p><p>พจน์ทั่วไปของ x คือ {x_result} + (n-1)({b}) ; โดย n คือจำนวนเต็ม</p><p>พจน์ทั่วไปของ y คือ {y_result} + (n-1)({y2}) ; โดย n คือจำนวนเต็ม</p>"
    else:
        return "<p>สมการไดโอแฟนไทล์นี้ไม่มีผลเฉลยเป็นจำนวนเต็ม</p>"


if __name__ == '__main__':
    app.run(debug=True)