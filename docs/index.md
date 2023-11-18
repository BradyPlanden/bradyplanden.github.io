---
title: Latest Posts
timetoread: False
---

<style>
.grid-item {
  border: 2px solid #eee;
  padding: 1em;
  display: inline-block;  
  width: 18em;
  height: 20em;
  vertical-align: middle;
  margin-bottom: 0.5em;
}

.grid-item .content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
}
</style>

<div class="grid">

{% for page in navigation.recent_pages() %}
<div class="grid-item">
  <div class="content">
    <a href="{{ page.url }}">
      <figure>
        <img src="{{ page.meta.image }}" width="240" loading="lazy"/>
        <figcaption>{{page.title}}</figcaption>
      </figure>
    </a>
  </div>
</div>
{% endfor %}
</div>