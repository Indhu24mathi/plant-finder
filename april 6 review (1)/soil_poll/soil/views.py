from django.shortcuts import render
import numpy as np
import joblib
from tensorflow.keras.models import load_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Crop

@csrf_exempt
def predict_soil(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # Get values
        N = data['N']
        P = data['P']
        K = data['K']
        temp = data['temperature']
        humidity = data['humidity']
        ph = data['ph']

        # Prepare input
        input_data = [[N, P, K, temp, humidity, ph]]
        input_data = scaler.transform(input_data)

        # Predict
        prediction = model.predict(input_data)
        result = labels[np.argmax(prediction)]

        return JsonResponse({
            "prediction": result
        })

@csrf_exempt
def recommend_crops(request):
    """API endpoint to recommend crops based on soil parameters"""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            
            temp = float(data.get('temperature', 0))
            moisture = float(data.get('humidity', 0))
            ph = float(data.get('ph', 0))
            
            # Determine soil type and enforce non-overlapping pH buckets
            soil_type = get_soil_type(ph)

            if soil_type == 'Acidic':
                ph_min, ph_max = 5.0, 6.4
            elif soil_type == 'Neutral':
                ph_min, ph_max = 6.5, 7.4
            else:
                ph_min, ph_max = 7.5, 8.5

            crops = Crop.objects.filter(
                min_ph__gte=ph_min,
                max_ph__lte=ph_max,
                min_ph__lte=ph,
                max_ph__gte=ph,
                min_moisture__lte=moisture,
                max_moisture__gte=moisture,
                min_temperature__lte=temp,
                max_temperature__gte=temp
            ).order_by('-priority')

            if not crops.exists():
                # Fallback: broaden to all matching moisture/temperature in the same bucket
                crops = Crop.objects.filter(
                    min_ph__gte=ph_min,
                    max_ph__lte=ph_max,
                    min_moisture__lte=moisture,
                    max_moisture__gte=moisture,
                    min_temperature__lte=temp,
                    max_temperature__gte=temp
                ).order_by('-priority')

            if not crops.exists():
                # Fallback: general top crops
                crops = Crop.objects.all().order_by('-priority')[:5]
            
            # Return ALL matching crops
            crop_list = []
            for crop in crops:
                crop_list.append({
                    "name": crop.name,
                    "scientific_name": crop.scientific_name,
                    "emoji": crop.emoji,
                    "description": crop.description,
                    "ph_range": f"{crop.min_ph}-{crop.max_ph}",
                    "moisture_range": f"{crop.min_moisture}-{crop.max_moisture}%",
                    "temperature_range": f"{crop.min_temperature}-{crop.max_temperature}°C",
                    "priority": crop.priority
                })
            
            # Create display string: "🌾 Rice, 🥔 Potato, 🍠 Sweet Potato..."
            crops_display = ", ".join([f"{crop['emoji']} {crop['name']}" for crop in crop_list])
            
            if crop_list:
                return JsonResponse({
                    "success": True,
                    "crops": crop_list,
                    "crops_display": crops_display,
                    "count": len(crop_list),
                    "soil_type": get_soil_type(ph),
                    "description": f"Recommended crops for {get_soil_type(ph)} soil"
                })
            else:
                return JsonResponse({
                    "success": False,
                    "crops": [],
                    "crops_display": "🌱 Mixed Crops",
                    "description": "No optimal match found"
                })
        
        except Exception as e:
            return JsonResponse({
                "success": False,
                "error": str(e)
            }, status=400)

def get_soil_type(ph):
    """Determine soil type based on pH value"""
    if ph < 6.5:
        return "Acidic"
    elif ph < 7.5:
        return "Neutral"
    else:
        return "Alkaline"

# Load once (IMPORTANT)
model = load_model("soil/soil_model.h5")
scaler = joblib.load("soil/scaler.pkl")

labels = ["Healthy", "Moderate", "Polluted"]

def dashboard(request):
    return render(request, "dashboard.html")

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def prediction_page(request):
    return render(request, "prediction.html")