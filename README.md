# stepik_auto_tests_course

Автоматизация тестирования с помощью Selenium и Python

https://stepik.org/course/575/syllabus

Настройка

1.  Убедитесь, что у вас установлен пакет virtualenv. Если нет, то установите его командой:

  pip install virtualenv

2.  Создайте новую директорию для вашего проекта и зайдите в нее:
  mkdir myproject
  cd myproject
  
3.  Cоздайте новое виртуальное окружение в этой директории:
  virtualenv myenv
  
4.  Активируйте виртуальное окружение:

  Для Windows:
  .\myenv\Scripts\activate
  
  Для Unix или Linux:
  source myenv/bin/activate
  
5.  Установите необходимые зависимости для вашего проекта:
  pip install -r requirements.txt
  
6.  Добавьте переменные окружения в файл .env, который должен быть расположен в корневой директории вашего проекта.
  Запишите в этот файл необходимые переменные окружения в формате NAME=VALUE.
  Например:
  
  DATABASE_URL=postgres://user:password@localhost/mydatabase
  SECRET_KEY=mysecretkey
  DEBUG=True
  
7.  Используйте переменные окружения в вашем коде, например:
  
  python
  import os

  DB_URL = os.environ.get('DATABASE_URL')
  SECRET_KEY = os.environ.get('SECRET_KEY')
  DEBUG = os.environ.get('DEBUG', False)
  
Это все, что нужно сделать для создания виртуального окружения и установки переменных окружения.
