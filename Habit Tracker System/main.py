import requests
from datetime import datetime


TOKEN = "kjznfe56r4g984d5f15687962659uxbde"
USERNAME = "aashish1077"

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graph_endpoint= f"{pixela_endpoint}/{user_parameters['username']}/graphs"

graph_config = {
    "id": "graph2",
    "name": "Walking Traker",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
    "timezone": "Asia/Kolkata"
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers={"X-USER-TOKEN": TOKEN})
# print(response.text)

# Create a pixel endpoint to add data to the graph
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

today = datetime.now()
today_date = today.strftime("%Y%m%d")  # Format date as YYYYMMDD

pixel_data = {
    "date": today_date,  # YYYYMMDD format
    "quantity": input("How many km did u walk today: ")  # Example quantity in km
}
response = requests.post(url=pixel_endpoint, json=pixel_data, headers={"X-USER-TOKEN": TOKEN})
print(response.text)




# To update a pixel, you can use the PUT method
update_pixel_endpoint = f"{pixel_endpoint}/{today_date}"
update_pixel_data = {
    "quantity": "30.0"
}
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_data, headers={"X-USER-TOKEN": TOKEN})
# print(response.text)



# To delete a pixel, you can use the DELETE method
delete_pixel_endpoint = f"{pixel_endpoint}/{today_date}"    
# response = requests.delete(url=delete_pixel_endpoint, headers={"X-USER-TOKEN": TOKEN})