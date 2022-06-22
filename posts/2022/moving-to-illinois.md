---
author: Max Grover
date: 2022-06-06
tags: Illinois, Argonne, Wisconsin
---

# Moving to Illinois (Again)

It has been a while since my last post! Over the past ~9 months, I started a new job at Argonne National Laboratory and relocated to the state of Illinois, more specifically the Western Suburbs of Chicago, Illinois. I work with Scott Collis, a scientist and Geospatial Computing, Innovations, and Sensing (GCIS) Department Head. He is also the inventor of the [Python Atomspheric Radiation Measurement Toolkit (Py-ART)](https://arm-doe.github.io/pyart/index.html), one of the go-to packages when working with weather radar data in Python.

## Closer to Home

One of the nicest things about relocating is the proximity to my family in Wisconsin. I have gone back to see them several times already, spending quite a bit of time on Delavan Lake (shown below)
![Delavan Lake Sunset Picture](../images/delavan-lake-sunset.png)

## Reflecting on my new role
My new role at Argonne is similar to my old job at NCAR - I am able to develop open-source, Python software for the atmospheric science/climate community. I serve in more of a hybrid software engineer/scientist role, which has been exciting, leveraging my background in meteorology and atmospheric science. I work on both Py-ART and the [Atmospheric data Community Toolkit (ACT)](https://arm-doe.github.io/ACT/).

### Maintaining Core Meteorology Packages
One of my first tasks within [Py-ART](https://arm-doe.github.io/pyart/index.html) and [ACT](https://arm-doe.github.io/ACT/) development was overhauling the continuous integration system, moving towards [Github Actions]() as the automation tool instead of [Travis-CI](https://travis-ci.org).

I have also been adding more examples, and helped organize the first ARM/ASR Open Science Workshop, taking the lead on the Tutorial side. Tutorials covered the core scientific Python packages (ex. NumPy, Matplotlib, SciPy, Xarray), and extended to domain-specific packages such as Py-ART, ACT, and Py-SP2. Here are links to the:
* [Youtube Recordings](https://www.youtube.com/playlist?list=PLqJPE7n0ZqA91W18gnmOge51VjpyFvLAt)
* [Tutorial Website](https://arm-development.github.io/ARM-Notebooks/Tutorials/Open-Science-Workshop-2022/presentations/view-abstracts.html)

## Goals for the Near Future
We have some exciting developments coming for Py-ART... 

### Xarray in Py-ART
One of the main projects I am working on right now is migrating the core data model ([`pyart.core.Radar`](https://arm-doe.github.io/pyart/API/generated/pyart.core.Radar.html)) object to the [`xarray.Dataset`](https://docs.xarray.dev/en/stable/generated/xarray.Dataset.html) data model. This will enable more cross-compatibility in the Pangeo ecosystem, and empower new tools to built on top of this ecosystem.

### Radar Cookbooks
Another key area of development are the [Project Pythia Cookbooks](https://projectpythia.org/cookbook-gallery.html) (ex. [Radar Cookbook](https://projectpythiatutorials.github.io/radar-cookbook/landing-page.html)), which extend the [Pythia Foundations](https://foundations.projectpythia.org/landing-page.html) content beyond the basics, diving more into domain-specific tools such as Py-ART. We link to existing foundational materials (ex. NumPy, Matplotlib) where possible, and build new content where neccessary.

### Machine Learning Applications
I am also working on learning more about machine learning applications for weather and climate. I purchased a couple of new books, and plan on trying some test project using various climate projects, weather radar data, and open source tools.

## Moving Away from Colorado
It was tough saying goodbye to my friends and former coworkers in Colorado. Living in the Boulder area was an amazing experience, one that I will always be thankful for. I miss Tuesday night trivia at Rayback, Friday Happy Hour at Jungle, and Saturday morning hikes around Boulder's world-class trails.

I look forward to visiting my Boulder friends in the future, and I am sure work will bring me to the Boulder at some point (looking forward to AMS 2023 in Denver).

## Conclusions

It has been a fun filled, productive first few months at Argonne! I have already met up new friends and coworkers around the Argonne area, and look forward to exploring the Chicago area more! 

Argonne's softball league starts Wednesday, we already found a new Tuesday trivia place, and I have reconnected with some of my best friends from undergrad, who live a short drive away. 

I am adjusting to my new home, and as with all things, it just takes time!
