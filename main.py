from flask import Flask
import time
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.event_handler.api_gateway import ApiGatewayResolver

app = Flask(__name__)
app_resolver = ApiGatewayResolver(app)

@app.route('/')
def hello_world():
    time.sleep(5)  # Simulate delay
    return 'Hello World'

@ApiGatewayResolver.get("/")  # Decorator to create Lambda handler
def lambda_handler(event: dict, context: LambdaContext):
    return app_resolver.resolve(event, context)

if __name__ == '__main__':
    app.run(debug=True)