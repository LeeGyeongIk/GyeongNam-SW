from flask import Flask, render_template, request, url_for
import naverSENS

app = Flask(__name__)

######################## index.html ########################

@app.route('/')
def index():
    return render_template('index.html')

######################## index.html ########################

######################## order.side ########################

@app.route('/order/order')
def order():
    return render_template('/order/order.html')

@app.route('/order/order_done', methods=['POST', 'GET'])
def order_done():
    if request.method == 'POST':
        naverSENS.send_sms("01037225398",request.form['phone_number'],"[알림서비스]",request.form['sms_content'])
    return render_template('/order/order_done.html')

@app.route('/order/deffered_pay_done')
def deffered_pay_done():
    return render_template('/order/deffered_pay_done.html')

######################## order.side ########################

######################## user_side ########################

@app.route('/user/login')
def user_login():
    return render_template('/user/login.html')

@app.route('/user/sign_up')
def user_sign_up():
    return render_template('/user/sign_up.html')

@app.route('/user/user_main')
def user_main():
    return render_template('/user/user_main.html')

@app.route('/user/reservation')
def user_reservation():
    return render_template('/user/reservation.html')

@app.route('/user/user_reservation_state')
def user_reservation_state():
    return render_template('/user/user_reservation_state.html')

@app.route('/user/user_info')
def user_info():
    return render_template('/user/user_info.html')

######################## user_side ########################

######################## store_side ########################

@app.route('/store/login')
def store_login():
    return render_template('store/login.html')

@app.route('/store/sign_up')
def store_sign_up():
    return render_template('store/sign_up.html')

@app.route('/store/menu')
def store_menu():
    return render_template('store/menu.html')

@app.route('/store/store_main')
def store_main():
    return render_template('store/store_main.html')

@app.route('/store/store_registration')
def store_registration():
    return render_template('store/store_registration.html')

@app.route('/store/order_sheet')
def store_order_sheet():
    return render_template('store/order_sheet.html')

@app.route('/store/POS_table')
def store_POS_table():
    return render_template('store/POS_table.html')

@app.route('/store/QRCODE')
def store_QRCODE():
    return render_template('store/QRCODE.html')

@app.route('/store/store_reservation_state')
def store_reservation_state():
    return render_template('store/store_reservation_state.html')

@app.route('/store/store_settings')
def store_settings():
    return render_template('store/store_settings.html')

######################## store_side ########################


app.run(host="0.0.0.0", port="5000", debug=True)