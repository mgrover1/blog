---
author: Max Grover
date: 2022-07-17
tags: SciPy, Conference, Outreach, Open-Science
---

# SciPy 2022 Reflection
This past week, I attended my third SciPy conference, with this being the first in-person event.

## Overview of the Conference
![ATT conference hotel at night](../images/att-conference.jpeg)
The AT&T Hotel and Conference Center near the University of Texas Campus in Austin, Texas.

### What’s SciPy?

The Scientific Python (SciPy) Conference is annual meeting, typically held in Austin, Texas, which brings the broad community doing science using the Python programming language together. The week long conference consists of three parts:
* [Tutorials](https://www.scipy2022.scipy.org/tutorials) - how to use the tools
* [Talks](https://www.scipy2022.scipy.org/talk-poster-presentations) - package updates and how people are using the tools
* [Birds of a Feather](https://www.scipy2022.scipy.org/bof-sessions) - mini sessions focused on specific topics or communities
* [Sprints](https://www.scipy2022.scipy.org/sprints) - gathering to contribute to projects

The conference provides an opportunity to learn about new updates within the community, meet and coordinate with other developers, and help entrain new contributors to tools within the ecosystem. 


### Who goes?

The conference included people interested in scientific software written in Python! This includes (but is not limited to):

* Scientists
* Software developers
* Data scientists
* Package maintainers
* Package users
* Outreach folks
* Companies looking to hire the people listed above

There were so many scientific disciplines represented at the conference! Everything from earth science, astrophysics, material science, and biology just to name a few. The combination of all these different parts of scientific software development process (first time user to maintainers).

As a software developer, this is a great opportunity to coordinate with other contributors to the scientific Python ecosystem. As a scientist, this is a fantastic opportunity to investigate innovative ways people are using tools in the scientific python ecosystem.

I am glad that many Pangeo community members attended, included folks from Columbia University, USGS, and CarbonPlan. I connected with new and old friends which is always a great time 😀. 

## The Tutorials
I attended tutorials covering distributed + parallel computing using Dask, and  interactive plotting tutorials showcasing hvPlot and PyVista. These toolsets are essential to the atmospheric data science stack - allowing us to scale our analysis, and visualize our output. 

Here is a link to the repositories/content used:
* [GitHub - dask/dask-tutorial: Dask tutorial](https://github.com/dask/dask-tutorial)
* [Installation — HoloViz 0.15.0 documentation](https://holoviz.org/installation.html)
* [PyVista Tutorial for SciPy 2022 — PyVista Tutorial](https://tutorial.pyvista.org)

I plan on adding a future blog post with a neat data visualization using the tools from the tutorials.

## The Talks
My favorite session (slightly biased I know) of the conference was the Earth, Geo, Ocean, and Atmosphere session. During this session, presenters showcased the latest and greatest tools including:

* [PyGMT](https://www.pygmt.org/latest/)  - a mapping and general data visualization/analysis tool
    * Presented by [Max Jones](https://github.com/maxrjones)
* [xMIP](https://cmip6-preprocessing.readthedocs.io/en/latest/?badge=latest) + Pangeo tools - a toolkit for working with CMIP6 data and other climate ensembles
    * Presented by [Julius Busecke](https://github.com/jbusecke)
* [GeoCAT](https://geocat.ucar.edu) - a toolkit to work with geoscience data, developed at the National Center for Atmospheric Research
    * Presented by [Orhan Eroglu](https://github.com/erogluorhan)
* [Project Pythia](https://projectpythia.org) - educational resources for learning the geoscience python ecosystem
    * Presented by [Kevin Tyle](https://github.com/ktyle)
* [xGCM](https://xgcm.readthedocs.io/en/latest/) + Pangeo tools - enabling petabyte scale climate analysis on staggered grids
    * Presented by [Tom Nicholas](https://github.com/TomNicholas) and [Julius Busecke](https://github.com/jbusecke)
* [Tobac](https://tobac.readthedocs.io/en/latest/) - a flexible langrangian analysis toolkit
    * Presented by [Bobby Jackson](https://github.com/rcjackson) and [Bhupendra Raut](https://github.com/RBhupi)

Some of the main themes from this track was how we need flexible and performant tools. Tom’s talk dug into debugging complex Dask issues, which was solved by working with the Dask core developers. Keeping these lines of communication open and working together to solve these tough technical issues are what enable new questions to be answered from datasets like the one Tom presented - at the petabyte scale (1,000 terabytes).

There were so many other great sessions on data, maintainers tools, and keynotes about how important open and inclusive science are (looking at you Ben and Ryan). 

I will be sure to link the videos here once they are posted on YouTube!

## Birds of a Feather (BoFs)
The main birds of a feather session I attended was the Pangeo one (Pangeo Community Gathering).

The session started with an overview of the Pangeo community and introductions. We moved onto highlighting key features currently missing within the technological toolset, and decided to separate into smaller groups at dinner after to discuss in more detail.

I am particularly interested in the outreach component - mainly how to continue to grow the community at larger organizations such as Department of Energy National Laboratories (ex. Argonne National Lab) and user facilities (ex. ARM).

If you are interested in the rest of the discussion, here are the notes!
* [Notes to Pangeo BoF](https://docs.google.com/document/d/1m0w9-caHLVAgxI5Meq8ZkErQwP8zhybIhTjirtPdhJU/edit?usp=sharing)

## The Sprints

### [Pangeo-Forge](https://pangeo-forge.org)

Ryan Abernathy gave an amazing talk on Pangeo-forge, a tool that enables data to be converted to analysis ready cloud-optimized (ARCO) datasets. This means thinking of datasets not necessarily at the **file** level, but rather at the **dataset** level, making the data openly available through an object store file system (think AWS Cloud). 

This project had a sprint on Saturday and Sunday, which I took part in! I worked on a “recipe” which pulls radar data from the Atmospheric Radiation Measurement (ARM) user facility, merges the files together, and writes to a single Zarr store (a cloud optimized file format). I look forward to working with the ARM community to see how we can explore the benefits of ARCO data.

### [Datatree](https://xarray-datatree.readthedocs.io/en/latest/#) + [Xarray](https://xarray.dev)

I initially worked with the Xarray group on investigating the new flexible index API, which enables more complex indexing within Xarray (selecting data based on non-dimensional coordinates).

An example of this would be a radar sweep. Imagine if you could select a single gate (point) from a radar dataset despite the coordinates being the angle around the radar and the distance from the radar.

After testing out the functionality, I moved to updating my example of prototype xradar object, which utilizes datatree.  Datatree is a project supporting hierachal datasets (ex. Radar with different sweeps, or netCDF groups) in xarray. The package was built by the xarray community, with the lead develpoer being Tom Nicholas. 

## How Do We Move Forward?
After this conference I am energized to make progress in the following areas:
* Continue to grow the Pangeo community within ARM/DOE and beyond
* Add our new xradar object to Py-ART
* Coordinate with the Pangeo community on package development related to Xarray + Datatree

I look forward to moving forward with all the new tools and knowledge from this conference. I am fortunate and privileged to have had an opportunity to attend in person, and to have met so many developers and users from the scientific python community.  I am thankful that my supervisor (Scott Collis) and fellow group members at Argonne National Laboratory were able to attend too!

I think this graphic from Julius’s talk sums up the key components of the Pangeo stack that enable science.

![pangeo stack](../images/pangeo-slide.jpeg)
A slide from Julius’s talk summarizing the components of the Pangeo stack enabling CMIP6 analysis.

I look forward to continuing to work with the Py-ART developer community to enable to use of this same stack for radar data (replacing xMIP with Py-ART in this case), enabling the same terabyte or even petabyte workflows described by Tom.

I encourage anyone remotely interested in learning more about how python empowers and enable science to attend SciPy. It was empowering to meet the people behind so many key packages in our ecosystem (SciPy, NumPy, Matplotlib, and Xarray).

I am already counting down the days until SciPy 2023.

If you were interested in this post, make sure to check out Scott's writeup too!
* [Link to Scott Collis's blog post on SciPy 2022](https://opensky.press/2022/07/15/scipy-thoughts/)
