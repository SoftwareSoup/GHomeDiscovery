# Get Off My GHome Webhook
# Pg 26
from http.server import BaseHTTPRequestHandler, HTTPServer
from network_devices import NetworkList
import requests, json, os

# Create Listening Server
class GHomeRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(bytes("Hello World", "utf-8"))
        return
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Log results, mainly for debugging
        print("\n---------- Request Start --------->\n")
        print(self.path)

        # Get body length
        request_headers = self.headers
        content_length = request_headers.__getitem__('content-length')
        length = int(content_length) if content_length else 0

        try:
            # Create Python Object with JSON recieved from header
            request = self.rfile.read(length).decode("utf-8")
            jsonRequest = json.loads(request)
            queryText = jsonRequest['queryResult']['queryText']
            
            # Create return JSON
            jsonResponse = [{'fulfillmentText': list_all_devices(), 'fulfillmentMessage': [{'text': {'text':[list_all_devices()]}}]}]

            if "new" in queryText:
                jsonResponse[0]['fulfillmentText'] = new_devices()
                jsonResponse[0]['fulfillmentMessage'][0]['text']['text'][0] = new_devices()

            print(request_headers.as_string())
            print(request)
            print(jsonResponse[0]['fulfillmentText'])
            print(json.dumps(jsonResponse).encode('utf-8'))
            self.wfile.write(bytes(json.dumps(jsonResponse), "utf-8"))
            #self.wfile.write(bytes("Hello World", "utf-8"))
        except ValueError:
            print("VALUE EXCEPTION FOUND")
        print("<---------- Request End -------------\n")

        return

def run():
    print("Starting Server...")

    # Server Settings
    server_address = ('localhost', 80)
    httpd = HTTPServer(server_address, GHomeRequestHandler)
    print('Running Server...')
    httpd.serve_forever()



