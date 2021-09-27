![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/DnC275/Users-CRUD-with-token-authentication)
![GitHub repo size](https://img.shields.io/github/repo-size/DnC275/Users-CRUD-with-token-authentication)
# CRUD для пользователей с токен аутентификацией

## Запуск и развертывание сервиса
### Вручную:
1. Склонить репозиторий и перейти в папку с проектом:
    ```
    git clone https://github.com/DnC275/Users-CRUD-with-token-authentication
    cd TokenUserAuthentication
    ```
2. Создать и активировать виртуальную среду:
   ```
   virtualenv venv 
   ```
   Для Windows:
   ```
   venv/Scripts/activate
   ```
   Для Linux/macOS:
   ```
   source venv/bin/activate
   ```
3. Установить зависимости:
   ```
   pip install -r requirements.txt
   ```
4. Создать миграции:
   ```
   python manage.py makemigrations token_authentication
   python manage.py migrate
   ```
5. Создать супер-пользователя:
   ```
   python manage.py createsuperuser
   ```
6. Запустить сервер:
   ```
   python manage.py runserver
   ```
После этого сервис будет доступен на localhost на порту 8000. 
Если необходимо использовать другой порт, добавьте к последней команде его номер.
Например, ```python manage.py runserver 5050```

### Через docker:
1. Склонить репозиторий и перейти в папку с проектом:
    ```
    git clone https://github.com/DnC275/Users-CRUD-with-token-authentication
    cd TokenUserAuthentication
    ```
2. Собрать и запустить docker-файл:
   ```
   docker build . 
   ```
   В конце успешной сборки появится сообщение ```Successfully built [хэш]```.
Полученный хэш необходимо скопировать и затем выполнить команду
   ```
   docker run --network host -d -p 8000:8000 [хэш]
   ```

## Использование
Для аутентификации необходимо у запроса установить заголовку Authentication значение "Token [значение токена]".
Токен пользователя выдается при регистрации и при логине. Аутентификация требуется для изменения данных пользователя, удаления пользователя, просмотра всех зарегистрированных пользователей.
Зарегистрировать нового пользователя может только superuser, либо те, кому он установил is_staff = True.
Просмотреть, изменить данные пользователя или удалить его, может либо он сам, либо пользователи с is_staff = True.
(У superuser is_staff по умолчанию True).

- ### Регистрация нового пользователя:
   
   **POST** ```/api/users/```

   Пример body запроса:
   ```
   {
      "user": {
         "email": "den@gmail.com",
         "username": "denis",
         "password": "12345678",
         "is_staff": false
      }
   }
   ```
- ### Логин пользователя:
  
   **POST** ```/api/users/login/```

   Чтобы залогиниться, достаточно только email и пароля. Пример body запроса:
   ```
   {
      "user": {
         "email": "den@gmail.com",
         "password": "12345678"
      }
   }
   ```
- ### Просмотр всех пользователей:
   
   **GET** ```/api/users/all/```. Админам также отображается id пользователей и параметр is_staff.
- ### Просмотр данных пользователя:

    **GET** ```/api/users/all/<int:id>/```
- ### Изменение данных пользователя:
  
    **PATCH**  ```/api/users/all/<int:id>/```
    
    В body запроса необходимо указать поля, которые нужно поменять. Email - обязательный параметр.
Только админы могут поменять значение параметры is_staff. Пример:
    ```
   {
      "user": {
         "email": "denis@gmail.com"
      }
   }
   ```
- ### Удаление пользователя:

    **DELETE** ```/api/users/all/<int:id>/```


