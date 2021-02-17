import setuptools


setuptools.setup(
    name="smsauth",
    version="0.1",
    author="Andrei Koptev",
    author_email="akoptev1989@ya.ru",
    description="Django application to auth (sign in/sign up) through sms code",
    license='MIT',
    long_description='',
    long_description_content_type="text/markdown",
    keywords='django',
    url="https://github.com/a1k89/django-rest-sms-auth",
    packages=setuptools.find_packages('smsauth'),
    install_requires=['Django >= 3.0',
                      'djangorestframework',
                      'django-phonenumber-field',
                      'celery'],
    classifiers=[
        "Framework :: Django",
        "Framework :: Django :: 3.1",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)