# Generated by Django 5.1.3 on 2024-11-09 15:21

from django.db import migrations


class Migration(migrations.Migration):

    def insert_data(apps, schema_editor):
        vacancies = {'Психолог': [0.65, 0.2, 0.9, 0.8, 0.75],
                    'Программист': [0.4, 0.25, 0.5, 0.75, 0.6],
                    'Менеджер по продажам': [0.8, 0.35, 0.7, 0.6, 0.55],
                    'Исследователь (в области науки)': [0.5, 0.3, 0.6, 0.7, 0.85],
                    'Учитель': [0.65, 0.25, 0.8, 0.75, 0.7],
                    'Хирург': [0.45, 0.2, 0.7, 0.9, 0.5],
                    'Дизайнер': [0.7, 0.3, 0.6, 0.65, 0.9],
                    'Журналист': [0.75, 0.35, 0.7, 0.65, 0.8],
                    'Финансовый аналитик': [0.4, 0.3, 0.6, 0.7, 0.55],
                    'Архитектор': [0.6, 0.25, 0.7, 0.8, 0.85],
                    'Юрист': [0.5, 0.3, 0.65, 0.75, 0.7],
                    'Научный сотрудник': [0.4, 0.2, 0.6, 0.7, 0.9],
                    'Социальный работник': [0.65, 0.25, 0.85, 0.8, 0.75],
                    'Строитель': [0.6, 0.3, 0.65, 0.7, 0.5],
                    'Художник': [0.55, 0.4, 0.65, 0.5, 0.95],
                    'Врач общей практики': [0.7, 0.25, 0.8, 0.9, 0.6],
                    'Писатель': [0.5, 0.35, 0.7, 0.6, 0.9],
                    'Маркетолог': [0.85, 0.3, 0.7, 0.65, 0.75],
                    'Рабочий на производстве': [0.55, 0.4, 0.6, 0.7, 0.5],
                    'Специалист по информационным технологиям': [0.45, 0.3, 0.55, 0.75, 0.65],
                    'Диетолог': [0.7, 0.3, 0.75, 0.8, 0.65],
                    'Фотограф': [0.7, 0.35, 0.65, 0.6, 0.85],
                    'Веб-дизайнер': [0.6, 0.3, 0.7, 0.65, 0.8],
                    'Химик': [0.5, 0.2, 0.6, 0.7, 0.75],
                    'Социолог': [0.6, 0.25, 0.75, 0.7, 0.9],
                    'Служба поддержки': [0.8, 0.3, 0.75, 0.75, 0.6],
                    'Логист': [0.5, 0.35, 0.6, 0.7, 0.55],
                    'Биолог': [0.5, 0.3, 0.6, 0.75, 0.7],
                    'Секретарь': [0.6, 0.35, 0.75, 0.7, 0.55]}
        Vacancy = apps.get_model('video_app', 'Vacancy')

        for vacancy in vacancies:
            Vacancy.objects.create(name=vacancy, description='Описание', vector=vacancies[vacancy])


    dependencies = [
        ('video_app', '0003_vacancy_vector'),
    ]

    operations = [
        migrations.RunPython(insert_data)
    ]
