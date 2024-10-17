# Awesome biomedical knowledge graphs [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of biomedical knowledge graphs and of resources for their construction.

![logo](src/logo.png)

This repository is inspired by [awesome lists](https://github.com/sindresorhus/awesome) and follows the style guide of the [awesome manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md).


## Table of Contents

- [Introduction](#introduction)
- [Survey](#survey)
- [Curation](#curation)
- [Notebooks](#notebooks)


## Introduction

The goal of this repository is to provide an overview of [knowledge graphs](https://en.wikipedia.org/wiki/Knowledge_graph) in the domain of [biomedicine](https://en.wikipedia.org/wiki/Biomedicine) and of resources for their construction. This is achieved in four complementary ways:

1. A survey presents a broad overview of academic and commercial projects that provide biomedical knowledge graphs or associated resources.
2. A curated list contains an opinionated selection of some of these projects that I find worth highlighting for various reasons.
3. A collection of notebooks delivers an in-depth inspection of a handful of projects by performing an exploratory data analysis on their knowledge graphs.
4. A Python package named "kgw" provides workflows for downloading selected biomedical knowledge graphs from different web data repositoriers, converting them into desired target formats (SQLite, SQL, CSV, JSONL, GraphML, MeTTa) and analyzing their contents (statistics, schema visualizations).

I hope this work serves you well! If you have a suggestion, notice an error, or just want to drop a message, please don't hesitate to [contact me](mailto:roberthaas@protonmail.com). Direct contributions via a [pull request](https://docs.github.com/en/pull-requests) are also highly welcome.


## Survey

A [PDF report](target/bmkg.pdf) and accompanying [website](https://robert-haas.github.io/awesome-biomedical-knowledge-graphs) present a comprehensive overview of available biomedical knowledge graphs and of resources for their construction.


## Curation

A [curated list](curation.md) presents and characterizes a carefully selected subset of the survey's entries in the style of an [awesome list](https://github.com/sindresorhus/awesome).


## Notebooks

The following Jupyter notebooks provide detailed inspections of five projects, with previews of their knowledge graph schemata:

1. [Human Aging and Longevity Dataset (HALD)](https://robert-haas.github.io/awesome-biomedical-knowledge-graphs/notebooks/hald.html)

<p align="center">
  <img src="https://github.com/robert-haas/awesome-biomedical-knowledge-graphs/blob/main/docs/notebooks/hald_schema.svg" alt="Schema" style="width: 70%;" />
</p>

2. [Oregano](https://robert-haas.github.io/awesome-biomedical-knowledge-graphs/notebooks/oregano.html)

<p align="center">
  <img src="https://github.com/robert-haas/awesome-biomedical-knowledge-graphs/blob/main/docs/notebooks/oregano_schema.svg" alt="Schema" style="width: 70%;" />
</p>

3. [Precision Medicine Knowledge Graph (PrimeKG)](https://robert-haas.github.io/awesome-biomedical-knowledge-graphs/notebooks/primekg.html)

<p align="center">
  <img src="https://github.com/robert-haas/awesome-biomedical-knowledge-graphs/blob/main/docs/notebooks/primekg_schema.svg" alt="Schema" style="width: 70%;" />
</p>

4. [Clinical Knowledge Graph (CKG)](https://robert-haas.github.io/awesome-biomedical-knowledge-graphs/notebooks/ckg.html)

<p align="center">
  <img src="https://github.com/robert-haas/awesome-biomedical-knowledge-graphs/blob/main/docs/notebooks/ckg_schema.svg" alt="Schema" style="width: 90%;" />
</p>

5. [Monarch](https://robert-haas.github.io/awesome-biomedical-knowledge-graphs/notebooks/monarch.html)

<p align="center">
  <img src="https://github.com/robert-haas/awesome-biomedical-knowledge-graphs/blob/main/docs/notebooks/monarch_schema.svg" alt="Schema" style="width: 100%;" />
</p>


## Python package

The Python 3 package [kgw](https://github.com/robert-haas/kgw) and its [documentation](https://robert-haas.github.io/kgw-docs) enable simple retrieving and conversion of several biomedical knowledge graphs. It is a clean reimplementation of functionality that was explored here previously in Jupyter notebooks. For example, instead of using a CSV file as intermediate format, a file-based SQLite database was chosen for faster and more flexible querying of the knowledge graph contents. This simplifies all downstream conversions and analyses. In future, a greater variety of knowledge graphs may be covered by simply adding an extraction function to get it from its web data repository and a transformation function to convert it into the shared SQLite representation. From there on, all existing conversion functions can be reused immediately. Contributions to the package are welcome and encouraged!
