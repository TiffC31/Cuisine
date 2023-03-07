from django.template.defaultfilters import slugify

def slug_unique(chaine, model, id):
    slug = slugify(chaine)
    unique_slug = slug
    nb = 2
    f = open("debug/debug.txt", "w")
    f.write(str(model.filter(slug=unique_slug).exists()))
    f.close()
    while model.filter(slug=unique_slug).exists():
        if(model.filter(slug=unique_slug).values('id')[0]['id'] == id):
            break
        unique_slug = '{}-{}'.format(slug, nb)
        nb += 1
    return unique_slug