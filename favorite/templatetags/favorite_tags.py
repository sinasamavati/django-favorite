from django import template
from django.template.loader import render_to_string
from django.contrib.contenttypes.models import ContentType
from favorite.models import Favorite


register = template.Library()

@register.simple_tag(takes_context=True)
def favorite_button(context, target):
    user = context['request'].user

    # do nothing when user isn't authenticated
    if not user.is_authenticated():
        return ''

    target_model = '.'.join((target._meta.app_label, target._meta.object_name))
    target_content_type = ContentType.objects.get_for_model(target)
    target_object_id = target.id
    fav_count = Favorite.objects.filter(target_content_type=target_content_type,
                                        target_object_id=target_object_id).count()
    undo = False
    if user.favorite_set.filter(target_content_type=target_content_type,
                                target_object_id=target_object_id):
        undo = True

    return render_to_string('favorite/button.html',
                            {'target_model': target_model, 'target_object_id': target_object_id,
                             'fav_count': fav_count, 'undo': undo})
