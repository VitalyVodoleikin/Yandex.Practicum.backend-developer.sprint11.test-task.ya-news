
# Задание

# В файле test_routes.py:
# + Главная страница доступна анонимному пользователю.
# + Страница отдельной новости доступна анонимному пользователю.
# + Страницы удаления и редактирования комментария доступны автору комментария.
# + При попытке перейти на страницу редактирования или удаления комментария
# анонимный пользователь перенаправляется на страницу авторизации.
# + Авторизованный пользователь не может зайти на страницы редактирования или
# удаления чужих комментариев (возвращается ошибка 404).
# + Страницы регистрации пользователей, входа в учётную запись и выхода из неё
# доступны анонимным пользователям.



import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import Client
from news.models import Comment, News

User = get_user_model()

@pytest.mark.django_db
class TestRoutes:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            is_active=True
        )
        self.news = News.objects.create(
            title='Test News',
            text='Content of the test news'
        )
        self.comment = Comment.objects.create(
            news=self.news,
            author=self.user,
            text='Test comment'
        )

    # Тесты для анонимного пользователя
    def test_anonymous_home_page(self):
        response = self.client.get(reverse('news:home'))
        assert response.status_code == 200

    def test_anonymous_news_detail(self):
        response = self.client.get(reverse('news:detail', args=[self.news.id]))
        assert response.status_code == 200

    def test_anonymous_comment_edit_redirect(self):
        login_url = reverse('users:login')
        response = self.client.get(reverse('news:edit', args=[self.comment.id]))
        assert response.status_code == 302
        assert response.url == f'{login_url}?next={reverse("news:edit", args=[self.comment.id])}'

    def test_anonymous_comment_delete_redirect(self):
        login_url = reverse('users:login')
        response = self.client.get(reverse('news:delete', args=[self.comment.id]))
        assert response.status_code == 302
        assert response.url == f'{login_url}?next={reverse("news:delete", args=[self.comment.id])}'

    def test_anonymous_auth_pages(self):
        response_login = self.client.get(reverse('users:login'))
        response_register = self.client.get(reverse('users:signup'))
        response_logout = self.client.post(reverse('users:logout'))
        assert response_login.status_code == 200
        assert response_register.status_code == 200
        assert response_logout.status_code == 200

    # Тесты для авторизованного пользователя
    def test_authorized_comment_edit(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('news:edit', args=[self.comment.id]))
        assert response.status_code == 200

    def test_authorized_comment_delete(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('news:delete', args=[self.comment.id]))
        assert response.status_code == 200

    def test_authorized_foreign_comment_edit(self):
        other_user = User.objects.create_user(
            username='otheruser',
            password='otherpassword'
        )
        other_comment = Comment.objects.create(
            news=self.news,
            author=other_user,
            text='Other user comment'
        )
        self.client.force_login(self.user)
        response = self.client.get(reverse('news:edit', args=[other_comment.id]))
        assert response.status_code == 404

    def test_authorized_foreign_comment_delete(self):
        other_user = User.objects.create_user(
            username='otheruser',
            password='otherpassword'
        )
        other_comment = Comment.objects.create(
            news=self.news,
            author=other_user,
            text='Other user comment'
        )
        self.client.force_login(self.user)
        response = self.client.get(reverse('news:delete', args=[other_comment.id]))
        assert response.status_code == 404







# # ==========>>>>>>>>>>!!!!!!!!!!

# from http import HTTPStatus
# import pytest
# from django.urls import reverse


# # Указываем в фикстурах встроенный клиент и обращение к БД
# def test_home_availability_for_anonymous_user(client, db):
#     # Адрес страницы получаем через reverse():
#     url = reverse('news:home')
#     response = client.get(url)
#     assert response.status_code == HTTPStatus.OK 


# # ---------->
# # Внимательно читаем план тестирования: в пункте 5
# # упоминается проверка доступности для всех
# # пользователей страниц логина, логаута и регистрации.
# # Если должно быть доступно всем, значит должно быть
# # доступно и анонимному пользователю.
# # Напишем один параметризованный тест, в котором
# # объединим адреса, доступные для анонимных
# # пользователей (добавьте проверку логаута самостоятельно).

# # test_routes.py
# @pytest.mark.parametrize(
#     'name, method, expected_status',  # Имя параметра функции.
#     # Значения, которые будут передаваться в name.
#     [
#         ('news:home', 'get', HTTPStatus.OK),
#         ('users:login', 'get', HTTPStatus.OK),
#         ('users:signup', 'get', HTTPStatus.OK),
#         ('users:logout', 'post', HTTPStatus.OK)
#     ]
# )
# # Указываем имя изменяемого параметра в сигнатуре теста.
# def test_pages_availability_for_anonymous_user(client, name, method, expected_status, db):
#     """
#     Тест проверяет доступность страниц для анонимного пользователя
#     """
#     url = reverse(name)  # Получаем ссылку на нужный адрес.
#     # Используем соответствующий метод запроса
#     if method == 'get':
#         response = client.get(url)
#     elif method == 'post':
#         response = client.post(url)
    
#     assert response.status_code == expected_status
# # <----------

