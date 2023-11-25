---
date: 2023-11-01 00:00 UK/London
categories: beamer latex presentation academic
published: true
title: Beamer Template
image: /images/2023/beamer-template-background.png
description: 
---

In an effort to move away from PowerPoint, I've been looking for an alternative presentation software. I've been using LaTeX for over ten years now and have found it to be a great tool for writing reports and papers. So, I thought I would give [Beamer](https://latex-beamer.com/) a try (and it's been great!).

I found a great starting template from the University of Oxford Maths' [template](https://www.maths.ox.ac.uk/members/it/faqs/latex/presentations). Starting from this template, I've updated it to a modern 16:9 aspect ratio and styling for my current lab, the [Battery Intelligence Lab](https://howey.eng.ox.ac.uk/).

The template is available on [GitHub](https://github.com/BradyPlanden/beamer-template), with a sample presentation below.

<!-- vertical space -->
<br>

<!-- centered: -->
<div style="text-align:center; width: 100%; height: 100%;">

<!-- solution from: https://stackoverflow.com/a/69276900 -->
{% with pdf_file = "../../../assets/beamer-template.pdf" %}

{% set solid_filepdf = '<i class="fas fa-file-pdf"></i>' %}
{% set empty_filepdf = '<i class="far fa-file-pdf"></i>' %}

<object data="{{ pdf_file }}#zoom=90" type="application/pdf" style="width: 80%; height: 50vh;">
    <embed src="{{ pdf_file }}#zoom=90" type="application/pdf" style="width: 80%; height: 50vh;"/>
</object>

{% endwith %}

<br>