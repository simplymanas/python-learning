import folium


# m = folium.Map(location=[51.98504, -0.18622])


m = folium.Map(
    location=[51.98504, -0.18622],
    tiles='Stamen Toner',
    zoom_start=13
)
m.save('index.html')