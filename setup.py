import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-rest-sms-auth",
    version="0.1.20",
    author="Andrei Koptev",
    author_email="akoptev1989@ya.ru",
    description="Django users authentication through SMS code",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='django rest auth sms registration rest-framework django-registration sms',
    url="https://github.com/a1k89/django-rest-sms-auth",
    packages=setuptools.find_packages(exclude=["demo"]),
    install_requires=['Django>=2.0',
                      'djangorestframework>=3.0',
                      'phonenumbers',
                      'django-phonenumber-field',
                      'celery>=5.0'],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
    include_package_data=True
)