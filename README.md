# DepistClic

![image](https://github.com/v-dav/DepistClic/assets/115344057/45ee7555-6cd5-4065-9d27-b0cb775008e0)


DepistClic is the first decision-help tool entirely dedicated to screening for complications in patients with type 2 diabetes, designed to speed up decision-making by healthcare professionals, particularly French general practitioners.

🇫🇷 The app is in French and can be accessed at www.depistclic.fr

☕️ The full detailed story of the development can be found at the related blog post at [Medium](https://medium.com/dev-genius/from-code-to-clinic-how-i-designed-and-launched-my-first-medical-web-app-f115d86a44ac)

## 🧐 Features
- A rapid logged-out UX
- A quick no more 2 min quiz
- A real-time updated patient dashboard to see the patient's global state in one glance
- No medical patient or user data storage
- Responsive on all devices with an ergonomic and interactive UI/UX
- Latest scientific and valid information with links to sources
- Our own custom algorithm drives the application and provides a proper report page personalized to the patient

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2.5-green.svg)
![MySQL](https://img.shields.io/badge/MySQL-Latest-blue.svg)
![HTML](https://img.shields.io/badge/HTML-5-orange.svg)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow.svg)
![CSS](https://img.shields.io/badge/CSS-3-blue.svg)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-0.0.1-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Latest-blue.svg)
![gunicorn](https://img.shields.io/badge/gunicorn-21.2.0-blue.svg)
![weasyprint](https://img.shields.io/badge/weasyprint-*--blue.svg)
![Hostinger](https://img.shields.io/badge/Hostinger-Latest-brightgreen.svg)
![Railway](https://img.shields.io/badge/Railway-Latest-blue.svg)

## Dependencies

![asgiref](https://img.shields.io/badge/asgiref-3.7.2-blue.svg)
![brotli](https://img.shields.io/badge/brotli-1.1.0-blue.svg)
![cffi](https://img.shields.io/badge/cffi-1.16.0-blue.svg)
![cssselect2](https://img.shields.io/badge/cssselect2-0.7.0-blue.svg)
![dj-database-url](https://img.shields.io/badge/dj--database--url-2.1.0-blue.svg)
![django-browser-reload](https://img.shields.io/badge/django--browser--reload-1.12.0-blue.svg)
![django-tailwind](https://img.shields.io/badge/django--tailwind-3.6.0-blue.svg)
![fonttools](https://img.shields.io/badge/fonttools-4.44.0-blue.svg)
![html5lib](https://img.shields.io/badge/html5lib-1.1-blue.svg)
![install](https://img.shields.io/badge/install-1.3.5-blue.svg)
![packaging](https://img.shields.io/badge/packaging-23.2-blue.svg)
![pillow](https://img.shields.io/badge/pillow-10.1.0-blue.svg)
![pycodestyle](https://img.shields.io/badge/pycodestyle-2.11.0-blue.svg)
![pycparser](https://img.shields.io/badge/pycparser-2.21-blue.svg)
![pydyf](https://img.shields.io/badge/pydyf-0.8.0-blue.svg)
![pyphen](https://img.shields.io/badge/pyphen-0.14.0-blue.svg)
![six](https://img.shields.io/badge/six-1.16.0-blue.svg)
![sqlparse](https://img.shields.io/badge/sqlparse-0.4.4-blue.svg)
![tinycss2](https://img.shields.io/badge/tinycss2-1.2.1-blue.svg)
![typing-extensions](https://img.shields.io/badge/typing--extensions-4.8.0-blue.svg)
![tzdata](https://img.shields.io/badge/tzdata-2023.3-blue.svg)
![webencodings](https://img.shields.io/badge/webencodings-0.5.1-blue.svg)
![whitenoise](https://img.shields.io/badge/whitenoise-6.6.0-blue.svg)
![zopfli](https://img.shields.io/badge/zopfli-0.2.3-blue.svg)
![pymysql](https://img.shields.io/badge/pymysql-*--blue.svg)
![cryptography](https://img.shields.io/badge/cryptography-*--blue.svg)

🛠️ Install Dependencies
```bash
pipenv install
```

## 🧑🏻‍💻 General Usage
- Search on Google in French "depistclic". One of the first results happens to be the DepistClic App.
- Clicks the result or directly access depistclic.fr
- Click the "Start" button on the landing page
- Respond to questions or skip if you don't have the information. You can correct the previous response by browsing back.
- Access the report page after the last question or at any time by clicking on the "Report" button
- Browse screening test recommendations, get more information, explore scientific sources, and print prescriptions if needed.
- You can restart the question session at any time. All previous responses will be reinitialized.

## 💻  Localhost Usage
```bash
git clone https://github.com/v-dav/DepistClic
pipenv shell
pipenv install
service mysql start
cd Depistclic/
python3 manage.py runserver
```
⚠️ Don't forget to use your own environment variables for your database.
The database with questions and screening tests is not provided with the source code.

## 📸 Screenshots
<img width="1416" alt="Skärmavbild 2023-11-29 kl  16 12 47" src="https://github.com/v-dav/DepistClic/assets/115344057/cf01bc80-38b4-4624-a327-6881ec47f32d">
<img width="1430" alt="Skärmavbild 2023-11-29 kl  16 09 11" src="https://github.com/v-dav/DepistClic/assets/115344057/f7367f68-b3da-4702-a06a-4422a1cb0ff5">
<img width="1411" alt="Skärmavbild 2023-11-29 kl  16 09 40" src="https://github.com/v-dav/DepistClic/assets/115344057/898bf188-6cb0-4fe2-a463-4a0460e3291f">
<img width="1439" alt="Skärmavbild 2023-11-29 kl  16 09 53" src="https://github.com/v-dav/DepistClic/assets/115344057/8788c924-8d4b-4ca0-8aa8-662b1003f5cd">
<img width="1420" alt="Skärmavbild 2023-11-29 kl  16 10 21" src="https://github.com/v-dav/DepistClic/assets/115344057/68dd3a8a-e8f9-457e-bc20-cf8e9bcd9de4">





## ❤️ Support  
A simple star to this project repo is enough to keep me motivated on this project for days. If you are excited about this project or have any questions, let me know with a tweet, a comment, or a private message.

Feel free to reach out to us on:
- [Twitter](https://twitter.com/v_dav_dev)
- [Linkedin](https://www.linkedin.com/in/v-dav/)
- Mail to 6002@holbertonstudents.com


## 🙇 Authors
#### Vladimir Davidov
- LinkedIn: [v-dav](https://www.linkedin.com/in/v-dav/)
- Github: [v-dav](https://github.com/v-dav)

#### Benjamin Alazet
- LinkedIn: [Yliaze](https://www.linkedin.com/in/benjamin-alazet-830846285/)
- Github: [Yliaze](https://github.com/Yliaze)

#### Hugo Castèras
- LinkedIn: [hug0-cstrs](https://www.linkedin.com/in/hugo-cast%C3%A9ras-968a92271/)
- Github: [hug0-cstrs](https://github.com/hug0-cstrs)


![Graphic Design (1)](https://github.com/v-dav/DepistClic/assets/115344057/6e3caaca-c4d7-453e-93da-7d5df00e6496)

## ➤ Disclaimer
DepistClic is an independent decision support tool intended for healthcare professionals. It uses the latest recommendations from medical societies to propose personalized procedures for screening for complications in type 2 diabetic patients. The information from this site does not replace a doctor's decision-making and prescribing responsibility. This tool has not benefited from any academic validation and its presentation is unsuitable for the general public. Application developed in open-source without conflicts of interest.

## ➤ License
This project is not licensed and is open for personal and non-commercial use. Feel free to explore and use the code as inspiration for your own projects. If you have any questions or need further clarification, please reach out.
