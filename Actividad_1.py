import pyfiglet
import requests
from concurrent.futures import ThreadPoolExecutor

sitios = {
    "Twitter": "https://twitter.com/{}",
    "GitHub": "https://github.com/{}",
    "Facebook": "https://facebook.com/{}",
    "Instagram": "https://instagram.com/{}",
    "YouTube": "https://www.youtube.com/@{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "Telegram": "https://t.me/{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "OLX Colombia": "https://www.olx.com.co/profile/{}",
    "Foros El Tiempo": "https://www.eltiempo.com/usuario/{}",
    "La Silla Vacía": "https://lasillavacia.com/usuario/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Mercado Libre": "https://perfil.mercadolibre.com.co/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Discord": "https://discord.com/users/{}",
    "Deezer": "https://www.deezer.com/profile/{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "WordPress": "https://{}.wordpress.com",
    "Blogger": "https://{}.blogspot.com",
    "TripAdvisor": "https://www.tripadvisor.com/Profile/{}",
    "Goodreads": "https://www.goodreads.com/user/show/{}"


}

def buscar_usuario(usuario):
    resultados = []
    for nombre, url in sitios.items():
        link = url.format(usuario)
        try:
            resp = requests.get(link, timeout=5)
            if resp.status_code == 200:
                resultados.append((nombre, link))
        except:
            pass
    return resultados

# Generar el banner
banner = pyfiglet.figlet_format("Sherlock Colombia")
print(banner)
usuario = input("Ingresa el usuario que deseas buscar: ")

# Llamar función y obtener resultados
resultados = buscar_usuario(usuario)

if resultados:
    print("\nResultados encontrados:")
    for nombre, link in sorted(resultados):
        print(f"+ {nombre} = {link}")
else:
    print("\nNo se encontraron perfiles con ese usuario.")