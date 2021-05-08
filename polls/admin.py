from django.contrib import admin
from .models import Question, Choice

# Register your models here.

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

# 필드셋 추가 : 수십 개의 필드가 있는 관리 폼의 경우에는 직관적인 순서
# class QuestionAdmin(admin.ModelAdmin):
#         fieldsets = [
#             ('Question',          {'fields' : ['question_text']}),
#             ('Date Information', {'fields': ['pub_date']}),
#         ]


# Choice 모델에 대한 register() 호출 제거

# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3

# class QuestionAdmin(admin.ModelAdmin):
#         fieldsets = [
#             ('Question',          {'fields' : ['question_text']}),
#             ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#         ]
#         inlines = [ChoiceInline]


# StackedInline 대신에 TabularInline을 사용하면, 관련된 객체는 좀 더 조밀하고 테이블 기반 형식으로 표
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
        fieldsets = [
            ('Question',          {'fields' : ['question_text']}),
            ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ]
        inlines = [ChoiceInline]
        list_display = ('question_text', 'pub_date', 'was_published_recently')
        list_filter = ['pub_date']
        search_fields = ['question_text']
        
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)