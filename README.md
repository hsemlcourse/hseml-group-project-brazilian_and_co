[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/kOqwghv0)
# ML Project — Прогноз стоимости заказа

**Студент:** Деговцов Кирилл Александрович

**Группа:** БИВ231


## Оглавление

1. [Описание задачи](#описание-задачи)
2. [Структура репозитория](#структура-репозитория)
3. [Запуск](#запуск)
4. [Данные](#данные)
5. [Результаты](#результаты)
7. [Отчёт](#отчёт)


## Описание задачи

Модель предсказывает ожидаемую сумму покупки, опираясь на признаки события заказа, товарной категории, временной метки и пользовательской активности

**Задача:** Регрессия

**Датасет:** eCommerce purchase history from jewelry store (https://www.kaggle.com/datasets/mkechinov/ecommerce-purchase-history-from-jewelry-store)

**Целевая метрика:** MAE, RMSE, R<sup>2</sup>


## Структура репозитория
Опишите структуру проекта, сохранив при этом верхнеуровневые папки. Можно добавить новые при необходимости.
```
.
├── data
│   ├── processed               # Очищенные и обработанные данные
│   └── raw                     # Исходные файлы
├── models                      # Сохранённые модели 
├── notebooks
│   ├── 01_eda.ipynb            # EDA
│   ├── 02_baseline.ipynb       # Baseline-модель
│   └── 03_experiments.ipynb    # Эксперименты и ablation study
├── presentation                # Презентация для защиты
├── report
│   ├── images                  # Изображения для отчёта
│   └── report.md               # Финальный отчёт
├── src
│   ├── preprocessing.py        # Предобработка данных
│   └── modeling.py             # Обучение и оценка моделей
├── tests
│   └── test.py                 # Тесты пайплайна
├── requirements.txt
├── README.md
├── Makefile
└── .pre-commit-config.yaml 
```

## Запуск

Этот блок замените способом запуска вашего сервиса.
```bash
# 1. Клонировать репозиторий
git clone https://github.com/hsemlcourse/hseml-group-project-brazilian_and_co.git
cd hseml-group-project-brazilian_and_co

# 2. Создать виртуальное окружение
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Установить зависимости и хуки
make install
make install-hooks

# 5. Проверить код вручную (линтеры)
   make lint

# 6. Запуск хуков на всех файлах
make run-hooks
```

## Данные
- `data/raw/` — исходные файлы
- `data/processed/` — предобработанные данные


## Результаты
Здесь коротко выпишите результаты.
| Модель | MAE | RMSE | R<sup>2</sup> | Примечание |
|--------|-------------|-------------|------------|------------|
| Baseline (Linear Regression) | 141.43 | 178.88 | -0.0171 | |
| Decision Tree | 102.40 | 137.91 | 0.4190 | |
| Random Forest | 100.09 | 135.10 | 0.4424 | |
| Gradient Boosting | 103.08 | 136.47 | 0.4311 | |
| Hist Gradient Boosting | 100.70 | 133.71 | 0.4539 | |
| XGBoost | 101.28 | 134.78 | 0.4451 | |
| LightGBM | 101.66 | 134.74 | 0.4454 | |
| Random Forest (Tuned) | 99.13 | 134.64 | 0.4462 | |
| Hist Gradient Boosting (Tuned) | 98.94 | 132.60 | 0.4629 | |
| Лучшая модель (Hist Gradient Boosting (Tuned)) | 98.94 | 132.60 | 0.4629 | |


## Отчёт

Финальный отчёт: [`report/report.md`](report/report.md)
