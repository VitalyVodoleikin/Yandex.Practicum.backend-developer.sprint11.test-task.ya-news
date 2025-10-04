# news/tests/test_routes.py
# Импортируем класс HTTPStatus.
from http import HTTPStatus
from django.test import TestCase
# Импортируем функцию reverse().
from django.urls import reverse
import unittest


@unittest.skip("Этот тест временно отключен")
class TestRoutes(TestCase):

    def test_home_page(self):
        # Вместо прямого указания адреса 
        # получаем его при помощи функции reverse().
        url = reverse('news:home')
        response = self.client.get(url)
        # Проверяем, что код ответа равен статусу OK (он же 200).
        self.assertEqual(response.status_code, HTTPStatus.OK)

# ---------->>>>>>>>>>!!!!!!!!!!
# Экспериментальный файл news/tests/test_trial.py вам больше не понадобится;
# можете удалить его или сохранить в качестве примера, решать вам.
# Если  оставите — импортируйте в код модуль unittest и оберните тестирующие
# классы декоратором @skip(), чтобы в дальнейшем эти тесты не мешали работе.
