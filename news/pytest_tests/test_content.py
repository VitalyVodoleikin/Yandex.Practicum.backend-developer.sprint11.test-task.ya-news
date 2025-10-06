
# Задание

# Тесты на pytest для проекта YaNews.

# В файле test_content.py:
# - Количество новостей на главной странице — не более 10.
# - Новости отсортированы от самой свежей к самой старой. Свежие новости в начале списка.
# - Комментарии на странице отдельной новости отсортированы в хронологическом порядке: старые в начале списка, новые — в конце.
# - Анонимному пользователю недоступна форма для отправки комментария на странице отдельной новости, а авторизованному доступна.


from http import HTTPStatus

from news.forms import CommentForm
from yanews import settings


def test_news_count(client, home_url, news_list):
    """Проверяет количество новостей на главной странице."""
    response = client.get(home_url)
    assert response.status_code == HTTPStatus.OK
    assert (
        response.context['object_list'].count()
        == settings.NEWS_COUNT_ON_HOME_PAGE
    )


def test_news_order(client, home_url, news_list):
    """Тестирует, что даты новостей отсортированы по убыванию."""
    response = client.get(home_url)
    all_news = response.context['object_list']
    dates = [news.date for news in all_news]
    assert dates == sorted(dates, reverse=True)


def test_comments_order(client, comments_list, detail_url):
    """Тестирует, что комментарии отсортированы по возрастанию."""
    response = client.get(detail_url)
    assert response.status_code == HTTPStatus.OK
    news = response.context['news']
    all_comments = news.comment_set.all()
    all_timestamps = [comment.created for comment in all_comments]
    sorted_timestamps = sorted(all_timestamps)
    assert all_timestamps == sorted_timestamps


def test_anonymous_client_has_no_form(client, news, detail_url, db):
    """Тестирует, что форма комментария не появляется у анонима."""
    response = client.get(detail_url)
    assert 'form' not in response.context


def test_authorized_user_has_form(author_client, news, detail_url):
    """Тестирует, что форма комментария появляется у пользователя."""
    response = author_client.get(detail_url)
    assert 'form' in response.context
    assert isinstance(response.context['form'], CommentForm)
