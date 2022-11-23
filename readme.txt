Поиск документов на cbr.ru

Программа ищет документы pdf на сайте https://www.cbr.ru.

Предусмотрена возможность запуска с разными браузерами (Сhrome, Firefox).

Для поиска элементов используется XPATH.

В файле test_search_pdf.py 2 теста:

    test_search_pdf_by_selenium - ведет поиск файлов используя selenium
    selen_result.txt - результат работы поиска
        Для атрибуты для запуска:
        --browser (Firefox or Chrome) - для выбора браузера.
        --headless (True or False) - для режима графического интерфейса. (headless=True default)
        -n (цифра - число потоков) - для работы в несколько потоков.

        Пример запуска через Firefox в 2 потока c поддержкой графического интерфейса:
            pytest -n 2 --browser Firefox --headless False test_search_pdf.py::test_search_pdf_by_selenium


    test_search_pdf_by_requests - использует модуль requests
    re_result.txt - результат работы поиска
        Пример запуска через Firefox в 2 потока:
            pytest -n 2 test_search_pdf.py::test_search_pdf_by_requests

Можно запустить оба теста одновремено с нужными параметрами.
    pytest --browser Firefox -n 2 -v --headless False test_search_pdf.py


