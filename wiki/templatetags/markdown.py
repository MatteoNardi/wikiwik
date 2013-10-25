import markdown2
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

# If content is not trusted, we should escape it
#from django.utils.html import escape


register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def convertTxt(value):
    return mark_safe(markdown2.markdown(force_unicode(value)))

register.filter('convertTxt', convertTxt)
