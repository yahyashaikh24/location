from flask import request, jsonify
from async_io import asyncio, aiohttp
from flask import Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return "<h1> Sensor </h1>"

@routes.route('/send-location', methods=['POST'])
def receive_location():
    data = request.json
    asyncio.run(forward_location_data(data))
    return jsonify({"status": "Location data received and forwarded"}), 200

# Async function to forward the location data to the remote server
async def forward_location_data(location_data):
    remote_url = 'http://192.168.0.12/location'
    async with aiohttp.ClientSession() as session:
        async with session.post(remote_url, json=location_data) as response:
            if response.status == 200:
                print("Location data successfully forwarded to remote server")
            else:
                print(f"Failed to forward data. Status code: {response.status}")