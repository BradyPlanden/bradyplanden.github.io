---
date: 2023-02-13 00:00 UK/London
categories: academic group presentation
published: true
title: PyBOP Battery Intelligence Group Presentation
image: /images/2024/pybop-background.png
description: 
---

Once a term, each member of our lab group gives a 30 minute presentation on their research progress. These presentations provide a great opportunity to cross pollinate ideas and methods within the group, as well as a great opportunity for each person to improve their presentation skills and ability to defend research decisions.

In an effort to disseminate these presentations beyond our group (more than just the obligatory preprint/article), I'm going to share them here. To start with, here is my presentation from last semester. This presentation is the first of a series of presentations on the development of PyBOP and it's applications.

These presentations will use the beamer template I've previously discussed [before](../2023/beamer.md).

<!-- vertical space -->
<br>

<!-- centered: -->
<div style="text-align:center; width: 100%; height: 100%;">

<!-- solution from: https://stackoverflow.com/a/69276900 -->
{% with pdf_file = "../../../assets/PyBOP_long_presentation.pdf" %}

{% set solid_filepdf = '<i class="fas fa-file-pdf"></i>' %}
{% set empty_filepdf = '<i class="far fa-file-pdf"></i>' %}

<object data="{{ pdf_file }}#zoom=90" type="application/pdf" style="width: 80%; height: 50vh;">
    <embed src="{{ pdf_file }}#zoom=90" type="application/pdf" style="width: 80%; height: 50vh;"/>
</object>

{% endwith %}

<br>