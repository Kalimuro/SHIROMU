import glob
import os


def local_db_srch(z):
    k = 0
    results = []
    directory = 'localdb'

    files = glob.glob(os.path.join(directory, '*'))

    for file_path in files:
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r') as f:
                    for line in f:
                        if z in line:
                            results.append((file_path, line.strip()))
                            k += 1
            except Exception:
                print(f"Ошибка при обработке файла, напишите Широ о проблеме пожалуйста")
                continue
        else:
            print("Пожалуйста, загрузите свою базу данных в дирректорию localdb, база данных SHIROMU не доступна в "
                  "бесплатной версии")

    if k > 10:
        print('Результатов может быть слишком много. Пожалуйста, введите более точную информацию о таргете.')
    else:
        if k > 0:
            print("Найдены результаты:")
            for file_path, result in results:
                print(result)
        else:
            print("Информация не найдена.")


