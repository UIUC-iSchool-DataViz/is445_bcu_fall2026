---
title: Lecture 7.2 - Maps!
layout: lecture
description: >-
 More about maps and their projections
date: 2024-10-15
---

## Lecture's Main Topics

 * Maps - in more detail
   * Projections
   * Coordinate Systems
   * Infoviz/Choropleth maps 
   * Plotting with CartoPy (extras in prep notebook)
   * Plotting with ipyleaflet(extras in prep notebook)
   * Plotting with geopandas
   * GeoJSON in general (extras in prep notebook)

notes:
in more detail: last week we started with maps and how we can use bqplot to do a lot of mapping type stuff

This week we will play with a few different mapping and viz engines and deal with the JSON and geo-json format for storing data

again, might not get to as much with cartopy/ipyleaflet

---

<br>
<br>
<br>

# Topic #2: Maps & their projections

---

## Maps

Thinking about map projections is important for GIS data, and generic global info viz.

Let's start by thinking about the fact that...

---

## Maps

Thinking about map projections is important for GIS data, and generic global info viz.

Let's start by thinking about the fact that...

The Earth is a sphere.

(Fun question: to what degree is it a sphere?)

Have you ever wrapped a piece of paper around a ball?

---

## Projections

To map from one system to another, we must "project" from the original sphere
to the flat object we are observing.

What are some things we could preserve during such a projection?

<img src="images/mapwrap.gif" height="350" alt="A gif of a world map being 'unwrapped' into a flat cylinder representation.">

notes:
One common conversion from sphere to plane is the squashed cylinder approach

This can be used to conserve straight lines (distances)


---

## Projections

<img src="images/mapsplode.gif" height="350" alt="A gif of a world map being 'exploded' into a set of soccer-ball like hexagons.">

notes:
There's always a weird way to do it too. Here we're exploding the sphere into lots of 
mostly planar pieces that we can just lie out side-by-side.

This may preserve shape well, but it will be hard to use to navigate!

---

## Projections: Common Preservations

Typically, one or more of these will be preserved, or at least, the distortion
will be minimized:

 * Area
 * Shape (Conformal)
 * Distance

---

## Projections: Common Preservations

Typically, one or more of these will be preserved, or at least, the distortion
will be minimized:

 * Area
 * Shape (Conformal)
 * Distance

There are other properties that can be preserved, as well.  Typically, maps
will be a "compromise" between preserving different properties.

What happens when we preserve one property over another?

---

Mercator is a "conformal" projection.  What is wrong with this?


<section data-background-image="images/mercator.png" aria-label="A Mercator projection of a world map." data-background-size="70% auto">


notes:
conformal = shape preserving (at the expense of accurate size)

---

## Projections: Distortions

We can characterize distortions in a projection by examining how a known shape
appears on them.  The Tissot Ellipse of Distortion is a method of showing this
by drawing circles of a fixed radius and examining their elliptical distortion.

<img src="images/Tissot_indicatrix_world_map_Mercator_proj.svg" height="400" alt="A Mercator projection of a world map with Tissot Ellipses of Distortion overlaid.">

notes: so here for example, we see that the mercator projection has circles that
stay circles, though they change in relative size depending on where they are on the map

---

What do you notice?

<section data-background-image="images/mercator.png" aria-label="A Mercator projection of a world map." data-background-size="70% auto">


---

<section data-background-image="images/mercator_tissot.png" aria-label="A Mercator projection of a world map with Tissot Ellipses of Distortion overlaid.  The ellipses are not distorted in shape, but are much bigger at the poles than at the equator." data-background-size="70% auto">


notes:
Greenland and Antarctica are HUGE

---

<section data-background-image="images/transversemercator.png" aria-label="A Transverse Mercator projection of a world map." data-background-size="95% auto">


---

<section data-background-image="images/transversemercator_tissot.png" aria-label="A Transverse Mercator projection of a world map with Tissot Ellipses of Distortion overlaid.  The ellipses are not distorted in shape, but are much toward the edges than in the middle." data-background-size="95% auto">


notes:
this projection is most accurate near the vertical center line

---


<section data-background-image="images/lambertcylindrical.png" aria-label="A Lambert Cylindrical projection of a world map." data-background-size="95% auto">


---

<section data-background-image="images/lambertcylindrical_tissot.png" aria-label="A Lambert Cylindrical projection of a world map with Tissot Ellipses of Distortion overlaid.  The ellipses are distorted in shape and size, but sizes are much less distorted than for Mercator projections. Shape is the most distorted at the poles." data-background-size="95% auto">


notes:
Also known as "equirectangular", this is the favorite format of NASA because it's mathematically straightforward.

Note that the very top line of the image represents a single point on the globe.

---

<section data-background-image="images/mollweide.png" aria-label="A Mollweide projection of a world map." data-background-size="95% auto">


---

<section data-background-image="images/mollweide_tissot.png" aria-label="A Mollweide projection of a world map with Tissot Ellipses of Distortion overlaid.  The ellipses are distorted in shape and size, sizes and shapes are medium-distorted compared to other projections." data-background-size="95% auto">


notes:
this is considered a good compromise between shape-preserving and angle preserving - but it's not perfect at either.

---

<section data-background-image="images/sinusoidal.png" aria-label="A Sinusoidal projection of a world map." data-background-size="95% auto">

---

<section data-background-image="images/sinusoidal_tissot.png" aria-label="A Sinusoidal projection of a world map with Tissot Ellipses of Distortion overlaid. The ellipses are distorted in shape and size, sizes and shapes are medium-distorted compared to other projections." data-background-size="95% auto">

notes:
this has even less distortion than mollweide, but the pointy ends don't feel very elegant and planet-like

---

<section data-background-image="images/gnomonic.png" aria-label="A Gnomonic projection of a world map. This map is difficult to parse visually." data-background-size="95% auto">

---

<section data-background-image="images/gnomonic_tissot.png" aria-label="A Gnomonic projection of a world map with Tissot Ellipses of Distortion overlaid.  The ellipses are distorted in shape and size, with large differences at the polls." data-background-size="95% auto">

notes:
this is another nightmare scenario like Mercator that was initially created for navigation. Straight lines on this map are the shortest route, but area, shape, and size are distorted.

---

## Why bother thinking about projections?

What happens when we make a map that minimizes one region and maximizes
another?

---

## Why bother thinking about projections?

<!--
<iframe width="1024" height="576" src="https://www.youtube.com/embed/vVX-PrBRtTY?rel=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
-->

<iframe width="1024" height="576" src="https://www.youtube.com/embed/vVX-PrBRtTY?rel=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

notes:

this is from the TV show "The West Wing"

after watching this, it's useful to know that the Peters projection is actually flawed as a teaching tool because of how much it distorts the shapes of countries near the poles.

**pause recording!**

---

## Why bother thinking about projections?

[The True Size Of...](https://thetruesize.com)

notes:
Let's go see what Greenland actually looks like ...

**did you remember to turn back on the recording??**

---

## Why bother thinking about projections?

Why is Europe at the center of all the maps we've looked at?

---

## Why bother thinking about projections?

<img src="images/Azimuthal_equidistant_projection.jpg" width="512" alt="A circular map with the center at the North Pole, the South Pole is the entirety of the circumference of the circle.">

notes: there is nothing specifically wrong with putting a pole at the center of the map

---

## Why bother thinking about projections?

<img src="images/Azimuthal_equidistant_tissot.png" width="512" alt="A circular map with the center at the North Pole, the South Pole is the entirety of the circumference of the circle. Tissot Ellipses of Distortion are overlaid, showing the distortion to shape and area grow more pronounced closer to the South Pole."/>

notes: also see here that now the equator is very distorted, and the south pole even more so!

---

## Why bother thinking about projections?

<img src="images/Waterman_projection.png" width="512" alt="A Waterman projection in which the globe is broken up into several attached, nearly-triangular shapes."/>

notes: or why bother having a spherical or rectangular shape at all?

---

## Why bother thinking about projections?

<img src="images/Waterman_tissot.png" width="512" alt="A Waterman projection in which the globe is broken up into several attached, nearly-triangular shapes.  Tissot Ellipses of Distortion are overlaid, showing that the distortion to shapes and areas is minimal, but several circles are split across triangular pieces."/>

notes: look how here there is very little distortion of size or shape

---

## Maps: Coordinate Systems

Once we have our system of transformation, we need to have a method of
representing positions.

Three common baseline methods:

 * Spherical coordinates
 * Latitude and Longitude
 * Degrees, minutes, seconds

Take care with:

 * Zero points
 * North/South, East/West
 * Ranges


---

## Maps: What to plot?

![A map highlighting all landmasses on Earth (oceans in blue) with the words 'More people live in the green area than in the blue' as a title.](images/moregreen.png)

Source: [Terrible Maps Twitter](https://twitter.com/TerribleMaps?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor)

notes:
What should we actually be plotting on a map?

but while it is tempting to plot geospatial data on a map, sometimes it is not useful

---

## Maps: What to plot?

![A map showing only Australia highlighted in red with the legend 'Countries with the word girt in their national anthem' in red.](https://pbs.twimg.com/media/FpbvfrEXEBgE5_Y?format=jpg&name=small)


notes:

or, on the otherhand, it can be useful to give people a sense of even small geospatial datasets to make a point

---

## Maps: What to plot?

![A map which has been formatted to have the majority of the land masses at the edges while the oceans appear larger and in the center of the map.  The title says 'World map according to fish'.](images/fishmap.png)

notes:
but it is important to think about projections since it is making use of a common visual encoding (sort of like how the temperature/battery/fill line encodings are used as metaphors for other types of data than temperature/battery/fill)

terrible maps are actually really great!

---

<br>
<br>
<br>

# Topic #2: Formatting for shape data

---

## JSON & GeoJSON

<img src="../week02/images/jsonex.png" alt="Screenshot of the data layout of a JSON file.">

notes:
json is meant to be a way to store data that is "query" based - i.e. it lends itself to searches well

for this reason, it shows up in web development a lot

---

## GeoJSON

<img src="https://www.avenza.com/wp-content/uploads/2017/01/image002-1.png" alt="Screenshot of the data layout of a GeoJSON file.  The EPSG code is highlighted as an extra element in this formatting.">

notes:
geojson is just a special json formatting for geographical data

it will specify the "shape" of the data file but also things like its default coordinate reference system which tells you something about the "center" and "stretch" of whatever it lists in its coordinates

---

## GeoJSON

<div class="left">

GeoJSON is:
* data format for encoding geographic data structures
* uses "geometries", "features" and "collections of features"
* seven Geometry types/objects
   1. Point
   1. LineString
   1. Polygon
   1. MultiPoint
   1. MultiLineString
   1. MultiPolygon
   1. GeometryCollection

</div>

<div class="right" markdown=1>

<img src="https://www.avenza.com/wp-content/uploads/2017/01/image002-1.png" alt="drawing" width="200" alt="Screenshot of the data layout of a GeoJSON file.  The EPSG code is highlighted as an extra element in this formatting."/>

</div>


notes:
cite: https://image.slidesharecdn.com/geojson-170417122110/95/geojson-1-638.jpg?cb=1492431924

We will see a lot of Polygons & MultiPolygons.

---

## GeoJSON

Tips for dealing with GeoJSON:
 * use `.keys()` and progressively drill down to data of interest
 * look for location of `properties` and `features`

We will get *a little bit* of practice at this during programming (and in extra notebook examples).

notes:
often our issue will be linking the information stored in JSON file formats with that of whatever plotting routine we are using

we probably won't have time to go through this in the coding portion of class, but there there is an example of this in the prep notebook

---

## Access to geometry files

 1. GeoPandas
 1. Cartopy (extra in prep notebook)
 1. ipyleaflet (extra in prep notebook)
 
notes:
so, we'll mostly be using geopandas for this lecture, but there are other tools available like cartopy and ipyleaflet

If we have time, we'll go into those, but if not, they are in the extra prep notebook for today if you want to look on your own

---

## Geopandas

<img src="https://geopandas.readthedocs.io/en/v0.4.0/_images/sphx_glr_create_geopandas_from_pandas_001.png" alt="A map from the GeoPandas documentation showing the continent of South America with several capitals highlighted.">

notes:
the calls for geopandas is going to look very similar to pandas calls!

---

## Geopandas

```python
gdf = geopandas.read_file('mapfile.geojson')
gdf.head()
gdf.plot()
```

notes:
very pandas-like calls we can use

---

## Geopandas

```python
gdf = geopandas.read_file('mapfile.geojson')
gdf.head()
gdf.plot()
```

Map information sources:
 * [https://datagateway.nrcs.usda.gov/](https://datagateway.nrcs.usda.gov/)
 * [US Census info](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html)
 * [City of Champaign](https://gis-cityofchampaign.opendata.arcgis.com/)
 
notes:
we'll just touch on a few data sources, and you'll have the opportunity to explore a few more in the HW, specifically HW#4

---

## Geopandas + contextily

<img src="https://geopandas.readthedocs.io/en/v0.9.0/_images/gallery_plotting_basemap_background_8_0.png" width='500px' alt="A map from the GeoPandas documentation showing a map of the New York city burroughs with a contextual map underneath showing outlines of the landmasses and streets.">

notes:
we'll also play around with using contextily to add backgrounds to maps

---

## Other Map Viz

 * Google Maps & Earth
 * WorldWide Telescope
 * CesiumJS
 * bqplot
 * Vega & friends
 * cartopy (see extra slides)
 * ipyleaflet (see extra slides)
 
notes:
I've added a few extra slides at the end of this slide deck about cartopy and ipyleaflet that we can look over if we get to those topics

otherwise they are left for your reference

---

# To Some Coding with Maps!

---

---

# Extra Items: CartoPy

---

## Intro to cartopy

CartoPy is a toolkit that builds on matplotlib to create fast, easy map
representations.

We will be relying on three key concepts:

 * Axes projections (similar to our polar projections)
 * Coordinate representations
 * Shapes

Using these, we will be able to build out many visualizations.

---

## CartoPy: Projections

We start out by constructing an axes in CartoPy that uses a given projection:

```python
import cartopy
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection=cartopy.crs.Mollweide())
ax.coastlines()
```

---

## CartoPy: Coordinate Reference Systems

Transforming from a spherical reference system to a flat reference system is
the job of the projection; transforming from one discretization of a sphere to
another is the job of the coordinate system.

We can utilize Coordinate Reference Systems to describe the *input* coordinate
system and the *rasterization* system are described.

For example, there are several different ways to draw "straight" lines.  We can
do both `PlateCarree` and `Geodetic`.

```python
c_lat, c_lon = 40.1164, -88.2434
a_lat, a_lon = -18.8792, 47.5079
fig = plt.figure()
ax = fig.add_subplot(111, projection = cartopy.crs.PlateCarree())
ax.gridlines()
ax.coastlines()
ax.set_global()
ax.plot([c_lon, a_lon], [c_lat, a_lat], transform = cartopy.crs.PlateCarree())
ax.plot([c_lon, a_lon], [c_lat, a_lat], transform = cartopy.crs.Geodetic())
```

---

<section data-background-image="images/map_plot1.png" aria-label="A rectangular map projection.  The blue line is straight on a Plate Carree projection, which maintains a straight line on the latitude-longitude grid and the orange line is geodetic which maintains a straight line around the curvature of the Earth." data-background-size="95% auto">


notes:
the blue line is Plate Carree, which maintains a straight line on the lat-lon grid

the orange line is Geodetic, which maintains a straight line around the curvature of the Earth

---

<section data-background-image="images/map_plot2.png" aria-label="A Mollweide map projection.  The blue line would be straight on a Plate Carree projection, but now is slightly curved and the orange line is geodetic which maintains a straight line around the curvature of the Earth." data-background-size="95% auto">

notes:
now even the blue line has some curvature because we are picking a best-of-both-worlds Mollweide projection that doesn't perfectly preserve angle or area.

---

## ipyleaflet

Leaflet is another mechanism of plotting, displaying and interacting with maps.

We will very briefly play with this in Python - could be of use for those that were having issues with cartopy.

