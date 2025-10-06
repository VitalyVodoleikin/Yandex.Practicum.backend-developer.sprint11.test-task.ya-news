

# Тесты на pytest для проекта YaNews.

# В файле test_logic.py:
# - Анонимный пользователь не может отправить комментарий.
# - Авторизованный пользователь может отправить комментарий.
# - Если комментарий содержит запрещённые слова, он не будет опубликован, а форма вернёт ошибку.
# - Авторизованный пользователь может редактировать или удалять свои комментарии.
# - Авторизованный пользователь не может редактировать или удалять чужие комментарии.

import pytest
from http import HTTPStatus

from django.urls import reverse
from news.models import Comment
from news.forms import BAD_WORDS, WARNING
from pytest_django.asserts import assertRedirects


COMMENT_FORM_DATA = {'text': 'Текст комментария'}
BAD_WORDS_DATA = {'text': f'Какой-то текст, {BAD_WORDS[0]}, еще текст'}


def test_anonymous_user_cant_create_comment(client, news, detail_url):
    """Анонимный пользователь не может отправить комментарий."""
    comments_count = Comment.objects.count()
    response = client.post(detail_url, data=COMMENT_FORM_DATA)
    assert response.status_code == HTTPStatus.FOUND
    assert Comment.objects.count() == comments_count


def test_user_can_create_comment(author, author_client, news, detail_url):
    """Авторизованный пользователь может отправить комментарий."""
    Comment.objects.all().delete()
    response = author_client.post(detail_url, data=COMMENT_FORM_DATA)
    assertRedirects(response, f'{detail_url}#comments')
    assert Comment.objects.count() == 1
    comment = Comment.objects.get()
    assert comment.text == COMMENT_FORM_DATA['text']
    assert comment.news == news
    assert comment.author == author


def test_user_cant_use_bad_words(author_client, news, detail_url):
    """Если комментарий содержит запрещённые слова, он не будет опубликован."""
    comments_count = Comment.objects.count()
    response = author_client.post(detail_url, data=BAD_WORDS_DATA)
    assert response.status_code == HTTPStatus.OK
    assert Comment.objects.count() == comments_count
    assert 'form' in response.context
    form = response.context['form']
    assert form.errors
    assert 'text' in form.errors
    assert WARNING in form.errors['text']


def test_author_can_edit_comment(author_client, comment, edit_url):
    """Авторизованный пользователь может редактировать свой комментарий."""
    response = author_client.post(edit_url, data=COMMENT_FORM_DATA)
    detail_url = reverse('news:detail', args=(comment.news.id,))
    assertRedirects(response, f'{detail_url}#comments')
    updated_comment = Comment.objects.get(pk=comment.id)
    assert updated_comment.text == COMMENT_FORM_DATA['text']
    assert updated_comment.author == comment.author
    assert updated_comment.news == comment.news


def test_author_can_delete_comment(author_client, comment, delete_url):
    """Авторизованный пользователь может удалять свой комментарий."""
    comments_count = Comment.objects.count()
    response = author_client.post(delete_url)
    detail_url = reverse('news:detail', args=(comment.news.id,))
    assertRedirects(response, f'{detail_url}#comments')
    assert Comment.objects.count() == comments_count - 1


def test_reader_cant_edit_comment(not_author_client, comment, edit_url):
    """Авторизованный пользователь не может редактировать чужой комментарий."""
    response = not_author_client.post(edit_url, data=COMMENT_FORM_DATA)
    assert response.status_code == HTTPStatus.NOT_FOUND
    updated_comment = Comment.objects.get(pk=comment.id)
    assert updated_comment.text == comment.text
    assert updated_comment.author == comment.author
    assert updated_comment.news == comment.news


def test_reader_cant_delete_comment(not_author_client, comment, delete_url):
    """Авторизованный пользователь не может удалять чужой комментарий."""
    comments_count = Comment.objects.count()
    response = not_author_client.post(delete_url)
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert Comment.objects.count() == comments_count

