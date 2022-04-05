from django import template

from instagramUser.models import Profile, Following


register = template.Library()

@register.inclusion_tag('who_is_follow.html')
def show_follow(**df):
    profile = Profile.objects.all()
    prof = Profile.objects.get(username=df['profile'])
    follow_status = Following.objects.exclude(follower=prof)
    ls = []
    for i in profile:
        follow_status = Following.objects.filter(following=i,follower=prof).exists()
        if not follow_status and i!=prof:
            ls.append(i.id)

    return {'profile':profile, 'ls':ls}
