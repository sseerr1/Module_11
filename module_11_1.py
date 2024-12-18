import os
from PIL import Image
from multiprocessing import Pool

# Путь к папке с изображениями
folder_path = "Images"

# Размер, до которого нужно изменить изображения
new_size = (800, 600)

# Создание папки для сохранения измененных изображений
output_folder = os.path.join(folder_path, "resized_images")
os.makedirs(output_folder, exist_ok=True)

def process_image(filename):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
        # Открытие изображения
        image_path = os.path.join(folder_path, filename)
        image = Image.open(image_path)

        # Изменение размера изображения
        resized_image = image.resize(new_size)

        # Преобразование в формат RGB (если изображение имеет альфа-канал)
        if resized_image.mode in ("RGBA", "LA") or (resized_image.mode == "P" and "transparency" in resized_image.info):
            resized_image = resized_image.convert("RGB")

        # Сохранение изображения в формате .jpg в новой папке
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")
        resized_image.save(output_path, format="JPEG")

        print(f"Изображение {filename} обработано и сохранено как {output_path}")

if __name__ == "__main__":
    # Получение списка всех файлов в папке
    files = os.listdir(folder_path)

    # Использование пула процессов для параллельной обработки изображений
    with Pool() as pool:
        pool.map(process_image, files)

    print("Все изображения обработаны.")
