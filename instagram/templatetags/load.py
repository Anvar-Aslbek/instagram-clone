from django import template

from instagramUser.models import Profile, Following
from instagram.models import Post


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

@register.inclusion_tag('latest.html')
def show_latest():
    posts = Post.objects.order_by('-created_at')[:4]
    return {'posts':posts}

@register.inclusion_tag('comment_index.html')
def show_comments():
    return {'son':1}
