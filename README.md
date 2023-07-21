
# Automated Amazon Price Tracker

![amazon](https://github.com/Sidharth1327/Automated-Amazon-Price-Tracker/assets/91174930/27a2f0fc-5235-44af-bb2b-4c0b3bb3cb11)


## Abstract

The Automated Amazon Price Tracker is a Python project that monitors the price of a specific product on Amazon and sends email notifications when the price drops below a set threshold. The application utilizes the Beautiful Soup library for web scraping to extract the product's current price from the Amazon website. Additionally, the SMTP module facilitates automated email notifications to users whenever the price meets their desired criteria.

## Key Features

- Web scraping with Beautiful Soup to extract real-time product prices from Amazon.
- Automated email notifications when the product price drops below a specified value.
- User-friendly interface for easy setup and interaction.

## How It Works

1. The program retrieves the current price of the product from the Amazon website using web scraping techniques.
2. Users can set their desired price threshold for the product.
3. The application constantly monitors the product's price and sends an email notification if the price drops below the user-defined threshold.


## Usage

1. Configure your email settings in `config.py`.
2. Run the program by executing `python main.py`.
3. Follow the on-screen instructions to set the desired product and price threshold.
4. The program will continuously monitor the product's price and notify you via email when the price drops.

![smtpp](https://github.com/Sidharth1327/Automated-Amazon-Price-Tracker/assets/91174930/547f32a3-70bf-4915-9883-32c65f60a2db)


## Credits

- Dr. Angela Yu: Instructor of the Udemy course "100 Days of Python," who provided invaluable insights for the development of this project.


If you have any questions or suggestions,  I would love to hear your feedback!
