
# # Задание

# # Тесты на pytest для проекта YaNews.

# # В файле test_content.py:
# # - Количество новостей на главной странице — не более 10.
# # - Новости отсортированы от самой свежей к самой старой. Свежие новости в начале списка.
# # - Комментарии на странице отдельной новости отсортированы в хронологическом порядке: старые в начале списка, новые — в конце.
# # - Анонимному пользователю недоступна форма для отправки комментария на странице отдельной новости, а авторизованному доступна.


# import pytest
# from datetime import datetime
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from pages.main_page import MainPage
# from pages.news_page import NewsPage
# from pages.login_page import LoginPage

# @pytest.mark.usefixtures('setup')
# class TestContent:
    
#     def test_max_news_count(self):
#         """Проверка количества новостей на главной странице (не более 10)"""
#         main_page = MainPage(self.driver)
#         news_list = main_page.get_news_list()
#         assert len(news_list) <= 10, f"Превышено допустимое количество новостей: {len(news_list)}"

#     def test_news_sorting(self):
#         """Проверка сортировки новостей от свежей к старой"""
#         main_page = MainPage(self.driver)
#         news_dates = main_page.get_news_dates()
        
#         # Преобразуем строки дат в объекты datetime для корректного сравнения
#         datetime_dates = [datetime.strptime(date, '%d.%m.%Y') for date in news_dates]
        
#         # Проверяем, что даты идут от новой к старой
#         assert datetime_dates == sorted(datetime_dates, reverse=True)

#     def test_comments_sorting(self):
#         """Проверка сортировки комментариев в хронологическом порядке"""
#         main_page = MainPage(self.driver)
#         news_page = main_page.open_random_news()
#         comments = news_page.get_comments_dates()
        
#         # Преобразуем строки дат в объекты datetime
#         datetime_dates = [datetime.strptime(date, '%d.%m.%Y %H:%M') for date in comments]
        
#         # Проверяем, что даты идут от старой к новой
#         assert datetime_dates == sorted(datetime_dates)

#     def test_anonymous_comment_form(self):
#         """Проверка недоступности формы комментариев для анонимного пользователя"""
#         main_page = MainPage(self.driver)
#         news_page = main_page.open_random_news()
#         assert not news_page.is_comment_form_visible(), "Форма комментариев доступна для анонимного пользователя"

#     def test_authorized_comment_form(self):
#         """Проверка доступности формы комментариев для авторизованного пользователя"""
#         login_page = LoginPage(self.driver)
#         login_page.login('test_user', 'test_password')
        
#         main_page = MainPage(self.driver)
#         news_page = main_page.open_random_news()
#         assert news_page.is_comment_form_visible(), "Форма комментариев недоступна для авторизованного пользователя"

#     def test_teardown(self):
#         """Выход из аккаунта после тестов"""
#         news_page = NewsPage(self.driver)
#         news_page.logout()
