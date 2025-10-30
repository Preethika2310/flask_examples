import asyncio
from flask import Blueprint,request,jsonify
from ..services.weather_agent import get_weather_with_agent

weather_bp=Blueprint('weather',__name__)

#Async func that wraps your agent call
async def get_weather_agent_output(city):
    print("Inside get_weather_agent_output")
    #call the weather agent service
    output=await get_weather_with_agent(city)
    return output

@weather_bp.route('/', methods=['POST'])
def get_weather():
    print("Inside weather_agent")
    data = request.get_json()
    city = data.get('city')
    if not city:
        return jsonify({"error": "City is required"}), 400
    try:
        result = asyncio.run(get_weather_agent_output(city))
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500