from urllib.parse import urlparse
from django import template

register = template.Library()

@register.filter
def urlify(value):
	return urlparse(value)
