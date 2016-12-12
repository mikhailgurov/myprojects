import vk
import time

login =input('input login:')
password = input('input password:')

session = vk.AuthSession('5660321',login,password,scope='photos,friends')
print(session.access_token)
api = vk.API(session)
friends = api.friends.get()
def get_photos(friends):
    photos = []
    for friend in friends :
        deact = api.users.get(user_ids=friend)[0].get("deactivated")
        if deact == "banned" or deact == "deleted": continue

        for album in api.photos.getAlbums(owner_id=friend) :
            print('user id='+str(friend)+'  album id='+str(album.get('aid')))
            try:
                albumid=str(album.get('aid'))
                for photo in api.photos.get(owner_id=friend,album_id=albumid):
                    if 'lat' in photo and 'long' in photo :
                        print(photo.get('pid'))
                        photos.append((photo['lat'], photo['long']))
            except:
                pass
            time.sleep(0.5)
        time.sleep(1)
    return photos

users = api.users.get(user_ids=friends)
for user in users :
    print(user.get('first_name')+' '+user.get('last_name') + ' id='+str(user.get('uid')))

locations = get_photos(friends)
print(locations)

js_code = ''
for loc in locations:
    js_code += 'new google.maps.Marker({position: {lat:%s,lng:%s}, map:map});\n' % (loc[0],loc[1])

html = open('index.html').read()
html = html.replace("/* PLACEHOLDER */",js_code)
f = open('map.html','w')
f.write(html)
f.close()