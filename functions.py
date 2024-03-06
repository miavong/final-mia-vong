import urllib.parse, urllib.request, urllib.error, json

base_url = "https://trefle.io/api/v1/plants/search?token=ipQ-vf8WvpBCOFV9RkmYuhbrhX-QeHkGyZen7bV4nZQ"

# Invoke a call to a Trefle API and returns search data for a plant 
def get_plant_data(plant):
    plant = urllib.parse.quote(plant.replace(' ', '_'))
    url = base_url + "&q=" + plant
    url_str = urllib.request.urlopen(url)
    data = url_str.read()
    plant_data = json.loads(data)
    list_data = plant_data["data"]
    return list_data
#print(get_plant_data("strawberry"))

# Extract relevant data about a specific plant
def extract_plant_data(plant):
    data = get_plant_data(plant)
    extract_data = []

    for plant_type in data:
        plant_info = {
            'common_name': plant_type.get('common_name', 'Data Not Avaliable'),
            'genus': plant_type.get('genus', 'Data Not Avaliable'),
            'scientific_name': plant_type.get('scientific_name', 'Data Not Avaliable'),
            'image_url': plant_type.get('image_url', 'Data Not Avaliable')
        }
        extract_data.append(plant_info)

    return extract_data 

# Handle any errors due to HTTP or connection related exceptions
def get_plant_data_safe(plant):
    try:
        result = get_plant_data(plant=plant)
        return result
    except urllib.error.URLError as error:
        print("Error trying to retrieve data:", error)
