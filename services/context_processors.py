from .models import homepage_box, homepage_box2, footer

def global_context(request):
    return {
        'box': homepage_box.objects.all(),
        'box2': homepage_box2.objects.all(),
        'foot': footer.objects.all(),
     
    }
