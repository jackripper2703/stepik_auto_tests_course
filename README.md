# stepik_auto_tests_course

Автоматизация тестирования с помощью Selenium и Python

https://stepik.org/course/575/syllabus

Настройка venv

1.  Убедитесь, что у вас установлен пакет virtualenv. Если нет, то установите его командой:

  pip install virtualenv

2.  Cоздайте новое виртуальное окружение в директории проекта:
  
  virtualenv myenv
  
3.  Активируйте виртуальное окружение:

  Для Windows:
  .\myenv\Scripts\activate
  
  Для Unix или Linux:
  source myenv/bin/activate
  
4.  Установите необходимые зависимости для вашего проекта:
  
  pip install -r requirements.txt

Так же в главное директории нужно создать файл с вашим логином и паролем от stepik, для успшеных тестов авторизации:

config.py

loggin = ""
password = ""