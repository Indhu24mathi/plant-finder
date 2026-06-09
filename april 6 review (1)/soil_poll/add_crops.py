import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soil_poll.settings')
django.setup()

from soil.models import Crop

# Clear existing crops
Crop.objects.all().delete()

# Add crop data with optimal conditions
crops_data = [
    # ===== ACIDIC SOIL (pH 5.0-6.4) =====
    # Rice, Potato, Sweet Potato, Ragi, Sweet Corn, Green Gram, Cowpea, Sunhemp
    {
        "name": "Rice",
        "scientific_name": "Oryza sativa",
        "emoji": "🌾",
        "min_ph": 5.0,
        "max_ph": 6.4,
        "min_moisture": 50,
        "max_moisture": 85,
        "min_temperature": 20,
        "max_temperature": 35,
        "description": "Excellent for acidic soil conditions",
        "priority": 5
    },
    {
        "name": "Potato",
        "scientific_name": "Solanum tuberosum",
        "emoji": "🥔",
        "min_ph": 5.0,
        "max_ph": 6.4,
        "min_moisture": 40,
        "max_moisture": 70,
        "min_temperature": 15,
        "max_temperature": 25,
        "description": "Potato cultivation in acidic soil",
        "priority": 5
    },
    {
        "name": "Sweet Potato",
        "scientific_name": "Ipomoea batatas",
        "emoji": "🍠",
        "min_ph": 5.0,
        "max_ph": 6.4,
        "min_moisture": 35,
        "max_moisture": 65,
        "min_temperature": 20,
        "max_temperature": 30,
        "description": "Sweet potato thrives in acidic soil",
        "priority": 5
    },
    {
        "name": "Ragi",
        "scientific_name": "Eleusine coracana",
        "emoji": "🌾",
        "min_ph": 5.0,
        "max_ph": 6.4,
        "min_moisture": 30,
        "max_moisture": 60,
        "min_temperature": 20,
        "max_temperature": 32,
        "description": "Finger millet for acidic soils",
        "priority": 4
    },
    {
        "name": "Sweet Corn",
        "scientific_name": "Zea mays",
        "emoji": "🌽",
        "min_ph": 5.0,
        "max_ph": 6.4,
        "min_moisture": 45,
        "max_moisture": 70,
        "min_temperature": 20,
        "max_temperature": 32,
        "description": "Sweet corn grows well in acidic conditions",
        "priority": 4
    },
    {
        "name": "Green Gram",
        "scientific_name": "Vigna radiata",
        "emoji": "🫘",
        "min_ph": 5.0,
        "max_ph": 6.4,
        "min_moisture": 30,
        "max_moisture": 55,
        "min_temperature": 20,
        "max_temperature": 30,
        "description": "Mung bean for acidic soil",
        "priority": 4
    },
    {
        "name": "Cowpea",
        "scientific_name": "Vigna unguiculata",
        "emoji": "🫘",
        "min_ph": 5.0,
        "max_ph": 6.4,
        "min_moisture": 25,
        "max_moisture": 50,
        "min_temperature": 20,
        "max_temperature": 32,
        "description": "Legume crop for acidic soils",
        "priority": 4
    },
    {
        "name": "Sunhemp",
        "scientific_name": "Crotalaria juncea",
        "emoji": "🌱",
        "min_ph": 5.0,
        "max_ph": 6.4,
        "min_moisture": 30,
        "max_moisture": 60,
        "min_temperature": 20,
        "max_temperature": 32,
        "description": "Green manure crop for acidic soil",
        "priority": 3
    },

    # ===== NEUTRAL SOIL (pH 6.5-7.4) =====
    # Wheat, Maize, Sugarcane, Banana, Tomato, Onion, Cabbage, Carrot
    {
        "name": "Wheat",
        "scientific_name": "Triticum aestivum",
        "emoji": "🌾",
        "min_ph": 6.5,
        "max_ph": 7.4,
        "min_moisture": 40,
        "max_moisture": 60,
        "min_temperature": 18,
        "max_temperature": 28,
        "description": "Excellent for wheat cultivation",
        "priority": 5
    },
    {
        "name": "Maize",
        "scientific_name": "Zea mays",
        "emoji": "🌽",
        "min_ph": 6.5,
        "max_ph": 7.4,
        "min_moisture": 50,
        "max_moisture": 75,
        "min_temperature": 22,
        "max_temperature": 35,
        "description": "Perfect for corn cultivation",
        "priority": 5
    },
    {
        "name": "Sugarcane",
        "scientific_name": "Saccharum officinarum",
        "emoji": "🩸",
        "min_ph": 6.5,
        "max_ph": 7.4,
        "min_moisture": 60,
        "max_moisture": 85,
        "min_temperature": 20,
        "max_temperature": 30,
        "description": "Ideal for sugarcane growth",
        "priority": 5
    },
    {
        "name": "Banana",
        "scientific_name": "Musa",
        "emoji": "🍌",
        "min_ph": 6.5,
        "max_ph": 7.4,
        "min_moisture": 70,
        "max_moisture": 90,
        "min_temperature": 18,
        "max_temperature": 32,
        "description": "Fruit crop for neutral soil",
        "priority": 4
    },
    {
        "name": "Tomato",
        "scientific_name": "Solanum lycopersicum",
        "emoji": "🍅",
        "min_ph": 6.5,
        "max_ph": 7.4,
        "min_moisture": 30,
        "max_moisture": 55,
        "min_temperature": 20,
        "max_temperature": 32,
        "description": "Ideal for tomato growth",
        "priority": 5
    },
    {
        "name": "Onion",
        "scientific_name": "Allium cepa",
        "emoji": "🧅",
        "min_ph": 6.5,
        "max_ph": 7.4,
        "min_moisture": 35,
        "max_moisture": 55,
        "min_temperature": 15,
        "max_temperature": 25,
        "description": "Great for bulb crops",
        "priority": 4
    },
    {
        "name": "Cabbage",
        "scientific_name": "Brassica oleracea",
        "emoji": "🥬",
        "min_ph": 6.5,
        "max_ph": 7.4,
        "min_moisture": 55,
        "max_moisture": 75,
        "min_temperature": 15,
        "max_temperature": 25,
        "description": "Perfect for leafy vegetables",
        "priority": 4
    },
    {
        "name": "Carrot",
        "scientific_name": "Daucus carota",
        "emoji": "🥕",
        "min_ph": 6.5,
        "max_ph": 7.4,
        "min_moisture": 40,
        "max_moisture": 65,
        "min_temperature": 15,
        "max_temperature": 25,
        "description": "Perfect for root vegetable growth",
        "priority": 4
    },

    # ===== BASIC/ALKALINE SOIL (pH 7.5-8.5) =====
    # Barley, Cotton, Mustard, Sorghum, Pearl Millet (Bajra), Beetroot, Spinach
    {
        "name": "Barley",
        "scientific_name": "Hordeum vulgare",
        "emoji": "🌾",
        "min_ph": 7.5,
        "max_ph": 8.5,
        "min_moisture": 35,
        "max_moisture": 55,
        "min_temperature": 15,
        "max_temperature": 25,
        "description": "Cereal crop for alkaline soil",
        "priority": 5
    },
    {
        "name": "Cotton",
        "scientific_name": "Gossypium",
        "emoji": "🤎",
        "min_ph": 7.5,
        "max_ph": 8.5,
        "min_moisture": 30,
        "max_moisture": 50,
        "min_temperature": 22,
        "max_temperature": 35,
        "description": "Fiber crop for alkaline conditions",
        "priority": 5
    },
    {
        "name": "Mustard",
        "scientific_name": "Brassica juncea",
        "emoji": "🌾",
        "min_ph": 7.5,
        "max_ph": 8.5,
        "min_moisture": 30,
        "max_moisture": 50,
        "min_temperature": 15,
        "max_temperature": 25,
        "description": "Oil seed crop for alkaline soil",
        "priority": 5
    },
    {
        "name": "Sorghum",
        "scientific_name": "Sorghum bicolor",
        "emoji": "🌾",
        "min_ph": 7.5,
        "max_ph": 8.5,
        "min_moisture": 25,
        "max_moisture": 50,
        "min_temperature": 20,
        "max_temperature": 35,
        "description": "Drought resistant cereal crop",
        "priority": 4
    },
    {
        "name": "Pearl Millet",
        "scientific_name": "Pennisetum glaucum",
        "emoji": "🌾",
        "min_ph": 7.5,
        "max_ph": 8.5,
        "min_moisture": 20,
        "max_moisture": 45,
        "min_temperature": 20,
        "max_temperature": 35,
        "description": "Bajra - millet for alkaline soil",
        "priority": 4
    },
    {
        "name": "Beetroot",
        "scientific_name": "Beta vulgaris",
        "emoji": "🔴",
        "min_ph": 7.5,
        "max_ph": 8.5,
        "min_moisture": 45,
        "max_moisture": 65,
        "min_temperature": 15,
        "max_temperature": 25,
        "description": "Root vegetable for alkaline soil",
        "priority": 4
    },
    {
        "name": "Spinach",
        "scientific_name": "Spinacia oleracea",
        "emoji": "🥬",
        "min_ph": 7.5,
        "max_ph": 8.5,
        "min_moisture": 50,
        "max_moisture": 70,
        "min_temperature": 10,
        "max_temperature": 25,
        "description": "Leafy green for alkaline conditions",
        "priority": 4
    }
]

# Add crops to database
for crop_data in crops_data:
    Crop.objects.create(**crop_data)

print(f"✅ Successfully added {len(crops_data)} crops to the database!")
print("\nCrops added:")
for crop in Crop.objects.all():
    print(f"  {crop.emoji} {crop.name} (Priority: {crop.priority})")
