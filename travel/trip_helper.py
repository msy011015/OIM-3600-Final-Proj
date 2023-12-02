import requests
from pprint import pprint


def location_search(query, category=None):
    """
    Given a query string (keyword of locations), returns up to 10 locations, including the corresponding ID and address.
    Users can also use category ("hotels", "attractions", "restaurants", "geos") to search with more accuracy.
    """
    modified_query = query.replace(" ", "%20")

    # Modified From API
    base_url = "https://api.content.tripadvisor.com/api/v1/location/search?key=5FB479A24F294AB299C43C899A8E22AD"
    url = f"{base_url}&searchQuery={modified_query}&language=en"

    if category:
        url += f"&category={category}"

    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    # print(response.text)

    # get the id and the address for each location result
    if response.status_code == 200:
        data = response.json()["data"]
        locations = []
        for location in data:
            location_info = {"id": location.get("location_id"),
                             "name": location.get("name"),
                             "address": location.get("address_obj", {}).get("address_string")}
            locations.append(location_info)
        return locations
    else:
        print("Error: Unable to search for the location.")
        return None


def get_location_details(location_id):
    """
    Given a location id, return detailed information of the location (hotel, restaurant, or an attraction) , such as description, email, phone, rating, etc.
    """

    url = f"https://api.content.tripadvisor.com/api/v1/location/{location_id}/details?key=5FB479A24F294AB299C43C899A8E22AD&language=en&currency=USD"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    # print(response.text)

    if response.status_code == 200:
        data = response.json()
        info = {
            'description': data.get('description'),
            "address": data.get("address_obj", {}).get("address_string"),
            'email': data.get('email'),
            'phone': data.get('phone'),
            'website': data.get('website'),
            'ranking_string': data.get('ranking_data', {}).get('ranking_string'),
            'rating': data.get('rating'),
            'weekday_text': data.get('hours', {}).get('weekday_text'),
            'category_name': data.get('category', {}).get('localized_name'),
            'subcategory_name': [sub.get('localized_name') for sub in data.get('subcategory', [])],
            'awards': data.get('awards', []),
            'explore': data.get('web_url'),
            'lat': data.get('latitude'),
            'long': data.get('longitude'),
            'name': data.get('name')
        }
        return info
    else:
        print("Error: Unable to search for the detail info.")
        return None


def get_location_reviews(location_id):
    """
    Given a location id, return up to 5 of the most recent reviews for a specific location.
    """
    url = f"https://api.content.tripadvisor.com/api/v1/location/{location_id}/reviews?key=5FB479A24F294AB299C43C899A8E22AD&language=en"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    # print(response.text)

    if response.status_code == 200:
        data = response.json()["data"]
        reviews = []
        for review in data:
            review_info = {'ratings': review.get('rating'),
                           'review_title': review.get('title'),
                           'review_text': review.get('text', '').replace('\n', ' '),
                           'trip_type': review.get('trip_type'),
                           'travel_date': review.get('travel_date')}
            reviews.append(review_info)
        return reviews
    else:
        print("Error: Unable to search for the review.")
        return None


def get_photos(location_id):
    """Given a location id, return up to 5 high-quality photos for a specific location."""
    url = f"https://api.content.tripadvisor.com/api/v1/location/{location_id}/photos?language=en&key=5FB479A24F294AB299C43C899A8E22AD"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()["data"]
        photos = []
        for photo in data:
            photo_url = photo['images']['medium']['url']
            photos.append(photo_url)
        return photos
    else:
        print("Error: Unable to search for the review.")
        return None


def get_neardy_location(latitude, longtitude, category=None):
    """
    Return up to 10 locations found near the given latitude/longtitude.
    Users can use category ("hotels", "attractions", "restaurants", "geos") to search with more accuracy.
    """
    url = f"https://api.content.tripadvisor.com/api/v1/location/nearby_search?latLong={latitude}%2C{longtitude}&key=5FB479A24F294AB299C43C899A8E22AD&language=en"

    if category:
        url += f"&category={category}"

    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()["data"]
        nearby = []
        for item in data:
            nearby_info = {"id": item.get("location_id"),
                           "name": item.get("name"), "address": item.get("address_obj", {}).get("address_string")}
            nearby.append(nearby_info)
        return nearby
    else:
        print("Error: Unable to search for the location.")
        return None


def combined_location_info(location_id, category=None):
    """
    Given a location ID, return detailed information, reviews, photos, and nearby locations for that specific location.
    """
    # Combined all the info for a given location id
    details = get_location_details(location_id)

    if not details:
        return "No details found for the given location ID."

    # Get up to 5 recent reviews for the location
    reviews = get_location_reviews(location_id)

    # Get up to 5 photos for the location
    photos = get_photos(location_id)

    # Get up to 10 nearby locations
    if details.get('lat') and details.get('long'):
        nearby_locations = get_neardy_location(
            details['lat'], details['long'], category)
    else:
        nearby_locations = []

    # Combine all the information
    combined_info = {
        'location_id': location_id,
        'name': details.get('name'),
        'address': details.get('address'),
        'details': details,
        'reviews': reviews,
        'photos': photos,
        'nearby_locations': nearby_locations
    }

    return combined_info


def main():
    query = "queenstown"
    location1 = location_search(query)
    # pprint(location1)
    location_id = 197985
    location_id2 = 255122
    latitude = -45.03106
    longitude = 168.66235
    # pprint(get_location_details(location_id))
    # pprint(get_location_reviews(location_id))
    # pprint(get_photos(location_id))
    # pprint(get_neardy_location(latitude, longitude, "geos"))
    pprint(combined_location_info(location_id2))


if __name__ == '__main__':
    main()
