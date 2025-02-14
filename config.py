from platformdirs import user_data_dir
import os
# Конфигурационные параметры приложения

app_name = "MonikaDesktopAI"
app_author = "GooseDev72"

# Пути к ресурсам
data_dir = user_data_dir(app_name, app_author)
assets_dir = os.path.join(os.path.dirname(__file__), "assets")
output_file = os.path.join(data_dir, "output.png")