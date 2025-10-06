

# # Тесты на pytest для проекта YaNews.
# #
# # В файле test_logic.py:
# # - Анонимный пользователь не может отправить комментарий.
# # - Авторизованный пользователь может отправить комментарий.
# # - Если комментарий содержит запрещённые слова, он не будет опубликован, а форма вернёт ошибку.
# # - Авторизованный пользователь может редактировать или удалять свои комментарии.
# # - Авторизованный пользователь не может редактировать или удалять чужие комментарии.
# #


# # test_logic.py

# import pytest
# from news.models import User, Comment
# # from news.services import comment_service


# # Фикстуры для тестовых данных
# @pytest.fixture
# def anonymous_user():
#     return None


# @pytest.fixture
# def authorized_user():
#     return User(id=1, username='test_user', is_authenticated=True)


# @pytest.fixture
# def another_user():
#     return User(id=2, username='another_user', is_authenticated=True)


# @pytest.fixture
# def test_comment(authorized_user):
#     return Comment(id=1, user=authorized_user, text='Хороший комментарий')


# @pytest.fixture
# def forbidden_words():
#     return ['запрет', 'блок', 'неприемл']


# # Тест 1: Анонимный пользователь не может отправить комментарий
# def test_anonymous_cant_comment(anonymous_user):
#     result = comment_service.create_comment(anonymous_user, 'Новый комментарий')
#     assert result is False


# # Тест 2: Авторизованный пользователь может отправить комментарий
# def test_authorized_can_comment(authorized_user):
#     result = comment_service.create_comment(authorized_user, 'Новый комментарий')
#     assert result is True


# # Тест 3: Проверка запрещённых слов
# def test_forbidden_words(authorized_user, forbidden_words):
#     for word in forbidden_words:
#         result = comment_service.create_comment(authorized_user, f'Текст с {word}')
#         assert result is False


# # Тест 4: Редактирование и удаление своих комментариев
# def test_edit_own_comment(authorized_user, test_comment):
#     # Редактирование
#     result_edit = comment_service.edit_comment(test_comment.id, authorized_user, 'Отредактировано')
#     assert result_edit is True

#     # Удаление
#     result_delete = comment_service.delete_comment(test_comment.id, authorized_user)
#     assert result_delete is True


# # Тест 5: Невозможность редактирования чужих комментариев
# def test_cant_edit_ чужие_comments(authorized_user, another_user, test_comment):


# # Попытка редактирования чужого комментария
# result_edit = comment_service.edit_comment(test_comment.id, another_user, 'Попытка редактирования')
# assert result_edit is False

# # Попытка удаления чужого комментария
# result_delete = comment_service.delete_comment(test_comment.id, another_user)
# assert result_delete is False




































































# # =========>>>>>>>>>>!!!!!!!!!!
# # # Задание

# # # В файле test_logic.py:
# # # + Анонимный пользователь не может отправить комментарий.
# # # - Авторизованный пользователь может отправить комментарий.
# # # - Если комментарий содержит запрещённые слова, он не будет опубликован, а форма вернёт ошибку.
# # # - Авторизованный пользователь может редактировать или удалять свои комментарии.
# # # - Авторизованный пользователь не может редактировать или удалять чужие комментарии.


# # import pytest
# # from django.urls import reverse
# # from django.contrib.auth.models import User
# # from news.models import Comment
# # from django.test import Client
# # from news.views import NewsComment

# # @pytest.fixture
# # def anonymous_client():
# #     return Client()

# # @pytest.fixture
# # def authenticated_client(db):
# #     user = User.objects.create_user(username='testuser1', password='testpass1')
# #     client = Client()
# #     client.force_login(user)
# #     return client

# # @pytest.fixture
# # def another_authenticated_client(db):
# #     user = User.objects.create_user(username='anotheruser2', password='testpass2')
# #     client = Client()
# #     client.force_login(user)
# #     return client

# # @pytest.fixture
# # def test_comment(authenticated_client):
# #     return Comment.objects.create(
# #         text='Test comment',
# #         author=authenticated_client.user
# #     )

# # class TestCommentLogic:

# #     def test_anonymous_cannot_comment(self, anonymous_client):
# #         # Попытка отправки комментария анонимным пользователем
# #         response = anonymous_client.post(NewsComment.post, {'text': 'Test'})
# #         assert response.status_code == 404

# #     def test_authenticated_can_comment(self, authenticated_client):
# #         # Успешная отправка комментария авторизованным пользователем
# #         response = authenticated_client.post(NewsComment.post, {'text': 'Test'})
# #         assert response.status_code == 302  # Успешное перенаправление
# #         assert Comment.objects.count() == 1

# # #     def test_forbidden_words(self, authenticated_client):
# # #         # Проверка на запрещенные слова
# # #         forbidden_word = 'badword'
# # #         response = authenticated_client.post(reverse('add_comment'), {'text': forbidden_word})
# # #         assert response.status_code == 200  # Форма возвращается с ошибкой
# # #         assert Comment.objects.count() == 0

# # #     def test_edit_own_comment(self, authenticated_client, test_comment):
# # #         # Редактирование собственного комментария
# # #         new_text = 'Updated comment'
# # #         response = authenticated_client.post(
# # #             reverse('edit_comment', args=[test_comment.id]),
# # #             {'text': new_text}
# # #         )
# # #         assert response.status_code == 302
# # #         test_comment.refresh_from_db()
# # #         assert test_comment.text == new_text

# # #     def test_delete_own_comment(self, authenticated_client, test_comment):
# # #         # Удаление собственного комментария
# # #         response = authenticated_client.post(reverse('delete_comment', args=[test_comment.id]))
# # #         assert response.status_code == 302
# # #         assert Comment.objects.count() == 0

# # #     def test_cannot_edit_ чужие_comments(
# # #         self, 
# # #         authenticated_client, 
# # #         another_authenticated_client, 
# # #         test_comment
# # #     ):
# # #         # Попытка редактирования чужого комментария
# # #         another_client = another_authenticated_client
# # #         response = another_client.post(
# # #             reverse('edit_comment', args=[test_comment.id]),
# # #             {'text': 'Trying to edit'}
# # #         )
# # #         assert response.status_code == 404

# # #     def test_cannot_delete_ чужие_comments(
# # #         self, 
# # #         authenticated_client, 
# # #         another_authenticated_client, 
# # #         test_comment
# # #     ):
# # #         # Попытка удаления чужого комментария
# # #         another_client = another_authenticated_client
# # #         response = another_client.post(reverse('delete_comment', args=[test_comment.id]))
# # #         assert response.status_code == 404








