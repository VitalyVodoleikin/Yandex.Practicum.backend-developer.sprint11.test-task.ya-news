
# # Задание

# # В файле test_logic.py:
# # + Анонимный пользователь не может отправить комментарий.
# # - Авторизованный пользователь может отправить комментарий.
# # - Если комментарий содержит запрещённые слова, он не будет опубликован, а форма вернёт ошибку.
# # - Авторизованный пользователь может редактировать или удалять свои комментарии.
# # - Авторизованный пользователь не может редактировать или удалять чужие комментарии.


# import pytest
# from django.urls import reverse
# from django.contrib.auth.models import User
# from news.models import Comment
# from django.test import Client
# from news.views import NewsComment

# @pytest.fixture
# def anonymous_client():
#     return Client()

# @pytest.fixture
# def authenticated_client(db):
#     user = User.objects.create_user(username='testuser1', password='testpass1')
#     client = Client()
#     client.force_login(user)
#     return client

# @pytest.fixture
# def another_authenticated_client(db):
#     user = User.objects.create_user(username='anotheruser2', password='testpass2')
#     client = Client()
#     client.force_login(user)
#     return client

# @pytest.fixture
# def test_comment(authenticated_client):
#     return Comment.objects.create(
#         text='Test comment',
#         author=authenticated_client.user
#     )

# class TestCommentLogic:

#     def test_anonymous_cannot_comment(self, anonymous_client):
#         # Попытка отправки комментария анонимным пользователем
#         response = anonymous_client.post(NewsComment.post, {'text': 'Test'})
#         assert response.status_code == 404

#     def test_authenticated_can_comment(self, authenticated_client):
#         # Успешная отправка комментария авторизованным пользователем
#         response = authenticated_client.post(NewsComment.post, {'text': 'Test'})
#         assert response.status_code == 302  # Успешное перенаправление
#         assert Comment.objects.count() == 1

# #     def test_forbidden_words(self, authenticated_client):
# #         # Проверка на запрещенные слова
# #         forbidden_word = 'badword'
# #         response = authenticated_client.post(reverse('add_comment'), {'text': forbidden_word})
# #         assert response.status_code == 200  # Форма возвращается с ошибкой
# #         assert Comment.objects.count() == 0

# #     def test_edit_own_comment(self, authenticated_client, test_comment):
# #         # Редактирование собственного комментария
# #         new_text = 'Updated comment'
# #         response = authenticated_client.post(
# #             reverse('edit_comment', args=[test_comment.id]),
# #             {'text': new_text}
# #         )
# #         assert response.status_code == 302
# #         test_comment.refresh_from_db()
# #         assert test_comment.text == new_text

# #     def test_delete_own_comment(self, authenticated_client, test_comment):
# #         # Удаление собственного комментария
# #         response = authenticated_client.post(reverse('delete_comment', args=[test_comment.id]))
# #         assert response.status_code == 302
# #         assert Comment.objects.count() == 0

# #     def test_cannot_edit_ чужие_comments(
# #         self, 
# #         authenticated_client, 
# #         another_authenticated_client, 
# #         test_comment
# #     ):
# #         # Попытка редактирования чужого комментария
# #         another_client = another_authenticated_client
# #         response = another_client.post(
# #             reverse('edit_comment', args=[test_comment.id]),
# #             {'text': 'Trying to edit'}
# #         )
# #         assert response.status_code == 404

# #     def test_cannot_delete_ чужие_comments(
# #         self, 
# #         authenticated_client, 
# #         another_authenticated_client, 
# #         test_comment
# #     ):
# #         # Попытка удаления чужого комментария
# #         another_client = another_authenticated_client
# #         response = another_client.post(reverse('delete_comment', args=[test_comment.id]))
# #         assert response.status_code == 404








