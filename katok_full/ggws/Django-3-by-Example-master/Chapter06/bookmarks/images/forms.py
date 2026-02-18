import urllib
import urllib.request
from django.core.files.base import ContentFile
from django.utils.text import slugify
from django import forms
from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not match valid image extensions.')
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = f'{slugify(image.title)}.{image_url.rsplit(".", 1)[1].lower()}'

        # ============ ИСПРАВЛЕНИЕ: Добавляем нормальный User-Agent ============
        from urllib.request import Request, urlopen

        # Создаем запрос с нормальным User-Agent (как у реального браузера)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'ru,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }

        try:
            req = Request(image_url, headers=headers)
            response = urlopen(req, timeout=10)
            image_data = response.read()
            response.close()

            image.image.save(image_name, ContentFile(image_data), save=False)

        except Exception as e:
            # Если не удалось загрузить изображение - пропускаем этот шаг
            # Можно добавить логирование ошибки
            print(f'Error downloading image: {e}')

        # ======================================================================

        if commit:
            image.save()
        return image