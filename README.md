# django-favorite

A simple reusable app for django that makes it easy to have a favorite button for any model.

## Installation

    $ pip install django-favorite

## Usage

First off, include its css/js file

```html
<link rel="stylesheet" href="{% static 'css/favorite.css' %}">

<!-- inside your javascript block -->
<script src="{% static 'js/favorite.js' %}"></script>
```

and then

```
{% load favorite_tags %}

{% for comment in post.comments %}
  {% favorite_button comment %}
{% endfor %}
```
