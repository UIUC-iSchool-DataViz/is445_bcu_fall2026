---
title: Lecture 7.1 - Viz Engines
layout: lecture
description: >-
 A bit about Viz Engines
date: 2025-10-14
---

## Where we are: Last week

<img src="images/dataviz_lastweek_t3.png" alt="A mind-map style visualization of topics covered last week in class, including interactive dashboard building.">

notes:
last week we messed around a bit with mappable data and made some interactive dashboards

---

## Where we are: This week

<img src="images/this_week_diagram.png" alt="A mind-map style visualization of topics covered this week in class, highlighting map projections and various visualization engines.">

notes:

this week we'll start by talking a bit about different visualization engines and then 

we'll talk a bit about map projections and a few specific engines

fyi -- we might not get to much of ipyleaflet and cartopy, but there are some extra notebooks from other years with more examples

---

<br />
<br />
<br />

# TOPIC 1: Visualization Engines

notes: 
since we are starting to explore our first new viz engine, it is worth spending some time thinking about some questions we might want to ask our selves about said engines


---

## Evaluating Visualization Engines

 * Costs
 * Functionality
 * Aesthetics
 
notes: is this engine free or do you have to pay for it?  Does it do what I want?
Does its plots look like plots I want to make?

---

## Choices

 * Can I get ahold of this software?
 * Do I install it, or do I use it on a server?
 * What's the user interface like?
 * Is it declarative or is it procedural/imperative?
 
notes: we'll go over some basic considerations when choosing a viz engine, but here are a few broad questions to ask 

---

## License: Software

 * What can you do with the software?
 * Can you study the software?
 * Who can you share it with?
 * Who can you give your derivative works to?
 
notes: while the viz engines we use in this class are generally open source, you may run into engines that are not or "somewhere in between"

In this case, you might have to think carefully about how you share your viz with others, you can use what you create? Can you actually study how the software works?

---

## License: Software

 * Copyleft: share and share-alike
 * Non-copyleft: share, but don't necessarily need to share-alike
 * https://choosealicense.com/
 
notes: this website has a bunch of "auto" generated licenses, depending on what kind of license
you want *your* software to use

If you are ever in a position to create software, you can check this out to see what sorts of options you have.

Also, many of the open source packages we'll be using (including python) use a specific kind of license.  A lot of folks use the MIT licenses, fyi.

---

## License: Data

 * What can you do with the data?
 * How do you credit that data?
 * Can the data be redistributed, remixed, modified?
 * http://opendefinition.org/guide/data/
 * https://theodi.org/article/publishers-guide-to-open-data-licensing/

notes: additionally, the data that you chose to use might have a specific license.  So maybe you can use the data for your viz, but not share the data itself with others.

How can the data be modified?  Can you share the modified data?


---

## Accessibility

 * Is the software installed locally on your machine?
 * Is it hosted at a local or remote instance?
 * Who owns the visualizations, and how is access to them controlled?

---

## Interface

How do you interact with the software?

 * Declarative: how do you want the plot to look?
 * Imperative/Procedural: what are the steps to make the plot look that way?

notes:
reminder -- you now have experiences with both, matplotlib for imperitive and bqplot for declarative (and we'll get more experience with declartive viz when we move to altair/vega-lite)

---

## Evaluation: Costs

The "cost" of software is not exclusively the number of dollars you place on
the counter when you get a big cardboard box with marketing blurbs on the side.

Think about cost in several ways:

 * Monetary cost for *you* to use the software
 * Monetary cost for *someone else* to view your creations
 * Temporal cost of setting up
 * Cognitive cost for learning and using the system (documentation matters!)
 * Transmission cost for sharing your creations

---

## Evaluation: Aesthetics

Visualization is trendy.

When you construct something, think about the different ways it will be
interpreted:

 * How will the viewer understand the story of the data?
 * What will the _message_ of the visualization be?
 * Does the visualization say something about you and your handling of the data
   or utilization of tools?




