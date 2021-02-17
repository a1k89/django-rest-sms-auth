import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-sms-auth",
    version="0.1",
    author="Andrei Koptev",
    author_email="akoptev1989@ya.ru",
    description="Django users authentication through SMS code",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='django rest auth sms registration rest-framework django-registration sms',
    url="https://github.com/a1k89/django-rest-sms-auth",
    packages=setuptools.find_packages(),
    install_requires=['Django',
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