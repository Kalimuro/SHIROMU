import os
from PIL import Image
from PIL.ExifTags import TAGS


def get_image_metadata(image_path):
    try:
        img = Image.open(image_path)
        exifdata = img.getexif()

        if not exifdata:
            return {}

        metadata = {}
        for tagid in exifdata:
            tagname = TAGS.get(tagid, tagid)
            value = exifdata.get(tagid)
            metadata[tagname] = value

        return metadata

    except FileNotFoundError:
        print(f"Ошибка: изображение '{image_path}' не найдено")
        return {}
    except Exception as e:
        print(f"Ошибка при обработке изображения '{image_path}'")
        return {}


def process_images_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):  #Список расширений
            image_path = os.path.join(directory, filename)  #Полный путь к файлу
            print(f"Обработка файла: {image_path}")
            metadata = get_image_metadata(image_path)

            if metadata:
                print(f"Метаданные для изображения {filename}:")
                for tag, value in metadata.items():
                    print(f"  {tag}: {value}")
            else:
                print(f"  Метаданные не найдены для изображения {filename}")
    print("Обработка завершена")

