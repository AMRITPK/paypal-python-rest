import json

def applicationConfig():
	_config = {
		"IS_APPLICATION_IN_SANDBOX" : "true",
	}

	_jsonSandBox = {
	
		"CLIENT_ID" :"AViCPcsftEkFlWCou9c4Yq3onzvndHtm-OsqMpUp306-WwCl_A63SbSZcNB0uRzhLVbbu_k1a3Vxb4Si",
		"SECRET":"EMJzmmce4g_ScPr2MA7y9_-tU3Q9Z4zLJWu8CAZM5BMti2xYDkdB8HN39k_A6hGCWlT-QbGivm78kSwG",
		"ACCESS_TOKEN_URL":"https://api.sandbox.paypal.com/v1/oauth2/token",
		"CREATE_PAYMENT_URL":"https://api.sandbox.paypal.com/v1/payments/payment",
		"EXECUTE_PAYMENT_URL":"https://api.sandbox.paypal.com/v1/payments/payment/{payment_id}/execute/",
		"GET_PAYMENT_DETAILS":"https://api.sandbox.paypal.com/v1/payments/payment/{payment_id}",
		"CANCEL_URL":"cancelUrl",
		"RETURN_URL":"cancelUrl",
		"BN_CODE":"PP-DemoPortal-EC-JSV4-python-REST"
	}

	_jsonLive = {
		"CLIENT_ID" :"YOUR_CLIENT_ID",
		"SECRET":"YOUR_SECRET_ID",
		"ACCESS_TOKEN_URL":"https://api.paypal.com/v1/oauth2/token",
		"CREATE_PAYMENT_URL":"https://api.paypal.com/v1/payments/payment",
		"EXECUTE_PAYMENT_URL":"https://api.paypal.com/v1/payments/payment/{payment_id}/execute/",
		"GET_PAYMENT_DETAILS":"https://api.paypal.com/v1/payments/payment/{payment_id}",
		"CANCEL_URL":"cancelUrl",
		"RETURN_URL":"cancelUrl",
		"BN_CODE":"PP-DemoPortal-EC-JSV4-python-REST`"
	}

	if _config['IS_APPLICATION_IN_SANDBOX'] == 'true':
		print "T"
		return _jsonSandBox
	else:
		print "F"
		return _jsonLive

def getCreatePaymentPayloadTemplate():
	return "{\r\n  \"intent\": \"sale\",\r\n  \"payer\": {\r\n    \"payment_method\": \"paypal\"\r\n  },\r\n  \"transactions\": [\r\n    {\r\n      \"amount\": {\r\n        \"total\": \"0.00\",\r\n        \"currency\": \"USD\",\r\n        \"details\": {\r\n          \"subtotal\": \"0.00\",\r\n          \"tax\": \"0.00\",\r\n          \"shipping\": \"0.00\",\r\n          \"handling_fee\": \"0.00\",\r\n          \"shipping_discount\": \"0.00\",\r\n          \"insurance\": \"0.00\"\r\n        }\r\n      },\r\n      \"description\": \"This is the payment transaction description.\",\r\n      \"custom\": \"EBAY_EMS_90048630024435\",\r\n      \"invoice_number\": \"48787589663\",\r\n      \"payment_options\": {\r\n        \"allowed_payment_method\": \"INSTANT_FUNDING_SOURCE\"\r\n      },\r\n      \"soft_descriptor\": \"ECHI5786786\",\r\n      \"item_list\": {\r\n        \"items\": [\r\n          {\r\n            \"name\": \"hat\",\r\n            \"description\": \"Brown color hat\",\r\n            \"quantity\": \"5\",\r\n            \"price\": \"3\",\r\n            \"tax\": \"0.01\",\r\n            \"sku\": \"1\",\r\n            \"currency\": \"USD\"\r\n          }\r\n          \r\n        ],\r\n        \"shipping_address\": {\r\n          \"recipient_name\": \"Pam Jones\",\r\n          \"line1\": \"4thFloor\",\r\n          \"line2\": \"unit #34\",\r\n          \"city\": \"San Jose\",\r\n          \"country_code\": \"US\",\r\n          \"postal_code\": \"95131\",\r\n          \"phone\": \"011862212345678\",\r\n          \"state\": \"CA\"\r\n        }\r\n      }\r\n    }\r\n  ],\r\n  \"note_to_payer\": \"Contact us for any questions on your order.\",\r\n  \"redirect_urls\": {\r\n    \"return_url\": \"http://www.yourUrl.com\",\r\n    \"cancel_url\": \"http://www.yourUrl.com\"\r\n  }\r\n}"
	
