from django import forms
from .models import PostCategory, Post
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    login = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль')


class PostAddModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['profile']


class PostAddForm(forms.Form):
    title = forms.CharField(label='Заголовок')
    text = forms.CharField(label='Текст',widget=forms.Textarea)
    category = forms.ModelChoiceField(label='Категория', queryset=PostCategory.objects.all())


    def clean_text(self):
        text = self.cleaned_data['text']
        words = ['дурак', 'козёл', '']
        for word in words:
            if word in text:
                raise ValidationError('в тексте есть запрещённые слова!')
        return text



class FeedbackForm(forms.Form):
    feedback = forms.CharField(label='Текст', widget=forms.Textarea)

    def clean_feedback(self):
        text = self.cleaned_data['feedback']
        words = ['дурак', 'козёл']
        for word in words:
            if word in text:
                raise ValidationError('в тексте есть запрещённые слова!')
        return text


class CommentAddForm(forms.Form):
    title = forms.CharField(label='', widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 15:
            raise ValidationError('Длина должна быть не больше 15')
        return title


class PostFilterForm(forms.Form):
    category = forms.ModelMultipleChoiceField(queryset=PostCategory.objects.all(),
                            widget=forms.CheckboxSelectMultiple,
                            label='Категория', required=False)
    order = forms.ChoiceField(choices=[('like_desc', 'много лайков'), ('date_desc', 'сначала старые'),
                            ('like_asc', 'мало лайков'), ('date_asc', 'сначала новые')],
                            label='Сортировка', required=False)









