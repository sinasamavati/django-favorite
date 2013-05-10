from django.http import HttpResponse
from django.db.models import get_model
from django.utils import simplejson
from django.contrib.contenttypes.models import ContentType
from favorite.models import Favorite


def add_or_remove(request):
    if request.is_ajax():
        user = request.user
        target_model = get_model(*request.POST['target_model'].split('.') or None)
        target_content_type = ContentType.objects.get_for_model(target_model)
        target_object_id = request.POST['target_object_id']

        # delete it if it's already a faorite
        if user.favorite_set.filter(target_content_type=target_content_type,
                                 target_object_id=target_object_id):
            user.favorite_set.get(target_content_type=target_content_type,
                                     target_object_id=target_object_id).delete()
            status = 'deleted'

        # otherwise, create it
        else:
            user.favorite_set.create(target_content_type=target_content_type,
                                     target_object_id=target_object_id)
            status = 'added'

        response = {'status': status,
                    'fav_count': Favorite.objects.filter(target_content_type=target_content_type,
                                                         target_object_id=target_object_id).count()}

        return HttpResponse(simplejson.dumps(response, ensure_ascii=False),
                            mimetype='application/json')

    return HttpResponse(status=405)
