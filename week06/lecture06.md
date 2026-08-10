---
title: Lecture 6.1 - Dashboards & Maps 
layout: lecture
description: >-
 Linking data with Dashboards 
date: 2023-09-26
---

## Reminder: change of modalities today

Topics:
 * announcements
 * short lecture about linked data
 * some brief Lab #5 hints
 * rest of time used to ask questions about Lab #5

---

## Quick note about Homework extensions

These are typically processed the day after the Homework is due (typically Mondays/weekend), so don't worry if you request an extension and don't hear back from us right away!

---

## Where we are: Last week

<img src="images/dataviz_map_lastweek_take2.png" alt="A 'mind map' of last week's topics including introducing grammar of graphics and beginning interactivity.">

notes: last week in the recording we started playing with dashboarding using some randomly generated data in bqplot

we also started working with the Grammar of Graphics and used bqplot declaratively to start "painting" scales and axis on our canvas

we also talked about different viz engines and you got to look at this in the HW


---

## Where we are: Today

<img src="images/dataviz_map_thisweek.png" alt="A 'mind map' of this week's topics including dashboard building with bqplot and some things with maps (but most likely maps next time).">

notes: 

Today we'll continue with bqplot and work on building up dashboards

if we have time we'll also start talking about map projections this week (but we might only get to it next week)

---

## Today's Main Lecture Topics

 1. Interactivity and linked views
 1. More dashboarding
 1. Dashboards with maps

---

<br>
<br>
<br>

# TOPIC 1: Interactivity


---

## Interactivity

This week, we'll talk about some more basics principles of interactivity in
visualization.

What do you think of when you think of interactive visualizations?

---

## Interactivity: Parameters


   <section data-background-image="images/brushlink_01.svg" aria-label="A simple scatter plot with points." data-background-size="80% auto" data-background-position="right 50% bottom 50%">


 * Point characteristics
 * Axis limits/bounds
 * Transform/scale

note: we'll think a little about different ways to manipulate each of these types of plot characteristics

---

## Interactivity: Parameters

<section data-background-image="images/brushlink_01.svg" aria-label="A simple scatter plot with points." data-background-size="80% auto" data-background-position="right 50% bottom 50%">

 * Point characteristics - Click-and-drag
 * Axis limits/bounds - Rectangle zoom
 * Transform/scale - Adjustment

---

## Interactivity: Linking & Brushing

<section data-background-image="images/brushlink_02.svg" aria-label="Two simple graphs, first is for variable 1 (x-axis) and variable 2 (y-axis), second is for variable 3 (x-axis) and variable 4 (y-axis)." data-background-size="80% auto" data-background-position="right 50% bottom 50%">


`data(variable1, variable2, variable3, variable4)`

note: here we are plotting a set of data that is a function of 4 variables.

For example, this could be the amount you are late to class as a function of (1) how much sleep you got, (2) how excited you are about the topic that day (3) how nervous you are about the topic that day and (4) how much of your homework the dog ate.

here we are plotting 2 2d plots of this dataset - were we know intuitively each point is represented both as a dot on the first graph *and* as a dot on the 2nd graph

---

## Interactivity: Linking & Brushing

<section data-background-image="images/brushlink_02.svg" aria-label="Two simple graphs, first is for variable 1 (x-axis) and variable 2 (y-axis), second is for variable 3 (x-axis) and variable 4 (y-axis)." data-background-size="80% auto" data-background-position="right 50% bottom 50%">


`data(variable1, variable2, variable3, variable4)`

`filter( variable2 > variable1 )`

note: now we are going to think about applying a simple filter, based around the first plot

we'll only show data where variable2 > variable1

---

## Interactivity: Linking & Brushing

<section data-background-image="images/brushlink_03.svg" aria-label="Two simple graphs, first is for variable 1 (x-axis) and variable 2 (y-axis), second is for variable 3 (x-axis) and variable 4 (y-axis).  The first plot has a line where variable 1 is equal to variable 2." data-background-size="80% auto" data-background-position="right 50% bottom 50%">

`data(variable1, variable2, variable3, variable4)`

`filter( variable2 > variable1 )`

note: lets draw a line where the demarkation of our filter would be

---

## Interactivity: Linking & Brushing

<section data-background-image="images/brushlink_04.svg" aria-label="Two simple graphs, first is for variable 1 (x-axis) and variable 2 (y-axis), second is for variable 3 (x-axis) and variable 4 (y-axis).  Data has been removed from both plot where variable 1 is less than to variable 2. " data-background-size="80% auto" data-background-position="right 50% bottom 50%">

`data(variable1, variable2, variable3, variable4)`

`filter( variable2 > variable1 )`

note: ... and lets take out all the data of both plots that has variable2 <= variable1

---

## Interactivity: Linking & Brushing

<section data-background-image="images/brushlink_05.svg" aria-label="Two simple graphs, first is for variable 1 (x-axis) and variable 2 (y-axis), second is for variable 3 (x-axis) and variable 4 (y-axis).  The first plot has a oval selecting several points in a cluster in variable 1 - variable 2 space." data-background-size="80% auto" data-background-position="right 50% bottom 50%">

note: we can also select regions in our linked view

---

## Interactivity: Linking & Brushing

<section data-background-image="images/brushlink_06.svg" aria-label="Two simple graphs, first is for variable 1 (x-axis) and variable 2 (y-axis), second is for variable 3 (x-axis) and variable 4 (y-axis).  The first plot has a oval selecting several points in a cluster in variable 1 - variable 2 space, dashed lines link points in the first and second plots." data-background-size="80% auto" data-background-position="right 50% bottom 50%">

note: here are how these points are linked in the plot of variable3 vs variable4

---

## Interactivity: Linking & Brushing

<section data-background-image="images/brushlink_07.svg" aria-label="Two simple graphs, first is for variable 1 (x-axis) and variable 2 (y-axis), second is for variable 3 (x-axis) and variable 4 (y-axis).  The first plot has several points selected in variable 1 - variable 2 space, the linked data points in variable 3 - variable 4 space are also highlighted." data-background-size="80% auto" data-background-position="right 50% bottom 50%">

note: so when we select with our brush in the first plot we can show what is selected in the second plot

---

## Interactivity: Linking & Brushing with UFO data

![Scatter plot from the 'ufo dataset' with the year of the sighting on the x-axis and the duration of the sighting in seconds on the y-axis.](images/durationAllPoints.png)

note: as a "practical" example, we can for example make cuts in things like the
duration of UFO sitings for all years

---

## Interactivity: Linking & Brushing with UFO data

![Scatter plot from the 'ufo dataset' with the year of the sighting on the x-axis and the duration of the sighting in seconds on the y-axis.  A horizontal line is drawn at duration in seconds of about 5000.](images/durationAllPoints_p2.png)

note: we can select only the longest sitings

---

## Interactivity: Linking & Brushing with UFO data

![Scatter plot from the 'ufo dataset' with the year of the sighting on the x-axis and the duration of the sighting in seconds on the y-axis.  Points below duration in seconds of about 5000 are removed.](images/durationLongPoints.png)

note: this is how this plot would now look

---

## Interactivity: Linking & Brushing with UFO data

![Scatter plot from the 'ufo dataset' with the latitude of the sighting on the x-axis and the longitude of a sighting on the y-axis (a simple map plot).](images/mapAllPoints.png)

note: and then we can see how the map changes

this is our original

---

## Interactivity: Linking & Brushing with UFO data

![Scatter plot from the 'ufo dataset' with the latitude of the sighting on the x-axis and the longitude of a sighting on the y-axis (a simple map plot).  Sightings with durations shorter than 5000 seconds are removed.](images/mapLongPoints.png)

note: this is how this dataset looks now w/o the shortest duration ufo sitings

---

## Interactivity: Linking & Brushing with UFO data

As a dashboard:

<!-- .slide: class="two-floating-elements" -->

<div class="left">
  <img src="images/durationAllPoints.png" alt="Scatter plot from the 'ufo dataset' with the year of the sighting on the x-axis and the duration of the sighting in seconds on the y-axis.">
</div>

<div class="right">
 <img src="images/mapAllPoints.png" alt="Scatter plot from the 'ufo dataset' with the latitude of the sighting on the x-axis and the longitude of a sighting on the y-axis (a simple map plot).">
</div>

notes:
as a dashboard, this process would look something like this where we have the duration in seconds on the left "driving" changes in the lat/long points shown on the right


---

## Interactivity: Linking & Brushing with UFO data

As a dashboard:

<!-- .slide: class="two-floating-elements" -->

<div class="left">
  <img src="images/durationAllPoints_p2.png" alt="Scatter plot from the 'ufo dataset' with the year of the sighting on the x-axis and the duration of the sighting in seconds on the y-axis.  A horizontal line is drawn at duration in seconds of about 5000.">
</div>

<div class="right">
 <img src="images/mapAllPoints.png" alt="Scatter plot from the 'ufo dataset' with the latitude of the sighting on the x-axis and the longitude of a sighting on the y-axis (a simple map plot).">
</div>

notes:

our user would then select a threshold they wanted to cull the data by

---

## Interactivity: Linking & Brushing with UFO data

As a dashboard:

<!-- .slide: class="two-floating-elements" -->

<div class="left">
  <img src="images/durationAllPoints_p2.png" alt="Scatter plot from the 'ufo dataset' with the year of the sighting on the x-axis and the duration of the sighting in seconds on the y-axis.  A horizontal line is drawn at duration in seconds of about 5000.">
</div>

<div class="right">
 <img src="images/mapLongPoints.png" alt="Scatter plot from the 'ufo dataset' with the latitude of the sighting on the x-axis and the longitude of a sighting on the y-axis (a simple map plot).  Sightings with durations shorter than 5000 seconds are removed.">
</div>

notes:

and those changes would propagete to our right-hand plot through a data "linkage", thus allowing our user to have multiple views of this dataset

---

<iframe width="1024" height="576"
src="https://www.youtube.com/embed/B7XoW2qiFUA?rel=0" frameborder="0"
allow="autoplay; encrypted-media" allowfullscreen></iframe>

[Link to video](https://www.youtube.com/embed/B7XoW2qiFUA)

note: here is one of the first examples of a "linked view" visualization machine.  We won't watch this whole video, but
if you are interested, they talk about how they can "interact" with different views

this was developed by SLAC (stanford linear accelerator)

prim9 = picturing, rotation, isolation & masking in up to 9 dimensions - for looking at multidimensional datasets
this was developed for particle data (so, like x,y,z and vx,vy,vz might be of interest)

*pause recording here!*

---

## Implementing This

Two main approaches to the selection process:

 * Concurrent filtering ("masks")
 * Index-based selection (i, j - based)

What are the pros and cons of each?

What are methods of showing "linked" and "brushed" data if you have:

 * Scatter plot
 * Histogram
 * Field / image plot

notes: 
hint -- we already discussed index based last class with the grid heatmap and the histogram plots

and we've done masking before with the filtering of images AND there are more hints in the recording you all watched before this class

---

<br>
<br>
<br>

# TOPIC 2: Dashboarding

---

## Pre-class Video's Python Programming:

We progressively build a dashboard for the UFO dataset using the following steps:

 * Create heat maps of the sightings in the UFO dataset
 * Select based on location (do not use map marks yet)
 * Manually create "bins" for aggregation (**this is "pre-done" for us**)
 * Use different scales for dates, times, locations

And build up a _dashboard_ for our data.

notes:
in the prep notebook, it is shown how the histogramming is done, however for timing purposes we'll just use a function

---

## Dashboards: Tableau
![An example Tableau dashboard showing several views of sales data across the United States.  Views include a map of the United States with regions (Central, East, West, South) highlighted, a bar chat showing sales in specific states, and sales over time.](images/Tableau-Sample-Training-Dashboard-Original.png)

notes: so here is an example of a dashboard, I *think* from Tableau.  Here we see a linked view which
displays data in several different ways to give the user the ability to visualize what their data
means spatially (with the map & region bargraph) and temporally (with the calendar/bar view at the bottom)

---

## Dashboards: Glueviz
![An example dashboard from GlueViz.  Dashboard shows region of an image of the sky with a portion highlighted (left plot), and the grayscale distribution of pixels for the full image and the selected region showing the selected region is brighter.](images/histogram.png)

note: aside, there are opensource dashboarding type software, this is an example of glueviz that is
used a lot in astronomy and built on python

This is an example of binning light (dark or bright pixels) in an image of a star forming region (I think),
and linking this with a histogram which responds to a selection tool (in red) in the image.

---

## Dashboards: Building our own in Python

Why bother?

notes: so, given that there is dashboarding software out there, why would be bother going through the difficulty of doing it ourselves?

---

## Dashboards: Building our own in Python

Why bother?
 * Understand choices about data formatting/missing data

notes: the first reason is that we can learn a bit about what choices we make for "messy" data

---

## Dashboards: Building our own in Python

Why bother?
 * Understand choices about data formatting/missing data
 * Understand necessary data transformations

notes: next, we can learn a bit about how data is transformed to make it dash-boardable

---

## Dashboards: Building our own in Python

Why bother?
 * Understand choices about data formatting/missing data
 * Understand necessary data transformations
 * Understand data links

notes: also we want to understand the ways we can actually link parts of our data together -- what choices do we make to link data like this?

if we use dashboarding software, it can often obfuscate a lot of of these aspects

---

## Lab \#5 hints

notes:
* so as discussed last week, 5.1 is basically just a walk through of what we did in class but feel free to check out the prep notebook for more info
* 5.2 is some practice doing pivot tables so its suggested you do this next 
* 5.3 is based on things that we went over in the video for this week, this combines ideas from 5.1 & 5.2 so save this for last

Reminder: 
* do each "step" one at a time and hit Save & Grade 
* this will catch any "variable overwrite" errors that you may have
* plus you want to make sure you've got one step "correct" before moving on

