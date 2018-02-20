

from flask import Flask , request, send_from_directory
app = Flask(__name__ , static_url_path='')

import requests
import json
import requests
import base64
import uuid

import config
configuration = config.applicationConfig()
createPaymentPayloadTemplate = config.getCreatePaymentPayloadTemplate()


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

@app.route("/")
def root():
	return app.send_static_file('index.html')

def getAccessToken(clientId, secret):
	try:
		url = configuration['ACCESS_TOKEN_URL']
		token = configuration['CLIENT_ID']+":"+configuration['SECRET']
		encoded = base64.b64encode(token)
		payload = "grant_type=client_credentials&Content-Type=application%2Fx-www-form-urlencoded&response_type=token&return_authn_schemes=true"
		headers = {
			'authorization': "Basic "+encoded,
			'accept': "application/json",
			'accept-language': "en_US",
			'cache-control': "no-cache",
			'content-type': "application/x-www-form-urlencoded",
			'PayPal-Partner-Attribution-Id' : configuration['BN_CODE']
			}
		response = requests.request("POST", url, data=payload, headers=headers)
		resdata=json.loads(response.text)
		return resdata['access_token']
	except Exception as err:
		print err
		return "error"
	
@app.route("/CreatePayment",methods=['POST','OPTIONS']) 
def createPayment():
	try:
		
		postData = request.get_json()
		accessToken = getAccessToken(configuration['CLIENT_ID'], configuration['SECRET']);
		url = configuration['CREATE_PAYMENT_URL']
		stringPayload = createPaymentPayloadTemplate
		jsonPayload=json.loads(stringPayload)
		jsonPayload['intent']='sale';
		jsonPayload['payer']["payment_method"]="paypal"
		jsonPayload['note_to_payer']="Contact us for any questions on your order"
		jsonPayload['redirect_urls']["return_url"]= request.url_root+configuration["RETURN_URL"]
		jsonPayload['redirect_urls']["cancel_url"]= request.url_root+configuration["CANCEL_URL"]
		jsonPayload['transactions'][0]["amount"]["total"]=postData["total"]
		jsonPayload['transactions'][0]["amount"]["currency"]=postData["currency"]
		jsonPayload['transactions'][0]["amount"]["details"]["subtotal"]=postData["subtotal"]
		jsonPayload['transactions'][0]["amount"]["details"]["shipping_discount"]=postData["shipping_discount"]
		jsonPayload['transactions'][0]["amount"]["details"]["insurance"]=postData["insurance"]
		jsonPayload['transactions'][0]["amount"]["details"]["shipping"]=postData["shipping"]
		jsonPayload['transactions'][0]["amount"]["details"]["tax"]=postData["tax"]
		jsonPayload['transactions'][0]["amount"]["details"]["handling_fee"]=postData["handling_fee"]
		jsonPayload['transactions'][0]["item_list"]["items"][0]["price"]=postData["price"]
		jsonPayload['transactions'][0]["item_list"]["items"][0]["quantity"]=postData["quantity"]
		jsonPayload['transactions'][0]["item_list"]["items"][0]["description"]=postData["description"]
		jsonPayload['transactions'][0]["item_list"]["items"][0]["price"]=postData["price"]
		jsonPayload['transactions'][0]["description"]=postData["description"]
		jsonPayload['transactions'][0]["invoice_number"] = uuid.uuid4().hex
		jsonPayload['transactions'][0]["custom"] = 'some custom text'

		if(postData["customFlag"]=="true"):
			jsonPayload['transactions'][0]["item_list"]["shipping_address"]["recipient_name"] = postData["recipient_name"]
			jsonPayload['transactions'][0]["item_list"]["shipping_address"]["line1"] = postData["line1"]
			jsonPayload['transactions'][0]["item_list"]["shipping_address"]["line2"] = postData["line2"]
			jsonPayload['transactions'][0]["item_list"]["shipping_address"]["city"] = postData["city"]
			jsonPayload['transactions'][0]["item_list"]["shipping_address"]["state"] = postData["state"]
			jsonPayload['transactions'][0]["item_list"]["shipping_address"]["phone"] = postData["phone"]
			jsonPayload['transactions'][0]["item_list"]["shipping_address"]["postal_code"] = postData["postal_code"]
			jsonPayload['transactions'][0]["item_list"]["shipping_address"]["country_code"] = postData["country_code"]
		
		headers = {
			'content-type': "application/json",
			'authorization': "Bearer "+accessToken,
			'cache-control': "no-cache",
			'PayPal-Partner-Attribution-Id' : configuration['BN_CODE']
			}
		response = requests.request("POST", url, data=json.dumps(jsonPayload), headers=headers)
		return response.text
	except Exception as err:
		print err
		return "error"


@app.route("/ExecutePayments",methods=['POST','OPTIONS']) 
def executePayment():
	try:
		
		postData = request.get_json()
		paymentId = postData['paymentID']
		payerId = postData['payerID']
		accessToken =  getAccessToken(configuration['CLIENT_ID'], configuration['SECRET']);
		url = configuration['EXECUTE_PAYMENT_URL']
		url = url.replace('{payment_id}', paymentId);
		
		data = {
			"payer_id" : payerId
		}
		

		headers = {
			'content-type': "application/json",
			'authorization': "Bearer "+accessToken,
			'cache-control': "no-cache",
			'PayPal-Partner-Attribution-Id' : configuration['BN_CODE']
			}
		response = requests.request("POST", url, data=json.dumps(data), headers=headers)
		return response.text
	except Exception as err:
		print err
		return "error"

@app.route("/successPayment", methods=['GET','OPTIONS']) 
def showSuccessPage():
	query_string = request.query_string 
	return app.send_static_file('success.html')

@app.route("/cancelUrl", methods=['GET','OPTIONS']) 
def showCancelPage():
	return app.send_static_file('cancel.html')

@app.route("/successPayment", methods=['POST','OPTIONS']) 
def showSuccessPageData():
	try:
		query_string = request.query_string 
		token = request.args.get('token')
		payerId = request.args.get('payerID')
		accessToken =  getAccessToken(configuration['CLIENT_ID'], configuration['SECRET']);
		url = configuration['GET_PAYMENT_DETAILS']
		url = url.replace('{payment_id}', token);
		headers = {
			'content-type': "application/json",
			'authorization': "Bearer "+accessToken,
			'cache-control': "no-cache",
			'PayPal-Partner-Attribution-Id' : configuration['BN_CODE']
			}
		response = requests.request("GET", url, headers=headers)
		return response.text
	except Exception as err:
		return "error"



if __name__ == '__main__':
   app.run(debug = True)