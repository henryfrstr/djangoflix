from django.contrib import admin
from .models import VideoAllProxy, VideoPublishProxy



class VideoAllAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'state', 'video_id', 'is_published']
    search_fields = ['title']
    list_filter = ['state', 'active']
    readonly_fields = ['id', 'is_published', 'publish_timestamp']

    class Meta:
        model = VideoAllProxy

    # def published(self, obj):
    #     return obj.active


class VideoPublishAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_id']
    search_fields = ['title']
    # list_filter = ['active']

    class Meta:
        model = VideoPublishProxy

    def get_queryset(self, request):
        return VideoPublishProxy.objects.filter(active=True)


admin.site.register(VideoAllProxy, VideoAllAdmin)
admin.site.register(VideoPublishProxy, VideoPublishAdmin)
