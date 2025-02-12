<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">MonikaDesktopAI</h3>

  <p align="center">
    Моника на рабочем столе... самая продвинутая реализация
    <br />
    <a href="https://github.com/goosedev72-projects/MonikaDesktopAI/wiki"><strong>Разработчикам »</strong></a>
    <br />
    <br />
    <a href="https://github.com/goosedev72-projects/MonikaDesktopAI/wiki">Демонстрация</a>
    &middot;
    <a href="https://github.com/goosedev72-projects/MonikaDesktopAI/wiki/issues/">Сообщить о баге</a>
    &middot;
    <a href="https://github.com/goosedev72-projects/MonikaDesktopAI/wiki/issues/">Предложить функцию</a>
  </p>
</div>

## О проекте
Я видел кучу реализаций от Denis Solicen, San4ES-TV, PiMaker, т.д., но они довольно "упоротые" по этим причинам:

- нету гибкости (менять можно только диалоги)
- мало фишек (чисто разговаривает)
- нету кроссплатформенности (а значит макоюзеры и линуксоиды отпадают)
- сами себя превозносят (из-за отсутсвия альтернатив)
- модификация только при пересборке, да еще и через C# (а значит все, что не винда - отлетает)

Главная киллер-фича проекта перед всеми остальными - гибкость и модульность. Ты можешь использовать документацию, соблюдая несколько условий такие как использование MonikaDesktopAI Utils для изменения лица и вывода текста в диалоги, а также структура SubMods для поддержания красоты, похожей на меню из Monika After Story - и все! Дальше можно использовать стандартные Python библиотеки и код - от простой темы для разговора до выполнения эксплоита!

### Сделано через
* Python
* PyQt
* Pillow
* PlatformDirs


## Начало

Это пример, как запустить проект локально.

### Подготовка

Здесь перечислены вещи о том, как запустить проект.

* Зависимости
  ```sh
  pip3 install -r requirements.txt
  ```

### Запуск

1. Устанавливаем Python (это должен знать каждый)
2. Клонируем
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Ставим зависимости
   ```sh
   pip3 install -r requirements.txt
   ```
4. Запускаем
   ```js
   python3 main.py
   ```

<!-- USAGE EXAMPLES -->
## Примеры использовния Utils (aka API)

Изменения лица
```python
utils.render_face('happy')
```
Изменения текста
```python
utils.expression('пример текста')
```
Пустой текст
```python
utils.empty_expression()
```
<!-- ROADMAP -->
## Хотелки

- [x] База
- [ ] Правильный рендеринг
    - [x] Лицо
    - [ ] Слова
         - [ ] пустой блок
         - [ ] текст
- [ ] Сабмоды
    - [x] API
    - [ ] Структура саб-модов

<!-- CONTRIBUTING -->
## Сделать свой вклад

Свой вклад можно очень легко сделать - благодаря хорошей структуре кода, популярности Python и опен-сорс структуре!
### Обновление диалогов
Диалоги, поставляемые по умолчанию, входят в дополнение "Internals", которое можно отредактировать простым текстовым редактором и знаниями Python.
Функции по умолчанию, входящие в "Internals". также обновляются, как и диалоги.

### Создание саб-мода
Сначала, нужно создать такую структуру папки:
- src (необязательно называть так же, здесь структура зависит от манифеста)
  - main.py
  - script.py
  - additional.py
- manifest.txt (манифест)

Манифест:
```
категория.функция(script.py)
```
Дальше можно использовать примеры использования API и любые Python библиотеки и код (можно даже сделать 
Если вы хотите поправить внутренний функционал API или базового кода (все, что НЕ модульное), нужно открыть pull request.

1. Сделать форк
2. Создать ветку со своими фичами (`git checkout -b something`)
3. После всех изменений и git add ., сделать коммит (`git commit -m 'Добавить какую-нибудь фишку'`)
4. Сделать пуш (`git push origin something`)
5. Открыть pull request

<!-- LICENSE -->
## License

Находится под MIT лицензией. Отдельное спасибо https://github.com/Monika-After-Story/MonikaModDev за свободные спрайты.

<!-- CONTACT -->
## Связь

Гусь - https://t.me/GooseDev72
Project Link: https://github.com/goosedev72-projects/MonikaDesktopAI
