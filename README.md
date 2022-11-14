# Crashmap
"All heat maps are population maps"

Mostly created to see if any interesting patterns came out of mapping fatal crashes over a 10 year period (2009-2019)

<h1> Lessons from doing this </h1>
<ul>
<li> "Heat maps are population maps" is very true</li>
<li> Generally obvious things came to light: Arterial street intersections are very dangerous. Busy, twisting higways are dangerous. Etc </li>
<li> More work needs to be done to fully grok the Mapbox API</li>
</ul>

<h1> Local Server needed for testing </h1>
Due to CORS issues (and not being able to just launch from local anymore, probably obvious to most web devs at this point?)
Run the following in the directory the project is in, then access via localhost:8000

The following command works for python 3:

$ python3 -m http.server 

<h1> Example Images </h1>
<h2>Full View</h2>
<img src="https://raw.githubusercontent.com/Dsrts-edu/Crashmap/main/map1.png" width=100% height=100%>

<h2>Zoomed View</h2>
<img src="https://raw.githubusercontent.com/Dsrts-edu/Crashmap/main/map2.png" width=100% height=100%>



