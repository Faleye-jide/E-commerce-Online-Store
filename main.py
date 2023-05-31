import os
from dotenv import load_dotenv
import json, base64
from requests import post, get
import csv


with open('keys.json', 'rb') as out_file:
    keys = json.load(out_file)
    

client_id, client_secret = keys.get('CLIENT_ID'), keys.get('CLIENT_SECRET')

def get_token(client_id, client_secret):
    auth_string = client_id + ':' + client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        "authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {'grant_type': "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result['access_token']
    
    return token

def get_auth_header(token):
    return {'Authorization': "Bearer " + token}


def search_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f'?q={artist_name}&type=artist&limit=1'
    query_url = url + query
    
    
    response = get(query_url, headers=headers)
    json_result = json.loads(response.content)['artists']['items']
    if len(json_result) == 0:
        print("no artist with this exists")
        return None
    return json_result[0]

def get_songs_by_artist(token, artist_id, country):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country={country}"
    
    headers = get_auth_header(token)
    response = get(url, headers=headers)
    json_result = json.loads(response.content)['tracks']
    return json_result
    
token = get_token(client_id, client_secret)
#
artist = search_artist(token, 'Davido')
total_followers, id = artist['followers']['total'], artist['id']
# print(total_followers, id)
songs = get_songs_by_artist(token, id, 'US')

with open('music.csv', 'w', newline='') as out_file:
    fieldnames = ['Number', 'name']
    writer = csv.DictWriter(out_file, fieldnames=fieldnames, delimiter='\t')
    writer.writeheader()
    for index, song in enumerate(songs):
        writer.writerow({'Number':index+1, 'name':song['name']})
    
    
with open('music.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    # data = list(reader)
    
    for row in reader:
        print(", ".join(row))