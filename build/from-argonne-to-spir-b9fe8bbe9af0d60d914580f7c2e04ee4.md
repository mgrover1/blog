---
author: Max Grover
date: 2026-04-01
tags:
- Career
- Spire
- gribberish
- Weather
- Open Source
description: Reflections on transitioning from Argonne National Laboratory to Spire Global, and the open-source tools powering satellite weather data pipelines.
---

# From Argonne to Spire: A New Chapter in Weather Software Engineering

## A Career Transition

In September 2025, I made the leap from Argonne National Laboratory — a Department of Energy facility where I spent three years as an Atmospheric Data Scientist — to [Spire Global](https://spire.com/), where I now work as a Senior Weather Software Engineer.

At Argonne, I had the privilege of working on open-source tools for the atmospheric science community, contributing to programs like the [ARM User Facility](https://arm.gov), the [Open Radar Community](https://openradarscience.org/), and the [Earth System Grid Federation](https://esgf.llnl.gov/). That work deepened my conviction that open-source infrastructure is essential for advancing weather and climate science, and building a strong open science community around these tools.

So when the opportunity at Spire came along, it felt like a natural evolution, taking those same skills and tools to scaling data pipelines in industry, especially on cloud platforms such as Amazon Web Services (AWS).

## Why Spire

[Spire Global](https://spire.com/) is a space-based data, analytics, and space services company. They operate a constellation of nanosatellites that collect global weather data through radio occultation, AIS (ship tracking), and ADS-B (aircraft tracking), among other payloads. For someone working at the intersection of weather data and software engineering, it's a compelling environment. I also knew a few of the employees, based in Boulder Colorado, before making the leap. They all had great things to say, and an opportunity opened at the right time.

What drew me in was the combination of:

- **Global-scale weather data**
- **A commitment to supporting open-source (where applicable)**
- **Cloud-native infrastructure**

My role focuses on building and deploying data pipelines that process numerical weather prediction and observations, making them available for downstream applications for our customers.

## The Technical Work

### gribberish: Decoding Weather Data at Speed

One of the key tools in this space is [gribberish](https://github.com/mpiannucci/gribberish), a Rust-based GRIB2 decoder with Python bindings. GRIB2 is the standard binary format for weather data, used by meteorological agencies worldwide. If you've worked with weather model output or observational datasets, you've almost certainly encountered it. It is structured to work well with operational writing, but it is not the optimal storage format for archives.

The challenge with GRIB2 is that decoding it at scale. Millions of messages per day from global models and satellite retrievals requires high throughput. Traditional Python-based decoders struggle at this volume. Gribberish solves this by doing the heavy lifting in Rust while exposing a clean Python API, giving you the performance of a systems language with the broader ecosystem support of Python.

I've been contributing to gribberish to improve its support for the kinds of GRIB2 messages we encounter in satellite weather pipelines. Edge cases in packing schemes, template definitions, and metadata handling that matter when you're processing data from diverse sources.

## Continuing Open-Source Commitments

Moving to industry hasn't changed my commitment to open-source work. I continue to maintain and contribute to:

- [**Py-ART**](https://github.com/ARM-DOE/pyart) — the Python ARM Radar Toolkit for weather radar processing
- [**xradar**](https://github.com/openradar/xradar) — bringing weather radar data into the Xarray/Pangeo ecosystem
- The broader [**Pangeo community**](https://pangeo.io/) — building tools and practices for scalable geoscience

I also continue co-chairing the AMS Committee on Environmental Information Processing Technologies and helping organize the Earth/Ocean/Geo/Atmospheric Science track at [SciPy](https://www.scipy2024.scipy.org/).

Open-source weather infrastructure benefits everyone — operational forecasters, researchers, and the communities that depend on accurate weather information. I'm glad to be in a role where I can contribute to it from both the open-source and industry sides.

## Looking Forward

The convergence of weather model data, cloud computing, and open-source tooling is creating new possibilities for weather and climate science. At Spire, I get to work at that intersection every day, building pipelines that turn raw satellite observations into actionable data, using tools like gribberish that the whole community can benefit from.

If you're working on similar problems or interested in any of these tools, feel free to reach out. The weather data community is small and collaborative, and there's always room for more contributors.
