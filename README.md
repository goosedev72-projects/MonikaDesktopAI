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
## Roadmap

- [x] Feature 1
- [x] Feature 2
- [ ] Feature 3
    - [ ] API
    - [ ] Структура саб-модов
See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/github_username/repo_name/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=github_username/repo_name" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the project_license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


