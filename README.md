
# Kun.uz clone

This is a clone project for the Kun.uz website, aimed at replicating its functionality and design. The project aims to provide a similar user experience to the original Kun.uz website, with the ability to browse and read news articles, view different categories, and stay updated on current events.


## Authors

- [@robiya07](https://www.github.com/robiya07)


## Features

- News Articles: Users can browse and read news articles from different regions, including various categories such as technologies, society sports, etc. Each news will have a title, publication date, and content

- Regional Filtering: The clone will include regional categorization to organize news articles based on different regions. This allows users to easily access news specific to their desired region

- Categories and Tags: The clone will include a categorization system to organize news articles into different categories for easy navigation. Articles can also be tagged with relevant keywords for improved search and filtering options

- Search Functionality: The clone will include a search feature to enable users to find specific articles based on keywords

- Template: The frontend of this clone is made very close to the real site and has many design features that mimic the original
## Screenshots
Home Page:

![Home Page](https://github.com/robiya07/kun_uz/blob/master/main/screenshots/Screenshot%20from%202023-07-04%2018-25-09.png)

![Home Page](https://github.com/robiya07/kun_uz/blob/master/main/screenshots/Screenshot%20from%202023-07-04%2018-25-38.png)


Filtering by Category:

![Filtering by Category](https://github.com/robiya07/kun_uz/blob/master/main/screenshots/Screenshot%20from%202023-07-04%2018-26-12.png)


Filtering by Region:

![Filtering by Region](https://github.com/robiya07/kun_uz/blob/master/main/screenshots/Screenshot%20from%202023-07-04%2018-26-54.png)


Search:

![Search](https://github.com/robiya07/kun_uz/blob/master/main/screenshots/Screenshot%20from%202023-07-04%2018-27-21.png)


Detail Page:

![Detail Page](https://github.com/robiya07/kun_uz/blob/master/main/screenshots/Screenshot%20from%202023-07-04%2018-27-56.png)
## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Create a virtual environment

```bash
  python3 -m venv .venv
```

Activate virtual environment

```bash
  . .venv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Migrate

```bash
  python3 manage.py makemigrations
  python3 manage.py migrate
```

Start the server

```bash
  python3 manage.py runserver
```
