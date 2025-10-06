import datetime
from time import timezone
from django.test import Client
from django.urls import reverse
from django.utils import timezone
import pytest

from news.models import Comment, News
from yanews import settings


@pytest.fixture
def author(django_user_model):
    """Создаёт пользователя-автора."""
    return django_user_model.objects.create(username='Автор')


@pytest.fixture
def not_author(django_user_model):
    """Создаёт пользователя, не-автора."""
    return django_user_model.objects.create(username='Не автор')


@pytest.fixture
def author_client(author):
    """Логинит автора и возвращает клиент."""
    client = Client()
    client.force_login(author)
    return client


@pytest.fixture
def not_author_client(not_author):
    """Логинит не-автора и возвращает клиент."""
    client = Client()
    client.force_login(not_author)
    return client


@pytest.fixture
def news(db):
    """Создаёт новость."""
    return News.objects.create(
        title='Заголовок',
        text='Текст'
    )


@pytest.fixture
def comment(news, author):
    """Создаёт комментарий к новости от автора."""
    comment = Comment.objects.create(
        news=news,
        text='Текст комментария',
        author=author,
    )
    return comment


@pytest.fixture
def news_list(db):
    """Список новостей на 1 больше NEWS_COUNT_ON_HOME_PAGE."""
    today = datetime.date.today()
    for index in range(settings.NEWS_COUNT_ON_HOME_PAGE + 1):
        News.objects.create(
            title=f'Новость {index}',
            text='Просто текст.',
            date=today - datetime.timedelta(days=index)
        )


@pytest.fixture
def comments_list(author, news):
    """Список комментариев."""
    now = timezone.now()
    for index in range(10):
        comment = Comment.objects.create(
            news=news, author=author, text=f'Tекст {index}',
        )
        comment.created = now + datetime.timedelta(days=index)
        comment.save()


@pytest.fixture
def home_url():
    """Возвращает URL главной страницы."""
    return reverse('news:home')


@pytest.fixture
def detail_url(news):
    """Возвращает URL детальной страницы новости."""
    return reverse('news:detail', args=(news.id,))


@pytest.fixture
def edit_url(comment):
    """Возвращает URL редактирования комментария."""
    return reverse('news:edit', args=(comment.id,))


@pytest.fixture
def delete_url(comment):
    """Возвращает URL удаления комментария."""
    return reverse('news:delete', args=(comment.id,))


@pytest.fixture
def login_url():
    """Возвращает URL страницы входа."""
    return reverse('users:login')


@pytest.fixture
def signup_url():
    """Возвращает URL страницы регистрации."""
    return reverse('users:signup')
