# Подбор кандидатов на вакансию по типу личности
> Данный репозиторий является решением команды **ZhимоVики** на хакатоне *Цифровой прорыв 2024: сезон ИИ (Международный хакатон)*.

---
### PersonScout - scout of personal qualities
---

## Содержание

- [Задача](#Задача)
- [Сборка и запуск проекта](#Сборка-и-запуск-проекта)
- [Стек технологий](#Стек-технологий)
- [Концепция решения](#Концепция-решения)
- [Модель](#Модель)
- [Обработка данных](#Обработка-данных)
- [Точность модели](#Точность-модели)
- [Масштабируемость и дообучение](#Масштабируемость-и-дообучение)
- [О команде](#О-команде)

---

## Задача
> Создать систему подбора кандидатов работодателю по типу личности по видеовизитке

На основе датасета создать систему, которая может по видеовизитке кандидатов определять:
+ К какому из типу личностей относится кандидат
+ Предлагать работодателю подходящих кандидатов для данной специальности согласно их типу личности
+ Трансформировать результаты модели из системы OCEAN в систему MBTI (алгоритм трансформации должен опираться на официальные методы)

---

## Сборка проекта

> ### Требуется Python 3.10.12
+ ### 

### 1. Клонировать репозиторий на локальную машину
```bash
git clone git@github.com:zibestr/PersonScout.git
```

### 2. Установить и активировать виртуальное окружение
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Установить зависимости
```bash
pip3 install -r requirements.txt
```

### 4. Запустить проект
```bash
python3 main.py
```

---

## Концепция решения

![Использование](media/usage.png)

---

## Модель

---

## Стек технологий

+ [Python 3.10](https://www.python.org/)
+ [NumPy](https://numpy.org/) - для быстрых вычислений
+ [scikit-learn](https://scikit-learn.org/stable/) - для препроцессинга данных и получения метрик точности модели
+ [xgboost](https://xgboost.ai/) - для обучения и дообучения модели
+ [optuna](https://optuna.org/) - оптимизация гиперпараметров модели

---

## Обработка данных

![Важные параметры](media/features.png)

---

## Точность модели

---

## Масштабируемость и дообучение

Модель может дообучаться на основе incremental learning.

---

## Запуск и использование

Консольная утилита MYSDA работает с файлами формата .csv и имеет функционал:
+ определение оставшегося времени работы для каждого диска из поданного на вход файла
+ обучения модели на новых данных из файла .csv с нуля
+ дообучения модели на данных из файла .csv

![MYSDA](media/MYSDA.png)

---

## О команде

- [Яшин Данила](https://github.com/zibestr) (Team Lead, ML Engineer)
- [Основин Александр](https://github.com/PyAlexOs) (Full-stack Developer, Docs)
- [Егоров Леонид](https://github.com/Grander78498) (UI/UX, DevOps)
- [Корольков Александр](https://github.com/adkorolkov) (Backend, Data Engineer)
